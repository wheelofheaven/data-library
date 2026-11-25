#!/usr/bin/env python3
"""Deterministic script conversions for the WoH library interlinear.

geez(text)    Ethiopic (Ge'ez) → Latin transliteration. First order a, sixth
              order ə (dropped word-finally), labiovelars with ʷ, Ethiopic
              numerals → digits, word divider ፡ dropped. Gemination is not
              written in the script and so is not marked.
coptic(text)  Sahidic Coptic → Latin (Layton-style): ϣ š, ϥ f, ϩ h, ϫ j, ϭ c,
              ϯ ti, ⲏ ē, ⲱ ō, ⲑ th, ⲫ ph, ⲭ kh, ⲯ ps, ⲝ ks; the supralinear
              stroke is kept as a macron on the letter it marks.
avestan(text) avesta.org (Geldner-style) Latin transliteration → Avestan script.
              Derived, not a manuscript reading: š/ṣ̌/š́ and t/t̰ are not
              distinguished by the source and default to š and t.
Each function preserves the space-delimited token count.
"""
import re
import unicodedata

# ---------------------------------------------------------------- Ge'ez
_GEEZ_CONS = {
    'H': 'h', 'L': 'l', 'HH': 'ḥ', 'M': 'm', 'SZ': 'ś', 'R': 'r', 'S': 's', 'SH': 'š',
    'Q': 'q', 'QH': 'q̱', 'B': 'b', 'V': 'v', 'T': 't', 'C': 'č', 'X': 'ḫ', 'N': 'n',
    'NY': 'ñ', 'GLOTTAL': 'ʾ', 'K': 'k', 'KX': 'x', 'W': 'w', 'PHARYNGEAL': 'ʿ',
    'Z': 'z', 'ZH': 'ž', 'Y': 'y', 'D': 'd', 'DD': 'ḍ', 'J': 'ǧ', 'G': 'g', 'GG': 'ŋ',
    'TH': 'ṭ', 'CH': 'č̣', 'PH': 'p̣', 'TS': 'ṣ', 'TZ': 'ḍ', 'F': 'f', 'P': 'p',
}
_GEEZ_VOW = {'A': 'a', 'U': 'u', 'I': 'i', 'AA': 'ā', 'EE': 'ē', 'E': 'ə', 'O': 'o', 'OA': 'ʷā'}
_ETH_DIGITS = {chr(0x1369 + i): str(i + 1) for i in range(9)}
_ETH_DIGITS.update({'፲': '10', '፳': '20', '፴': '30', '፵': '40', '፶': '50', '፷': '60',
                    '፸': '70', '፹': '80', '፺': '90', '፻': '100', '፼': '10000'})


def _geez_syl(ch):
    n = unicodedata.name(ch, '')
    if not n.startswith('ETHIOPIC SYLLABLE '):
        return None
    rest = n[len('ETHIOPIC SYLLABLE '):]
    parts = rest.split()
    if parts[0] in ('GLOTTAL', 'PHARYNGEAL'):
        cons, vow = parts[0], parts[1]
    else:
        word = parts[0]
        m = re.match(r'^([B-DF-HJ-NP-TV-Z]+?)(W?)(AA|EE|OA|A|U|I|E|O)$', word)
        if not m:
            return None
        cons, labio, vow = m.group(1), m.group(2), m.group(3)
        if labio:
            c = _GEEZ_CONS.get(cons, cons.lower())
            return c + 'ʷ', _GEEZ_VOW.get(vow, vow.lower())
    return _GEEZ_CONS.get(cons, cons.lower()), _GEEZ_VOW.get(vow, vow.lower())


def geez(text):
    out = []
    for tok in text.split():
        syls = []
        buf = ''
        for ch in tok:
            if ch in '፡':
                continue
            if ch in _ETH_DIGITS:
                buf += _ETH_DIGITS[ch]; continue
            s = _geez_syl(ch)
            if s:
                syls.append(s); continue
            if ch == '።':
                buf += '.'; continue
            if ch == '፣':
                buf += ','; continue
            syls.append((ch, ''))
        # Sixth order: zero when it closes a syllable. Decide right to left:
        # word-final → zero; otherwise zero iff the next syllable has a real
        # vowel (so no consonant cluster forms mid-word); word-initial keeps ə.
        vs = [v for _, v in syls]
        for i in range(len(syls) - 1, -1, -1):
            if vs[i] != 'ə':
                continue
            if i == len(syls) - 1:
                vs[i] = ''
            elif i > 0 and vs[i + 1] != '':
                vs[i] = ''
        word = ''.join(c + v for (c, _), v in zip(syls, vs))
        out.append((word + buf) if word else (buf or tok))
    return ' '.join(out)


