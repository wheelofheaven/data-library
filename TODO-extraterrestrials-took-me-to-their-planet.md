# Extraterrestrials Took Me to Their Planet — Curation TODO

## Status

First-cut ingest complete. Three chapter files + `_meta.json` written to
`data-library/extraterrestrials-took-me-to-their-planet/`. French text
populated as primary, all 8 i18n slots initialized empty pending
translation.

Catalog updated: `status = "partial"`, `chapters = 3`, `paragraphs = 457`.

| Chapter | French para count | EPUB English para count | Ratio |
|---|---|---|---|
| 1. Ma Vie Jusqu'à La Première Rencontre | 74 | 139 | 1.88x |
| 2. La Deuxième Rencontre | 118 | 250 | 2.12x |
| 3. Les Clés | 265 | 322 | 1.22x |

The English EPUB segments paragraphs ~2x finer than the French original
(translator broke long French paragraphs into shorter English ones), so
the EPUB text is **not** pre-filled into `paragraphs[].i18n.en` — that
would index-misalign content. The EPUB text is preserved as a
translator reference at:
`curator-work/extraterrestrials-took-me-to-their-planet/en-reference-chapter-{1,2,3}.md`.

## Sources

- French PDF: `data-sources/pdf/_combined/le-message-donne-par-les-extra-terrestres.pdf`
  (1998 Foundation Raëlienne reissue bundling TBWTT + ETTMTTP)
- English EPUB: `claude-projects/projects/wheel-of-heaven/files/Message from the Designers.epub`
  (2005 IRM anthology, English translation)
- Ingest script: `data-library/scripts/ingest_extraterrestrials_took_me_to_their_planet.py`

## Known issues — curation pass needed

The first-cut French extraction has the following known artifacts that
should be cleaned up in a second pass before publication:

1. **Subsection headers that may have leaked through.** The script
   filters a static `SUBSECTION_HINTS` list against PyMuPDF blocks, but
   the list may be incomplete or font-substituted apostrophes may
   bypass the comparison. Scan each chapter for short non-uppercase
   paragraphs that look like section titles (e.g. `L'enfance, Ovni sur
   Ambert`, `Le deuxième message`).
2. **Mid-paragraph splits from page breaks.** When a PDF page break
   interrupts a paragraph (with footnotes / running headers /
   page numbers in between), PyMuPDF emits the two halves as separate
   blocks. The script merges blocks that start with a lowercase letter,
   but a continuation that happens to start with a proper noun or quote
   will be missed. Scan for paragraphs that look like sentence
   fragments at start or end.
3. **Speaker attribution.** Every paragraph is currently marked
   `speaker: "Narrator"`. ETTMTTP has substantial dialogue between Raël
   and the Elohim spokesperson, with embedded scripture quotes
   attributed to Yahweh. Run a speaker-assignment pass mirroring what
   `curate_the_book_which_tells_the_truth.py` did for TBWTT.

## Next steps

1. **Curation pass** — write or adapt a `curate_*.py` script for ETTMTTP
   that fixes the issues above. Validate against the EPUB English
   reference (paragraph counts won't match 1:1 but content should align
   when read side-by-side).
2. **Translation pass** — once French text is clean, run the standard
   Claude+`_glossary.json` translation workflow used for TBWTT. The
   existing `_glossary.json` was authored for TBWTT but generalizes to
   ETTMTTP (same author, same canon, same scripture-handling policy,
   same divine-name carve-outs). Each chapter produces a
   `new-chapter-N.json` to be promoted to `chapter-N.json` with the
   translation provenance block added.
3. **Catalog promotion** — once all 3 chapters carry all 8 translations,
   bump `status` from `"partial"` to `"complete"` and add the
   complete language list to `completeLangs`.

## Scope notes

- The 1998 French PDF treats SM (Sensual Meditation) as a subsection of
  ETTMTTP Chapter 3 ("Les Clés"), not as its own book. The standalone
  1980 SM publication is a separate book and not ingested here.
- The PDF also contains supplementary material after Chapter 3 (Message
  du 13 décembre 1997, Post-scriptum, Additional info, Addendum,
  Technique of telepathic contact). These are NOT included in the
  current 3-chapter cut — they may be appended as appendix chapters in
  a future pass if desired, or kept as separate documents.
