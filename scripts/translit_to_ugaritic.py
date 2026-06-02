#!/usr/bin/env python3
"""Convert KTU/standard Ugaritic transliteration to Ugaritic Unicode (U+10380-U+1039F).

The Ugaritic alphabet is a 30-letter Northwest-Semitic abjad rendered in cuneiform
wedges. Unlike Sumero-Akkadian logographic cuneiform, the mapping from standard
scholarly transliteration to Unicode is 1:1 and mechanical.

Usage:
    from translit_to_ugaritic import translit_to_unicode
    translit_to_unicode("yam")          # → "𐎊𐎎"
    translit_to_unicode("bʿl")          # → "𐎁𐎓𐎍"
    translit_to_unicode("aliyn bʿl")    # → "𐎀𐎍𐎊𐎐𐎟𐎁𐎓𐎍"   (word divider 𐎟 between words)

Lacunae:
    [...]   passes through unchanged (project lacuna-bracket convention)
    [xyz]   restored text: brackets pass through, letters convert
    <xyz>   editorial addition: brackets pass through, letters convert
    {xyz}   editorial deletion: brackets pass through, letters convert
"""

# Standard KTU/Smith transliteration → Ugaritic Unicode block (U+10380-U+10399)
# 30 letters + word divider (U+1039F)
TRANSLIT_MAP = {
    # ALPHA (glottal stop + vowel): ʾa, ʾi, ʾu — Ugaritic distinguishes three alef letters,
    # each representing the glottal stop plus its accompanying vowel. These are LETTERS in
    # the script, not vowel-marks. Strict KTU transliteration requires explicit ʾ marking.
    "ʾa": "𐎀",  # U+10380 LETTER ALPHA
    "ʾi": "𐎛",  # U+1039B LETTER I
    "ʾu": "𐎜",  # U+1039C LETTER U
    # NOTE: bare vowels "a", "i", "u" without ʾ are NOT mapped — they represent
    # comparative-Semitics vowel reconstructions that have no surface in the script.
    # Source files must use strict KTU transliteration: ʾaliyn baʿl, not aliyn b'l.

    # Consonants in standard KTU order:
    "b": "𐎁",   # U+10381 LETTER BETA
    "g": "𐎂",   # U+10382 LETTER GAMLA
    "ḫ": "𐎃",   # U+10383 LETTER KHA (voiceless velar fricative)
    "d": "𐎄",   # U+10384 LETTER DELTA
    "h": "𐎅",   # U+10385 LETTER HO
    "w": "𐎆",   # U+10386 LETTER WO
    "z": "𐎇",   # U+10387 LETTER ZETA
    "ḥ": "𐎈",   # U+10388 LETTER HOTA (voiceless pharyngeal fricative)
    "ṭ": "𐎉",   # U+10389 LETTER TET (emphatic t)
    "y": "𐎊",   # U+1038A LETTER YOD
    "k": "𐎋",   # U+1038B LETTER KAF
    "š": "𐎌",   # U+1038C LETTER SHIN
    "l": "𐎍",   # U+1038D LETTER LAMDA
    "m": "𐎎",   # U+1038E LETTER MEM
    "ḏ": "𐎏",   # U+1038F LETTER DHAL (voiced interdental)
    "n": "𐎐",   # U+10390 LETTER NUN
    "ẓ": "𐎑",   # U+10391 LETTER ZU (emphatic z, sometimes ġ in some systems)
    "s": "𐎒",   # U+10392 LETTER SAMKA
    "ʿ": "𐎓",   # U+10393 LETTER AIN (voiced pharyngeal)
    "p": "𐎔",   # U+10394 LETTER PU
    "ṣ": "𐎕",   # U+10395 LETTER SADE (emphatic s)
    "q": "𐎖",   # U+10396 LETTER QOPA
    "r": "𐎗",   # U+10397 LETTER RASHA
    "ṯ": "𐎘",   # U+10398 LETTER THANNA (voiceless interdental)
    "ġ": "𐎙",   # U+10399 LETTER GHAIN
    "t": "𐎚",   # U+1039A LETTER TO
    # ALPHA-I and ALPHA-U already listed above (ʾi, ʾu)
    "ś": "𐎝",   # U+1039D LETTER SSU (rare; sin variant)
}

WORD_DIVIDER = "𐎟"  # U+1039F WORD DIVIDER

# Sort keys by length descending so multi-char patterns (ʾa, ʾi, ʾu) match before "a", "i", "u"
SORTED_KEYS = sorted(TRANSLIT_MAP.keys(), key=lambda k: -len(k))


def translit_word(translit: str) -> str:
    """Convert a single transliterated word to Ugaritic Unicode."""
    result = []
    i = 0
    n = len(translit)
    while i < n:
        ch = translit[i]
        # Pass through bracket characters unchanged (lacuna convention)
        if ch in "[](){}<>...":
            result.append(ch)
            i += 1
            continue
        # Try multi-char keys first (sorted by length descending)
        matched = False
        for key in SORTED_KEYS:
            if translit[i:i+len(key)] == key:
                result.append(TRANSLIT_MAP[key])
                i += len(key)
                matched = True
                break
        if not matched:
            # Unknown char — preserve as-is (e.g. punctuation, numbers, parentheticals)
            result.append(ch)
            i += 1
    return "".join(result)


def translit_to_unicode(translit: str) -> str:
    """Convert a transliterated line/phrase (space-separated words) to Ugaritic Unicode.

    Words separated by whitespace are joined with the Ugaritic word divider 𐎟.
    Hyphens within words (rare in Ugaritic) are dropped.
    """
    words = translit.replace("-", "").split()
    return WORD_DIVIDER.join(translit_word(w) for w in words)


if __name__ == "__main__":
    # Self-test
    examples = [
        ("ym",              "𐎊𐎎"),                          # Yamm, the Sea
        ("bʿl",             "𐎁𐎓𐎍"),                         # Baʿl, the storm-god
        ("ʾil",             "𐎛𐎍"),                          # ʾIl (= El), head of pantheon — uses ALEF-I
        ("ʾaṯrt",           "𐎀𐎘𐎗𐎚"),                       # ʾAṯirat (= Asherah)
        ("ʾant",            "𐎀𐎐𐎚"),                         # ʾAnat the warrior consort — alef-a + n + t (the "a" is intrinsic to the alef-a letter)
        ("kṯr",             "𐎋𐎘𐎗"),                         # Kothar, divine craftsman
        ("mt",              "𐎎𐎚"),                          # Môt, death personified
        ("ʾalʾiyn bʿl",     "𐎀𐎍𐎛𐎊𐎐𐎟𐎁𐎓𐎍"),                # "Mightiest Baʿl" (epithet) — 5 letters then 3, ʾalʾiyn has TWO alef variants
        ("ymlk bʿl",        "𐎊𐎎𐎍𐎋𐎟𐎁𐎓𐎍"),                # "Baʿl reigns"
        ("bn ʾilm",         "𐎁𐎐𐎟𐎛𐎍𐎎"),                    # "Sons of El" = bnei elohim
        ("lṭn bṯn brḥ",     "𐎍𐎉𐎐𐎟𐎁𐎘𐎐𐎟𐎁𐎗𐎈"),           # "Lôtanu the fleeing serpent" (= Leviathan, Isa 27:1)
    ]
    for translit, expected in examples:
        got = translit_to_unicode(translit)
        status = "✓" if got == expected else "✗"
        print(f"{status} {translit!r} → {got!r}  (expected {expected!r})")
