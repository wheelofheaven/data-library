#!/usr/bin/env python3
"""Check or apply a reviewed alignment manifest without renumbering source refs.

Dry-run by default. --check requires the reviewed result already on disk.
--epub additionally verifies the source archive and conservation of its text.
"""
import argparse
import copy
import hashlib
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(data):
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode()


def compact(text):
    return re.sub(r'\s+', '', text)


def witness_text(raw, exclusions):
    elements = [e for e in ET.fromstring(raw).iter()
                if e.tag.split('}')[-1] in {'p', 'li', 'h1', 'h2', 'h3', 'h4'}]
    excluded = {r['element']: r for r in exclusions}
    parts = []
    for n, element in enumerate(elements, 1):
        text = ' '.join(''.join(element.itertext()).split())
        if n in excluded:
            if text != excluded[n]['text']:
                raise ValueError(f'Excluded source element {n} changed')
        else:
            parts.append(text)
    if not set(excluded).issubset(range(1, len(elements) + 1)):
        raise ValueError('Invalid excluded element')
    return ''.join(parts)


def verify_text(manifest, epub=None):
    text = ''.join(p['en'] for p in manifest['paragraphs'])
    text = compact(text)
    for move in manifest.get('relocations', []):
        fragment = compact(move['text'])
        if text.count(fragment) != 1:
            raise ValueError('Relocated text is missing or duplicated')
        text = text.replace(fragment, '')
    if digest(text.encode()) != manifest['source']['readingTextSha256']:
        raise ValueError('Reviewed English text does not conserve the witness')
    if epub:
        if digest(epub.read_bytes()) != manifest['source']['sha256']:
            raise ValueError('Source EPUB changed')
        with zipfile.ZipFile(epub) as archive:
            raw = archive.read(manifest['source']['member'])
        if digest(raw) != manifest['source']['memberSha256']:
            raise ValueError('Source member changed')
        source = compact(witness_text(raw, manifest['excludedElements']))
        for move in manifest.get('relocations', []):
            fragment = compact(move['text'])
            if source.count(fragment) != 1:
                raise ValueError('Relocated source text is missing or duplicated')
            source = source.replace(fragment, '')
        if source != text:
            raise ValueError('Source and reviewed reading text differ')


def transform(data, manifest):
    rows = manifest['paragraphs']
    expected = {p['n']: p for p in rows}
    if len(expected) != len(rows) or list(expected) != [p['n'] for p in data['paragraphs']]:
        raise ValueError('Reference set or order changed')
    result = copy.deepcopy(data)
    refs = {p['refId'] for p in data['paragraphs']}
    for p in result['paragraphs']:
        row = expected[p['n']]
        p.setdefault('i18n', {})['en'] = row['en']
        if 'kind' in row:
            p['kind'] = row['kind']
        if 'alignment' in row:
            alignment = row['alignment']
            status = alignment['status']
            if status not in {'group', 'covered-by', 'not-in-witness'}:
                raise ValueError('Unknown alignment status')
            if status in {'covered-by', 'not-in-witness'} and row['en']:
                raise ValueError('An absent counterpart must not contain English text')
            if status == 'covered-by' and alignment['refId'] not in refs:
                raise ValueError('Unknown shared passage reference')
            if status == 'group' and not set(alignment['refIds']).issubset(refs):
                raise ValueError('Unknown group reference')
            p.setdefault('alignment', {})['en'] = alignment
        if 'note' in row:
            notes = p.setdefault('notes', {})
            existing = notes.get('official', '')
            if existing and existing != row['note']:
                raise ValueError('Existing editorial note needs reconciliation')
            notes['official'] = row['note']
    return result


def prepare(root, manifest, epub=None):
    verify_text(manifest, epub)
    path = (root / manifest['path']).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Chapter path escapes library root')
    raw = path.read_bytes()
    if digest(raw) == manifest['afterSha256']:
        return path, raw, False
    if digest(raw) != manifest['beforeSha256']:
        raise ValueError('Chapter changed since review; review again before applying')
    updated = encode(transform(json.loads(raw), manifest))
    if digest(updated) != manifest['afterSha256']:
        raise ValueError('Result differs from the reviewed chapter')
    return path, updated, True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifests', nargs='+', type=Path)
    ap.add_argument('--root', type=Path, default=ROOT)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true')
    mode.add_argument('--check', action='store_true')
    ap.add_argument('--epub', type=Path)
    args = ap.parse_args()
    # Validate the whole batch before writing any chapter.
    results = [prepare(args.root, json.loads(p.read_text()), args.epub) for p in args.manifests]
    if args.check and any(changed for _, _, changed in results):
        ap.error('Reviewed alignment has not been applied')
    for path, raw, changed in results:
        if changed and args.apply:
            path.write_bytes(raw)
        print(f'{path.name}: ' + ('updated' if changed and args.apply else 'would update' if changed else 'verified'))


if __name__ == '__main__':
    main()
