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


def load_treatments_config() -> dict:
    """Per-speaker ffmpeg filter chains (v3). Optional file — returns {} if
    treatments.yaml is missing, which means every paragraph passes through
    untreated (v1/v2 behavior). Schema: {treatments: {Speaker: {filter: str}}}."""
    path = LIB / 'audio' / 'treatments.yaml'
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return (data.get('treatments') or {})


def treatment_filter(treatments_cfg: dict, speaker: str) -> str:
    """Return the ffmpeg filter chain for a speaker, or '' for no treatment."""
    spk = treatments_cfg.get(speaker) or {}
    return spk.get('filter', '') or ''


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

import base64

def call_elevenlabs(
    text: str,
    voice_id: str,
    settings: dict,
    model: str,
    api_key: str,
    timeout: int = 120,
    max_retries: int = 4,
) -> tuple[bytes, dict]:
    """POST text to ElevenLabs `with-timestamps`, return (mp3_bytes, alignment).

    alignment is {characters: [str], character_start_times_seconds: [float],
    character_end_times_seconds: [float]} — one entry per output character
    in the text the model received (so SSML tag characters are present too,
    we strip those when grouping into words downstream).

    Handles rate-limit retry.
    """
    url = f'{ELEVENLABS_API}/text-to-speech/{voice_id}/with-timestamps'
    headers = {
        'xi-api-key': api_key,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
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
            payload = resp.json()
            audio_bytes = base64.b64decode(payload['audio_base64'])
            alignment = payload.get('alignment') or {}
            return audio_bytes, alignment
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


def paragraph_alignment_path(slug: str, lang: str, chap: int, pn: int) -> Path:
    """Raw char-level alignment from ElevenLabs, before word grouping."""
    return WORK / slug / lang / f'c{chap}' / f'p{pn}.alignment.json'


def paragraph_treated_path(slug: str, lang: str, chap: int, pn: int) -> Path:
    """v3: per-speaker treatment output (ffmpeg-filtered cache copy)."""
    return WORK / slug / lang / f'c{chap}' / f'p{pn}.treated.mp3'


def treatment_cache_key(filter_str: str) -> str:
    """Short hash so a filter change invalidates the treated cache."""
    if not filter_str:
        return 'raw'
    return hashlib.sha256(filter_str.encode('utf-8')).hexdigest()[:12]


def apply_treatment(raw_path: Path, treated_path: Path, filter_str: str) -> Path:
    """Run raw_path through `filter_str` and write to treated_path, preserving
    the original input duration to within ~10 ms (so word timings stay valid).

    The duration preservation uses `apad,atrim` after the user filter chain
    to handle reverb-style filters that extend the audio with a decay tail
    — pad to 1.5x the input duration first (covers any echo tail) then trim
    back to the exact input duration. EQ-only chains see no audible change
    from the apad/atrim wrap (it's a no-op when there's no tail).

    Returns the path it wrote to. If filter_str is empty, returns raw_path
    unchanged (no treatment).
    """
    if not filter_str:
        return raw_path
    raw_duration = ffprobe_duration(raw_path)
    pad_duration = raw_duration * 1.5
    # filter chain: user filter → apad (extend with silence beyond any tail)
    #               → atrim to original duration → asetpts (rebase PTS)
    full_chain = (
        f'{filter_str},'
        f'apad=whole_dur={pad_duration},'
        f'atrim=0:{raw_duration},'
        f'asetpts=PTS-STARTPTS'
    )
    treated_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ['ffmpeg', '-y', '-loglevel', 'error',
         '-i', str(raw_path),
         '-af', full_chain,
         '-acodec', 'libmp3lame', '-b:a', '128k',
         str(treated_path)],
        capture_output=True, check=True,
    )
    return treated_path


