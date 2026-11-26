# Chapter 35 Editor Report

Isaiah 35 (10 verses), wave I-5 (Isa 28, 30, 31, 33–35).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v4.0.0 and isaiah-woh overlay v3.0.0, both read-only, with `wave-i5-rulings.md` in force.
All glossary changes are in `wave-i5-ch35-overlay-diff.json` and `wave-i5-ch35-central-diff.json`.

## Summary

- **Editorial questions:** all 16 are resolved and `editorial_questions[]` is empty. One of them (35:10 pᵉḏûyê) is decided in the line and escalated as a founder decision.
- **English-line changes:** three verses change, and each change is backed by a glossary op.
  - 35:4: the message is set in quotation marks (overlay `title-and-meta-conventions-isaiah`).
  - 35:7: "shall be grass with reeds and rushes" → "grass shall become reeds and rushes" (overlay `lexical-cruxes-isaiah-35`).
  - 35:10: "the redeemed of YHWH" → "the ransomed of YHWH" (central `goel-geullah-redeemer-redemption-cross-corpus`, staged context clause; **founder decision**).
- **Commentary:** all 10 verses have `notes.official`. Two verses (35:2, 35:10) end with a separately headed reception note labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`, and "claude-opus-5-5 (editor)" is added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 4.0.0 and 3.0.0; the orchestrator sets them on merge. `lexical-cruxes-isaiah-35` exists only in the wave diff.
- **Lens audit:** no English line carries a project reading. The canon in data-library (TBWTT chs. 3 and 5, ETTMTTP ch. 2) does not cite Isa 35. The two speculative notes rest on canon readings of other verses: TBWTT 3:193–194 (Ezek 43:2, "the large ship respectfully called the «glory of God»") and 3:104–107 (1 Kgs 8:10–12) for 35:2, and TBWTT 5:25 (Isa 43:5–7, ingathering) for 35:10. Each says plainly that the canon does not cite Isa 35.
- **Verification (2026-11-26):**
  - ASV and KJV of Isa 35 through bible-api.com, plus ASV 1:27, 29:22, 50:2, 51:10–11, Jer 31:11 and Hos 13:14.
  - JPS 1917 and NJPS of Isa 35 through the Sefaria API v3. NJPS is "Tanakh: The Holy Scriptures, published by JPS", not the Gender-Sensitive Edition. The NJPS notes at 35:1, 7 and 8 were checked too.
  - 1QIsaᵃ readings come from Fred P. Miller's online collation of col. XXVIII (ao.net/~fmoeller). That is not DJD 32, and the commentary says so.
  - Not verified, and labelled "recalled" or "not verified" in the commentary: NRSV, LXX, BDB/HALOT, the grammars, commentators, and the NT references (Matt 11:5; Luke 7:22; Heb 12:12).

## Speculative entries requiring sign-off

No speculative glossary entry is proposed. Every new or extended entry is `claim_type: direct`.

There are two commentary paragraphs labelled speculative (reception notes, founder policy keeps such notes):

### ISA-35:2 reception note (kᵉḇôḏ-YHWH)

**Why speculative:** it carries TBWTT's reading of "the glory of God" in Ezek 43:2 as a craft (and the cloud of 1 Kgs 8 as a craft in orbit) over to Isa 35:2, which the canon does not cite.
**Recommendation:** ship as a labelled reception note.

### ISA-35:10 reception note (return to Zion)

**Why speculative:** it carries TBWTT 5:25's reading of Isa 43:5–7 as the return of the Jewish people and the State of Israel over to Isa 35:10, which the canon does not cite. This follows the 11:12 precedent.
**Recommendation:** ship as a labelled reception note.

## Founder decision

### ISA-35:10 — pᵉḏûyê YHWH "the ransomed of YHWH" (central `goel-geullah-redeemer-redemption-cross-corpus`)

**Issue:** the central entry's wohChoice gives pāḏâ the corpus English "redeem" (stable 1:27 "Zion shall be redeemed"; 29:22 "who redeemed Abraham"). Applied at 35:10, that puts gᵉʾûlîm (35:9, "the redeemed") and pᵉḏûyê (35:10) under one English word in adjacent verses, where the Hebrew pairs two roots.

**Evidence (checked):**
- ASV prints "redeem" for finite pdh (1:27; 29:22) and "the ransomed" for the participle wherever it is paired with gʾl: 35:9–10 and 51:10–11.
- ASV does the same with finite verbs in parallel: Jer 31:11 "hath ransomed Jacob, and redeemed him" and Hos 13:14 "I will ransom them … I will redeem them".
- JPS 1917, KJV and NJPS all have "the ransomed" at 35:10.
- The central entry's own rationale already says pāḏâ "is not governed by this entry; commentary distinguishes the two where they meet."

**Decision taken in the line:** "the ransomed of YHWH". The central diff stages a `changes.wohChoice` that rewrites only the pāḏâ sentence into a context clause: "ransom" where pāḏâ stands in parallel with gāʾal, and "redeem" elsewhere. That leaves 1:27 and 29:22 unchanged. The diff also extends appliesTo to ISA-35:9 and 35:10. claim_type stays `direct`.

**Scope:** the ruling will govern the duplicate 51:11 (with 51:10 gᵉʾûlîm), which is not yet drafted. It would also govern Jer 31:11 and Hos 13:14 if those books enter the corpus.

**Options:**
- (A) Accept the context clause (recommended).
- (B) Decline it. The orchestrator then drops the changes and rationaleAppend and reverts 35:10 to "the redeemed of YHWH", and the 35:10 commentary paragraph has to be rewritten to record the merge.
- (C) Make "ransom" the rendering of pāḏâ everywhere in Isaiah. This would revise the stable 1:27 and 29:22; it is not recommended, because ASV and the versions keep "redeem" there.

**Semver:** minor if treated like the earlier context clauses (`eretz`, `yeor-nile-egyptian-loanword`); major if any wohChoice edit counts as a modification.

## Items for the founder (recommended defaults, not blocking)

### ISA-35:7 — ḥāṣîr lᵉqāneh wāḡōmeʾ

**Line:** "grass shall become reeds and rushes". This keeps ASV's noun ("grass") and the MT vowels. It gives lᵉ the sense "become" that it has twice earlier in the same verse (laʾăḡam, lᵉmabbûʿê mayim), replacing ASV's "with", which is not a sense of lᵉ.

**Alternative:** read ḥāṣîr as "court, abode", as at 34:13 (ḥāṣîr liḇnôṯ yaʿănāh). That is the reading of JPS 1917 ("an enclosure for reeds and rushes") and NJPS. It would mirror 34:13 exactly. If the chapter 34 Editor builds on that mirror, the founder may prefer "an abode for reeds and rushes".

**Recommendation:** accept "grass shall become reeds and rushes".

### ISA-35:10 / 22:13 — joy vocabulary

śāśôn wᵉśimḥāh is "gladness and joy" here (ASV, JPS 1917), and the stable 22:13 has "joy and gladness" for the same pair. No entry fixes the book's joy vocabulary. The inconsistency is recorded in `lexical-cruxes-isaiah-35` and not changed.

**Recommendation:** leave it unless a book-wide joy entry is wanted later.

### ISA-35:7 — tannîm (coordination with chapter 34)

"jackals" matches 13:22, 43:20 and the 34:13 draft. The item sits in `lexical-cruxes-isaiah-35`. If the chapter 34 Editor creates a book-wide tannîm entry, move ISA-35:7 into it.

## Unresolved editorial questions

None.

## Decisions on the Translator's questions

1. **35:1 yᵉśuśûm.** "shall be glad"; the -m is not rendered (ASV, JPS 1917, NJPS). KJV "glad for them" is reported. → cruxes, `mt-qere-textual-policy-isaiah`.
2. **35:1 ḥăḇaṣṣeleṯ.** "the rose" is kept (ASV, JPS 1917, NJPS text). The NJPS note "Lit. crocus" was checked; NRSV and the lexica are not verified. → cruxes.
3. **35:1 desert vocabulary.** wilderness / the dry land / desert, as in ASV. ʿărāḇāh is a common noun. The 53:2 "parched ground" (ʾereṣ ṣiyyāh) is noted. → cruxes.
4. **35:2 hak-karmel.** "Carmel", a place name between Lebanon and Sharon, as in every version checked; the mountain takes the article (1 Kgs 18:19–20; Amos 1:2). "the fruitful field" stays where the context is agricultural. → cruxes.
5. **35:2 gîlaṯ wᵉrannēn.** ASV is kept; NJPS is reported. rnn is "sing/singing" throughout the chapter. → cruxes.
6. **35:4 nimhărê-lēḇ.** "those who are of a fearful heart" (ASV, JPS 1917). NJPS and the literal "hasty", with 32:4, are given in commentary. → cruxes.
7. **35:4 syntax and "do not fear".** The ASV/JPS 1917 construal is kept. The NJPS exclamation (cf. 40:9) and the accents are in commentary. "do not fear" matches 7:4, 40:9 and 43:1. The central al-tira entry is deliberately not applied. Quotation marks are added. → cruxes, `title-and-meta-conventions-isaiah`.
8. **35:6 modernised nouns.** the lame / like a deer / the mute, without the supplied "man" (wave I-4 ruling 13). → cruxes.
9. **35:7 šārāḇ.** "the glowing sand" (ASV). The other versions and the "mirage" proposal (not verified) are in commentary. → cruxes.
10. **35:7 crux.** "jackals" and "where they lay" are kept. The line is now "grass shall become reeds and rushes" (see the founder item above). 1QIsaᵃ rēḇeṣ is reported. → cruxes, `mt-qere-textual-policy-isaiah`.
11. **35:8 maslûl wāḏereḵ.** MT is kept: "a highway … and a way". The dittography deletion and NJPS are reported. → `mt-qere-textual-policy-isaiah`, cruxes.
12. **35:8 name.** "the Way of Holiness", capitalised as a called name, as at 19:18. The ASV, JPS 1917 and NJPS wordings were checked; NRSV is recalled. → cruxes.
13. **35:8 wᵉhûʾ-lāmô crux.** "but it shall be for them" (NJPS), without ASV's supplied "[the redeemed]". The athnach construal "the wayfarers, even fools, shall not go astray" is kept. The emendation "for His people" is in commentary. → cruxes.
14. **35:9 number and adverb.** ASV's "they … shall walk there" is kept. KJV's singular and NJPS's "walk it" are reported. → cruxes.
15. **35:10 pᵉḏûyê.** "the ransomed of YHWH" (founder decision above). → central goel entry (staged), cruxes.
16. **35:10 joy vocabulary.** ASV is kept, and the inconsistency with 22:13 is recorded (founder item above). → cruxes.

## Glossary changes for review

### Central glossary (4.0.0 → 4.1.0 proposed)

- Modified: `kavod-yhwh`. appliesTo +ISA-35:2; rationale addendum.
- Modified: `harbah-arbeh-doubled-infinitive-intensive`. appliesTo +ISA-35:2; rationale addendum.
- Modified: `goel-geullah-redeemer-redemption-cross-corpus`. appliesTo +ISA-35:9, 35:10. `changes.wohChoice` makes the pāḏâ sentence a context clause ("ransom" in parallel with gāʾal) and adds Isa 1:27 to its site list; rationale addendum. **Founder decision.**
- Deliberately not extended: `al-tira-fear-not-divine-encouragement-formula` (35:4).

### Per-translation overlay (3.0.0 → 3.1.0 proposed)

- Added: `lexical-cruxes-isaiah-35` (claim_type: `direct`), ISA-35:1–4 and 35:6–10.
- Modified (appliesTo, with addenda):
  - `hadar-splendor-isaiah` (+35:2)
  - `kavod-nondivine-glory-isaiah` (+35:2)
  - `elohai-elohenu-doxology-isaiah-25` (+35:2, 35:4)
  - `elohim-el-eloah-monotheistic-formula-isaiah` (+35:4)
  - `title-and-meta-conventions-isaiah` (+35:1, 35:4: title ratified, quotation marks)
  - `mt-qere-textual-policy-isaiah` (+35:1, 2, 6, 7, 8, 9, 10; MT kept, 1QIsaᵃ variants listed)

## Post-review corrections

The Reviewer returned the chapter as `awaiting-human` (reviewerReport in `chapter-35.json`). These corrections change only commentary and the wave diff files. No English line, `translation.status`, the reviewerReport block or any shared glossary was changed.

1. **35:1 ʿărāḇāh.** The 35:1 note and the `lexical-cruxes-isaiah-35` wohChoice now cite "35:6 and 40:3 (cf. 33:9)". The claim for 43:19–20 is withdrawn, because there the second noun is yᵉšîmôn. The loose "(cf. 43:19–20)" in the 35:6 note was dropped for the same reason.
2. **35:4 quotation scope.** The quotation of the whole message matches NJPS only; JPS 1917 quotes only 'Be strong, fear not'. This is corrected in the 35:4 note and in the `title-and-meta-conventions-isaiah` rationaleAppend (overlay diff).
3. **35:7 construal.** The note now cites RSV, ESV and NRSVue "the grass shall become reeds and rushes" (checked by the Reviewer on BibleGateway). "ASV's 'with' is not a sense of lᵉ" is softened to "is not the sense lᵉ has elsewhere in this verse". The same change is made in the cruxes rationale, and standardEnglish now records those versions and ESV 35:8 "the Way of Holiness".
4. **Central goel-geullah context clause** (still pending the founder's ruling):
   - The justification now rests explicitly on ASV.
   - KJV reverses the pair at Isa 51:10–11 and Jer 31:11.
   - Ps 69:19 (ASV 69:18) and Lev 27:27 are added as further paired sites, in the wohChoice parenthesis and the rationaleAppend.
   - The 35:10 note carries the same sites and the same KJV caveat.
5. **35:2 speculative note** (optional item, applied). The note now adds that the same verse uses kāḇôḏ for the glory of Lebanon, and that the reader should weigh this against the transfer.
