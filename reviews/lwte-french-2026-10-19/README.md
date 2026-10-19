# LWTE French source and narration review — 19 October 2026

The four French chapters were compared with the local Nova Distribution 2001 PDF, `data-sources/pdf/lets-welcome-the-extraterrestrials/lets-welcome-the-extraterrestrials-fr.pdf`.
Each chapter receipt records the witness hash, the previous and resulting chapter hashes, and every changed reference.
The existing 836 reference IDs, English assignments, and other translations are preserved.

## Source repairs

Thirty reference units recover dropped section headings, author bylines, citations, and short narrative passages.
These include “Je lui répondis”, the closing “A vous de jouer!”, and “groupes” at the page turn in 3:26.
Page counters and the following chapter marker are removed from 1:201 and 3:26.
The bibliographic footnotes in 1:21 and 3:26 are separated from the narrative; 3:26's interrupted sentence is completed before its footnote.
French paragraph 2:50 is a continuation of the quotation in 2:49, which was split at a page turn.
Restored block breaks are retained by `preserveParagraphBreaks.fr`.

A normalized word-sequence comparison of the chapter bodies against PDF pages 15–62, 63–94, 95–111, and 112–145 leaves only the chapter headings held in metadata, the removed page counters, and the recorded movement of “groupes” before the footnote.
Chapter 4's narrative through reference 219 matches the PDF's word sequence completely.
PDF pages 15 and 99 were also rendered to inspect the opening heading and interrupted sentence.
Original spellings and source-edition typographical errors are retained; this is not a modernization or a new translation.
The introduction before chapter 1 and the bibliography after the directory remain outside the existing four-chapter reader.

## Narration scope

The French recording covers 707 spoken reference units across four chapters.
129 reference units are silent: citation-only units, the chapter 3 postal address, and the chapter 4 contact directory (220–312).
The directory is a multi-column print appendix whose existing extraction interleaves entries; it remains visible in the source reader, but is not synthesized as speech.
The closing date at 4:219 remains spoken.
Embedded edition footnotes are omitted from the spoken versions of 1:21 and 3:26 while their narrative text is retained.

`audio/text-overrides/lets-welcome-the-extraterrestrials.fr.json` makes these French-only exceptions reproducible by `scripts/dump_tts_text.py`.
The standard normalization and French pronunciation lexicon then apply.
Phoenix narrates with Multilingual v2 and the existing treatment settings; there are no ambient or cinematic layers for this book.
Generation uses a durable request ledger, cached per-paragraph audio, and a fixed credit cap; ambiguous paid requests are not automatically retried.
Technical checks cover audio decoding, source/cache correspondence, timestamp bounds, and reader reference targets.
They do not substitute for a full human listening review.

## Validation

From `data-library`, using Python 3.11 or later:

```sh
python3 scripts/validate_lwte_french.py
python3 -m unittest discover -s scripts -p 'test_reviewed_alignment.py'
python3 -m unittest discover -s scripts -p 'test_narration_overrides.py'
python3 scripts/dump_tts_text.py --slug lets-welcome-the-extraterrestrials --lang fr
```

The validator reverses the recorded French-only changes in memory and verifies the exact bytes of the preceding English-alignment revision.
The earlier English review manifests remain historical records; their strict whole-file `--check` intentionally rejects these subsequently revised French chapters.
Use the successor validator and regression tests above to verify the current edition.
