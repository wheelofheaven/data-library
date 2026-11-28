"""Tests for validate_genesis_lenses.py using a tiny fixture corpus in a temp dir.

Run: python3 -m unittest discover -s scripts -p 'test_validate_genesis_lenses.py'
"""
import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import validate_genesis_lenses as v

LAYER2 = {
    1: ['When the Elohim began to shape the skies and the land—', 'The land was empty.', 'Let there be light.'],
    2: ['The skies were finished.', 'They rested.'],
}

CANON = {
    'the-book-which-tells-the-truth': ('TBWTT', [
        (2, [('Narrator', 'He began to speak.'),
             ('Yahweh', 'Take Genesis first: «In the beginning Elohim created».'),
             ('Yahweh', 'Elohim means those who came from the sky.')]),
    ]),
    'extraterrestrials-took-me-to-their-planet': ('ETTMTTP', [
        (2, [('Yahweh', 'A dictated paragraph.')]),
        (3, [('Yahweh', 'A Keys paragraph.')]),
    ]),
    'lets-welcome-the-extraterrestrials': ('LWTE', [
        (1, [('Narrator', 'Author commentary on the light.')]),
    ]),
}

RULES = [
    {'book': 'TBWTT', 'speaker': 'Yahweh', 'standing': 'canon'},
    {'book': 'TBWTT', 'speaker': '*', 'standing': 'narration'},
    {'book': 'ETTMTTP', 'chapter': 2, 'speaker': 'Yahweh', 'standing': 'canon'},
    {'book': 'ETTMTTP', 'chapter': 3, 'speaker': '*', 'standing': 'check'},
    {'book': 'ETTMTTP', 'speaker': '*', 'standing': 'narration'},
    {'book': 'LWTE', 'speaker': '*', 'standing': 'author-opinion'},
]

CANON_MAP = {
    'version': '1.0.0',
    'bookSlug': 'genesis-woh',
    'standingRules': RULES,
    'entries': [
        {'range': ['1:1', '1:1'], 'relation': 'quotes', 'refs': [
            {'ref': 'TBWTT-2:2', 'relation': 'quotes', 'standing': 'canon'},
            {'ref': 'TBWTT-2:3', 'relation': 'comments', 'standing': 'canon'}]},
        {'range': ['1:2', '1:2'], 'relation': 'silent', 'refs': []},
        {'range': ['1:3', '1:3'], 'relation': 'opinion', 'refs': [
            {'ref': 'LWTE-1:1', 'relation': 'opinion', 'standing': 'author-opinion'}]},
        {'range': ['2:1', '2:2'], 'relation': 'silent', 'refs': []},
    ],
}

CATALOG = {'catalog_version': '1', 'claims': [
    {'id': 'woh-claim-0001', 'version': '0.2.0'},
    {'id': 'woh-claim-0009', 'version': '0.1.0'},
]}


def segment(text, claim, canon=None, core=None):
    s = {'text': {'en': text}, 'claim': claim}
    if canon is not None:
        s['canon'] = canon
    if core:
        s['coreClaim'] = core
    return s


def decoded(text, *refs):
    return {'refs': list(refs), 'text': {'en': text}}


def lens_chapter(digest):
    return {
        'schemaVersion': 2,
        'bookSlug': 'genesis-woh',
        'chapter': 1,
        'basedOn': {'translationVersion': '1.1.0', 'layer2Digest': digest, 'canonMapVersion': '1.0.0'},
        'lens': {'track': 'lens', 'version': '0.1.0', 'status': 'draft', 'modelDrafts': [],
                 'reviewerReport': {}, 'signedOffBy': None, 'signedOffAt': None,
                 'coreClaims': {'woh-claim-0009': '0.1.0'}},
        'passages': [
            {'id': 'gen-1-opening', 'range': ['1:1', '1:1'], 'title': {'en': 'Opening'},
             'canonCoverage': 'quotes',
             'decoded': [],
             'meaning': [dict(segment('The Elohim began to shape the land.', 'framework',
                                       ['TBWTT-2:2'], 'woh-claim-0009'), refs=['1:1'], basis='canon')],
             'note': {'paragraphs': [[
                 segment('The Hebrew word is plural in form.', 'direct'),
                 segment('The canon reads it as a people from the sky.', 'framework', ['TBWTT-2:3'])]]}},
            {'id': 'gen-1-light', 'range': ['1:2', '1:3'], 'title': {'en': 'Light'},
             'canonCoverage': 'silent',
             'decoded': [],
             'meaning': [dict(segment('The land lay empty; then light.', 'inferred'),
                               refs=['1:2-3'], basis='synthesis')],
             'note': {'paragraphs': [[
                 segment('Raël reads this as a remark on light.', 'inferred',
                         [{'ref': 'LWTE-1:1', 'standing': 'author-opinion'}])]]}},
        ],
    }


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


