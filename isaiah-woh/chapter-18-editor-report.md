# Chapter 18 Editor Report

Isaiah 18 (7 verses), wave I-4 (Isa 16–23).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v3.0.0 and isaiah-woh overlay v2.0.0, both read-only.
`wave-i4-rulings.md` (rules 1–13) is in force.
All glossary changes are in `wave-i4-ch18-overlay-diff.json` and `wave-i4-ch18-central-diff.json`.

## Summary

- **Editorial questions:** all 14 resolved; `editorial_questions[]` is empty. Two items are escalated below: the 27:13 shofar harmonization and the 18:1 reception note.
- **English-line changes:** one verse. At 18:3 "when a trumpet is blown" is now "when a shofar is blown", under central `shofar-rams-horn-signal-instrument-cross-corpus`. Every other line is the Translator's.
- **Commentary:** all 7 verses have `notes.official`. 18:1 ends with a separately headed reception note labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` (3.0.0) and `overlayGlossaryVersion` (2.0.0) are left for the orchestrator to set on merge.
  - The `glossaryRefs` to `cush-names-isaiah`, `tziltzal-kenafayim-whirring-wings-isaiah-18`, `qav-qav-line-isaiah` and `lexical-cruxes-isaiah-18` point to entries that exist only in the overlay diff.
  - No `translit` field was touched.
- **Verification (2026-11-26):**
  - JPS 1917, NJPS (Tanakh, JPS 1985, not the gender-sensitive edition) and Koren for Isa 18 were checked on Sefaria API v3, footnotes included. So were NJPS and JPS 1917 for 11:11, 20:3–5, 28:10, 43:3, 45:14, Gen 10:6 and Zeph 3:10.
  - ASV (1901) and KJV for Isa 18, ASV for Isa 28:10, 13, Deut 28:26, Jer 7:33, Zeph 3:10 and 20:3, and KJV for 26:19 were checked on bible-api.com.
  - The LXX for Isa 18 and 28:10, 13 was checked on getbible.net ("LXX Accented").
  - These BDB articles were checked through Sefaria's lexicon: *ṣilṣāl*, *kānāp̄* (sense on Isa 18:1), *qaw* / *qawqāw*, *māšaḵ* (Pual), *bāzāʾ*, *ṣîr*, *gōmeʾ*, *šay*, *ḥārap̄* II and *ṭal*. Klein was checked for *mrṭ* and *zalzal*.
  - Not verified: NRSV, 1QIsaᵃ, HALOT. Strong's numbers are from recall and are marked so in the entries. Herodotus 3.20 is cited as the commonly adduced parallel and was not checked against an edition.
- **Canon check:** the Raëlian canon books in data-library were searched: `the-book-which-tells-the-truth`, `extraterrestrials-took-me-to-their-planet` and `lets-welcome-the-extraterrestrials`. **None cites Isa 18.** The only canon reading of wings in Isaiah is TBWTT 3:144–145, on Isa 6:2.
- **Lens audit:** no English line carries a project reading. 18:1 names no referent for the wings, and the 18:7 "gift" line is literal MT.

## Speculative entries requiring sign-off

No speculative glossary entry is proposed. One commentary item is labelled speculative.

### ISA-18:1 reception note (commentary, not a glossary entry)

**Source:** הוֹי אֶרֶץ צִלְצַל כְּנָפָיִם
**WoH reading (commentary only):** The note says three things. The canon does not cite Isa 18. TBWTT 3:144–145 reads the seraphim's wings of Isa 6:2 as "an autonomous suit fitted with six small thrusters". Reading the "whirring of wings" of 18:1 as flying craft would extend that reading to a verse the canon does not discuss. The note also states the counter-evidence: BDB connects *ṣilṣal* with insects, and the envoys of 18:2 travel in papyrus boats.
**Why speculative:** it applies a canon reading of a different verse to one the canon does not cite. That goes beyond any single source.
**Recommendation:** ship as worded. This follows the 4:5, 7:14, 9:5 and 11:12 precedent (ruling 9). If the founder prefers silence at verses the canon does not cite, delete the final paragraph of the 18:1 note. Nothing else depends on it.

---

## Unresolved editorial questions

### `ISA-27:13` (stable) against `ISA-18:3`: "trumpet" or "shofar"

**Issue:** central `shofar-rams-horn-signal-instrument-cross-corpus` transliterates *šôp̄ār* as "shofar" in every context and reserves "trumpet" for *ḥăṣōṣᵉrāh*. The corpus follows it everywhere I checked: Exodus, Leviticus, Joshua, Judges, 2 Samuel, 1 Kings, Zeph 1:16 and Zech 9:14. The one exception is the signed-off Isa 27:13 "a great trumpet", which is governed by the verse-scoped overlay `shofar-gadol-ingathering-isaiah-27`. 18:3 now follows the central entry, so the book has both forms.
**Options considered:**
- A. Keep 18:3 "shofar" and revise 27:13 to "a great shofar" at its next stable revision. This is the recommendation.
- B. Revert 18:3 to "a trumpet" and record an Isaiah exception in the central entry.
- C. Accept the split.
**Why escalating:** option A touches a signed-off chapter, and option B would carve an exception into a cross-corpus convention. Both need the founder.

---

## Decisions on the Translator's questions

1. **18:1 *ṣilṣal kᵉnāp̄āyim*.** ASV "the land of the rustling of wings" is kept, and no referent is named. The four readings (insects, army, shadow, sails) are given in commentary with their sources: BDB, KJV, NJPS and the LXX, all verified. The reception note is labelled speculative. → new overlay `tziltzal-kenafayim-whirring-wings-isaiah-18` (direct).
2. **18:1 Kûš.** "Cush" per ruling 12. → new overlay `cush-names-isaiah` (direct), with appliesTo 11:11, 18:1, 20:3, 20:4, 20:5, 43:3 and 45:14. The entry also records:
   - the ASV split ("Cush" at 11:11, "Ethiopia" elsewhere);
   - NJPS "Nubia" in Isaiah but "Cush" at Gen 10:6;
   - the Torah "Kush" convention.

   "beyond the rivers of Cush" is kept, with the Zeph 3:10 parallel.
3. **18:2 envoys / sea / papyrus.** The draft is kept, and the Nile reading of *yām* is noted. → `lexical-cruxes-isaiah-18`.
4. **18:2 the unintroduced imperative.** No "[saying]" is supplied. The NJPS reordering and its agreement note are reported. → `lexical-cruxes-isaiah-18`, `title-and-meta-conventions-isaiah`.
5. **18:2 *mᵉmuššāḵ ûmôrāṭ*.** "tall and smooth" (ASV) is kept. BDB gives "tall"; the JPS 1917, KJV, NJPS and LXX readings are reported. → `lexical-cruxes-isaiah-18`.
6. **18:2 *nôrāʾ min-hûʾ wāhālᵊʾāh*.** "feared from their beginning onward" is kept. → `lexical-cruxes-isaiah-18`. Note for the orchestrator: the chapter 21 draft has "a terrible land" for *nôrāʾāh* (21:1). Harmonize if wanted; I did not touch chapter 21.
7. **18:2 *qaw-qāw ûmᵉḇûsāh*.** The ASV "line" reading is kept: "measures out and treads down". → new overlay `qav-qav-line-isaiah` (**inferred**, because BDB reports the "mighty" reading as the majority view). The entry fixes the link to 28:10, 13. The default there is "line upon line" (ASV). If the chapter 28 Editor departs from it, that Editor must revisit 18:2, 7 or escalate. The LXX "hope" derivation at both sites is recorded.
8. **18:2 *bāzᵉʾû*.** "whose land the rivers divide" (BDB "divide, cut through"). → `lexical-cruxes-isaiah-18`.
9. **18:3 *šôp̄ār* and the verbs.** The line is changed to "a shofar" under the central entry, which is extended (see the escalation above). No book-level shofar entry is created, since the central entry already governs. Imperatives are kept. → `nes-signal-isaiah`, `eretz-cosmic-scope-isaiah-24`, `lexical-cruxes-isaiah-18`.
10. **18:4 ketiv/qere.** The qere is read. → `mt-qere-textual-policy-isaiah` + ISA-18:4.
11. **18:4 images.** ASV is kept throughout. The NJPS and KJV readings are reported. The LXX "day of harvest" (*bᵉyôm*) is now **verified** for the LXX; 1QIsaᵃ is still not verified. → `lexical-cruxes-isaiah-18`, `mt-qere-textual-policy-isaiah`.
12. **18:5 viticulture.** MT "harvest" and the asyndeton are kept, and the subject is left unnamed. → `lexical-cruxes-isaiah-18`.
13. **18:6 *bᵉhemaṯ hāʾāreṣ* and *ʿêṭ*.** "the beasts of the earth" is kept, because this is the carrion curse formula (Deut 28:26; Jer 7:33; corpus 1 Sam 17:46). → central `eretz`: a new **carrion-formula context clause** is proposed, excluding Gen 1 and Gen 9. "ravenous birds" is kept.
14. **18:7 MT without "from".** MT is kept. The LXX ἐκ λαοῦ is now verified; 1QIsaᵃ is not. "a gift" is kept. → `mt-qere-textual-policy-isaiah` + ISA-18:7, `lexical-cruxes-isaiah-18`, `qav-qav-line-isaiah`, `yhwh-tzevaot-hosts-isaiah`.

### Corrections to the Translator's attributions

- NRSV "mighty and conquering" was given as recalled. The verified attribution is **Koren**, which does print it.
- The LXX "wings of ships" was given as not verified. It is verified: γῆς πλοίων πτέρυγες.

### Items for the Reviewer's attention (not escalations)

- **18:7 apposition.** "a gift shall be brought … a people tall and smooth" is literal MT, but it reads awkwardly. Every English version supplies "from".
- **`qav-qav-line-isaiah` as inferred.** The Reviewer may judge that keeping the PD baseline makes the entry direct. I chose inferred because the lexicon calls the alternative the majority view.
- **18:3 line change.** This is the only change to the Translator's English.

## Glossary changes for review

### Central glossary (`wave-i4-ch18-central-diff.json`, 3.0.0 → proposed 3.1.0)

- Modified: `eretz` (claim_type unchanged, `inferred`).
  - appliesTo + ISA-18:1, 18:2, 18:6, 18:7.
  - A carrion-formula context clause is appended to wohChoice. The existing text is unchanged, and the clause is also given as `wohChoiceAppend` for a safe merge.
  - If this counts as a modification, bump to 4.0.0 instead.
- Modified: `shofar-rams-horn-signal-instrument-cross-corpus` (appliesTo + ISA-18:3; rationale addendum).

### Per-translation overlay (`wave-i4-ch18-overlay-diff.json`, 2.0.0 → proposed 2.1.0)

- Added: `cush-names-isaiah` (claim_type: `direct`). This is the book-level names entry that the chapter 20 Editor cites.
- Added: `tziltzal-kenafayim-whirring-wings-isaiah-18` (claim_type: `direct`)
- Added: `qav-qav-line-isaiah` (claim_type: `inferred`)
- Added: `lexical-cruxes-isaiah-18` (claim_type: `direct`)
- Modified (appliesTo, with addenda): `hoy-woe-isaiah`, `nes-signal-isaiah`, `mt-qere-textual-policy-isaiah`, `eretz-cosmic-scope-isaiah-24`, `title-and-meta-conventions-isaiah`, `yhwh-tzevaot-hosts-isaiah`.
- Modified (cross-reference addendum only, no scope change): `shofar-gadol-ingathering-isaiah-27`.

## Post-review corrections

These were applied after the Reviewer's report (2026-11-26). Out of scope and not changed: `translation.status` (still `awaiting-human`), the `reviewerReport` block, every English line and the shared glossaries.

1. **ISA-18:1 commentary (Reviewer verdict: revise, commentary only).** One sentence has been added to the speculative reception paragraph. It names the closest canon parallel outside Isaiah, LWTE 2:187–190. That passage quotes the locusts of Rev 9:7–10 ("the sound of their wings was as the sound of chariots") and reads them as metal aircraft: "the noise comes from the jet engines", with missiles "tucked under their wings". I checked the wording against `data-library/lets-welcome-the-extraterrestrials/chapter-2.json`. The sentence also says that the passage concerns human aircraft dropping atomic bombs in a future war (LWTE 2:184) and does not concern Isa 18. The finding that the canon does not cite Isa 18 still stands.
2. **`cush-names-isaiah` (overlay diff).** Isa 37:9, "Tirhakah king of Cush" (= 2 Kgs 19:9), is now named in wohChoice as an expected site. ISA-37:9 is to be added to appliesTo once chapter 37 is drafted. appliesTo itself is unchanged.
