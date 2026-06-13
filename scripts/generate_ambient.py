#!/usr/bin/env python3
"""Generate per-chapter ambient tracks (v4) from scene tags.

For each chapter, walks the source `paragraphs[].scene` tags + the voice
`c{N}.timing.json` to figure out which scene applies during which time
range, tiles each scene's ambient loop into a single per-chapter track
of the same duration as the voice track, and writes
`c{N}.ambient.opus` alongside the voice file.

The ambient loop for each scene is generated once via the ElevenLabs
`/v1/sound-generation` endpoint (cached by sha256(prompt + duration)
under `audio/_work/_sfx/`). Ambient files are language-agnostic — the
same `elohim-vessel.<hash>.mp3` is reused across en/fr/de/etc., only
the per-chapter timing differs.

Sparse-tagging: a paragraph's `scene` value persists until a different
`scene` tag appears (or `scene: null` ends it). Paragraphs with no
preceding scene play with no ambient bed.

Setup:
    pip install pyyaml requests
    brew install ffmpeg
    export ELEVENLABS_API_KEY="sk_..."

Usage:
    python3 data-library/scripts/generate_ambient.py \\
        --slug the-book-which-tells-the-truth --lang en
    python3 data-library/scripts/generate_ambient.py \\
        --slug the-book-which-tells-the-truth --lang en --chapter 3
    python3 data-library/scripts/generate_ambient.py --slug ... --dry-run
"""

import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    print('Install PyYAML: pip install pyyaml', file=sys.stderr)
    sys.exit(1)
try:
    import requests
except ImportError:
    print('Install requests: pip install requests', file=sys.stderr)
    sys.exit(1)

LIB = Path(__file__).resolve().parent.parent
ASSETS_AUDIO = LIB.parent / 'assets.wheelofheaven.world' / 'audio'
SFX_CACHE = LIB / 'audio' / '_work' / '_sfx'

ELEVENLABS_API = 'https://api.elevenlabs.io/v1'


def load_scenes_config() -> dict:
    """Return {scene_id: {description, ambient_prompt, ambient_duration_seconds,
    gain_db, sfx_at_start?}}. Empty dict if scenes.yaml is missing."""
    path = LIB / 'audio' / 'scenes.yaml'
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return (data.get('scenes') or {})


def sfx_cache_key(prompt: str, duration: float) -> str:
    h = hashlib.sha256()
    h.update(prompt.encode('utf-8'))
    h.update(str(duration).encode('ascii'))
    return h.hexdigest()[:16]


def generate_sound(prompt: str, duration_seconds: float, api_key: str,
                   timeout: int = 120, max_retries: int = 3) -> bytes:
    """POST to ElevenLabs sound-generation, return MP3 bytes. Caches by
    (prompt, duration) — re-runs return cached bytes for free."""
    key = sfx_cache_key(prompt, duration_seconds)
    SFX_CACHE.mkdir(parents=True, exist_ok=True)
    cached = SFX_CACHE / f'{key}.mp3'
    if cached.exists():
        return cached.read_bytes()
    url = f'{ELEVENLABS_API}/sound-generation'
    headers = {
        'xi-api-key': api_key,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
    }
    body = {
        'text': prompt,
        'duration_seconds': duration_seconds,
    }
    backoff = 2.0
    for attempt in range(max_retries):
        resp = requests.post(url, headers=headers, json=body, timeout=timeout)
        if resp.status_code == 200:
            cached.write_bytes(resp.content)
            # save the source prompt next to the bytes for human inspection
            (SFX_CACHE / f'{key}.prompt.txt').write_text(
                f'prompt: {prompt}\nduration_seconds: {duration_seconds}\n'
            )
            return resp.content
        if resp.status_code == 429:
            wait = backoff * (2 ** attempt)
            print(f'    rate-limited, sleeping {wait}s …')
            time.sleep(wait)
            continue
        raise RuntimeError(f'ElevenLabs sound-generation {resp.status_code}: {resp.text[:400]}')
    raise RuntimeError('ElevenLabs sound-generation rate-limited beyond retries')


def ffprobe_duration(path: Path) -> float:
    out = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def load_cue_sheet(slug: str, chap: int) -> dict:
    """Load `{slug}/audioplay/cues/c{chap}.yaml` (Phase 1+). {} if absent.

    The cue sheet is the production-side source of truth for scene tags
    (and, in later phases, SFX + pauses). Inline `scene` fields on
    paragraphs in `chapter-N.json` are the legacy v4 location; this
    function returns the cue-sheet contents so callers can prefer them
    over the inline data.
    """
    path = LIB / slug / 'audioplay' / 'cues' / f'c{chap}.yaml'
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text()) or {}