def group_chars_to_words(alignment: dict, offset_seconds: float) -> list[dict]:
    """Collapse ElevenLabs char-level alignment into word-level timings.

    SSML tag characters (anything between `<` and `>`) are skipped so the
    word stream maps back to the displayed text. Whitespace characters
    delimit words; consecutive whitespace collapses. Each emitted word
    carries start/end times offset by `offset_seconds` so the chapter-
    level timing is monotonic across the concatenated MP3.

    Returns [{w, start, end}] where times are rounded to 3 decimals.
    """
    chars = alignment.get('characters') or []
    starts = alignment.get('character_start_times_seconds') or []
    ends = alignment.get('character_end_times_seconds') or []
    if not chars or len(chars) != len(starts) or len(chars) != len(ends):
        return []

    words: list[dict] = []
    cur_chars: list[str] = []
    cur_start = None
    cur_end = None
    in_tag = False
    for c, s, e in zip(chars, starts, ends):
        if c == '<':
            in_tag = True
            continue
        if c == '>':
            in_tag = False
            continue
        if in_tag:
            continue
        if c.isspace():
            if cur_chars:
                words.append({
                    'w': ''.join(cur_chars),
                    'start': round(cur_start + offset_seconds, 3),
                    'end': round(cur_end + offset_seconds, 3),
                })
                cur_chars = []
                cur_start = None
                cur_end = None
            continue
        cur_chars.append(c)
        if cur_start is None:
            cur_start = s
        cur_end = e
    if cur_chars:
        words.append({
            'w': ''.join(cur_chars),
            'start': round(cur_start + offset_seconds, 3),
            'end': round(cur_end + offset_seconds, 3),
        })
    return words


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


