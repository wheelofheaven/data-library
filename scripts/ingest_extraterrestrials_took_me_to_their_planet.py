#!/usr/bin/env python3
"""Ingest ETTMTTP from French PDF + English EPUB into data-library shape.

French source: 1998 Le Message reissue (DEUXIÈME LIVRE region of the
bundled PDF, since the 1975 standalone French PDF isn't in the repo).
English source: 2005 IRM "Message from the Designers" anthology EPUB
(chapters 11-13 cover the same ETTMTTP material).

Output mirrors data-library/the-book-which-tells-the-truth/ shape:
_meta.json + chapter-N.json files. Paragraphs carry French text in
paragraphs[].text and English in paragraphs[].i18n.en; the other 7
i18n slots are initialized empty for a later Claude+_glossary pass.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------------------
# Sources & target

REPO = Path('/Users/zara/Development/github.com/wheelofheaven')
PDF_FR = REPO / 'data-sources/pdf/_combined/le-message-donne-par-les-extra-terrestres.pdf'
EPUB_DIR = Path('/tmp/ettmttp-extract/epub/OPS')
OUTPUT_DIR = REPO / 'data-library/extraterrestrials-took-me-to-their-planet'

I18N_LANGS = ['en', 'de', 'es', 'ru', 'ja', 'ko', 'zh', 'zh-Hant']

CHAPTERS = [
    {
        'n': 1,
        'fr_title': 'Ma Vie Jusqu’à La Première Rencontre',
        'titles': {
            'en': 'My Life Until the First Encounter',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-11.xhtml',
        # French slice — markers in the PDF text. The header pattern
        # `^ +1$` followed by the chapter title is what separates
        # chapters in pdftotext -layout output. We use explicit search
        # strings to be robust against page-number noise.
        'fr_start_marker': 'Introduction',
        'fr_end_marker_next_chapter': 'LA DEUXIÈME RENCONTRE',
    },
    {
        'n': 2,
        'fr_title': 'La Deuxième Rencontre',
        'titles': {
            'en': 'The Second Encounter',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-12.xhtml',
        'fr_start_marker': 'LA DEUXIÈME RENCONTRE',
        # Body uses LES CLEFS (with EF), TOC uses LES CLÉS — anchor on body.
        'fr_end_marker_next_chapter': 'LES CLEFS',
    },
    {
        'n': 3,
        'fr_title': 'Les Clés',
        'titles': {
            'en': 'The Keys',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-13.xhtml',
        # The 1998 PDF body uses "LES CLEFS" (with F); the TOC uses
        # "LES CLÉS". We anchor on the body wording.
        'fr_start_marker': 'LES CLEFS',
        # Chapter 3 ends before the "MESSAGE DU 13 DÉCEMBRE 52 (1997)"
        # appendix in the French. In EPUB it ends before the
        # ___ separator + "LET'S WELCOME THE EXTRA-TERRESTRIALS".
        'fr_end_marker_next_chapter': 'MESSAGE DU 13 DÉCEMBRE',
    },
]


# ---------------------------------------------------------------------------
# French PDF: extract + clean

def extract_fr_pdf() -> list[str]:
    """Extract paragraphs from the French PDF using PyMuPDF.

    PyMuPDF's `get_text("blocks")` returns layout blocks per page —
    each block is typically one logical paragraph. We concatenate
    blocks across pages and filter noise (page numbers, running
    headers, footnotes).
    """
    import fitz
    paragraphs: list[str] = []
    doc = fitz.open(str(PDF_FR))
    for page in doc:
        blocks = page.get_text("blocks")
        # blocks is a list of (x0, y0, x1, y1, text, block_no, block_type)
        # Sort by reading order (top-to-bottom, left-to-right).
        blocks.sort(key=lambda b: (round(b[1] / 5), b[0]))
        for b in blocks:
            text = b[4]
            if not isinstance(text, str):
                continue
            text = re.sub(r'\s+', ' ', text).strip()
            if not text:
                continue
            paragraphs.append(text)
    return paragraphs


PAGE_NUM_RE = re.compile(r'^\s*\d{1,3}\s*$')
FOOTNOTE_DIVIDER_RE = re.compile(r'^_{3,}\s*$')
# Lines that recur as page-break running headers; case-insensitive.
RUNNING_HEADER_RE = re.compile(
    r'^\s*('
    r'SOMMAIRE|'
    r'Ma vie jusqu’à la première rencontre|'
    r'La deuxième rencontre|'
    r'Les clefs|Les clés|'
    r'PREMIER LIVRE|DEUXIÈME LIVRE'
    r')\s*$',
    re.IGNORECASE,
)
# Footnote bodies look like `N. text...` on a short line right after a
# divider. The MADECH footnote is the most common one.
FOOTNOTE_BODY_RE = re.compile(
    r'^\s*\d+\.?\s+N\.D\.L\.R\.|^\s*1\.\s+N\.D\.L\.R\.', re.IGNORECASE
)
# Subsection headers in the PDF appear as short non-uppercase blocks
# between body paragraphs. We strip them so the output is just body.
# Apostrophes are normalized below before comparison (PyMuPDF can emit
# either curly ’ or straight ' depending on font).
_RAW_SUBSECTION_HINTS = [
    'Introduction', 'Deux ans déjà', "L'enfance, Ovni sur Ambert",
    'Le pape des Druides', 'La poésie', 'La rencontre', 'Les conférences',
    "L'apparition du 31 juillet 1975", 'Le deuxième message', 'Le Bouddhisme',
    'Ni dieu ni âme', 'Le paradis terrestre', "L'autre monde",
    'Présentation aux anciens prophètes', 'Un avant goût de paradis',
    'Les nouveaux commandements', "Au peuple d'Israël",
    "L'homme", 'La naissance', "L'éducation", "L'éducation sensuelle",
    "L'épanouissement", 'La société', 'La méditation et la prière',
    'Les arts', 'La méditation sensuelle', 'La justice des hommes',
    'La science', 'Le cerveau humain', "L'apocalypse",
    'La communication télépathique', 'La récompense', 'Les guides',
    'Société et gouvernement',
]


def _norm_apo(s: str) -> str:
    return s.replace('’', "'").replace('‘', "'")


SUBSECTION_HINTS = {_norm_apo(h) for h in _RAW_SUBSECTION_HINTS}


def slice_french_chapter(blocks: list[str], start_marker: str, end_marker: str) -> list[str]:
    """Return the slice of paragraphs between the markers. The start
    marker matches a block that *is* the chapter title heading. The
    chapter body is everything until the next chapter's start marker.

    Both markers are searched as occurring at the *body* of the
    document, skipping any TOC appearance. TOC entries are short and
    typically include a page number on the same block; body markers
    are titles standing alone.
    """
    def is_body_marker(block_text: str, marker: str) -> bool:
        # Body marker: the block is mostly just the marker (allowing
        # for adjacent chapter number like "3 LES CLEFS" or the
        # following subtitle "LES CLEFS LES CLEFS" continuation).
        # Reject TOC entries which have trailing page numbers.
        if marker not in block_text:
            return False
        # TOC entries end with a page number.
        if re.search(r'\b\d{1,3}\s*$', block_text):
            return False
        # Body marker block should be short and contain the marker.
        return len(block_text) < 80

    start_idx = None
    for i, block in enumerate(blocks):
        if is_body_marker(block, start_marker):
            start_idx = i
            break
    if start_idx is None:
        raise RuntimeError(f"body start marker not found: {start_marker!r}")

    end_idx = len(blocks)
    for j in range(start_idx + 1, len(blocks)):
        if is_body_marker(blocks[j], end_marker):
            end_idx = j
            break

    return blocks[start_idx:end_idx]


def clean_fr_paragraphs(chapter_blocks: list[str]) -> list[str]:
    """Filter and reconstruct paragraphs from PyMuPDF blocks.

    Steps:
      1) Drop noise blocks (page numbers, running headers, headings,
         subsection labels, footnotes, image captions).
      2) Merge mid-page-break splits: when a block starts with a
         lowercase letter, it is a continuation of the previous body
         paragraph (the page break interrupted it).
    """
    kept: list[str] = []
    for block in chapter_blocks:
        text = re.sub(r'\s+', ' ', block).strip()
        if not text:
            continue
        norm = _norm_apo(text)
        if PAGE_NUM_RE.match(text):
            continue
        if RUNNING_HEADER_RE.match(text):
            continue
        if re.fullmatch(r'[1-9]', text):
            continue
        if text.isupper() and len(text) < 80:
            continue
        if norm in SUBSECTION_HINTS:
            continue
        if 'N.D.L.R' in text.upper():
            continue
        if text.startswith('![') or text.startswith('<image'):
            continue
        # Image-caption style: short block with a date in it ("...Raël le
        # 7 octobre 1975..."). Skip if it looks like a caption (under
        # 200 chars and contains "Raël"+year, or specifically the known
        # caption pattern).
        if (len(text) < 200 and 'Raël' in text and
                re.search(r'\b(19|20)\d{2}\b', text) and
                not text.endswith('.') and not text.endswith('»')):
            continue
        if len(text) < 20:
            continue
        kept.append(text)

    # Merge continuation paragraphs (start with lowercase = mid-sentence
    # resumption after a page break).
    merged: list[str] = []
    for text in kept:
        if merged and text[0].islower():
            # Append to previous, joining with a single space.
            # If previous ended with a hyphen-broken word, drop the hyphen.
            prev = merged[-1]
            if prev.endswith('-') and not prev.endswith(' -'):
                merged[-1] = prev[:-1] + text
            else:
                merged[-1] = prev + ' ' + text
        else:
            merged.append(text)
    return merged


# ---------------------------------------------------------------------------
# English EPUB: parse <p> tags

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


def truncate_epub_paragraphs_for_ch3(paragraphs: list[str]) -> list[str]:
    """EPUB chapter-13 contains both ETTMTTP ch3 AND the start of the
    third book ('Let's Welcome the Extra-Terrestrials'). Cut at the
    separator paragraph."""
    out: list[str] = []
    for p in paragraphs:
        # Heuristic: the third book is introduced by a long underscore
        # separator or by the title text itself.
        if '___' in p or p.strip().upper() == "LET'S WELCOME THE EXTRA-TERRESTRIALS":
            break
        out.append(p)
    return out


# ---------------------------------------------------------------------------
# Build JSONs

def build_chapter(n: int, fr_paras: list[str], fr_title: str,
                  titles: dict[str, str]) -> dict:
    """Build a chapter JSON with French-primary text and empty i18n slots.

    English from the EPUB is NOT pre-filled into paragraphs[].i18n.en
    because the IRM English translation segments paragraphs ~2x more
    finely than the French original — index-pairing would mis-align
    content. The EPUB text is saved separately as a translator
    reference for the Claude+_glossary pass to consult."""
    paragraphs = []
    for i, fr in enumerate(fr_paras, start=1):
        paragraphs.append({
            'n': i,
            'speaker': 'Narrator',
            'text': fr,
            'refId': f'ETTMTTP-{n}:{i}',
            'i18n': {lang: '' for lang in I18N_LANGS},
        })
    return {
        'n': n,
        'bookSlug': 'extraterrestrials-took-me-to-their-planet',
        'bookCode': 'ETTMTTP',
        'refId': f'ETTMTTP-{n}',
        'title': fr_title,
        'i18n': titles,
        'paragraphs': paragraphs,
    }


def build_meta(chapter_results: list[dict]) -> dict:
    chapter_files = []
    total_paras = 0
    for ch in chapter_results:
        chapter_files.append({
            'n': ch['n'],
            'file': f'chapter-{ch["n"]}.json',
            'title': ch['title'],
            'paragraphs': len(ch['paragraphs']),
        })
        total_paras += len(ch['paragraphs'])
    return {
        'slug': 'extraterrestrials-took-me-to-their-planet',
        'code': 'ETTMTTP',
        'refId': 'ETTMTTP',
        'titles': {
            'fr': 'Les Extra-Terrestres M’ont Emmené sur Leur Planète',
            'en': 'Extraterrestrials Took Me to Their Planet',
            'de': '', 'es': '', 'ru': '',
            'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'publicationYear': 1975,
        'primaryLang': 'fr',
        'schema': ['book', 'chapters', 'paragraphs'],
        'revision': 1,
        'updated': '2026-05-17T00:00:00Z',
        'chapterCount': len(chapter_results),
        'paragraphCount': total_paras,
        'chapterFiles': chapter_files,
    }


# ---------------------------------------------------------------------------
# Main

CURATOR_DIR = REPO / 'curator-work/extraterrestrials-took-me-to-their-planet'


def main(dry_run: bool = False) -> None:
    print(f"[1/5] Extracting French PDF: {PDF_FR.name}")
    fr_blocks = extract_fr_pdf()
    print(f"   extracted {len(fr_blocks)} blocks from PDF")

    print(f"[2/5] Parsing English EPUB (reference only — not paired)")
    en_reference: dict[int, list[str]] = {}
    for spec in CHAPTERS:
        n = spec['n']
        en_paras = parse_epub_chapter(EPUB_DIR / spec['epub_file'])
        if n == 3:
            en_paras = truncate_epub_paragraphs_for_ch3(en_paras)
        if en_paras and en_paras[0].isupper() and len(en_paras[0]) < 80:
            en_paras = en_paras[1:]
        en_reference[n] = en_paras
        print(f"   ch{n} EPUB: {len(en_paras)} English paragraphs")

    print(f"[3/5] Building {len(CHAPTERS)} chapter JSONs (French primary)")
    chapter_results = []
    for spec in CHAPTERS:
        n = spec['n']
        fr_slice = slice_french_chapter(
            fr_blocks, spec['fr_start_marker'], spec['fr_end_marker_next_chapter']
        )
        fr_paras = clean_fr_paragraphs(fr_slice)
        ratio = len(en_reference[n]) / max(1, len(fr_paras))
        print(f"   ch{n}: fr={len(fr_paras)} (en={len(en_reference[n])}, ratio={ratio:.2f}x)")
        chapter_json = build_chapter(n, fr_paras, spec['fr_title'], spec['titles'])
        chapter_results.append(chapter_json)

    print(f"[4/5] Writing outputs")
    if dry_run:
        print("   (dry-run, not writing)")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for ch in chapter_results:
        path = OUTPUT_DIR / f'chapter-{ch["n"]}.json'
        path.write_text(json.dumps(ch, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(f"   wrote {path.relative_to(REPO)}")
    meta = build_meta(chapter_results)
    meta_path = OUTPUT_DIR / '_meta.json'
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"   wrote {meta_path.relative_to(REPO)}")

    # Save EPUB English as translator reference, one file per chapter.
    CURATOR_DIR.mkdir(parents=True, exist_ok=True)
    for n, en_paras in en_reference.items():
        path = CURATOR_DIR / f'en-reference-chapter-{n}.md'
        body = '\n\n'.join(en_paras)
        path.write_text(
            f"# ETTMTTP Chapter {n} — English reference (IRM 2005 anthology)\n\n"
            f"Source: 'Message from the Designers' EPUB, "
            f"chapter file: {CHAPTERS[n-1]['epub_file']}\n\n"
            f"This is the official IRM English translation, extracted "
            f"verbatim. The translator broke many French paragraphs into "
            f"shorter English ones (~2x more paragraphs than the French "
            f"source), so this is not 1:1 alignable with chapter-{n}.json's "
            f"paragraphs[] array. Use as a stylistic reference for the "
            f"Claude+_glossary translation pass, NOT as a drop-in source.\n\n"
            f"---\n\n{body}\n",
            encoding='utf-8',
        )
        print(f"   wrote {path.relative_to(REPO)}")

    print(f"[5/5] Summary")
    for ch in chapter_results:
        fr_count = len(ch['paragraphs'])
        print(f"   ch{ch['n']}: {fr_count} French paragraphs, 0/8 i18n langs populated")


if __name__ == '__main__':
    main(dry_run='--dry-run' in sys.argv)
