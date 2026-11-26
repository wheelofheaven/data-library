# Chapter 4 Editor Report

Isaiah 4 (6 verses), wave I-1 (Isa 1–5).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v2.93.0 and isaiah-woh overlay v1.6.1, both read-only. All changes are in the diff files.

## Summary

- **Editorial questions:** all 9 resolved, 0 escalated. `editorial_questions[]` is empty.
- **English-line changes:** one verse, 4:5, backed by the new overlay entry `anan-chuppah-sukkah-zion-canopy-isaiah-4`:
  - ḥuppāh "covering" → "canopy".
  - The day/night group is now punctuated by the accents: "a cloud by day and smoke, and the shining of a flaming fire by night".
- **Commentary:** all 6 verses now have `notes.official`. 4:5 also carries a separately headed reception note labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` and `overlayGlossaryVersion` are left at 2.93.0 and 1.6.1. The orchestrator sets them on merge.
  - Some `glossaryRefs` point to overlay entries that exist only in the diff.
- **Lens audit:** no English line carries a project reading. The line at 4:5 adds no "pillar".

## Speculative entries requiring sign-off

No speculative glossary entry is proposed. One item in the commentary is labelled speculative and needs founder sign-off.

### ISA-4:5 reception note (commentary, not a glossary entry)

**Source:** עָנָן יוֹמָם וְעָשָׁן וְנֹגַהּ אֵשׁ לֶהָבָה לָיְלָה … כִּי עַל־כָּל־כָּבוֹד חֻפָּה
**WoH reading (commentary only):** *The Book Which Tells the Truth* (ch. 3) reads the Exodus pillar as a guidance craft. The note says this is a framework claim of the canon for Exod 13:21. Carrying it to the cloud, smoke and fire over Zion is a project synthesis.
**Why speculative:** the canon does not cite Isa 4:5. The extension goes beyond what any single source states. The central pillar entry also explicitly disavows the craft reading for the Hebrew.
**Recommendation:** ship as worded. The note reports the canon and labels the extension, and it does not argue for it. If the founder prefers silence at uncited verses, drop the final paragraph of the 4:5 note. Nothing else depends on it.

## Decisions on the Translator's questions

1. **ISA-4:1, chapter division and idioms.**
   - The MT division is kept, and the commentary notes that 4:1 closes the 3:16–4:1 oracle.
   - ASV's sense "let us be called by your name — take away our reproach" is kept. The literal idiom is in the commentary.
   - Central `yosef-double-name-aetiology` is cited and not extended. → `lexical-cruxes-isaiah-4`.
2. **ISA-4:2, ṣemaḥ YHWH.**
   - Lower-case "the branch of YHWH" and "the fruit of the land" are kept.
   - The vegetation reading is preferred by Wildberger, Williamson and Blenkinsopp.
   - The Targum's messianic reading and the Jer/Zech title are given in the commentary and not imposed by capitalisation.
   - `eretz-cosmic-scope-isaiah-24` is not extended. → new `tsemach-yhwh-branch-isaiah-4`.
3. **ISA-4:2, lᵉ-predicates and pᵉlêṭāh.**
   - The predicates stay nouns, and bare kāḇôḏ is "glory".
   - pᵉlêṭaṯ is "the survivors of Israel".
   - Central `pleitah-…` is not extended because its wohChoice is the event sense "a great deliverance". → `lexical-cruxes-isaiah-4`.
4. **ISA-4:3, remnant participles and kāṯûḇ la-ḥayyîm.**
   - Central `she-erit-…` is not extended because it governs the noun, not the participles.
   - ASV "written among the living" is kept, and "recorded/inscribed for life" is recorded in the commentary. → `lexical-cruxes-isaiah-4`.
5. **ISA-4:4, rûaḥ / mišpāṭ / bāʿēr / ṣōʾāh / dᵉmê.**
   - The draft is kept: "by a spirit of justice and by a spirit of burning".
   - The overlay `ruach-divine-spirit-lower-case-isaiah` is extended to cover the purging rûaḥ.
   - NJPS "blast", "judgment" and the purge sense are recorded in the commentary. → `lexical-cruxes-isaiah-4`, plus `adonai-standalone-title-isaiah` extended to 4:4.
6. **ISA-4:5, pillar entry and word order.**
   - Central `pillar-of-cloud-…` is extended to ISA-4:5, with a conditional-scope sentence: the verse has no ʿammûd and the line gives no "pillar", but the entry's Exodus relation and its disavowals govern the verse.
   - The word order is the Hebrew's, punctuated at the zaqef on wᵉʿāšān. → `anan-chuppah-sukkah-zion-canopy-isaiah-4`.
7. **ISA-4:5, kî ʿal-kol-kāḇôḏ ḥuppāh.**
   - ḥuppāh is now "canopy" (HALOT, NRSV, NJPS), a change for precision. ASV's construal "over all the glory" is kept.
   - The alternative "the glory shall be a canopy" is in the commentary.
   - No kāḇôḏ entry is extended. → `anan-chuppah-sukkah-zion-canopy-isaiah-4`.
8. **ISA-4:5, mᵉḵôn and miqrāʾehā; bārāʾ.**
   - "Habitation" and "her assemblies" (MT) are kept, and the LXX variants are reported.
   - `bara-create-isaiah` and `mt-qere-textual-policy-isaiah` are extended to 4:5. The LXX's *kai hēxei* is reported.
9. **ISA-4:6, sukkāh.**
   - ASV and NJPS "pavilion" is kept. The commentary sets it against "booth" at 1:8.
   - Central `sukkot-…` is not extended. → `anan-chuppah-sukkah-zion-canopy-isaiah-4`.

## Unresolved editorial questions

None.

## Glossary changes for review

### Central glossary (`wave-i1-ch4-central-diff.json`, "CENTRAL — apply by orchestrator")

- **Modified:** `pillar-of-cloud-and-fire-ammud-ha-anan-ve-esh-divine-presence-marker-cross-corpus` (claim_type stays `direct`).
  - appliesTo gains ISA-4:5, and one conditional-scope sentence is appended to the rationale. The wohChoice is unchanged.
  - If this wave's central policy is appliesTo-only, drop `rationaleAppend`.
  - Recommended version: 2.94.0. Renumber if the other wave I-1 diffs merge first.
- **Not extended (recorded):** `pleitah-…`, `she-erit-…`, `yosef-double-name-aetiology`, `sukkot-toponym-and-festival-etymology`, `kavod-yhwh`, `he-anan-cloud-fills-the-sanctuary-cross-corpus`, `tanur-ashan-lappid-esh-theophany`.
- **Possible future item:** make the pleitah entry conditional (event sense vs. collective "survivors"). That would change its wohChoice and require a major bump, so it is not proposed here.

### Per-translation overlay (`wave-i1-ch4-overlay-diff.json`, 1.6.1 → 1.7.0 recommended)

- **Added:** `tsemach-yhwh-branch-isaiah-4` (claim_type: `direct`) — ISA-4:2.
- **Added:** `anan-chuppah-sukkah-zion-canopy-isaiah-4` (claim_type: `direct`) — ISA-4:5, 4:6.
- **Added:** `lexical-cruxes-isaiah-4` (claim_type: `direct`) — ISA-4:1–4. This can be folded into a wave entry `lexical-cruxes-wave-i1-isaiah`.
- **Extended** (appliesTo plus one appended rationale sentence each; no wohChoice changed):
  - `title-and-meta-conventions-isaiah` (+ISA-4:1)
  - `adonai-standalone-title-isaiah` (+ISA-4:4)
  - `ruach-divine-spirit-lower-case-isaiah` (+ISA-4:4)
  - `bara-create-isaiah` (+ISA-4:5)
  - `mt-qere-textual-policy-isaiah` (+ISA-4:5)

## Post-review corrections

These were applied after the Reviewer pass. `translation.status` (`awaiting-human`) and the `reviewerReport` block are unchanged, and the shared glossaries were not touched.

1. **4:2, Zechariah claim** (commentary; rationale and wohChoice of `tsemach-yhwh-branch-isaiah-4`).
   - "A branch for David" is now attributed to Jer 23:5; 33:15 only.
   - In Zech 3:8; 6:12, "Branch" is described as a name: "my servant the Branch", "a man whose name is Branch".
   - None of these four passages has the construct ṣemaḥ YHWH.
   - Oswalt (*The Book of Isaiah 1–39*, NICOT, 1986) is named for the messianic reading. The Reviewer cited him for the same reading.
2. **4:4, NJPS misquotation** (commentary; `ruach-divine-spirit-lower-case-isaiah` rationaleAppend; `lexical-cruxes-isaiah-4` rationale).
   - The false NJPS "blast" quotation is removed. NJPS reads "a spirit of judgment … a spirit of purging".
   - The wind sense is now grounded in HALOT s.v. rûaḥ and recorded, not adopted.
   - NJPS "purging" is cited as a witness for the purge sense of bāʿar.
3. **4:2, concordance fix (English line changed).**
   - tip̄ʾereṯ changes from "splendor" to "honor": "pride and honor for the survivors of Israel". The grounding is the triad "for praise, for fame and for honor" (Deut 26:19; Jer 13:11).
   - "Splendor" stays reserved for hāḏār (`hadar-splendor-isaiah`, ch. 2 diff), "glory" for kāḇôḏ, and "beauty" for ṣᵉḇî.
   - The change is recorded in the `tsemach-yhwh-branch-isaiah-4` entry, which now lists tip̄ʾereṯ (H8597) among its forms.
   - Outstanding conflict: the signed-off 13:19 renders tip̄ʾereṯ "splendor" ("the splendor of the pride of the Chaldeans") and ṣᵉḇî "glory". That stable text already conflicts with `hadar-splendor-isaiah` and should be reconciled at merge. Elsewhere, 44:13 renders tip̄ʾereṯ "beauty" and the ch. 3 draft (3:18) renders it "finery".
4. **4:5, reception paragraph.**
   - The canon is now described from its own text: TBWTT 3:10–11 "we guided them" (Exod 13:21), and 3:13–14, the smoke laid behind the people as a curtain that slowed the pursuers (Exod 14:19).
   - "Guidance craft", which comes from the TBWTT apparatus note and not the canon, is removed.
   - The paragraph is still labelled speculative. Whether it ships is the founder's decision.
   - The matching clause in the central diff's `rationaleAppend` is reworded in the same way.
5. **Minor items the Reviewer raised.**
   - The unverified "Wildberger 'Baldachin'" is dropped from the `anan-chuppah-sukkah-zion-canopy-isaiah-4` rationale.
   - The NJPS footnote emendation "spread" (compare Ps 105:39) is added to the 4:5 commentary.
6. **Not changed; for the human (raised by the Reviewer).** Disavowal (i) of the central pillar entry says the canon engages Exod 13:21–22 in *Extra-Terrestrials Took Me To Their Planet*. The verified site is TBWTT ch. 3 (3:10–14). That is existing central text, outside this diff.
