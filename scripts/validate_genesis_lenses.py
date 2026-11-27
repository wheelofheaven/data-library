#!/usr/bin/env python3
"""Validate the Genesis four-lens reader data in genesis-woh/lenses/.

Checks the canon map, the lens index and every lens chapter file against
the rules in genesis-woh/lenses/README.md. Python stdlib only.

Usage:
    python3 scripts/validate_genesis_lenses.py
    python3 scripts/validate_genesis_lenses.py --core-catalog ../core/model/catalog.json
    python3 scripts/validate_genesis_lenses.py --staged     # also refuse staged layer-2 files
    python3 scripts/validate_genesis_lenses.py --digest 1   # print the layer-2 digest of Gen 1

Exit status: 0 when no errors (warnings are printed but do not fail), 1 otherwise.

layer2Digest
    For chapter N, read genesis-woh/chapter-N.json, sort its paragraphs by
    "n", and build one line per verse: "<N>:<n>" + TAB + i18n.en, taken
    byte-for-byte (no normalisation or trimming). Join the lines with "\n"
    (no trailing newline), encode as UTF-8, and hash with SHA-256. The value
    is "sha256:" + the lowercase hex digest. Any change to an English verse,
    or to the verse set, changes the digest and marks the lens file stale.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = 'genesis-woh'
LENS_DIR = Path(BOOK) / 'lenses'

CANON_BOOKS = {
    'TBWTT': 'the-book-which-tells-the-truth',
    'ETTMTTP': 'extraterrestrials-took-me-to-their-planet',
    'LWTE': 'lets-welcome-the-extraterrestrials',
}
CANON_REF_RE = re.compile(r'^(TBWTT|ETTMTTP|LWTE)-(\d+):(\d+)$')
VERSE_RE = re.compile(r'^(\d+):(\d+)$')
READING_REF_RE = re.compile(r'^(\d+):(\d+)(?:-(\d+))?$')
SEMVER_RE = re.compile(r'^\d+\.\d+\.\d+$')
DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}([T ][0-9:.]+(Z|[+-]\d{2}:\d{2})?)?$')
PASSAGE_ID_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
LENS_FILE_RE = re.compile(r'^chapter-(\d+)\.json$')
STAGED_FORBIDDEN_RE = re.compile(r'(^|/)genesis-woh/chapter-\d+\.json$')

REF_RELATIONS = ('quotes', 'comments', 'alludes', 'opinion')
ENTRY_RELATIONS = ('quotes', 'comments', 'alludes', 'opinion', 'check', 'silent')
STANDINGS = ('canon', 'narration', 'check', 'author-opinion')
RANK = {'quotes': 3, 'comments': 2, 'alludes': 1}
CLAIMS = ('direct', 'framework', 'inferred', 'speculative')
STATUSES = ('draft', 'editor-review', 'reviewer-approved', 'awaiting-human', 'stable')
PASSAGE_COVERAGE = ('quotes', 'comments', 'alludes', 'silent')
BASES = ('canon', 'synthesis')
STRICT_DIGEST_STATUSES = ('reviewer-approved', 'awaiting-human', 'stable')


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append(f'{where}: {msg}')

    def warn(self, where, msg):
        self.warnings.append(f'{where}: {msg}')


# ---------------------------------------------------------------- loading

def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def load_layer2(root, chapter):
    return load_json(Path(root) / BOOK / f'chapter-{chapter}.json')


def verse_counts(root):
    counts = {}
    for path in (Path(root) / BOOK).glob('chapter-*.json'):
        m = LENS_FILE_RE.match(path.name)
        if m:
            counts[int(m.group(1))] = len(load_json(path)['paragraphs'])
    return counts


def layer2_digest(root, chapter):
    """Digest of the chapter's layer-2 English; see module docstring."""
    paragraphs = sorted(load_layer2(root, chapter)['paragraphs'], key=lambda p: p['n'])
    lines = [f"{chapter}:{p['n']}\t{p['i18n']['en']}" for p in paragraphs]
    data = '\n'.join(lines).encode('utf-8')
    return 'sha256:' + hashlib.sha256(data).hexdigest()


def canon_speakers(root):
    """refId -> speaker for every paragraph of the three canon books."""
    speakers = {}
    for slug in CANON_BOOKS.values():
        for path in sorted((Path(root) / slug).glob('chapter-*.json')):
            for p in load_json(path).get('paragraphs', []):
                speakers[p['refId']] = p.get('speaker')
    return speakers