def scene_tags(chap_source: dict, slug: str, chap: int) -> dict:
    """Return {paragraph_n: scene_str_or_empty} for every paragraph that
    carries an explicit scene tag.

    Precedence: per-paragraph cue-sheet entries (Phase 1) win over the
    legacy inline `scene` field on `chapter-N.json` paragraphs (v4). The
    fallback is per-paragraph, not per-chapter, so a half-migrated
    chapter is well-defined — but Phase 1's migration moves all tags at
    once, so in practice a chapter is either entirely cue-driven or
    entirely legacy.

    The empty string is preserved as the explicit "end the current run"
    sentinel — callers map it to `None` themselves.
    """
    tags: dict[int, str] = {}
    for p in chap_source['paragraphs']:
        if 'scene' in p:
            tags[p['n']] = p['scene']
    cue_sheet = load_cue_sheet(slug, chap)
    for cue in cue_sheet.get('cues') or []:
        if 'scene' in cue:
            tags[cue['paragraph']] = cue['scene']
    return tags


def scene_spans(chap_source: dict, timing: dict,
                slug: str = '', chap: int = 0) -> list[dict]:
    """Build a list of {scene, start, end} spans from paragraph scene tags
    and timing.

    Sparse-tagging: a paragraph's `scene` value persists until another
    paragraph carries a `scene` field (any value, including the empty
    string to explicitly end a scene). Paragraphs with no `scene` field
    inherit the current scene. Paragraphs with `scene: ""` end the
    current run without starting a new one.
    """
    tags = scene_tags(chap_source, slug, chap) if slug else {
        p['n']: p['scene'] for p in chap_source['paragraphs'] if 'scene' in p
    }
    # Walk paragraphs in n-order, building (n → effective_scene) by
    # propagating the most recent explicit tag.
    paras = sorted(chap_source['paragraphs'], key=lambda p: p['n'])
    effective = {}
    current = None
    for p in paras:
        if p['n'] in tags:
            current = tags[p['n']] or None  # "" or null → no scene
        effective[p['n']] = current

    # Walk timing in order; emit a span whenever the effective scene changes.
    spans = []
    current_scene = None
    current_start = None
    for entry in timing['paragraphs']:
        pn = entry['n']
        new_scene = effective.get(pn)
        if new_scene != current_scene:
            if current_scene is not None and current_start is not None:
                spans.append({'scene': current_scene, 'start': current_start, 'end': entry['start']})
            current_scene = new_scene
            current_start = entry['start'] if new_scene is not None else None
    if current_scene is not None and current_start is not None:
        spans.append({'scene': current_scene, 'start': current_start, 'end': timing['duration_seconds']})
    return spans


def build_chapter_ambient(spans: list[dict], scenes_cfg: dict, total_duration: float,
                          api_key: str, out_path: Path) -> dict:
    """Build c{N}.ambient.opus from a list of scene spans. Returns stats."""
    if not spans:
        return {'scenes': 0, 'wrote': False, 'reason': 'no scene tags in chapter'}

    # Ensure each unique scene has its ambient bed cached
    scene_ids = sorted({s['scene'] for s in spans})
    bed_paths = {}
    for sid in scene_ids:
        scfg = scenes_cfg.get(sid)
        if not scfg:
            print(f'  WARN scene {sid!r} not in scenes.yaml — skipping', file=sys.stderr)
            continue
        prompt = scfg['ambient_prompt']
        dur = float(scfg.get('ambient_duration_seconds', 30))
        print(f'  bed for {sid!r} ({dur:.0f}s) …')
        mp3_bytes = generate_sound(prompt, dur, api_key)
        bed_path = SFX_CACHE / f'{sfx_cache_key(prompt, dur)}.mp3'
        bed_paths[sid] = bed_path

    # Build per-span ambient files (silence outside scenes, tiled bed inside)
    tmp_dir = out_path.parent / f'.{out_path.stem}.tmp'
    tmp_dir.mkdir(parents=True, exist_ok=True)
    pieces = []
    last_end = 0.0
    crossfade_s = 0.3
    for i, span in enumerate(spans):
        sid = span['scene']
        if sid not in bed_paths:
            continue
        # Silence gap before this span
        if span['start'] > last_end:
            gap_dur = span['start'] - last_end
            gap_path = tmp_dir / f'gap_{i}.flac'
            subprocess.run(
                ['ffmpeg', '-y', '-loglevel', 'error',
                 '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo',
                 '-t', str(gap_dur),
                 '-acodec', 'flac', '-sample_fmt', 's16', str(gap_path)],
                capture_output=True, check=True,
            )
            pieces.append(gap_path)
        # Tiled bed for this span
        span_dur = span['end'] - span['start']
        bed_path = bed_paths[sid]
        gain_db = scenes_cfg[sid].get('gain_db', -18)
        bed_dur = ffprobe_duration(bed_path)
        loops_needed = int(span_dur / bed_dur) + 1
        span_path = tmp_dir / f'scene_{i}.flac'
        # stream_loop + atrim + gain
        subprocess.run(
            ['ffmpeg', '-y', '-loglevel', 'error',
             '-stream_loop', str(loops_needed),
             '-i', str(bed_path),
             '-af', f'atrim=0:{span_dur},volume={gain_db}dB,aresample=48000',
             '-ac', '2',
             '-acodec', 'flac', '-sample_fmt', 's16', str(span_path)],
            capture_output=True, check=True,
        )
        pieces.append(span_path)
        last_end = span['end']

    # Trailing silence to fill out to total_duration
    if last_end < total_duration:
        tail_dur = total_duration - last_end
        tail_path = tmp_dir / 'tail.flac'
        subprocess.run(
            ['ffmpeg', '-y', '-loglevel', 'error',
             '-f', 'lavfi', '-i', f'anullsrc=r=48000:cl=stereo',
             '-t', str(tail_dur),
             '-acodec', 'flac', str(tail_path)],
            capture_output=True, check=True,
        )
        pieces.append(tail_path)

    # Concat all pieces (FLAC stream copy, no padding issues like MP3)
    concat_list = tmp_dir / 'concat.txt'
    concat_list.write_text('\n'.join(f"file '{p.resolve()}'" for p in pieces) + '\n')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ['ffmpeg', '-y', '-loglevel', 'error',
         '-f', 'concat', '-safe', '0', '-i', str(concat_list),
         '-c:a', 'libopus', '-b:a', '48k', '-application', 'audio',
         '-ac', '2', '-vbr', 'on',
         str(out_path)],
        capture_output=True, check=True,
    )

    # Cleanup
    for p in pieces:
        p.unlink(missing_ok=True)
    concat_list.unlink(missing_ok=True)
    tmp_dir.rmdir()

    return {
        'scenes': len(scene_ids),
        'spans': len(spans),
        'wrote': True,
        'duration_seconds': total_duration,
        'size_bytes': out_path.stat().st_size,
    }


