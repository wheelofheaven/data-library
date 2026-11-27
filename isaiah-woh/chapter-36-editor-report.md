# Chapter 36 Editor Report

Isaiah 36 (22 verses), wave I-6 (Isa 36–39, 41).
Editor: claude-opus-5-5 (editor), 2026-11-27.
Base: central glossary v5.0.0 and isaiah-woh overlay v4.0.0, both read-only, with `wave-i6-rulings.md` in force.
All glossary changes are in `wave-i6-ch36-overlay-diff.json` and `wave-i6-ch36-central-diff.json`.

## Summary

- **Editorial questions:** all 18 are resolved and `editorial_questions[]` is empty. None is left unresolved. Five decisions are listed below for the founder, each with a recommended default.
- **English-line changes:** ten verses change, plus the chapter title. Each change is backed by a glossary op.
  - Title, 36:2, 4, 11, 12, 13, 22: "Rabshakeh" becomes "the Rabshakeh" (new overlay `rabshakeh-title-isaiah`; wave I-6 rule 7).
  - 36:6: "this bruised reed" becomes "this crushed reed", to match the stable 42:3 (`lexical-cruxes-isaiah-36`).
  - 36:8: "give pledges, I pray you, to my master" becomes "please make a wager with my master" (JPS 1917; cruxes).
  - 36:11: "I pray you" becomes "Please"; 36:11, 13: "the Jews’ language" becomes "Judean" (NJPS; cruxes).
  - 36:16: "eat every one of his vine, and every one of his fig tree, and drink every one the waters of his own cistern" becomes "eat, everyone from his vine and everyone from his fig tree, and drink, everyone the waters of his own cistern" (cruxes, `adam-humankind-ish-man-isaiah`).
  - 36:21: the king's order takes double quotation marks (`title-and-meta-conventions-isaiah`).
