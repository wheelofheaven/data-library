#!/usr/bin/env python3
"""Attach the original Hebrew / Greek to the public-domain Bible editions.

The public-domain books (ASV 1901: `genesis`, `psalms`, `matthew`, …) carry the
English translation in `text`. This adds, per verse:

  original   the source text — Westminster Leningrad Codex (Sefaria "Tanach
             with Ta'amei Hamikra", public domain) for the Hebrew Bible, SBL
             Greek New Testament (© 2010 SBL and Logos, CC BY 4.0) for the NT
  translit   generated transliteration (hebrew_translit / script_translit.greek)
  text_lang  "arc" on the Aramaic passages (Dan 2:4b–7:28, Ezra 4:8–6:18,
             7:12–26, Jer 10:11); otherwise the book's language applies

English (KJV/ASV) and Hebrew versification differ in ~40 places; the shift
table below maps English chapter:verse to Hebrew. Psalm superscriptions, which
the Hebrew numbers as verse 1 (or 1–2) and the ASV leaves unnumbered, are not
attached to any English verse. Verses SBLGNT omits (Matt 17:21 …) get no Greek.

Usage: python3 scripts/add_pd_originals.py --sources <dir> [--dry-run] [slug ...]
  <dir> holds he/<slug>.json (Sefaria v3 whole-book responses) and
  grc/<slug>.txt (SBLGNT data/sblgnt/text/<Book>.txt).
"""
import argparse, glob, json, os, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from hebrew_translit import translit_text as he_translit
from script_translit import greek as grc_translit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (en_ch, en_v_from, en_v_to, he_ch, he_v_from): English verses shifted to Hebrew.
SHIFT = {
    'genesis': [(31, 55, 55, 32, 1), (32, 1, 32, 32, 2)],
    'exodus': [(20, 17, 26, 20, 14), (8, 1, 4, 7, 26), (8, 5, 32, 8, 1), (22, 1, 1, 21, 37), (22, 2, 31, 22, 1)],
    'leviticus': [(6, 1, 7, 5, 20), (6, 8, 30, 6, 1)],
    'numbers': [(16, 36, 50, 17, 1), (17, 1, 13, 17, 16), (29, 40, 40, 30, 1), (30, 1, 16, 30, 2)],
    'deuteronomy': [(5, 21, 33, 5, 18), (12, 32, 32, 13, 1), (13, 1, 18, 13, 2), (22, 30, 30, 23, 1), (23, 1, 25, 23, 2),
                    (29, 1, 1, 28, 69), (29, 2, 29, 29, 1)],
    '1-samuel': [(21, 1, 15, 21, 2), (23, 29, 29, 24, 1), (24, 1, 22, 24, 2)],
    '2-samuel': [(18, 33, 33, 19, 1), (19, 1, 43, 19, 2)],
    '1-kings': [(4, 21, 34, 5, 1), (5, 1, 18, 5, 15), (22, 44, 53, 22, 45)],
    '2-kings': [(11, 21, 21, 12, 1), (12, 1, 21, 12, 2)],
    '1-chronicles': [(6, 1, 15, 5, 27), (6, 16, 81, 6, 1), (12, 5, 40, 12, 6)],
    '2-chronicles': [(2, 1, 1, 1, 18), (2, 2, 18, 2, 1), (14, 1, 1, 13, 23), (14, 2, 15, 14, 1)],
    'nehemiah': [(7, 69, 73, 7, 68), (4, 1, 6, 3, 33), (4, 7, 23, 4, 1), (9, 38, 38, 10, 1), (10, 1, 39, 10, 2)],
    'job': [(41, 1, 8, 40, 25), (41, 9, 34, 41, 1)],
    'ecclesiastes': [(5, 1, 1, 4, 17), (5, 2, 20, 5, 1)],
    'song-of-solomon': [(6, 13, 13, 7, 1), (7, 1, 13, 7, 2)],
    'isaiah': [(9, 1, 1, 8, 23), (9, 2, 21, 9, 1), (64, 2, 12, 64, 1)],
    'jeremiah': [(9, 1, 1, 8, 23), (9, 2, 26, 9, 1)],
    'ezekiel': [(20, 45, 49, 21, 1), (21, 1, 32, 21, 6)],
    'daniel': [(4, 1, 3, 3, 31), (4, 4, 37, 4, 1), (5, 31, 31, 6, 1), (6, 1, 28, 6, 2)],
    'hosea': [(1, 10, 11, 2, 1), (2, 1, 23, 2, 3), (11, 12, 12, 12, 1), (12, 1, 14, 12, 2),
              (13, 16, 16, 14, 1), (14, 1, 9, 14, 2)],
    'joel': [(2, 28, 32, 3, 1), (3, 1, 21, 4, 1)],
    'jonah': [(1, 17, 17, 2, 1), (2, 1, 10, 2, 2)],
    'micah': [(5, 1, 1, 4, 14), (5, 2, 15, 5, 1)],
    'nahum': [(1, 15, 15, 2, 1), (2, 1, 13, 2, 2)],
    'zechariah': [(1, 18, 21, 2, 1), (2, 1, 13, 2, 5)],
    'malachi': [(4, 1, 6, 3, 19)],
}
# Hebrew verses that continue an English verse (English verse ← extra Hebrew verse).
MERGE = {
    '1-samuel': {(20, 42): [(21, 1)]},
    '1-kings': {(22, 43): [(22, 44)]},
    '1-chronicles': {(12, 4): [(12, 5)]},
}
# English verses with no separate Hebrew verse (their words sit in the previous one).
NO_SOURCE = {'isaiah': {(64, 1)}, 'nehemiah': {(7, 68)}}
# The Decalogue in the upper cantillation (ta'am elyon) joins four short
# commandments into one Hebrew verse; split it at sof pasuq back onto the
# four English verses: (en_ch, first_en_v, he_ch, he_v, parts).
DECALOGUE = {'exodus': (20, 13, 20, 13, 4), 'deuteronomy': (5, 17, 5, 17, 4)}


