"""Reject the stale-media/timing combinations that cause paragraph seek drift."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_audio_release as release


class AudioRelease(unittest.TestCase):
    def check(self, media=b'narration', duration=10, expected_hash=None, paragraphs=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / 'audio/en/test'
            book.mkdir(parents=True)
            (book / 'c1.opus').write_bytes(media)
            version = expected_hash or hashlib.sha256(media).hexdigest()[:12]
            paragraphs = paragraphs or [{'n': 1, 'start': 0, 'end': 10}]
            (book / 'c1.timing.json').write_text(json.dumps({
                'duration_seconds': 10, 'paragraphs': paragraphs,
            }))
            url = f'audio/en/test/c1.opus?v={version}'
            manifest = book / 'manifest.json'
            manifest.write_text(json.dumps({'book': 'test', 'lang': 'en', 'chapters': [{
                'n': 1, 'duration_seconds': 10, 'paragraph_count': len(paragraphs),
                'audio_url': url, 'formats': [{'url': url}],
                'timing_url': 'audio/en/test/c1.timing.json',
            }]}))
            with patch.object(release, 'media_duration', return_value=duration):
                return release.validate(manifest, root, library_root=root)

    def test_matching_release_accepts_codec_padding(self):
        result = self.check(duration=10.026)
        self.assertEqual(result['errors'], [])
        self.assertEqual(len(result['checked']), 1)

    def test_accumulated_clip_drift_is_rejected(self):
        result = self.check(duration=8.4)
        self.assertTrue(any('differs from timing by -1.600s' in e for e in result['errors']))

    def test_replaced_media_requires_a_new_manifest_hash(self):
        result = self.check(expected_hash=hashlib.sha256(b'old narration').hexdigest()[:12])
        self.assertTrue(any('stale content hash' in e for e in result['errors']))

    def test_overlapping_paragraphs_are_rejected(self):
        result = self.check(paragraphs=[{'n': 1, 'start': 0, 'end': 6},
                                        {'n': 2, 'start': 5, 'end': 10}])
        self.assertTrue(any('overlapping interval' in e for e in result['errors']))


if __name__ == '__main__':
    unittest.main()
