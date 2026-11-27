# Chapter 38 Editor Report

Isaiah 38 (22 verses), wave I-6 (Isa 36–39, 41).
Editor: claude-opus-5-5 (editor), 2026-11-27.
Base: central glossary v5.0.0 and isaiah-woh overlay v4.0.0, both read-only, with `wave-i6-rulings.md` in force.
All glossary changes are in `wave-i6-ch38-overlay-diff.json` (proposes overlay 4.1.0) and `wave-i6-ch38-central-diff.json` (proposes central 5.1.0).

## Summary

- **Editorial questions:** all 18 are resolved and `editorial_questions[]` is empty. No question needs a founder decision. Two items are flagged below for the founder's attention (38:8 speculative note; 38:11 decision recorded).
- **English-line changes:** six verses change, and each change is backed by a glossary op.
  - 38:3: "with a perfect heart" → "with a whole heart" (JPS 1917); "wept bitterly" → "wept greatly" (overlay `lexical-cruxes-isaiah-38`). In this book "bitterly" translates *mar*/*mrr* (22:4; 33:7), and *mar* is the psalm's own word (38:15, 17).
  - 38:6: "defend" → "protect", the book's verb for *gnn* (31:5); NJPS also has "protect" (overlay `lexical-cruxes-isaiah-38`).
  - 38:8: "on the dial of Ahaz" → "on the steps of Ahaz"; "on the dial on which it had gone down" → "on the steps down which it had gone". *Maʿălôṯ* is now "steps" at all five sites (new overlay `maalot-steps-of-ahaz-isaiah-38`).
  - 38:14: "chattered" → "chirped", the book's bird verb for *ṣpṣp* (10:14; also 8:19) (overlay `lexical-cruxes-isaiah-38`).
  - 38:18: "cannot praise you … cannot celebrate you" → "cannot give thanks to you … cannot praise you" (new overlay `ydh-give-thanks-hll-praise-isaiah`).
  - 38:19: "he shall praise you" → "he shall give thanks to you" (same entry).
- **Commentary:** all 22 verses have `notes.official`. One verse (38:8) ends with a separately headed reception note labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`, and "claude-opus-5-5 (editor)" is added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 5.0.0 and 4.0.0; the orchestrator sets them on merge. No paragraph `translit` was added.
- **Rule 3 (Kings parallel):** the differences from 2 Kgs 20:1–11 are recorded at 38:1, 2, 3, 4, 5, 6, 7, 8, 21 and 22. The psalm (38:9–20) has no parallel in Kings, and 38:9 says so. Isaiah's text is not harmonised with Kings anywhere.
- **Lens audit:** no English line carries a project reading. The canon in data-library (TBWTT, ETTMTTP, LWTE) does not cite Isa 38 or 2 Kgs 20.
- **Verification (2026-11-27):**
  - ASV and KJV of Isa 38 through bible-api.com.
  - JPS 1917 and NJPS of Isa 38 through the Sefaria API v3. NJPS is "Tanakh: The Holy Scriptures, published by JPS", not the Gender-Sensitive Edition. Its notes at 38:8, 10, 11, 12, 15, 19 and 20 were checked too.
  - MT and NJPS of 2 Kgs 20:1–11, and the MT of Pss 6:6, 16:1, 30:10, 39:6, 42:5, 56:1, 60:1, 115:17, Jer 8:7, 2 Chr 32:24, Josh 10:13 and Isa 10:14, 12:1, all through Sefaria.
  - Rashi, Ibn Ezra and Radak on 38:11, and Rashi and Metzudat David on 38:8, through Sefaria.
  - The Translator's draft cited ASV only; every JPS 1917 and NJPS statement in the commentary was checked against the texts above.
  - Not verified, and labelled so in the commentary: 1QIsaᵃ (DJD 32; the "upper chamber of Ahaz" reading at 38:8 and the later-hand insertion of 38:21–22), the LXX, NRSV, BDB/HALOT, the sources of the emendations *miḵtām*, *šiwwaʿtî* and *ḥāśaḵtā*, and the reported manuscript spelling *ḥeleḏ* at 38:11. The Fred P. Miller site (ao.net/~fmoeller) has no collation for Isa 36–39, only a translation and commentary, so it was not used.

## Speculative entries (founder sign-off 2026-11-27)

No speculative glossary entry is proposed. Every new or extended entry is `claim_type: direct`.

There is one commentary paragraph labelled speculative (a reception note; founder policy keeps such notes):

### ISA-38:8 reception note (the sun returned ten steps)

**Source:** *wattāšoḇ haššemeš ʿeśer maʿălôṯ* "So the sun returned ten steps"
**WoH choice:** none in the line. The line keeps the literal subject, "the sun", with ASV, KJV and JPS 1917, and names no mechanism.
**Why speculative:** the canon does not cite Isa 38 or 2 Kgs 20. The note's premise has a source: TBWTT 3:69–71 reads Josh 10:13 ("the sun stood still") as people's impression of a one-day war, "men believed the sun had stopped". Applying that reading to 38:8 extends it to a verse the canon does not discuss. The note says so, and it also names the difference between the two passages: Joshua's sun stops during a battle, while Hezekiah's sign is announced in advance and goes backward.
**Recommendation:** ship as labelled. If the founder judges the analogy too weak (it is a different verse and a different kind of sign), drop the paragraph. The philological notes stand without it.
**Ruling:** kept as labelled (founder sign-off 2026-11-27).

---

## Unresolved editorial questions

None need escalation. Two decisions are recorded here so the founder and the Reviewer can see them:

### `ISA-38:11` (MT *ḥeḏel* vs ASV "the world")

**Issue:** the Masoretic word is *ḥeḏel* "cessation". ASV, JPS 1917 and NJPS all translate it "world"/"earth", which seems to presuppose *ḥeleḏ*.
**Options considered:** (A) keep "the inhabitants of the world"; (B) "the inhabitants of cessation", that is, with the dead (Rashi); (C) emend to *ḥeleḏ*.
**Decision:** (A), so the line does not change. Ibn Ezra and Radak (checked) read the Masoretic consonants themselves as *ḥeleḏ* with the letters transposed (as in *keḇeś*/*keśeḇ*). Ibn Ezra also explains that this world is called *ḥeḏel* because life in it ceases. "The world" therefore translates MT as the Jewish tradition and both JPS versions read it, and no consonant is changed, so the house policy `mt-qere-textual-policy-isaiah` holds. Rashi's reading is given as the alternative in the commentary. This is escalated only for information. If the founder prefers the strictly lexical (B), the line would read "among the inhabitants of cessation" (or "of the land where all ceases"), and only `lexical-cruxes-isaiah-38` would need its 38:11 item changed.