def find_catalog(root, explicit=None):
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    if os.environ.get('WOH_CORE_CATALOG'):
        candidates.append(Path(os.environ['WOH_CORE_CATALOG']))
    candidates.append(Path(root).resolve().parent / 'core' / 'model' / 'catalog.json')
    for c in candidates:
        if c.is_file():
            return c
    return None


def load_catalog(path):
    data = load_json(path)
    claims = data.get('claims', data) if isinstance(data, dict) else data
    if isinstance(claims, dict):
        return {k: (v or {}).get('version') for k, v in claims.items()}
    return {c['id']: c.get('version') for c in claims}


# ---------------------------------------------------------------- verses

def verse_key(text):
    m = VERSE_RE.match(text or '')
    return (int(m.group(1)), int(m.group(2))) if m else None


def expand_range(start, end, counts):
    """Inclusive list of (chapter, verse) from start to end across chapters."""
    out = []
    c, v = start
    while True:
        if c not in counts or v < 1 or v > counts[c]:
            raise ValueError(f'verse {c}:{v} does not exist')
        out.append((c, v))
        if (c, v) == end:
            return out
        if (c, v) > end:
            raise ValueError('range runs backwards')
        v += 1
        if v > counts[c]:
            c, v = c + 1, 1


def expand_reading_ref(text, chapter, counts):
    m = READING_REF_RE.match(text or '')
    if not m:
        raise ValueError(f'bad verse ref {text!r} (use "C:V" or "C:V-W")')
    c, a = int(m.group(1)), int(m.group(2))
    b = int(m.group(3)) if m.group(3) else a
    if c != chapter:
        raise ValueError(f'ref {text!r} is outside chapter {chapter}')
    if b < a:
        raise ValueError(f'ref {text!r} runs backwards')
    return expand_range((c, a), (c, b), counts)


# ---------------------------------------------------------------- standing

def standing_of(ref, rules, speakers):
    m = CANON_REF_RE.match(ref)
    if not m or ref not in speakers:
        return None
    book, chapter = m.group(1), int(m.group(2))
    speaker = speakers[ref]
    for rule in rules:
        if rule.get('book') != book:
            continue
        if 'chapter' in rule and rule['chapter'] != chapter:
            continue
        if rule.get('speaker', '*') not in ('*', speaker):
            continue
        return rule['standing']
    return None


# ---------------------------------------------------------------- canon map

