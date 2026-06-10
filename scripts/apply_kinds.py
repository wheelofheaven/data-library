#!/usr/bin/env python3
"""
apply_kinds.py — Write reviewed paragraph kinds back into chapter-N.json.

Reads <book>/_kinds-proposal.json (produced by scan_kinds.py, then edited
by hand to drop false positives) and adds the `kind` field to each
listed paragraph in the corresponding chapter file.

The `kind` field is language-agnostic — it lives on the paragraph object
itself, beside `speaker` and `text`, so a single edit covers all
translations in the i18n block.

Idempotent: re-running this with the same proposal yields no diff.
Removing an entry from the proposal does NOT remove the kind already
written; pass --strip first if you want a clean slate.

Usage:
    scripts/apply_kinds.py <book-slug>
    scripts/apply_kinds.py the-book-which-tells-the-truth
    scripts/apply_kinds.py --strip the-book-which-tells-the-truth   # remove all kinds first
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_proposal(book_dir: Path) -> dict:
    p = book_dir / "_kinds-proposal.json"
    if not p.exists():
        raise FileNotFoundError(f"missing {p} — run scan_kinds.py first")
    return json.loads(p.read_text())


def strip_kinds(book_dir: Path) -> int:
    meta = json.loads((book_dir / "_meta.json").read_text())
    removed = 0
    for entry in meta["chapterFiles"]:
        path = book_dir / entry["file"]
        chapter = json.loads(path.read_text())
        dirty = False
        for p in chapter["paragraphs"]:
            if "kind" in p:
                del p["kind"]
                removed += 1
                dirty = True
        if dirty:
            path.write_text(json.dumps(chapter, indent=2, ensure_ascii=False) + "\n")
    return removed


def apply(book_dir: Path) -> tuple[int, int]:
    proposal = load_proposal(book_dir)
    meta = json.loads((book_dir / "_meta.json").read_text())

    # Group candidates by chapter.
    by_chapter: dict[int, dict[int, str]] = defaultdict(dict)
    for c in proposal["candidates"]:
        by_chapter[c["chapter"]][c["n"]] = c["kind"]

    applied = 0
    skipped = 0
    for entry in meta["chapterFiles"]:
        ch_n = entry["n"]
        if ch_n not in by_chapter:
            continue
        path = book_dir / entry["file"]
        chapter = json.loads(path.read_text())
        wants = by_chapter[ch_n]
        dirty = False
        for p in chapter["paragraphs"]:
            want_kind = wants.get(p["n"])
            if want_kind is None:
                continue
            if p.get("kind") == want_kind:
                skipped += 1
                continue
            # Insert `kind` after `speaker` for readable diffs.
            new_p = {}
            for k, v in p.items():
                new_p[k] = v
                if k == "speaker":
                    new_p["kind"] = want_kind
            if "kind" not in new_p:  # speaker missing — append
                new_p["kind"] = want_kind
            p.clear()
            p.update(new_p)
            applied += 1
            dirty = True
        if dirty:
            path.write_text(json.dumps(chapter, indent=2, ensure_ascii=False) + "\n")
    return applied, skipped


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book_slug")
    ap.add_argument("--strip", action="store_true", help="Remove all existing kinds before applying")
    args = ap.parse_args(argv[1:])

    book_dir = Path(args.book_slug)
    if not book_dir.is_dir():
        print(f"error: {book_dir} is not a directory", file=sys.stderr)
        return 1

    if args.strip:
        n = strip_kinds(book_dir)
        print(f"stripped {n} existing kind fields")

    applied, skipped = apply(book_dir)
    print(f"applied {applied} kind assignments  ({skipped} already up-to-date)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