class Fixture:
    def __init__(self, base):
        self.root = Path(base)
        for n, verses in LAYER2.items():
            write(self.root / 'genesis-woh' / f'chapter-{n}.json', {
                'n': n, 'translation': {'version': '1.1.0'},
                'paragraphs': [{'n': i, 'refId': f'GEN-WOH-{n}:{i}', 'i18n': {'en': t}}
                               for i, t in enumerate(verses, 1)]})
        for slug, (code, chapters) in CANON.items():
            for ch, paras in chapters:
                write(self.root / slug / f'chapter-{ch}.json', {'paragraphs': [
                    {'n': i, 'refId': f'{code}-{ch}:{i}', 'speaker': sp, 'i18n': {'en': t}}
                    for i, (sp, t) in enumerate(paras, 1)]})
        self.catalog = self.root / 'catalog.json'
        write(self.catalog, CATALOG)
        self.lens_dir = self.root / 'genesis-woh' / 'lenses'
        self.canon_map = copy.deepcopy(CANON_MAP)
        self.lens = lens_chapter(v.layer2_digest(self.root, 1))
        self.index = {'schemaVersion': 2, 'bookSlug': 'genesis-woh', 'canonMapVersion': '1.0.0',
                      'chapters': [{'chapter': 1, 'file': 'chapter-1.json', 'status': 'draft',
                                    'version': '0.1.0', 'signedOffBy': None, 'signedOffAt': None}]}

    def run(self, staged=False, with_lens=True):
        write(self.lens_dir / 'canon-map.json', self.canon_map)
        write(self.lens_dir / '_lenses.json', self.index)
        lens_path = self.lens_dir / 'chapter-1.json'
        if with_lens:
            write(lens_path, self.lens)
        elif lens_path.exists():
            lens_path.unlink()
        return v.validate(self.root, self.catalog, staged)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.fx = Fixture(self.tmp.name)

    def assertFails(self, needle, **kw):
        rep = self.fx.run(**kw)
        joined = '\n'.join(rep.errors)
        self.assertTrue(any(needle in e for e in rep.errors),
                        f'expected an error containing {needle!r}; got:\n{joined}')

    # -- valid
    def test_valid_fixture_passes(self):
        rep = self.fx.run()
        self.assertEqual(rep.errors, [])
        self.assertEqual(rep.warnings, [])

    def test_empty_index_without_lens_files_passes(self):
        self.fx.index['chapters'] = []
        rep = self.fx.run(with_lens=False)
        self.assertEqual(rep.errors, [])

    # -- digest
    def test_digest_definition(self):
        import hashlib
        text = '\n'.join(f'1:{i}\t{t}' for i, t in enumerate(LAYER2[1], 1)).encode('utf-8')
        self.assertEqual(v.layer2_digest(self.fx.root, 1), 'sha256:' + hashlib.sha256(text).hexdigest())

    def test_stale_digest_is_warning_for_draft(self):
        self.fx.lens['basedOn']['layer2Digest'] = 'sha256:' + '0' * 64
        rep = self.fx.run()
        self.assertEqual(rep.errors, [])
        self.assertTrue(any('STALE' in w for w in rep.warnings))

    def test_stale_digest_is_error_when_approved(self):
        self.fx.lens['basedOn']['layer2Digest'] = 'sha256:' + '0' * 64
        self.fx.lens['lens']['status'] = 'reviewer-approved'
        self.fx.index['chapters'][0]['status'] = 'reviewer-approved'
        self.assertFails('STALE')

    def test_translation_version_mismatch(self):
        self.fx.lens['basedOn']['translationVersion'] = '1.0.0'
        self.assertFails('translationVersion')

    def test_canon_map_version_mismatch(self):
        self.fx.lens['basedOn']['canonMapVersion'] = '0.9.0'
        self.assertFails('canonMapVersion')

    # -- coverage
    def test_verse_missing_from_passages_and_readings(self):
        p = self.fx.lens['passages'][1]
        p['range'] = ['1:2', '1:2']
        p['meaning'][0]['refs'] = ['1:2']
        self.assertFails('verse 1:3 is in no passage')
        self.assertFails('verse 1:3 is in no Meaning unit')

    def test_overlapping_passages(self):
        self.fx.lens['passages'][1]['range'] = ['1:1', '1:3']
        self.assertFails('already in passage')

    def test_verse_in_two_readings(self):
        self.fx.lens['passages'][1]['meaning'].append(
            dict(segment('Again.', 'inferred'), refs=['1:3'], basis='synthesis'))
        self.assertFails('already rendered by another Meaning unit')

    def test_reading_outside_passage(self):
        self.fx.lens['passages'][0]['meaning'][0]['refs'] = ['1:1-2']
        self.assertFails('outside the passage range')

    def test_canon_coverage_must_match_map(self):
        self.fx.lens['passages'][1]['canonCoverage'] = 'comments'
        self.assertFails("canon map gives 'silent'")

    # -- canon refs
    def test_unknown_canon_ref(self):
        self.fx.lens['passages'][0]['note']['paragraphs'][0][1]['canon'] = ['TBWTT-2:99']
        self.assertFails('does not exist in the canon chapter files')

    def test_lwte_needs_author_opinion_label(self):
        self.fx.lens['passages'][1]['note']['paragraphs'][0][0]['canon'] = ['LWTE-1:1']
        self.assertFails('author-opinion')

    def test_lwte_never_sole_basis_of_framework(self):
        seg = self.fx.lens['passages'][1]['note']['paragraphs'][0][0]
        seg['claim'] = 'framework'
        seg['coreClaim'] = 'woh-claim-0009'
        self.assertFails('rests only on non-canon refs')

    def test_framework_with_canon_plus_lwte_passes(self):
        seg = self.fx.lens['passages'][0]['note']['paragraphs'][0][1]
        seg['canon'] = ['TBWTT-2:3', {'ref': 'LWTE-1:1', 'standing': 'author-opinion'}]
        self.assertEqual(self.fx.run().errors, [])

    def test_check_standing_must_be_written_out(self):
        seg = self.fx.lens['passages'][1]['note']['paragraphs'][0][0]
        seg['canon'] = ['ETTMTTP-3:1']
        self.assertFails("standing is 'check'")

    def test_framework_without_any_grounding(self):
        seg = self.fx.lens['passages'][0]['note']['paragraphs'][0][1]
        del seg['canon']
        self.assertFails('needs a canon-standing ref or a coreClaim')

    def test_canon_basis_needs_mapped_ref(self):
        self.fx.lens['passages'][0]['meaning'][0]['canon'] = ['ETTMTTP-2:1']
        self.assertFails('none of its canon refs is mapped')

    # -- core claims
    def test_core_claim_missing_from_catalog(self):
        self.fx.lens['lens']['coreClaims']['woh-claim-9999'] = '0.1.0'
        self.assertFails('woh-claim-9999 does not exist in the core catalog')

    def test_core_claim_not_pinned_in_lens(self):
        self.fx.lens['passages'][0]['meaning'][0]['coreClaim'] = 'woh-claim-0001'
        self.assertFails('not listed in lens.coreClaims')

    def test_core_claim_version_drift_warns(self):
        self.fx.lens['lens']['coreClaims']['woh-claim-0009'] = '0.0.9'
        rep = self.fx.run()
        self.assertEqual(rep.errors, [])
        self.assertTrue(any('re-check the binding' in w for w in rep.warnings))

    # -- sign-off
    def test_stable_requires_signoff(self):
        self.fx.lens['lens']['status'] = 'stable'
        self.fx.index['chapters'][0]['status'] = 'stable'
        self.assertFails('stable requires lens.signedOffBy')
        self.assertFails('stable requires lens.signedOffAt')

    def test_stable_with_signoff_passes(self):
        for d in (self.fx.lens['lens'], self.fx.index['chapters'][0]):
            d.update(status='stable', signedOffBy='founder', signedOffAt='2026-12-01')
        self.assertEqual(self.fx.run().errors, [])

    def test_prerelease_version_allowed_before_signoff(self):
        for d in (self.fx.lens['lens'], self.fx.index['chapters'][0]):
            d.update(version='1.1.0-rc1', status='editor-review')
        self.assertEqual(self.fx.run().errors, [])

    def test_prerelease_version_rejected_when_stable(self):
        for d in (self.fx.lens['lens'], self.fx.index['chapters'][0]):
            d.update(version='1.1.0-rc1', status='stable', signedOffBy='founder', signedOffAt='2026-12-01')
        self.assertFails('cannot carry a pre-release tag')

    def test_malformed_version_rejected(self):
        for d in (self.fx.lens['lens'], self.fx.index['chapters'][0]):
            d['version'] = '1.1'
        self.assertFails('lens.version must be semver')

    # -- index
    def test_index_must_list_lens_files(self):
        self.fx.index['chapters'] = []
        self.assertFails('exists but is not listed')

    def test_index_must_match_lens_status(self):
        self.fx.index['chapters'][0]['status'] = 'stable'
        self.assertFails('chapter 1 status')

    # -- canon map
    def test_canon_map_gap(self):
        self.fx.canon_map['entries'].pop()
        self.assertFails('verse 2:1 is not covered')

    def test_canon_map_overlap(self):
        self.fx.canon_map['entries'][1]['range'] = ['1:1', '1:2']
        self.assertFails('already covered')

    def test_canon_map_silent_with_refs(self):
        self.fx.canon_map['entries'][1]['refs'] = [
            {'ref': 'TBWTT-2:2', 'relation': 'alludes', 'standing': 'canon'}]
        self.assertFails('silent entries must have empty refs')

    def test_canon_map_lwte_standing(self):
        self.fx.canon_map['entries'][2]['refs'][0]['standing'] = 'canon'
        self.assertFails('LWTE refs must carry standing "author-opinion"')

    def test_canon_map_unknown_ref(self):
        self.fx.canon_map['entries'][0]['refs'][0]['ref'] = 'TBWTT-9:1'
        self.assertFails('paragraph does not exist')

    def test_canon_map_relation_consistency(self):
        self.fx.canon_map['entries'][0]['relation'] = 'comments'
        self.assertFails("should be 'quotes'")

    def test_canon_map_rejects_narration(self):
        self.fx.canon_map['entries'][0]['refs'].append(
            {'ref': 'TBWTT-2:1', 'relation': 'comments', 'standing': 'narration'})
        self.assertFails('narration paragraphs are not canon')

    # -- staged guard
    def test_forbidden_staged_pattern(self):
        self.assertEqual(v.forbidden_staged([
            'genesis-woh/chapter-1.json', 'genesis-woh/lenses/chapter-1.json',
            'genesis-woh/lenses/canon-map.json', 'exodus-woh/chapter-1.json']),
            ['genesis-woh/chapter-1.json'])

    def test_staged_mode_against_git_index(self):
        root = self.fx.root
        git = ['git', '-C', str(root), '-c', 'user.name=t', '-c', 'user.email=t@example.invalid']
        subprocess.run(git + ['init', '-q'], check=True)
        self.fx.run()  # write fixture files
        subprocess.run(git + ['add', 'genesis-woh/lenses'], check=True)
        self.assertEqual(self.fx.run(staged=True).errors, [])
        subprocess.run(git + ['add', 'genesis-woh/chapter-1.json'], check=True)
        self.assertFails('is staged', staged=True)

    def test_cli_digest(self):
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = v.main(['--root', str(self.fx.root), '--digest', '1'])
        self.assertEqual(code, 0)
        self.assertEqual(buf.getvalue().strip(), v.layer2_digest(self.fx.root, 1))


