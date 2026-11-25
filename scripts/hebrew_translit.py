#!/usr/bin/env python3
"""Rule-based transliteration of pointed Tiberian Hebrew (WLC / Sefaria text).

Scheme (documented in each book's _meta as `translitScheme`):
SBL academic consonants (ʾ b g d h w z ḥ ṭ y k l m n s ʿ p ṣ q r š ś t), no
spirantization marks; long vowels with macrons (ā ē ī ō ū), short a e i o u,
reduced ă ĕ ŏ ə; dagesh forte written as a doubled consonant; vocal shewa ə,
silent shewa unwritten; furtive patah before its guttural; qamets qatan o by
heuristic; the divine name יהוה as YHWH. One output token per space-separated
Hebrew token (maqqef → hyphen), so the reader's word-pair interlinear aligns.
Ketiv (unpointed) → bare consonants; [qere] keeps its brackets; (ס)/(פ) → (s)/(p);
paseq ׀ → |.

This is a machine transliteration. It is consistent, not infallible: shewa
and qamets-qatan decisions are heuristic.
"""
import re
import unicodedata

CONS = {
    'א': 'ʾ', 'ב': 'b', 'ג': 'g', 'ד': 'd', 'ה': 'h', 'ו': 'w', 'ז': 'z', 'ח': 'ḥ',
    'ט': 'ṭ', 'י': 'y', 'כ': 'k', 'ך': 'k', 'ל': 'l', 'מ': 'm', 'ם': 'm', 'נ': 'n',
    'ן': 'n', 'ס': 's', 'ע': 'ʿ', 'פ': 'p', 'ף': 'p', 'צ': 'ṣ', 'ץ': 'ṣ', 'ק': 'q',
    'ר': 'r', 'ש': 'š', 'ת': 't',
}
SHEVA, HPATAH, HSEGOL, HQAMATS = 'ְ', 'ֲ', 'ֱ', 'ֳ'
HIRIQ, TSERE, SEGOL, PATAH, QAMATS, HOLAM, HOLAM_V, QUBUTS = (
    'ִ', 'ֵ', 'ֶ', 'ַ', 'ָ', 'ֹ', 'ֺ', 'ֻ')
QAMATS_QATAN = 'ׇ'
DAGESH, METEG, RAFE, SHIN_DOT, SIN_DOT = 'ּ', 'ֽ', 'ֿ', 'ׁ', 'ׂ'
VOWELS = {HIRIQ: 'i', TSERE: 'ē', SEGOL: 'e', PATAH: 'a', QAMATS: 'ā', HOLAM: 'ō',
          QUBUTS: 'u', HPATAH: 'ă', HSEGOL: 'ĕ', HQAMATS: 'ŏ', QAMATS_QATAN: 'o'}
FULL = {HIRIQ, TSERE, SEGOL, PATAH, QAMATS, HOLAM, QUBUTS, QAMATS_QATAN}
LONG = {TSERE, QAMATS, HOLAM}
GUTT_FURTIVE = {'ח', 'ע', 'ה'}


def is_accent(c):
    return 0x0591 <= ord(c) <= 0x05AF


def parse(word):
    """Split a pointed word into letters: dicts with base, marks."""
    out = []
    for c in unicodedata.normalize('NFD', word):
        if 'א' <= c <= 'ת':
            out.append({'b': c, 'v': None, 'dag': False, 'sin': False, 'acc': False,
                        'met': False, 'holam_v': False})
        elif not out:
            continue
        else:
            L = out[-1]
            if c in VOWELS or c == SHEVA:
                if c == HOLAM_V:
                    L['holam_v'] = True
                    L['v'] = HOLAM
                elif L['v'] is None or L['v'] == SHEVA:
                    L['v'] = c
                elif c == HIRIQ and L['v'] in FULL:
                    L['v2'] = HIRIQ  # yərūšālayim
            elif c == DAGESH:
                L['dag'] = True
            elif c == SIN_DOT:
                L['sin'] = True
            elif c == METEG:
                L['met'] = True
            elif is_accent(c):
                L['acc'] = True
    return out


def translit_word(word):
    if not any('א' <= c <= 'ת' for c in word):
        return word
    letters = parse(word)
    cons_only = ''.join(L['b'] for L in letters)
    pointed = any(L['v'] or L['dag'] for L in letters)
    if not pointed:  # ketiv: bare consonants
        return ''.join(CONS[L['b']] if not (L['b'] == 'ש' and L['sin']) else 'ś' for L in letters)
    # divine name, possibly with prefixes
    m = re.search('יהוה$', cons_only)
    if m and m.start() <= 2:
        pre = translit_letters(letters[:m.start()]) if m.start() else ''
        return pre + 'YHWH'
    return translit_letters(letters)


