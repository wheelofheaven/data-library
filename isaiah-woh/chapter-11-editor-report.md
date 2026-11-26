# Chapter 11 Editor Report

Isaiah 11 (16 verses), wave I-3 (Isa 7–12).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v2.93.0 and isaiah-woh overlay v1.6.1, both read-only. Wave I-1 diffs and rulings and `wave-i3-rulings.md` are treated as in force. All glossary changes are in `wave-i3-ch11-overlay-diff.json` and `wave-i3-ch11-central-diff.json`.

## Summary

- **Editorial questions:** all 14 resolved. Two are also escalated: the book-level nēṣer question and the 11:12 reception note. `editorial_questions[]` is empty.
- **English-line changes:** one verse, 11:15. "will utterly destroy" is now "will devote to destruction", under central `cherem-devote-to-destruction-cross-corpus`, which is extended. Every other line is the Translator's.
- **Commentary:** all 16 verses have `notes.official`. 11:12 also has a separately headed reception note labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` and `overlayGlossaryVersion` are left at 2.93.0 and 1.6.1. The orchestrator sets them on merge.
  - The `glossaryRefs` for 11:1, 11:2, 11:3, 11:6, 11:8, 11:10, 11:11, 11:12, 11:13, 11:14 and 11:15 point to overlay entries that exist only in the diff.
- **Verification:**
  - ASV, JPS 1917 and NJPS for Isa 11 were checked against the texts. ASV came from getbible.net; JPS 1917 and NJPS, with their footnotes, came from Sefaria.
  - NRSV readings are marked "not verified" where cited.
  - The LXX and Vulgate wording at 11:1 and 11:2 is from memory. It is standard and stated with confidence, but it was not checked this session.
  - The proposed emendation *lišʾēṯ* at 11:11 is marked not verified.
  - Strong's numbers in the new entries are from model recall and are marked as such.
  - TBWTT 5:25 was checked in `data-library/the-book-which-tells-the-truth/chapter-5.json`.
- **Lens audit:**
  - No English line carries a project reading.
  - The lower case stays at 11:1 ("a shoot", "a twig") and 11:10 ("the root of Jesse").
  - The peaceable-creatures verses (11:6–9) are rendered plainly.

## Speculative entries requiring sign-off

No speculative glossary entry is proposed. One commentary item is labelled speculative.

### ISA-11:12 reception note (commentary, not a glossary entry)

**Source:** וְנָשָׂא נֵס לַגּוֹיִם וְאָסַף נִדְחֵי יִשְׂרָאֵל וּנְפֻצוֹת יְהוּדָה יְקַבֵּץ מֵאַרְבַּע כַּנְפוֹת הָאָרֶץ
**WoH reading (commentary only):** *The Book Which Tells the Truth* (TBWTT 5:25) reads the ingathering of Isa 43:5–7 as the creation of the State of Israel. The note says that reading the second gathering of 11:11–12 the same way is a project extension.
**Why speculative:** the canon does not cite Isa 11. The extension goes beyond what any single source states.
**Recommendation:** ship as worded. This follows the 4:5 precedent from wave I-1. If the founder prefers silence at verses the canon does not cite, drop the final paragraph of the 11:12 note. Nothing else depends on it.

---

## Unresolved editorial questions

### `ISA-11:1` / book level: one English word for nēṣer

**Issue:** nēṣer occurs at 11:1, 14:19 and 60:21 (and Dan 11:7).
- The line at 11:1 now has "a twig", with JPS 1917 and NJPS. This keeps "branch" for ṣemaḥ (4:2) as the book's title-word.
- The stable 14:19 has "a loathed branch", from ASV "an abominable branch".
- 14:19 cannot be changed in this wave.

**Options considered:**
- A. Accept two renderings by context, and record the split in the entry. Under this option 14:19 stays outside `appliesTo`.
- B. Revise 14:19 at its next stable revision to "a loathed twig" or "a loathed shoot", and add it to `choter-netser-geza-shoot-twig-stock-isaiah-11`. This needs a ch. 14 Editor pass and a version bump.
- C. Use "branch" at 11:1 as well. This matches ASV and 14:19 but loses the visible ṣemaḥ / nēṣer distinction.

**Recommendation:** B. 14:19 is a simile, a cast-off growth, and "twig" serves there too. Until then, A is the de facto state. 60:21 should be decided by the same ruling.

**Why escalating:** the decision touches a signed-off chapter.

---

## Decisions on the Translator's questions

1. **ISA-11:1, ḥōṭer / nēṣer / gezaʿ.** Decided on the merits:
   - "a shoot … a twig": nēṣer "twig" follows JPS 1917 and NJPS.
   - gezaʿ "stock" follows ASV and JPS 1917 and the stable 40:24. NJPS "stump" is recorded, and "stump" stays with maṣṣeḇeṯ (6:13).
   - The messianic reception (Targum; Matt 2:23) is in commentary only.
   - → new overlay `choter-netser-geza-shoot-twig-stock-isaiah-11`. The book-level question is escalated above.
2. **ISA-11:1, yip̄reh.** MT "shall bear fruit" is kept. The LXX and Vulgate "come up" and NJPS "sprout" are in the commentary. → `mt-qere-textual-policy-isaiah` extended.
3. **ISA-11:2, the rûaḥ list.**
   - The line gives MT's six qualities, with ASV wording and lower-case "spirit" for all four occurrences.
   - The LXX *eusebeia* and the seven-gifts tradition are in the commentary.
   - → `ruach-divine-spirit-lower-case-isaiah` extended to 11:2. Its rationale now records that 11:4 ("breath of his lips", the king's breath) and 11:15 ("his scorching wind") lie outside the entry and take the standard English. No wind clause is added, since that would change the wohChoice and need a major bump.
   - ʿēṣāh "counsel" and gᵉḇûrāh "might" → `lexical-cruxes-isaiah-11`.
4. **ISA-11:3, hărîḥô.**
   - The line keeps "his delight shall be in the fear of YHWH" (ASV, JPS 1917).
   - The commentary gives the literal "his smelling" and NJPS "sense the truth", with NJPS's note that the meaning is uncertain.
   - The deletion as dittography is reported and not adopted. → `lexical-cruxes-isaiah-11`.
5. **ISA-11:4, ʾereṣ ×2.**
   - "the earth" both times (ASV) is kept, because the oracle widens to the nations in vv 9–10.
   - JPS 1917 and NJPS have "land", which is recorded as a defensible alternative.
   - The emendation ʿārîṣ is reported (NJPS note) and MT kept.
   - "breath" is outside the spirit entry.
   - → `eretz-cosmic-scope-isaiah-24` and `mt-qere-textual-policy-isaiah` extended.
6. **ISA-11:6, verbless clause and gār.**
   - The MT verbless clause and "dwell" are kept.
   - The 1QIsaᵃ/LXX "shall feed" is reported from the NJPS note.
   - → `mt-qere-textual-policy-isaiah` and `lexical-cruxes-isaiah-11`.
7. **ISA-11:8, hapaxes.** The ASV words are kept: "hole of the asp", "adder's den", "put his hand". NJPS "viper" and its "meaning uncertain" note are given. → `lexical-cruxes-isaiah-11`.
8. **ISA-11:9, paradise-by-negation.** The entry is applied at 11:9 only, since only that verse has the negations; 11:6–8 are linked in commentary. "the earth" is kept, and NJPS "land" is noted. → central `paradise-by-negation-…` and overlay `eretz-cosmic-scope-isaiah-24` extended.
9. **ISA-11:10, mᵉnuḥāṯô kāḇôḏ, nēs and drš.**
   - "his resting place shall be glory" is kept under wave ruling 6. This departs from ASV "glorious" and is recorded in the diff and in the commentary.
   - nēs "signal" is checked against 5:26 (wave I-1, "raise a signal for the nations") and the stable 13:2 ("raise a signal"). All agree, and there was no entry, so the new overlay `nes-signal-isaiah` records the book practice. Its `appliesTo` includes ISA-5:26 and ISA-13:2; the glossaryRefs of those chapters are left to the orchestrator.
   - "seek" is kept, and central `darash-yhwh-seeking-oracle` is not applied.
10. **ISA-11:11, the ingathering list.**
    - Supplied "set" (ASV) and "to recover" are kept.
    - The place names keep the ASV forms (wave I-3 ruling 4), with "coastlands of the sea" as at 24:15.
    - "Shinar" is the bare name: central `eretz-shinar` is extended, with a sentence on the conditional form.
    - `adonai-standalone-title-isaiah` is extended.
    - Central `she-erit-…` is not applied to šᵉʾār at 11:11 and 11:16.
11. **ISA-11:12, four corners.** "the four corners of the earth" is kept. The 1 Enoch central entry is not applied. → `nes-signal-isaiah` and `eretz-cosmic-scope-isaiah-24`. The reception note is escalated above.
12. **ISA-11:13, ṣōrᵉrê yᵉhûḏāh.** The ASV construal is kept, with "harass" for both forms. The subjective reading (NJPS) is reported. → `lexical-cruxes-isaiah-11`.
13. **ISA-11:14, ʿwp, kāṯēp̄ and the nominal clauses.** "swoop down", "shoulder" and the ASV verbal rendering are kept. The slope sense (Josh 15:8–11) and NJPS are reported. → `lexical-cruxes-isaiah-11`.
14. **ISA-11:15, three sites.**
    - (a) MT ḥrm is kept, and the line now reads "devote to destruction", following the corpus rule that the ḥērem root stays visible. NJPS "dry up" and the emendation are in the commentary.
    - (b) "with his scorching wind" is kept.
    - (c) "cause men to march over dryshod" is kept, and the commentary says that "men" is supplied.
    - The central Exodus 14 parting entry is not applied.
    - → central `cherem-…` extended, plus `mt-qere-textual-policy-isaiah` and `lexical-cruxes-isaiah-11`.

### Items for the Reviewer's attention (not escalations)

- **11:15 line change.** "devote to destruction the tongue of the sea" is literal MT but reads oddly in English. The oddness is the same reason NJPS emends. If the Reviewer judges the corpus ḥērem rule inappropriate for a non-personal object, the alternative is to restore ASV "utterly destroy" and drop the central extension.
- **11:4 "earth" vs "land".** The JPS tradition reads territorially. The line follows ASV.
- **11:15 "men".** This is a supplied gendered generic. If the wave I-1 ruling on ʾāḏām/ʾîš (C1, gender-neutral) is ratified, "people" may be preferred. That is a wording choice with no Hebrew word behind it.

## Glossary changes for review

### Central glossary (`wave-i3-ch11-central-diff.json`, 2.93.0 → proposed 2.95.0)

- Modified: `paradise-by-negation-no-predation-no-illness-no-aging-cross-corpus` (appliesTo + ISA-11:9; rationale sentence)
- Modified: `eretz-shinar` (appliesTo + ISA-11:11; conditional bare-name sentence)
- Modified: `cherem-devote-to-destruction-cross-corpus` (appliesTo + ISA-11:15; rationale sentence)
- Modified: `eretz` (appliesTo + ISA-11:16)
- Note op: deliberate non-extensions (`she-erit-…`, `four-corners-…`, `keriat-yam-suf-…`, `darash-yhwh-seeking-oracle`, `mitsrayim`, `kavod-yhwh`)

### Per-translation overlay (`wave-i3-ch11-overlay-diff.json`, 1.6.1 → proposed 1.8.0)

- Added: `choter-netser-geza-shoot-twig-stock-isaiah-11` (claim_type: `direct`)
- Added: `nes-signal-isaiah` (claim_type: `direct`; covers 5:26, 11:10, 11:12, 13:2)
- Added: `lexical-cruxes-isaiah-11` (claim_type: `direct`)
- Modified (appliesTo + rationaleAppend only):
  - `title-and-meta-conventions-isaiah` (11:1)
  - `ruach-divine-spirit-lower-case-isaiah` (11:2)
  - `eretz-cosmic-scope-isaiah-24` (11:4, 11:9, 11:12)
  - `mt-qere-textual-policy-isaiah` (11:1, 11:4, 11:6, 11:11, 11:15)
  - `adonai-standalone-title-isaiah` (11:11)

### Coordination for the orchestrator

- If the chapter 7 or 10 Editor creates a šᵉʾār ("remnant") entry for 7:3 / 10:20–22, ISA-11:11 and ISA-11:16 can be added to it at merge.
- The chapter 9 Editor's 9:5 rendering of *yôʿēṣ* is referred to by root only in the 11:2 note. If 9:5 departs from "Counselor", the note needs no change.

## Post-review corrections (2026-11-26)

The Reviewer returned the chapter as `awaiting-human`. 15 verses were approved, and 11:15 was flagged for the human. In the glossary review, 2 entries came back as revise and 2 as flag-for-human.

Only the non-decision corrections are applied here. `translation.status`, the `reviewerReport` block, every English line (11:15 included) and both shared glossaries are unchanged.

1. **`nes-signal-isaiah` (overlay diff, add op), from Reviewer revise.**
   - The wohChoice now limits "signal" to nēs as a raised pole or banner. It lists the later banner sites (18:3; 30:17; 31:9; 49:22; 62:10).
   - It also excepts 33:23, where nēs is a ship's sail, as at Ezek 27:7, and is rendered "sail".
   - One rationale sentence records the nautical sense (BDB).
   - The 11:10 commentary now reads "wherever it is a raised pole or banner … at 33:23 it is a ship's sail", replacing "throughout the book".
2. **`lexical-cruxes-isaiah-11` (overlay diff, add op), from Reviewer revise.** The rationale wrongly said only one item departs from ASV. It now names three departures, each with its reason:
   - (a) 11:10: the noun "glory" is kept for kāḇôḏ, under ruling 6 and the 6:3 / 24:23 precedent.
   - (b) 11:11: "the coastlands of the sea" replaces ASV "islands", for concordance with the stable 24:15 and 42:4.
   - (c) 11:14: "swoop down" replaces ASV "fly down", as the raptor's descent (NJPS "pounce").
3. **Central diff, `eretz-shinar`, from the Reviewer's suggestion.**
   - The bare-name clause is now in the wohChoice via `changes`: "the land of Shinar" where ʾereṣ šinʿār stands, and bare "Shinar" where the name has no ʾereṣ (Gen 14:1, 9; Isa 11:11).
   - No existing rendering changes.
   - Strictly, this is a wohChoice modification and so a major bump. The Editor recommends treating it as minor, at the orchestrator's call.
4. **Central diff, `cherem-devote-to-destruction-cross-corpus`, follows from the Reviewer's flag.**
   - A `pendingFounderRuling` block, marked "PENDING FOUNDER RULING — do not apply unless ratified", stages the complete proposed wohChoice. It is the current text plus a non-war-object clause for 11:15, and can be applied verbatim if ratified.
   - The same block gives the rejection path: remove ISA-11:15 from appliesTo, drop the rationaleAppend, and restore ASV/JPS 1917 "utterly destroy" in the 11:15 line and note.
   - The current appliesTo extension and the 11:15 line are left as drafted, pending the founder.
5. **Version notes.** Both diffs' version ops record the post-review changes. Overlay stays at 1.8.0, minor, because both amended entries are new in this diff. Central stays at 2.95.0. The bump effect of the two central wohChoice changes is stated for the orchestrator.

**Still open for the founder:**
- The nēṣer split with 14:19 (Reviewer concurs with option B).
- The 11:15 ḥērem scope (Reviewer recommends ratifying the non-war clause; the fallback is "utterly destroy").
- The 11:12 speculative reception note.
- An optional wording point, raised by the Reviewer: "cause people to march over dryshod" for the supplied "men" at 11:15.
