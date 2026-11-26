# Chapter 12 Editor Report

Isaiah 12 (6 verses), wave I-3 (Isa 7–12).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v2.93.0 and isaiah-woh overlay v1.6.1, both read-only, with the wave I-1 diffs and `wave-i3-rulings.md` treated as in force.
All glossary changes are in `wave-i3-ch12-overlay-diff.json` and `wave-i3-ch12-central-diff.json`.

## Summary

- **Editorial questions:** all 11 resolved, 0 escalated as unresolved. `editorial_questions[]` is empty.
- **English-line changes:** two verses, each backed by a glossary op:
  - 12:4 "call upon his name" → "call on his name" (central `qara-b-shem-yhwh`, extended).
  - 12:5 "he has done excellent things" → "he has done majestic things" (new overlay `geut-majesty-isaiah`).
- **Commentary:** all 6 verses have `notes.official`.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` and `overlayGlossaryVersion` are left at 2.93.0 and 1.6.1. The orchestrator sets them on merge.
  - Some `glossaryRefs` point to entries that exist only in the diffs.
- **Lens audit:** no English line carries a project reading. The chapter has no canon citation, and no commentary paragraph is labelled speculative.

## Speculative entries requiring sign-off

None. Every new entry is `claim_type: direct`.

## Items for the founder (recommended defaults, not blocking)

### ISA-12:5 — gēʾûṯ "majestic things" (departure from the PD baseline)

**Issue:** ASV has "excellent things", and JPS 1917 and NJPS have "gloriously".
**Decision:** "majestic things", which keeps the gʾh root concordant with gāʾôn "majesty" and with the stable 26:10 "the majesty of YHWH". "Gloriously" is excluded by wave rule 6, which reserves "glory" strictly for kāḇôḏ.
**Alternative:** revert to ASV "excellent things". That reading has no concordance problem but uses an obsolete sense of "excellent".
**Recommendation:** ship "majestic things".

### ISA-12:2 / Exod 15:2 / Ps 118:14 — one shared wording fixed now (central add)

**Issue:** the Translator asked whether to fix the wording of the shared line before exodus-woh 15 and psalms-woh 118 exist.
**Decision:** add the central entry `ozzi-ve-zimrat-yah-strength-and-song-exod-15-2-parallel-cross-corpus` with the wording "[Yah] is my strength and my song, and he has become my salvation". The zimrāh II "might" reading (NJPS; NRSV recalled) is disclosed at every site. appliesTo has only ISA-12:2; EXO-15:2 and PSA-118:14 are named as forward scope.
**Why flag:** this fixes a Torah wording from a prophetic book. A later Exodus Editor who prefers "might" will have to escalate rather than diverge.
**Recommendation:** accept.

### ISA-12:4 — Ps 105:1 = 1 Chr 16:8 parallel

No central entry is created now. The Isaiah line follows ASV's wording of Ps 105:1. The overlay `lexical-cruxes-isaiah-12` recommends a central parallel entry when the psalm is drafted.
**Recommendation:** accept the deferral.

## Decisions on the Translator's questions

1. **12:1 verbal sense.** Kept as a statement: "your anger has turned away, and you comfort me" (ASV, JPS 1917, NJPS). The Translator's attribution of a wish reading to "LXX/Vulgate" is not followed. The Vulgate has a past statement (recalled), and the LXX was not verified. The reversal of the 5:25 / 9:7–10:4 refrain is noted. → `lexical-cruxes-isaiah-12`.
2. **12:2 ʾēl syntax.** Nominal clause "God is my salvation" (ASV, JPS 1917). The NJPS construct reading is noted. → `lexical-cruxes-isaiah-12`; `elohim-el-eloah-monotheistic-formula-isaiah` extended.
3. **12:2 zimrāṯ.** "my strength and my song", with "my" supplied on both nouns. HALOT zimrāh II / NJPS "might" is disclosed. → central add (see above).
4. **12:2 Yah YHWH.** "Yah YHWH" with no comma, as at 26:4. → `yah-tzur-olamim-everlasting-rock-isaiah-26` extended. 1QIsaᵃ and the LXX were not verified, and the line follows MT.
5. **12:2 cross-book parallel.** Fixed now in the central entry (see above).
6. **12:3 maʿyān.** "wells" kept (ASV, JPS 1917). The lexical sense "spring / fountain" (NJPS "fountains") is given in commentary. Central `maayanot-tehom-rabbah` is not extended. → `lexical-cruxes-isaiah-12`.
7. **12:4 qirʾû ḇišmô / hazkîrû / Ps 105:1.** "call on his name" (central formula), "make mention" (ASV, JPS 1917). The "proclaim" alternative is noted. → central `qara-b-shem-yhwh` extended; `lexical-cruxes-isaiah-12`.
8. **12:4 quotation extents.** First song 12:1b–2, second song 12:4b–6, with 12:3 as narration. JPS 1917 and NJPS mark the same extents (checked on Sefaria). → `title-and-meta-conventions-isaiah` extended with an addendum.
9. **12:5 gēʾûṯ.** "majestic things" (see above). → new `geut-majesty-isaiah`.
10. **12:5 ketiv/qere and participle.** The qere is translated. The participle is read as a wish, "let this be known" (ASV, NJPS), and JPS 1917's "This is made known" is noted. → `mt-qere-textual-policy-isaiah` extended. On merge, the orchestrator should add "12:5" to that entry's wohChoice qere list.
11. **12:6 yôšeḇeṯ ṣiyyôn.** "O inhabitant of Zion" (ASV collective). The enthroned-city reading (NRSV "royal Zion", recalled) is noted. → `lexical-cruxes-isaiah-12`.

Also: 12:5 bᵉḵol-hāʾāreṣ is now governed by the overlay `eretz-cosmic-scope-isaiah-24` (universal horizon) instead of the central `eretz`. The rendering "earth" is unchanged.

## Verification notes

- **Checked:**
  - ASV wording of Isa 12, Exod 15:2, Ps 118:14 and Ps 105:1, against the data-library PD copies.
  - JPS 1917 Isa 12 and Exod 15:2, and the JPS gender-sensitive revision of NJPS at Isa 12, on Sefaria.
- **Not verified, and marked so in the commentary:** NRSV readings, the LXX, the Vulgate (recalled), 1QIsaᵃ at 12:2, and the Strong's numbers in the new entries.

## Concurrency notes for the orchestrator

- `geut-majesty-isaiah` names Isa 9:17 (Heb.) gēʾûṯ ʿāšān "a column of smoke" as a context clause, matching the chapter 9 draft. The chapter 9 Editor may add ISA-9:17 to its appliesTo.
- Likely overlaps with the 7–11 overlay diffs: `mt-qere-textual-policy-isaiah`, `elohim-el-eloah-monotheistic-formula-isaiah`, `title-and-meta-conventions-isaiah`, `eretz-cosmic-scope-isaiah-24`.

## Glossary changes for review

### Central glossary (proposed 2.95.0)

- Added: `ozzi-ve-zimrat-yah-strength-and-song-exod-15-2-parallel-cross-corpus` (claim_type: `direct`)
- Modified: `qara-b-shem-yhwh` (appliesTo + ISA-12:4; rationale addendum; wohChoice unchanged)

### Per-translation overlay (proposed 1.8.0)

- Added: `geut-majesty-isaiah` (claim_type: `direct`)
- Added: `lexical-cruxes-isaiah-12` (claim_type: `direct`)
- Modified (appliesTo only, some with rationale addenda): `yah-tzur-olamim-everlasting-rock-isaiah-26` (+12:2), `elohim-el-eloah-monotheistic-formula-isaiah` (+12:2), `mt-qere-textual-policy-isaiah` (+12:5), `eretz-cosmic-scope-isaiah-24` (+12:5), `title-and-meta-conventions-isaiah` (+12:1, 12:4)

## Post-review corrections

Applied 2026-11-26 after the Reviewer's report. `translation.status`, the `reviewerReport` block, every English line and both shared glossaries are unchanged.

1. **ISA-12:2 note, NJPS quotation.** "NJPS 'Yah—GOD—'" now reads "NJPS 'Yah the LORD' (the JPS gender-sensitive edition prints 'GOD' for the Tetragrammaton)". The 1985 NJPS has "Yah the LORD", and "GOD" is the gender-sensitive edition's rendering. Caveat: the other NJPS wordings quoted in the chapter-12 notes and entries were checked only in the gender-sensitive edition on Sefaria. These are "the God who gives me triumph", "might", "fountains of triumph", "proclaim", "declare", "Let this be made known" and "You who dwell in Zion". Their wording in the 1985 printing is not verified.
2. **Central diff, `ozzi-ve-zimrat-yah-strength-and-song-exod-15-2-parallel-cross-corpus`.**
   - The zammᵉrû (12:5) echo is now marked as Isaiah-specific support that does not carry over to Exod 15:2 or Ps 118:14.
   - The forward scope (EXO-15:2, PSA-118:14) is now stated as a DEFAULT. Those books' Editors confirm it before the refIds are added to appliesTo (founder ruling 2026-11-26: default, confirmed per book).
   - The wohChoice wording was adjusted to match.

## Founder rulings applied (2026-11-26)

The founder signed off wave I-3 with every recommended default ("Sign-off ok", 2026-11-26; `wave-i3-signoff-package.md`), together with wave I-1 decisions 1 and 2. `translation.status` and the `reviewerReport` block are unchanged. Statements above marked pending or provisional are settled as follows.

- **Forward scope of `ozzi-ve-zimrat-yah-…`:** the wohChoice and rationale now read "founder ruling 2026-11-26: default, confirmed per book" in place of "pending founder ruling". EXO-15:2 and PSA-118:14 stay outside appliesTo until those books' Editors confirm the wording.
- **12:5 "majestic things"** and the **12:4 deferral:** accepted as recommended. No change.