def decalogue_part(slug, c, v, he):
    d = DECALOGUE.get(slug)
    if not d or c != d[0] or not (d[1] <= v < d[1] + d[4]):
        return None
    parts = [p.strip() for p in re.split(r'(?<=׃)\s*(?:\(ס\))?\s*', he.get((d[2], d[3]), '')) if p.strip()]
    if len(parts) != d[4]:
        return None
    return parts[v - d[1]] + (' (ס)' if v - d[1] < d[4] - 1 else '')
ARAMAIC = {
    'daniel': lambda c, v: (c == 2 and v >= 4) or 3 <= c <= 7,
    'ezra': lambda c, v: (c == 4 and v >= 8) or c == 5 or (c == 6 and v <= 18) or (c == 7 and 12 <= v <= 26),
    'jeremiah': lambda c, v: c == 10 and v == 11,
}
# Greek: English verse → SBLGNT verse where the numbering differs.
GRC_SHIFT = {
    '3-john': {(1, 14): [(1, 14), (1, 15)]},
    '2-corinthians': {(13, 12): [(13, 12)], (13, 13): [], (13, 14): [(13, 13)]},
    'revelation': {(12, 17): [(12, 17), (12, 18)]},
}
SBL_SIGNS = re.compile('[⸀-⸃]')


def load_he(path):
    raw = json.load(open(path, encoding='utf-8'))['versions'][0]['text']
    return {(c + 1, v + 1): t.strip() for c, ch in enumerate(raw) for v, t in enumerate(ch) if t and t.strip()}


