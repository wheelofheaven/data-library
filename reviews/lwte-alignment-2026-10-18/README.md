# LWTE English alignment, 18 October 2026

All four chapters have been aligned to the existing 836 French reference units.
The official English wording comes from the IRM 2005 anthology EPUB, members `OPS/chapter-14.xhtml` through `OPS/chapter-17.xhtml`.
Each manifest records the archive and member hashes, the French witness hash, excluded page furniture and dialogue labels, and the complete reviewed English assignments.
No French text, reference number, speaker attribution, or other translation was rewritten.
This is a correction of reference alignment, not a new translation or an endorsement of the source's claims.

## Editorial decisions

- Restore every substantive heading, list item, and the short “Rael,” signature skipped by the old paragraph-only importer.
- Remove repeated running heads and page-number/object artifacts; retain the source's wording, spelling, biblical version differences, and endnote markers.
- Read LWTE-1:20–21 together: the witnesses order the two Matthew quotations differently.
- LWTE-1:201 is a French bibliographic note with page/chapter furniture, absent from the English chapter.
- LWTE-3:53 is an inline French bibliographic citation represented by endnote marker 25 in the English chapter.
- English condensation/reordering requires five shared groups in chapter 4: 28–30, 34–36, 37–39, 47–48, and 50–52.
  The English passage is stored once, at the first reference; subsequent units explicitly point to it.
- LWTE-4:40–41 (continental separation/residual velocity) is absent from the English witness.
  French PDF page 116 (printed page 120) was rendered and inspected to confirm its separate paragraphs.
- LWTE-4:179's additional byline role and 219–312's date/contact directory/back matter are absent from this English EPUB chapter.
  PDF page 146 (printed page 150) confirms the contact directory is a multi-column page, not the continuation of the testimonial.
- The English Ndjoga-Awirondjogo byline precedes his essay; it is placed at the existing French byline reference, LWTE-4:203.
  This is the sole substantive block relocation in the conservation check.
- Existing French extraction defects, embedded footnotes, and directory row segmentation remain visible in the French witness.
  They are not silently repaired by generating English substitutes.

The English reading text is conserved character for character after whitespace normalization and the one recorded byline relocation.
The original French reference sequence remains unchanged.
English EPUB block boundaries identify 128 continuations (16, 49, 13, and 50 by chapter), recorded as `kindByLang.en` without changing French reading flow.
A continuation is recorded only when the preceding reference has English text; LWTE-4:53 remains separate after the shared-passage notices.
`preserveParagraphBreaks.en` retains source paragraph breaks inside a reference unit.
The catalog's stale total has been corrected from 826 to 836.
The reader labels shared passages and missing counterparts and provides the French source without presenting it as English.

## Reproduce and verify

From the `data-library` root (Python 3.11+):

```sh
python3 scripts/apply_reviewed_alignment.py reviews/lwte-alignment-2026-10-18/chapter-*.json --check
python3 scripts/apply_reviewed_alignment.py reviews/lwte-alignment-2026-10-18/chapter-*.json --check --epub '../claude-projects/projects/wheel-of-heaven/files/Message from the Designers.epub'
python3 -m unittest discover -s scripts -p 'test_reviewed_alignment.py'
```

To apply a reviewed manifest to its exact pre-review chapter, use `--apply`.
The command is a dry run by default, validates the entire batch before writing, and refuses changed chapter bytes, missing/duplicate references, lost source text, and unresolved shared targets.
The proportional importer `fill_en_from_epub.py` now exits without writing.

## Citations and audio

`citation-migration.json` records the reference-only migration of article/wiki quotations and their locale copies.
Targets were checked against the quoted assertion, rather than the largest overlapping old paragraph.
Existing French references in the Great Flood entry remain unchanged.
In the *Six Mornings* article, the former 2:92 citation of the switch to `tu` resolves specifically to 2:88; the parentage quotation in *The Religion of Religions* resolves to 2:87.

English TTS sidecars have been regenerated from the corrected text.
The old third-book recordings/timings still refer to the proportional assignments and must not be used for highlighting this edition.
`_meta.json.audioHold.en` withholds the English reader's Listen controls until all four English tracks, timings, and ambient variants have been rebuilt and validated.
No paid synthesis was performed in this repair.
French recordings and the first two books are unaffected.
Remove the hold only after the replacement audio is available and its paragraph targets have been checked.

### English audio release, 19 October 2026

The subsequent audio release replaces the hold with narration for all four English chapters.
It covers 728 spoken reference units, reusing the 33 previously generated preview units.
French-only material and secondary references to shared English passages remain unvoiced.
Phoenix narrates throughout; this book has no configured ambient or cinematic tracks.
The release report in `../lwte-audio-2026-10-19.json` records source and asset hashes, durations, and technical validation.
Every spoken reference has a target in the rendered English reader; full listening review remains separate from those checks.
