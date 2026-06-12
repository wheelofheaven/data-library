# The Song of the Hoe — sign-off package

**Book:** `song-of-the-hoe-woh` · **Composition:** 1 (110 lines) · **Source:** ETCSL 5.5.4 (Sumerian composite, ETCSL academic-use terms with attribution)
**Status:** `awaiting-human` · **Version:** `1.0.0-rc1`
**Pipeline:** woh-translator → woh-editor → woh-reviewer, all complete. Awaiting human sign-off to advance to `stable` / `1.0.0`.

This is the Wheel of Heaven's translation of the Sumerian "humanity-from-the-ground" hymn — Enlil sunders heaven and earth, sets the hoe to the soil at Uzu-e-a ("Where Flesh Came Forth"), and the first humans break up through the ground to bear the gods' labor. It recovers the human-creation-for-toil theme that the (source-unavailable) Atraḫasīs Tablet I would have carried, on a fully open, re-fetchable source.

## Summary table

| Metric | Value |
|---|---|
| Lines translated | 110 / 110 (`i18n.en` filled; `translit` carried verbatim from source) |
| Lines with per-line commentary | 29 |
| Editorial questions raised → resolved | 20 → 0 |
| Overlay glossary entries added | 11 (overlay `0.1.0` → `1.0.0`) |
| — claim_type breakdown | 4 `direct` / 7 `inferred` / **0 `speculative`** |
| Central glossary | untouched (4.6 MB; grepped by id only; 19 cross-corpus lemmas referenced, 0 dangling) |
| Reviewer verse verdicts | **110 approve / 0 revise / 0 flag** |
| Reviewer lens-leakage flags | **0** |
| Reviewer glossary verdicts | 11 confirmed (claim_types sound; 0 speculative-in-disguise; no contested-as-`direct`) |

## Overlay glossary entries (v1.0.0)

**`direct` (4):** `al-paronomasia-hoe-syllable-whole-composition-convention` · `al-gishal-hoe-mattock-brick-mould-lexeme` · `shu-giri-nose-hand-to-nose-obeisance-idiom` · `nunamnir-enlil-epithet`

**`inferred` (7):** `al-tar-hoe-wielder-construction-work-pun-lexeme` · `uzu-ea-uzu-mua-where-flesh-came-forth` · `dur-an-ki-bond-of-heaven-and-earth-bulug-axis` · `sag-namluulu-ushub-brick-mould-human-prototype` · `numun-kalam-ma-seed-of-the-land` · `ninmena-birth-goddess-epithet-crown-lady` · `al-initial-technical-noun-catalogue-vv83-93`

## Licensing (documented exception, openly disclosed)

- **WoH translation + commentary + glossary:** CC0-1.0 (original work).
- **Underlying Sumerian transliteration:** ETCSL composite (ETCSL 5.5.4), reproduced under ETCSL's academic-use terms with acknowledgment to *The ETCSL project, Faculty of Oriental Studies, University of Oxford*.
- Recorded in `_meta.json` `licensing` block; rendered by the library-book "Licensing" sidebar panel. This is a transparency note, not a restriction on the WoH translation.

## Items requiring decision (human reviewer)

The Reviewer set `awaiting-human` (not `reviewer-approved`) for these four — none is a philology problem; all are project-stance / eyeball confirmations:

1. **Epistemic pitch of the four lens-bearing `inferred` readings** — `uzu-ea-uzu-mua`, `sag-namluulu-ushub` (brick-mould human-prototype), `numun-kalam-ma` (seed/germination), and the toil-relief topos (L31 commentary via central `du-lum-dullu`). All correctly labelled `inferred`, all on named scholarship; the gate is project-stance, not philology. **Confirm the labels stand.**
2. **Two source-insecure cruxes, honestly preserved rather than smoothed** — L81–82 ("sons of the hoe … born from heaven after sleep had been spoken of") and L95 (damaged `šabra-[…]` variant vs principal `sa-par4`). No reading is secure in the standard editions; the conservative flag-and-preserve handling is the correct call. **Eyeball.**
3. **L18/18A manuscript divergence** immediately before the human-creation line 19 — composite is uneven; 18A is single-witness. Inline-variant rendering reads cleanly, 18A correctly subordinated to 19. **Eyeball.**
4. **Two editor non-promotions to central** — Ninmena → birth-goddess cluster; Nunamnir → Enlil/triad entry. Both sound as overlay-recorded single-text epithets under the recurrence criterion; promote only if either recurs in a later composition. **Note for future maintenance.**

## Reports (full detail)

- **Editor escalation report:** `chapter-1-editor-report.md` (this directory).
- **Reviewer report:** `chapter-1.json` → `translation.reviewerReport` (110 verse verdicts, 11 glossary verdicts, 0 lens-leakage flags, 4 human-reviewer notes).

## Recommendation

The chapter is philologically serious and source-honest: a credentialed Sumerologist reading only the `i18n.en` column would find a defensible rendering of c.5.5.4, and the Wheel of Heaven reading lives entirely in the apparatus. The four decision items are confirmations, not blockers. **Recommend human sign-off** → advance `translation.status` to `stable`, `version` to `1.0.0`, set `reviewer` to `zarazinsfuss` + `reviewedAt`, and register the chapter in `_meta.json`.
