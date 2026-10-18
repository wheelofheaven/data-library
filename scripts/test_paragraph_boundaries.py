"""Regression checks for reviewed boundary repairs and published reference data."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from repair_paragraph_boundaries import ROOT, apply_manifest, compact


class BoundaryRepairs(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / 'curation/2026-10-18-paragraph-boundaries.json').read_text())
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        paths = {o['path'] for o in self.manifest['textMoves'] + self.manifest['continuations']}
        self.current = {p: json.loads((ROOT / p).read_text()) for p in paths}
        self.before = copy.deepcopy(self.current)
        # Reconstruct the reviewed pre-repair corpus, including overlapping moves.
        for op in reversed(self.manifest['textMoves']):
            for n, text in zip(op['paragraphs'], op['before']):
                p = next(p for p in self.before[op['path']]['paragraphs'] if p['n'] == n)
                if op['language'] == 'fr':
                    p['text'] = text
                else:
                    p['i18n'][op['language']] = text
        for op in self.manifest['continuations']:
            p = next(p for p in self.before[op['path']]['paragraphs'] if p['n'] == op['paragraph'])
            p.pop('kind', None)
        self.write(self.before)

    def write(self, records):
        for path, data in records.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(data, ensure_ascii=False))

    def test_repair_preserves_all_words_and_references(self):
        result = apply_manifest(self.root, self.manifest)
        self.assertEqual(result, self.current)
        for path, after in result.items():
            before = self.before[path]['paragraphs']
            after = after['paragraphs']
            self.assertEqual([(p['n'], p['refId']) for p in before],
                             [(p['n'], p['refId']) for p in after])
            for lang in ['fr'] + list(before[0]['i18n']):
                def text(ps):
                    return compact(''.join(p['text'] if lang == 'fr' else p['i18n'][lang] for p in ps))
                self.assertEqual(text(before), text(after), (path, lang))
        self.write(result)
        self.assertEqual(apply_manifest(self.root, self.manifest), {})

    def test_changed_source_aborts_without_writing(self):
        op = self.manifest['textMoves'][0]
        data = self.before[op['path']]
        p = next(p for p in data['paragraphs'] if p['n'] == op['paragraphs'][0])
        p['i18n'][op['language']] += ' Changed after review.'
        self.write(self.before)
        snapshot = {p: (self.root / p).read_bytes() for p in self.before}
        with self.assertRaisesRegex(ValueError, 'Source changed'):
            apply_manifest(self.root, self.manifest)
        self.assertEqual(snapshot, {p: (self.root / p).read_bytes() for p in self.before})

    def test_published_books_have_consistent_references_counts_and_bundle(self):
        catalog = json.loads((ROOT / 'catalog.json').read_text())
        for slug in ['the-book-which-tells-the-truth', 'extraterrestrials-took-me-to-their-planet']:
            meta = json.loads((ROOT / slug / '_meta.json').read_text())
            total = 0
            bundle_path = ROOT / (slug + '.json')
            bundle = json.loads(bundle_path.read_text()) if bundle_path.exists() else None
            for chapter in meta['chapterFiles']:
                data = json.loads((ROOT / slug / chapter['file']).read_text())
                ps = data['paragraphs']
                self.assertEqual(len(ps), chapter['paragraphs'])
                self.assertEqual([p['n'] for p in ps], list(range(1, len(ps) + 1)))
                self.assertEqual(len({p['refId'] for p in ps}), len(ps))
                self.assertNotEqual(ps[0].get('kind'), 'continuation')
                if bundle:
                    self.assertEqual(bundle['chapters'][chapter['n'] - 1]['paragraphs'], ps)
                total += len(ps)
            self.assertEqual(meta['paragraphCount'], total)
            entry = next(b for b in catalog['books'] if b['slug'] == slug)
            self.assertEqual(entry['paragraphs'], total)


if __name__ == '__main__':
    unittest.main()
