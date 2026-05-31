#!/usr/bin/env python3
"""ElevenLabs audiobook generation for library books.

Reads TTS sidecars + lexicon + voice config, calls the ElevenLabs API per
paragraph, concatenates per-chapter MP3s with timing sidecars, writes the
result into assets.wheelofheaven.world/audio/.

Idempotent: re-runs skip already-generated paragraphs. Re-runs after
lexicon/voice/text edits re-generate only the affected paragraphs.

Setup:
    pip install pyyaml requests
    brew install ffmpeg       # for concat + duration
    export ELEVENLABS_API_KEY="sk_..."

Usage:
    python3 data-library/scripts/generate_audio.py --slug the-book-which-tells-the-truth --chapter 1 --lang en
    python3 data-library/scripts/generate_audio.py --slug the-book-which-tells-the-truth --lang en  # whole book
    python3 data-library/scripts/generate_audio.py --slug ... --lang en --dry-run   # report cost, no API calls

Cost estimate:
    Each ElevenLabs API call charges per character. The script reports a
    running total of characters sent and the estimated cost based on the
    pricing tier passed via --price-per-1k (default $0.30 for creator tier).
"""

import argparse
import hashlib
import json
import os
import re
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lexicon import apply_ssml  # noqa: E402

LIB = Path(__file__).resolve().parent.parent  # data-library/
ASSETS_AUDIO = LIB.parent / 'assets.wheelofheaven.world' / 'audio'
WORK = LIB / 'audio' / '_work'

ELEVENLABS_API = 'https://api.elevenlabs.io/v1'


# ===== Config loading =====

def load_voices_config() -> dict:
    return yaml.safe_load((LIB / 'audio' / 'voices.yaml').read_text())


def resolve_voice(cfg: dict, speaker: str, lang: str) -> tuple[str, dict]:
    """Return (voice_id, settings_dict) for a (speaker, lang). Raises if unset."""
    lang_voices = (cfg.get('voices') or {}).get(lang) or {}
    spk_cfg = lang_voices.get(speaker) or {}
    voice_id = spk_cfg.get('voice_id')
    if not voice_id:
        raise ValueError(
            f'No voice_id set for ({speaker!r}, {lang!r}) in voices.yaml. '
            'Pick a voice from https://elevenlabs.io/app/voice-library and '
            'set voice_id in the (speaker, lang) entry.'
        )
    defaults = (cfg.get('defaults') or {}).get(speaker, {})
    settings = {
        'stability': spk_cfg.get('stability', defaults.get('stability', 0.5)),
        'similarity_boost': spk_cfg.get('similarity_boost', defaults.get('similarity_boost', 0.75)),
        'style': spk_cfg.get('style', defaults.get('style', 0.0)),
        'use_speaker_boost': spk_cfg.get('use_speaker_boost', defaults.get('use_speaker_boost', True)),
    }
    return voice_id, settings


# ===== TTS sidecar + source loading =====

def load_sidecar(slug: str, chap: int, lang: str) -> dict:
    path = LIB / slug / 'tts' / f'chapter-{chap}.{lang}.json'
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def load_chapter(slug: str, chap: int) -> dict:
    return json.loads((LIB / slug / f'chapter-{chap}.json').read_text())


# ===== ElevenLabs API =====

def call_elevenlabs(
    text: str,
    voice_id: str,
    settings: dict,
    model: str,
    api_key: str,
    timeout: int = 120,
    max_retries: int = 4,
) -> bytes:
    """POST text to ElevenLabs, return MP3 bytes. Handles rate-limit retry."""
    url = f'{ELEVENLABS_API}/text-to-speech/{voice_id}'
    headers = {
        'xi-api-key': api_key,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
    }
    body = {
        'text': text,
        'model_id': model,
        'voice_settings': settings,
    }
    backoff = 2.0
    for attempt in range(max_retries):
        resp = requests.post(url, headers=headers, json=body, timeout=timeout)
        if resp.status_code == 200:
            return resp.content
        if resp.status_code == 429:
            # Rate limit — exponential backoff
            wait = backoff * (2 ** attempt)
            print(f'    rate-limited, sleeping {wait}s …')
            time.sleep(wait)
            continue
        # Other errors — show body and raise
        raise RuntimeError(f'ElevenLabs API {resp.status_code}: {resp.text[:500]}')
    raise RuntimeError('ElevenLabs API rate-limited beyond retries')


