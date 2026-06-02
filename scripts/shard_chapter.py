#!/usr/bin/env python3
"""Split a chapter JSON into smaller paragraph-range shards.

Use when a chapter is too large to fit in a Claude Project's context
window. Each shard is a self-contained mini-chapter JSON the Claude
Project can translate independently. After all shards come back
translated, merge_shards.py reassembles them into the full chapter.

Usage:
  ./shard_chapter.py <chapter-json> [--size N] [--out-dir DIR]

Example:
  ./shard_chapter.py /Users/.../lwte/chapter-1.json --size 50 \\
      --out-dir /tmp/lwte-shards/input
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def shard_chapter(chapter_path: Path, size: int, out_dir: Path) -> list[Path]:
    data = json.loads(chapter_path.read_text(encoding='utf-8'))
    paras = data['paragraphs']
    total = len(paras)
    shards: list[Path] = []
    n_shards = (total + size - 1) // size
    base_stem = chapter_path.stem  # e.g. "chapter-1"

    out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(n_shards):
        start = i * size
        end = min(start + size, total)
        slice_paras = paras[start:end]
        first_n = slice_paras[0]['n']
        last_n = slice_paras[-1]['n']

        shard = {k: data[k] for k in ['n', 'bookSlug', 'bookCode', 'refId', 'title', 'i18n'] if k in data}
        shard['shard'] = {
            'index': i + 1,
            'of': n_shards,
            'paragraphRange': [first_n, last_n],
            'chapterTotalParagraphs': total,
        }
        shard['paragraphs'] = slice_paras

        out_path = out_dir / f'{base_stem}-shard-{i+1:02d}-of-{n_shards:02d}.json'
        out_path.write_text(
            json.dumps(shard, indent=2, ensure_ascii=False) + '\n',
            encoding='utf-8',
        )
        shards.append(out_path)
        print(f'  wrote {out_path.name}: paragraphs [{first_n}..{last_n}] ({len(slice_paras)} of {total})')
    return shards


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('chapter', type=Path, help='path to chapter-N.json')
    ap.add_argument('--size', type=int, default=50, help='paragraphs per shard (default 50)')
    ap.add_argument('--out-dir', type=Path, default=Path('/tmp/lwte-shards/input'),
                    help='output directory for shard files')
    args = ap.parse_args()

    if not args.chapter.exists():
        ap.error(f'chapter not found: {args.chapter}')
    print(f'Sharding {args.chapter.name} (size={args.size}) → {args.out_dir}')
    shards = shard_chapter(args.chapter, args.size, args.out_dir)
    print(f'Done: {len(shards)} shards.')


if __name__ == '__main__':
    main()
