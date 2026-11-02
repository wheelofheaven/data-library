# Wave MC (Hebrew part) — Editor Report

Chapters: Leviticus 17, 25 (`leviticus-woh`, new book LEV-WOH); Numbers 11 (`numbers-woh`); Joshua 3 (`joshua-woh`); Judges 7 (`judges-woh`); 2 Samuel 6 (`2-samuel-woh`, new book 2SA-WOH); Micah 5 (`micah-woh`, new book MIC-WOH, MT numbering).
The wave has 185 verses and 63 editorial questions.
Editor pass: 2026-11-02, claude-opus-5-5.
Base: central glossary v2.90.0 (read-only); the ratified Torah, Former Prophets and Latter Prophets overlays.

## Summary

- All seven chapters are now `status: editor-review` and `version: 1.0.0-rc1`.
- `glossaryVersion` stays pinned at `2.90.0`, as instructed.
- `overlayGlossaryVersion` is `1.0.0` for leviticus-woh, 2-samuel-woh and micah-woh, and `1.1.0` for numbers-woh, joshua-woh and judges-woh.
- `editorial_questions` is empty in every chapter, and "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
- All 63 questions are resolved in glossary entries, and 15 of them are listed below for founder sign-off.
- 181 of the 185 verses have commentary.
  The four without commentary (Lev 25:19, 37, 51, 52) have no divergence and no new term.
- 10 English lines were changed. Each change is backed by an overlay or central entry (see the line-change table below).
- Eight verses carry a separately headed reception note ("Wheel of Heaven reading (reception note, not a translation claim)"): Lev 17:11; 25:8; Num 11:7; Josh 3:15; Judg 7:22; 2 Sam 6:6; Mic 5:1, 5:4.
  No English line uses lens vocabulary.
- Every glossaryRef resolves to a central id, an overlay id of the same book, or the proposed new central id.
- Every backticked id in a note is also in that verse's glossaryRefs.
- The shared Former Prophets set is identical (text and appliesTo) in the joshua-woh, judges-woh, 1-samuel-woh and 2-samuel-woh overlays.

## Speculative entries requiring sign-off

None.
Every new overlay entry and the new central entry are `direct`.
The canon readings (the 49-year lease, the soul as genetic code, manna as a chemical food, the repelling ray at the Jordan, ultrasound at Judges 7, electrocution at the ark, the Messiah) appear only in the eight labelled reception notes.

## Founder decisions (sign-off requested)

1. **Lev 17:10-15, *nep̄eš*** (`nefesh-blood-life-leviticus-17`).
   One word is rendered three ways in six verses:
   - 'nefesh' at v 10 (central `karet-penalty-cut-off-from-people`);
   - 'life' / 'lives' at vv 11 and 14 (central `basar-b-nafsho-damo`, as Gen 9:4);
   - 'person' at vv 12 and 15 (`nefesh-scope-torah`).

   The note at v 10 sets out the sequence, and every site names *nep̄eš*.
   'soul' (the ASV and the canon) is not used.
   The v 11 reception note reports the canon's 'soul' = genetic code reading.
   It also observes that the canon's rejection of an ethereal soul and the line's 'life' both refuse the dualist sense.
   **Recommendation: ship.**
   The alternative is 'nefesh' at vv 10, 11 and 14, which keeps one word through the equation but breaks the Gen 9:4 rendering.
2. **Judg 7, 'shofars' against the ASV's and the canon's 'trumpets'** (central `shofar-rams-horn-signal-instrument-cross-corpus`).
   The central rule is applied at all six sites.
   The difference from the canon is stated in the line note at 7:22, and the canon's ultrasound reading is in the reception note there.
   **Recommendation: ship.**
3. **Lev 25, *yôḇēl* 'jubilee', not 'ram's horn'** (`shofar-teruah-yovel-deror-jubilee-leviticus-25`; a jubilee clause is proposed for the central shofar entry).
   Here *yôḇēl* names the year, and the central entry already derives that sense from the horn.
   'jubilee' is lower case.
   The same entry renders *šôp̄ar tərûʿâ* 'a shofar blast' (25:9, a line change) and capitalises 'the Day of Atonement' (a line change).
   **Recommendation: ship.**
4. **Mic 5:4, 'And this one shall be peace'** (`zeh-shalom-this-one-shall-be-peace-micah-5-4`).
   The line has no supplied words.
   'this one' keeps the masculine demonstrative open between the ruler and the situation he brings about.
   The ASV prints 'this [man] shall be [our] peace', and the canon 'this man shall be the Peace'.
   **Recommendation: ship.**
