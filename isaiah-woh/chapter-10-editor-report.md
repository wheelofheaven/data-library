# Chapter 10 Editor Report

Isaiah 10 (34 verses), wave I-3 (Isa 7–12).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v2.93.0 and isaiah-woh overlay v1.6.1, both read-only.
The wave I-1 diffs and `wave-i3-rulings.md` are treated as in force.
All glossary changes are in `wave-i3-ch10-overlay-diff.json` and `wave-i3-ch10-central-diff.json`.

## Summary

- **Editorial questions:** all 32 resolved, 0 left open. `editorial_questions[]` is empty. Items that need human judgement are listed below.
- **Commentary:** 32 of 34 verses have `notes.official`. 10:7 and 10:8 have none, since they are standard.
- **English-line changes:** eight verses, each backed by a glossary entry.
  - 10:1: ʿāmāl "perverseness" becomes "mischief".
  - 10:4: the first half becomes "Nothing remains but to crouch under the prisoners, and they shall fall under the slain". The refrain is unchanged.
  - 10:6: "a profane nation" becomes "a godless nation" (ruling 5).
  - 10:11: ʿăṣabbêhā "her idols" becomes "her images".
  - 10:12: "the honor of his haughty looks" becomes "the boasting of his haughty looks", a recorded concordance departure under ruling 6.
  - 10:18: "as when a standard-bearer faints" becomes "as when a sick man wastes away".
  - 10:21: the line becomes "A remnant will return, the remnant of Jacob, to the Mighty God." (rulings 1 and 2).
  - 10:22: "shall return" becomes "will return", to match 10:21.
- **Glossary refs:** `ha-adon-definite-title-isaiah` is removed from 10:16 and 10:33 (ruling 7).
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
  - `glossaryVersion` and `overlayGlossaryVersion` are left at 2.93.0 and 1.6.1. The orchestrator sets them on merge.
- **Lens audit:** no English line carries a project reading. No Wheel of Heaven reading is added in commentary, because none was needed at any verse.
  - 10:5 keeps the instrument image plain.
  - 10:27 keeps MT "fatness" and does not use "anointing".
  - 10:28–32 names no army.

## Speculative entries requiring sign-off

None. Both new overlay entries and the new central entry are `direct`.

---

## Unresolved editorial questions (escalated for human judgement)

### `ISA-10:16`, `ISA-10:33`

**Issue:** hā-ʾāḏôn YHWH ṣᵉḇāʾôṯ. Following ruling 7, the line gives "the Sovereign, YHWH of hosts", which is option B of wave I-1 decision 1, and carries only `ha-adon-articular-title-isaiah`.
**Options considered:** A "the Lord, YHWH of hosts"; B "the Sovereign, YHWH of hosts"; "the Master".
**Why escalating:** the founder ruling was pending. Resolved 2026-11-26: option B, "the Sovereign", stands, and the reversion sentences were deleted.

### `ISA-10:18`

**Issue:** kimsōs nōsēs. The line now departs from ASV ("standard-bearer") and gives "as when a sick man wastes away". This follows the lexical derivation from nss "be sick", which NRSV also follows.
**Options considered:** ASV "standard-bearer faints"; "a sick man wastes away"; "an invalid wastes away".
**Why escalating:** this is an accuracy-driven departure from the corpus baseline at a hapax. The BDB citation in the commentary was not checked at the page. The Reviewer should confirm the derivation.

### `ISA-10:23` (and `ISA-10:14`)

**Issue:** kol-hāʾāreṣ. Both sites read "all the earth" under `eretz-cosmic-scope-isaiah-24`. At 10:23 a territorial reading, "the whole land" (the decree on Israel), is also current.
**Options considered:** earth at both sites; earth at 10:14 and land at 10:23; land at both sites.
**Why escalating:** the choice rests on how far the decree reaches, and the context does not settle it. 28:22, which uses the same formula, is not drafted yet, and the two sites should agree.

### `ISA-10:12`

**Issue:** tip̄ʾereṯ is rendered "boasting", departing from the wave default "honor" (ruling 6 names this verse as an allowed departure).
**Options considered:** "honor" (concordant); ASV "glory", which is ruled out because kāḇôḏ is strict; "pomp"; "boasting".
**Why escalating:** it is recorded for sign-off, as ruling 6 requires. "Boasting" also links the noun to yiṯpāʾēr in 10:15.

---

## Decisions on the Translator's questions

