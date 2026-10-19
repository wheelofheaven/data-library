#!/usr/bin/env python3
"""Dry-run-first cleanup of reproducible audio intermediates after release QA.

Never removes provider MP3s, alignments, input metadata, or request ledgers.
Published delivery hashes must match the release report before any deletion.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def candidates(report_path):
    report = json.loads(report_path.read_text())
    slug, lang = report['book'], report['language']
    if any('/' in x or x in ('', '.', '..') for x in (slug, lang)):
        raise ValueError('Invalid book/language')
    assets = ROOT.parent / 'assets.wheelofheaven.world'
    manifest = assets / 'audio' / lang / slug / 'manifest.json'
    if hashlib.sha256(manifest.read_bytes()).hexdigest() != report['manifest_sha256']:
        raise ValueError('Delivery manifest differs from verified release')
    for chapter in report['chapters']:
        for asset in chapter['assets']:
            path = (assets / asset['path']).resolve()
            if not path.is_relative_to(assets.resolve()):
                raise ValueError('Asset path escapes asset repository')
            if hashlib.sha256(path.read_bytes()).hexdigest() != asset['sha256']:
                raise ValueError(f'Delivery asset changed: {path.name}')
    work = ROOT / 'audio/_work' / slug / lang
    result = []
    for chapter in report['chapters']:
        directory = work / f"c{chapter['chapter']}"
        for pattern in ('p*.treated.mp3', 'p*.treated.meta.json',
                        'p*.treated.concat.wav', 'p*.treated.concat.meta.json'):
            for path in directory.glob(pattern):
                if path.is_symlink() or not path.resolve().is_relative_to(work.resolve()):
                    raise ValueError('Refusing symlink/out-of-scope cache entry')
                # Each disposable file must have its paid regeneration source.
                raw = directory / (path.name.split('.')[0] + '.mp3')
                if not raw.exists() or not raw.with_suffix('.alignment.json').exists() or not raw.with_suffix('.meta.json').exists():
                    raise ValueError(f'Missing provider cache for {path.name}')
                result.append(path)
    return sorted(set(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    paths = candidates(args.report)
    size = sum(p.stat().st_size for p in paths)
    print(f'{len(paths)} reproducible files; {size / 2**30:.2f} GiB; mode=' + ('apply' if args.apply else 'dry-run'))
    if args.apply:
        for path in paths:
            path.unlink()
        print('Removed derived files; paid audio, alignments, and ledgers retained.')
