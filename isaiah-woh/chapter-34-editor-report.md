# Chapter 34 Editor Report

Isaiah 34 (17 verses), wave I-5 (Isa 28, 30, 31, 33–35).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v4.0.0 and isaiah-woh overlay v3.0.0, both read-only.
`wave-i5-rulings.md` is binding, including the corrected rule 3 (*šāmayim* is "skies"; "heavens" only inside the fixed phrase "the host of the heavens").
All glossary changes are in `wave-i5-ch34-overlay-diff.json` and `wave-i5-ch34-central-diff.json`.

## Summary

- **Editorial questions:** all 20 resolved; `editorial_questions[]` is empty.
- **Commentary:** 16 of 17 verses have `notes.official`. 34:10 has none, because it has no crux or ruled decision. The 34:8 note is a single short note on *rîḇ*.
- **English-line changes:** two verses, both backed by glossary entries.
  - 34:4: "shall be dissolved" becomes "shall rot away" (`lexical-cruxes-isaiah-34`). "the heavens shall be rolled up" becomes "the skies shall be rolled up" (central `shamayim`, corrected rule 3).
  - 34:5: "drunk its fill in the heavens" becomes "drunk its fill in the skies" (central `shamayim`, corrected rule 3).
- **Title:** "the host of the heavens dissolved" becomes "the host of the heavens rots away", to follow 34:4 (`title-and-meta-conventions-isaiah`).
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 4.0.0 and 3.0.0 for the orchestrator to set on merge. `i18n.he` is unchanged, and no paragraph `translit` was added.
- **Lens audit:** no English line carries a project reading. Two final paragraphs are labelled "Wheel of Heaven reading (reception note, not a translation claim; claim type: speculative)", at 34:4 and 34:14. Both say plainly that the canon does not cite the verse.
  - **Canon check:** the data-library texts of *The Book Which Tells the Truth*, *Extraterrestrials Took Me to Their Planet* and *Let's Welcome the Extraterrestrials* were searched. None cites Isaiah 34 or names Lilith.
    - TBWTT's Isaiah citations are all in chs. 3 and 5. They cover Isa 6, 13, 14, 15, 26, 27, 29, 32, 40, 42–45, 48, 54 and 65.
    - LWTE ch. 2 (LWTE-2:148–153) quotes Rev 6:12–15, which takes up Isa 34:4. It reads "the sky receded as a scroll" as the blast of an atomic explosion. The 34:4 note quotes that text and states that the canon applies the image to Revelation only.
- **References checked on 2026-11-26.**
  - NJPS ("Tanakh: The Holy Scriptures, published by JPS", 1985) and JPS 1917 on Sefaria, `/api/v3/texts/Isaiah.34?version=english|all`. The Gender-Sensitive Edition was not used.
  - ASV 1901 and KJV (34:4, 11–15) on bible-api.com.
  - Rev 6:13–14 (Greek and English) from the corpus `revelation-woh` file.
  - Lev 17:7 and its entry from `leviticus-woh`.
  - The following are cited from memory and marked "recalled" or "not verified": NRSV, RSV, LXX, the Vulgate, 1QIsaᵃ (except as the NJPS notes report it), CAD, BDB, HALOT, DDD, and the Qumran and Talmud references for Lilith.

## Speculative entries requiring sign-off

There are no speculative glossary entries. All three new overlay entries are `direct`, and the modify ops only extend appliesTo and add rationale sentences.

The two speculative commentary paragraphs (34:4 and 34:14) are listed here for founder review under the founder policy that keeps such notes.

### Commentary paragraph at `ISA-34:4`

**Content:** the paragraph quotes LWTE-2:153 on Rev 6:14 and states that the canon does not cite Isa 34:4. It says that carrying the atomic-war reading back to Isaiah would be a project synthesis.
**Recommendation:** ship. The paragraph asserts nothing beyond what the canon text says, and it labels the extension as going beyond the canon.

### Commentary paragraph at `ISA-34:14`