### `ISA-38:21–22` (pluperfect)

**Issue:** ASV and KJV make *wayyōʾmer* pluperfect ("had said"). JPS 1917 has the simple past, and NJPS has a subordinate clause.
**Decision:** keep the ASV pluperfect, so the flashback to 2 Kgs 20:7–8 is visible in English. The verses are not moved. This is recorded, not escalated.

---

## Open concordance items outside this chapter (not changed here)

- **25:1** *ʾôḏeh šimḵā* "I will praise your name" (stable). Under the new `ydh-give-thanks-hll-praise-isaiah` entry it would read "I will give thanks to your name". It is recorded in the entry as an exception for the next revision of chapter 25.
- **29:4** *ṣpṣp* "whisper" (stable). It is kept as a rendering bound to its context (speech from the dust). 8:19, 10:14 and now 38:14 have "chirp". The open item in `ob-yiddeoni-ghosts-familiar-spirits-isaiah` remains.
- **37:35** (chapter 37 Editor): *gnn* should be "protect", as at 31:5 and 38:6. The 37:35 draft already reads "protect".

## Glossary changes for review

### Central glossary (`wave-i6-ch38-central-diff.json`, 5.0.0 → 5.1.0)

- Modified: `sheol-underworld-realm-of-the-dead`: appliesTo + ISA-38:10, ISA-38:18 (rationale addendum)
- Modified: `bor-pit-cistern-dry-water-shaft`: appliesTo + ISA-38:18 (rationale addendum)
- Modified: `hithallekh-lefanai-patriarchal-walking-before-elohim-covenantal-formula`: appliesTo + ISA-38:3 (the rationale already cites the verse)
- Modified: `davar-yhwh-prophetic-formula`: appliesTo + ISA-38:4
- Deliberately not extended:
  - `chesed-v-emet-steadfast-love-and-truth`: only *ʾĕmeṯ* occurs, not the pair, so the Translator's refs at 38:3, 18 and 19 were dropped. *ʾĕmeṯ* "truth" is recorded book-wide in `lexical-cruxes-isaiah-38`.
  - `hithpallel-first-prayer-occurrence`: scoped to first occurrences.
  - `shechin-ra`: scoped to the phrase in Job 2:7.