5. **Num 11, *rûaḥ*: lower-case 'spirit'** (`ruach-spirit-on-the-elders-numbers-11`).
   This is the Torah practice, as genesis-woh 41:38 prints it.
   The Kings / Former Prophets 'ruach' is not adopted, although 2 Kgs 2:9, 15 ('the ruach of Eliyahu rests on Elisha') is the nearest parallel.
   11:31 *rûaḥ* is 'wind'.
   This adds a fourth instance to the existing corpus split ('ruach' in Kings, Ezekiel and the Former Prophets; 'spirit' in the Torah, Isaiah and the Latter Prophets).
   **Recommendation: ship.** Keep the split on the founder's harmonisation list.
6. **Josh 3:10, 'the living El'** (new clause 8 of the shared `elohim-referent-and-article-conventions-former-prophets`).
   Bare *ʾēl* is transliterated as in the Torah overlays and the central El-compounds.
   The determiner follows clause 7.
   'God' would merge *ʾēl ḥay* with the *ʾĕlōhîm ḥayyîm* of 1 Sam 17:26.
   **Recommendation: ship.**
7. **Lev 17, 25: *gēr* 'sojourner', *tôšāḇ* 'resident'** (`ger-toshav-sojourner-resident-leviticus-25`; central `megurim-patriarchal-sojourner-self-identity-gur-root`).
   Lev 25:23 reads 'sojourners and residents' (ASV 'strangers and sojourners'; canon 'guests and residents').
   Corpus conflict: the published genesis-woh 23:4 has the ASV pair 'a stranger and a sojourner' for the same *gēr wəṯôšāḇ*.
   **Recommendation: ship.** Harmonise Gen 23:4 at the next Genesis pass ('a sojourner and a resident').
8. **Ketiv/Qere.** The Qere is translated at all five sites, and the Ketiv is recorded in the commentary:
   - Lev 25:30, under the Torah `mt-baseline-ketiv-qere-and-accent-division-torah`;
   - Josh 3:4 and 3:16, under the shared `ketiv-qere-qere-translated-former-prophets`;
   - Judg 7:13 and 7:21, under the same entry.

   The ASV follows the Ketiv at Josh 3:16 ('at Adam') and Judg 7:21 ('put [them] to flight'), so the line departs from it there.
   **Recommendation: confirm.**
9. **Lev 25, *ʿeḇeḏ*** (`eved-amah-slave-servant-leviticus-25`).
   Owned persons are 'slave' / 'female slave' (vv 6, 39, 42b, 44).
   YHWH's claim is 'servants' (vv 42a, 55).
   The wordplay is stated in the notes at vv 39, 42 and 55.
   v 6 changes from 'male servant ... maidservant' to 'male slave ... female slave', to match v 44 (same Hebrew; NRSV).
   **Recommendation: ship.** The alternative is Alter's 'my slaves' at vv 42 and 55, which keeps one English word but breaks the corpus 'servant of YHWH'.
10. **Lev 17:7, 'goat-demons ... after whom they prostitute themselves'** (`seirim-goat-demons-leviticus-17-7`; line change).
    The ASV has 'he-goats ... play the harlot'.
    NRSV, NJPS and HALOT all read the cult sense.
    **Recommendation: ship.**
11. **Mic 5:3, 5, 'shepherd'** (`lexical-cruxes-micah-5`; two line changes).
    At 5:3 the ASV supplies an object, 'feed [his flock]', and the canon has 'feed'.
    At 5:5 the ASV has 'waste', from *rāʿaʿ*, while the MT vocalisation is that of *rāʿâ*.
    Mic 5:6 changes 'the children of men' to 'the sons of human' (central `ben-adam`, the corpus rendering of anarthrous *bənê ʾāḏām*, as proverbs-woh 8:4, 31).
    **Recommendation: ship.**
12. **Num 11:28, 'the attendant of Moses from his youth'** (`lexical-cruxes-numbers-11`; line change).
    The MT pointing is the abstract plural *bəḥurîm* 'youth' (BDB; NJPS).
    The ASV has 'one of his chosen men'.
    **Recommendation: ship.**
13. **Judg 7:20 and 7:25** (`lexical-cruxes-judges-7`; two line changes).
    7:20 now reads 'A sword for YHWH and for Gid'on!', with the same *lə-* as the watchword of 7:18 (NRSV, NJPS; ASV 'The sword of Jehovah and of Gideon').
    7:25 now reads 'captains' for *śārê* (ASV 'princes'), as the corpus 'captain of the host'.
    **Recommendation: ship.**
