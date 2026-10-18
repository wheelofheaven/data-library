"""Ambient scene boundaries retain gaps and total duration after assembly."""
import contextlib
import io
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import generate_ambient as ambient


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'requires FFmpeg')
class AmbientTiming(unittest.TestCase):
    def test_scenes_with_silence_gaps_keep_the_voice_timeline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scene = dict(ambient_prompt='test-tone', ambient_duration_seconds=0.2, gain_db=-18)
            bed = root / (ambient.sfx_cache_key('test-tone', 0.2) + '.mp3')
            subprocess.run([
                'ffmpeg', '-y', '-v', 'error', '-f', 'lavfi',
                '-i', 'sine=frequency=440:sample_rate=44100', '-t', '0.2',
                '-c:a', 'libmp3lame', str(bed),
            ], check=True, capture_output=True)
            spans = [dict(scene='a', start=0.1, end=0.35),
                     dict(scene='b', start=0.4, end=0.9)]
            output = root / 'chapter.ambient.opus'
            with patch.object(ambient, 'SFX_CACHE', root), contextlib.redirect_stdout(io.StringIO()):
                result = ambient.build_chapter_ambient(spans, {'a': scene, 'b': scene}, 1.2, '', output)
            self.assertTrue(result['wrote'])
            decoded = subprocess.run([
                'ffmpeg', '-v', 'error', '-i', str(output), '-ar', '48000',
                '-ac', '2', '-f', 's16le', 'pipe:1',
            ], check=True, capture_output=True).stdout
            self.assertAlmostEqual(len(decoded) / (48000 * 2 * 2), 1.2, delta=0.002)


if __name__ == '__main__':
    unittest.main()
