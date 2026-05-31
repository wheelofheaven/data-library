#!/usr/bin/env python3
"""Find split markers using an FR anchor + relative-position heuristic for other langs.

For each (book, chap, pn) the user provides a list of FR anchor phrases (one per split).
The script:
  1. Finds the FR sentence-end marker as the full sentence containing the anchor.
  2. For each target language, finds the sentence-end NEAREST to the same relative
     position in the target text. Returns the full sentence as the marker.

Cross-language alignment may drift by ~1 sentence for languages with different
sentence structures (esp. JA/KO compared to FR). This is acceptable for audiobook
purposes since each language reads its own paragraph file.
"""

import json
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent  # data-library/ (this script lives in data-library/scripts/)

TERMINATORS = '.!?:。！？：…'


def find_terminators(text: str) -> list[tuple[int, int]]:
    """Return list of (term_start, term_end) — terminator runs including closing quotes."""
    out = []
    i = 0
    while i < len(text):
        if text[i] in TERMINATORS:
            j = i + 1
            while j < len(text) and text[j] in TERMINATORS:
                j += 1
            while j < len(text) and text[j] in '»"」』）)':
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return out


def sentence_containing(text: str, pos: int, terms: list) -> str:
    """Return the sentence containing position pos (between previous and next terminator)."""
    # Find terminator at or just before pos
    prev_end = 0
    next_end = len(text)
    for ts, te in terms:
        if te <= pos:
            prev_end = te
        elif ts >= pos:
            next_end = te
            break
        else:
            # pos is inside this terminator run; this is "the" terminator
            next_end = te
            break
    # Strip leading whitespace
    s = prev_end
    while s < len(text) and text[s] in ' \n\t':
        s += 1
    return text[s:next_end].strip()


def find_fr_sentence(fr_text: str, anchor: str) -> tuple[str, int]:
    """Return (sentence_marker, end_pos_in_text). Anchor must be unique."""
    norm_text = fr_text.replace('’', "'")
    norm_anchor = anchor.replace('’', "'")
    cnt = norm_text.count(norm_anchor)
    if cnt != 1:
        raise ValueError(f'FR anchor count={cnt}: {anchor!r}')
    pos = norm_text.find(norm_anchor)
    terms = find_terminators(fr_text)
    sent = sentence_containing(fr_text, pos, terms)
    # end_pos = the end of the terminator at the end of this sentence
    end_pos = pos + len(anchor)
    for ts, te in terms:
        if ts >= end_pos:
            end_pos = te
            break
        elif te > end_pos:
            end_pos = te
            break
    return sent, end_pos


def find_lang_sentence(text: str, target_pos: int) -> str:
    """Return the sentence whose terminator-end is nearest to target_pos."""
    terms = find_terminators(text)
    if not terms:
        return text
    closest = min(terms, key=lambda t: abs(t[1] - target_pos))
    return sentence_containing(text, closest[0], terms)


# (book, chap, pn) -> [fr_anchor_per_split, ...]
FR_ANCHORS = {
    ('extraterrestrials-took-me-to-their-planet', 1, 3): [
        "primitifs de son époque",
    ],
    ('extraterrestrials-took-me-to-their-planet', 1, 66): [
        "qu'on ne l'avait toujours pas retrouvé",
    ],
    ('extraterrestrials-took-me-to-their-planet', 1, 74): [
        "seul quotidien de la région",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 1): [
        "prendre part aux décisions",
        "ouvrir à leur tour des esprits",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 2): [
        "réunion du 6 août à Clermont-Ferrand",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 11): [
        "un bain m'attendait",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 22): [
        "en l'imitant",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 25): [
        "cela nous avons pu le prouver",
        "n'a eu que le temps de faire un pas",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 30): [
        "engraisser une seule personne: le patron",
        "Mais vous n'êtes plus des primitifs maintenant",
        "à force de manoeuvres contre des cibles d'entraînement",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 31): [
        "qui amènent une crainte de \"l'étranger\"",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 33): [
        "en même temps que des fleurs gigantesques",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 38): [
        "sept cents Elohim membres du conseil des éternels",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 40): [
        "sept-cents ans environ",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 73): [
        "toutes modifications qui me feraient plaisir",
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 83): [
        "vers la haine et l'obscurantisme",
    ],
    ('extraterrestrials-took-me-to-their-planet', 3, 2): [
        "font semblant de ne rien voir par peur de ce qu'ils ne connaissent pas",
    ],
    # === LWTE ===
    ('lets-welcome-the-extraterrestrials', 1, 28): [
        "rien n'est constant dans l'univers ni dans l'espace ni dans le temps",
    ],
    ('lets-welcome-the-extraterrestrials', 1, 85): [
        "un parti politique ne pèse pas lourd face aux messages des Elohim",
    ],
    ('lets-welcome-the-extraterrestrials', 1, 176): [
        "parfaitement adaptée à sa véritable personnalité",
        "le reflet exact du niveau de conscience de ceux qui les habitent",
    ],
    ('lets-welcome-the-extraterrestrials', 2, 59): [
        "le fruit d'une expérience ratée",
        "vous serez rapidement puissant et riche",
    ],
    ('lets-welcome-the-extraterrestrials', 3, 41): [
        "léger, moyen, fort ou très fort",
    ],
    ('lets-welcome-the-extraterrestrials', 3, 74): [
        "Il y a toujours une justice pour justifier les pires injustices",
    ],
    ('lets-welcome-the-extraterrestrials', 4, 88): [
        "là réside la vérité",
        "Comment s'aimer soi-même pour aimer vraiment les autres",
    ],
}


def main():
    for (book, chap, pn), anchors in FR_ANCHORS.items():
        path = LIB / book / f'chapter-{chap}.json'
        ch = json.loads(path.read_text())
        p = next(x for x in ch['paragraphs'] if x['n'] == pn)
        fr_text = p['text']
        L_fr = len(fr_text)

        print(f"\n('{book}', {chap}, {pn}): [")
        for split_idx, anchor in enumerate(anchors, start=1):
            print(f"    # split {split_idx}: anchor={anchor!r}")
            try:
                fr_sent, fr_end_pos = find_fr_sentence(fr_text, anchor)
            except ValueError as e:
                print(f"    # FR_ERROR: {e}")
                continue
            ratio = fr_end_pos / L_fr
            print("    {")
            print(f"        'fr': {json.dumps(fr_sent, ensure_ascii=False)},")
            for lang in ['en', 'de', 'es', 'ru', 'ja', 'ko', 'zh', 'zh-Hant']:
                text = p['i18n'][lang]
                target_pos = int(ratio * len(text))
                sent = find_lang_sentence(text, target_pos)
                # Check uniqueness
                if text.count(sent) != 1:
                    print(f"        # {lang}: NOT_UNIQUE count={text.count(sent)}")
                print(f"        '{lang}': {json.dumps(sent, ensure_ascii=False)},")
            print("    },")
        print("],")


if __name__ == '__main__':
    main()