# ===== Caching =====

def cache_key(text: str, voice_id: str, settings: dict, model: str) -> str:
    """Hash inputs so cache invalidates when any of text/voice/settings/model change."""
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    h.update(voice_id.encode('ascii'))
    h.update(model.encode('ascii'))
    h.update(json.dumps(settings, sort_keys=True).encode('utf-8'))
    return h.hexdigest()[:16]


def paragraph_audio_path(slug: str, lang: str, chap: int, pn: int) -> Path:
    return WORK / slug / lang / f'c{chap}' / f'p{pn}.mp3'


def paragraph_meta_path(slug: str, lang: str, chap: int, pn: int) -> Path:
    return WORK / slug / lang / f'c{chap}' / f'p{pn}.meta.json'


# ===== ffmpeg helpers =====

def ffprobe_duration(mp3_path: Path) -> float:
    """Return duration in seconds (float)."""
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(mp3_path)],
        capture_output=True, text=True, check=True,
    )
    return float(result.stdout.strip())


def ffmpeg_silence(out_path: Path, duration_seconds: float):
    """Generate a silent MP3 of given duration."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ['ffmpeg', '-y', '-f', 'lavfi', '-i',
         f'anullsrc=r=22050:cl=mono',
         '-t', str(duration_seconds),
         '-acodec', 'libmp3lame', '-b:a', '128k',
         str(out_path)],
        capture_output=True, check=True,
    )


def ffmpeg_concat(parts: list[Path], out_path: Path):
    """Concatenate MP3 files into one. Uses concat demuxer (no re-encode)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    list_file = out_path.with_suffix('.concat.txt')
    list_file.write_text('\n'.join(f"file '{p.resolve()}'" for p in parts) + '\n')
    try:
        subprocess.run(
            ['ffmpeg', '-y', '-f', 'concat', '-safe', '0',
             '-i', str(list_file),
             '-c', 'copy',
             str(out_path)],
            capture_output=True, check=True,
        )
    finally:
        list_file.unlink(missing_ok=True)


# ===== Main per-chapter generation =====