def ffmpeg_concat(parts: list[Path], out_path: Path, reencode: bool = False):
    """Concatenate MP3 files into one.

    When `reencode` is False (default), uses concat demuxer with `-c copy`
    — fast, bit-exact stream copy. Works when all parts share encoder
    metadata (e.g. v1/v2 pipeline where every paragraph comes straight
    from ElevenLabs).

    When `reencode` is True (used for v3 treatments), re-encodes through
    libmp3lame on the way out. Required because mixing libmp3lame-encoded
    treated paragraphs with raw ElevenLabs MP3s and silence inserts via
    `-c copy` preserves each file's LAME encoder delay/padding (~100 ms
    of silence at every boundary), causing the chapter's measured duration
    to drift several seconds longer than the sum of its pieces — and
    breaking word-timing sync. Re-encoding the concatenated stream
    re-stitches frames without honoring the per-file padding.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    list_file = out_path.with_suffix('.concat.txt')
    list_file.write_text('\n'.join(f"file '{p.resolve()}'" for p in parts) + '\n')
    try:
        cmd = ['ffmpeg', '-y', '-loglevel', 'error',
               '-f', 'concat', '-safe', '0',
               '-i', str(list_file)]
        if reencode:
            cmd += ['-c:a', 'libmp3lame', '-b:a', '128k']
        else:
            cmd += ['-c', 'copy']
        cmd += [str(out_path)]
        subprocess.run(cmd, capture_output=True, check=True)
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
    treatments_cfg=None,
):
    """Generate audio for one chapter. Returns stats dict.

    `treatments_cfg` is the per-speaker ffmpeg filter map from
    treatments.yaml (v3). When provided, each paragraph is post-processed
    through its speaker's filter chain before chapter concat, with the
    output cached at p{n}.treated.mp3.
    """
    sidecar = load_sidecar(slug, chap, lang)
    if not sidecar:
        return {'chars': 0, 'paragraphs': 0, 'skipped_paragraphs': 0,
                'cached_paragraphs': 0, 'new_paragraphs': 0,
                'duration_seconds': 0.0, 'estimated_cost': 0.0}
    ch_source = load_chapter(slug, chap)
    para_speakers = {str(p['n']): p.get('speaker', 'Narrator')
                     for p in ch_source['paragraphs']}
    # Per-paragraph `kind` (see docs Audio Play Cue Sheets). Absent = body.
    # Title  → longer lead-pause; the heading reads as a section break.
    # Continuation → no inter-paragraph silence; the split quotation flows
    # as a single utterance.
    para_kinds = {str(p['n']): p.get('kind', 'body')
                  for p in ch_source['paragraphs']}

    treatments_cfg = treatments_cfg or {}
    model = voices_cfg.get('model', 'eleven_multilingual_v2')
    pause_default_ms = voices_cfg.get('pause_ms_between_paragraphs', 600)
    pause_speaker_ms = voices_cfg.get('pause_ms_between_speakers', 900)
    pause_title_ms = voices_cfg.get('pause_ms_before_title', 1500)
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
        align_path = paragraph_alignment_path(slug, lang, chap, pn)

        # Cache check: key match + audio present + alignment present (v2).
        # Paragraphs cached under v1 (no alignment.json) will re-call the
        # API to pick up word timings.
        cached = False
        if meta_path.exists() and para_path.exists() and align_path.exists():
            try:
                old_meta = json.loads(meta_path.read_text())
                if old_meta.get('key') == key and old_meta.get('endpoint') == 'with-timestamps':
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
                print(f'  ch{chap} p{pn} [{speaker}] ({len(api_text)} chars) → API (ts) …')
                audio_bytes, alignment = call_elevenlabs(api_text, voice_id, settings, model, api_key)
                para_path.parent.mkdir(parents=True, exist_ok=True)
                para_path.write_bytes(audio_bytes)
                align_path.write_text(json.dumps(alignment, ensure_ascii=False))
                meta_path.write_text(json.dumps({
                    'key': key, 'speaker': speaker, 'voice_id': voice_id,
                    'chars': len(api_text), 'model': model,
                    'endpoint': 'with-timestamps',
                    'api_text': api_text,
                }, indent=2))

        # For dry-run, skip duration measurement (no audio file).
        if not dry_run and para_path.exists():
            duration = ffprobe_duration(para_path)
            # v3: per-speaker treatment (if treatments.yaml provides one).
            # Treated file is cached at p{n}.treated.mp3 keyed by the
            # filter-chain hash, so a treatments.yaml edit invalidates only
            # the affected speaker's treated cache.
            filter_str = treatment_filter(treatments_cfg, speaker)
            treated_path = paragraph_treated_path(slug, lang, chap, pn)
            treated_meta_path = treated_path.with_suffix('.meta.json')
            piece_path = para_path  # default: untreated
            if filter_str:
                tk = treatment_cache_key(filter_str)
                treated_cached = False
                if treated_path.exists() and treated_meta_path.exists():
                    try:
                        tmeta = json.loads(treated_meta_path.read_text())
                        if tmeta.get('treatment_key') == tk:
                            treated_cached = True
                    except json.JSONDecodeError:
                        pass
                if not treated_cached:
                    print(f'    treating ch{chap} p{pn} [{speaker}]: {filter_str[:60]}…')
                    apply_treatment(para_path, treated_path, filter_str)
                    treated_meta_path.write_text(json.dumps({
                        'treatment_key': tk, 'speaker': speaker,
                        'filter': filter_str,
                    }, indent=2))
                piece_path = treated_path
            # Insert silence before this paragraph (except first). Kind
            # overrides the speaker-aware default:
            #   - continuation: zero silence (TTS-concat with previous)
            #   - title:        longer lead-pause (section break)
            #   - body:         speaker change → pause_speaker_ms,
            #                   same speaker → pause_default_ms
            kind = para_kinds.get(pn_str, 'body')
            if pieces and kind != 'continuation':
                if kind == 'title':
                    pause_ms = pause_title_ms
                else:
                    pause_ms = pause_speaker_ms if speaker != prev_speaker else pause_default_ms
                silence_path = WORK / 'silence' / f'{pause_ms}ms.mp3'
                if not silence_path.exists():
                    ffmpeg_silence(silence_path, pause_ms / 1000.0)
                silence_duration = ffprobe_duration(silence_path)
                pieces.append(silence_path)
                running_t += silence_duration
            pieces.append(piece_path)
            # Load alignment (if present) and group into words at the
            # chapter offset. Silence pauses already advanced running_t.
            words = []
            if align_path.exists():
                try:
                    alignment = json.loads(align_path.read_text())
                    words = group_chars_to_words(alignment, running_t)
                except (json.JSONDecodeError, KeyError):
                    pass
            entry = {
                'n': pn, 'speaker': speaker,
                'start': round(running_t, 3),
                'end': round(running_t + duration, 3),
            }
            if kind != 'body':
                entry['kind'] = kind
            if words:
                entry['words'] = words
            paragraph_timings.append(entry)
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

    # Concatenate per-chapter MP3 + write timing sidecar to assets repo.
    # v3: when any speaker has a treatment filter active, re-encode on
    # concat (see ffmpeg_concat docstring for why `-c copy` loses sync
    # across libmp3lame-treated MP3s).
    chapter_mp3 = ASSETS_AUDIO / lang / slug / f'c{chap}.mp3'
    chapter_timing = ASSETS_AUDIO / lang / slug / f'c{chap}.timing.json'
    any_treatment = any(
        treatment_filter(treatments_cfg, s) for s in para_speakers.values()
    )
    ffmpeg_concat(pieces, chapter_mp3, reencode=any_treatment)
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
    """Update audio/{lang}/{slug}/manifest.json listing available chapters.

    Probes for sibling Opus files (`c{N}.opus`) produced by
    `transcode_audio.py` and emits a `formats[]` array per chapter when
    Opus is present. Player picks Opus first when supported and falls
    back to the MP3. `audio_url` always points at the MP3 for legacy
    players that don't know about `formats[]`.
    """
    book_dir = ASSETS_AUDIO / lang / slug
    if not book_dir.exists():
        return
    # Load source chapter JSONs once so we can pull `title` for the
    # manifest's chapter entries — the player uses it for the chapter
    # jump overlay (v4.3). Tolerate missing files (no title shown).
    chapter_titles = {}
    src_root = LIB / slug
    for src in src_root.glob('chapter-*.json'):
        try:
            n = int(src.stem.split('-')[1])
            data = json.loads(src.read_text())
            # Prefer the translated title for the requested language; fall
            # back to the source-language title only if no translation
            # exists. The chapter JSON shape is:
            #   {title: <source-lang>, i18n: {en: ..., fr: ...}}
            i18n_titles = data.get('i18n', {})
            t = ''
            if isinstance(i18n_titles, dict):
                # i18n can be a flat {lang: title} or a nested structure;
                # take whichever string matches the lang key.
                cand = i18n_titles.get(lang)
                if isinstance(cand, str):
                    t = cand
            if not t:
                t = data.get('title', '') or ''
            t = t.strip()
            if t:
                chapter_titles[n] = t
        except (ValueError, json.JSONDecodeError):
            continue

    chapters = []
    for timing_path in sorted(book_dir.glob('c*.timing.json'),
                              key=lambda p: int(p.stem.split('c')[1].split('.')[0])):
        timing = json.loads(timing_path.read_text())
        chap_n = timing['chapter']
        mp3_name = f'c{chap_n}.mp3'
        opus_name = f'c{chap_n}.opus'
        mp3_path = book_dir / mp3_name
        opus_path = book_dir / opus_name
        formats = []
        if opus_path.exists():
            formats.append({
                'type': 'audio/ogg; codecs=opus',
                'url': f'audio/{lang}/{slug}/{opus_name}',
            })
        if mp3_path.exists():
            formats.append({
                'type': 'audio/mpeg',
                'url': f'audio/{lang}/{slug}/{mp3_name}',
            })
        # audio_url is the legacy single-URL fallback for players that
        # don't read formats[]. Prefer MP3 (universal compat) when it
        # exists; fall back to Opus if it doesn't (e.g. when MP3 was
        # dropped because it exceeded Cloudflare Pages' 25 MiB per-file
        # cap — happens on very long chapters at 128k mono).
        legacy_url = f'audio/{lang}/{slug}/{mp3_name if mp3_path.exists() else opus_name}'
        # v4 — ambient track produced by generate_ambient.py from scenes.yaml
        # + paragraph scene tags. Sibling file if present; omitted from
        # manifest otherwise.
        ambient_name = f'c{chap_n}.ambient.opus'
        ambient_path = book_dir / ambient_name
        chap_entry = {
            'n': chap_n,
            'audio_url': legacy_url,
            'timing_url': f'audio/{lang}/{slug}/c{chap_n}.timing.json',
            'duration_seconds': timing['duration_seconds'],
            'paragraph_count': len(timing['paragraphs']),
            'formats': formats,
        }
        if chap_n in chapter_titles:
            chap_entry['title'] = chapter_titles[chap_n]
        if ambient_path.exists():
            chap_entry['ambient_url'] = f'audio/{lang}/{slug}/{ambient_name}'
        chapters.append(chap_entry)
    manifest = {
        'book': slug, 'lang': lang,
        'model': voices_cfg.get('model'),
        'timing_version': 2,
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
    treatments_cfg = load_treatments_config()
    api_key = os.environ.get('ELEVENLABS_API_KEY')
    if not api_key and not args.dry_run:
        print('ELEVENLABS_API_KEY env var not set. Use --dry-run to estimate cost without an API key.',
              file=sys.stderr)
        sys.exit(1)

    meta = json.loads((LIB / args.slug / '_meta.json').read_text())
    chapters = [args.chapter] if args.chapter else list(range(1, meta['chapterCount'] + 1))

    print(f'Book: {args.slug} | Lang: {args.lang} | Chapters: {chapters}')
    print(f'Model: {voices_cfg.get("model")} | Dry-run: {args.dry_run}')
    if treatments_cfg:
        treated_speakers = [s for s, cfg in treatments_cfg.items() if (cfg or {}).get('filter')]
        print(f'Treatments: {", ".join(treated_speakers) or "none"}')
    print()

    grand_chars = 0
    grand_duration = 0.0
    grand_cost = 0.0
    grand_new = 0
    grand_cached = 0

    for chap in chapters:
        print(f'=== Chapter {chap} ===')
        stats = generate_chapter(args.slug, chap, args.lang, voices_cfg, api_key,
                                 dry_run=args.dry_run, price_per_1k=args.price_per_1k,
                                 treatments_cfg=treatments_cfg)
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
