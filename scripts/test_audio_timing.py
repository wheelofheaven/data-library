"""Exercise real MP3 padding and mixed-rate clips without any TTS API calls."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from generate_audio import bound_word_timings, ffmpeg_concat, ffmpeg_silence, prepare_concat_piece


class WordTimingBounds(unittest.TestCase):
    def test_provider_alignment_stays_inside_playable_clip(self):
        paragraph = {'start': 10.0, 'end': 11.0, 'words': [
            {'w': 'first', 'start': 9.98, 'end': 10.4},
            {'w': 'last', 'start': 10.8, 'end': 11.162},
        ]}
        bound_word_timings(paragraph)
        self.assertEqual(paragraph['words'], [
            {'w': 'first', 'start': 10.0, 'end': 10.4},
            {'w': 'last', 'start': 10.8, 'end': 11.0},
        ])


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'requires FFmpeg')
class AudioTiming(unittest.TestCase):
    def tone(self, path, seconds, rate):
        subprocess.run([
            'ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi',
            '-i', f'sine=frequency=440:sample_rate={rate}', '-t', str(seconds),
            '-c:a', 'libmp3lame', '-b:a', '128k', str(path),
        ], check=True, capture_output=True)

    def decoded_duration(self, path):
        result = subprocess.run([
            'ffmpeg', '-v', 'error', '-i', str(path), '-ar', '44100', '-ac', '1',
            '-f', 's16le', 'pipe:1',
        ], check=True, capture_output=True)
        return len(result.stdout) / (44100 * 2)

    def test_repeated_mixed_rate_clips_do_not_accumulate_mp3_padding(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, second = root / 'first.mp3', root / 'second.mp3'
            self.tone(first, 0.17, 22050)
            self.tone(second, 0.23, 44100)
            a, da = prepare_concat_piece(first)
            b, db = prepare_concat_piece(second)
            silence = root / 'silence.mp3'
            ffmpeg_silence(silence, 0.07)
            s, ds = prepare_concat_piece(silence)
            output = root / 'chapter.mp3'
            repetitions = 30
            ffmpeg_concat([a, s, b, s] * repetitions, output, reencode=True)
            expected = (da + ds + db + ds) * repetitions
            actual = self.decoded_duration(output)
            self.assertAlmostEqual(actual, expected, delta=0.002)

    def test_replaced_narration_invalidates_decoded_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'paragraph.mp3'
            self.tone(source, 0.2, 44100)
            decoded, before = prepare_concat_piece(source)
            timestamp = decoded.stat().st_mtime_ns
            self.assertEqual(prepare_concat_piece(source), (decoded, before))
            self.assertEqual(decoded.stat().st_mtime_ns, timestamp)
            self.tone(source, 0.4, 44100)
            _, after = prepare_concat_piece(source)
            self.assertAlmostEqual(after - before, 0.2, delta=0.002)


if __name__ == '__main__':
    unittest.main()
