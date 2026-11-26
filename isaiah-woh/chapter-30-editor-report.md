# Chapter 30 Editor Report

Isaiah 30 (33 verses), wave I-5 (Isa 28, 30, 31, 33–35).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v4.0.0 and isaiah-woh overlay v3.0.0, both read-only, with `wave-i5-rulings.md` in force.
All glossary changes are in `wave-i5-ch30-overlay-diff.json` (proposes 3.1.0) and `wave-i5-ch30-central-diff.json` (proposes 4.1.0).

## Summary

- **Editorial questions:** all 32 are resolved, and `editorial_questions[]` is empty. Two resolutions change the line and are put to the founder (below). No question is left unresolved.
- **English-line changes:** four verses change. Each change is backed by a glossary op.
  - 30:8 "inscribe it in a book" → "inscribe it on a scroll" (overlay `sefer-sealed-scroll-isaiah-29`, extended; consistent with the chapter 34 Editor's extension to 34:4 and 34:16).
  - 30:10 "to the prophets, 'Do not prophesy … prophesy deceptions'" → "to the visionaries, 'Do not see for us visions … see visions of deceptions'" (new overlay `roeh-chozeh-seer-visionary-isaiah`).
  - 30:20 "your teachers" (twice) → "your teacher" (new overlay `lexical-cruxes-isaiah-30`).
  - 30:30 "his glorious voice" → "the grandeur of his voice" (new overlay `hod-grandeur-isaiah`).
- **Title:** "the written witness" → "the tablet and the scroll". The line keeps MT *lāʿaḏ* "for ever" at 30:8 and does not print "witness" (`title-and-meta-conventions-isaiah`, appended).
- **Commentary:** all 33 verses have `notes.official`. Every overlay or central id cited in a note is in that verse's `glossaryRefs` and in the entry's appliesTo, either in the base or through this diff. The build script checked this.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 4.0.0 and 3.0.0; the orchestrator sets them on merge. No paragraph `translit` was added.
- **Verification:**
  - ASV: Isa 30 through bible-api.com.
  - JPS 1917 and NJPS (Tanakh, JPS 1985, not the Gender-Sensitive Edition): through the Translator's Sefaria v3 fetch.
  - Rashi on 30:20 and 30:26, and Targum Jonathan on 30:7, 8, 20, 26 and 33: through Sefaria v3.
  - Corpus usage of *hôḏ*: data-library psalms-woh, job-woh and daniel-woh.
  - The canon: TBWTT chs. 2, 3 and 5, and ETTMTTP ch. 2, in data-library.
  - Not verified, and labelled "recalled" or "not verified" in the commentary: LXX, 1QIsaᵃ, NRSV, BDB, HALOT, GKC, and the emendations.

## Speculative entries requiring sign-off

None. All four new overlay entries and all extensions are `claim_type: direct`.

**Speculative commentary paragraph (for the founder's information):** ISA-30:26 ends with a paragraph labelled "Wheel of Heaven reading (speculative; reception note, not a translation claim)".
- It says plainly that the canon does not cite the verse. I checked this: TBWTT quotes Isaiah only in chs. 3 and 5, and ETTMTTP only in ch. 2, and none of those passages is from Isaiah 30.
- It quotes TBWTT ch. 2 ("about two thousand Earth years") on the Genesis "day".
- It makes the reading conditional on the disputed creation-week sense of the article in *šiḇʿaṯ hayyāmîm*.
- The line renders the article and no more.

**Recommendation:** keep (per ruling 4 and the founder policy that keeps such notes).

---

## Founder decisions (recommended defaults; the line already carries the recommendation)

### `hod-grandeur-isaiah` — ISA-30:30 *hôḏ qôlô*

**Source:** הוֹד (*hôḏ*), "splendour, majesty, vigour". It occurs in Isaiah only here (not concordance-verified).

**WoH choice:** "the grandeur of his voice".

**Why it is escalated:** the house concordance already reserves every standard English word for this noun:
- "glory" for *kāḇôḏ*
- "splendor" for *hāḏār*
- "majesty" for *gāʾôn* and *gēʾûṯ* of God
- "honor" for *tip̄ʾereṯ*
- "beauty" for *ṣᵉḇî*

The versions read: ASV and JPS 1917 "his glorious voice", NJPS "His majestic voice" (all checked).

The corpus outside Isaiah is not settled:
- Ps 8:2 "your splendor"
- Job 37:22 "fearsome majesty"
- Job 40:10 *hôḏ wᵉhāḏār* "honor and splendor"
- Dan 11:21 "the honor of the kingdom"

"Grandeur" gives *hôḏ* its own word, and the Psalms pair *hôḏ wᵉhāḏār* (Ps 96:6; 104:1; 111:3; 1 Chr 16:27) would then read "grandeur and splendor".

**Options:**
- (A) "the grandeur of his voice". Recommended.
- (B) "the majesty of his voice" (NJPS), recording a collision with *gāʾôn*/*gēʾûṯ*.
- (C) ASV "his glorious voice". Not recommended: it puts the *kāḇôḏ* word on *hôḏ*.

**Possible follow-up:** a central *hôḏ* entry to align Psalms, Job and Daniel.

### `roeh-chozeh-seer-visionary-isaiah` — ISA-30:10

**Issue:** *lārōʾîm … wᵉlaḥōzîm* are two "seer" nouns, and the verse has no *nāḇîʾ*. ASV, JPS 1917 and NJPS print "the seers … the prophets" and render the *ḥzh* verbs "prophesy". The stable 29:10 prints *nᵉḇîʾîm* "the prophets" and *ḥōzîm* "the seers". The ASV wording would therefore give "prophets" to two different nouns in neighbouring chapters.

**Decision:**
- *rōʾeh* is "seer".
- *ḥōzeh* is "seer" when it stands alone (29:10) and "visionary" when *rōʾeh* stands beside it (30:10).
- The verbs are "see" and "see visions".

**Alternative:** revert to ASV "prophets / prophesy".

**Recommendation:** accept.

### ISA-30:20 — *môreyḵā* "your teacher" (in `lexical-cruxes-isaiah-30`)

**Decision:** singular, lower case, "your teacher". The draft and ASV have the plural.

**Grounds:**
- The verb *yikkānēp̄* is singular.
- The yod-before-suffix form occurs with singular III-he nouns. This chapter has an example: *miqneyḵā* with a singular verb at 30:23.
- JPS 1917 "thy Teacher", NJPS "your Guide" and Rashi (checked) read the singular.

Lower case keeps the identification with God in the commentary, as the book does with its other lower-case epithets.

**Options:**
- (A) "your teacher". Recommended.
- (B) "your Teacher" (JPS 1917). This puts the identification in the line.
- (C) ASV "your teachers".

There is no lens reading at this verse.

## Unresolved editorial questions

None.

## Decisions on the Translator's questions

1. **30:1 *nsk massēḵāh*.** ASV "make a league" is kept (the treaty libation). NJPS "weaving schemes", JPS 1917 "form projects" and the 25:7 and 30:22 homonyms are in the commentary. → `lexical-cruxes-isaiah-30`.
2. **30:1 *hôy* vocative.** Confirmed, "Woe, rebellious children". → `hoy-woe-isaiah` extended.
3. **30:2 *lāʿôz*.** JPS 1917 "take refuge" (from *ʿwz*). → `maoz-shalom-refuge-peace-isaiah-27` extended to 30:2–3 (the refuge/peace clause does not apply), plus the crux entry.
4. **30:2 *ûp̄î*.** The literal "asked of my mouth" is kept. → crux.
5. **30:4 "his".** The Hebrew suffix is kept. → crux.
6. **30:4 Zoan and Hanes.** ASV spellings. The identifications Tanis (NJPS note, checked) and Heracleopolis (not verified) are in the commentary. → `aram-names-isaiah` extended.
7. **30:5 ketiv/qere.** The qere is read. → `mt-qere-textual-policy-isaiah`, with the site added to the qere list.
8. **30:6 heading.** ASV and JPS 1917 with the overlay forms. The NJPS-noted emendation is in the commentary. → massa, oracle-names, seraphim and mt-qere extended, plus central `eretz`.
9. **30:7 Rahab.** MT and the name are kept. → new `rahab-sea-monster-name-isaiah`. Central `chaoskampf-sea-conflict-…` extended (commentary-only citation).
10. **30:7 *heḇel*.** Adverbial "in vain" kept. → crux.
11. **30:8 *sēp̄er*.** "scroll". → `sefer-sealed-scroll-isaiah-29` extended. This is consistent with the coordinator's note on the chapter 34 extension.
12. **30:8 *lāʿaḏ* / *yôm ʾaḥărôn*.** MT "for ever" and "the time to come" are kept. NJPS and Targum "witness" (checked) are in the commentary. → mt-qere and crux.
13. **30:9 *tôrāh*.** "teaching". → `torah-teaching-isaiah` extended.
14. **30:10 seers.** Changed; escalated above.
15. **30:15 *šûḇāh*.** "returning" (ASV) is kept. "Sitting still" (JPS 1917) and "stillness" (NJPS) are in the commentary, and the line does not decide between return and repentance. → crux.
16. **30:17 *tōren*.** "beacon" kept. → crux; `nes-signal-isaiah` extended.
17. **30:17 ellipsis and *gᵉʿārāh*.** The ellipsis is kept, with "rebuke". → crux.
18. **30:18 *yārûm* and *ʾašrê*.** "be exalted" and "blessed" (as the stable 32:20). → crux; `elohim-el-eloah-…` extended.
19. **30:19 *yēšēḇ*.** MT's finite verb is kept. The vocative of JPS 1917 and NJPS is in the commentary. → mt-qere, crux; central `zaaqah-…` extended.
20. **30:20 *môreyḵā*.** Changed to the singular; escalated above. Central `elon-moreh` is deliberately not extended, because it governs the toponym.
21. **30:20 bread and water.** ASV's construct reading is kept. → crux.
22. **30:22 *dāwāh*.** ASV "as an unclean thing" is kept. NJPS and the NJPS-noted revocalization are in the commentary. → crux, mt-qere; central `pesel-utemunah-…` extended.
23. **30:26 article.** "the light of the seven days", with the article rendered. Targum Jonathan and Rashi (343) were checked. A speculative reception paragraph follows. → crux; `kavod-labanah-chammah-isaiah-24` extended (moon/sun pair).
24. **30:27 *maśśāʾāh*.** "rising smoke" (ASV) is kept. NJPS "heavy burden" is in the commentary. → crux.
25. **30:28 sieve.** ASV "sieve of destruction" is kept. NJPS "yoke" is in the commentary. → crux; `ruach-…` extended ("breath" clause).
26. **30:29 *ṣûr*.** Lower-case "rock" confirmed. → `yah-tzur-olamim-…` extended.
27. **30:30 *hôḏ*.** Changed; escalated above.
28. **30:30 *nep̄eṣ*.** "cloudburst" kept. → crux.
29. **30:31 subject.** The unmarked "he" is kept. → crux.
30. **30:31 *yēḥaṯ*.** "be dismayed" kept. → crux.
31. **30:32 ketiv/qere, *mûsāḏāh*, *tᵉnûp̄āh*.** The qere is read; ASV "appointed staff" and "brandishing" are kept. → mt-qere (site added to the qere list), crux.
32. **30:33 Topheth and Molech.**
    - The qere *hîʾ* is read.
    - "a Topheth" (ASV) is kept; JPS 1917 "a hearth" is in the commentary.
    - MT "for the king" is kept; NJPS "Melech" (Molech) is in the commentary.
    - ASV's clause division is kept.
    - Targum "Gehinnom" (checked) is reported.
    - → mt-qere, crux; central `gehenna-valley-of-hinnom-…` extended (the line keeps the place name; the entry's wohChoice still governs only 1 En 27). Central `gophrit-va-esh-…` already lists 30:33.

## Glossary changes for review

### Central glossary (4.0.0 → 4.1.0, minor; appliesTo only)

- Modified: `eretz` (+30:6)
- Modified: `avon-iniquity-cross-corpus-keyword` (+30:13)
- Modified: `zaaqah-outcry-of-the-oppressed` (+30:19)
- Modified: `pesel-utemunah-graven-image-iconographic-prohibition-cross-corpus` (+30:22)
- Modified: `adam-adamah` (+30:23, 30:24)
- Modified: `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible` (+30:7)
- Modified: `gehenna-valley-of-hinnom-1-enoch-27-nt-cross-corpus` (+30:33)

All except `eretz` and `avon` also carry a rationale addendum.

Not extended, deliberately: `elon-moreh`, `sinai-theophany-…`, `yamm-yammu-…`.

### Per-translation overlay (3.0.0 → 3.1.0, minor)

Added (all `direct`):
- `hod-grandeur-isaiah`
- `roeh-chozeh-seer-visionary-isaiah`
- `rahab-sea-monster-name-isaiah`
- `lexical-cruxes-isaiah-30`

Modified (appliesTo plus rationale addendum; no field rewritten):
- `title-and-meta-conventions-isaiah`
- `hoy-woe-isaiah`
- `ruach-divine-spirit-lower-case-isaiah`
- `maoz-shalom-refuge-peace-isaiah-27`
- `aram-names-isaiah`
- `massa-oracle-superscription-isaiah`
- `oracle-names-isaiah-21`
- `seraphim-burning-ones-isaiah`
- `mt-qere-textual-policy-isaiah`. Orchestrator: add 30:5, 30:32 and 30:33 to the qere list in wohChoice.
- `sefer-sealed-scroll-isaiah-29`. Orchestrator: add the 30:8 clause to wohChoice, as a union with the chapter 34 op.
- `torah-teaching-isaiah`
- `yotser-potter-clay-image-isaiah`
- `adonai-yhwh-compound-isaiah-25`
- `nes-signal-isaiah`
- `elohim-el-eloah-monotheistic-formula-isaiah`
- `adonai-standalone-title-isaiah`
- `kavod-labanah-chammah-isaiah-24`
- `yah-tzur-olamim-everlasting-rock-isaiah-26`

**Concurrency:** merge appliesTo as a union with the other wave I-5 Editors. The known overlap is `sefer-sealed-scroll-isaiah-29` with chapter 34.

## Post-review corrections

These were applied after the Reviewer's pass, at the coordinator's instruction. `translation.status`, the `reviewerReport` block and the shared glossaries are unchanged.

1. **ISA-30:15 (Reviewer: revise, concordance).** The line now reads "For thus says the Lord YHWH, the Holy One of Israel:" (was "thus said").
   - *kî kōh ʾāmar* is the same formula as in v. 12, and the book prints "thus says" at every other *kōh ʾāmar* (checked: 7:7, 10:24, 29:22).
   - ASV and JPS 1917 "thus said" is recorded in the note.
   - Backed by `lexical-cruxes-isaiah-30` (source, translit, wohChoice and rationale updated in the overlay diff).
2. **ISA-30:26 (Reviewer: revise).** The unverified sentence "a reading that takes 'the seven days' as the week of creation is also current" is replaced with the readings checked on Sefaria:
   - Ibn Ezra: the seven days' light joined together (checked by the Editor).
   - Radak: figuratively, the light of the seven days of the week as one (checked by the Editor); his alternative, Solomon's seven-day dedication, was checked by the Reviewer.
   - b. Pesachim 68a and b. Sanhedrin 91b: the brightness of the days of the Messiah (checked by the Reviewer).
   - Targum Jonathan and Rashi: × 343.

   The note now says that none of them takes "the seven days" as the creation week.

   **The labelled speculative paragraph is dropped.** Its only link to the canon was the creation-week premise. No checked source supports that premise, and the canon does not cite the verse. Reworded, it would have been a project association attached to a verse that neither the text tradition nor the canon connects with it, so it no longer stands. The chapter now has no Wheel of Heaven paragraph. `lexical-cruxes-isaiah-30` records the checked readings.
3. **`roeh-chozeh-seer-visionary-isaiah` (Reviewer: revise, scope).** The wohChoice now limits ḥzh "see visions" to the places where it stands beside rʾh with these titles (30:10). Elsewhere ḥzh is "see" / "saw", as in the stable 1:1, 2:1, 13:1 and 26:11 and in the wave I-5 lines 33:17 and 20. The rationale records the scope correction. The 30:10 line is unchanged and remains a founder decision.
4. **ISA-30:33 (Reviewer: non-blocking).** The Topheth–Molech link now cites 2 Kgs 23:10, with the note that Jer 32:35 names the Hinnom valley and Molech but not Topheth.

The founder decisions above are unchanged: 30:30 *hôḏ* "grandeur", 30:10 "visionaries", and 30:20 "your teacher".

## Founder rulings applied (sign-off 2026-11-26)

The founder (zarazinsfuss) signed off wave I-5 on 2026-11-26 through an interactive form and chose every recommended option. No English line changes as a result; only notes and glossary-diff wording were updated. The wave merges as overlay 4.0.0 and central 5.0.0.

- **`hod-grandeur-isaiah`** (30:30 "the grandeur of his voice"): accepted. NJPS "majesty" stays recorded as the alternative.
- **`roeh-chozeh-seer-visionary-isaiah`** (30:10 "seers … visionaries"): accepted. ASV "prophets" stays recorded as the alternative.
- **30:20 "your teacher"** (`lexical-cruxes-isaiah-30`): accepted.
- The "pending" and "escalated" wording has been removed from the overlay diff (version note, hod wohChoice and rationale, roeh-chozeh rationale) and from the 30:30 note.
- Ch. 30 has no speculative paragraph (the 30:26 paragraph was dropped after review).
