#!/usr/bin/env python3
"""
migrate_scenes_to_cues.py — Move inline scene tags out of chapter-N.json
into audioplay/cues/cN.yaml.

The v4 implementation tagged scenes inline on paragraphs:

    {"n": 9, "speaker": "Yahweh", "scene": "elohim-vessel", ...}

The Phase 1 cue-sheet refactor moves these out to per-chapter YAML:

    # audioplay/cues/c1.yaml
    chapter: 1
    cues:
      - paragraph: 9
        scene: elohim-vessel

Sparse-tagging semantics are preserved exactly: any paragraph that
carried a `scene` field — including empty-string end markers — gets a
cues entry; paragraphs with no field are not emitted. The empty string
remains the "explicit scene end" sentinel.

Speaker labels stay in chapter-N.json — they're editorial, not
production-only.

Idempotent: re-running on an already-migrated book is a no-op.

Usage:
    scripts/migrate_scenes_to_cues.py <book-slug>
    scripts/migrate_scenes_to_cues.py the-book-which-tells-the-truth
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def write_yaml(path: Path, chapter_n: int, cues: list[tuple[int, str]]) -> None:
    """Hand-roll the YAML so the diff against documented examples is exact.
    PyYAML would emit `scene: ''` for the empty string with single quotes;
    the docs use double quotes. Either is valid YAML but matching the docs
    keeps reviewers from second-guessing."""
    lines = [
        '# Schema 1 — per-chapter cue sheet',
        '#',
        '# Sparse: paragraphs not listed inherit the current scene.',
        '# scene: ""  ends the current run without starting a new one.',
        '# See docs.wheelofheaven.world Audio Play Cue Sheets.',
        '',
        f'chapter: {chapter_n}',
        'cues:',
    ]
    for pn, scene in cues:
        lines.append(f'  - paragraph: {pn}')
        lines.append(f'    scene: "{scene}"')
    path.write_text('\n'.join(lines) + '\n')


def migrate_book(slug: str) -> dict:
    book_dir = Path(slug)
    meta = json.loads((book_dir / '_meta.json').read_text())
    cues_dir = book_dir / 'audioplay' / 'cues'
    cues_dir.mkdir(parents=True, exist_ok=True)

    chapters_written = 0
    tags_moved = 0
    chapters_skipped = 0
    for entry in meta['chapterFiles']:
        ch_n = entry['n']
        ch_path = book_dir / entry['file']
        chapter = json.loads(ch_path.read_text())
        cues: list[tuple[int, str]] = []
        for p in chapter['paragraphs']:
            if 'scene' in p:
                cues.append((p['n'], p['scene']))
                del p['scene']
        if not cues:
            chapters_skipped += 1
            continue
        cue_path = cues_dir / f'c{ch_n}.yaml'
        write_yaml(cue_path, ch_n, cues)
        # Rewrite chapter JSON without the scene fields.
        ch_path.write_text(json.dumps(chapter, indent=2, ensure_ascii=False) + '\n')
        chapters_written += 1
        tags_moved += len(cues)
        print(f'  wrote {cue_path} ({len(cues)} tags) and stripped scene fields from {ch_path}')

    return {'chapters_written': chapters_written, 'tags_moved': tags_moved,
            'chapters_skipped': chapters_skipped}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    slug = argv[1]
    if not Path(slug).is_dir():
        print(f'error: {slug} is not a directory', file=sys.stderr)
        return 1
    stats = migrate_book(slug)
    print(f"migrated {stats['chapters_written']} chapters, "
          f"{stats['tags_moved']} scene tags moved, "
          f"{stats['chapters_skipped']} chapters had no tags")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