def validate_canon_map(cmap, counts, speakers, rep):
    """Validate canon-map.json; return {(c, v): entry} for lens checks."""
    where = 'canon-map.json'
    by_verse = {}
    if not SEMVER_RE.match(str(cmap.get('version', ''))):
        rep.error(where, 'version must be semver (e.g. "1.0.0")')
    if cmap.get('bookSlug') != BOOK:
        rep.error(where, f'bookSlug must be "{BOOK}"')
    rules = cmap.get('standingRules')
    if not isinstance(rules, list) or not rules:
        rep.error(where, 'standingRules must be a non-empty list')
        rules = []
    for i, rule in enumerate(rules):
        if rule.get('book') not in CANON_BOOKS or rule.get('standing') not in STANDINGS:
            rep.error(where, f'standingRules[{i}] needs a known book and standing')
        if rule.get('book') == 'LWTE' and rule.get('standing') != 'author-opinion':
            rep.error(where, f'standingRules[{i}]: LWTE standing must be "author-opinion" (ADR 0018)')

    for i, entry in enumerate(cmap.get('entries', [])):
        ew = f"{where} entries[{i}] {entry.get('range')}"
        rng = entry.get('range')
        if not (isinstance(rng, list) and len(rng) == 2):
            rep.error(ew, 'range must be ["C:V", "C:V"]')
            continue
        start, end = verse_key(rng[0]), verse_key(rng[1])
        if not start or not end:
            rep.error(ew, 'range endpoints must be "C:V"')
            continue
        try:
            verses = expand_range(start, end, counts)
        except ValueError as exc:
            rep.error(ew, str(exc))
            continue
        for cv in verses:
            if cv in by_verse:
                rep.error(ew, f'verse {cv[0]}:{cv[1]} already covered')
            else:
                by_verse[cv] = entry

        relation = entry.get('relation')
        refs = entry.get('refs')
        if relation not in ENTRY_RELATIONS:
            rep.error(ew, f'relation must be one of {ENTRY_RELATIONS}')
        if not isinstance(refs, list):
            rep.error(ew, 'refs must be a list')
            continue
        if relation == 'silent' and refs:
            rep.error(ew, 'silent entries must have empty refs')
        canon_rel = []
        stands = set()
        for j, r in enumerate(refs):
            rw = f'{ew} refs[{j}] {r.get("ref")}'
            ref = r.get('ref', '')
            if not CANON_REF_RE.match(ref):
                rep.error(rw, 'ref must look like TBWTT-2:4')
                continue
            if ref not in speakers:
                rep.error(rw, 'paragraph does not exist in the canon chapter files')
                continue
            if r.get('relation') not in REF_RELATIONS:
                rep.error(rw, f'relation must be one of {REF_RELATIONS}')
            derived = standing_of(ref, rules, speakers)
            if r.get('standing') != derived:
                rep.error(rw, f'standing {r.get("standing")!r} != rule-derived {derived!r}')
            if ref.startswith('LWTE-'):
                if r.get('standing') != 'author-opinion':
                    rep.error(rw, 'LWTE refs must carry standing "author-opinion"')
                if r.get('relation') != 'opinion':
                    rep.error(rw, 'LWTE refs must have relation "opinion"')
            elif derived == 'author-opinion':
                if r.get('relation') != 'opinion':
                    rep.error(rw, 'author-opinion refs must have relation "opinion"')
            elif r.get('relation') == 'opinion':
                rep.error(rw, 'relation "opinion" is reserved for author-opinion refs')
            if derived == 'narration':
                rep.error(rw, 'narration paragraphs are not canon; cite the dictated paragraph instead')
            stands.add(derived)
            if derived == 'canon' and r.get('relation') in RANK:
                canon_rel.append(r['relation'])
        if canon_rel:
            expected = max(canon_rel, key=lambda v: RANK[v])
        elif 'author-opinion' in stands:
            expected = 'opinion'
        elif refs:
            expected = 'check'
        else:
            expected = 'silent'
        if relation in ENTRY_RELATIONS and relation != expected:
            rep.error(ew, f'relation {relation!r} should be {expected!r} given its refs')

    for c in sorted(counts):
        for v in range(1, counts[c] + 1):
            if (c, v) not in by_verse:
                rep.error(where, f'verse {c}:{v} is not covered')
    return by_verse


def passage_coverage_for(verses, by_verse):
    best = 0
    for cv in verses:
        entry = by_verse.get(cv)
        if entry:
            best = max(best, RANK.get(entry.get('relation'), 0))
    return {3: 'quotes', 2: 'comments', 1: 'alludes', 0: 'silent'}[best]


# ---------------------------------------------------------------- lens files

def check_text(obj, where, rep):
    if not (isinstance(obj, dict) and isinstance(obj.get('en'), str) and obj['en'].strip()):
        rep.error(where, 'needs a non-empty {"en": ...} text')


def normalise_canon_refs(items, where, ctx, rep):
    """Return [(ref, derived_standing)] after checking each canon citation."""
    out = []
    if items is None:
        return out
    if not isinstance(items, list):
        rep.error(where, 'canon must be a list')
        return out
    for item in items:
        if isinstance(item, str):
            ref, stated = item, None
        elif isinstance(item, dict):
            ref, stated = item.get('ref', ''), item.get('standing')
        else:
            rep.error(where, f'bad canon item {item!r}')
            continue
        if not CANON_REF_RE.match(ref) or ref not in ctx['speakers']:
            rep.error(where, f'canon ref {ref!r} does not exist in the canon chapter files')
            continue
        derived = standing_of(ref, ctx['rules'], ctx['speakers'])
        if ref.startswith('LWTE-') and stated != 'author-opinion':
            rep.error(where, f'{ref}: LWTE citations must be {{"ref", "standing": "author-opinion"}}')
        elif derived != 'canon' and stated != derived:
            rep.error(where, f'{ref}: standing is {derived!r}; cite it as {{"ref", "standing": "{derived}"}}')
        elif stated is not None and stated != derived:
            rep.error(where, f'{ref}: stated standing {stated!r} != rule-derived {derived!r}')
        out.append((ref, derived))
    return out


