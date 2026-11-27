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


def lens_chapter(digest):
    return {
        'schemaVersion': 1,
        'bookSlug': 'genesis-woh',
        'chapter': 1,
        'basedOn': {'translationVersion': '1.1.0', 'layer2Digest': digest, 'canonMapVersion': '1.0.0'},
        'lens': {'track': 'lens', 'version': '0.1.0', 'status': 'draft', 'modelDrafts': [],
                 'reviewerReport': {}, 'signedOffBy': None, 'signedOffAt': None,
                 'coreClaims': {'woh-claim-0009': '0.1.0'}},
        'passages': [
            {'id': 'gen-1-opening', 'range': ['1:1', '1:1'], 'title': {'en': 'Opening'},
             'canonCoverage': 'quotes',
             'readings': [dict(segment('The Elohim began to shape the land.', 'framework',
                                       ['TBWTT-2:2'], 'woh-claim-0009'), refs=['1:1'], basis='canon')],
             'explanation': {'paragraphs': [[
                 segment('The Hebrew word is plural in form.', 'direct'),
                 segment('The canon reads it as a people from the sky.', 'framework', ['TBWTT-2:3'])]]}},
            {'id': 'gen-1-light', 'range': ['1:2', '1:3'], 'title': {'en': 'Light'},
             'canonCoverage': 'silent',
             'readings': [dict(segment('The land lay empty; then light.', 'inferred'),
                               refs=['1:2-3'], basis='synthesis')],
             'explanation': {'paragraphs': [[
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
        self.index = {'schemaVersion': 1, 'bookSlug': 'genesis-woh', 'canonMapVersion': '1.0.0',
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
        p['readings'][0]['refs'] = ['1:2']
        self.assertFails('verse 1:3 is in no passage')
        self.assertFails('verse 1:3 is in no reading')

    def test_overlapping_passages(self):
        self.fx.lens['passages'][1]['range'] = ['1:1', '1:3']
        self.assertFails('already in passage')

    def test_verse_in_two_readings(self):
        self.fx.lens['passages'][1]['readings'].append(
            dict(segment('Again.', 'inferred'), refs=['1:3'], basis='synthesis'))
        self.assertFails('already rendered by another reading')

    def test_reading_outside_passage(self):
        self.fx.lens['passages'][0]['readings'][0]['refs'] = ['1:1-2']
        self.assertFails('outside the passage range')

    def test_canon_coverage_must_match_map(self):
        self.fx.lens['passages'][1]['canonCoverage'] = 'comments'
        self.assertFails("canon map gives 'silent'")

    # -- canon refs
    def test_unknown_canon_ref(self):
        self.fx.lens['passages'][0]['explanation']['paragraphs'][0][1]['canon'] = ['TBWTT-2:99']
        self.assertFails('does not exist in the canon chapter files')

    def test_lwte_needs_author_opinion_label(self):
        self.fx.lens['passages'][1]['explanation']['paragraphs'][0][0]['canon'] = ['LWTE-1:1']
        self.assertFails('author-opinion')

    def test_lwte_never_sole_basis_of_framework(self):
        seg = self.fx.lens['passages'][1]['explanation']['paragraphs'][0][0]
        seg['claim'] = 'framework'
        seg['coreClaim'] = 'woh-claim-0009'
        self.assertFails('rests only on non-canon refs')

    def test_framework_with_canon_plus_lwte_passes(self):
        seg = self.fx.lens['passages'][0]['explanation']['paragraphs'][0][1]
        seg['canon'] = ['TBWTT-2:3', {'ref': 'LWTE-1:1', 'standing': 'author-opinion'}]
        self.assertEqual(self.fx.run().errors, [])

    def test_check_standing_must_be_written_out(self):
        seg = self.fx.lens['passages'][1]['explanation']['paragraphs'][0][0]
        seg['canon'] = ['ETTMTTP-3:1']
        self.assertFails("standing is 'check'")

    def test_framework_without_any_grounding(self):
        seg = self.fx.lens['passages'][0]['explanation']['paragraphs'][0][1]
        del seg['canon']
        self.assertFails('needs a canon-standing ref or a coreClaim')

    def test_canon_basis_needs_mapped_ref(self):
        self.fx.lens['passages'][0]['readings'][0]['canon'] = ['ETTMTTP-2:1']
        self.assertFails('none of its canon refs is mapped')

    # -- core claims
    def test_core_claim_missing_from_catalog(self):
        self.fx.lens['lens']['coreClaims']['woh-claim-9999'] = '0.1.0'
        self.assertFails('woh-claim-9999 does not exist in the core catalog')

    def test_core_claim_not_pinned_in_lens(self):
        self.fx.lens['passages'][0]['readings'][0]['coreClaim'] = 'woh-claim-0001'
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


class RealDataTests(unittest.TestCase):
    """The committed canon map must validate against the real corpus."""

    def test_repository_canon_map(self):
        rep = v.validate(v.ROOT, v.find_catalog(v.ROOT))
        self.assertEqual([e for e in rep.errors if e.startswith('canon-map.json')], [])


if __name__ == '__main__':
    unittest.main()
