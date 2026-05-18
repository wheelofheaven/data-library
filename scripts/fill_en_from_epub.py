#!/usr/bin/env python3
"""Fill Raël foundational-book chapter JSONs with English from the
IRM 2005 EPUB. Supports ETTMTTP (default) and LWTE via --book.

The English translator broke many French paragraphs into ~2x as many
English paragraphs. We can't do per-paragraph 1:1 pairing, so we
group English paragraphs proportionally: for each French paragraph i
out of F total, the English content is en_paragraphs[round(i*E/F) :
round((i+1)*E/F)] joined by blank lines.

The cumulative reading order matches — readers see all French and all
English text — but individual paragraph alignment is approximate. The
reader's split-view will show asymmetric paragraph density.

This is a stop-gap so the book can be read locally. The eventual
Claude+_glossary pass will replace this with paragraph-aligned i18n.

Usage:
  ./fill_en_from_epub.py                   # fill ETTMTTP (default)
  ./fill_en_from_epub.py --book lwte       # fill LWTE
  ./fill_en_from_epub.py --book ettmttp --clear   # blank i18n.en (undo)
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path('/Users/zara/Development/github.com/wheelofheaven')
EPUB_DIR = Path('/tmp/ettmttp-extract/epub/OPS')

BOOKS = {
    'ettmttp': {
        'slug': 'extraterrestrials-took-me-to-their-planet',
        'chapters': [
            {'n': 1, 'epub_file': 'chapter-11.xhtml'},
            {'n': 2, 'epub_file': 'chapter-12.xhtml'},
            {'n': 3, 'epub_file': 'chapter-13.xhtml'},
        ],
    },
    'lwte': {
        'slug': 'lets-welcome-the-extraterrestrials',
        'chapters': [
            {'n': 1, 'epub_file': 'chapter-14.xhtml'},
            {'n': 2, 'epub_file': 'chapter-15.xhtml'},
            {'n': 3, 'epub_file': 'chapter-16.xhtml'},
            {'n': 4, 'epub_file': 'chapter-17.xhtml'},
        ],
    },
}


class ParagraphExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.paragraphs: list[str] = []
        self._buf: list[str] = []
        self._in_p = False

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self._in_p = True
            self._buf = []
        elif tag == 'br' and self._in_p:
            self._buf.append(' ')

    def handle_endtag(self, tag):
        if tag == 'p' and self._in_p:
            self._in_p = False
            text = ''.join(self._buf)
            text = re.sub(r'\s+', ' ', text).strip()
            if text and len(text) >= 10:
                self.paragraphs.append(text)
            self._buf = []

    def handle_data(self, data):
        if self._in_p:
            self._buf.append(data)


def parse_epub_chapter(path: Path) -> list[str]:
    p = ParagraphExtractor()
    p.feed(path.read_text(encoding='utf-8'))
    return p.paragraphs


def truncate_ettmttp_ch3(paragraphs: list[str]) -> list[str]:
    out: list[str] = []
    for p in paragraphs:
        if '___' in p or p.strip().upper() == "LET'S WELCOME THE EXTRA-TERRESTRIALS":
            break
        out.append(p)
    return out


def lib_targets(slug: str) -> list[Path]:
    return [
        REPO / f'data-library/{slug}',
        REPO / f'www.wheelofheaven.io/data/library/{slug}',
    ]


def fill_chapter(book_key: str, n: int, epub_file: str) -> None:
    en_paras = parse_epub_chapter(EPUB_DIR / epub_file)
    if book_key == 'ettmttp' and n == 3:
        en_paras = truncate_ettmttp_ch3(en_paras)
    if en_paras and en_paras[0].isupper() and len(en_paras[0]) < 80:
        en_paras = en_paras[1:]
    E = len(en_paras)
    slug = BOOKS[book_key]['slug']

    for lib in lib_targets(slug):
        ch_path = lib / f'chapter-{n}.json'
        if not ch_path.exists():
            print(f'  skip (not present): {ch_path.relative_to(REPO)}')
            continue
        data = json.loads(ch_path.read_text(encoding='utf-8'))
        fr_paras = data['paragraphs']
        F = len(fr_paras)

        for i, p in enumerate(fr_paras):
            start = round(i * E / F)
            end = round((i + 1) * E / F)
            slice_ = en_paras[start:end]
            p['i18n']['en'] = '\n\n'.join(slice_)

        ch_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + '\n',
            encoding='utf-8',
        )
        print(f'  ch{n}: {F} French → {E} English (ratio {E/F:.2f}x) — {ch_path.relative_to(REPO)}')


def clear_chapter(book_key: str, n: int) -> None:
    slug = BOOKS[book_key]['slug']
    for lib in lib_targets(slug):
        ch_path = lib / f'chapter-{n}.json'
        if not ch_path.exists():
            continue
        data = json.loads(ch_path.read_text(encoding='utf-8'))
        for p in data['paragraphs']:
            p['i18n']['en'] = ''
        ch_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + '\n',
            encoding='utf-8',
        )
        print(f'  cleared {ch_path.relative_to(REPO)}')


def main() -> None:
    book_key = 'ettmttp'
    if '--book' in sys.argv:
        idx = sys.argv.index('--book')
        book_key = sys.argv[idx + 1].lower()
        if book_key not in BOOKS:
            sys.exit(f"unknown --book {book_key!r}; expected one of {sorted(BOOKS)}")
    chapters = BOOKS[book_key]['chapters']
    if '--clear' in sys.argv:
        print(f'Clearing i18n.en for {book_key}')
        for spec in chapters:
            clear_chapter(book_key, spec['n'])
        return
    print(f'Filling i18n.en from EPUB for {book_key} ({len(chapters)} chapters)')
    for spec in chapters:
        fill_chapter(book_key, spec['n'], spec['epub_file'])


if __name__ == '__main__':
    main()
