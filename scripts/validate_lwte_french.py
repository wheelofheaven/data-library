#!/usr/bin/env python3
"""Verify the French source repair and reconstruct the preceding English audit."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEW = ROOT / 'reviews/lwte-french-2026-10-19'


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def preceding_chapter(chapter, verify_witness=False):
    receipt = json.loads((REVIEW / f'chapter-{chapter}.json').read_text())
    raw = (ROOT / receipt['path']).read_bytes()
    if digest(raw) != receipt['afterSha256']:
        raise ValueError('French chapter changed since review')
    source = ROOT.parent / receipt['source']['path']
    if verify_witness and digest(source.read_bytes()) != receipt['source']['sha256']:
        raise ValueError('French PDF witness changed')
    data = json.loads(raw)
    paragraphs = {p['refId']: p for p in data['paragraphs']}
    seen = set()
    for change in receipt['changes']:
        ref = change['refId']
        if ref in seen or paragraphs[ref] != change['after']:
            raise ValueError('Invalid or duplicate French repair')
        seen.add(ref)
        before, after = copy.deepcopy(change['before']), copy.deepcopy(change['after'])
        for p in (before, after):
            p.pop('text')
            p.get('kindByLang', {}).pop('fr', None)
            if not p.get('kindByLang'):
                p.pop('kindByLang', None)
        if before != after:
            raise ValueError('French repair changed another language or reference')
        paragraphs[ref].clear()
        paragraphs[ref].update(change['before'])
    baseline = encoded(data)
    if digest(baseline) != receipt['beforeSha256']:
        raise ValueError('French review does not reconstruct its baseline')
    english = json.loads((ROOT / 'reviews/lwte-alignment-2026-10-18' / f'chapter-{chapter}.json').read_text())
    if digest(baseline) != english['afterSha256']:
        raise ValueError('French review does not follow the English alignment')
    return baseline


if __name__ == '__main__':
    for chapter in range(1, 5):
        preceding_chapter(chapter, verify_witness=True)
        print(f'Chapter {chapter}: French repair verified; preceding English alignment conserved')
