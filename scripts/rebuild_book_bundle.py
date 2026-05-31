#!/usr/bin/env python3
"""Rebuild the bundled book JSON and update _meta.json counts from chapter files.

After an edit to per-chapter JSON in data-library/{slug}/chapter-N.json, this
re-assembles data-library/{slug}.json and updates data-library/{slug}/_meta.json
so paragraph counts stay in sync.
"""

import json
import sys
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent  # data-library/ (this script lives in data-library/scripts/)


def rebuild(slug: str) -> None:
    book_dir = LIB / slug
    meta_path = book_dir / '_meta.json'
    bundle_path = LIB / f'{slug}.json'

    meta = json.loads(meta_path.read_text())
    chapter_count = meta['chapterCount']

    # Read each chapter file in order
    chapters_out = []
    chapter_files_out = []
    total = 0
    for n in range(1, chapter_count + 1):
        ch_path = book_dir / f'chapter-{n}.json'
        ch = json.loads(ch_path.read_text())
        para_count = len(ch['paragraphs'])
        total += para_count

        # Append to bundle (bundle uses a compact chapter shape with i18n on the chapter title)
        chapters_out.append({
            'n': ch['n'],
            'title': ch.get('title'),
            'i18n': ch.get('i18n'),
            'paragraphs': ch['paragraphs'],
            'refId': ch.get('refId'),
        })

        # Update meta's chapterFiles entry, preserving existing fields
        existing = next((e for e in meta['chapterFiles'] if e['n'] == n), None)
        if existing is None:
            chapter_files_out.append({
                'n': n,
                'file': f'chapter-{n}.json',
                'title': ch.get('title'),
                'paragraphs': para_count,
            })
        else:
            existing['paragraphs'] = para_count
            chapter_files_out.append(existing)

    meta['chapterFiles'] = chapter_files_out
    meta['paragraphCount'] = total
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    print(f'updated {meta_path} (paragraphCount={total})')

    # If a combined bundle file exists, update it too. Otherwise skip (split-files-only book).
    if bundle_path.exists():
        bundle = json.loads(bundle_path.read_text())
        bundle['chapters'] = chapters_out
        bundle['paragraphCount'] = total
        bundle_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + '\n')
        print(f'updated {bundle_path} (chapters={len(chapters_out)}, paragraphCount={total})')
    else:
        print(f'no bundle at {bundle_path} (split-files-only book) — skipping')


if __name__ == '__main__':
    slugs = sys.argv[1:] if len(sys.argv) > 1 else ['the-book-which-tells-the-truth']
    for s in slugs:
        rebuild(s)