def check_claim_unit(unit, where, ctx, rep, core_claims):
    """Shared checks for a reading or an explanation segment."""
    check_text(unit.get('text'), f'{where} text', rep)
    claim = unit.get('claim')
    if claim not in CLAIMS:
        rep.error(where, f'claim must be one of {CLAIMS}')
    refs = normalise_canon_refs(unit.get('canon'), where, ctx, rep)
    has_canon = any(s == 'canon' for _, s in refs)
    weak = [r for r, s in refs if s != 'canon']
    core = unit.get('coreClaim')
    if core is not None:
        ctx['claims_used'].add(core)
        if core not in core_claims:
            rep.error(where, f'coreClaim {core!r} is not listed in lens.coreClaims')
    if claim == 'framework':
        if weak and not has_canon:
            rep.error(where, f'framework claim rests only on non-canon refs {weak} (ADR 0018)')
        if not has_canon and core is None:
            rep.error(where, 'framework claim needs a canon-standing ref or a coreClaim')
    return refs, has_canon


def validate_lens_file(path, ctx, rep):
    where = path.name
    m = LENS_FILE_RE.match(path.name)
    chapter = int(m.group(1))
    try:
        data = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        rep.error(where, f'unreadable JSON: {exc}')
        return None
    counts = ctx['counts']
    if chapter not in counts:
        rep.error(where, f'Genesis has no chapter {chapter}')
        return None
    if data.get('schemaVersion') != 1:
        rep.error(where, 'schemaVersion must be 1')
    if data.get('bookSlug') != BOOK:
        rep.error(where, f'bookSlug must be "{BOOK}"')
    if data.get('chapter') != chapter:
        rep.error(where, f'chapter must be {chapter} (matches the file name)')

    based = data.get('basedOn') or {}
    lens = data.get('lens') or {}
    status = lens.get('status')
    layer2 = load_layer2(ctx['root'], chapter)
    tv = (layer2.get('translation') or {}).get('version')
    if based.get('translationVersion') != tv:
        rep.error(where, f'basedOn.translationVersion {based.get("translationVersion")!r} != layer 2 {tv!r}')
    digest = layer2_digest(ctx['root'], chapter)
    if based.get('layer2Digest') != digest:
        msg = f'STALE: basedOn.layer2Digest does not match current layer 2 ({digest})'
        (rep.error if status in STRICT_DIGEST_STATUSES else rep.warn)(where, msg)
    if based.get('canonMapVersion') != ctx['canon_version']:
        rep.error(where, f'basedOn.canonMapVersion != canon-map version {ctx["canon_version"]!r}')

    if lens.get('track') != 'lens':
        rep.error(where, 'lens.track must be "lens"')
    if not SEMVER_RE.match(str(lens.get('version', ''))):
        rep.error(where, 'lens.version must be semver')
    if status not in STATUSES:
        rep.error(where, f'lens.status must be one of {STATUSES}')
    if status == 'stable':
        by, at = lens.get('signedOffBy'), lens.get('signedOffAt')
        if not (isinstance(by, str) and by.strip()):
            rep.error(where, 'stable requires lens.signedOffBy')
        if not (isinstance(at, str) and DATE_RE.match(at)):
            rep.error(where, 'stable requires lens.signedOffAt (ISO date)')
    core_claims = lens.get('coreClaims') or {}
    if not isinstance(core_claims, dict):
        rep.error(where, 'lens.coreClaims must be an object {claimId: version}')
        core_claims = {}
    for cid, ver in core_claims.items():
        ctx['claims_used'].add(cid)
        catalog = ctx.get('catalog')
        if catalog is not None and cid in catalog and ver and catalog[cid] and ver != catalog[cid]:
            rep.warn(where, f'{cid} pinned at {ver}, catalog has {catalog[cid]}; re-check the binding')

    passages = data.get('passages')
    if not isinstance(passages, list) or not passages:
        rep.error(where, 'passages must be a non-empty list')
        return data
    passage_seen = {}
    reading_seen = {}
    ids = set()
    for i, p in enumerate(passages):
        pw = f'{where} passages[{i}] {p.get("id")}'
        pid = p.get('id')
        if not (isinstance(pid, str) and PASSAGE_ID_RE.match(pid)):
            rep.error(pw, 'id must be lowercase-hyphenated')
        elif pid in ids:
            rep.error(pw, 'duplicate passage id')
        ids.add(pid)
        check_text(p.get('title'), f'{pw} title', rep)
        rng = p.get('range') or []
        start = verse_key(rng[0]) if len(rng) == 2 else None
        end = verse_key(rng[1]) if len(rng) == 2 else None
        if not start or not end or start[0] != chapter or end[0] != chapter:
            rep.error(pw, f'range must be ["{chapter}:V", "{chapter}:W"] within this chapter')
            continue
        try:
            pverses = expand_range(start, end, counts)
        except ValueError as exc:
            rep.error(pw, str(exc))
            continue
        for cv in pverses:
            if cv in passage_seen:
                rep.error(pw, f'verse {cv[0]}:{cv[1]} already in passage {passage_seen[cv]}')
            else:
                passage_seen[cv] = pid
        expected = passage_coverage_for(pverses, ctx['by_verse'])
        cov = p.get('canonCoverage')
        if cov not in PASSAGE_COVERAGE:
            rep.error(pw, f'canonCoverage must be one of {PASSAGE_COVERAGE}')
        elif cov != expected:
            rep.error(pw, f'canonCoverage {cov!r} but the canon map gives {expected!r}')

        readings = p.get('readings')
        if not isinstance(readings, list) or not readings:
            rep.error(pw, 'readings must be a non-empty list')
            readings = []
        pset = set(pverses)
        for j, rd in enumerate(readings):
            rw = f'{pw} readings[{j}]'
            rverses = []
            for ref in rd.get('refs') or []:
                try:
                    rverses += expand_reading_ref(ref, chapter, counts)
                except ValueError as exc:
                    rep.error(rw, str(exc))
            if not rd.get('refs'):
                rep.error(rw, 'refs must list the verses this reading renders')
            for cv in rverses:
                if cv not in pset:
                    rep.error(rw, f'verse {cv[0]}:{cv[1]} is outside the passage range')
                if cv in reading_seen:
                    rep.error(rw, f'verse {cv[0]}:{cv[1]} already rendered by another reading')
                else:
                    reading_seen[cv] = rw
            basis = rd.get('basis')
            if basis not in BASES:
                rep.error(rw, f'basis must be one of {BASES}')
            refs, has_canon = check_claim_unit(rd, rw, ctx, rep, core_claims)
            if basis == 'canon':
                if not has_canon:
                    rep.error(rw, 'basis "canon" needs a canon-standing ref')
                mapped = set()
                for cv in rverses:
                    entry = ctx['by_verse'].get(cv) or {}
                    mapped |= {r['ref'] for r in entry.get('refs', []) if r.get('standing') == 'canon'}
                if has_canon and not any(r in mapped for r, s in refs if s == 'canon'):
                    rep.error(rw, 'basis "canon" but none of its canon refs is mapped to its verses '
                                  'in canon-map.json')

        expl = p.get('explanation')
        if not isinstance(expl, dict) or not isinstance(expl.get('paragraphs'), list) \
                or not expl['paragraphs']:
            rep.error(pw, 'explanation.paragraphs must be a non-empty list')
        else:
            for k, para in enumerate(expl['paragraphs']):
                if not isinstance(para, list) or not para:
                    rep.error(f'{pw} explanation[{k}]', 'paragraph must be a non-empty list of segments')
                    continue
                for s, seg in enumerate(para):
                    check_claim_unit(seg, f'{pw} explanation[{k}][{s}]', ctx, rep, core_claims)
            vis = expl.get('visual')
            if vis is not None:
                if not (isinstance(vis, dict) and vis.get('kind') and vis.get('ref')):
                    rep.error(f'{pw} visual', 'visual needs kind and ref')
                else:
                    check_text(vis.get('alt'), f'{pw} visual alt', rep)

    for v in range(1, counts[chapter] + 1):
        if (chapter, v) not in passage_seen:
            rep.error(where, f'verse {chapter}:{v} is in no passage')
        if (chapter, v) not in reading_seen:
            rep.error(where, f'verse {chapter}:{v} is in no reading')
    return data


