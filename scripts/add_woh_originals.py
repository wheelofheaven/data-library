#!/usr/bin/env python3
"""Attach originals from the WoH apparatus to Charles's Enoch and Jubilees.

Charles's paragraphs (`book-of-enoch`, `book-of-jubilees`) each start at a verse
(refId `1ENO-1:4`) and run to the verse before the next paragraph. The WoH
books (`book-of-enoch-woh`, `jubilees-woh`, CC0) carry the reconstructed
original per verse with `text_lang` (Aramaic, Greek, Ge'ez, Hebrew) and a
transliteration. A paragraph gets `original`/`translit`/`text_lang` only when
every verse of its range is present and all share one language — a mixed-
witness paragraph would put right-to-left and left-to-right text in one row.

Usage: python3 scripts/add_woh_originals.py [--dry-run]
"""
import argparse, json, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = [('book-of-enoch', 'book-of-enoch-woh'), ('book-of-jubilees', 'jubilees-woh')]


def woh_verses(book):
    meta = json.load(open(f'{ROOT}/{book}/_meta.json', encoding='utf-8'))
    out = {}
    for ci in meta['chapterFiles']:
        ch = json.load(open(f"{ROOT}/{book}/{ci['file']}", encoding='utf-8'))
        for v in ch['paragraphs']:
            if (v.get('text') or '').strip():
                out[(ch['n'], int(v['n']))] = v
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    for pd, woh in PAIRS:
        src = woh_verses(woh)
        meta = json.load(open(f'{ROOT}/{pd}/_meta.json', encoding='utf-8'))
        st = Counter()
        for ci in meta['chapterFiles']:
            path = f"{ROOT}/{pd}/{ci['file']}"
            ch = json.load(open(path, encoding='utf-8'))
            c = ch['n']
            starts = []
            for p in ch['paragraphs']:
                m = re.search(r':(\d+)$', p.get('refId', ''))
                starts.append(int(m.group(1)) if m else None)
            last_v = max((v for (cc, v) in src if cc == c), default=0)
            for i, p in enumerate(ch['paragraphs']):
                for k in ('original', 'translit', 'text_lang'):
                    p.pop(k, None)
                s = starts[i]
                if s is None or not any(cc == c for (cc, _) in src):
                    st['no-source'] += 1; continue
                e = (starts[i + 1] - 1) if i + 1 < len(starts) and starts[i + 1] else last_v
                rng = [src.get((c, v)) for v in range(s, e + 1)]
                if not rng or any(x is None for x in rng):
                    st['gap'] += 1; continue
                langs = {x.get('text_lang') for x in rng}
                if len(langs) != 1:
                    st['mixed-language'] += 1; continue
                p['original'] = ' '.join(x['text'].strip() for x in rng)
                tr = [x.get('translit', '').strip() for x in rng]
                if all(tr):
                    p['translit'] = ' '.join(tr)
                lang = langs.pop()
                if lang:
                    p['text_lang'] = lang
                st['filled'] += 1
            if not a.dry_run:
                with open(path, 'w', encoding='utf-8') as fh:
                    json.dump(ch, fh, ensure_ascii=False, indent=2); fh.write('\n')
        print(pd, dict(st))


if __name__ == '__main__':
    main()