1. **10:1, ʾāwen and ʿāmāl.** The line reads "iniquitous decrees … the writers who write mischief". ʿāmāl is "mischief" (BDB), not ASV "perverseness". → `lexical-cruxes-isaiah-10`.
2. **10:3, pᵉquddāh and šôʾāh.** ASV "the day of visitation … the desolation" is kept. NRSV and the 10:12 verb are covered in commentary. The central paqod entry and the overlay yippaqedu entry are not extended. → crux entry.
3. **10:3, kāḇôḏ.** "Glory" is used at 10:3, 16 and 18 (strict ruling 6), and the "wealth" sense is in commentary.
4. **10:4, biltî crux.** The line becomes "Nothing remains but to crouch under the prisoners, and they shall fall under the slain". Lagarde's conjecture is reported and not adopted. The refrain is unchanged. → crux entry, `mt-qere-textual-policy-isaiah`, and refrain entry extended to ISA-10:4.
5. **10:5, the clause and the gloss.** The ASV construal and MT are kept, and the gloss-deletion is reported. The pair šēḇeṭ "rod" and maṭṭeh "staff" is fixed for the chapter, as at 9:3. → crux entry, policy entry.
6. **10:5, Assyria.** "Assyria" is used at every site (ruling 4; 14:25).
7. **10:6, ketiv/qere.** The qere is translated, and ASV "to tread them down" is kept. → policy entry.
8. **10:6, ḥānēp̄.** The line reads "a godless nation" (ruling 5).
9. **10:2, 10:6, šālāl and baz.** "Spoil" and "plunder" are fixed, and the echo of Maher-shalal-hash-baz is noted in commentary. The chapter 8 commentary should use the same pair when it glosses the name.
10. **10:9, 10:28–32, toponyms.** ASV spellings are used. Identifications (Aiath/Ai, Laishah/Laish, the Michmash pass) and the debated occasion of the march stay in commentary. The 25:10 madmēnāh entry is not applied. → new `march-itinerary-toponyms-isaiah-10`.
11. **10:10–11, idol nouns.** ʾĕlîlîm is "idols" (central elilim), and ʿăṣabbîm becomes "images", so that the two nouns are distinct within one verse. → central elilim and pesel extended, plus the crux entry.
12. **10:12, tip̄ʾereṯ.** "Boasting" is used (escalated above).
13. **10:12, ʾep̄qōḏ.** MT "I will punish" is kept, and the third-person versions are reported. → policy entry, `adonai-standalone-title-isaiah`.
14. **10:13, qere and lexical points.** The qere "treasures" is translated, and ASV "like a valiant man … those who sit on thrones" is kept. → policy entry, crux entry.
15. **10:14, 10:23, ʾereṣ.** "Earth" is used at both sites (escalated above). → `eretz-cosmic-scope-isaiah-24` extended.
16. **10:16, hā-ʾāḏôn and rāzôn.** "The Sovereign" (confirmed 2026-11-26). ASV "leanness among his fat ones" is kept.
17. **10:17, "light".** Lower-case "light" and capitalised "Holy One" are kept, as in ASV.
18. **10:18, nōsēs.** "A sick man wastes away" is used (escalated above).
19. **10:18, nep̄eš/bāśār.** ASV "both soul and body" is kept as a merism. The nefesh-throat entry is not applied.
20. **10:20, pᵉlêṭāh.** "The survivors of the house of Jacob" is kept, as at 4:2. Central pleitah is not extended.
21. **10:21, šᵉʾār yāšûḇ.** The line reads "A remnant will return" (ruling 1). 10:22 is harmonised to "will return". → modify op on `sign-names-isaiah-7-8` (ISA-10:21, 10:22).
22. **10:21, ʾēl gibbôr.** The line reads "to the Mighty God" (ruling 2). → modify op on `el-gibbor-mighty-god-isaiah`, plus `elohim-el-eloah-monotheistic-formula-isaiah` extended.
23. **10:22, kiḷḷāyôn ḥārûṣ and ṣᵉḏāqāh.** ASV is kept, and the "retribution" sense is in commentary. → new central entry and crux entry.
24. **10:23, kālāh wᵉneḥĕrāṣāh.** ASV "a full end, and that determined" is kept, matching the corpus Daniel at 9:27. → new central `kalah-venecheratzah-decreed-full-end-cross-corpus`.
25. **10:24, 10:26, bᵉḏereḵ miṣrāyim.** ASV "after the manner of Egypt" is kept, and the literal "on the way of Egypt" is in commentary. Central mitsrayim and al-tira are not extended.
26. **10:25, taḇlîṯām.** The ASV structure with the MT plural "their" is kept, and the emendation is reported. → policy entry.
27. **10:27, ʿōl mippᵉnê-šāmen.** MT "by reason of fatness" and the MT verse division are kept. KJV "anointing", the Targum and the NRSV "Rimmon" emendation are given in commentary. → policy entry, crux entry.
28. **10:29, mālôn lānû.** The narrative rendering of ASV and JPS 1917 is kept (NRSV likewise, from memory). The accentuation does not decide between the verb and the preposition, and NJPS's quoted-speech reading "Geba is to be our night quarters!" is reported in commentary. → crux entry. (Corrected after review; see below.)
29. **10:30, ʿăniyyāh.** MT "O poor Anathoth!" is kept, and the repointing is reported. → policy entry.
30. **10:32, ketiv/qere.** The qere "the daughter of Zion" is translated. → policy entry.
31. **10:33, hā-ʾāḏôn and maʿărāṣāh.** "The Sovereign" (confirmed 2026-11-26), and ASV "with terror" is kept.
32. **10:34, ʾaddîr.** ASV "by a mighty one" is kept, with the agent unspecified.

## Glossary changes for review

### Central glossary (propose 2.93.0 → 2.95.0)

