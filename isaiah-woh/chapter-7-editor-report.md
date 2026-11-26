# Chapter 7 Editor Report — Isaiah 7 (the sign given to Ahaz)

Wave I-3 (Isa 7–12), chapter 7 Editor.

**Chapter advanced:** `translation.status` → `editor-review`; `translation.version` → `1.0.0-rc1`; `reviewer` left `pending`.
`glossaryVersion` and `overlayGlossaryVersion` are left at the read base (2.93.0 / 1.6.1). The orchestrator bumps them at merge.

**Glossaries:** neither shared glossary was edited.
All changes are in `wave-i3-ch7-overlay-diff.json` (13 ops) and `wave-i3-ch7-central-diff.json` (7 ops).

**Line changes.** Each one is backed by a glossary entry.

| refId | Draft | Now | Entry |
|---|---|---|---|
| ISA-7:1, 2, 4, 5, 8 | "Syria" | "Aram" | `aram-names-isaiah` (wave ruling 4) |
| ISA-7:6 | "vex it" | "terrify it" | `qutz-dread-isaiah-7` (inferred) |
| ISA-7:15 | "Butter and honey" | "Curds and honey" | `lexical-cruxes-isaiah-7` |
| ISA-7:16 | "whose two kings you abhor" | "whose two kings you dread" | `qutz-dread-isaiah-7` |
| ISA-7:22 | "butter" (×2) | "curds" (×2) | `lexical-cruxes-isaiah-7` |

The Translator had already printed "the young woman" (7:14), "test" (7:12), "whistle" (7:18) and "hoed" (7:25). These are ratified and now have entries. No other line was altered.

---

## Speculative entries requiring sign-off

There are no speculative glossary entries. Of the six new overlay entries, five are `direct` and one is `inferred` (`qutz-dread-isaiah-7`).

### Speculative commentary paragraph at ISA-7:14 (founder sign-off 2026-11-26)

**Location:** the final paragraph of `notes.official` at ISA-7:14, headed "Wheel of Heaven reading (speculative; commentary only)".
**Content:** the canon reads the conception in Matt 1:18–20 as the birth of "a child issued from a woman and from one of their own" (TBWTT 4:3, wording checked in `the-book-which-tells-the-truth/chapter-4.json`). The canon does not cite Isa 7:14 there. Carrying that reading to this verse goes through Matthew's Greek, not the Hebrew. The Hebrew says nothing about how the child is conceived, and the line is unaffected.
**Why speculative:** applying the canon's Matthew reading to Isaiah 7:14 is a project extension. No source makes that link: the canon does not cite Isaiah, and the Hebrew does not support it.
**Recommendation:** ship it as written (founder sign-off 2026-11-26: kept). Wave ruling 3 permits exactly this form, and the paragraph tells the reader where the lens stops. If the founder prefers that the most-scrutinised verse in the book carry no lens paragraph at all, drop it. Nothing else depends on it.

---

## Escalations

### `ISA-7:14` — "the young woman" (orchestrator ruling 3; founder visibility)

**Issue:** the line departs from ASV/KJV "a virgin". This is the book's most visible departure from the ASV.
**Options considered:** (A) "the young woman" (NRSV, NJPS; ruling); (B) "a virgin" (ASV, KJV, following the LXX as cited in Matt 1:23); (C) "a young woman" (RSV, which drops the article).
**Why escalating:** the Editor considers A correct and has applied it (`almah-young-woman-isaiah-7-14`, direct). Because this is the most-scrutinised verse in the book, the founder should see the decision by name. The commentary sets out: the lexical range of ʿalmâ against bᵉṯûlâ (including the counter-observation that no biblical ʿalmâ is clearly a married woman); the article; the annunciation formula (Gen 16:11; Judg 13:5); the ambiguous wᵉqārāʾṯ; the LXX *parthenos*, with Aquila and Theodotion reported as *neanis* (Irenaeus 3.21.1); Justin's *Dialogue*; and Matt 1:23, governed by the central entry for the Matthew line.

### `ISA-7:14` — readings not verified

- 1QIsaᵃ *wqrʾ* for MT *wᵉqārāʾṯ* is marked "not verified" in the commentary and in the `mt-qere-textual-policy-isaiah` addendum, because DJD XXXII is not held.
- The LXX second-person verb (*kaléseis*, as commonly reported) is also marked not verified. It is not quoted in Greek.
- The Justin chapter numbers (43; 67) and the Irenaeus reference come from the Editor's knowledge and were not checked against an edition. The Reviewer should confirm them or cut them.

### `ISA-7:13` — "to weary men" (depends on wave I-1 decision 2)