14. **2 Sam 6:2, 'who is enthroned on the cherubim'** (`yoshev-hakkeruvim-enthroned-on-the-cherubim-2-samuel-6-2`; line change).
    The draft had 'who dwells on', from central `shakhan-dwell-divine-presence-verb-cross-corpus`, whose 'dwell' rule was written for the residence sense of 1 Kgs 8.
    *yōšēḇ hakkəruḇîm* is a throne title (NRSV, NJPS), and the central aron rationale already calls the ark 'enthroned above the cherubim'.
    The shakhan glossaryRef is removed from 2SA-WOH-6:2.
    **Recommendation: ship.**
15. **New central entry `goel-geullah-redeemer-redemption-cross-corpus`.**
    One root, 'redeem / redeemer / redemption', for *gʾl*.
    Lev 25:25 now reads 'his redeemer who is nearest to him' (draft wording kept; NJPS 'his nearest redeemer'; ASV 'kinsman').
    The entry's appliesTo also lists the published gʾl sites:
    - Isa 43:1, 14; 44:6, 22-24; 48:17, 20; 54:5, 8;
    - Ps 19:15;
    - Ezek 11:15 ('the men of your kindred').

    Those chapters already print these renderings but do not yet cite the id.
    *pāḏâ* 'redeem' (Ex 13; Num 18; 1 Kgs 1:29; Isa 29:22) is explicitly excluded.
    **Recommendation: approve the promotion.**

