#!/usr/bin/env python3
"""Merge a translation wave's per-chapter glossary diffs into the glossaries.

Editors in a parallel wave never write the shared glossaries; each writes
`{book}/wave-<id>-ch<N>-overlay-diff.json` and `-central-diff.json` against
the same base versions. This script applies all of them at once:

- add: the entry is added; the same id from two chapters is an error unless
  listed in an orchestrator ops file (--ops) as a merge.
- modify: appliesTo becomes the union of the current array and every
  chapter's `appliesToAdded` (the `changes.appliesTo` snapshots are ignored,
  since each was taken against the base); other `changes` fields replace the
  field (two chapters changing the same field is an error);
  `rationaleAppend` texts are appended to the rationale in chapter order.
- version / note ops are informational.

The orchestrator ops file holds the wave-wide rulings the Editors left to
the orchestrator: {"merge": {"drop-id": "keep-id"}, "appliesToAdd": {"id":
[...]}, "set": {"id": {"field": value}}, "add": [full entries]}, per glossary
("overlay" / "central"), plus a top-level "refsAdd": {"id": [refId, ...]}
that adds glossaryRefs to the chapters, and "extraChapters": [paths relative to
the repo root] for chapters outside the wave that refsAdd touches. Merged ids are renamed in the
chapters' glossaryRefs.

Two diff shapes are accepted: a list of ops, or an object with `ops`, or
(older) `newEntries` + `appliesToExtensions`.

Usage:
  python3 scripts/merge_wave_diffs.py --book isaiah-woh --wave i1 \
      --central <path/to/translation-glossary.json> \
      --overlay-version 1.7.0 --central-version 2.94.0 \
      [--ops isaiah-woh/wave-i1-orchestrator-ops.json] [--out-dir DIR]

Without --out-dir the glossaries are written in place.
"""
import argparse, glob, json, os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ops_of(d):
    if isinstance(d, list):
        return d
    if 'ops' in d:
        return d['ops']
    return ([{'op': 'add', 'entry': e} for e in d.get('newEntries', [])] +
            [dict(op='modify', **e) for e in d.get('appliesToExtensions', [])])


def union(a, b):
    out = list(a)
    for r in b:
        if r not in out:
            out.append(r)
    return out


