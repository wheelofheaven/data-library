#!/usr/bin/env python3
"""TTS text normalization for library books.

Transforms source paragraph text into clean prose for TTS engines (ElevenLabs,
OpenAI, etc.). Implements the rules from the TTS Normalization Spec.

Two operations:
- `normalize(text, lang)` — returns the TTS-ready string
- `should_skip(book, chap, pn)` — returns True if the paragraph should be
  omitted from audio entirely (pure addresses, footnote-only paragraphs)

Idempotent: normalize(normalize(x)) == normalize(x).
"""

import re

# === Strip rules: removed from audio ===

# Citation patterns — biblical, Quranic, classical, compound references in parens
# Match a parenthetical that starts with one of the recognized work names.
CITATION_WORKS = [
    # Biblical (FR forms)
    'Genèse', 'Exode', 'Lévitique', 'Nombres', 'Deutéronome', 'Josué', 'Juges',
    'Ruth', 'Samuel', 'Rois', 'Chroniques', 'Esdras', 'Néhémie', 'Esther',
    'Job', 'Psaume', 'Psaumes', 'Proverbes', 'Ecclésiaste', 'Cantique',
    'Esaïe', 'Isaïe', 'Jérémie', 'Lamentations', 'Ezéchiel', 'Daniel',
    'Osée', 'Joël', 'Amos', 'Abdias', 'Jonas', 'Michée', 'Nahum', 'Habacuc',
    'Sophonie', 'Aggée', 'Zacharie', 'Malachie',
    'Matthieu', 'Marc', 'Luc', 'Jean', 'Actes', 'Romains', 'Corinthiens',
    'Galates', 'Éphésiens', 'Ephésiens', 'Philippiens', 'Colossiens',
    'Thessaloniciens', 'Thess', 'Timothée', 'Tite', 'Philémon', 'Hébreux',
    'Jacques', 'Pierre', 'Apocalypse',
    # Biblical (EN forms)
    'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua',
    'Judges', 'Kings', 'Chronicles', 'Ezra', 'Nehemiah', 'Esther',
    'Psalm', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Isaiah', 'Jeremiah',
    'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Jonah', 'Micah',
    'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', 'Corinthians',
    'Galatians', 'Ephesians', 'Philippians', 'Colossians', 'Thessalonians',
    'Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', 'Peter', 'Revelation',
    # Other
    'Coran', 'Quran', 'sourate', 'verset', 'versets', 'Sourate',
    'Bhagavad', 'Veda', 'Vedas', 'Upanishad', 'Talmud', 'Mishnah',
]
# Pattern: opening paren, optional whitespace, one of the work names (case-sensitive),
# then anything up to closing paren (but only if it looks like a reference: contains digits
# or Roman numerals or other-work-name).
CITATION_RE = re.compile(
    r'\s*\(\s*(?:' + '|'.join(re.escape(w) for w in CITATION_WORKS) + r')\b[^)]*\)',
)

# Stand-alone bracketed editorial omissions: (...) or (…)
EDITORIAL_ELLIPSIS_RE = re.compile(r'\(\s*(?:\.\.\.|…)\s*\)')

# Asterisk footnote markers: (*) or (1), (2) when used as footnote anchors
ASTERISK_FOOTNOTE_RE = re.compile(r'\s*\(\*\)\s*')

# All quote marks across languages
QUOTE_MARKS_RE = re.compile(r'[«»"“”‘’„‚«»「」『』]')
# Note: U+2019 right single quotation mark IS used as apostrophe in French ("l'homme").
# We don't strip U+2019; only the explicit quote marks. The string above DOES include U+2019
# in the bracket — that's a mistake. Let me be explicit:
QUOTE_MARKS_RE = re.compile(
    '['
    '«»'      # « »
    '“”'      # " "
    '"'                 # straight double quote
    '「」'      # 「 」 JA/ZH/KO
    '『』'      # 『 』 JA/ZH/KO (less common, used for nested or book titles)
    '„'            # „ (German low quote)
    ']'
)

# Leading dialogue dash at paragraph start: "- ", "– ", or "— "
LEADING_DASH_RE = re.compile(r'^[-–—]\s+')

# OCR artifact: doubled punctuation
DOUBLED_DOT_RE = re.compile(r'\.{2,}(?!\.)')  # 2+ dots (but not part of …)
DOUBLED_COMMA_RE = re.compile(r',{2,}')
MULTI_SPACE_RE = re.compile(r'  +')

# MADECH1 leftover footnote anchor → MADECH
MADECH1_RE = re.compile(r'\bMADECH1\b')

# Multi-spelling of Yahweh in FR
IAHVÉ_RE = re.compile(r'\bIahvé\b')

# Abbreviations
M_DOT_RE = re.compile(r'\bM\.\s+([A-ZÉÈÊÀÂÎÔÛ])')
MM_DOT_RE = re.compile(r'\bMM\.\s+([A-ZÉÈÊÀÂÎÔÛ])')

# Currency: "100 000F" → "100 000 francs"
FRANCS_RE = re.compile(r'(\d)\s*F\b')