### Per-translation overlay (`wave-i6-ch38-overlay-diff.json`, 4.0.0 → 4.1.0)

- Added: `maalot-steps-of-ahaz-isaiah-38` (claim_type: `direct`). Promote it to central when 2 Kgs 20:9–11 is translated.
- Added: `ydh-give-thanks-hll-praise-isaiah` (claim_type: `direct`), governing 12:1, 12:4, 38:18 and 38:19.
- Added: `lexical-cruxes-isaiah-38` (claim_type: `direct`)
- Modified: `title-and-meta-conventions-isaiah`: appliesTo + 38:1, 2, 3, 4, 5, 7, 20, 22. The title is ratified, and the addendum records the quotation-mark extents and "Thus says". This also covers the Translator's `lexical-cruxes-isaiah-30` refs at 38:1 and 38:5, which are dropped: that entry is chapter-scoped, and the messenger-formula convention belongs to the meta entry.
- Modified: `elohei-yisrael-god-of-israel-isaiah-24`: appliesTo + 38:5
- Modified: `adam-humankind-ish-man-isaiah`: appliesTo + 38:11
- Modified: `yah-tzur-olamim-everlasting-rock-isaiah-26`: appliesTo + 38:11
- Modified: `adonai-standalone-title-isaiah`: appliesTo + 38:14, 38:16
- Modified: `mt-qere-textual-policy-isaiah`: appliesTo + 38:8, 9, 11, 13, 15, 17, 21

No existing wohChoice, claim_type or rationale text is changed. Every modify op only extends appliesTo and adds to the rationale.

## Post-review corrections

Applied after the Reviewer's report (2026-11-27). `translation.status` (awaiting-human), the `reviewerReport` block, every English line and both shared glossaries are unchanged. All changes are to `notes.official` only.

1. **ISA-38:8, speculative paragraph (Reviewer correction).** "The only biblical solar sign the canon discusses is Josh 10:13" was wrong: LWTE 2:148–176 reads the darkened sun of Rev 6:12, 8:12 and 9:2 as dust and ash giving "the impression" that days and nights are shorter (LWTE 2:174, checked in data-library). The sentence now reads "The only biblical passage in which the sun's course is altered that the canon discusses is Josh 10:13", and a parenthesis names the Revelation readings (there the sun is obscured, not moved).
2. **ISA-38:8, philological paragraph (optional precision, applied).** Added: *yārᵉḏāh* is feminine, while *ṣēl* takes masculine verbs in 2 Kgs 20:9–10 (*hālaḵ*, *yāšûḇ*; MT checked), so the relative clause may take the sun as subject. The same feminine form stands in 2 Kgs 20:11. The English leaves the subject open, so the line is unchanged.
3. **ISA-38:21 (Reviewer correction).** Now "with the pluperfect of ASV ('Now Isaiah had said') and KJV ('For Isaiah had said')". The earlier wording attributed ASV's phrasing to both.
4. **ISA-38:7 (optional precision, applied).** 2 Kgs 20:9 has *kî* for *ʾăšer* and lacks *hazzeh*; the note now says "nearly the same sentence" and gives both differences (MT checked).

## Founder rulings applied (sign-off 2026-11-27)

The founder signed off wave I-6 on 2026-11-27, choosing every recommended option.

- **ISA-38:8 speculative reception note.** Kept as labelled. The `maalot-steps-of-ahaz-isaiah-38` rationale in `wave-i6-ch38-overlay-diff.json` now reads "a separately labelled speculative reception note (founder sign-off 2026-11-27)". The commentary paragraph and the line are unchanged.
- **ISA-38:11 *ḥeḏel* "the world".** The decision recorded above (A, the line unchanged) stands.
- No pending wording remained in `chapter-38.json` outside the reviewerReport. `translation.status` and the reviewerReport were not touched.
