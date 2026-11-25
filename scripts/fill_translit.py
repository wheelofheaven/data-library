#!/usr/bin/env python3
"""Fill missing `translit` fields from the original script, per verse.

Never overwrites an existing transliteration. Dispatches on the script of
`text`: Hebrew → hebrew_translit, Ethiopic → geez, Coptic → coptic.
Usage: python3 scripts/fill_translit.py [--dry-run] [slug ...]
"""
import argparse, glob, json, os, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from hebrew_translit import translit_text as hebrew
from script_translit import geez, coptic, greek

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def script_of(s):
    for ch in s:
        n = unicodedata.name(ch, '')
        if n.startswith('HEBREW LETTER'):
            return 'he'
        if n.startswith('ETHIOPIC SYLLABLE'):
            return 'gez'
        if n.startswith('COPTIC') or 'COPTIC' in n:
            return 'cop'
        if n.startswith('GREEK'):
            return 'grc'
    return None


CONV = {'he': hebrew, 'gez': geez, 'cop': coptic, 'grc': greek}


def verses(j):
    for key in ('paragraphs', 'lines'):
        for v in j.get(key) or []:
            yield v
    for g in (j.get('segments') or []) + (j.get('tablets') or []):
        for v in g.get('lines') or []:
            yield v


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dry-run', action='store_true'); ap.add_argument('slugs', nargs='*')
    a = ap.parse_args()
    books = a.slugs or sorted(os.path.basename(d) for d in glob.glob(f'{ROOT}/*-woh'))
    for b in books:
        filled = mism = 0; by = {}
        for f in sorted(glob.glob(f'{ROOT}/{b}/*.json')):
            fn = os.path.basename(f)
            if fn.startswith(('_', 'source')) or 'diff' in fn:
                continue
            j = json.load(open(f, encoding='utf-8'))
            if not isinstance(j, dict):
                continue
            changed = False
            for v in verses(j):
                if not isinstance(v, dict) or (v.get('translit') or '').strip():
                    continue
                t = (v.get('text') or '').strip()
                sc = script_of(t)
                if not sc:
                    continue
                tr = CONV[sc](t)
                if len(tr.split()) != len(t.split()):
                    mism += 1
                v['translit'] = tr; filled += 1; by[sc] = by.get(sc, 0) + 1; changed = True
            if changed and not a.dry_run:
                with open(f, 'w', encoding='utf-8') as fh:
                    json.dump(j, fh, ensure_ascii=False, indent=2); fh.write('\n')
        if filled:
            print(f'{b:28} filled={filled} {by} token-mismatch={mism}')


if __name__ == '__main__':
    main()