def generate_chapter(
    slug,
    chap,
    lang,
    voices_cfg,
    api_key,
    dry_run=False,
    price_per_1k=0.30,
):
    """Generate audio for one chapter. Returns stats dict."""
    sidecar = load_sidecar(slug, chap, lang)
    if not sidecar:
        return {'chars': 0, 'paragraphs': 0, 'skipped_paragraphs': 0,
                'cached_paragraphs': 0, 'new_paragraphs': 0,
                'duration_seconds': 0.0, 'estimated_cost': 0.0}
    ch_source = load_chapter(slug, chap)
    para_speakers = {str(p['n']): p.get('speaker', 'Narrator')
                     for p in ch_source['paragraphs']}

    model = voices_cfg.get('model', 'eleven_multilingual_v2')
    pause_default_ms = voices_cfg.get('pause_ms_between_paragraphs', 600)
    pause_speaker_ms = voices_cfg.get('pause_ms_between_speakers', 900)
    use_ssml = voices_cfg.get('use_ssml_phoneme', True)

    # Iterate paragraphs in order
    pieces = []                    # list of (Path, duration_s) for final concat
    paragraph_timings = []         # for the timing sidecar
    chars_total = 0
    new_paragraphs = 0
    cached_paragraphs = 0
    skipped_paragraphs = 0
    prev_speaker = None
    running_t = 0.0

    para_keys = sorted(sidecar.keys(), key=int)

    for pn_str in para_keys:
        entry = sidecar[pn_str]
        if entry.get('skip'):
            skipped_paragraphs += 1
            continue
        text = entry.get('text', '')
        if not text.strip():
            skipped_paragraphs += 1
            continue
        pn = int(pn_str)
        speaker = para_speakers.get(pn_str, 'Narrator')

        try:
            voice_id, settings = resolve_voice(voices_cfg, speaker, lang)
        except ValueError as e:
            if dry_run:
                # Allow cost estimation without voices set — use placeholders
                voice_id = '<unset>'
                settings = {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0,
                            'use_speaker_boost': True}
            else:
                print(f'  ERROR ch{chap} p{pn}: {e}', file=sys.stderr)
                return {'chars': chars_total, 'paragraphs': 0, 'skipped_paragraphs': skipped_paragraphs,
                        'cached_paragraphs': cached_paragraphs, 'new_paragraphs': new_paragraphs,
                        'duration_seconds': 0.0, 'estimated_cost': 0.0,
                        'error': str(e)}

        # Apply lexicon SSML wrapping
        api_text = apply_ssml(text, lang) if use_ssml else text
        key = cache_key(api_text, voice_id, settings, model)

        para_path = paragraph_audio_path(slug, lang, chap, pn)
        meta_path = paragraph_meta_path(slug, lang, chap, pn)

        # Cache check: if meta exists and key matches and mp3 exists, reuse
        cached = False
        if meta_path.exists() and para_path.exists():
            try:
                old_meta = json.loads(meta_path.read_text())
                if old_meta.get('key') == key:
                    cached = True
            except json.JSONDecodeError:
                pass

        chars_total += len(api_text)

        if cached:
            cached_paragraphs += 1
        else:
            new_paragraphs += 1
            if dry_run:
                # Don't call the API; estimate based on character count
                pass
            else:
                if not api_key:
                    print(f'  ERROR ch{chap} p{pn}: ELEVENLABS_API_KEY not set', file=sys.stderr)
                    return {'chars': chars_total, 'error': 'API key not set'}
                print(f'  ch{chap} p{pn} [{speaker}] ({len(api_text)} chars) → API …')
                audio_bytes = call_elevenlabs(api_text, voice_id, settings, model, api_key)
                para_path.parent.mkdir(parents=True, exist_ok=True)
                para_path.write_bytes(audio_bytes)
                meta_path.write_text(json.dumps({
                    'key': key, 'speaker': speaker, 'voice_id': voice_id,
                    'chars': len(api_text), 'model': model,
                }, indent=2))

        # For dry-run, skip duration measurement (no audio file).
        if not dry_run and para_path.exists():
            duration = ffprobe_duration(para_path)
            # Insert silence before this paragraph (except first)
            if pieces:
                pause_ms = pause_speaker_ms if speaker != prev_speaker else pause_default_ms
                silence_path = WORK / 'silence' / f'{pause_ms}ms.mp3'
                if not silence_path.exists():
                    ffmpeg_silence(silence_path, pause_ms / 1000.0)
                silence_duration = ffprobe_duration(silence_path)
                pieces.append(silence_path)
                running_t += silence_duration
            pieces.append(para_path)
            paragraph_timings.append({
                'n': pn, 'speaker': speaker,
                'start': round(running_t, 3),
                'end': round(running_t + duration, 3),
            })
            running_t += duration
            prev_speaker = speaker

    cost = (chars_total / 1000.0) * price_per_1k

    if dry_run or not pieces:
        return {
            'chars': chars_total, 'paragraphs': len(para_keys) - skipped_paragraphs,
            'skipped_paragraphs': skipped_paragraphs,
            'cached_paragraphs': cached_paragraphs, 'new_paragraphs': new_paragraphs,
            'duration_seconds': running_t, 'estimated_cost': cost,
        }

    # Concatenate per-chapter MP3 + write timing sidecar to assets repo
    chapter_mp3 = ASSETS_AUDIO / lang / slug / f'c{chap}.mp3'
    chapter_timing = ASSETS_AUDIO / lang / slug / f'c{chap}.timing.json'
    ffmpeg_concat(pieces, chapter_mp3)
    chapter_timing.parent.mkdir(parents=True, exist_ok=True)
    chapter_timing.write_text(json.dumps({
        'book': slug, 'lang': lang, 'chapter': chap,
        'duration_seconds': round(running_t, 3),
        'paragraphs': paragraph_timings,
    }, ensure_ascii=False, indent=2) + '\n')

    return {
        'chars': chars_total, 'paragraphs': len(paragraph_timings),
        'skipped_paragraphs': skipped_paragraphs,
        'cached_paragraphs': cached_paragraphs, 'new_paragraphs': new_paragraphs,
        'duration_seconds': running_t, 'estimated_cost': cost,
        'chapter_mp3': str(chapter_mp3.relative_to(LIB.parent)),
    }


