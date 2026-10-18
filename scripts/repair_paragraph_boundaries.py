#!/usr/bin/env python3
"""Apply reviewed boundary corrections, preserving words and reference identities.

Dry-run by default. The manifest is an editorial decision record, never an
alignment heuristic. All files are checked in memory before any are written.
"""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def compact(text):
    return ''.join(text.split())


def apply_manifest(root, manifest):
    paths = {op['path'] for op in manifest['textMoves'] + manifest['continuations']}
    original = {path: json.loads((root / path).read_text()) for path in paths}
    result = copy.deepcopy(original)
    # The final value of every field also permits safe, complete reapplication
    # where two moves touch the same paragraph in succession.
    final = {}
    for op in manifest['textMoves']:
        for n, text in zip(op['paragraphs'], op['after']):
            final[op['path'], n, op['language']] = text
    def paragraph(path, n):
        return next(p for p in result[path]['paragraphs'] if p['n'] == n)
    def get(p, lang):
        return p['text'] if lang == 'fr' else p['i18n'][lang]
    applied = all(get(paragraph(path, n), lang) == text
                  for (path, n, lang), text in final.items())
    if not applied:
        for op in manifest['textMoves']:
            path, lang = op['path'], op['language']
            ps = [paragraph(path, n) for n in op['paragraphs']]
            before = [get(p, lang) for p in ps]
            if before != op['before']:
                raise ValueError(f"Source changed: {path} {op['paragraphs']} {lang}")
            if compact(''.join(before)) != compact(''.join(op['after'])):
                raise ValueError(f"Boundary repair changes wording: {path}")
            for p, text in zip(ps, op['after']):
                if lang == 'fr':
                    p['text'] = text
                else:
                    p['i18n'][lang] = text
    for op in manifest['continuations']:
        p = paragraph(op['path'], op['paragraph'])
        if p.get('kind') not in (None, op['kind']):
            raise ValueError(f"Unexpected kind: {op['path']} {op['paragraph']}")
        p['kind'] = op['kind']
    for path, data in result.items():
        before = original[path]['paragraphs']
        after = data['paragraphs']
        assert [(p['n'], p['refId']) for p in before] == [(p['n'], p['refId']) for p in after]
        langs = {'fr'} | {l for p in before for l in p.get('i18n', {})}
        for lang in langs:
            assert compact(''.join(get(p, lang) for p in before)) == compact(''.join(get(p, lang) for p in after)), (path, lang)
    return {path: data for path, data in result.items() if data != original[path]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--manifest', type=Path, default=ROOT / 'curation/2026-10-18-paragraph-boundaries.json')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    changes = apply_manifest(args.root, json.loads(args.manifest.read_text()))
    for path, data in sorted(changes.items()):
        if args.apply:
            (args.root / path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        print(('Updated ' if args.apply else 'Would update ') + path)
    print(f'{len(changes)} changed files; wording and reference IDs preserved')


if __name__ == '__main__':
    main()
