# The Book Which Tells the Truth Curation TODO

## Assessment

- `data-library` is the canonical library data repo. The website and API each vendor it as a submodule under `data/library`.
- `curator-work/the-book-which-tells-the-truth/book.json` is an unfinished monolithic working artifact. It has one chapter, all paragraphs marked unvetted, and still contains OCR/Markdown artifacts. Do not publish it as-is.
- The canonical `data-library/the-book-which-tells-the-truth` split files are structurally better: 7 chapters, 1029 paragraphs, and matching monolithic `the-book-which-tells-the-truth.json`.
- The canonical files still contain cleanup issues:
  - OCR line-break continuations split across paragraphs.
  - Hyphenated words split by OCR line breaks, e.g. `embryon- naires`.
  - Book/page decoration artifacts stored as paragraph text, e.g. repeated uppercase running heads and front/back matter fragments.
  - Missing speaker attribution outside chapter 1.
- After curation, update both the split chapter files and the monolithic JSON, then bump the `data/library` submodules in `api.wheelofheaven.io` and `www.wheelofheaven.io`.

## Work Items

- [x] Compare existing alternate JSON files (`output*.json`, `target_all_fr_clean_nosubheads.json`) before editing to avoid losing better curation already present elsewhere.
- [x] Remove decoration artifacts that are not scripture paragraphs.
- [x] Merge OCR-split paragraphs and repair hyphenated words.
- [x] Assign speaker fields consistently (`Narrator`, `Raël`, `Yahweh`) across all chapters.
- [x] Keep chapter metadata and paragraph counts consistent.
- [x] Regenerate `the-book-which-tells-the-truth.json` from the split files, or vice versa, so both formats match.
- [x] Validate JSON syntax and schema expectations.
- [ ] Update website/API submodule pointers once the canonical data repo is clean.

## Cleanup Pass 2026-04-26

- Added `scripts/curate_the_book_which_tells_the_truth.py` so the cleanup is repeatable.
- Reduced the canonical book from 1029 to 740 paragraphs.
- Removed 59 running-head, table-of-contents, image-caption, and editorial-note artifacts.
- Removed 42 chapter-7 back-matter paragraphs starting at the contact/advertisement section.
- Merged 188 OCR-split paragraphs.
- Validation passes:
  - No null speakers.
  - No lowercase paragraph starts.
  - No trailing OCR hyphen paragraphs.
  - No `word- word` OCR hyphen-space fragments.
  - Split chapters, `_meta.json`, `catalog.json`, and the monolithic JSON agree on paragraph counts.
- Applied the same generated data to the local `www.wheelofheaven.io/data/library` and `api.wheelofheaven.io/data/library` submodule working trees. The actual submodule pointer bump is still pending a `data-library` commit.