def apply(entries, diffs, ops_file, label, problems):
    by_id = {e['id']: e for e in entries}
    added_by = {}
    field_by = {}
    log = defaultdict(list)
    for chap, d in diffs:
        for o in ops_of(d):
            kind = o.get('op')
            if kind == 'add':
                e = dict(o['entry'])
                e.pop('term', None) if 'source' in e else None
                e.pop('rendering', None) if 'wohChoice' in e else None
                if e['id'] in by_id:
                    if e['id'] in added_by:
                        problems.append(f"{label}: {e['id']} added by ch{added_by[e['id']]} and ch{chap}")
                    else:
                        problems.append(f"{label}: ch{chap} adds {e['id']}, which already exists")
                    continue
                entries.append(e); by_id[e['id']] = e; added_by[e['id']] = chap
                log['added'].append(e['id'])
            elif kind == 'modify':
                e = by_id.get(o['id'])
                if e is None:
                    problems.append(f"{label}: ch{chap} modifies missing {o['id']}"); continue
                e['appliesTo'] = union(e.get('appliesTo', []), o.get('appliesToAdded', []))
                for f, v in (o.get('changes') or {}).items():
                    if f == 'appliesTo':
                        continue
                    if (o['id'], f) in field_by:
                        problems.append(f"{label}: {o['id']}.{f} changed by ch{field_by[(o['id'], f)]} and ch{chap}")
                        continue
                    e[f] = v; field_by[(o['id'], f)] = chap
                if o.get('rationaleAppend'):
                    e['rationale'] = (e.get('rationale', '').rstrip() + ' ' + o['rationaleAppend'].strip()).strip()
                log['modified'].append(o['id'])
    for e in ops_file.get('add') or []:
        if e['id'] in by_id:
            problems.append(f"{label}: orchestrator add {e['id']} already exists"); continue
        entries.append(dict(e)); by_id[e['id']] = entries[-1]; log['added'].append(e['id'])
    for drop, keep in (ops_file.get('merge') or {}).items():
        if drop in by_id and keep in by_id:
            by_id[keep]['appliesTo'] = union(by_id[keep].get('appliesTo', []), by_id[drop].get('appliesTo', []))
            entries.remove(by_id.pop(drop)); log['merged'].append(f'{drop}->{keep}')
    for i, refs in (ops_file.get('appliesToAdd') or {}).items():
        if i in by_id:
            by_id[i]['appliesTo'] = union(by_id[i].get('appliesTo', []), refs); log['extended'].append(i)
    for i, fields in (ops_file.get('set') or {}).items():
        if i in by_id:
            by_id[i].update(fields); log['set'].append(i)
    return log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', required=True); ap.add_argument('--wave', required=True)
    ap.add_argument('--central', required=True)
    ap.add_argument('--overlay-version', required=True); ap.add_argument('--central-version', required=True)
    ap.add_argument('--ops'); ap.add_argument('--out-dir')
    ap.add_argument('--overlay', help='overlay input (default: <book>/_translation-glossary.json); lets waves chain in a dry run')
    ap.add_argument('--chapters-from', help='read chapter files from this dir (default: the book dir)')
    a = ap.parse_args()
    book = f'{ROOT}/{a.book}'
    ops_file = json.load(open(a.ops)) if a.ops else {}

    def diffs(kind):
        out = []
        for p in glob.glob(f'{book}/wave-{a.wave}-ch*-{kind}-diff.json'):
            out.append((int(re.search(r'-ch(\d+)-', p).group(1)), json.load(open(p, encoding='utf-8'))))
        return sorted(out, key=lambda x: x[0])

    problems = []
    ov_path = f'{book}/_translation-glossary.json'
    ov = json.load(open(a.overlay or ov_path, encoding='utf-8'))
    ov_log = apply(ov['entries'], diffs('overlay'), ops_file.get('overlay', {}), 'overlay', problems)
    ce = json.load(open(a.central, encoding='utf-8'))
    ce_log = apply(ce['terms'], diffs('central'), ops_file.get('central', {}), 'central', problems)

    # Chapter glossaryRefs: rename merged ids, add refs the orchestrator
    # assigns (refsAdd: {id: [refId, ...]}), then check every ref resolves.
    renames = {**(ops_file.get('overlay', {}).get('merge') or {}), **(ops_file.get('central', {}).get('merge') or {})}
    refs_add = ops_file.get('refsAdd') or {}
    ids = {e['id'] for e in ov['entries']} | {e['id'] for e in ce['terms']}
    chapters = sorted({c for c, _ in diffs('overlay')} | {c for c, _ in diffs('central')})
    changed_chapters = {}
    paths = [f'{book}/chapter-{c}.json' for c in chapters]
    paths += [f'{ROOT}/{x}' for x in ops_file.get('extraChapters', [])]
    for path in paths:
        c = os.path.relpath(path, ROOT)
        alt = f'{a.chapters_from}/{os.path.basename(path)}' if a.chapters_from else None
        src_path = alt if alt and os.path.exists(alt) and os.path.dirname(path) == book else path
        raw = open(src_path, encoding='utf-8').read(); ch = json.loads(raw)
        # a chapter of another book also resolves against that book's own overlay
        own_ov = os.path.join(os.path.dirname(path), '_translation-glossary.json')
        own_ids = set()
        if os.path.dirname(path) != book and os.path.exists(own_ov):
            own_ids = {e['id'] for e in json.load(open(own_ov, encoding='utf-8')).get('entries', [])}
        for p in ch['paragraphs']:
            refs = [renames.get(r, r) for r in p.get('glossaryRefs', [])]
            for i, targets in refs_add.items():
                if p['refId'] in targets and i not in refs:
                    refs.append(i)
            refs = list(dict.fromkeys(refs))
            if refs != p.get('glossaryRefs', []):
                p['glossaryRefs'] = refs
            for r in refs:
                if r not in ids and r not in own_ids:
                    problems.append(f'{c} {p["refId"]}: unresolved glossaryRef {r}')
        new = json.dumps(ch, ensure_ascii=False, indent=2) + '\n'
        if new != raw:
            changed_chapters[path] = new

    ov['version'] = a.overlay_version
    ce['version'] = a.central_version
    out_ov, out_ce = ov_path, a.central
    if a.out_dir:
        os.makedirs(a.out_dir, exist_ok=True)
        out_ov = f'{a.out_dir}/{a.book}-_translation-glossary.json'
        out_ce = f'{a.out_dir}/translation-glossary.json'
    for path, data in ((out_ov, ov), (out_ce, ce)):
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2); fh.write('\n')
    for path, new in changed_chapters.items():
        if a.out_dir:
            path = f'{a.out_dir}/' + os.path.relpath(path, ROOT).replace('/', '__') if os.path.dirname(path) != book else f'{a.out_dir}/{os.path.basename(path)}'
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new)
    print('chapters with glossaryRef changes:', sorted(os.path.basename(p) for p in changed_chapters))
    for name, log in (('overlay', ov_log), ('central', ce_log)):
        print(name, {k: len(v) for k, v in log.items()}, {k: v for k, v in log.items() if k in ('merged', 'set')})
    print(f'overlay {len(ov["entries"])} entries -> {out_ov}')
    print(f'central {len(ce["terms"])} terms -> {out_ce}')
    for p in problems:
        print('PROBLEM', p)
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
