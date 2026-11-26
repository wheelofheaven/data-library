# Chapter 23 Editor Report

Isaiah 23 (18 verses), wave I-4 (Isa 16–23).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v3.0.0 and isaiah-woh overlay v2.0.0, both read-only, with `wave-i4-rulings.md` in force.
All glossary changes are in `wave-i4-ch23-overlay-diff.json` and `wave-i4-ch23-central-diff.json`.

## Summary

- **Editorial questions:** all 23 are resolved. None is escalated as unresolved, and `editorial_questions[]` is empty.
- **English-line changes:** three verses change, and each change is backed by a glossary op.
  - 23:3 "the harvest of the river" → "the harvest of the Nile" (central `yeor-nile-egyptian-loanword`, Isaiah context clause).
  - 23:10 "like the river" → "like the Nile" (same op).
  - 23:9 "the pride of all glory" → "the pride of all beauty" (overlay `tsemach-yhwh-branch-isaiah-4`, ṣᵉḇî item, extended).
- **Commentary:** all 18 verses have `notes.official`.
- **Status:** `editor-review`, `1.0.0-rc1`, and "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` and `overlayGlossaryVersion` stay at 3.0.0 and 2.0.0. The orchestrator sets them on merge.
  - `lexical-cruxes-isaiah-23` and `gaon-pride-human-arrogance-isaiah` exist only in the wave diffs. The second is added by the chapter 16 Editor.
- **Lens audit:** no English line carries a project reading. I checked the canon in data-library: *The Book Which Tells the Truth* chs. 3 and 5 and *Extraterrestrials Took Me to Their Planet* ch. 2 quote Isaiah, but never chapter 23, and the canon does not mention Tyre or Tarshish. For that reason the chapter has no speculative commentary paragraph.
- **Verification:** I checked these against the texts:
  - ASV through bible-api.com: Isa 23, 19:5–8 and 7:18.
  - JPS 1917 and NJPS (Tanakh, JPS 1985, not the Gender-Sensitive Edition) through the Sefaria API v3, including 23:18.
  - KJV 23:5.

  The 1QIsaᵃ readings come from Fred P. Miller's online collation of col. XVIII (ao.net/~fmoeller), which is not DJD 32, and the commentary marks them that way. I did not verify the NRSV, the LXX (verified afterwards by the Reviewer; see Post-review corrections), the BDB and HALOT articles, or the commentators, and the commentary labels them "recalled" or "not verified".

## Speculative entries requiring sign-off

None. Every new or extended entry is `claim_type: direct`.

## Items for the founder (recommended defaults, not blocking)

### ISA-23:3, 23:10 — yᵉʾôr "the Nile" (central context clause)

**Issue:** the central entry's default is "the river", and it rests on the ASV baseline.
- In Isaiah, ASV itself prints "the Nile" for singular yᵉʾôr (19:7, 8; 23:3, 10; checked). JPS 1917 and NJPS do the same at 23:3 and 23:10.
- "The river" would also collide with nāhār "the River", the Euphrates (7:20; 8:7; 11:15; 27:12).

**Decision:** add a `changes.wohChoice` Isaiah context clause: "the Nile" for singular yᵉʾôr, and "rivers" for the plural (7:18). The Genesis default is unchanged.

**Concurrency:** the chapter 19 Editor's diff only extends appliesTo on this entry and does not change its wohChoice, so the merge has no field conflict. (Corrected after review; an earlier version of this report warned of a clash.)

**Semver:** I propose a minor bump, by analogy with the `eretz` context clauses. If any wohChoice edit counts as a modification, the bump is major.

**Alternative:** revert both lines to "the river".

**Recommendation:** accept "the Nile".

### ISA-23:9 — ṣᵉḇî "beauty" vs stable 13:19 and 24:16 "glory"

**Decision:** "beauty", for four reasons:
- Wave I-4 ruling 2 reserves "glory" for kāḇôḏ.
- The stable 4:2 already prints ṣᵉḇî "beauty".
- NJPS has "all glorious beauty" here.
- It is the lexical sense.

**Open:** the stable 13:19 "the glory of kingdoms" and 24:16 "Glory to the righteous one!" print "glory" for ṣᵉḇî. These two verses are not added to appliesTo.