**Issue:** ʾănāšîm is a generic plural set against "my God". NRSV has "mortals".
**Options considered:** (A) "men" (ASV; kept); (B) "people"; (C) "mortals" (NRSV).
**Why escalating:** this is not an ʾāḏām/ʾîš pair, so wave I-1 decision 2 does not formally cover it. If the founder adopts that decision's recommended option C1 (avoid gendered generics), this line should read "to weary people" for consistency. The Editor kept the ASV pending that ruling.

### `ISA-7:6` — "terrify it" (inferred)

**Issue:** the root of nᵉqîṣennāh is disputed. It may be qûṣ I "dread" (BDB) or a root meaning "cut, tear apart" (NRSV "cut off").
**Why flagged:** the Editor adopted BDB's derivation so that 7:6 and 7:16 share the same root. The derivation is not certain, so the entry is `inferred`. The Reviewer may prefer to restore ASV "vex it". If so, 7:16 "dread" still stands on its own (Exod 1:12; Num 22:3).

### Central housekeeping — the Matt 1:23 parthenos entry (founder approval)

`isa-7-14-virgin-birth-mt-1-22-23-parthenos-vs-almah-philological-dispute-cross-corpus` has two inaccurate statements. The central diff records them as a `note` op, not an automatic change.

1. Its `wohChoice` says the LXX "adds" the article *hē*, which it claims is "not in Hebrew". In fact the Hebrew hā- is the definite article, and the LXX renders it.
2. Its disavowal (iv) attributes to the canon an "engineered conception using preserved Mary-genome material". TBWTT 4:3 says only "a child issued from a woman and from one of their own", and it does not cite Isaiah.

Corrected wording is proposed in the note. Applying it changes existing text, which is a major bump.

### Coordination (orchestrator)

- `sign-names-isaiah-7-8` is added here with 8:1, 8:3, 8:8, 8:10 and 10:21 pre-listed. The chapter 8 Editor's modify op on that id becomes redundant in scope, but its `rationaleAppend` should be kept. The chapter 10 Editor's op is merged the same way.
- `aram-names-isaiah` pre-lists ISA-9:11. The chapter 9 line already prints "Aram", but chapter 9 has no entry for it. Add the ref to chapter 9's `glossaryRefs` at merge.
- `sharaq-whistle-isaiah` lists ISA-5:26, the wave I-1 line, which has no entry of its own. Add the ref to chapter 5's `glossaryRefs` at merge. The entry sits alongside the chapter 11 Editor's `nes-signal-isaiah` at the same verse.
- Strong's numbers in all new entries come from recall and are marked "not concordance-verified".

---

## Editorial questions resolved (22 of 22)

R = Translator's default ratified; O = overruled.

1. **7:1 ʾărām** — O (wave ruling 4). "Aram" at 7:1, 2, 4, 5, 8; new `aram-names-isaiah` (direct).
2. **7:1 yāḵōl** — R. "but could not prevail against it" (ASV). The MT singular against 2 Kgs 16:5's plural, and NRSV's alternative, are in the commentary.
3. **7:2 nāḥāh ʿal** — R. "Aram is confederate with Ephraim" (ASV sense). The literal "has settled upon" and the echo of the same verb in 7:19 are in the commentary.
4. **7:3 Shear-jashub** — R. Transliterated (wave ruling 1); new `sign-names-isaiah-7-8` (direct). `she-erit-remnant…` is not applied.
5. **7:6 nᵉqîṣennāh / Tabeel** — O on the verb ("terrify it"; `qutz-dread-isaiah-7`, inferred). R on "Tabeel"; the pausal pun is in the commentary.
6. **7:8 sixty-five years** — R, with the gloss hypothesis in commentary. The site is added to `mt-qere-textual-policy-isaiah`.
7. **7:9 ʾmn wordplay** — R. ASV wording. The root-play, the link to 2 Sam 7:16, the plural address and NRSV's imitation are in the commentary.
8. **7:11 šᵉʾālāh** — R (MT pointing). The Sheol repointing (NRSV; Vulgate) is reported. Added to the policy entry.
9. **7:12 nsh** — R. "I will not test YHWH". The central `nisah-divine-testing` is extended, with a rationale addendum for the human-tests-God direction (Deut 6:16).
10. **7:13 ʾănāšîm** — R ("men"). Escalated as conditional on wave I-1 decision 2.
11. **7:14 hā-ʿalmâ** — R (wave ruling 3). New `almah-young-woman-isaiah-7-14` (direct). The central parthenos entry is cross-referenced and not applied. Escalated for visibility.
12. **7:14 tense / qārāʾṯ** — R. "is with child and shall bear a son, and shall call his name". The 1QIsaᵃ reading is marked "not verified".
13. **7:14 ʾôṯ** — R. "a sign"; no entry applied. The central `aya…` and Genesis ot entries are listed as non-extensions.
14. **7:14 Immanuel** — R. Transliterated; covered by `sign-names-isaiah-7-8`.
15. **7:15 ḥemʾâ / lᵉḏaʿtô** — O on ḥemʾâ: "curds" (BDB; NRSV, NJPS) at 7:15 and 7:22. R on "when he knows". `tov-ra-merism` is not applied.
16. **7:16 qāṣ mippᵉnê / ʾăḏāmāh** — O on the verb: "dread" (idiom of Exod 1:12; Num 22:3), replacing "abhor". R on the ASV syntax and on "the ground" (central `adam-adamah` extended).
17. **7:17 gloss** — R. MT kept, with the gloss hypothesis in commentary; added to the policy entry.
18. **7:18 šāraq / fly, bee / yᵉʾōrê** — R. "whistle" now has the new `sharaq-whistle-isaiah` (direct; 5:26 + 7:18). The collective singulars are literal. Central `yeor…` and `eretz` are extended.
19. **7:19 rare words** — R. ASV for all three. "settle" for nāḥû is ratified and recorded in `lexical-cruxes-isaiah-7`.
20. **7:20 razor** — R. ASV wording. The euphemism is kept literally and explained in commentary, along with the hiring irony (2 Kgs 16:7–8) and the gloss *bᵉmeleḵ ʾaššûr* (policy entry).
21. **7:22 diet** — R, apart from "curds". The question of plenty versus poverty is left open in the commentary.
22. **7:25 construal / hoed** — R. 2ms "you shall not come there"; the 3fs construal is in commentary. "hoed with the hoe" matches 5:6.