def main():
    ap = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=__doc__)
    ap.add_argument('--slug', required=True)
    ap.add_argument('--lang', required=True)
    ap.add_argument('--chapter', type=int)
    ap.add_argument('--dry-run', action='store_true',
                    help='Walk scene tags + estimate sfx-generation cost, no API calls or audio output')
    args = ap.parse_args()

    scenes_cfg = load_scenes_config()
    if not scenes_cfg:
        print('No scenes.yaml found at data-library/audio/scenes.yaml', file=sys.stderr)
        sys.exit(1)
    api_key = os.environ.get('ELEVENLABS_API_KEY')
    if not api_key and not args.dry_run:
        print('ELEVENLABS_API_KEY env var not set.', file=sys.stderr)
        sys.exit(1)

    meta = json.loads((LIB / args.slug / '_meta.json').read_text())
    chapters = [args.chapter] if args.chapter else list(range(1, meta['chapterCount'] + 1))

    print(f'Book: {args.slug} | Lang: {args.lang} | Chapters: {chapters}')
    print(f'Scenes defined: {", ".join(sorted(scenes_cfg.keys()))}')
    print()

    grand_scenes = set()
    grand_wrote = 0
    grand_skipped = 0
    for chap in chapters:
        print(f'=== Chapter {chap} ===')
        ch_source = json.loads((LIB / args.slug / f'chapter-{chap}.json').read_text())
        timing_path = ASSETS_AUDIO / args.lang / args.slug / f'c{chap}.timing.json'
        if not timing_path.exists():
            print(f'  no timing sidecar — skip (generate voice first)')
            grand_skipped += 1
            continue
        timing = json.loads(timing_path.read_text())
        spans = scene_spans(ch_source, timing, slug=args.slug, chap=chap)
        if not spans:
            print('  no scene tags in this chapter — no ambient track')
            grand_skipped += 1
            continue
        for s in spans:
            grand_scenes.add(s['scene'])
            print(f"  span {s['scene']!r}: {s['start']:.1f}s → {s['end']:.1f}s "
                  f"({s['end']-s['start']:.1f}s)")
        if args.dry_run:
            continue
        out_path = ASSETS_AUDIO / args.lang / args.slug / f'c{chap}.ambient.opus'
        stats = build_chapter_ambient(spans, scenes_cfg, timing['duration_seconds'],
                                      api_key, out_path)
        if stats.get('wrote'):
            mb = stats['size_bytes'] / (1024 * 1024)
            print(f"  wrote {out_path.relative_to(LIB.parent)}  ({mb:.2f} MB, "
                  f"{stats['spans']} spans across {stats['scenes']} scenes)")
            grand_wrote += 1
        else:
            print(f"  skipped: {stats.get('reason', 'unknown')}")
            grand_skipped += 1
        print()

    print('=' * 60)
    print(f'wrote: {grand_wrote}  skipped: {grand_skipped}')
    print(f'unique scenes: {", ".join(sorted(grand_scenes)) or "none"}')


if __name__ == '__main__':
    main()
