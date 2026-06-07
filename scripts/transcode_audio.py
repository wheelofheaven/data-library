#!/usr/bin/env python3
"""Transcode per-chapter MP3 audiobooks to Opus.

Walks `assets.wheelofheaven.world/audio/**/*.mp3` and emits a sibling
`.opus` file next to each, using libopus in voip mode at 40 kbps mono
VBR — voice sweet spot. Idempotent: skips chapters whose `.opus` is
newer than their `.mp3`.

The MP3s stay in place as a fallback for any browser without Opus
support; the bifrost prerecorded engine prefers the `.opus` source
when both are present (see manifest `formats[]` in
`generate_audio.py`'s `update_book_manifest`).

Output bitrate / mode rationale:
  - libopus `voip` application — speech-optimised, better than `audio`
    or `lowdelay` for our voice-only content.
  - 40 kbps mono VBR — comfortably above the 32 kbps speech floor,
    leaves head-room for the mild reverbs planned for v3.
  - Variable bitrate — matches Opus's design intent; silences encode
    to nearly nothing.

Word-timing alignment: re-encoding preserves the audio timeline, so
`c{N}.timing.json` paragraph/word `start`/`end` values remain valid
on the Opus track without regeneration. Verify on first chapter.

Usage:
    python3 data-library/scripts/transcode_audio.py
    python3 data-library/scripts/transcode_audio.py --slug the-book-which-tells-the-truth --lang en
    python3 data-library/scripts/transcode_audio.py --force          # ignore mtime check, re-encode all
    python3 data-library/scripts/transcode_audio.py --bitrate 48k    # override default 40k
"""

import argparse
import subprocess
import sys
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent
ASSETS_AUDIO = LIB.parent / 'assets.wheelofheaven.world' / 'audio'


def transcode_one(mp3_path: Path, opus_path: Path, bitrate: str, force: bool) -> str:
    """Encode mp3_path → opus_path. Return 'wrote' | 'skipped' | 'failed'."""
    if not force and opus_path.exists() and opus_path.stat().st_mtime >= mp3_path.stat().st_mtime:
        return 'skipped'
    opus_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        'ffmpeg', '-y', '-loglevel', 'error',
        '-i', str(mp3_path),
        '-c:a', 'libopus',
        '-b:a', bitrate,
        '-application', 'voip',
        '-ac', '1',
        '-vbr', 'on',
        str(opus_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f'  FAILED {mp3_path.name}: {result.stderr.strip()[:200]}', file=sys.stderr)
        return 'failed'
    return 'wrote'


def main():
    ap = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=__doc__)
    ap.add_argument('--slug', help='Limit to a single book slug')
    ap.add_argument('--lang', help='Limit to a single language')
    ap.add_argument('--force', action='store_true', help='Re-encode even if .opus exists and is newer')
    ap.add_argument('--bitrate', default='40k', help='libopus -b:a value (default 40k)')
    args = ap.parse_args()

    if not ASSETS_AUDIO.exists():
        print(f'No audio directory at {ASSETS_AUDIO}', file=sys.stderr)
        sys.exit(1)

    # Build the search root based on filters
    if args.lang and args.slug:
        roots = [ASSETS_AUDIO / args.lang / args.slug]
    elif args.lang:
        roots = [ASSETS_AUDIO / args.lang]
    else:
        roots = [ASSETS_AUDIO]

    total = {'wrote': 0, 'skipped': 0, 'failed': 0}
    sample_sizes = []
    for root in roots:
        if not root.exists():
            print(f'  (no audio at {root})')
            continue
        mp3s = sorted(root.rglob('c*.mp3'))
        if args.slug and not args.lang:
            mp3s = [p for p in mp3s if args.slug in p.parts]
        for mp3 in mp3s:
            opus = mp3.with_suffix('.opus')
            outcome = transcode_one(mp3, opus, args.bitrate, args.force)
            total[outcome] += 1
            if outcome == 'wrote':
                mp3_mb = mp3.stat().st_size / (1024 * 1024)
                opus_mb = opus.stat().st_size / (1024 * 1024)
                ratio = (1 - opus_mb / mp3_mb) * 100 if mp3_mb else 0
                rel = mp3.relative_to(ASSETS_AUDIO)
                print(f'  {rel} → .opus  ({mp3_mb:.1f} MB → {opus_mb:.1f} MB, -{ratio:.0f}%)')
                sample_sizes.append((mp3_mb, opus_mb))
            elif outcome == 'skipped':
                rel = mp3.relative_to(ASSETS_AUDIO)
                print(f'  {rel} (cached)')

    print()
    print('=' * 60)
    print(f'wrote: {total["wrote"]}  cached: {total["skipped"]}  failed: {total["failed"]}')
    if sample_sizes:
        mp3_total = sum(m for m, _ in sample_sizes)
        opus_total = sum(o for _, o in sample_sizes)
        saved = (1 - opus_total / mp3_total) * 100
        print(f'this run: {mp3_total:.1f} MB MP3  →  {opus_total:.1f} MB Opus  (-{saved:.0f}%)')


if __name__ == '__main__':
    main()
