"""Regression checks for source conservation and stable bilingual references."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

from apply_reviewed_alignment import ROOT, compact, digest, encode, prepare, transform, verify_text


class ReviewedAlignmentTests(unittest.TestCase):
    def fixture(self):
        data = {'paragraphs': [
            {'n': 1, 'refId': 'TEST-1:1', 'text': 'Source un.',
             'i18n': {'en': 'Wrong.', 'de': 'Andere.'}, 'speaker': 'Narrator'},
            {'n': 2, 'refId': 'TEST-1:2', 'text': 'Source deux.',
             'i18n': {'en': 'Misplaced.'}},
        ]}
        manifest = {'path': 'chapter.json', 'paragraphs': [
            {'n': 1, 'en': 'The complete passage.', 'kind': 'title',
             'alignment': {'status': 'group', 'refIds': ['TEST-1:1', 'TEST-1:2']}},
            {'n': 2, 'en': '', 'alignment': {'status': 'covered-by', 'refId': 'TEST-1:1'}},
        ], 'source': {'readingTextSha256': digest(compact('The complete passage.').encode())}}
        manifest['beforeSha256'] = digest(encode(data))
        manifest['afterSha256'] = digest(encode(transform(data, manifest)))
        return data, manifest

    def test_only_reviewed_language_and_metadata_change(self):
        data, manifest = self.fixture()
        original = copy.deepcopy(data)
        result = transform(data, manifest)
        self.assertEqual(data, original)
        for before, after in zip(data['paragraphs'], result['paragraphs']):
            for field in ('n', 'refId', 'text', 'speaker'):
                self.assertEqual(before.get(field), after.get(field))
            self.assertEqual(before['i18n'].get('de'), after['i18n'].get('de'))

    def test_language_specific_flow_preserves_source_kind(self):
        data, manifest = self.fixture()
        data['paragraphs'][0]['kind'] = 'body'
        del manifest['paragraphs'][0]['kind']
        manifest['paragraphs'][0]['kindByLang'] = {'en': 'continuation'}
        result = transform(data, manifest)
        self.assertEqual(result['paragraphs'][0]['kind'], 'body')
        self.assertEqual(result['paragraphs'][0]['kindByLang'], {'en': 'continuation'})

    def test_source_loss_is_rejected(self):
        _, manifest = self.fixture()
        manifest['paragraphs'][0]['en'] = 'The passage.'
        with self.assertRaisesRegex(ValueError, 'conserve'):
            verify_text(manifest)

    def test_idempotence_and_stale_source_guard(self):
        data, manifest = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / 'chapter.json'
            path.write_bytes(encode(data))
            _, raw, changed = prepare(root, manifest)
            self.assertTrue(changed)
            path.write_bytes(raw)
            self.assertFalse(prepare(root, manifest)[2])
            result = json.loads(raw)
            result['paragraphs'][0]['kind'] = 'body'
            path.write_bytes(encode(result))
            with self.assertRaisesRegex(ValueError, 'changed since review'):
                prepare(root, manifest)

    def test_duplicate_reference_is_rejected(self):
        data, manifest = self.fixture()
        manifest['paragraphs'][1]['n'] = 1
        with self.assertRaisesRegex(ValueError, 'Reference set'):
            transform(data, manifest)

    def test_shared_reference_must_exist(self):
        data, manifest = self.fixture()
        manifest['paragraphs'][1]['alignment']['refId'] = 'TEST-1:99'
        with self.assertRaisesRegex(ValueError, 'Unknown shared'):
            transform(data, manifest)

    def test_all_reviewed_chapters_are_applied_and_conserve_text(self):
        for path in sorted((ROOT / 'reviews/lwte-alignment-2026-10-18').glob('chapter-*.json')):
            with self.subTest(chapter=path.name):
                self.assertFalse(prepare(ROOT, json.loads(path.read_text()))[2])

    def test_cited_passages_and_edition_gaps(self):
        def paragraphs(c):
            return json.loads((ROOT / f'lets-welcome-the-extraterrestrials/chapter-{c}.json').read_text())['paragraphs']
        self.assertIn('There is no “God”, but there are the Elohim', paragraphs(1)[69]['i18n']['en'])
        self.assertIn('each human to be like a cell', paragraphs(2)[100]['i18n']['en'])
        self.assertIn('Joseph Smith', paragraphs(3)[26]['i18n']['en'])
        ch4 = paragraphs(4)
        self.assertIn('Kojiki', ch4[105]['i18n']['en'])
        self.assertIn('Nazca', ch4[108]['i18n']['en'])
        for n in (40, 41, 220, 312):
            self.assertEqual(ch4[n-1]['i18n']['en'], '')
            self.assertEqual(ch4[n-1]['alignment']['en']['status'], 'not-in-witness')


if __name__ == '__main__':
    unittest.main()
