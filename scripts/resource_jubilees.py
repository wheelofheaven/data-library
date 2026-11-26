#!/usr/bin/env python3
"""Re-source jubilees-woh's original from VanderKam's Ge'ez edition.

Source: Beta maṣāḥǝft LIT1697Jubilees.xml, edition `Ran` — Ran HaCohen's
transcription of VanderKam, The Book of Jubilees: A Critical Text (CSCO 510,
1989); CC BY-SA 4.0. The transcription sometimes runs several verses into one
<l>, with the later verse numbers inline ("… 10 ወይትሐጐሉ …"); those are split
so every verse stands alone.

Writes every chapter to jubilees-woh/vanderkam/geez-N.json — the source for
re-translating chapters 1–12 (whose English followed a model-written
reconstruction; see _meta.sourceIntegrityNote) and translating 13–50. The
published chapter files are not touched: pairing VanderKam's Ge'ez with the
current English would show mismatched verses. vanderkam/ is outside the
dataset builder's source-*.json glob.

Usage: python3 scripts/resource_jubilees.py --xml <LIT1697Jubilees.xml> [--dry-run]
"""
import argparse, json, os, re, sys
import xml.etree.ElementTree as ET
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from script_translit import geez

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = f'{ROOT}/jubilees-woh'
T = '{http://www.tei-c.org/ns/1.0}'
LICENSE = ("CC BY-SA 4.0 — Beta maṣāḥǝft LIT1697Jubilees, Ran HaCohen's transcription of "
           "J. C. VanderKam, The Book of Jubilees: A Critical Text (CSCO 510, 1989)")
URL = 'https://betamasaheft.eu/works/LIT1697Jubilees/main'


def norm(s):
    s = ' '.join(s.split())
    s = s.replace(' ፡ ', '፡ ').replace(' ።', '።').replace(' ፡', '፡')
    return s.strip()


def parse(xml):
    ed = [e for e in ET.parse(xml).getroot().iter(T + 'div')
          if e.get('type') == 'edition' and e.get('{http://www.w3.org/XML/1998/namespace}id') == 'Ran'][0]
    out = defaultdict(dict)
    for c in ed.iter(T + 'div'):
        if c.get('subtype') != 'chapter' or not (c.get('n') or '').isdigit():
            continue
        ch = int(c.get('n'))
        for l in c.iter(T + 'l'):
            text = ' '.join(''.join(l.itertext()).split())
            parts = re.split(r'\s(\d{1,2})\s(?=[ሀ-፿])', ' ' + text)
            first = int(l.get('n'))
            out[ch][first] = norm(parts[0])
            for i in range(1, len(parts) - 1, 2):
                out[ch][int(parts[i])] = norm(parts[i + 1])
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--xml', required=True); ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    vk = parse(a.xml)
    os.makedirs(f'{BOOK}/vanderkam', exist_ok=True)
    for c in sorted(vk):
        nums = sorted(vk[c])
        gaps = sorted(set(range(1, max(nums) + 1)) - set(nums))
        src = {'schemaVersion': '1', 'bookSlug': 'jubilees-woh', 'chapter': c,
               'source': {'edition': 'J. C. VanderKam, The Book of Jubilees: A Critical Text (CSCO 510, 1989), '
                                     'transcribed by Ran HaCohen (Beta maṣāḥǝft LIT1697Jubilees)',
                          'license': LICENSE, 'url': URL},
               'verses': [{'n': str(n), 'refId': f'JUB-WOH-{c}:{n}', 'text_geez': vk[c][n], 'text_lang': 'gez',
                           'translit': geez(vk[c][n])} for n in nums]}
        if gaps:
            src['transcriptionGaps'] = gaps
        if not a.dry_run:
            with open(f'{BOOK}/vanderkam/geez-{c}.json', 'w', encoding='utf-8') as fh:
                json.dump(src, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f'{len(vk)} chapters, {sum(len(v) for v in vk.values())} verses written to jubilees-woh/vanderkam/')


if __name__ == '__main__':
    main()
