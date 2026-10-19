"""Narration exclusions must retain prose and remain language-specific."""
import json
import unittest
from dump_tts_text import LIB, process_chapter

SLUG = 'lets-welcome-the-extraterrestrials'


class NarrationOverridesTests(unittest.TestCase):
    def test_directory_is_silent_but_closing_date_remains(self):
        side = process_chapter(SLUG, 4, 'fr')['sidecar']
        self.assertIn('Cannes', side['219']['text'])
        self.assertTrue(all(side[str(n)]['skip'] for n in range(220, 313)))

    def test_interrupted_sentence_is_complete_without_footnote(self):
        side = process_chapter(SLUG, 3, 'fr')['sidecar']
        self.assertTrue(side['26']['text'].endswith('seuls ou en groupes.'))
        self.assertNotIn('Depuis 1998', side['26']['text'])
        self.assertTrue(side['88']['skip'])

    def test_english_sidecars_are_unchanged(self):
        for c in range(1, 5):
            with self.subTest(chapter=c):
                existing = json.loads((LIB / SLUG / 'tts' / f'chapter-{c}.en.json').read_text())
                self.assertEqual(process_chapter(SLUG, c, 'en')['sidecar'], existing)

    def test_reviewed_spoken_reference_counts(self):
        for c, count in enumerate((200, 203, 85, 219), 1):
            side = process_chapter(SLUG, c, 'fr')['sidecar']
            self.assertEqual(sum(bool(p['text']) and not p.get('skip') for p in side.values()), count)


if __name__ == '__main__':
    unittest.main()