**Content:** the paragraph states that the canon neither cites the verse nor names Lilith, so no canon reading is quoted. It points to the wiki's comparative treatment (*Adam and Eve*; *Satan*), which records the Lilith traditions without adopting them, and it says that an Eden link would rest on the medieval *Alphabet of Ben Sira*, not on Isaiah or the canon.
**Recommendation:** ship. It could also be dropped without loss, because it reports an absence.

---

## Unresolved editorial questions

None are blocked. These decisions are flagged for the Reviewer and the founder.

### `ISA-34:14`: śāʿîr, "the wild goat" or "goat-demon"

**Issue:** the corpus prints "goat-demons" at LEV-WOH-17:7 (`seirim-goat-demons-leviticus-17-7`) and "wild goats" at the stable ISA-13:21 (`lexical-cruxes-wave-i2-isaiah`).
**Decision:** "the wild goat" (ASV), following 13:21. The rule is recorded in the `lexical-cruxes-wave-i2-isaiah` rationaleAppend. In a cult context, where the *śᵉʿîrîm* receive sacrifice, the noun is rendered "goat-demon". In Isaiah's lists of creatures in a ruin it is rendered "wild goat".
**Options considered:** "the wild goat" (ASV; 13:21); "Goat-demons" (NJPS; Lev 17:7); "the satyr" (JPS 1917).
**Why flagged:** in this verse the next clause has *lîlîṯ*, which is a demon by philology. That makes the demonic reading stronger here than at 13:21, and NJPS reads demons at both sites. If the founder prefers "goat-demon(s)", 13:21 (stable) and 34:14 should change together, and the i2 entry's wohChoice would change (a major bump).

### `ISA-34:4` and `ISA-34:5`: "skies" beside "the host of the heavens"

**Decision:** corrected rule 3 applied: "all the host of the heavens shall rot away, and the skies shall be rolled up like a scroll"; and at 34:5, "in the skies".
**Register exception considered and declined at 34:5:** *baš-šāmayim* there names the place where the sword acts against the host of v. 4. It does not name YHWH's dwelling, and NJPS has "in the sky". The divine-realm test of the central entry (which put 14:12–13 in "the heavens") is therefore not met.
**Cost, recorded:** one Hebrew word has two English forms in one verse (34:4). The 34:4 note states this.

### `ISA-34:11`: qippōḏ "porcupine"

**Decision:** kept for concordance with stable 14:23 ("the porcupine"; `ruin-fauna-isaiah`), although the bird list favours a bird (JPS 1917 "bittern", NJPS "owls").
**Why flagged:** if a later pass changes it, 14:23 should change with it.

### `ISA-34:16`: MT "my mouth"

**Decision:** MT is translated ("for my mouth, it has commanded"), with ASV and JPS 1917. The NJPS emendation "His" is reported in commentary. The 1QIsaᵃ "his mouth" was not checked and is marked so.

### `ISA-34:16`: "the scroll of YHWH"

**Decision:** "scroll", consistent with 34:4 and chapter 29 (`sefer-sealed-scroll-isaiah-29`). No referent is named in the line or the apparatus.
**Cross-chapter note:** the chapter-30 draft has "in a book" for *bᵉsēp̄er* at 30:8. That is for the chapter-30 Editor, and this Editor did not touch it.

---

## Decisions on the Translator's questions