def normalize(text: str, lang: str = 'fr') -> str:
    """Apply normalization rules. Returns TTS-ready string."""
    if not text:
        return ''

    s = text

    # 1. Strip citations BEFORE stripping other parens
    s = CITATION_RE.sub('', s)

    # 2. Strip editorial brackets
    s = EDITORIAL_ELLIPSIS_RE.sub('', s)
    s = ASTERISK_FOOTNOTE_RE.sub(' ', s)

    # 3. Strip leading dialogue dash (per line, in case paragraph is multi-line)
    s = LEADING_DASH_RE.sub('', s)

    # 4. Strip quote marks (FR « », EN " ", JA/KO/ZH 「」, DE „ ", etc.)
    s = QUOTE_MARKS_RE.sub('', s)

    # 5. Fix the MADECH1 footnote artifact
    s = MADECH1_RE.sub('MADECH', s)

    # 6. Per-language name normalization
    if lang == 'fr':
        s = IAHVÉ_RE.sub('Yahvé', s)

    # 7. Abbreviation expansion (FR primarily; same forms used in EN translations)
    if lang in ('fr', 'en', 'es', 'de'):
        s = MM_DOT_RE.sub(r'Messieurs \1', s)
        s = M_DOT_RE.sub(r'Monsieur \1', s)

    # 8. Currency rewrite (FR francs convention)
    if lang in ('fr',):
        s = FRANCS_RE.sub(r'\1 francs', s)

    # 9. OCR noise cleanup
    s = DOUBLED_DOT_RE.sub('…', s)
    s = DOUBLED_COMMA_RE.sub(',', s)

    # 10. Collapse whitespace
    s = MULTI_SPACE_RE.sub(' ', s)
    s = s.strip()

    # 11. Clean up orphaned punctuation left after stripping
    # e.g. "...à rien.». " → "...à rien." (stripping » then ». leaves orphan)
    s = re.sub(r'\s+\.', '.', s)
    s = re.sub(r'\s+,', ',', s)
    s = re.sub(r'\s+;', ';', s)
    s = re.sub(r'\s+:', ':', s)
    s = re.sub(r'\s+!', '!', s)
    s = re.sub(r'\s+\?', '?', s)

    # 12. Collapse adjacent sentence terminators (artifact of stripping quotes around
    # exclamations/questions). Source "!»." → after strip → "!.". Keep the first.
    s = re.sub(r'([!?])[.]+', r'\1', s)
    s = re.sub(r'[.](?=[!?])', '', s)
    # Also handle ":." → ":" or "."? Stronger one wins, so keep ":" if it ends a clause
    s = re.sub(r':[.]', '.', s)

    return s


# === Paragraph-level skip flags ===
# Paragraphs that should be omitted from audio entirely.
SKIP_PARAGRAPHS = {
    # ETTMTTP ch3: closing-address paragraphs
    ('extraterrestrials-took-me-to-their-planet', 3, 264): 'address-line',
    ('extraterrestrials-took-me-to-their-planet', 3, 265): 'address-line',
    # ETTMTTP ch3 p266 has the "et n'oublie pas" closing that's still readable speech
    # so it stays.
}


def should_skip(book: str, chap: int, pn: int) -> bool:
    return (book, chap, pn) in SKIP_PARAGRAPHS


def skip_reason(book: str, chap: int, pn: int) -> str | None:
    return SKIP_PARAGRAPHS.get((book, chap, pn))


# === Quick self-test ===
if __name__ == '__main__':
    cases = [
        # (input, lang, expected_substring_NOT_present)
        ('«Le temps de la fin du monde est venu.» (Genèse, II-1)', 'fr', '«'),
        ('«Le temps de la fin du monde est venu.» (Genèse, II-1)', 'fr', '(Genèse'),
        ('- Redressez-vous et suivez-moi.', 'fr', '-'),
        ('Iahvé Elohim dit au serpent', 'fr', 'Iahvé'),  # should normalize to Yahvé
        ('le MADECH1 est en route', 'fr', 'MADECH1'),
        ('100 000F par an', 'fr', '100 000F'),
        ('M. Jullian nous dit', 'fr', 'M.'),
        ('texte (...) suite', 'fr', '(...)'),
        ('texte (*) suite', 'fr', '(*)'),
    ]
    print('Self-test:')
    for text, lang, must_not_contain in cases:
        out = normalize(text, lang)
        status = '✓' if must_not_contain not in out else '✗'
        print(f'  {status} {text!r}')
        print(f'    → {out!r}')

    # Positive expectations
    pos_cases = [
        ('Iahvé Elohim', 'fr', 'Yahvé'),
        ('MADECH1', 'fr', 'MADECH'),
        ('100 000F', 'fr', 'francs'),
        ('M. Jullian', 'fr', 'Monsieur Jullian'),
    ]
    print('\nPositive transformations:')
    for text, lang, must_contain in pos_cases:
        out = normalize(text, lang)
        status = '✓' if must_contain in out else '✗'
        print(f'  {status} {text!r} → {out!r} (expected to contain {must_contain!r})')