# ---------------------------------------------------------------- Coptic
_COPTIC = {
    'ⲁ': 'a', 'ⲃ': 'b', 'ⲅ': 'g', 'ⲇ': 'd', 'ⲉ': 'e', 'ⲍ': 'z', 'ⲏ': 'ē', 'ⲑ': 'th',
    'ⲓ': 'i', 'ⲕ': 'k', 'ⲗ': 'l', 'ⲙ': 'm', 'ⲛ': 'n', 'ⲝ': 'ks', 'ⲟ': 'o', 'ⲡ': 'p',
    'ⲣ': 'r', 'ⲥ': 's', 'ⲧ': 't', 'ⲩ': 'u', 'ⲫ': 'ph', 'ⲭ': 'kh', 'ⲯ': 'ps', 'ⲱ': 'ō',
    'ϣ': 'š', 'ϥ': 'f', 'ϧ': 'x', 'ϩ': 'h', 'ϫ': 'j', 'ϭ': 'c', 'ϯ': 'ti', 'ⳁ': '900',
}
_STROKE = {'̄', '̅', '︤', '︥', '︦'}
_DROP = {'⳯', '⳿'}


def coptic(text):
    out = []
    for tok in text.split():
        s = ''
        for ch in unicodedata.normalize('NFD', tok):
            low = ch.lower()
            if low in _COPTIC:
                s += _COPTIC[low]
            elif ch in _STROKE:
                if s and not s.endswith('̄'):
                    s += '̄'
            elif ch in _DROP:
                continue
            else:
                s += ch
        out.append(unicodedata.normalize('NFC', s) or tok)
    return ' '.join(out)


# ---------------------------------------------------------------- Avestan
_AV = {
    'a': '\U00010B00', 'â': '\U00010B01', 'å': '\U00010B03', 'ã': '\U00010B04',
    'e': '\U00010B06', 'ê': '\U00010B07', 'o': '\U00010B0A', 'ô': '\U00010B0B',
    'i': '\U00010B0C', 'î': '\U00010B0D', 'u': '\U00010B0E', 'û': '\U00010B0F',
    'k': '\U00010B10', 'x': '\U00010B11', 'hv': '\U00010B13', 'g': '\U00010B14',
    'gh': '\U00010B16', 'c': '\U00010B17', 'j': '\U00010B18', 't': '\U00010B19',
    'th': '\U00010B1A', 'd': '\U00010B1B', 'dh': '\U00010B1C', 'p': '\U00010B1E',
    'f': '\U00010B1F', 'b': '\U00010B20', 'w': '\U00010B21', 'ng': '\U00010B22',
    'n': '\U00010B25', 'ñ': '\U00010B27', 'm': '\U00010B28', 'ý': '\U00010B2A',
    'y': '\U00010B2B', 'v': '\U00010B2C', 'r': '\U00010B2D', 's': '\U00010B2F',
    'z': '\U00010B30', 'sh': '\U00010B31', 'zh': '\U00010B32', 'h': '\U00010B35',
}
_AV_EE = '\U00010B09'  # ē, in the diphthong aē
_AV_TOKEN = re.compile(r'ngh|ng(?=h)|sh|zh|th|dh|gh|hv|[a-zâãåêîñôûý]')


def avestan(text):
    out = []
    for tok in text.split():
        res = ''
        prev = ''
        for m in _AV_TOKEN.finditer(tok.lower()):
            pass
        i = 0
        low = tok.lower()
        while i < len(low):
            m = _AV_TOKEN.match(low, i)
            if not m:
                res += low[i]; i += 1; prev = ''; continue
            g = m.group(0)
            if g == 'ngh':
                res += _AV['ng'] + _AV['h']
            elif g == 'ê' and prev == 'a':
                res += _AV_EE
            else:
                res += _AV[g]
            prev = g
            i = m.end()
        out.append(res)
    return ' '.join(out)


if __name__ == '__main__':
    print(geez('ወበ፫ ሰቡዕ፡ ለዝንቱ፡ ኢዮቤልዉ፡ ተከለ፡ ኖኅ፡ ወይነ፡ በደብር፡'))
    print(coptic('ⲁⲩⲱ ⲡⲉϫⲁϥ ϫⲉⲡⲉⲧⲁϩⲉ ⲉⲑⲉⲣⲙⲏⲛⲉⲓⲁ ⲛⲛⲉⲉⲓϣⲁϫⲉ ϥⲛⲁϫⲓϯⲡⲉ ⲁⲛ ⲙ̄ⲡⲙⲟⲩ ·'))
    print(avestan('peresat zarathushtrô ahurem mazdãm, ahura mazda mainyô spênishta gaêthanãm hvãthwâi vîvanghana'))