class DecodedTests(unittest.TestCase):
    """Lens 3 (decoded): optional per chapter, complete once started."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.fx = Fixture(self.tmp.name)
        p0, p1 = self.fx.lens['passages']
        p0['decoded'] = [decoded('When the Elohim began to shape the skies and the land—', '1:1')]
        p1['decoded'] = [decoded('The land was empty.', '1:2'), decoded('Let there be light.', '1:3')]

    def assertFails(self, needle):
        rep = self.fx.run()
        joined = '\n'.join(rep.errors)
        self.assertTrue(any(needle in e for e in rep.errors),
                        f'expected an error containing {needle!r}; got:\n{joined}')

    def test_full_decoded_chapter_passes(self):
        rep = self.fx.run()
        self.assertEqual(rep.errors, [])
        self.assertEqual(rep.warnings, [])

    def test_empty_decoded_passes(self):
        for p in self.fx.lens['passages']:
            p['decoded'] = []
        self.assertEqual(self.fx.run().errors, [])

    def test_decoded_must_be_present(self):
        del self.fx.lens['passages'][0]['decoded']
        self.assertFails('decoded must be present')

    def test_partial_decoded_chapter_fails(self):
        self.fx.lens['passages'][1]['decoded'] = []
        self.assertFails('verse 1:2 is in no decoded unit')
        self.assertFails('verse 1:3 is in no decoded unit')

    def test_decoded_verse_twice(self):
        self.fx.lens['passages'][1]['decoded'].append(decoded('Again.', '1:3'))
        self.assertFails('already rendered by another decoded unit')

    def test_decoded_outside_passage(self):
        self.fx.lens['passages'][0]['decoded'][0]['refs'] = ['1:1-2']
        self.fx.lens['passages'][1]['decoded'].pop(0)
        self.assertFails('outside the passage range')

    def test_decoded_bad_ref(self):
        self.fx.lens['passages'][0]['decoded'][0]['refs'] = ['2:1']
        self.assertFails('outside chapter 1')

    def test_decoded_needs_text(self):
        self.fx.lens['passages'][0]['decoded'][0]['text'] = {'en': ' '}
        self.assertFails('decoded[0] text')

    def test_decoded_rejects_claim_fields(self):
        self.fx.lens['passages'][0]['decoded'][0]['claim'] = 'framework'
        self.assertFails('a decoded unit is refs and text only')

    def test_decoded_group_across_cards_warns(self):
        p1 = self.fx.lens['passages'][1]
        p1['meaning'] = [dict(segment('The land lay empty.', 'inferred'), refs=['1:2'], basis='synthesis'),
                         dict(segment('Then light.', 'inferred'), refs=['1:3'], basis='synthesis')]
        p1['decoded'] = [decoded('The land was empty. Let there be light.', '1:2-3')]
        rep = self.fx.run()
        self.assertEqual(rep.errors, [])
        self.assertTrue(any('another Meaning card' in w for w in rep.warnings))

    def test_v1_names_rejected(self):
        p0 = self.fx.lens['passages'][0]
        p0['readings'] = p0.pop('meaning')
        self.assertFails('"readings" is the schemaVersion 1 name')

    def test_v1_schema_version_rejected(self):
        self.fx.lens['schemaVersion'] = 1
        self.assertFails('migrate_genesis_lenses_v2.py')

    def test_glossary_hook_loads(self):
        gl = self.fx.root / 'decoding-glossary.json'
        write(gl, {'terms': []})
        self.fx.run()
        rep = v.validate(self.fx.root, self.fx.catalog, glossary_path=gl)
        self.assertEqual(rep.errors, [])

    def test_glossary_hook_unreadable(self):
        self.fx.run()
        rep = v.validate(self.fx.root, self.fx.catalog, glossary_path=self.fx.root / 'missing.json')
        self.assertTrue(any('unreadable decoding glossary' in e for e in rep.errors))


class MigrationTests(unittest.TestCase):
    def test_v1_to_v2_is_lossless_and_ordered(self):
        import migrate_genesis_lenses_v2 as mig
        v2 = lens_chapter('sha256:' + '0' * 64)
        v1 = mig.back_to_v1(v2)
        self.assertEqual(v1['schemaVersion'], 1)
        self.assertIn('readings', v1['passages'][0])
        out, did = mig.migrate_chapter(v1)
        self.assertTrue(did)
        self.assertEqual(out, v2)
        self.assertEqual(list(out['passages'][0])[4:], ['decoded', 'meaning', 'note'])
        self.assertEqual(mig.back_to_v1(out), v1)
        again, did = mig.migrate_chapter(out)
        self.assertFalse(did)
        self.assertIs(again, out)

    def test_migrate_dir(self):
        import migrate_genesis_lenses_v2 as mig
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            v1 = mig.back_to_v1(lens_chapter('sha256:' + '0' * 64))
            write(d / 'chapter-1.json', v1)
            write(d / '_lenses.json', {'schemaVersion': 1, 'chapters': []})
            import io
            from contextlib import redirect_stdout
            with redirect_stdout(io.StringIO()):
                self.assertEqual(mig.main(['--dir', str(d)]), 0)
            got = json.loads((d / 'chapter-1.json').read_text(encoding='utf-8'))
            self.assertEqual(got['schemaVersion'], 2)
            self.assertEqual(got['passages'][1]['decoded'], [])
            self.assertEqual(json.loads((d / '_lenses.json').read_text())['schemaVersion'], 2)


class RealDataTests(unittest.TestCase):
    """The committed canon map must validate against the real corpus."""

    def test_repository_canon_map(self):
        rep = v.validate(v.ROOT, v.find_catalog(v.ROOT))
        self.assertEqual([e for e in rep.errors if e.startswith('canon-map.json')], [])

    def test_repository_lens_files(self):
        # Core-catalog errors depend on a sibling core/ checkout; the rest
        # must be clean on the committed lens files.
        rep = v.validate(v.ROOT, v.find_catalog(v.ROOT))
        self.assertEqual([e for e in rep.errors if not e.startswith('core:')], [])


if __name__ == '__main__':
    unittest.main()
