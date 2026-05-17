# Extraterrestrials Took Me to Their Planet — Curation TODO

## Status

**Ingest + curation complete.** Three chapter files + `_meta.json`
written to `data-library/extraterrestrials-took-me-to-their-planet/`.
French text populated as primary, speakers assigned by chapter
heuristic, all 8 i18n slots initialized empty pending translation.

Catalog: `status = "partial"`, `chapters = 3`, `paragraphs = 455`.

| Chapter | Paras | Speakers | EPUB En paras | Ratio |
|---|---|---|---|---|
| 1. Ma Vie Jusqu'à La Première Rencontre | 74 | 74 Narrator | 139 | 1.88x |
| 2. La Deuxième Rencontre | 116 | 51 Narrator + 65 Yahweh | 250 | 2.16x |
| 3. Les Clés | 265 | 7 Narrator + 258 Yahweh | 322 | 1.22x |

Speaker distribution mirrors TBWTT's pattern: ch1 fully Narrator
(autobiographical), ch2 mixed (Raël arrives at the meeting, then long
Yahweh monologues), ch3 almost entirely Yahweh teaching (matching
TBWTT ch3's 292/303 Yahweh proportion).

The English EPUB segments paragraphs ~2x finer than the French original
(translator broke long French paragraphs into shorter English ones), so
the EPUB text is **not** pre-filled into `paragraphs[].i18n.en` — that
would index-misalign content. The EPUB text is preserved as a
translator reference at:
`curator-work/extraterrestrials-took-me-to-their-planet/en-reference-chapter-{1,2,3}.md`.

## What the curation pass fixed (vs first-cut)

1. **Inline footnotes** stripped from blocks where PyMuPDF concatenated
   body + footnote into one layout block. Previously the whole block
   was dropped on `N.D.L.R` match, losing body content. Now the
   footnote tail (`____... 1. N.D.L.R. ...`) is stripped and the body
   preserved. This recovered ch2's opening paragraph
   ("C'est au mois de juin 1975 que je décidai…", 2771 chars).
2. **Image-caption prefixes** stripped from continuation blocks where
   PyMuPDF prepended the caption ("L'endroit de la seconde rencontre
   de Raël le 7 octobre 1975…") to the body paragraph that resumed
   after the image.
3. **Standalone footnote artifacts** (e.g. `____________________________
   1. Voir Le Livre qui dit la Vérité.`) dropped via the
   `FOOTNOTE_STANDALONE_RE` filter.
4. **Subsection headers** (e.g. `Un avant-goût de paradis`,
   `L'apparition du 31 juillet 1975`) dropped via the expanded
   `SUBSECTION_HINTS` set, including hyphenated variants.
5. **Speaker assignment** per chapter:
   - ch1: all Narrator
   - ch2: dash/guillemet detection with sticky-Yahweh continuation
   - ch3: paragraphs 1-3 + Raël wrap markers = Narrator; rest Yahweh

## Sources

- French PDF: `data-sources/pdf/_combined/le-message-donne-par-les-extra-terrestres.pdf`
  (1998 Foundation Raëlienne reissue bundling TBWTT + ETTMTTP)
- English EPUB: `claude-projects/projects/wheel-of-heaven/files/Message from the Designers.epub`
  (2005 IRM anthology, English translation)
- Ingest script: `data-library/scripts/ingest_extraterrestrials_took_me_to_their_planet.py`

## Known residual issues

After the curation pass:

1. **Sticky Yahweh in ch2** — a few paragraphs that are actually
   narrator interludes inside Yahweh's long monologues may stay
   attributed to Yahweh because they don't match the
   `STRONG_NARRATION_MARKERS` set. A human spot-check during the
   translation pass review can re-attribute as needed.
2. **Dialogue tag lines** — short lines like "Mon guide parla alors :"
   appear as their own paragraphs (one example: ch2 para 17). These
   are legitimate (consistent with the TBWTT pattern), kept as
   Narrator. No action needed.

## Next steps

1. **Translation pass** — French text is curated and clean. Run the
   standard Claude+`_glossary.json` translation workflow used for
   TBWTT. The existing `_glossary.json` was authored for TBWTT but
   generalizes to ETTMTTP (same author, canon, scripture-handling
   policy, divine-name carve-outs). Each chapter produces a
   `new-chapter-N.json` to be promoted to `chapter-N.json` with the
   translation provenance block added.
2. **Spot-check speaker attributions** — during translation review,
   scan ch2 for any Yahweh attributions that should be Narrator (or
   vice versa).
3. **Catalog promotion** — once all 3 chapters carry all 8
   translations, bump `status` from `"partial"` to `"complete"` and
   add the complete language list to `completeLangs`.

## Scope notes

- The 1998 French PDF treats SM (Sensual Meditation) as a subsection of
  ETTMTTP Chapter 3 ("Les Clés"), not as its own book. The standalone
  1980 SM publication is a separate book and not ingested here.
- The PDF also contains supplementary material after Chapter 3 (Message
  du 13 décembre 1997, Post-scriptum, Additional info, Addendum,
  Technique of telepathic contact). These are NOT included in the
  current 3-chapter cut — they may be appended as appendix chapters in
  a future pass if desired, or kept as separate documents.