Applied without change, as ratified (not reopened):
- 'Aharon' (as published; the brief's 'Aaron' was not used);
- Torah 'Moses' / 'Mitsrayim' / 'Canaan';
- the Former Prophets transliteration with '-ite' gentilics, including 'Moshe' in Josh 3:7;
- 'the Elohim' only with the Hebrew article, plus the central narrative rule;
- Micah's 'God', English names, 'declares YHWH', and no quotation marks for the oracle;
- 'earth' / 'land' by scope;
- *tərûmâ*, *tôrâ* and *ḥērem* (none occurs in these chapters).

## Unresolved editorial questions

None. Each of the 63 questions is resolved as follows.

- **Book-level conventions** (LEV-WOH-17:1, 25:1; 2SA-WOH-6:1; MIC-WOH-5:1).
  Option A: new overlays carry the family conventions.
  - leviticus-woh carries the five Torah conventions, with text identical to the numbers-woh / exodus-woh / deuteronomy-woh copies and LEV refIds in appliesTo.
  - 2-samuel-woh carries the nine Former Prophets conventions, shared verbatim with joshua-woh, judges-woh and 1-samuel-woh.
  - micah-woh carries the twelve Latter-Prophets conventions, with the text of the amos / jeremiah / jonah / zephaniah / zechariah copies.
- **Lev 17.**
  - 17:7: 'goat-demons'; 'prostitute themselves' (decision 10).
  - 17:10, 17:11: nefesh / life (decision 1).
  - 17:11: 'by reason of the life' kept (ASV). The NJPS *bet essentiae* and the *bet pretii* / ransom readings (Schwartz 1991; Milgrom AB 3A) are in the note.
  - 17:14: MT 'its blood is with its life'. The Samaritan / LXX shorter text is in the note.
- **Lev 25.**
  - 25:2: 'Sabbath' capitalised; 'a Sabbath of solemn rest' (ASV); 'the Day of Atonement' capitalised. Exodus 16:23 'Sabbath observance' is to be reconciled later.
  - 25:6 and 25:23: decision 7.
  - 25:8, 25:14, 25:23 (canon quotes): lines kept, with one reception note at 25:8 and pointers at 14 and 23.
  - 25:9: 'a shofar blast'.
  - 25:10: 'jubilee', 'liberty'.
  - 25:14: 'crops' for the count plural in vv 15-16, 'produce' elsewhere.
  - 25:25: 'redeemer' (decision 15).
  - 25:30: Qere.
  - 25:33: MT in the ASV construal; NJPS and the Vulgate negative reported.
  - 25:34: 'open land'.
  - 25:39: decision 9.
- **Num 11.**
  - 11:3: 'Tav'erah (Burning)', 'Qivrot-haTa'avah (Graves of Craving)' under the Torah causal-clause rule.
  - 11:6: 'appetite'.
  - 11:7: reception note (the manna entry's disavowal iii applies).
  - 11:8: 'fresh oil' kept; LXX, NJPS and the canon in the note.
  - 11:15: MT, with the tiqqun reported (central tiqqun entry cited).
  - 11:16: 'seventy' (the central 'threescore and ten' is Genesis-scoped) and 'present themselves' (central mit'yatzev).
  - 11:17: decision 5.
  - 11:25: MT 'did not do so again'.
  - 11:28: decision 12; 'restrain'.
  - 11:31: 'ground' (central eretz ground clause).
  - 11:33: 'chewed' (ASV).
- **Josh 3.**
  - 3:1: forms as drafted; the Torah 'Avel-haShittim' noted.
  - 3:4: Qere.
  - 3:10: decision 6.
  - 3:11: the ASV construct reading, with the apposition reading and the article anomaly of vv 14 and 17 recorded under the MT-baseline entry; 'earth' (universal-formula clause proposed for central eretz).
  - 3:15: reception note; nēḏ 'heap' (`ned-echad-waters-stand-in-one-heap-joshua-3`).
  - 3:16: Qere (decision 8).
- **Judg 7.**
  - 7:1: forms as drafted, with descriptive toponyms translated.
  - 7:3, 7:6, 7:8: MT.
  - 7:5: no break in the English line (central piska cited).
  - 7:13, 7:21: Qere.
  - 7:14: clause 1 'the Elohim', with the reason added to the shared entry.
  - 7:15: 'bowed down' (central hishtachavah).
  - 7:20: decision 13.
  - 7:22: decision 2.
- **2 Sam 6.**
  - 6:1: 'again gathered'.
  - 6:2: MT, with the doubled *šēm* kept; 'enthroned' (decision 14).
  - 6:4: MT.
  - 6:5: MT 'instruments of fir-wood' and the ASV instrument names, which match psalms-woh 33:2.
  - 6:6: 'reached out', with nothing supplied; 'stumbled'.
  - 6:7: 'for his error'.
  - 6:8: 'Peretz-Uzzah' unglossed; 'displeased'.
  - 6:19: 'a portion of meat'.
  - 6:22: MT.
- **Mic 5.**
  - 5:1: MT numbering (`mt-versification-micah-5`); 'thousands', 'from everlasting'.
  - 5:3: 'shepherd'.
  - 5:4: decision 4.
  - 5:5: 'shepherd'; MT 'in its entrances'.
  - 5:9: 'declares YHWH'.
  - 5:12: 'bow down', 'carved images', 'pillars'.
  - 5:13: MT 'cities'.

## English-line changes

| refId | Draft | Now | Governing entry |
|---|---|---|---|
| LEV-WOH-17:7 | to the he-goats, after which they play the harlot | to the goat-demons, after whom they prostitute themselves | `seirim-goat-demons-leviticus-17-7` |
| LEV-WOH-25:6 | your male servant ... your maidservant | your male slave ... your female slave | `eved-amah-slave-servant-leviticus-25` |
| LEV-WOH-25:9 | the shofar of the blast ... the day of atonement | a shofar blast ... the Day of Atonement | `shofar-teruah-yovel-deror-jubilee-leviticus-25` |
| NUM-WOH-11:28 | the attendant of Moses, one of his chosen men | the attendant of Moses from his youth | `lexical-cruxes-numbers-11` |
| JDG-WOH-7:20 | "The sword of YHWH and of Gid'on!" | "A sword for YHWH and for Gid'on!" | `lexical-cruxes-judges-7` |
| JDG-WOH-7:25 | the two princes of Midyan | the two captains of Midyan | `lexical-cruxes-judges-7` |
| 2SA-WOH-6:2 | who dwells on the cherubim | who is enthroned on the cherubim | `yoshev-hakkeruvim-enthroned-on-the-cherubim-2-samuel-6-2` |
| MIC-WOH-5:3 | stand and feed | stand and shepherd | `lexical-cruxes-micah-5` |
| MIC-WOH-5:5 | they shall waste the land of Assyria | they shall shepherd the land of Assyria | `lexical-cruxes-micah-5` |
| MIC-WOH-5:6 | the children of men | the sons of human | central `ben-adam`; `lexical-cruxes-micah-5` |

## Glossary changes for review

### Central glossary (proposal: `leviticus-woh/wave-mc-he-central-diff.json`, 2.90.0 → 2.93.0)

- Added: `goel-geullah-redeemer-redemption-cross-corpus` (claim_type: `direct`).
- Modified (clause appended to wohChoice, existing text unchanged, plus appliesTo):
  - `eretz`: universal-formula clause for 'the Lord of all the earth' (Josh 3:11, 13).
  - `shofar-rams-horn-signal-instrument-cross-corpus`: jubilee clause (Lev 25), plus the Judg 7 and 2 Sam 6 sites.
- appliesTo-only extensions (38 ids), each with `appliesToAdded`: achuzzah, ad-ha-yom-ha-zeh, al-ken-qara-shemah, amalek, aron (+21), avon, basar-b-nafsho-damo, be-yedkhem-nittanu, ben-adam, cherubim-ezek, chinnam, elohim-as-translation (+14), elohim-imkha, esh-yhwh, har-sinai, hishtachavah, hithpallel, karet, mannah, matza-chen, matzevah, megurim, mit'yatzev-al-YHWH, mitsrayim, navi-first-occurrence-abraham, nimrod-gibbor, olah, peretz-breach, pesel, piska, qorbanot, reach-hannichoach, she-erit, tiqun-soferim, vayered-yhwh, yad-yhwh, yirat-elohim, zonah.
- The version note explains the 2.93.0 numbering: the NT wave-MC diff targets 2.91.0.
  It also gives the re-base rule (union with `appliesToAdded`).

### Per-translation overlays

- **leviticus-woh v1.0.0 (new):**
  - Torah conventions copied with identical text: names, quotation marks, MT baseline / Ketiv-Qere, Elohim referent, nefesh scope.
  - Added (all `direct`): `nefesh-blood-life-leviticus-17`, `seirim-goat-demons-leviticus-17-7`, `shofar-teruah-yovel-deror-jubilee-leviticus-25`, `ger-toshav-sojourner-resident-leviticus-25`, `eved-amah-slave-servant-leviticus-25`, `lexical-cruxes-leviticus-25`.
- **numbers-woh v1.1.0:**
  - The Torah conventions keep their text, and their appliesTo gains Num 11.
  - Added (`direct`): `ruach-spirit-on-the-elders-numbers-11`, `lexical-cruxes-numbers-11`.
- **joshua-woh, judges-woh, 1-samuel-woh v1.1.0, and 2-samuel-woh v1.0.0 (new): shared Former Prophets set.**
  The set is modified identically in all four overlays.
  - Names table: Josh 3, Judg 7, 2 Sam 6 forms added.
  - Elohim referent: wave sites added, and new clause 8 'the living El'.
  - Ketiv/Qere: 4 sites added.
  - MT baseline: wave sites added, with the 4QSamᵃ paragraph.
  - YHWH of hosts: 2 Sam 6:2, 18 added.
  - Ba'al: Judg 7:1 added.
  - The "shared by three" sentence now reads "four".

  Book entries added (`direct`):
  - joshua-woh: `ned-echad-waters-stand-in-one-heap-joshua-3`;
  - judges-woh: `lexical-cruxes-judges-7`;
  - 2-samuel-woh: `yoshev-hakkeruvim-enthroned-on-the-cherubim-2-samuel-6-2`, `lexical-cruxes-2-samuel-6`.

  The 1-samuel-woh copy is updated only to keep the set identical.
  Its chapters still pin overlay 1.0.0.
- **micah-woh v1.0.0 (new):**
  - The twelve Latter-Prophets conventions are copied, and their text is verified identical to the amos-woh copy.
  - Their appliesTo is the five-book union plus MIC-WOH-5:1, 5:3, 5:5, 5:9 and 5:13.
  - Added (`direct`): `mt-versification-micah-5`, `zeh-shalom-this-one-shall-be-peace-micah-5-4`, `lexical-cruxes-micah-5`.

## Orchestrator follow-ups (not done here; outside the files I was allowed to touch)

1. Add the Micah refIds (MIC-WOH-5:1, 5:3, 5:5, 5:9, 5:13) to the five other Latter-Prophets overlay copies.
   Those copies are amos-woh, jeremiah-woh, jonah-woh, zephaniah-woh and zechariah-woh.
   This makes the shared set identical in all six overlays again.
2. Add 'Tav'erah = Taberah' to the shared Torah name table at the next Torah overlay extension.
   It is recorded in `lexical-cruxes-numbers-11` so as not to break text identity now.
3. Corpus harmonisations to schedule:
   - exodus-woh 16:23 *šabbāṯôn* 'a Sabbath observance', against Lev 25:4-5 'solemn rest';
   - genesis-woh 23:4 *gēr wəṯôšāḇ* (decision 7);
   - the ruach split (decision 5).
4. The hosted reference for Micah (`data-library/micah/`) is the World English Bible in English numbering, not the ASV.
   The printed ASV (1901) was used for comparison.
   This is a library note, as for Jonah.
5. The published Isaiah 43, 44, 48 and 54, psalms-woh 19 and ezekiel-woh 11 could add `goel-geullah-redeemer-redemption-cross-corpus` to their glossaryRefs once the central entry is applied.
6. Bump the chapters' `glossaryVersion` from 2.90.0 at sign-off if house practice requires; they were pinned at 2.90.0 as instructed.
7. No `_meta.json` or catalog entries were created for the three new books.