**Options:**
- (A) Revise 13:19 and 24:16 to "beauty". At 24:16 that gives "Beauty to the righteous one!", which is awkward.
- (B) Record both as idiomatic departures.
- (C) Revert 23:9 to ASV "glory".

**Recommendation:** (B) for 24:16, where the acclamation idiom favors "Glory". For 13:19, either (A) or (B); "the beauty of kingdoms" (NJPS-type) is natural English.

### ISA-23:9 — gāʾôn "pride" (recorded ruling-2 departure)

Per the coordinator's addendum, I extend the chapter 16 Editor's `gaon-pride-human-arrogance-isaiah` (appliesToAdded ISA-23:9) and create no separate entry. The commentary cites that entry. This op depends on the chapter 16 add being merged first.

### ISA-23:13 — Chaldeans / Assyria crux

The line follows MT and ASV, keeps "Chaldeans" rather than the central `eretz-kasdim` form "Kasdim", and keeps MT's change of number in the second half. The commentary gives the other readings: the NJPS construal and the "ships" reading, the NRSV repunctuation (recalled), the kittîm emendation (NJPS note), and the gloss hypothesis. **Recommendation:** accept.

## Unresolved editorial questions

None.

## Decisions on the Translator's questions

1. **23:1 mibbayit mibbôʾ.** Kept as ASV's privative reading. The NJPS construal and the harbor sense are given in commentary. → `lexical-cruxes-isaiah-23`.
2. **23:1 place names.** Kittim, Shihor (no article, as MT, JPS 1917 and NJPS), Canaan, Tarshish and Chaldeans. The identifications appear in commentary only. → `lexical-cruxes-isaiah-23`; `aram-names-isaiah` extended for Egypt and Assyria.
3. **23:2 dōmmû / millᵉʾûḵ.**
   - "Be still" and MT are kept.
   - NJPS "Moan" was checked and is reported.
   - 1QIsaᵃ mlʾkyk is confirmed in the online collation, but not against DJD 32.

   → `lexical-cruxes-isaiah-23`, `mt-qere-textual-policy-isaiah`.
4. **23:2, 6 ʾî.** "coastland" → `lexical-cruxes-isaiah-11` extended (as chapter 20 did).
5. **23:3, 10 yᵉʾôr.** "the Nile" (see the founder item above).
6. **23:3 sᵉḥar.** "the market of nations".
7. **23:4, 12 bᵉṯûlāh.** "virgins" and "virgin daughter of Sidon" (ASV, JPS 1917). NJPS "maidens" is given in commentary.
8. **23:5.** Temporal "When the report comes" (ASV). KJV (checked) and NJPS are reported.
9. **23:7, 12 ʿlz.** "jubilant city" and "exult", kept apart from śmḥ.
10. **23:8 hammaʿăṭîrāh.** "the bestower of crowns" (ASV).
11. **23:8 kinʿāneyhā.** "traders".
12. **23:8–9 niḵbaddê.** "the honored of the earth". It is a participle, not kāḇôḏ (as in 43:4). The qll/kbd wordplay is noted in commentary.
13. **23:9 concordance.** "to profane the pride of all beauty" (see the founder items above).
14. **23:10 crux.** MT and ASV are kept.
    - **Correction:** the draft's claim that 1QIsaᵃ reads "ships of Tarshish" is not supported, because the collation lists no variant. "Ships of Tarshish" is reported as an emendation ("Emendation yields", NJPS note, checked) with partial support in the LXX's "ships".
    - The LXX (Rahlfs) "work your land … ships no longer come from Carthage" is now verified (see Post-review corrections).
15. **23:12 ketiv/qere.** Kittim, qere → `mt-qere-textual-policy-isaiah`. The orchestrator should add 23:12 and 23:13 to the wohChoice qere list.
16. **23:13 crux.** See the founder item above. "those who dwell in the wilderness" (ASV) is kept against 13:21 "desert creatures", because it leaves open whether people or beasts are meant.
17. **23:13 qere and number.** "his siege towers … he made it a ruin", with MT's numbers kept.
18. **23:15 "like the days of one king".** Kept. The seventy-related central entries are not applied.
19. **23:15–16 song and kinnôr.** The song is quoted and kinnôr is "lyre".
20. **23:17 pqd.** "visit" (ASV).
    - **Correction:** "remember" is JPS 1917; NJPS reads "take note of".
    - The "punished" entry for 24:22 is not extended.