1. **34:1 hāʾāreṣ ûmᵉlōʾāh:** the earth, its fullness (ASV) is kept. → `eretz-cosmic-scope-isaiah-24` extended; `lexical-cruxes-isaiah-34`.
2. **34:2 ṣᵉḇāʾām / heḥĕrîmām:** "their host" is kept. "devoted them to destruction" is kept. → central `cherem` extended.
3. **34:3 nāmassû:** "melted" (ASV, JPS 1917) is kept. NJPS "drenched" is in commentary. → crux entry.
4. **34:4 šāmayim register:** "the host of the heavens … the skies" (corrected rule 3; line change). → central `shamayim` and `tzeva-ha-shamayim-…` extended.
5. **34:4 nāmaqqû:** "shall rot away" is a line change. The 1QIsaᵃ reading is reported through the NJPS note. → crux entry; `mt-qere-textual-policy-isaiah`.
6. **34:4 nbl / kas-sēp̄er:** "fade" and the supplied "leaf" (ASV) are kept. "like a scroll" is kept. → crux entry; `sefer-sealed-scroll-isaiah-29` extended.
7. **34:5 baššāmayim:** "in the skies" is a line change. The register exception was declined (see above). The 1QIsaᵃ "be seen" is reported through the NJPS note.
8. **34:5 ʿam ḥermî:** "the people I have devoted to destruction" is kept, rendered verbally as NJPS does. → central `cherem` rationaleAppend.
9. **34:6 ḥereḇ laYHWH:** ASV is kept. The NJPS construal is in commentary. "fat … fat" is kept. → crux entry; central `qorbanot` and `eretz` extended.
10. **34:7:** ASV is kept. The NJPS emendation note is in commentary. → `mt-qere-textual-policy-isaiah`; central `eretz`.
11. **34:11 ruin-birds:** pelican, porcupine, owl, raven (ASV; 14:23). → new `ruin-fauna-isaiah`; central `yonah-orev` extended.
12. **34:11 qaw-tōhû wᵉʾaḇnê-ḇōhû:** "the line of wasteland and the plummet of emptiness" is kept. → central `tohu-vavohu` (governs the pair) and overlay `qav-qav-line-isaiah` extended. The overlay `tohu-bare-emptiness-wasteland-isaiah` is cited in commentary but not extended, because the split pair belongs to the central entry (one entry per decision).
13. **34:12 crux:** ASV is kept. The JPS 1917 and NJPS readings and the lost-word proposal are in commentary. → crux entry.
14. **34:13 tannîm / ḥāṣîr:** "jackals" and "a court" (ASV). Central `taninim` is deliberately not applied. → `ruin-fauna-isaiah`; crux entry.
15. **34:14 ṣiyyîm / ʾiyyîm:** "desert creatures … hyenas", as at 13:21–22. → `ruin-fauna-isaiah`.
16. **34:14 śāʿîr:** "the wild goat" (see above). → `lexical-cruxes-wave-i2-isaiah` extended.
17. **34:14 lîlîṯ:** "the night-monster" (ASV, JPS 1917). The philology is in the line note, then the Lilith reception, then the labelled speculative paragraph. → new `lilit-night-monster-isaiah-34`.
18. **34:15 qippôz / dayyôṯ:** "dart-snake … kites" (ASV). → `ruin-fauna-isaiah`.
19. **34:16 sēp̄er YHWH:** "the scroll of YHWH". → `sefer-sealed-scroll-isaiah-29` extended.
20. **34:16 p̄î / rûḥô:** MT "my mouth" and lower-case "his spirit". JPS 1917 "the breath thereof" is in commentary. → `ruach-divine-spirit-lower-case-isaiah` and `mt-qere-textual-policy-isaiah` extended.

---

## Glossary changes for review

### Central glossary (proposed 4.0.0 → 4.1.0; `wave-i5-ch34-central-diff.json`)

All seven ops are appliesTo-only, and six of them also append one rationale sentence.

- Modified: `shamayim`, ISA-34:4 and 34:5 ("skies").
- Modified: `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus`, ISA-34:4.
- Modified: `cherem-devote-to-destruction-cross-corpus`, ISA-34:2 and 34:5 (the suffixed noun is rendered verbally).
- Modified: `tohu-vavohu`, ISA-34:11.
- Modified: `yonah-orev`, ISA-34:11.
- Modified: `eretz`, ISA-34:6, 34:7 and 34:9 (territorial "land").
- Modified: `qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus`, ISA-34:6 (*zeḇaḥ*). This op has no rationaleAppend.
- No op: `gophrit-va-esh-destruction-formula` already lists ISA-34:9.

### Per-translation overlay (proposed 3.0.0 → 3.1.0; `wave-i5-ch34-overlay-diff.json`)

