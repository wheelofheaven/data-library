#!/usr/bin/env python3
"""Generate TTS-ready sidecar files and an optional side-by-side review.

For each book (or specified book), walk every chapter × language, normalize each
paragraph via normalize_tts.normalize, and write a sidecar:

    data-library/{slug}/tts/chapter-N.{lang}.json

Sidecar format:
{
  "1": {"text": "..."},
  "2": {"text": "...", "skip": true, "reason": "address-line"},
  ...
}

Empty translations produce empty sidecars (just `{}`) and are not written.

Usage:
    python3 data-library/scripts/dump_tts_text.py                    # all books, all langs
    python3 data-library/scripts/dump_tts_text.py --slug the-book-which-tells-the-truth
    python3 data-library/scripts/dump_tts_text.py --slug ... --chapter 1 --lang fr
    python3 data-library/scripts/dump_tts_text.py --review --slug ... --chapter 1 --lang fr
        # also prints a side-by-side review of source vs normalized
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_tts import normalize, should_skip, skip_reason  # noqa: E402

LIB = Path(__file__).resolve().parent.parent  # data-library/

LANGS = ['fr', 'en', 'de', 'es', 'ru', 'ja', 'ko', 'zh', 'zh-Hant']


def get_source_text(p: dict, lang: str) -> str:
    """Return the source text for the given language ('' if missing)."""
    if lang == 'fr':
        return p.get('text', '')
    return p.get('i18n', {}).get(lang, '')


def process_chapter(book: str, chap: int, lang: str, review: bool = False) -> dict:
    """Build the sidecar dict for one (book, chap, lang). Returns the dict."""
    ch_path = LIB / book / f'chapter-{chap}.json'
    if not ch_path.exists():
        # Some books have _meta.json chapterCount that exceeds actual chapter files
        # (in-progress translations etc). Skip silently.
        return {'sidecar': {}, 'changes': 0, 'skipped': 0, 'diffs': []}
    ch = json.loads(ch_path.read_text())

    out = {}
    changes = 0
    skipped = 0
    diffs = []  # for review mode

    for p in ch['paragraphs']:
        pn = p['n']
        source = get_source_text(p, lang)
        if not source:
            # Skip empty translations
            continue
        skip = should_skip(book, chap, pn)
        if skip:
            out[str(pn)] = {'text': '', 'skip': True, 'reason': skip_reason(book, chap, pn)}
            skipped += 1
            continue
        normalized = normalize(source, lang)
        # Auto-skip paragraphs that became empty (or just punctuation) after normalization
        # — typically orphaned citations from OCR
        if not normalized or all(c in '.,;:!?…«»"\'-–— ' for c in normalized):
            out[str(pn)] = {'text': '', 'skip': True, 'reason': 'empty-after-normalization'}
            skipped += 1
            if review:
                diffs.append((pn, source, '[skipped — orphan citation/punct only]'))
            continue
        entry = {'text': normalized}
        out[str(pn)] = entry
        if normalized != source:
            changes += 1
            if review:
                diffs.append((pn, source, normalized))

    return {'sidecar': out, 'changes': changes, 'skipped': skipped, 'diffs': diffs}


def write_sidecar(book: str, chap: int, lang: str, sidecar: dict) -> Path | None:
    """Write the sidecar to disk. Returns the path, or None if empty (skipped)."""
    if not sidecar:
        return None
    tts_dir = LIB / book / 'tts'
    tts_dir.mkdir(exist_ok=True)
    path = tts_dir / f'chapter-{chap}.{lang}.json'
    path.write_text(json.dumps(sidecar, ensure_ascii=False, indent=2) + '\n')
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slug', help='Book slug (default: all books)')
    ap.add_argument('--chapter', type=int, help='Chapter N (default: all chapters)')
    ap.add_argument('--lang', help='Language code (default: all langs)')
    ap.add_argument('--review', action='store_true', help='Print side-by-side diffs')
    ap.add_argument('--review-limit', type=int, default=30, help='Max diffs to print in review mode')
    args = ap.parse_args()

    # Discover books
    if args.slug:
        books = [args.slug]
    else:
        books = sorted(p.name for p in LIB.iterdir()
                       if p.is_dir() and (p / '_meta.json').exists())

    langs = [args.lang] if args.lang else LANGS

    grand_total_changes = 0
    grand_total_skipped = 0
    grand_total_files = 0

    for book in books:
        meta_path = LIB / book / '_meta.json'
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text())
        chapters = [args.chapter] if args.chapter else list(range(1, meta['chapterCount'] + 1))

        for chap in chapters:
            for lang in langs:
                result = process_chapter(book, chap, lang, review=args.review)
                sidecar = result['sidecar']
                if not sidecar:
                    continue
                path = write_sidecar(book, chap, lang, sidecar)
                grand_total_files += 1
                grand_total_changes += result['changes']
                grand_total_skipped += result['skipped']
                rel_path = path.relative_to(LIB)
                print(f'  {rel_path}: {len(sidecar):4d} paragraphs '
                      f'({result["changes"]} normalized, {result["skipped"]} skipped)')

                if args.review and result['diffs']:
                    print(f'\n    === DIFFS ({len(result["diffs"])} total, showing first {args.review_limit}) ===')
                    for pn, source, normalized in result['diffs'][:args.review_limit]:
                        # Compact one-line view: show only the changed parts via short context
                        src_short = source[:140].replace('\n', ' ')
                        norm_short = normalized[:140].replace('\n', ' ')
                        print(f'    p{pn:3d} SRC : {src_short!r}')
                        print(f'    p{pn:3d} TTS : {norm_short!r}')
                        print()

    print(f'\nTotal: {grand_total_files} sidecar files written, '
          f'{grand_total_changes} paragraphs normalized, '
          f'{grand_total_skipped} paragraphs skipped')


if __name__ == '__main__':
    main()
