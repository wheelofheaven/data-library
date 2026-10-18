"""A cached-only pause repair must invalidate the playback manifest too."""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import generate_audio as audio


class ManifestRefresh(unittest.TestCase):
    def run_generation(self, dry_run=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / 'test-book'
            book.mkdir()
            (book / '_meta.json').write_text(json.dumps({'chapterCount': 1}))
            stats = dict(chars=100, paragraphs=2, skipped_paragraphs=0,
                         cached_paragraphs=2, new_paragraphs=0,
                         duration_seconds=19.4, estimated_cost=0,
                         chapter_mp3='test-book/c1.mp3')
            argv = ['generate_audio.py', '--slug', 'test-book', '--lang', 'en']
            if dry_run:
                argv.append('--dry-run')
            with (patch.object(audio, 'LIB', root),
                  patch.object(audio, 'load_voices_config', return_value={}),
                  patch.object(audio, 'load_treatments_config', return_value={}),
                  patch.object(audio, 'load_normalize_filter', return_value=''),
                  patch.object(audio, 'load_audioplay_manifest', return_value={}),
                  patch.object(audio, 'generate_chapter', return_value=stats),
                  patch.object(audio, 'update_book_manifest') as update,
                  patch.dict(os.environ, {'ELEVENLABS_API_KEY': 'test-only'}),
                  patch('sys.argv', argv), contextlib.redirect_stdout(io.StringIO())):
                audio.main()
                return update.call_args_list

    def test_cached_only_render_refreshes_manifest(self):
        calls = self.run_generation()
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0].args[:2], ('test-book', 'en'))

    def test_dry_run_does_not_refresh_manifest(self):
        self.assertEqual(self.run_generation(dry_run=True), [])

    def test_local_oversized_mp3_is_not_advertised(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / 'en' / 'test-book'
            book.mkdir(parents=True)
            (book / 'c1.timing.json').write_text(json.dumps({
                'chapter': 1, 'duration_seconds': 3000, 'paragraphs': [],
            }))
            (book / 'c1.opus').write_bytes(b'published-opus')
            with (book / 'c1.mp3').open('wb') as master:
                master.truncate(25 * 1024 * 1024 + 1)
            with patch.object(audio, 'ASSETS_AUDIO', root), patch.object(audio, 'LIB', root):
                audio.update_book_manifest('test-book', 'en', {})
            entry = json.loads((book / 'manifest.json').read_text())['chapters'][0]
            self.assertEqual([f['type'] for f in entry['formats']], ['audio/ogg; codecs=opus'])
            self.assertEqual(entry['audio_url'], entry['formats'][0]['url'])


if __name__ == '__main__':
    unittest.main()