`editorial_questions[]` is now empty.

---

## Commentary written (notes.official)

19 of 25 verses: 7:1, 2, 3, 4, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 25.
No commentary at 7:5, 7, 10, 21, 23, 24. These are standard readings, and their lexical points are covered at neighbouring verses.
The 7:14 note has eight paragraphs:
1. lexeme
2. bᵉṯûlâ
3. article and identity
4. grammar of the formula
5. qārāʾṯ and variants
6. the name and the sign
7. reception
8. the labelled speculative paragraph

---

## Glossary changes for review

### Central glossary (`wave-i3-ch7-central-diff.json`; 2.94.0 → 2.95.0 proposed, read base 2.93.0)

- Modified: `nisah-divine-testing`. Added ISA-7:12, with a rationale addendum on a human testing God; `wohChoice` unchanged.
- Modified: `yeor-nile-egyptian-loanword`. Added ISA-7:18.
- Modified: `adam-adamah`. Added ISA-7:16.
- Modified: `eretz`. Added ISA-7:18, 22, 24.
- Note (housekeeping, founder approval): corrections proposed for `isa-7-14-virgin-birth-mt-1-22-23-parthenos-vs-almah-philological-dispute-cross-corpus`.
- Note: deliberate non-extensions (`she-erit…`, `al-tira…`, `elohim-imkha…`, `emmanuel-frame…`, `tov-ra-merism`, `sheol…`, `aya…`/ot entries).

### Per-translation overlay (`wave-i3-ch7-overlay-diff.json`; 1.7.0 → 1.8.0 proposed, read base 1.6.1)

- Added: `sign-names-isaiah-7-8` (claim_type: `direct`)
- Added: `almah-young-woman-isaiah-7-14` (claim_type: `direct`)
- Added: `aram-names-isaiah` (claim_type: `direct`)
- Added: `qutz-dread-isaiah-7` (claim_type: `inferred`)
- Added: `sharaq-whistle-isaiah` (claim_type: `direct`)
- Added: `lexical-cruxes-isaiah-7` (claim_type: `direct`)
- Modified (appliesTo only, plus addenda where noted): `mt-qere-textual-policy-isaiah` (7:8, 11, 14, 17, 20; addendum), `title-and-meta-conventions-isaiah` (title ratified, quotation extents; addendum), `adonai-standalone-title-isaiah` (7:14, 20), `adonai-yhwh-compound-isaiah-25` (7:7), `elohai-elohenu-doxology-isaiah-25` (7:11, 13).
- Note: deliberate non-applications (`elohim-el-eloah…` at the name site, `chemah-shamir-shayit…`, `eretz-cosmic-scope…`).

---

## Post-review corrections (2026-11-26)

The Reviewer's report (`translation.reviewerReport` in `chapter-7.json`) gives 2 revise verdicts (7:6, 7:14) and 2 flag-for-human verdicts (7:13, and the central housekeeping note). Every other verse and glossary item is approved, and no lens leakage was found.
Only the non-decision corrections are applied here.

Left unchanged:
- `translation.status` (`awaiting-human`)
- the `reviewerReport` block
- every English line (checked programmatically)
- both shared glossaries