def validate_index(index, lens_files, ctx, rep):
    where = '_lenses.json'
    if index.get('schemaVersion') != 1:
        rep.error(where, 'schemaVersion must be 1')
    if index.get('canonMapVersion') != ctx['canon_version']:
        rep.error(where, f'canonMapVersion != canon-map version {ctx["canon_version"]!r}')
    chapters = index.get('chapters')
    if not isinstance(chapters, list):
        rep.error(where, 'chapters must be a list')
        return
    listed = {}
    for i, ch in enumerate(chapters):
        n = ch.get('chapter')
        if n in listed:
            rep.error(where, f'chapter {n} listed twice')
        listed[n] = ch
        if ch.get('file') != f'chapter-{n}.json':
            rep.error(where, f'chapters[{i}].file must be "chapter-{n}.json"')
        data = lens_files.get(n)
        if data is None:
            rep.error(where, f'chapter {n} is listed but lenses/chapter-{n}.json is missing')
            continue
        lens = data.get('lens') or {}
        for key in ('status', 'version', 'signedOffBy', 'signedOffAt'):
            if ch.get(key) != lens.get(key):
                rep.error(where, f'chapter {n} {key} {ch.get(key)!r} != lens file {lens.get(key)!r}')
    for n in lens_files:
        if n not in listed:
            rep.error(where, f'lenses/chapter-{n}.json exists but is not listed')


