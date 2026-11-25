#!/usr/bin/env python3
"""Attach the Sanskrit original to Griffith's Rig Veda, Book 10.

Source: Sanskrit Wikisource, one page per hymn ("ऋग्वेदः सूक्तं १०.N"),
transcription CC BY-SA 4.0 (the Vedic text itself is public domain).
Griffith's English stores each verse as a numbered paragraph ("1. HIGH hath
…") plus a continuation paragraph for its second half. Sanskrit verses end in
॥N॥ and are written as two half-lines; when a verse has as many half-lines as
Griffith has paragraphs they pair one to one, otherwise the whole verse sits on
the numbered paragraph. IAST transliteration via script_translit.sanskrit.

Usage: python3 scripts/add_rv_originals.py --sources <dir-with-N.json> [--dry-run]
"""
import argparse, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from script_translit import sanskrit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = 'rig-veda-book-10'
DIG = str.maketrans('०१२३४५६७८९', '0123456789')


def sa_verses(wikitext):
    # The continuous text can span several <poem> blocks (10.16); later blocks
    # without verse markers are commentary. First occurrence of a verse wins.
    blocks = re.findall(r'<poem>(.*?)</poem>', wikitext, re.S) or [wikitext]
    body = '\n'.join(blocks)
    body = re.sub(r'<[^>]+>', '', body)
    body = re.sub(r'\{\{[^}]*\}\}', '', body)
    verses = {}
    for chunk in re.finditer(r'(.*?)॥\s*([०-९0-9]+)\s*॥', body, re.S):
        n = int(chunk.group(2).translate(DIG))
        lines = [l.strip() for l in chunk.group(1).strip().split('\n') if l.strip()]
        verses.setdefault(n, lines)
    return verses


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--sources', required=True); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    meta = json.load(open(f'{ROOT}/{BOOK}/_meta.json', encoding='utf-8'))
    tot = pairs = whole = 0; issues = []
    for ci in meta['chapterFiles']:
        path = f"{ROOT}/{BOOK}/{ci['file']}"
        ch = json.load(open(path, encoding='utf-8'))
        hymn = ch['n']
        src = json.load(open(f"{a.sources}/{hymn}.json", encoding='utf-8'))
        sv = sa_verses(src['wikitext'])
        groups = {}; cur = None
        for p in ch['paragraphs']:
            m = re.match(r'^\s*(\d+)\.\s', p['text'])
            if m:
                cur = int(m.group(1)); groups[cur] = [p]
            elif cur is not None:
                groups[cur].append(p)
        if set(groups) != set(sv):
            issues.append(f'{hymn}: en verses {len(groups)} vs sa {len(sv)}')
        for n, ps in groups.items():
            lines = sv.get(n)
            for p in ps:
                for k in ('original', 'translit'):
                    p.pop(k, None)
            if not lines:
                continue
            tot += 1
            if len(lines) == len(ps):
                for p, l in zip(ps, lines):
                    p['original'] = l; p['translit'] = sanskrit(l)
                pairs += 1
            else:
                l = ' '.join(lines)
                ps[0]['original'] = l; ps[0]['translit'] = sanskrit(l)
                whole += 1
        if not a.dry_run:
            with open(path, 'w', encoding='utf-8') as fh:
                json.dump(ch, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f'verses={tot} half-line-paired={pairs} whole-verse={whole} hymns-with-count-mismatch={len(issues)}')
    for i in issues[:20]:
        print('  ', i)


if __name__ == '__main__':
    main()