- Added: `lilit-night-monster-isaiah-34` (claim_type: `direct`)
- Added: `ruin-fauna-isaiah` (claim_type: `direct`). It recommends that the orchestrator add ISA-13:21, 13:22, 14:23 and 43:20 with no line change, and that the chapter-35 Editor add 35:7.
- Added: `lexical-cruxes-isaiah-34` (claim_type: `direct`)
- Modified (appliesTo, plus a rationale sentence):
  - `title-and-meta-conventions-isaiah` (34:1)
  - `eretz-cosmic-scope-isaiah-24` (34:1)
  - `sefer-sealed-scroll-isaiah-29` (34:4, 16)
  - `qav-qav-line-isaiah` (34:11, 17)
  - `lexical-cruxes-wave-i2-isaiah` (34:14)
  - `ruach-divine-spirit-lower-case-isaiah` (34:16)
  - `mt-qere-textual-policy-isaiah` (34:4, 5, 7, 16)

Strong's numbers in the new entries come from memory and are marked as not checked against a concordance.

---

## Post-review corrections

The Reviewer's verdicts (`translation.reviewerReport`, 2026-11-26T19:09:19Z) are applied as listed below. Only three files changed: the 34:14 commentary, this report and the Editor's own overlay diff. Nothing else was touched: no English line, `translation.status` (still `awaiting-human`), the `reviewerReport` block, the central diff or any shared glossary.

1. **`lilit-night-monster-isaiah-34` (revise).**
   - The rationale no longer says that "the night-monster" "matches the philology".
     - It now says that the rendering reflects how Hebrew hearers took the word, as related to *layil* "night", and that it is the public-domain baseline.
     - It records that the Akkadian–Sumerian philology traces the class name to *líl* "wind, breath".
     - It names NJPS "the lilith" (a lower-case class noun) as the alternative that follows that philology.
   - The wohChoice now stages "the lilith", marked **PENDING FOUNDER RULING**. The staged line is "yes, there the lilith shall settle, and shall find for herself a place of rest."
   - The 34:14 note says the same.
2. **KJV characterisation (34:14 note and entry).** The text no longer says that KJV takes "every name in the list as an animal". It now says that KJV takes *lîlîṯ* as a bird ("the screech owl"), although it renders *śāʿîr* in the same verse as "the satyr".
3. **Talmud references (34:14 note and entry).**
   - Long hair: b. ʿErub. 100b.
   - Wings: b. Nid. 24b.
   - Seizing those who sleep alone: b. Šabb. 151b.
   - All three are still marked "recalled".
4. **`ruin-fauna-isaiah` (revise).**
   - The Strong's number for *tan* "jackal" is corrected to H8565. The field notes that Strong's concordance tags Isa 34:13 under H8577 *tannîn* only because KJV reads "dragons".
   - Zeph 2:14 is added to the *qippōḏ* discussion as evidence that it is a bird: there *qāʾaṯ* and *qippōḏ* lodge on the capitals of columns.
5. **śāʿîr at 34:14 (flag-for-human).** "The wild goat" stays in the line.
   - "Goat-demon" is staged in the `lexical-cruxes-wave-i2-isaiah` modify op, marked **PENDING FOUNDER RULING**.
   - If it is adopted, both lines change together:
     - 34:14 becomes "and the goat-demon shall cry to its fellow".
     - The stable 13:21 becomes "and goat-demons will dance there", with a version bump for chapter 13.
   - The entry's wohChoice item for 13:21 would also change. That is a wohChoice modification, so it needs a major bump.
   - The 34:14 note points to the staged alternative.

Items for the founder:
- *lîlîṯ*: "the night-monster" (current) or "the lilith" (staged).
- *śāʿîr* at 34:14 and 13:21: "wild goat(s)" (current) or "goat-demon(s)" (staged).

The other escalations above (the skies/heavens register at 34:4–5, *qippōḏ*, and MT "my mouth") were approved by the Reviewer and need no ruling.