21. **23:17 ʾeṯnan / znh.** "hire" and "prostitute herself" → central `zonah-…` extended to the verb and the fee noun (23:15–18).
22. **23:18 qōḏeš laYHWH.** "holiness to YHWH" (ASV, JPS 1917). NJPS "consecrated" is reported.
23. **23:18 ʿāṯîq.** "durable clothing" (ASV). JPS 1917 "stately" and NJPS "elegantly" are given in commentary.

## Glossary changes for review

### Central glossary (3.0.0 → 3.1.0 proposed)

- Modified: `yeor-nile-egyptian-loanword`. appliesTo +ISA-23:3, 23:10; `changes.wohChoice` appends the Isaiah "the Nile" context clause; rationale addendum.
- Modified: `zonah-prostitute-status-vocabulary-cross-corpus`. appliesTo +ISA-23:15–18; addendum covering the verb znh and ʾeṯnan "hire".
- Modified: `eretz`. appliesTo +ISA-23:1, 23:10, 23:13.
- Modified: `adam-adamah`. appliesTo +ISA-23:17.
- Deliberately not extended: `eretz-kasdim`, `paqod-yiphqod-…`, and the seventy-related entries.

### Per-translation overlay (2.0.0 → 2.1.0 proposed)

- Added: `lexical-cruxes-isaiah-23` (claim_type: `direct`).
- Modified (appliesTo plus addenda; no wohChoice changed):
  - `massa-oracle-superscription-isaiah`
  - `title-and-meta-conventions-isaiah`
  - `mt-qere-textual-policy-isaiah` (the qere list needs 23:12 and 23:13 on merge)
  - `lexical-cruxes-isaiah-11`
  - `aram-names-isaiah`
  - `eretz-cosmic-scope-isaiah-24`
  - `yhwh-tzevaot-hosts-isaiah`
  - `gaon-pride-human-arrogance-isaiah` (added by the chapter 16 diff)
  - `tsemach-yhwh-branch-isaiah-4` (ṣᵉḇî item)

## Post-review corrections

These corrections were applied after the Reviewer's report (chapter status `awaiting-human`). Every one is a correction to commentary or apparatus. No English line, no `translation.status`, no `reviewerReport` content and no shared glossary was changed.

1. **ISA-23:10, note.** The unverified LXX sentence is replaced by the reading the Reviewer verified in Rahlfs: ἐργάζου τὴν γῆν σου "work your land" (ʿbdy for ʿbry), continuing "for ships no longer come from Carthage". "Ships of Tarshish" is no longer called a modern emendation. The note now says it is an emendation ("Emendation yields", NJPS note) with partial support in the LXX's "ships". The 1QIsaᵃ point stays "not verified". The same correction is made in the overlay diff: the `lexical-cruxes-isaiah-23` wohChoice and standardEnglish, and the `mt-qere-textual-policy-isaiah` rationaleAppend.
2. **Collation author.** The online 1QIsaᵃ collation is by Fred P. Miller (ao.net/~fmoeller, "Moellerhaus"), not "F. Moeller". This is corrected in the notes at 23:2, 10, 11, 13 and 15, in the `lexical-cruxes-isaiah-23` rationale, in the `mt-qere-textual-policy-isaiah` rationaleAppend, and in this report.
3. **ISA-23:9, note.** 4:2 is removed as an instance of gāʾôn in the sense of human self-exaltation, because at 4:2 the word is positive. The note now cites 13:19 ("the pride of the Chaldeans") and 16:6 only.
4. **ISA-23:1, note.** The quotation "without house or haven" is recalled RSV rather than NRSV and could not be verified, so the attribution is removed. The note now says only that some modern versions make the harbor sense explicit.
5. **Central `yeor-nile-egyptian-loanword`, `changes.wohChoice`.** The plural rule now reads: "the plural yᵉʾōrîm is 'rivers' (7:18 'the rivers of Egypt') or 'streams' where nᵉhārôt 'rivers' stands beside it (19:6)."
6. **This report.** The concurrency warning about chapter 19 is corrected. The chapter 19 diff only adds appliesTo on the yeor entry, so the merge has no `changes.wohChoice` conflict.
