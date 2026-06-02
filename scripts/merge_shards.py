#!/usr/bin/env python3
"""Merge translated shards back into a full chapter JSON.

Picks up shard files that match the chapter's basename and reads
their paragraphs back into a single chapter JSON, preserving the
translation block. Validates that paragraph indices are contiguous
and that no shard is missing.

Usage:
  ./merge_shards.py <chapter-json> --shard-dir <dir> [--out <path>]
                    [--in-place]

Examples:
  # Merge translated shards back over chapter-1.json in place
  ./merge_shards.py /Users/.../lwte/chapter-1.json \\
      --shard-dir /tmp/lwte-shards/translated --in-place

  # Write merged result to a new file (default if --in-place omitted)
  ./merge_shards.py /Users/.../lwte/chapter-1.json \\
      --shard-dir /tmp/lwte-shards/translated \\
      --out /tmp/lwte-shards/chapter-1-merged.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SHARD_RE = re.compile(r'^(?P<stem>.+?)-shard-(?P<idx>\d+)-of-(?P<total>\d+)\.json$')


def find_shards(shard_dir: Path, chapter_stem: str) -> list[Path]:
    matches = []
    for path in sorted(shard_dir.iterdir()):
        if not path.is_file() or not path.name.endswith('.json'):
            continue
        m = SHARD_RE.match(path.name)
        if not m or m.group('stem') != chapter_stem:
            continue
        matches.append((int(m.group('idx')), int(m.group('total')), path))
    if not matches:
        raise SystemExit(f'no shards found in {shard_dir} matching stem {chapter_stem!r}')
    totals = {t for _, t, _ in matches}
    if len(totals) != 1:
        raise SystemExit(f'inconsistent shard totals: {totals}')
    expected_total = next(iter(totals))
    indices = sorted(i for i, _, _ in matches)
    missing = [i for i in range(1, expected_total + 1) if i not in indices]
    if missing:
        raise SystemExit(f'missing shards: {missing} (expected {expected_total} total)')
    if len(indices) != expected_total:
        raise SystemExit(f'duplicate shards present; got {len(indices)} for {expected_total}')
    return [path for _, _, path in sorted(matches)]


def merge(chapter_path: Path, shard_paths: list[Path]) -> dict:
    base = json.loads(chapter_path.read_text(encoding='utf-8'))
    merged_paras: list[dict] = []
    translation_block: dict | None = None
    i18n_titles: dict | None = None
    seen_ns: set[int] = set()

    for sp in shard_paths:
        shard = json.loads(sp.read_text(encoding='utf-8'))
        # Translator may also fill chapter-level i18n titles; prefer
        # the latest non-empty block we see across shards.
        if shard.get('i18n'):
            i18n_titles = shard['i18n']
        if shard.get('translation'):
            translation_block = shard['translation']
        for p in shard['paragraphs']:
            n = p['n']
            if n in seen_ns:
                raise SystemExit(f'duplicate paragraph n={n} in shard {sp.name}')
            seen_ns.add(n)
            merged_paras.append(p)

    merged_paras.sort(key=lambda p: p['n'])

    # Sanity check: contiguous run from 1..len.
    expected = list(range(1, len(merged_paras) + 1))
    actual = [p['n'] for p in merged_paras]
    if actual != expected:
        gaps = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        raise SystemExit(f'paragraph numbering not contiguous; gaps={gaps[:5]}, extra={extra[:5]}')

    out = {}
    for k in ['n', 'bookSlug', 'bookCode', 'refId', 'title']:
        if k in base:
            out[k] = base[k]
    out['i18n'] = i18n_titles if i18n_titles else base.get('i18n', {})
    if translation_block:
        out['translation'] = translation_block
    out['paragraphs'] = merged_paras
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('chapter', type=Path, help='path to original chapter-N.json')
    ap.add_argument('--shard-dir', type=Path, required=True,
                    help='directory containing translated shard files')
    ap.add_argument('--out', type=Path, default=None,
                    help='output path (default: chapter-{N}-merged.json beside the original)')
    ap.add_argument('--in-place', action='store_true',
                    help='overwrite the original chapter file with the merged result')
    args = ap.parse_args()

    if not args.chapter.exists():
        ap.error(f'chapter not found: {args.chapter}')
    if not args.shard_dir.is_dir():
        ap.error(f'shard dir not found: {args.shard_dir}')

    shard_paths = find_shards(args.shard_dir, args.chapter.stem)
    print(f'Merging {len(shard_paths)} shards for {args.chapter.name}')
    for sp in shard_paths:
        print(f'  - {sp.name}')
    merged = merge(args.chapter, shard_paths)

    if args.in_place:
        out_path = args.chapter
    elif args.out:
        out_path = args.out
    else:
        out_path = args.chapter.with_name(args.chapter.stem + '-merged.json')

    out_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Wrote {out_path} ({len(merged["paragraphs"])} paragraphs)')


if __name__ == '__main__':
    main()