def update_book_manifest(slug: str, lang: str, voices_cfg: dict):
    """Update audio/{lang}/{slug}/manifest.json listing available chapters."""
    book_dir = ASSETS_AUDIO / lang / slug
    if not book_dir.exists():
        return
    chapters = []
    for timing_path in sorted(book_dir.glob('c*.timing.json'),
                              key=lambda p: int(p.stem.split('c')[1].split('.')[0])):
        timing = json.loads(timing_path.read_text())
        chap_n = timing['chapter']
        mp3_name = f'c{chap_n}.mp3'
        chapters.append({
            'n': chap_n,
            'audio_url': f'audio/{lang}/{slug}/{mp3_name}',
            'timing_url': f'audio/{lang}/{slug}/c{chap_n}.timing.json',
            'duration_seconds': timing['duration_seconds'],
            'paragraph_count': len(timing['paragraphs']),
        })
    manifest = {
        'book': slug, 'lang': lang,
        'model': voices_cfg.get('model'),
        'chapters': chapters,
    }
    (book_dir / 'manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')


# ===== CLI =====

def main():
    ap = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=__doc__)
    ap.add_argument('--slug', required=True, help='Book slug')
    ap.add_argument('--lang', required=True, help='Language code (en, fr, …)')
    ap.add_argument('--chapter', type=int, help='Single chapter (default: all chapters in book)')
    ap.add_argument('--dry-run', action='store_true', help='Report cost without API calls')
    ap.add_argument('--price-per-1k', type=float, default=0.30,
                    help='ElevenLabs price per 1k characters (default 0.30 for creator tier)')
    args = ap.parse_args()

    voices_cfg = load_voices_config()
    api_key = os.environ.get('ELEVENLABS_API_KEY')
    if not api_key and not args.dry_run:
        print('ELEVENLABS_API_KEY env var not set. Use --dry-run to estimate cost without an API key.',
              file=sys.stderr)
        sys.exit(1)

    meta = json.loads((LIB / args.slug / '_meta.json').read_text())
    chapters = [args.chapter] if args.chapter else list(range(1, meta['chapterCount'] + 1))

    print(f'Book: {args.slug} | Lang: {args.lang} | Chapters: {chapters}')
    print(f'Model: {voices_cfg.get("model")} | Dry-run: {args.dry_run}')
    print()

    grand_chars = 0
    grand_duration = 0.0
    grand_cost = 0.0
    grand_new = 0
    grand_cached = 0

    for chap in chapters:
        print(f'=== Chapter {chap} ===')
        stats = generate_chapter(args.slug, chap, args.lang, voices_cfg, api_key,
                                 dry_run=args.dry_run, price_per_1k=args.price_per_1k)
        if 'error' in stats:
            print(f'  ABORTED: {stats["error"]}')
            sys.exit(1)
        print(f'  paragraphs: {stats["paragraphs"]} '
              f'(new: {stats["new_paragraphs"]}, cached: {stats["cached_paragraphs"]}, '
              f'skipped: {stats["skipped_paragraphs"]})')
        print(f'  chars: {stats["chars"]:,}  cost est: ${stats["estimated_cost"]:.2f}')
        if not args.dry_run:
            mins = stats["duration_seconds"] / 60
            print(f'  duration: {mins:.1f} min  → {stats.get("chapter_mp3", "n/a")}')
        grand_chars += stats['chars']
        grand_duration += stats['duration_seconds']
        grand_cost += stats['estimated_cost']
        grand_new += stats['new_paragraphs']
        grand_cached += stats['cached_paragraphs']
        print()

    if not args.dry_run and grand_new > 0:
        update_book_manifest(args.slug, args.lang, voices_cfg)

    print('=' * 60)
    print(f'TOTAL: {grand_chars:,} chars  •  est cost: ${grand_cost:.2f}  '
          f'•  duration: {grand_duration/60:.1f} min')
    print(f'       {grand_new} new paragraphs, {grand_cached} from cache')


if __name__ == '__main__':
    main()
