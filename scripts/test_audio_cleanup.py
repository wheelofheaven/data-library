"""Cleanup must retain paid synthesis and reject unverified replacements."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import cleanup_audio_intermediates as cleanup


class AudioCleanupTests(unittest.TestCase):
    def fixture(self, directory):
        root = Path(directory) / 'data-library'
        assets = root.parent / 'assets.wheelofheaven.world'
        book = assets / 'audio/fr/book'
        book.mkdir(parents=True)
        media = book / 'c1.opus'
        media.write_bytes(b'verified delivery')
        manifest = book / 'manifest.json'
        manifest.write_text('{}')
        work = root / 'audio/_work/book/fr/c1'
        work.mkdir(parents=True)
        for suffix in ('mp3', 'alignment.json', 'meta.json', 'treated.mp3', 'treated.concat.wav'):
            (work / f'p1.{suffix}').write_text('cached')
        report = root / 'report.json'
        report.write_text(json.dumps({'book': 'book', 'language': 'fr',
            'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(),
            'chapters': [{'chapter': 1, 'assets': [{'path': 'audio/fr/book/c1.opus',
                'sha256': hashlib.sha256(media.read_bytes()).hexdigest()}]}]}))
        return root, work, report, media

    def test_paid_originals_are_never_cleanup_candidates(self):
        with tempfile.TemporaryDirectory() as directory:
            root, work, report, _ = self.fixture(directory)
            with patch.object(cleanup, 'ROOT', root):
                paths = cleanup.candidates(report)
            self.assertEqual({p.name for p in paths}, {'p1.treated.mp3', 'p1.treated.concat.wav'})
            for path in paths:
                path.unlink()
            self.assertTrue(all((work / f'p1.{suffix}').exists() for suffix in ('mp3', 'alignment.json', 'meta.json')))

    def test_changed_delivery_or_missing_paid_cache_blocks_cleanup(self):
        with tempfile.TemporaryDirectory() as directory:
            root, work, report, media = self.fixture(directory)
            with patch.object(cleanup, 'ROOT', root):
                media.write_bytes(b'unverified replacement')
                with self.assertRaisesRegex(ValueError, 'Delivery asset changed'):
                    cleanup.candidates(report)
                media.write_bytes(b'verified delivery')
                (work / 'p1.alignment.json').unlink()
                with self.assertRaisesRegex(ValueError, 'Missing provider cache'):
                    cleanup.candidates(report)
            self.assertTrue((work / 'p1.treated.mp3').exists())


if __name__ == '__main__':
    unittest.main()