The changes are in commentary, in the two wave diff files and in this report.

1. **ISA-7:6 note.**
   - **BDB's reservation added.** BDB parses the form as the Hiphil of *qûṣ*, but it calls that parse weak and recommends *nᵉṣîqennāh* (from *ṣûq* "distress"). Both readings give a sense of pressure or terror, so "terrify it" stays.
   - **Tabeel's two explanations separated.** One is a simple pausal form for *ṭāḇᵉʾēl* (Ezra 4:7), after Olshausen and König. The other is the "good-for-nothing" pun, after Delitzsch, Dillmann, Duhm and Stade (BDB s.v.).
   - **Glossary diff.** In `qutz-dread-isaiah-7`, the rationale's "The Editor follows BDB" is rewritten to report BDB's reservation; claim_type stays `inferred`. In `lexical-cruxes-isaiah-7`, "the pausal pun" now reads "a pausal form or … pun".
2. **ISA-7:14 note.**
   - The queens and concubines are now attributed to Song 6:8 only, not 1:3.
   - The *bᵉṯûlâ* sentence is softened to "The word that usually carries the sense of virginity is *bᵉṯûlâ*".
   - The Septuagint second person *kaléseis* is now stated as verified, with the Greek clause transliterated. Only 1QIsaᵃ *wqrʾ* is still "not verified".
   - The same updates are made in `almah-young-woman-isaiah-7-14` (rationale, which now also quotes BDB's gloss "maid or newly married") and in the `mt-qere-textual-policy-isaiah` addendum.
3. **`almah-young-woman-isaiah-7-14`.** "ASV here translates the Greek text" now reads "ASV here follows the rendering of the Greek text cited in Matt 1:23".
4. **Central housekeeping note** (`isa-7-14-virgin-birth-…`).
   - Approved by the founder 2026-11-26 and applied through `wave-i3-orchestrator-ops.json` central.set. The Reviewer endorses points (1) and (2) as accurate.
   - Point (2) now names ETTMTTP 2:62 as the likely source of the "Mary-genome" confusion. That passage is about recreating Jesus from a preserved cell after the crucifixion, not about the conception.
   - Two further points are added, marked "to verify before applying". (3) RSV Matt 1:23 reads "a virgin shall conceive", so the entry is wrong to group RSV with ASV. (4) The entry uses Joel 1:8 as a plain "virgin" text, but it is the counter-case.
5. **Optional items applied.** NJPS is now named in three notes:
   - 7:8: NJPS moves the sixty-five-year clause after v. 9a, with a note. This is also in the mt-qere addendum.
   - 7:25: NJPS adopts the 3fs construal (quoted). This is also in `lexical-cruxes-isaiah-7`.
   - 7:11: NJPS takes the Sheol reading, as the Reviewer suggested (quoted). This is also in the mt-qere addendum.

**Superseded statements in this report:** the "readings not verified" escalation above is now partly out of date. The LXX *kaléseis*, Justin (Dial. 43, 67) and Irenaeus (AH 3.21.1) are verified by the Reviewer. Only 1QIsaᵃ *wqrʾ* remains unverified.
The 7:6 escalation's offer to restore "vex it" is withdrawn, since the Reviewer keeps "terrify it".

**Still for the founder** (all resolved 2026-11-26; see the final section):
- 7:13, "men" or "people" (wave I-1 decision 2)
- the speculative paragraph at 7:14 (the Reviewer approved it as written)
- the 7:14 departure from the ASV
- the central housekeeping note

## Founder rulings applied (2026-11-26)

The founder signed off wave I-3 with every recommended default ("Sign-off ok", 2026-11-26; `wave-i3-signoff-package.md`), together with wave I-1 decisions 1 and 2. `translation.status` and the `reviewerReport` block are unchanged. Statements above marked pending or provisional are settled as follows.

- **ISA-7:13** (wave I-1 decision 2, C1): line "to weary men" → "to weary people". Commentary rewritten to give ASV/NJPS "men" and NRSV "mortals". Recorded in `lexical-cruxes-isaiah-7` (wohChoice item and one rationale sentence). `adam-humankind-ish-man-isaiah` is not extended: its scope excludes ʾănāšîm outside the 2:9–22 / 5:15 refrain.
- **ISA-7:14 speculative paragraph:** kept (founder sign-off 2026-11-26).
- **ISA-7:14 "the young woman":** stands.
- **Central Matt 1:23 housekeeping:** all four points approved. Full corrected `standardEnglish`, `wohChoice` and `rationale` are written in `wave-i3-orchestrator-ops.json` central.set, and the note op in `wave-i3-ch7-central-diff.json` is marked applied. Because existing text changes, the strict policy is a major bump.
