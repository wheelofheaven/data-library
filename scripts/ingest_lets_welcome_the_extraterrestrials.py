#!/usr/bin/env python3
"""Ingest "Accueillir les Extra-Terrestres" (LWTE, Raël's 3rd
foundational book, 1979) from the standalone Nova Distribution 2001
French reprint + the IRM 2005 "Message from the Designers" English
EPUB.

Source PDF: 154 pages, single book (not an anthology like the
TBWTT/ETTMTTP combined PDF). 4 main chapters:
  CHAPITRE I:  Questions Revenant Le Plus Souvent
  CHAPITRE II: Nouvelles Révélations
  CHAPITRE III: Une Religion Athée
  CHAPITRE IV: Commentaires Et Témoignages De Raëliens

The English EPUB material covering this book is at chapters 14-17:
  EPUB ch14 = LWTE ch1 (Frequently Asked Questions)
  EPUB ch15 = LWTE ch2 (The New Revelations)
  EPUB ch16 = LWTE ch3 (An Atheist Religion)
  EPUB ch17 = LWTE ch4 (Commentaries And Testimonials Of Raelians)

The French ingest mirrors the proven ETTMTTP pipeline:
  - PyMuPDF for paragraph blocks (cleaner than pdftotext -layout)
  - Filter page numbers, running headers, subsection headings
  - Strip inline footnote tails and editorial-note (‡) prefixes
  - Merge cross-page sentence splits via lowercase-start +
    mid-clause-end heuristics
  - Per-chapter speaker assignment (conservative; LWTE is mostly
    Raël's narration in Q&A and explanatory form, with named guides
    in ch4 testimonials)

The pre-chapter material (Introduction recap, Apparition 7-10-1976,
Message 14-3-1978, Modification des Nouveaux Commandements) appears
at the front of the 2001 French edition but at the back as ADDENDUM
in the 2005 English EPUB. NOT included in this first-cut ingest —
the recap Introduction is summary of TBWTT/ETTMTTP we already have,
and the Apparitions/Messages can become a separate Chapter 0 or
ADDENDUM chapter in a future pass.
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
PDF_FR = REPO / 'data-sources/pdf/lets-welcome-the-extraterrestrials/lets-welcome-the-extraterrestrials-fr.pdf'
EPUB_DIR = Path('/tmp/ettmttp-extract/epub/OPS')
OUTPUT_DIR = REPO / 'data-library/lets-welcome-the-extraterrestrials'
CURATOR_DIR = REPO / 'curator-work/lets-welcome-the-extraterrestrials'

I18N_LANGS = ['en', 'de', 'es', 'ru', 'ja', 'ko', 'zh', 'zh-Hant']

CHAPTERS = [
    {
        'n': 1,
        'fr_title': 'Questions Revenant le Plus Souvent',
        'titles': {
            'en': 'Frequently Asked Questions',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-14.xhtml',
        # The body uses the chapter TITLE (not "CHAPITRE I") as the
        # heading. "CHAPITRE I" appears only in the back-matter TOC.
        'fr_start_marker': 'QUESTIONS REVENANT LE PLUS SOUVENT',
        'fr_end_marker_next_chapter': 'NOUVELLES RÉVÉLATIONS',
    },
    {
        'n': 2,
        'fr_title': 'Nouvelles Révélations',
        'titles': {
            'en': 'The New Revelations',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-15.xhtml',
        'fr_start_marker': 'NOUVELLES RÉVÉLATIONS',
        'fr_end_marker_next_chapter': 'UNE RELIGION ATHÉE',
    },
    {
        'n': 3,
        'fr_title': 'Une Religion Athée',
        'titles': {
            'en': 'An Atheist Religion',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-16.xhtml',
        'fr_start_marker': 'UNE RELIGION ATHÉE',
        # No "CHAPITRE IV / COMMENTAIRES" heading in body — only TOC.
        # Anchor on the title of the first testimonial.
        'fr_end_marker_next_chapter': "Le Raëlisme sous l'œil de la science",
    },
    {
        'n': 4,
        'fr_title': 'Commentaires et Témoignages de Raëliens',
        'titles': {
            'en': 'Commentaries and Testimonials of Raelians',
            'de': '', 'es': '', 'ru': '', 'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'epub_file': 'chapter-17.xhtml',
        'fr_start_marker': "Le Raëlisme sous l'œil de la science",
        # Ends at the BIBLIOGRAPHIE section preceding the TOC.
        'fr_end_marker_next_chapter': 'BIBLIOGRAPHIE',
    },
]


# ---------------------------------------------------------------------------
# French PDF: PyMuPDF block extraction

_TERMINAL_PUNCT_CHARS = '.!?»…'
_INDENT_PARA_RE = re.compile(r'^ {2,}\S')


def extract_fr_pdf() -> list[str]:
    """Extract paragraphs from the LWTE French PDF using two
    paragraph-boundary signals from pdftotext -layout output:

      1) Blank lines (the obvious case)
      2) Indented body lines (≥2 leading spaces) when the previous
         logical line ended with terminal punctuation — pdftotext
         doesn't insert blank lines between indented paragraphs in
         dense layouts, so we must detect indent-based paragraph
         starts directly. We skip the indent signal when the previous
         line was a page number or running header (those are noise
         that don't reset paragraph state, even though they're
         indented).

    Hyphenated line-breaks (`word-\\nword` with lowercase
    continuation) are rejoined.
    """
    out = subprocess.run(
        ['pdftotext', '-layout', '-nopgbrk', str(PDF_FR), '-'],
        capture_output=True, text=True, check=True,
    )
    raw_lines = out.stdout.splitlines()

    def is_noise_line(ln: str) -> bool:
        s = ln.strip()
        if not s:
            return False
        if PAGE_NUM_RE.match(s):
            return True
        if RUNNING_HEADER_RE.match(s):
            return True
        return False

    def is_subsection_heading_line(ln: str) -> bool:
        """A line that's a centered/heavily-indented short MIXED-CASE
        heading with no terminal punctuation — these mark subsection
        breaks in the source but pdftotext doesn't put blank lines
        around them. We use them as paragraph break signals; the
        heading itself is emitted as its own paragraph so the chapter
        slicer can anchor to it (e.g. ch4's "Le Raëlisme sous l'œil de
        la science") before clean_fr_paragraphs filters subsection
        headings via SUBSECTION_HINTS.

        Chapter markers ("CHAPITRE I", "UNE RELIGION ATHÉE") are
        all-uppercase and are NOT caught here — they need to flow
        through to the slicer for chapter-boundary detection."""
        leading = len(ln) - len(ln.lstrip(' '))
        s = ln.strip()
        if not s or len(s) > 100:
            return False
        if leading < 10:
            return False
        if s.endswith(tuple(_TERMINAL_PUNCT_CHARS)):
            return False
        # Skip chapter / section markers (handled by the slicer +
        # uppercase filter in clean_fr_paragraphs).
        if s.isupper():
            return False
        return True

    paragraphs: list[str] = []
    current: list[str] = []  # accumulating lines for current paragraph

    def flush():
        if not current:
            return
        text = ''
        for i, ln in enumerate(current):
            stripped = ln.strip()
            if i == 0:
                text = stripped
            elif text.endswith('-') and not text.endswith(' -'):
                next_first = stripped.split(' ', 1)[0] if stripped else ''
                if next_first and next_first[0].islower():
                    text = text[:-1] + stripped
                else:
                    text = text + ' ' + stripped
            else:
                text = text + ' ' + stripped
        text = re.sub(r'\s+', ' ', text).strip()
        if text:
            paragraphs.append(text)
        current.clear()

    for ln in raw_lines:
        # Blank → paragraph boundary.
        if not ln.strip():
            flush()
            continue
        # Noise lines (page num, running header) → don't break the
        # paragraph but don't include them either.
        if is_noise_line(ln):
            continue
        # Subsection heading line → flush current, emit the heading
        # as its own paragraph (so the chapter slicer can anchor to
        # it), body picks up on the next line. Headings get filtered
        # later via SUBSECTION_HINTS in clean_fr_paragraphs.
        if is_subsection_heading_line(ln):
            flush()
            paragraphs.append(re.sub(r'\s+', ' ', ln.strip()))
            continue
        # Indented line where prev paragraph's last logical line ended
        # with terminal punctuation → start a new paragraph.
        if current and _INDENT_PARA_RE.match(ln):
            prev_last = current[-1].rstrip()
            if prev_last.endswith(tuple(_TERMINAL_PUNCT_CHARS)):
                flush()
        current.append(ln)

    flush()
    return paragraphs


PAGE_NUM_RE = re.compile(r'^\s*\d{1,3}\s*$')
# Running headers — "ACCUEILLIR LES EXTRA-TERRESTRES" on every page.
RUNNING_HEADER_RE = re.compile(
    r'^\s*(ACCUEILLIR LES EXTRA-TERRESTRES|TABLE DES MATIÈRES|SOMMAIRE)\s*$',
    re.IGNORECASE,
)
FOOTNOTE_TAIL_RE = re.compile(
    r'\s*_{5,}\s*\d+\.?\s*N\.D\.L\.R\..*$', re.IGNORECASE | re.DOTALL,
)
FOOTNOTE_STANDALONE_RE = re.compile(
    r'^_{5,}\s*\d+\.?\s+', re.IGNORECASE,
)
EDITORIAL_DAGGER_RE = re.compile(r'^\s*‡\s+')
MID_CLAUSE_END_RE = re.compile(
    r'\b(le|la|les|l[’\']|un|une|des|du|de|à|en|et|ou|car|mais|si|'
    r'ce|cette|ces|son|sa|ses|mon|ma|mes|ton|ta|tes|notre|votre|leur|leurs|'
    r'qui|que|dont|où|comme|chez|sur|sous|dans|pour|par|sans|avec)\s*$',
    re.IGNORECASE,
)

_RAW_SUBSECTION_HINTS = [
    # Chapter I (FAQ) subsections — match the TOC entries.
    'Contradictions apparentes',
    'Contradictions apparentes entre le premier et le deuxième message',
    "Datation de l'œuvre des Elohim", "Le peuple d'Israël et les Juifs",
    "Le Mouvement Raëlien et l'argent",
    'Rien de constant dans le temps et l’espace',
    "Rien de constant dans le temps et l'espace",
    'Transmission du plan cellulaire et os frontal',
    "La Terre est-elle un atome du doigt de dieu ?",
    "L'arche de Noé : un vaisseau spatial",
    'La vie après la vie ou le rêve et la réalité',
    "Le niveau d'évolution scientifique des Elohim",
    'Ni dieu, ni âme, mais les Elohim. et le code génétique',
    'Ni dieu, ni âme, mais les Elohim, et le code génétique',
    "La religion de l'infini",
    "L'avenir des religions traditionnelles",
    'L’avenir des religions traditionnelles',
    'Raëlisme et géniocratie',
    'Qui a créé les créateurs des créateurs ?',
    'A quoi sert-il de vivre ?',
    "Qu'est-ce que le plaisir ?",
    "Qu'est-ce que la mort ?",
    'Liberté sexuelle et non obligation',
    'Raëlisme et homosexualité',
    'Déistes et évolutionnistes : les faux prophètes',
    'Le suicide',
    # Chapter II (Nouvelles Révélations)
    "Le diable n'existe pas, je l'ai rencontré",
    'Mon père qui est dans les cieux',
    "Message de Yahvé aux hommes de la Terre",
    "Message de Yahvé aux hommes de la Terre : l'Apocalypse du cataclysme nucléaire final",
    "L'Apocalypse du cataclysme nucléaire final",
    # Chapter III (Religion Athée)
    'Des anges sans ailes', 'La déresponsabilisation',
    # Chapter IV (Témoignages) — these are the titles, but they're also
    # the chapter content start markers. Don't filter them.
]


def _norm_apo(s: str) -> str:
    return s.replace('’', "'").replace('‘', "'")


SUBSECTION_HINTS = {_norm_apo(h) for h in _RAW_SUBSECTION_HINTS}


def slice_french_chapter(blocks: list[str], start_marker: str, end_marker: str) -> list[str]:
    def is_body_marker(block_text: str, marker: str) -> bool:
        if marker not in block_text:
            return False
        # TOC entries end with a page number.
        if re.search(r'\b\d{1,3}\s*$', block_text):
            return False
        # The body marker block should not be a long body paragraph
        # containing the marker as a substring. Some headings include
        # author/role bylines so allow up to 150 chars.
        return len(block_text) < 150

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


def strip_footnote_tail(text: str) -> str:
    return FOOTNOTE_TAIL_RE.sub('', text).strip()


def clean_fr_paragraphs(chapter_blocks: list[str]) -> list[str]:
    kept: list[str] = []
    for block in chapter_blocks:
        text = re.sub(r'\s+', ' ', block).strip()
        if not text:
            continue
        text = strip_footnote_tail(text)
        if not text:
            continue
        norm = _norm_apo(text)
        if PAGE_NUM_RE.match(text):
            continue
        if RUNNING_HEADER_RE.match(text):
            continue
        if re.fullmatch(r'[IVX]+', text) or re.fullmatch(r'[1-9]', text):
            continue
        # Chapter heading blocks: short uppercase
        if text.isupper() and len(text) < 80:
            continue
        if norm in SUBSECTION_HINTS:
            continue
        if FOOTNOTE_STANDALONE_RE.match(text):
            continue
        if EDITORIAL_DAGGER_RE.match(text):
            continue
        if text.startswith('![') or text.startswith('<image'):
            continue
        if len(text) < 20:
            continue
        kept.append(text)

    # Merge cross-page splits. Two cases trigger merge, BOTH guarded
    # by `prev doesn't end with terminal punctuation` — if the
    # previous paragraph clearly closed (with .!?»…), it's a complete
    # paragraph and the next block — even one starting lowercase —
    # is a separate paragraph, not a continuation.
    #   1) Block starts with lowercase AND prev didn't end terminal —
    #      mid-sentence continuation after a page break.
    #   2) Prev is SHORT (< 400 chars) AND ends mid-clause (function
    #      word) — paragraph cut mid-clause by a page break.
    TERMINAL_PUNCT = '.!?»…'
    MID_CLAUSE_MAX_PREV_LEN = 400
    merged: list[str] = []
    for text in kept:
        if merged:
            prev = merged[-1]
            prev_ends_terminal = prev.rstrip().endswith(tuple(TERMINAL_PUNCT))
            lowercase_continuation = text[0].islower() and not prev_ends_terminal
            mid_clause = (
                not prev_ends_terminal
                and len(prev) < MID_CLAUSE_MAX_PREV_LEN
                and MID_CLAUSE_END_RE.search(prev.rstrip(' ,;:'))
            )
            if lowercase_continuation or mid_clause:
                if prev.endswith('-') and not prev.endswith(' -'):
                    merged[-1] = prev[:-1] + text
                else:
                    merged[-1] = prev + ' ' + text
                continue
        merged.append(text)
    return merged


# ---------------------------------------------------------------------------
# EPUB English reference

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


# ---------------------------------------------------------------------------
# Speaker assignment

def assign_speaker(text: str, prev_speaker: str, para_n: int) -> str:
    """Conservative speaker assignment for LWTE.

    The book is overwhelmingly Raël's own voice — Q&A style in ch1,
    explanatory prose in ch2-3, and named testimonials in ch4. The
    only consistent dialogue is in ch2's "Apocalypse" section where
    Yahweh speaks. Default to Narrator throughout; mark dash- or
    guillemet-prefixed dialogue blocks as Yahweh when they appear in
    a teaching context (heuristic, may need manual refinement).
    """
    t = text.strip()
    if not t:
        return 'Narrator'
    # Dash-prefixed quoted speech blocks → Yahweh (Elohim convention).
    if t.startswith(('—', '–')) and prev_speaker == 'Yahweh':
        return 'Yahweh'
    # Pure quoted speech ending with guillemet → Yahweh continuation
    # only if we were already in a Yahweh block.
    if t.startswith('«') and t.rstrip('.').endswith('»') and prev_speaker == 'Yahweh':
        return 'Yahweh'
    return 'Narrator'


# ---------------------------------------------------------------------------
# Build JSONs

def build_chapter(n: int, fr_paras: list[str], fr_title: str,
                  titles: dict[str, str]) -> dict:
    paragraphs = []
    prev_speaker = 'Narrator'
    for i, fr in enumerate(fr_paras, start=1):
        speaker = assign_speaker(fr, prev_speaker, i)
        paragraphs.append({
            'n': i,
            'speaker': speaker,
            'text': fr,
            'refId': f'LWTE-{n}:{i}',
            'i18n': {lang: '' for lang in I18N_LANGS},
        })
        prev_speaker = speaker
    return {
        'n': n,
        'bookSlug': 'lets-welcome-the-extraterrestrials',
        'bookCode': 'LWTE',
        'refId': f'LWTE-{n}',
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
        'slug': 'lets-welcome-the-extraterrestrials',
        'code': 'LWTE',
        'refId': 'LWTE',
        'titles': {
            'fr': 'Accueillir les Extra-Terrestres',
            'en': "Let's Welcome the Extraterrestrials",
            'de': '', 'es': '', 'ru': '',
            'ja': '', 'ko': '', 'zh': '', 'zh-Hant': '',
        },
        'publicationYear': 1979,
        'primaryLang': 'fr',
        'schema': ['book', 'chapters', 'paragraphs'],
        'revision': 1,
        'updated': '2026-05-18T00:00:00Z',
        'chapterCount': len(chapter_results),
        'paragraphCount': total_paras,
        'chapterFiles': chapter_files,
    }


# ---------------------------------------------------------------------------
# Main

def main(dry_run: bool = False) -> None:
    print(f"[1/5] Extracting French PDF: {PDF_FR.name}")
    fr_blocks = extract_fr_pdf()
    print(f"   extracted {len(fr_blocks)} blocks from PDF")

    print(f"[2/5] Parsing English EPUB chapters (reference only)")
    en_reference: dict[int, list[str]] = {}
    for spec in CHAPTERS:
        n = spec['n']
        en_paras = parse_epub_chapter(EPUB_DIR / spec['epub_file'])
        # Drop chapter title heading if it leaked through.
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
            f"# LWTE Chapter {n} — English reference (IRM 2005 anthology)\n\n"
            f"Source: 'Message from the Designers' EPUB, "
            f"chapter file: {CHAPTERS[n-1]['epub_file']}\n\n"
            f"This is the official IRM English translation, extracted "
            f"verbatim. Per-paragraph alignment with the French source "
            f"is approximate (the English translator breaks paragraphs "
            f"differently). Use as a stylistic reference for the "
            f"Claude+_glossary translation pass.\n\n"
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
