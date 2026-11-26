# Chapter 21 Editor Report

Isaiah 21 (17 verses), wave I-4 (Isa 16–23).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v3.0.0 and isaiah-woh overlay v2.0.0, both read-only.
`wave-i4-rulings.md` is binding, including ruling 14, added during drafting.
All glossary changes are in `wave-i4-ch21-overlay-diff.json` and `wave-i4-ch21-central-diff.json`.

## Summary

- **Editorial questions:** all 30 resolved, none left open. `editorial_questions[]` is empty.
- **Commentary:** all 17 verses have `notes.official`. Every verse has a crux or a ruled decision.
- **English-line changes:** seven verses, each backed by a glossary entry.
  - 21:2: "A grievous vision" becomes "A harsh vision" (`lexical-cruxes-isaiah-21`).
  - 21:3: "I am pained" becomes "I am bowed down" (same entry).
  - 21:4: "My heart flutters" becomes "My heart reels" (same entry).
  - 21:6: "station the watchman" becomes "station the lookout" (`watch-lookout-vocabulary-isaiah-21`).
  - 21:13: "In the forest in Arabia" becomes "In the thicket in Arabia" (`lexical-cruxes-isaiah-21`).
  - 21:14: "with their bread" becomes "with his bread" (same entry).
  - 21:16: "according to the years of a hireling" becomes "as the years of a hireling" (ruling 14; `shnei-sakhir-years-of-hireling-isaiah`).
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` are left at 3.0.0 and 2.0.0 for the orchestrator to set on merge. `i18n.he` is unchanged. No `translit` field was added or edited.
- **Lens audit:** no English line carries a project reading. The Raëlian canon texts in data-library (*The Book Which Tells the Truth*, *Extraterrestrials Took Me to Their Planet*, *Let's Welcome the Extraterrestrials*) cite no verse of Isaiah 21. Their Isaiah citations are to chapters 6, 13, 14, 15, 26, 27, 29, 32, 40, 42–45, 48, 54 and 65. No Wheel of Heaven commentary paragraph was written, because nothing in the chapter calls for one.
- **References checked on 2026-11-26.**
  - NJPS ("Tanakh: The Holy Scriptures, published by JPS", 1985) and JPS 1917 on Sefaria, `/api/v3/texts/Isaiah.21?version=english|all`. The Gender-Sensitive Edition was not used.
  - ASV 1901 on bible-api.com.
  - LXX only through Brenton's 1851 English (biblehub). The Greek was not checked, and the commentary says so wherever LXX is cited.
  - Rev 14:8 and 18:2 (Greek) and Jer 51:8 from the corpus `revelation` and `jeremiah` files.
  - NRSV and the lexicons are cited from memory and marked "not verified" or "recalled".

## Speculative entries requiring sign-off

None. All four new overlay entries are `direct`, and the central ops only extend appliesTo.

---

## Unresolved editorial questions

None are blocked. These decisions are flagged for the Reviewer and the founder.

### `ISA-21:6` (and 21:5, 21:8, 21:11–12): lookout and watchman

**Issue:** two Hebrew nouns for the watcher: *mᵉṣappeh* (ṣph, 21:6) and *šōmēr* (šmr, 21:11–12). ASV and JPS 1917 call both "watchman".
**Decision:** they are kept distinct: "the lookout" (21:6) and "Watchman" (21:11–12, as ruled). The places use the standard words: *miṣpeh* "watchtower" and *mišmeret* "post" (21:8). The 21:5 hapax *ṣāp̄îṯ* stays "they set the watch" (ASV).
**Options considered:** "watchman" for both (ASV; the draft); "lookout" and "watchman"; "sentinel" and "watchman" (NRSV-type).
**Why flagged:** ruling 6 asks for a consistent watch vocabulary. The project values showing distinct Hebrew words, and NJPS ("sentry") and NRSV ("sentinel") also separate *mᵉṣappeh*. The decision is recorded either way. One cost: "watchtower" shares an English stem with "watchman" although the roots differ. Later sites with *ṣōp̄eh* (52:8; 56:10) and *šōmᵉrîm* (62:6) are not governed by this entry, and their Editors should keep or explicitly drop the distinction. To revert, the 21:6 line goes back to "watchman" and the entry's wohChoice is edited.

### `ISA-21:8`: "like a lion" and the 1QIsaᵃ variant

**Decision:** MT is kept: "And he cried out like a lion", with "like" supplied as in ASV, JPS 1917 and NJPS "[like]".
**Verification:** the 1QIsaᵃ attribution is **verified at second hand**. The NJPS note at 21:8 reads "1QIsa reads 'The watcher.'" It was not checked against the scroll or a DJD edition. The NRSV adoption ("the watcher called out") is not verified. The commentary uses exactly these terms.

### `ISA-21:14`: hêṯāyû, imperative or perfect

**Decision:** ASV's perfect "they brought" is kept. The following *qiddᵉmû* is pointed as a perfect, and the accents make the inhabitants of Tema its subject. The imperative of JPS 1917 ("bring ye water") and NJPS is in commentary.
**Why flagged:** two of the three references read an imperative. A Reviewer who prefers JPS 1917 would print "To meet the thirsty bring water!" and leave the second colon as it is.

### `ISA-21:16`: dependency on chapter 16

**Decision:** "as the years of a hireling" (ruling 14). The overlay op is a **modify** on `shnei-sakhir-years-of-hireling-isaiah`, which the chapter-16 Editor adds. The orchestrator must apply the chapter-16 add first. The current chapter-16 file reads "as the years of a hireling" at 16:14, so the two sites now match. (An earlier version of this report said 16:14 still read "like"; that was out of date, as the Reviewer noted.)
**Variant:** 1QIsaᵃ is reported to read "three years" here. This is not verified and is marked so in commentary.

### `ISA-21:2`: māḏay, "Media" against stable 13:17 "the Medes"

**Decision:** "O Media" (ASV, JPS 1917, NJPS). The two sites differ in syntax. At 13:17 the name is an object and governs plural verbs, so it is the people. At 21:2 it is a vocative beside the country name Elam. The rule is recorded in `oracle-names-isaiah-21` so that later sites follow it. Stable 13:17 is consistent with the rule and is not touched.

### `ISA-21:2`: bôḡēḏ concordance with stable 24:16

**Decision:** "the treacherous one deals treacherously". This is the same English family as 24:16 ("The treacherous have dealt treacherously"), in the present tense because the Hebrew has participles. The new entry `bgd-shdd-treachery-destroyer-isaiah` is written to be extended at 33:1. ISA-24:16 is not in its appliesTo because that chapter is out of scope. The orchestrator may add it with no change to the line. *šôḏēḏ* "the destroyer" matches the chapter-16 draft at 16:4.

---

## Decisions on the Translator's questions

1. **21:1 midbar-yām.** Ruled wording kept. The Sea-Land referent, the NJPS emendation note and the LXX minus are in commentary. → `oracle-names-isaiah-21`, `mt-qere-textual-policy-isaiah`.
2. **21:1 bannegeḇ.** "in the South" (ASV, JPS 1917), with NJPS "Negeb" in commentary. → names entry.
3. **21:2 qāšāh.** "harsh" (NJPS; BDB). This is a line change, and it also frees "grievous" for 21:15. → crux entry.
4. **21:2 bôḡēḏ.** The 24:16 family is kept (see above). → `bgd-shdd-treachery-destroyer-isaiah`.
5. **21:2 māḏay.** "O Media" (see above).
6. **21:2 ʾanḥāṯāh.** "All its sighing" (ASV). The suffix question and the NJPS emendation note are in commentary.
7. **21:3 privative min / ʿwh.** The privative reading is kept, since all three references are privative. ʿwh "bowed down" (JPS 1917 "bent") is a line change.
8. **21:4 tāʿāh.** "My heart reels" is a line change.
9. **21:4 śām.** Passive kept (ASV, JPS 1917). The active reading (NJPS "He") is in commentary. → central `va-yecherad-charadah-trembling-formula` extended.
10. **21:5 infinitives absolute.** Descriptive (ASV, JPS 1917). NJPS's quoted orders are in commentary.
11. **21:5 ṣāp̄îṯ.** "set the watch" (ASV; NJPS also takes the watch sense). JPS 1917 "lamps" and the "rugs" reading of the lexicons and NRSV (recalled, not verified) are in commentary. The draft's claim that NJPS reads "rugs" was **corrected**: NJPS reads "Let the watchman watch!".
12. **21:6 watchman vocabulary.** "lookout" / "watchman" (see above).
13. **21:7 reḵeḇ.** "a troop" (ASV, JPS 1917).
14. **21:7 ṣemeḏ pārāšîm.** "horsemen in pairs".
15. **21:7 hiqšîḇ.** "he shall listen" (future, with all three references).
16. **21:8 ʾaryēh.** MT kept. The 1QIsaᵃ reading is verified through the NJPS note (see above).
17. **21:8 ʾăḏōnāy.** "O Lord" (MT pointing). NJPS's construct reading and its note "my lord" are in commentary. → `adonai-standalone-title-isaiah`.
18. **21:8 kol-hallêlôṯ / mišmartî.** "whole nights" (ASV) and "my post".
19. **21:9 reḵeḇ ʾîš.** "a troop of men", settled by ruling 13. `adam-humankind-ish-man-isaiah` is deliberately not applied.
20. **21:9 šibbar.** Passive kept. The active and intransitive readings are in commentary.
21. **21:9 Rev 14:8, 18:2 and Jer 51:8.** In commentary, with Greek quoted from the corpus Revelation. → central `pesel-…` and overlay `elohim-el-eloah-…` extended ("her gods").
22. **21:10 mᵉḏušāṯî.** ASV kept. The NJPS note "Connection of Heb. uncertain" is in commentary.
23. **21:11 Dumah.** Ruled. The NJPS note (Gen 25:14), LXX "Idumea" (Brenton) and the *dûmāh* "silence" play are in commentary.
24. **21:12 šuḇû ʾēṯāyû.** "turn back, come". The Aramaic forms and NJPS "Come back again" are in commentary.
25. **21:13 maśśāʾ baʿrāḇ.** "The oracle concerning Arabia". The bᵉ- form, the NJPS "steppe" reading and LXX "evening" are in commentary. → `massa-oracle-superscription-isaiah` extended with a note.
26. **21:13 yaʿar.** "thicket" is a line change. "Forest" stays elsewhere.
27. **21:14 hêṯāyû / bᵉlaḥmô.** Perfect kept. "his bread" is a line change (see above).
28. **21:15 kōḇeḏ.** "grievousness" (ASV, JPS 1917). There is no stem clash now that 21:2 has "harsh". The kāḇôḏ concordance does not reach kōḇeḏ.
29. **21:16 śāḵîr.** Ruling 14 (see above). kāḇôḏ is strictly "glory".
30. **21:17 gibbôrê.** "the mighty men", settled by ruling 13, as at 13:3.

---

## Glossary changes for review

### Central glossary (proposed 3.0.0 → 3.1.0; `wave-i4-ch21-central-diff.json`)

- Modified: `eretz`, appliesTo += ISA-21:1, ISA-21:14 ("land"). `lā-ʾāreṣ` at 21:9 is deliberately not added.
- Modified: `pesel-utemunah-graven-image-iconographic-prohibition-cross-corpus`, appliesTo += ISA-21:9.
- Modified: `va-yecherad-charadah-trembling-formula`, appliesTo += ISA-21:4. Its rationale already names Isa 21:4. The Gen 27:33 wording is not imported.

### Per-translation overlay (proposed 2.0.0 → 2.1.0; `wave-i4-ch21-overlay-diff.json`)

- Added: `watch-lookout-vocabulary-isaiah-21` (claim_type: `direct`)
- Added: `bgd-shdd-treachery-destroyer-isaiah` (claim_type: `direct`)
- Added: `oracle-names-isaiah-21` (claim_type: `direct`)
- Added: `lexical-cruxes-isaiah-21` (claim_type: `direct`)
- Modified (appliesTo, plus a rationale sentence):
  - `massa-oracle-superscription-isaiah` (21:1, 11, 13)
  - `title-and-meta-conventions-isaiah` (21:1, 10, 17)
  - `adonai-standalone-title-isaiah` (21:6, 8, 16)
  - `yhwh-tzevaot-hosts-isaiah` (21:10)
  - `elohei-yisrael-god-of-israel-isaiah-24` (21:10, 17)
  - `elohim-el-eloah-monotheistic-formula-isaiah` (21:9)
  - `mt-qere-textual-policy-isaiah` (21:1, 2, 5, 8, 16; the orchestrator updates the wohChoice variant list on merge)
  - `shnei-sakhir-years-of-hireling-isaiah` (21:16; pending add by chapter 16)
- Deliberate non-application: `adam-humankind-ish-man-isaiah` at 21:9 and 21:17 (ruling 13).

Strong's numbers in the new entries come from memory and are marked as not checked against a concordance.

---

## Post-review corrections

The Reviewer's verdicts (`translation.reviewerReport`, 2026-11-26T15:12:28Z) were applied as listed below. Only the commentary, this report and the Editor's own overlay diff were changed. No English line, `translation.status` (still `awaiting-human`), the `reviewerReport` block or any shared glossary was touched.

1. **21:1 (revise).** The Sea-Land attribution to Wildberger and Blenkinsopp is now marked "recalled, not verified" in the 21:1 note and in the `oracle-names-isaiah-21` rationale.
2. **21:8 (revise).** The 21:8 note and the `mt-qere-textual-policy-isaiah` rationaleAppend now say that NJPS gives only the English "The watcher". The Hebrew *hārōʾeh* is marked as the Editor's reconstruction, and the scroll was not checked. The orchestrator instruction for the wohChoice variant list now reads "21:8 the watcher" in place of "hārōʾeh".
3. **21:14 (revise).** The 21:14 note and the `lexical-cruxes-isaiah-21` rationale now cite Jer 12:9. There the identical form *hêṯāyû* follows the imperatives *lᵉḵû ʾispû* and is itself an imperative. The Reviewer checked it in WLC, and the Editor re-checked it on Sefaria. This is the strongest support for the command reading. The entry's wohChoice stages the alternative line, marked **PENDING FOUNDER RULING**: "To meet the thirsty bring water! The inhabitants of the land of Tema met the fugitive with his bread." The printed line keeps ASV's "they brought" until the founder rules.
4. **21:9 (non-blocking suggestion, applied).** "taken up word for word" is now "taken up in Rev 14:8 and 18:2, which keep the doubled verb and add 'the great'". The unsourced "the dirge form" is dropped; the sentence now reads "The doubled perfect speaks of the fall as already complete."
5. **21:16.** The report's statement that 16:14 still read "like" is corrected above: 16:14 now reads "as the years of a hireling".

Not acted on, because it is not a correction: the Reviewer recalls NRSV 21:6 as "post a lookout" rather than the "sentinel" listed in `watch-lookout-vocabulary-isaiah-21` standardEnglish. Neither form is verified, and the field is left as it was until someone checks NRSV.

Items for the human: the lookout/watchman split (21:6); the perfect or imperative at 21:14, with the staged line above; and the 1QIsaᵃ reading at 21:8, still confirmed only through the NJPS note.