# ---------------------------------------------------------------- staged guard

def forbidden_staged(paths):
    return [p for p in paths if STAGED_FORBIDDEN_RE.search(p)]


def staged_paths(root):
    out = subprocess.run(['git', '-C', str(root), 'diff', '--cached', '--name-only'],
                         capture_output=True, text=True, check=True)
    return [line for line in out.stdout.splitlines() if line.strip()]


# ---------------------------------------------------------------- driver

def validate(root, catalog_path=None, staged=False):
    root = Path(root)
    rep = Report()
    lens_dir = root / LENS_DIR
    counts = verse_counts(root)
    speakers = canon_speakers(root)

    if staged:
        try:
            bad = forbidden_staged(staged_paths(root))
        except (OSError, subprocess.CalledProcessError) as exc:
            rep.error('staged', f'cannot read git index: {exc}')
            bad = []
        for p in bad:
            rep.error('staged', f'{p} is staged: a lens commit must not touch layer-2 files')

    try:
        cmap = load_json(lens_dir / 'canon-map.json')
    except (OSError, json.JSONDecodeError) as exc:
        rep.error('canon-map.json', f'unreadable: {exc}')
        return rep
    by_verse = validate_canon_map(cmap, counts, speakers, rep)
    ctx = {
        'root': root, 'counts': counts, 'speakers': speakers, 'by_verse': by_verse,
        'rules': cmap.get('standingRules') or [], 'canon_version': cmap.get('version'),
        'claims_used': set(), 'catalog': None,
    }
    found = find_catalog(root, catalog_path)
    if found:
        ctx['catalog'] = load_catalog(found)

    lens_files = {}
    for path in sorted(lens_dir.glob('chapter-*.json')):
        m = LENS_FILE_RE.match(path.name)
        if m:
            data = validate_lens_file(path, ctx, rep)
            if data is not None:
                lens_files[int(m.group(1))] = data

    try:
        index = load_json(lens_dir / '_lenses.json')
        validate_index(index, lens_files, ctx, rep)
    except (OSError, json.JSONDecodeError) as exc:
        rep.error('_lenses.json', f'unreadable: {exc}')

    if ctx['claims_used']:
        if ctx['catalog'] is None:
            rep.error('core', 'core claims are referenced but core/model/catalog.json was not found; '
                              'pass --core-catalog or set WOH_CORE_CATALOG')
        else:
            for cid in sorted(ctx['claims_used']):
                if cid not in ctx['catalog']:
                    rep.error('core', f'{cid} does not exist in the core catalog')
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', default=str(ROOT), help='data-library root')
    ap.add_argument('--core-catalog', help='path to core/model/catalog.json')
    ap.add_argument('--staged', action='store_true',
                    help='also fail if genesis-woh/chapter-*.json is staged in git')
    ap.add_argument('--digest', type=int, metavar='N', help='print the layer-2 digest for chapter N')
    args = ap.parse_args(argv)
    if args.digest is not None:
        print(layer2_digest(args.root, args.digest))
        return 0
    rep = validate(args.root, args.core_catalog, args.staged)
    for w in rep.warnings:
        print(f'WARNING {w}')
    for e in rep.errors:
        print(f'ERROR {e}')
    print(f'{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)')
    return 1 if rep.errors else 0


if __name__ == '__main__':
    sys.exit(main())