def translit_letters(letters):
    n = len(letters)
    # Pass 1: mark matres lectionis and vowel letters.
    for i, L in enumerate(letters):
        L['skip'] = False
        L['vowel_out'] = None
    for i, L in enumerate(letters):
        prev = letters[i - 1] if i else None
        if L['b'] == 'ו':
            prev_novowel = prev is None or prev['v'] is None
            if L['dag'] and L['v'] is None and (prev_novowel or i == 0):
                L['skip'] = True
                if prev is not None and prev['v'] is None:
                    prev['vowel_out'] = 'ū'
                else:
                    L['skip'] = False
                    L['shureq_alone'] = True
                continue
            if L['v'] == HOLAM and not L['holam_v'] and prev is not None and prev['v'] is None:
                L['skip'] = True
                prev['vowel_out'] = 'ō'
                continue
        if L['b'] == 'י' and L['v'] is None and not L['dag'] and prev is not None:
            if prev['v'] == HIRIQ:
                L['skip'] = True; prev['vowel_out'] = 'ī'; continue
            if prev['v'] in (TSERE, SEGOL):
                L['skip'] = True; prev['vowel_out'] = 'ē'; continue
    out = []
    prev_vowel = False      # previous (non-skipped) letter carried a full/reduced vowel
    prev_shva_silent = False
    prev_long = False
    for i, L in enumerate(letters):
        if L['skip']:
            continue
        b = L['b']
        if L.get('shureq_alone'):
            out.append('ū'); prev_vowel = True; prev_shva_silent = False; prev_long = True; continue
        c = 'ś' if (b == 'ש' and L['sin']) else CONS[b]
        final = i == n - 1 or all(x['skip'] for x in letters[i + 1:])
        # dagesh: forte (double) after a vowel inside the word; mappiq on final he
        forte = L['dag'] and i > 0 and prev_vowel and not (b == 'ה' and final)
        cons = c * 2 if forte else c
        v = L['v']
        vo = L['vowel_out']
        # furtive patah
        if final and v == PATAH and b in GUTT_FURTIVE and i > 0 and (prev_vowel or letters[i - 1]['skip']) and vo is None:
            if b != 'ה' or L['dag']:
                out.append('a' + cons); prev_vowel = True; continue
        if b == 'א' and v is None and vo is None and not final:
            out.append(cons)  # quiescent aleph: keeps the preceding vowel's syllable open
            prev_shva_silent = False
            continue
        if vo:
            vtxt = vo
        elif v == SHEVA:
            vocal = (i == 0 or forte or (prev_shva_silent and not final)
                     or prev_long)
            if final:
                vocal = False
            vtxt = 'ə' if vocal else ''
        elif v == QAMATS:
            vtxt = 'o' if qamets_qatan(letters, i) else 'ā'
        elif v:
            vtxt = VOWELS[v]
        else:
            vtxt = ''
        if L.get('v2'):
            vtxt += 'yi'
        out.append(cons + vtxt)
        prev_shva_silent = (v == SHEVA and vtxt == '') or (v is None and vo is None and not final)
        prev_vowel = bool(vtxt) and vtxt != ''
        prev_long = vtxt in ('ā', 'ē', 'ī', 'ō', 'ū')
    return ''.join(out)


QATAN_STEMS = ('חכמ', 'קדש', 'אזנ', 'שרש', 'אכל', 'גדל', 'עזנ', 'תמ', 'ערל', 'אהל')


def qamets_qatan(letters, i):
    """Heuristic qamets qatan (short o). Defaults to long ā."""
    L = letters[i]
    if L['met'] or L['acc']:
        return False
    rest = [x for x in letters[i + 1:] if not x['skip']]
    if not rest:
        return False
    nxt = rest[0]
    if nxt['v'] == HQAMATS:
        return True
    word_accented = any(x['acc'] or x['met'] for x in letters)
    if len(rest) == 1 and rest[0]['b'] in ('ה', 'א') and not rest[0]['dag']:
        return False
    # unaccented maqqef word ending in a closed syllable: kol-, ḥoq-
    if nxt['v'] is None and len(rest) == 1 and not word_accented:
        return True
    # short wayyiqtol: wayyāqom, wayyāmot — final closed syllable, accent earlier
    if (len(rest) == 1 and nxt['v'] is None and word_accented and len(letters) >= 4
            and letters[0]['b'] == 'ו' and letters[0]['v'] == PATAH and letters[1]['dag']
            and not any(x['acc'] for x in letters[i:])):
        return True
    # lexical closed-syllable stems: ḥokmāh, qodš-, ʾozn-, šorš-, ʾokl-
    cons = ''.join(x['b'] for x in letters[i:] if not x['skip'])[:3]
    if nxt['v'] == SHEVA and any(cons.startswith(s) for s in QATAN_STEMS):
        return True
    return False


def translit_text(text):
    toks = []
    for tok in text.split():
        if tok in ('(ס)', '(פ)'):
            toks.append('(s)' if 'ס' in tok else '(p)'); continue
        if tok.strip('[]') == '׀':
            toks.append(tok.replace('׀', '|')); continue
        lead = tok[0] if tok[0] in '[(' else ''
        trail = tok[-1] if tok[-1] in '])' else ''
        core = tok[len(lead):len(tok) - len(trail)] if trail else tok[len(lead):]
        core = core.replace('׃', '').replace('׀', '').replace('‍', '').replace('ׄ', '')
        parts = [translit_word(p) for p in core.split('־') if p != '']
        toks.append(lead + '-'.join(parts) + trail)
    return ' '.join(toks)


if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        print(translit_text(line.strip()))
