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
    'Matthieu', 'Mathieu', 'Marc', 'Luc', 'Jean', 'Actes', 'Romains', 'Corinthiens',
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
    # Biblical (EN forms) — minor prophets + deuterocanon that the first
    # pass missed (they leaked "(Zechariah, V-9)" etc. into the audio)
    'Zechariah', 'Zephaniah', 'Habakkuk', 'Haggai', 'Malachi', 'Obadiah',
    'Nahum', 'Amos', 'Wisdom', 'Tobit', 'Song',
    # Deuterocanon / other (FR forms)
    'Sagesse', 'Tobie',
    # Other
    'Coran', 'Quran', 'Koran', 'Corán', 'Коран', 'sourate', 'sura', 'сура',
    'verset', 'versets', 'Sourate',
    'Bhagavad', 'Veda', 'Vedas', 'Upanishad', 'Talmud', 'Mishnah',
]
# Pattern: opening paren, then optionally a book-number prefix ("I Kings",
# "II Samuel", "1 Corinthians") and/or an article/qualifier ("The Wisdom of
# Solomon", "after Matthew", "d'après Luc"), then one of the work names,
# then anything up to closing paren.
_CITATION_PREFIX = r"(?:(?:I{1,3}|[123])\s+)?(?:(?:[Tt]he|[Aa]fter|[Ll][ae]|[Ee]l|[Dd]'après|[Ss]elon|[Nn]ach|[Ss]egún)\s+)?"
CITATION_RE = re.compile(
    r'\s*\(\s*' + _CITATION_PREFIX +
    r'(?:' + '|'.join(re.escape(w) for w in CITATION_WORKS) + r')\b[^)]*\)',
)

# Bare-numeral citation: "(X-13)", "(XIV-25)" — chapter-verse with no work
# name (the work was named in the running prose just before).
BARE_NUMERAL_CITATION_RE = re.compile(r'\s*\(\s*[IVXLC]+\s*-\s*\d+[^)]*\)')

# Generic chapter-verse citation, any language/script. The work-name list
# above only covers FR/EN spellings; translations cite with their own book
# names ("(Génesis, I-5)", "(Бытие, I-7)", "（創世記 I-7）", "(창세기 I-7)").
# In this corpus a parenthetical containing a Roman-numeral chapter-verse
# pair is always a scripture citation, so strip on that signature alone.
# Handles both ASCII and fullwidth parens.
GENERIC_CITATION_RE = re.compile(
    r'\s*[(（][^()（）]*\b[IVXLC]+\s*-\s*\d+[^()（）]*[)）]'
)

# Hebrew-script chapter-verse citation: "(תהילים, י״ט-5)", "(איוב, ב׳-6)".
# The he translation cites chapters with Hebrew-letter numerals, which carry a
# geresh (׳ U+05F3) or gershayim (״ U+05F4); combined with an Arabic verse digit
# inside a parenthetical, that signature is always a scripture citation in this
# corpus (metric glosses like "(9 מטרים)" carry no geresh/gershayim, so they are
# not stripped). Without this, Hebrew citations both leak into the spoken audio
# and, when a paragraph is citation-only, produce an empty TTS clip.
HEBREW_CITATION_RE = re.compile(
    r'\s*[(（][^()（）]*[׳״][^()（）]*\d[^()（）]*[)）]'
)

# Truncated citation at paragraph end: OCR lost the chapter-verse tail and
# the closing paren — "…the first day.» (Genesis," — strip the dangler.
# (The canonical data has been repaired; this guards future ingests.)
TRUNCATED_CITATION_RE = re.compile(
    r'\s*[(（]\s*' + _CITATION_PREFIX +
    r'(?:' + '|'.join(re.escape(w) for w in CITATION_WORKS) + r')\s*[,、，]?\s*$',
)

