# Chapter 16 Editor Report

Isaiah 16 (14 verses), wave I-4 (Isa 16–23).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v3.0.0 and isaiah-woh overlay v2.0.0, both read-only, with `wave-i4-rulings.md` in force.
All glossary changes are in `wave-i4-ch16-overlay-diff.json` (proposed 2.1.0) and `wave-i4-ch16-central-diff.json` (proposed 3.1.0).

## Summary

- **Editorial questions:** all 14 resolved, 0 escalated as unresolved. `editorial_questions[]` is empty.
- **English-line changes:** three verses, each backed by a glossary op:
  - 16:6 "of his arrogance and his pride" → "of his haughtiness and his pride" (new overlay `gaon-pride-human-arrogance-isaiah`; gaʾăwāh "haughtiness" as at stable 13:11).
  - 16:11 "my heart sounds like a lyre for Moab, and my inward parts" → "my inner parts sound like a lyre for Moab, and my inmost being" (new overlay `meim-inner-parts-isaiah`; "heart" kept for lēḇ, stable 15:5).
  - 16:14 "like the years of a hireling" → "as the years of a hireling" (new overlay `shnei-sakhir-years-of-hireling-isaiah`, wave ruling 14).
- **Commentary:** 13 of 14 verses have `notes.official`. 16:13 has none; its formula is covered in the 16:14 note.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` and `overlayGlossaryVersion` stay at 3.0.0 and 2.0.0. The orchestrator sets them on merge.
  - Some `glossaryRefs` point to entries that exist only in the diffs.
- **Lens audit:**
  - No English line carries a project reading.
  - The canon does not cite Isaiah 16: TBWTT ch. 3 quotes 15:8–9 and then 26:20, and no other data-library canon text cites the chapter. No speculative reception paragraph was written.
  - 16:5 (the Davidic throne) is rendered and annotated lexically only.

## Speculative entries requiring sign-off

None. Five new entries are `direct`. One, `moab-lament-present-tense-isaiah-16`, is `inferred`.

## Items for the founder (recommended defaults, not blocking)

### ISA-16:6: gāʾôn "pride" (recorded departure from ruling 2)

**Issue:** ruling 2 makes "majesty" the default for gāʾôn. Here gāʾôn names Moab's arrogance.
**Decision:**
- gāʾôn is "pride" (ASV, JPS 1917, NJPS; stable 13:19).
- gaʾăwāh is "haughtiness" (stable 13:11).
- gēʾ is "proud".
- ʿeḇrāh keeps ASV "wrath".
**Known inconsistency, not reopened:** the stable 9:8 and 25:11 render gaʾăwāh as "pride". Recommend a book-wide concordance pass on the gʾh nouns later.
**Recommendation:** ship.

### ISA-16:11: mēʿay "my inner parts" (departure from ASV, JPS 1917 and NJPS "my heart")

**Issue:** all three PD and Jewish baselines have "my heart". The stable 15:5, in the same lament, already gives "heart" to lēḇ.
**Decision:**
- mēʿay is "my inner parts" and qirbî is "my inmost being".
- The parallel Jer 48:36 has libbî twice, which is reported in commentary.
**Alternative:** revert to "my heart … my inward parts" (the draft and ASV). That would leave one English word for two Hebrew nouns in adjacent verses.
**Recommendation:** ship.

### ISA-16:7, 9–11: present-tense lament (`inferred`)

**Decision:** the lament is in the present, for consistency with stable ch. 15 (ruling 3). ASV and JPS 1917 have the future. NJPS has a jussive at 16:7 ("let Moab howl"), which is the main alternative and is disclosed in commentary.
**Recommendation:** ship.

### Isa 16 // Jer 48 parallel

**Decision:** recorded in the overlay entry `moab-lament-jer-48-parallel-isaiah-16`, with a verse map checked against the Hebrew of Jer 48:29–38 on Sefaria. jeremiah-woh 48 does not exist, so no central entry is created.
**Recommendation:** promote the entry to a central parallel entry when Jer 48 is drafted.

## Decisions on the Translator's questions

1. **16:1 kar / construction.** "Send the lamb for the ruler of the land" kept (singular kar, the tribute reading of ASV; 2 Kgs 3:4). ASV and JPS 1917 "the lambs" and NJPS "Dispatch as messenger" are given in commentary. "toward the wilderness" is kept. → `lexical-cruxes-isaiah-16`.
2. **16:1 Sela.** Place name, as at 42:11 and in NJPS. JPS 1917 "crags" is noted. → `lexical-cruxes-isaiah-16`.
3. **16:2 daughters of Moab / bird simile.** "the daughters of Moab" is kept, and the singular simile is kept with ASV's supplied "so" dropped. NJPS "villagers" and Num 21:25 are noted. → `lexical-cruxes-isaiah-16`.
4. **16:3 ketiv/qere and pᵉlîlāh.** The qere hāḇîʾî is translated. → `mt-qere-textual-policy-isaiah` extended. Orchestrator: add "16:3" to the qere list in wohChoice on merge. pᵉlîlāh "execute justice" is kept, and the commentary warns that it is not mišpāṭ. → `lexical-cruxes-isaiah-16`.
5. **16:3 quotation marks.** None, as in ASV. JPS 1917 marks 16:3–4a and NJPS marks 16:2–4a and 16:6 (checked); both are reported. → `title-and-meta-conventions-isaiah` extended.
6. **16:4 niddāḥay môʾāḇ.** MT is kept: "my outcasts; as for Moab". The NJPS construct and its note are reported; the LXX was not verified. hammēṣ "extortioner" and "those who trample" are kept. → `mt-qere-textual-policy-isaiah`, `lexical-cruxes-isaiah-16`.
7. **16:5 chesed.** A split pair takes the solitary entry, so ḥeseḏ is "kindness" and ʾĕmeṯ is "truth". → central `chesed-solitary-covenant-kindness` extended, with a split-pair rationale addendum. `chesed-v-emet` and `tzedakah-u-mishpat` are deliberately not extended. "swift in righteousness" is kept.
8. **16:6 gʾh cluster.** See above. → new `gaon-pride-human-arrogance-isaiah`.
9. **16:7 tense / raisin-cakes.** Present tense. → new `moab-lament-present-tense-isaiah-16`. "raisin-cakes" is MT; the Jer 48:31 reading "men" is reported.
10. **16:8 baʿălê ḡôyim.** ASV is kept. The JPS 1917 and NJPS (Baale-goiim) readings are reported. → `lexical-cruxes-isaiah-16`.
11. **16:9 hêḏāḏ.** "the shout" at both sites, without ASV's supplied words. Jer 48:32 šōḏēḏ and bᵉṣîrēḵ are reported. → `lexical-cruxes-isaiah-16`.
12. **16:11 mēʿay vs 15:5 lēḇ.** Decided for concordance: "my inner parts … my inmost being". → new `meim-inner-parts-isaiah`. kinnôr "lyre" and yehĕmû "sound" are kept.
13. **16:12 nirʾāh / nilʾāh.** MT and ASV are kept. The deletion as a dittography is reported only and not verified for particular editions. → `mt-qere-textual-policy-isaiah`, `lexical-cruxes-isaiah-16`.
14. **16:14 kišnê śāḵîr.** "as the years of a hireling" (ruling 14; ASV and JPS 1917 checked). → new `shnei-sakhir-years-of-hireling-isaiah`. The chapter 21 Editor's diff already contains the matching modify for ISA-21:16. "the great multitude" and kāḇôḏ "glory" are kept.

Also: `eretz` (16:1, 16:4) and `kerem-vineyard` (16:10) were extended centrally, and the existing refs are now backed by appliesTo.

## Verification notes

- **Checked:**
  - ASV Isa 16, in the data-library PD copy.
  - JPS 1917 and NJPS ("Tanakh: The Holy Scriptures, published by JPS") Isa 16 and Jer 48:29–38, on Sefaria.
  - The Hebrew of Jer 48:29–38 (Sefaria, Miqra according to the Masorah).
  - The canon's citations of Isaiah, in the data-library.
- **Not verified, and marked so in the text:** the LXX at 16:4, editions that delete nirʾāh at 16:12, and every Strong's number in the new entries (all flagged "from recall").
- **Not used:** NRSV.
- **Commentaries cited generally:** Wildberger and Blenkinsopp, "ad loc.", in the rationales only.

## Concurrency notes for the orchestrator

- Apply the `shnei-sakhir-years-of-hireling-isaiah` add before the chapter 21 modify.
- `gaon-pride-human-arrogance-isaiah` may be relevant to 23:9 (gᵉʾôn kol-ṣᵉḇî).
- Overlaps with sibling diffs:
  - overlay: `mt-qere-textual-policy-isaiah`, `title-and-meta-conventions-isaiah` (ch 17, 20, 21);
  - central: `eretz` (ch 21).

## Glossary changes for review

### Central glossary (proposed 3.1.0)

- Modified: `chesed-solitary-covenant-kindness` (appliesTo + ISA-16:5; split-pair addendum; wohChoice unchanged)
- Modified: `eretz` (appliesTo + ISA-16:1, ISA-16:4; addendum)
- Modified: `kerem-vineyard` (appliesTo + ISA-16:10; addendum)

### Per-translation overlay (proposed 2.1.0)

- Added: `shnei-sakhir-years-of-hireling-isaiah` (claim_type: `direct`)
- Added: `gaon-pride-human-arrogance-isaiah` (claim_type: `direct`)
- Added: `moab-lament-present-tense-isaiah-16` (claim_type: `inferred`)
- Added: `meim-inner-parts-isaiah` (claim_type: `direct`)
- Added: `moab-lament-jer-48-parallel-isaiah-16` (claim_type: `direct`)
- Added: `lexical-cruxes-isaiah-16` (claim_type: `direct`)
- Modified: `mt-qere-textual-policy-isaiah` (appliesTo + ISA-16:3, 16:4, 16:12; addendum; orchestrator to add 16:3 to the qere list)
- Modified: `title-and-meta-conventions-isaiah` (appliesTo + ISA-16:1, 16:3, 16:6, 16:13, 16:14; addendum)

## Post-review corrections

Applied 2026-11-26 after the Reviewer's report (status `awaiting-human`).
Untouched:
- `translation.status`;
- the `reviewerReport` block;
- all English lines;
- the shared glossaries.

Changes are confined to `notes.official` in `chapter-16.json` and two entries in `wave-i4-ch16-overlay-diff.json`.

1. **ISA-16:7 note (Reviewer revise).**
   - The note now says that the NJPS footnote reads "Jer. 48.36 has 'men'". The phrase ʾanšê qîr-ḥereś occurs at both Jer 48:31 and 48:36.
   - Added: Jer 48:31 is in the first person (ʾêlîl … ʾezʿāq "I wail … I cry out") with 3ms yehgeh, against Isaiah's yᵉyêlîl and 2mp tehgû.
2. **ISA-16:10 note (Reviewer revise).** The speaker shift is hedged, following the Reviewer's wording: "The first person who silences the shout is most naturally YHWH (cf. Jer 48:33, 35); whether the weeping 'I' of vv. 9 and 11 is the same speaker is disputed."
3. **Overlay `gaon-pride-human-arrogance-isaiah` (glossary revise).**
   - The wohChoice is now scoped to the recorded departure at 16:6. It no longer states a book-wide rule, and further sites need their Editor's recorded decision; the chapter 23 Editor extends the entry to 23:9.
   - Added a context clause for the planned concordance pass. It lists the stable renderings of gāʾôn as human arrogance, 13:11 "arrogance" and 14:11 "Your pomp", together with 4:2 and 13:19 "pride" and the gaʾăwāh "pride" sites at 9:8 and 25:11.
   - Added a rationale sentence recording the change. claim_type is unchanged (`direct`).
4. **Overlay `moab-lament-jer-48-parallel-isaiah-16` (glossary revise).** The four missing differences were added to the verse map:
   - Jer 48:31 is in the first person;
   - Jer 48:36 has ʾel-ʾanšê qîr-ḥereś where Isa 16:11 has lᵉqîr ḥāreś;
   - Jer 48:33 has ûmēʾereṣ môʾāḇ and ends hêḏāḏ lōʾ hêḏāḏ;
   - Jer 48:32 has mibbᵉḵî yaʿzēr ʾeḇkeh-lāḵ.

   Jer's gēʾeh for gēʾ at 48:29 was also noted. The rationale sentence now reads "records the differences that affect the English (completed after the wave I-4 review, which found four omitted)".
5. **ISA-16:2 note (Reviewer nit).** The note no longer implies that the Arnon appears in chapter 15. It now reads: "The Arnon is not named in chapter 15; the verse adds it to the Moabite places of that lament." Ruling 3 has the same slip; that is for the orchestrator to note.