- Added: `kalah-venecheratzah-decreed-full-end-cross-corpus` (claim_type: `direct`). appliesTo: ISA-10:22, ISA-10:23 and DAN-WOH-9:27. Daniel 9:27 already uses the wording, but its `glossaryRefs` were not touched. The orchestrator may add the ref there.
- Modified: `elilim-idols-cross-corpus`, a pending add from wave-i1-ch2. appliesTo is extended to ISA-10:10 and 10:11, and no wohChoice is changed.
- Modified: `pesel-utemunah-graven-image-iconographic-prohibition-cross-corpus`. appliesTo is extended to ISA-10:10.
- Note op: deliberate non-extensions (she-erit, pleitah, al-tira, patriarchal triad, zub-sig, vayisha-er-noach, paqod-yiphqod, mitsrayim, eretz).

### Per-translation overlay (propose 1.6.1 → 1.8.0)

- Added: `lexical-cruxes-isaiah-10` (claim_type: `direct`).
- Added: `march-itinerary-toponyms-isaiah-10` (claim_type: `direct`).
- Modified, appliesTo extensions with rationaleAppend; no wohChoice is changed:
  - On entries that exist only in pending diffs:
    - `sign-names-isaiah-7-8` (ch7)
    - `el-gibbor-mighty-god-isaiah` (ch9)
    - `ha-adon-articular-title-isaiah` (wave-i1-ch1)
    - `hoy-woe-isaiah` (wave-i1-ch1)
    - `bekhol-zot-lo-shav-appo-refrain-isaiah` (wave-i1-ch5)
  - On existing entries:
    - `eretz-cosmic-scope-isaiah-24`
    - `mt-qere-textual-policy-isaiah` (nine sites)
    - `adonai-standalone-title-isaiah`
    - `adonai-yhwh-compound-isaiah-25`
    - `yhwh-tzevaot-hosts-isaiah`
    - `elohim-el-eloah-monotheistic-formula-isaiah`
    - `title-and-meta-conventions-isaiah`
- Note op: the concordance record (kāḇôḏ is strict, with the departure at 10:12) and deliberate non-applications.
- Merge hint: if the chapter 9 Editor creates a ḥānēp̄ entry for 9:16, add ISA-10:6 to it.

## Verifications not completed (disclosed)

- The following citations come from model recall and were not checked against texts:
  - the ASV and NRSV wordings quoted in commentary;
  - the LXX and Syriac third person at 10:12;
  - the Targum at 10:27;
  - Lagarde's conjecture at 10:4, which is reported through the commentaries;
  - BDB on nss at 10:18.
- The Strong's numbers in all new entries are from model recall and are marked as such.

## Post-review corrections

The Reviewer returned the chapter as `awaiting-human`. Only non-decision corrections were applied. No English line, `translation.status`, `reviewerReport` block or shared glossary was changed, and daniel-woh was not edited.

1. **10:29 (revise).**
   - The accent argument is withdrawn from three places: the 10:29 note, item (8) of `lexical-cruxes-isaiah-10` (rationale and wohChoice) and decision 28 above.
   - The argument was wrong: the suffixed preposition lā́nû "to us" is also stressed on the first syllable (WLC 9:5; 1:9), so the accent cannot mark the verb.
   - The line now rests on ASV and JPS 1917, with NRSV marked from memory. NJPS's quoted-speech reading "Geba is to be our night quarters!" is reported.
2. **Central `kalah-venecheratzah-decreed-full-end-cross-corpus` (revise).**
   - standardEnglish now records ASV by site. Isa 28:22 reads "a decree of destruction … upon the whole earth" and does not keep the pair, so 28:22 will depart from ASV under this entry. Dan 9:27 reads "the full end, and that determined".
   - wohChoice now allows the article ("a/the full end", as English idiom requires at each site).
   - DAN-WOH-11:36 "that which is determined" is noted as a participle-only echo, outside appliesTo.
   - The rationale says the orchestrator adds the DAN-WOH-9:27 glossaryRef at merge.
3. **Optional note improvements (advisory).**
   - The 10:4 note now says that "to crouch" (as in JPS 1917) hides the singular of kāraʿ. It also reports that NJPS continues the question of 10:3 into 10:4a.
   - The 10:10 note reports NJPS "the insignificant kingdoms" (ʾĕlîl in the sense "worthless").

## Founder rulings applied (2026-11-26)

The founder signed off wave I-3 with every recommended default ("Sign-off ok", 2026-11-26; `wave-i3-signoff-package.md`), together with wave I-1 decisions 1 and 2. `translation.status` and the `reviewerReport` block are unchanged. Statements above marked pending or provisional are settled as follows.

- **10:16, 10:33, hā-ʾāḏôn:** "the Sovereign" stands (wave I-1 decision 1, option B). The 10:16 note drops "provisionally … pending founder ruling" and the option-A reversion sentence, and now cites NJPS "The Sovereign LORD of Hosts" and ASV "the Lord". The 10:33 note drops "provisional … founder ruling pending". The `ha-adon-articular-title-isaiah` rationaleAppend is rewritten without the proviso. Lines are unchanged.
