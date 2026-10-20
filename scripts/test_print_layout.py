"""Print-layout repairs must preserve reference wording and published audio."""
import json
import re
import unittest

from dump_tts_text import LIB, process_chapter

SLUG = "extraterrestrials-took-me-to-their-planet"
LANGS = ["fr", "en", "de", "es", "ru", "ja", "ko", "zh", "zh-Hant", "he"]


class PrintLayoutTests(unittest.TestCase):
    def test_reviewed_lines_preserve_words_and_reference_ids(self):
        audit = json.loads((LIB / "curation/2026-10-20-ett-print-layout.json").read_text())
        for change in audit["textChanges"]:
            chapter = json.loads((LIB / SLUG / f"chapter-{change['chapter']}.json").read_text())
            current = next(p for p in chapter["paragraphs"] if p["n"] == change["paragraph"])
            self.assertEqual(current, change["after"])
            before = change["before"]
            self.assertEqual(current["refId"], before["refId"])
            self.assertTrue(current["preserveLineBreaks"])
            for lang in LANGS:
                with self.subTest(ref=current["refId"], lang=lang):
                    old = before["text"] if lang == "fr" else before["i18n"][lang]
                    new = current["text"] if lang == "fr" else current["i18n"][lang]
                    self.assertEqual(len(new.splitlines()), 4)
                    # Hebrew slash marks were inline representations of verse breaks.
                    if lang == "he" and change["chapter"] == 1:
                        old = old.replace(" / ", "\n")
                    self.assertEqual(re.sub(r"\s+", "", old), re.sub(r"\s+", "", new))

    def test_headings_are_localized_without_new_reference_units(self):
        for chapter, paragraph in [(1, 41), (3, 4)]:
            data = json.loads((LIB / SLUG / f"chapter-{chapter}.json").read_text())
            heading = next(p for p in data["paragraphs"] if p["n"] == paragraph)["headingBefore"]
            self.assertTrue(heading["text"])
            self.assertEqual(set(heading["i18n"]), set(LANGS) - {"fr"})
            self.assertTrue(all(heading["i18n"].values()))

    def test_all_published_narration_inputs_remain_identical(self):
        for chapter in (1, 2, 3):
            for lang in LANGS:
                with self.subTest(chapter=chapter, lang=lang):
                    published = json.loads((LIB / SLUG / "tts" / f"chapter-{chapter}.{lang}.json").read_text())
                    self.assertEqual(process_chapter(SLUG, chapter, lang)["sidecar"], published)


if __name__ == "__main__":
    unittest.main()