- **Commentary:** all 22 verses have `notes.official`. Each note records where the 2 Kgs 18:13–37 Hebrew differs (wave I-6 rule 3). No note carries a Wheel of Heaven reading.
- **Status:** `editor-review`, `1.0.0-rc1`, and "claude-opus-5-5 (editor)" is added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 5.0.0 and 4.0.0; the orchestrator sets them on merge. `rabshakeh-title-isaiah` and `lexical-cruxes-isaiah-36` exist only in the wave diff until then.
- **Lens audit:** no English line carries a project reading. The canon in data-library (*The Book Which Tells the Truth*, *Extraterrestrials Took Me to Their Planet*, *Let's Welcome the Extraterrestrials*) does not mention Isa 36, Hezekiah, Sennacherib or the Rabshakeh (grep, 2026-11-27). Rule 4 asks for a premise a source supports, and there is none, so no speculative note was written.
- **Verification (2026-11-27):**
  - ASV Isa 36 and ASV 7:3, 24:2, 42:3, Prov 5:15, 2 Kgs 18:20, 18:31 and Neh 13:24, through bible-api.com.
  - NJPS ("Tanakh: The Holy Scriptures, published by JPS", 1985) and JPS 1917 Isa 36 through the Sefaria API v3, including the NJPS notes at 36:1, 2, 5, 16 and 19. NJPS 42:3 was checked too.
  - The Hebrew of 2 Kgs 18:13–37 in the Westminster Leningrad Codex ("Tanach with Ta'amei Hamikra", Sefaria). Ezek 29:6 and Isa 31:1 Hebrew were checked as well.
  - BDB through Sefaria: *rab-šāqēh* (under רַב), *rṣṣ*, *peḥāh*, *ʿrḇ* Hithpael, *swt* Hiphil, *yᵉhûḏîṯ*, *bôr*; *bᵉrāḵāh* "treaty of peace" only in the BDB Augmented Strong abridgement.
  - Not verified, and labelled "recalled" in the commentary: HALOT, CAD, *šarru rabû*, Sennacherib's annals, Prov 14:23, 2 Kgs 18:4, the chronology of the fourteenth year, the surrender sense of *bᵉrāḵāh* in commentators, and the location of Sepharvaim.

## Speculative entries requiring sign-off

None. Both new entries and all extensions are `claim_type: direct`. The central `bor` entry stays `inferred`. No commentary paragraph is labelled speculative.

## Founder decisions (recommended defaults, decided in the line)

### ISA-36:11, 13 — yᵉhûḏîṯ "in Judean"

**Issue:** ASV and JPS 1917 have "in the Jews’ language"; NJPS has "in Judean" (checked).
**Decision in the line:** "in Judean". The word is the feminine gentilic of *yᵉhûḏāh*, used as an adverb (BDB: "only as adv."), and is built like *ʾărāmîṯ* "in Aramaic" in the same verse. In a narrative set in 701 BCE, "the Jews’ language" brings in the later sense of *yᵉhûḏî*.
**Options:**
- (A) "Judean" (recommended).
- (B) "the language of Judah". This is NRSV-type wording, not verified.
- (C) Keep ASV "the Jews’ language".

The ruling carries to 2 Kgs 18:26, 28, 2 Chr 32:18 and Neh 13:24 when those books are drafted.

### ISA-36:6 — hārāṣûṣ "crushed"

**Decision in the line:** "this crushed reed". The form and the noun are the same as at 42:3, which the stable chapter prints "A crushed reed", and BDB groups the two sites together. ASV and JPS 1917 have "bruised" at both sites. NJPS has "splintered" here and "bruised" at 42:3.
**Options:**
- (A) "crushed" here, to match 42:3 (recommended).
- (B) Keep ASV "bruised" here. The two Isaiah sites would then differ.

### ISA-36:8 — hiṯʿāreḇ "make a wager with"

**Decision in the line:** "please make a wager with my master". The wording is JPS 1917's, and NJPS has "make this wager". BDB glosses the Hithpael "exchange pledges (make a bargain) with", citing this verse. ASV's "give pledges … to" renders *ʾeṯ* "with" as "to".
**Recommendation:** accept.

### ISA-36:12 — the qere euphemism kept

**Decision in the line:** ASV and JPS 1917's "their own dung … their own water", which renders the qere *mêmê raḡlêhem*. NJPS has "their urine".
**Why this is flagged:** at 13:16 the qere policy rendered a euphemism by its sense. Here the polite English hides nothing, so the register of the qere is kept. The distinction is recorded in the `mt-qere-textual-policy-isaiah` rationaleAppend.
**Options:**
- (A) Keep "their own water" (recommended).
- (B) "their urine" (NJPS), on the 13:16 model.

### Central `bor-pit-cistern-dry-water-shaft` — household-cistern context clause

**Issue:** the entry renders *bôr* "pit". At 36:16 the noun is a household water cistern, *mê-ḇôrô* "the waters of his cistern". That is BDB's first sense, and BDB cites Isa 36:16 = 2 Kgs 18:31 for it. ASV, JPS 1917 and NJPS all have "cistern" here.
**Staged op:** `changes.wohChoice` keeps the existing text verbatim and appends a clause: "cistern" where *bôr* is a water cistern named with its water. ISA-36:16 is added to appliesTo. The sites already governed keep "pit".
**Semver:** minor if the clause is treated like the earlier eretz and goel-geullah clauses; major if any wohChoice edit counts as a modification.
**Recommendation:** accept. If declined, the orchestrator drops the `changes` and the appliesTo addition, removes `bor-pit-cistern-dry-water-shaft` from the 36:16 glossaryRefs, and rewords the last sentence of the 36:16 cistern paragraph. The line keeps "cistern" in either case.

## Items for the founder (not blocking)

- **36:16 distributive *ʾîš*.** The draft had copied ASV without ASV's "ye", which made it ungrammatical. The line now reads "everyone … his", as at 19:2. NJPS's purpose clause ("so that you may all eat …") is reported in commentary.
- **36:9 *paḥaṯ*.** "captain" is kept with ASV and JPS 1917, and BDB itself places this verse under "as Assyrian captains". "governor" (the loanword's sense) and NJPS "deputy" are in commentary.
- **36:18 *yassîṯ*.** "persuade" is kept with ASV and JPS 1917. BDB's pejorative "instigate" and NJPS "mislead" are in commentary.
- **36:2 Rabshakeh untranslated.** The title is not translated ("the chief cupbearer"), because BDB's "chief of the officers (?)" and the modern "chief cupbearer" disagree. The line uses the article only.

## Unresolved editorial questions

None.

## Decisions on the Translator's questions

1. **36:2 raḇ-šāqēh.** "the Rabshakeh" at all six sites, with NJPS and on the 20:1 "the Tartan" model (rule 7). → new `rabshakeh-title-isaiah`.
2. **36:2 conduit.** The stable 7:3 English is kept; only the preposition differs ("by" for *bᵉ*, against 7:3 *ʾel-qᵉṣēh* "at the end of"). The Kings 18:17 *ʾăšer* is reported. → cruxes.
3. **36:3, 22 ʾăšer ʿal-habbāyiṯ.** "who was over the house", extending the 22:15 decision. ASV "household" and NJPS "in charge of the palace" are reported. → `lexical-cruxes-isaiah-22` (+36:3, 36:22; the chapter 37 Editor adds 37:2).
4. **36:4 bṭḥ.** The noun is "confidence" and the verb "trust (in)" throughout, as at 31:1 and 32:17. → cruxes.
5. **36:5 ʾāmartî.** MT's first person is kept. Kings *ʾāmartā* (WLC) and the NJPS note are reported. The idiom stays literal, in ASV's construal without its supplied word. → `mt-qere-textual-policy-isaiah`, cruxes.
6. **36:6 rāṣûṣ.** "crushed", to match 42:3 (founder item above). → cruxes.
7. **36:6 ʾîš.** "anyone … his hand". → `adam-humankind-ish-man-isaiah`.
8. **36:8 hiṯʿāreḇ.** "make a wager with" (JPS 1917; BDB). → cruxes.
9. **36:8 ʾăḏōnî.** "my master / your master" (ASV, JPS 1917, NJPS; cf. 24:2). The 22:18 "your lord" is left as it is. → cruxes.
10. **36:9 paḥaṯ.** "captain" is kept (BDB "as Assyrian captains"). → cruxes.
11. **36:11, 13 language names.** "Aramaic" (aram-names principle) and "Judean" (founder item above). → `aram-names-isaiah`, cruxes.
12. **36:12 qere.** The qere is read, in ASV's words. → `mt-qere-textual-policy-isaiah` (+36:12; ketiv spellings ḥrʾyhm in Isaiah and ḥryhm in Kings).
13. **36:12 "the men".** Kept under ruling 13 (the defenders on the wall). → `adam-humankind-ish-man-isaiah`.
14. **36:16 bᵉrāḵāh.** "Make your peace with me" (ASV, JPS 1917, NJPS). → cruxes.
15. **36:16 bôr.** "cistern" under the proposed central context clause (founder item above). → central `bor-pit-cistern-dry-water-shaft`.
16. **36:16 setumah.** Noted in commentary: a mid-verse break (*pisqah bᵉʾemṣaʿ pāsûq*), absent from the Kings parallel as printed on Sefaria. The English line is unchanged.
17. **36:19 wᵉḵî.** "And have they delivered Samaria …?" (ASV, JPS 1917). The NJPS note and Kings' Hena and Ivvah are reported. → `march-itinerary-toponyms-isaiah-10` (+36:19), cruxes.
18. **36:14, 18 yaššîʾ / yassîṯ.** "deceive" / "persuade", kept distinct with ASV. BDB and NJPS are reported. → cruxes.

## Glossary changes for review

### Central glossary (5.0.0 → 5.1.0 proposed)

- Modified: `bor-pit-cistern-dry-water-shaft`. appliesTo +ISA-36:16; `changes.wohChoice` appends the household-cistern clause; rationale addendum (founder item).
- Modified (appliesTo, with addenda):
  - `eretz` (+36:10, 17, 18, 20)
  - `hishtachavah-bow-down-obeisance-worship` (+36:7)
  - `mizbeach-olah` (+36:7)
  - `kerem-vineyard` (+36:17)

### Per-translation overlay (4.0.0 → 4.1.0 proposed)

- Added: `rabshakeh-title-isaiah` (claim_type: `direct`), ISA-36:2, 4, 11, 12, 13, 22. The chapter 37 Editor extends it to 37:4 and 37:8.
- Added: `lexical-cruxes-isaiah-36` (claim_type: `direct`), ISA-36:1–22. It also records the Kings parallel for the chapter.
- Modified (appliesTo, with addenda):
  - `lexical-cruxes-isaiah-22` (+36:3, 36:22)
  - `aram-names-isaiah` (+36:1, 2, 4, 6, 8, 9, 11, 13, 15, 16, 18; includes "Aramaic")
  - `march-itinerary-toponyms-isaiah-10` (+36:19)
  - `mt-qere-textual-policy-isaiah` (+36:5, 36:12)
  - `adam-humankind-ish-man-isaiah` (+36:6, 12, 16)
  - `elohai-elohenu-doxology-isaiah-25` (+36:7)
  - `elohim-el-eloah-monotheistic-formula-isaiah` (+36:18, 19, 20)
  - `title-and-meta-conventions-isaiah` (+36:1, 4, 13, 21: title, quotation structure, 36:21 marks)

## Coordination notes for the orchestrator

- Apply the `rabshakeh-title-isaiah` add op before the chapter 37 Editor's modify op.
- The chapter 37 Editor should extend `lexical-cruxes-isaiah-22` to 37:2 with the same wording, "who was over the house".
- Several ops in the wave touch the same entries (aram-names, title-and-meta, mt-qere, elohim-el-eloah, adam-humankind). Merge them as a union of appliesTo additions and append the addenda in chapter order.

## Post-review corrections

The Reviewer returned the chapter as `awaiting-human` (reviewerReport in `chapter-36.json`). The corrections below change only commentary and the wave overlay diff. No English line, `translation.status`, the reviewerReport block or any shared glossary was changed.

1. **36:3 note.** Adds that 2 Kgs 18:18 has *wayyēṣēʾ ʾălēhem* "and he came out to them" where Isaiah has *ʾēlāyw* "to him", in keeping with Kings' three envoys (18:17).
2. **36:10 note.** Adds that Isaiah opens *wᵉʿattāh* "And now" and Kings 18:25 opens *ʿattāh* without *wᵉ*.
3. **36:2 note.** Adds the two smaller 18:17 variants: Kings *min-lāḵîš* for Isaiah's contracted *millāḵîš*, and Kings' *yᵉrûšālāim* placed after *bᵉḥêl kāḇēḏ*, where Isaiah has *yᵉrûšālaymāh* before *ʾel-hammeleḵ*.
4. **`lexical-cruxes-isaiah-36` (overlay diff).** The wohChoice sentence now says that every verse records the differences of wording, names the small variants at 36:2, 3 and 10, and states that purely orthographic plene/defective differences are not listed. A post-review sentence is appended to the rationale.
5. **36:12 (founder decision, revised).** The line keeps ASV, "to eat their own dung and to drink their own water with you". The Reviewer's alternative, "to eat their dung and to drink the water of their feet with you", is staged in `lexical-cruxes-isaiah-36`, marked **PENDING FOUNDER RULING**. The 36:12 note now presents it on the model of 7:20. The `mt-qere-textual-policy-isaiah` addendum now relates 36:12 to the stable 7:20 ("the hair of the feet", kept literally and explained in commentary) as well as to 13:16 (rendered by sense). It also says why ASV was kept for now.
   - **Options:**
     - (A) Keep ASV "their own water".
     - (B) The literal qere, "the water of their feet", concordant with 7:20.
     - (C) NJPS "their urine".
   - **If B is adopted:** the orchestrator changes the 36:12 line, rewrites the PENDING clause as the ruling, and trims the 36:12 note.
   - **Editor's view after review:** B is the more concordant choice. A remains defensible.
