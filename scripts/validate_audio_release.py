#!/usr/bin/env python3
"""Check advertised media hashes and durations against paragraph timing files.

Read-only and offline: validates local release files without synthesis or API
calls. Run before publishing narration, timing, or manifest changes together.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import parse_qs, urlsplit

LIBRARY = Path(__file__).resolve().parent.parent


def media_duration(path):
    return float(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=nw=1:nk=1', str(path),
    ], text=True))


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def validate(manifest_path, assets_root, library_root=LIBRARY):
    manifest = json.loads(manifest_path.read_text())
    errors = []
    checked = []
    for chapter in manifest['chapters']:
        label = f"{manifest['lang']}/{manifest['book']}/c{chapter['n']}"
        timing_path = assets_root / urlsplit(chapter['timing_url']).path
        timing = json.loads(timing_path.read_text())
        duration = timing['duration_seconds']
        if abs(chapter['duration_seconds'] - duration) > .002:
            errors.append(f'{label}: manifest/timing duration mismatch')
        paragraphs = timing['paragraphs']
        if chapter['paragraph_count'] != len(paragraphs):
            errors.append(f'{label}: manifest paragraph count mismatch')
        sidecar_path = library_root / manifest['book'] / 'tts' / f"chapter-{chapter['n']}.{manifest['lang']}.json"
        if sidecar_path.exists():
            sidecar = json.loads(sidecar_path.read_text())
            expected = sorted(int(n) for n, p in sidecar.items() if not p.get('skip') and p.get('text', '').strip())
            actual = [p['n'] for p in paragraphs if p['n'] != 0]
            if actual != expected:
                errors.append(f'{label}: spoken paragraph references differ from current TTS source')
        previous = 0
        for p in paragraphs:
            if not (previous - .002 <= p['start'] <= p['end'] <= duration + .002):
                errors.append(f"{label} paragraph {p['n']}: invalid or overlapping interval")
            previous = p['end']
            if any(not (p['start'] - .002 <= w['start'] <= w['end'] <= p['end'] + .002)
                   for w in p.get('words', [])):
                errors.append(f"{label} paragraph {p['n']}: word outside paragraph interval")
            words = p.get('words', [])
            if any(b['start'] < a['start'] - .002 for a, b in zip(words, words[1:])):
                errors.append(f"{label} paragraph {p['n']}: word timestamps out of order")
        urls = {chapter['audio_url'], *(f['url'] for f in chapter.get('formats', []))}
        if chapter.get('ambient_url'):
            urls.add(chapter['ambient_url'])
        for url in sorted(urls):
            parsed = urlsplit(url)
            path = assets_root / parsed.path
            if not path.is_file():
                errors.append(f'{label}: missing {parsed.path}')
                continue
            version = parse_qs(parsed.query).get('v', [''])[0]
            if not version or not sha256(path).startswith(version):
                errors.append(f'{label}: stale content hash for {path.name}')
            if path.stat().st_size > 25 * 1024 * 1024:
                errors.append(f'{label}: advertised {path.name} exceeds host file limit')
            measured = media_duration(path)
            delta = round(measured - duration, 6)
            checked.append(dict(file=parsed.path, duration=measured, timing=duration, delta=delta))
            if abs(delta) > .15:
                errors.append(f'{label}: {path.name} differs from timing by {delta:+.3f}s')
    return dict(book=manifest['book'], lang=manifest['lang'], checked=checked, errors=errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets-root', type=Path, default=LIBRARY.parent / 'assets.wheelofheaven.world')
    parser.add_argument('--slug', required=True)
    parser.add_argument('--lang', required=True)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    manifest = args.assets_root / 'audio' / args.lang / args.slug / 'manifest.json'
    result = validate(manifest, args.assets_root)
    if args.report:
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f"{args.slug} {args.lang}: {len(result['checked'])} media files; {len(result['errors'])} errors")
    for error in result['errors']:
        print(error)
    raise SystemExit(bool(result['errors']))


if __name__ == '__main__':
    main()
