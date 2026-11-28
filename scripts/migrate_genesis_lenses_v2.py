#!/usr/bin/env python3
"""Migrate the Genesis lens files from schemaVersion 1 to 2.

Founder decision 2026-11-28: the reader's lenses become
    1 Hebrew   (layer 1, unchanged)
    2 Literal  (layer 2, unchanged)
    3 Reading  NEW: the literal sentence with canon-decoded words swapped in
    4 Meaning  the old lens-3 per-verse readings
and the old lens-4 passage explanation becomes a folded note under the
Meaning cards. Per passage that is:

    readings     -> meaning   (same fields, same order)
    explanation  -> note      (same fields)
    (new)           decoded = []   (written later; see README.md)

Everything else is carried over untouched: basedOn, lens (version, status,
sign-off, modelDrafts, reviewerReport, coreClaims) and every passage field.
lens.version is NOT bumped: no reader-facing text changes, so the founder's
sign-off still covers the content. _lenses.json moves to schemaVersion 2.

The migration is lossless and idempotent: a v2 file is left as it is, and
every v1 value can be read back from the v2 file under its new key (each
file is mapped back to v1 and compared before it is written). Layer-2 files
(genesis-woh/chapter-N.json) are never opened for writing.

Usage:
    python3 scripts/migrate_genesis_lenses_v2.py            # migrate in place
    python3 scripts/migrate_genesis_lenses_v2.py --dry-run  # report only
"""
import argparse
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LENS_DIR = ROOT / 'genesis-woh' / 'lenses'
LENS_FILE_RE = re.compile(r'^chapter-(\d+)\.json$')

RENAMES = {'readings': 'meaning', 'explanation': 'note'}


def migrate_passage(p):
    """Return the v2 passage: keys in reading order, decoded before meaning."""
    out = {}
    for key, value in p.items():
        if key == 'readings':
            out['decoded'] = p.get('decoded', [])
            out['meaning'] = value
        elif key == 'explanation':
            out['note'] = value
        elif key == 'decoded':
            continue
        else:
            out[key] = value
    out.setdefault('decoded', [])
    return out


def migrate_chapter(data):
    if data.get('schemaVersion') == 2:
        return data, False
    if data.get('schemaVersion') != 1:
        raise ValueError(f'unexpected schemaVersion {data.get("schemaVersion")!r}')
    out = {}
    for key, value in data.items():
        if key == 'schemaVersion':
            out[key] = 2
        elif key == 'passages':
            out[key] = [migrate_passage(p) for p in value]
        else:
            out[key] = value
    return out, True


def back_to_v1(data):
    """Inverse mapping, used to prove the migration lost nothing."""
    out = copy.deepcopy(data)
    out['schemaVersion'] = 1
    passages = []
    for p in out['passages']:
        q = {}
        for key, value in p.items():
            if key == 'decoded':
                continue
            inv = {v: k for k, v in RENAMES.items()}
            q[inv.get(key, key)] = value
        passages.append(q)
    out['passages'] = passages
    return out


def dump(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--dir', default=str(LENS_DIR), help='genesis-woh/lenses directory')
    ap.add_argument('--dry-run', action='store_true', help='report, write nothing')
    args = ap.parse_args(argv)
    lens_dir = Path(args.dir)

    changed = 0
    for path in sorted(lens_dir.glob('chapter-*.json'), key=lambda p: p.name):
        m = LENS_FILE_RE.match(path.name)
        if not m:
            continue
        before = json.loads(path.read_text(encoding='utf-8'))
        after, did = migrate_chapter(before)
        if not did:
            print(f'{path.name}: already schemaVersion 2')
            continue
        if back_to_v1(after) != before:
            print(f'{path.name}: round trip failed, not written', file=sys.stderr)
            return 1
        n_meaning = sum(len(p['meaning']) for p in after['passages'])
        print(f'{path.name}: v1 -> v2, {len(after["passages"])} passages, '
              f'{n_meaning} meaning units, decoded [] (lossless)')
        if not args.dry_run:
            path.write_text(dump(after), encoding='utf-8')
        changed += 1

    index_path = lens_dir / '_lenses.json'
    if index_path.is_file():
        index = json.loads(index_path.read_text(encoding='utf-8'))
        if index.get('schemaVersion') == 1:
            index['schemaVersion'] = 2
            print('_lenses.json: schemaVersion 1 -> 2')
            if not args.dry_run:
                index_path.write_text(dump(index), encoding='utf-8')
            changed += 1
    print(f'{changed} file(s) {"would change" if args.dry_run else "migrated"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