# Orphan citation tail at paragraph start: "XIV-25) This moreover…" — the
# other half of a truncated citation that drifted into the next paragraph.
ORPHAN_CITATION_TAIL_RE = re.compile(r'^\s*[IVXLC]+\s*-\s*\d+\s*[)）]\s*')

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

# Inline footnote asterisk glued to a word: "Mammon*" → "Mammon"
INLINE_ASTERISK_RE = re.compile(r'(\w)\*')

# Verse-range abbreviation inside surviving prose parens: "(v. 14 to 29)".
# The parens themselves are silent in TTS but "v." reads as the letter vee.
VERSE_ABBREV_RE = re.compile(r'\(\s*v\.\s*(\d+)\s*(to|à|-|–|bis)\s*(\d+)\s*\)')
_VERSE_WORD = {'en': 'verses', 'fr': 'versets', 'de': 'Verse', 'es': 'versículos'}

# Roman numerals in running prose ("In Genesis, XXVIII, there is…",
# "chapter XIX of Exodus"). TTS engines spell these out as letters, so
# convert to Arabic digits. Only multi-char tokens — a lone "I" is the
# English pronoun, and single-char numerals don't survive citation
# stripping anyway. Conversion runs AFTER citation strips so "(I Kings,
# VIII-11)" never reaches it.
ROMAN_TOKEN_RE = re.compile(r'\b[IVXLC]{2,8}\b')
_ROMAN_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}


def _roman_to_int(tok: str) -> int | None:
    """Strict Roman parse; None if invalid (e.g. 'VV', 'IL', 'CIVIC' words)."""
    total, prev = 0, 0
    for c in reversed(tok):
        v = _ROMAN_VALUES.get(c)
        if v is None:
            return None
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    # Round-trip check rejects malformed sequences the loose parse accepts
    if _int_to_roman(total) != tok:
        return None
    return total


def _int_to_roman(n: int) -> str:
    out = []
    for v, sym in ((100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                   (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
        while n >= v:
            out.append(sym)
            n -= v
    return ''.join(out)


def _roman_sub(m: re.Match) -> str:
    val = _roman_to_int(m.group(0))
    return str(val) if val is not None else m.group(0)


def normalize(text: str, lang: str = 'fr') -> str:
    """Apply normalization rules. Returns TTS-ready string."""
    if not text:
        return ''

    s = text

    # 1. Strip citations BEFORE stripping other parens
    s = CITATION_RE.sub('', s)
    s = BARE_NUMERAL_CITATION_RE.sub('', s)
    s = GENERIC_CITATION_RE.sub('', s)
    s = HEBREW_CITATION_RE.sub('', s)
    s = TRUNCATED_CITATION_RE.sub('', s)
    s = ORPHAN_CITATION_TAIL_RE.sub('', s)

    # 1b. Verbalize verse-range abbreviations that survive in prose parens
    verse_word = _VERSE_WORD.get(lang)
    if verse_word:
        s = VERSE_ABBREV_RE.sub(
            lambda m: f'({verse_word} {m.group(1)} {"à" if lang == "fr" else "to" if lang == "en" else "bis" if lang == "de" else "a"} {m.group(3)})',
            s)

    # 2. Strip editorial brackets
    s = EDITORIAL_ELLIPSIS_RE.sub('', s)
    s = ASTERISK_FOOTNOTE_RE.sub(' ', s)
    s = INLINE_ASTERISK_RE.sub(r'\1', s)

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

    # 9b. Roman numerals in surviving prose → Arabic digits (only for
    # Latin-script languages; CJK translations use Arabic digits already
    # except inside citations, which are stripped above).
    if lang in ('fr', 'en', 'de', 'es'):
        s = ROMAN_TOKEN_RE.sub(_roman_sub, s)

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
    # TBWTT ch5 p44: "*Mammon: wealth in Aramaic." — print-edition footnote
    # that leaked into the text stream. Visible in the reader (historical
    # text), but not speech.
    ('the-book-which-tells-the-truth', 5, 44): 'footnote-only',
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