def load_grc(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^\S+ (\d+):(\d+)\t(.*)$', line.rstrip('\n'))
        if m:
            out[(int(m.group(1)), int(m.group(2)))] = re.sub(r'\s+', ' ', SBL_SIGNS.sub('', m.group(3))).strip()
    return out


def he_ref(slug, c, v, he):
    if (c, v) in NO_SOURCE.get(slug, ()):
        return []
    for ec, a, b, hc, hv in SHIFT.get(slug, []):
        if ec == c and a <= v <= b:
            return [(hc, hv + v - a)]
    if slug == 'psalms':
        return [(c, v + psalm_offset(c, he))]
    refs = [(c, v)]
    refs += MERGE.get(slug, {}).get((c, v), [])
    return refs


_ps_en_counts = {}


def psalm_offset(c, he):
    he_n = max((v for (hc, v) in he if hc == c), default=0)
    return max(0, he_n - _ps_en_counts.get(c, he_n))


def verses(book):
    meta = json.load(open(f'{ROOT}/{book}/_meta.json', encoding='utf-8'))
    for ci in meta['chapterFiles']:
        p = f"{ROOT}/{book}/{ci['file']}"
        yield p, json.load(open(p, encoding='utf-8'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sources', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('slugs', nargs='*')
    a = ap.parse_args()
    jobs = []
    for f in sorted(glob.glob(f'{a.sources}/he/*.json')):
        jobs.append((os.path.basename(f)[:-5], 'he', f))
    for f in sorted(glob.glob(f'{a.sources}/grc/*.txt')):
        jobs.append((os.path.basename(f)[:-4], 'grc', f))
    grand = Counter()
    for slug, lang, src in jobs:
        if a.slugs and slug not in a.slugs:
            continue
        source = load_he(src) if lang == 'he' else load_grc(src)
        chapters = list(verses(slug))
        if slug == 'psalms':
            for _, ch in chapters:
                _ps_en_counts[ch['n']] = len(ch['paragraphs'])
        used = Counter(); missing = []; filled = 0
        for path, ch in chapters:
            c = ch['n']
            for v in ch['paragraphs']:
                n = v['n']
                single = len(ch['paragraphs']) == 1
                if single:
                    # whole chapter stored as one paragraph (single-chapter books)
                    refs = sorted(k for k in source if k[0] == c)
                elif lang == 'he':
                    refs = he_ref(slug, c, n, source)
                else:
                    refs = GRC_SHIFT.get(slug, {}).get((c, n), [(c, n)])
                dec = decalogue_part(slug, c, n, source) if lang == 'he' and not single else None
                if dec is not None:
                    refs = [(DECALOGUE[slug][2], DECALOGUE[slug][3])]
                parts = [dec] if dec is not None else [source[r] for r in refs if r in source]
                for r in refs:
                    if r in source:
                        used[r] += 1
                if not parts:
                    missing.append(f'{c}:{n}')
                    for k in ('original', 'translit', 'text_lang'):
                        v.pop(k, None)
                    continue
                orig = ' '.join(parts)
                v['original'] = orig
                v['translit'] = he_translit(orig) if lang == 'he' else grc_translit(orig)
                if lang == 'he' and ARAMAIC.get(slug, lambda *_: False)(c, n):
                    v['text_lang'] = 'arc'
                else:
                    v.pop('text_lang', None)
                filled += 1
            if not a.dry_run:
                with open(path, 'w', encoding='utf-8') as fh:
                    json.dump(ch, fh, ensure_ascii=False, indent=2); fh.write('\n')
        unused = sorted(k for k in source if used[k] == 0)
        dec_src = (DECALOGUE[slug][2], DECALOGUE[slug][3]) if lang == 'he' and slug in DECALOGUE else None
        dup = sorted(k for k, n in used.items() if n > 1 and k != dec_src)
        if slug == 'psalms':  # superscriptions are expected to be unused
            unused = [k for k in unused if k[1] > psalm_offset(k[0], source)]
        grand['filled'] += filled; grand['missing'] += len(missing)
        flag = '' if not (missing or unused or dup) else '  <-- check'
        print(f'{slug:18} {lang} filled={filled:5} missing={len(missing):3} unused-src={len(unused):3} dup={len(dup)}{flag}')
        if missing:
            print('   missing:', ' '.join(missing[:12]))
        if unused:
            print('   unused :', ' '.join(f'{c}:{v}' for c, v in unused[:12]))
    print(dict(grand))


if __name__ == '__main__':
    main()