# ---------------------------------------------------------------- Greek
_GR = {'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'ē', 'θ': 'th',
       'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x', 'ο': 'o', 'π': 'p',
       'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'y', 'φ': 'ph', 'χ': 'ch', 'ψ': 'ps',
       'ω': 'ō'}
_ROUGH = '̔'


def greek(text):
    """SBL-style Greek transliteration (y, but u in au/eu/ou/ēu/ui; h for rough breathing)."""
    out = []
    for tok in text.split():
        chars = []  # (base_lower, is_upper, rough)
        for ch in unicodedata.normalize('NFD', tok):
            if unicodedata.category(ch) == 'Mn':
                if ch == _ROUGH and chars:
                    chars[-1][2] = True
                continue
            chars.append([ch.lower(), ch != ch.lower(), False])
        s = ''
        for i, (c, up, rough) in enumerate(chars):
            prev = chars[i - 1][0] if i else ''
            nxt = chars[i + 1][0] if i + 1 < len(chars) else ''
            if c in _GR:
                t = _GR[c]
                if c == 'υ' and prev in ('α', 'ε', 'ο', 'η'):
                    t = 'u'
                if c == 'γ' and nxt in ('γ', 'κ', 'ξ', 'χ'):
                    t = 'n'
                # rough breathing sits on the second vowel of a diphthong
                rough_here = rough or (nxt in ('ι', 'υ') and i + 1 < len(chars) and chars[i + 1][2] and c in 'αεοηυ')
                diphthong_second = (c in ('ι', 'υ') and prev in ('α', 'ε', 'ο', 'η', 'υ') and rough)
                if c == 'ρ' and rough:
                    t = 'rh'
                elif rough_here and c != 'ρ' and not diphthong_second:
                    t = 'h' + t
                if up:
                    t = t[0].upper() + t[1:]
                s += t
            else:
                s += c
        out.append(s)
    return ' '.join(out)


# ---------------------------------------------------------------- Sanskrit
_DEV_V = {'अ': 'a', 'आ': 'ā', 'इ': 'i', 'ई': 'ī', 'उ': 'u', 'ऊ': 'ū', 'ऋ': 'ṛ', 'ॠ': 'ṝ',
          'ऌ': 'ḷ', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au'}
_DEV_M = {'ा': 'ā', 'ि': 'i', 'ी': 'ī', 'ु': 'u', 'ू': 'ū', 'ृ': 'ṛ', 'ॄ': 'ṝ', 'ॢ': 'ḷ',
          'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au'}
_DEV_C = {'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ṅ', 'च': 'c', 'छ': 'ch', 'ज': 'j',
          'झ': 'jh', 'ञ': 'ñ', 'ट': 'ṭ', 'ठ': 'ṭh', 'ड': 'ḍ', 'ढ': 'ḍh', 'ण': 'ṇ', 'त': 't',
          'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n', 'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh',
          'म': 'm', 'य': 'y', 'र': 'r', 'ल': 'l', 'ळ': 'ḷ', 'व': 'v', 'श': 'ś', 'ष': 'ṣ',
          'स': 's', 'ह': 'h'}
_DEV_SIGN = {'ं': 'ṃ', 'ः': 'ḥ', 'ँ': 'm̐', 'ऽ': "'", 'ॐ': 'oṃ'}
_DEV_DIG = {chr(0x0966 + i): str(i) for i in range(10)}
_DEV_SKIP = {'॑', '॒', '᳚', '‌', '‍', 'ꣳ'}  # Vedic accents, joiners


def sanskrit(text):
    """Devanagari (incl. Vedic) → IAST; Vedic accent marks are dropped."""
    out = []
    for tok in text.split():
        s = ''
        chars = [c for c in unicodedata.normalize('NFC', tok) if c not in _DEV_SKIP and not (0x1CD0 <= ord(c) <= 0x1CFF)]
        for i, c in enumerate(chars):
            nxt = chars[i + 1] if i + 1 < len(chars) else ''
            if c in _DEV_C:
                s += _DEV_C[c]
                if nxt not in _DEV_M and nxt != '्' and nxt != '़':
                    s += 'a'
            elif c in _DEV_M:
                s += _DEV_M[c]
            elif c == '्' or c == '़':
                continue
            elif c in _DEV_V:
                s += _DEV_V[c]
            elif c in _DEV_SIGN:
                s += _DEV_SIGN[c]
            elif c in _DEV_DIG:
                s += _DEV_DIG[c]
            elif c == '।':
                s += '|'
            elif c == '॥':
                s += '||'
            else:
                s += c
        out.append(s)
    return ' '.join(out)
