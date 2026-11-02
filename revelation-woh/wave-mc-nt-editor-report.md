# Wave MC (New Testament part) Editor Report: Revelation 5 and 1 Thessalonians 5

**Book / chapters:** `revelation-woh` 5 (14 verses; extends the published volume) and `1-thessalonians-woh` 5 (28 verses; new book, code `1TH-WOH`). That is 42 verses.
**Editor pass:** 2026-11-02 (claude-opus-5-5, woh-editor role).
**Status at end of pass:**
- Both chapters moved from `draft` to `editor-review`, version `0.1.0` to `1.0.0-rc1`.
- `glossaryVersion` pinned to 2.90.0 (as briefed); the central proposals are in `wave-mc-nt-central-diff.json` (2.90.0 → 2.91.0, not applied).
- `overlayGlossaryVersion`: Revelation 1.3.0; 1 Thessalonians 1.0.0 (new overlay).
- `reviewer` left `pending`. `claude-opus-5-5 (editor)` added to `modelDrafts`.

**Editorial questions:** 23 received (Rev 9, 1 Thess 14). All 23 are resolved and both arrays are empty. None needed escalation, and there are no speculative entries.

**Files written (only these)**

- `revelation-woh/chapter-5.json`
- `revelation-woh/_translation-glossary.json` (1.2.0 → 1.3.0)
- `revelation-woh/wave-mc-nt-central-diff.json` (proposed; 2.90.0 → 2.91.0)
- `1-thessalonians-woh/chapter-5.json`
- `1-thessalonians-woh/_translation-glossary.json` (new, 1.0.0)
- this report

No `_meta.json`, catalog or central glossary file was written. No git operations were run.

## Summary

- **Commentary:** Rev 5, 14 of 14 verses. 1 Thess 5, 27 of 28 verses; 5:16 ('Rejoice always') is left blank because it has no divergence and no variant.
- **Reception notes** (headed "**Wheel of Heaven reading (reception note, not a translation claim).**"): Rev 5:1 (LWTE-4:88); 1 Thess 5:3 (LWTE-4:90, full note with the canon's French and English); 1 Thess 5:1 and 5:2 (short pointers to 5:3, because the canon cites the range 5:1-3). Both canon passages were checked against `lets-welcome-the-extraterrestrials/chapter-4.json`.
- **English-line changes:** two, both in 1 Thessalonians (5:3, 5:12). Revelation 5 is unchanged.
- **Apparatus verification.** The draft marked several claims "verify against NA28". I checked them against the SBLGNT apparatus (Faithlife/SBLGNT `data/sblgntapp/text/{Rev,1Thess}.txt`). That apparatus records, for each variation unit, the readings of Westcott-Hort, Tregelles, NA28 and the Robinson-Pierpont Byzantine text. Every NA28 and "Byzantine" statement in the notes rests on it. Textus Receptus readings are inferred from the KJV wording and are labelled as such. Manuscript sigla are given only where Metzger's *Textual Commentary* is the stated source (Rev 5:9, Alexandrinus; 1 Thess 5:4, A and B). Everything else was dropped or softened, as listed below.

### Apparatus corrections to the draft questions

| Site | Draft claim | Finding (SBLGNT apparatus) | Handling |
|---|---|---|---|
| Rev 5:1 | *exōthen* in "other witnesses" | *exōthen* is the Byzantine (RP) reading. The TR has *opisthen* (KJV 'backside'). | Stated as such. |
| Rev 5:3 | (not raised) | RP adds *anō* 'above'; the KJV lacks it. | Noted. |
| Rev 5:4 | (not raised) | **NA28 omits *egō*.** SBLGNT prints it with WH, Treg and RP. | Noted; English unaffected. |
| Rev 5:5 | *ho anoigōn* in "some witnesses" | This is the RP reading. The KJV 'and to loose' reflects a TR *lysai*. | Corrected. |
| Rev 5:6 | TR *kai idou* | RP has no *kai idou*, so it is a TR reading only. RP has *echon*, *ha*, *apostellomena*. | Stated. |
| Rev 5:7 | TR *to biblion* | RP has no object, so it is a TR reading only. | Stated. |
| Rev 5:9 | Byzantine and TR *hēmas*; "some witnesses" read *hēmas* without *tō theō* | RP and Tregelles add *hēmas*; NA28 is the same as SBLGNT. The *hēmas*-without-*tō theō* claim could not be verified. | That claim is dropped. Alexandrinus is cited after Metzger. |
| Rev 5:10 | Byzantine *basileusousin* | **NA28 also reads the future.** SBLGNT's present *basileuousin* follows WH and Treg against NA28. RP also reads *basileis* 'kings'. The TR's 'us ... we shall reign' is not the Byzantine reading. | Stated. |
| Rev 5:13 | "some witnesses (TR) add *amēn*" | **Wrong.** RP adds *Amēn*; the TR/KJV does not. | Corrected. |
| Rev 5:14 | TR additions "to be verified" as absent from the Byzantine text | Confirmed: RP's only difference here is *legonta to*. | Stated as verified against RP. |
| 1 Thess 5:4 | A and B read *kleptas* | WH prints *kleptas*. The sigla rest on Metzger. | Attributed to Metzger. |
| 1 Thess 5:10 | *hyper* is the TR reading | **NA28 and RP read *hyper*.** SBLGNT's *peri* follows WH and Treg. | Stated as an NA28 divergence. |
| 1 Thess 5:13 | Sinaiticus and other witnesses read *en autois* | The apparatus shows *autois* only for Tregelles. | Witness names dropped: "Tregelles prints ...; a reading found in part of the manuscript tradition". |
| 1 Thess 5:15 | (not raised) | NA28 and RP add *kai*. | Noted. |
| 1 Thess 5:25 | P30, B and D* add *kai* | NA28 and WH print *kai*; SBLGNT, Treg and RP lack it. | Sigla dropped; editions named. |
| 1 Thess sourceText | "papyri P30 and P46 in part" | Not verifiable against NA28 here. | Softened to "the papyri P30 and P46 preserve fragments of the letter". |

## Decisions (resolution of the 23 questions)

### Revelation 5

- **5:1 *biblion* 'book' vs 'scroll'. Ruled 'book', line unchanged.** The published volume already applies a rule, stated in the 10:2 commentary: 'book' for *biblion* as a written object (1:11; 10:2, 8-10; 'the book of life' 13:8, 21:27), and 'scroll' only where the text describes the rolling (6:14 *hōs biblion helissomenon*, from Isa 34:4). Rev 5:1-9 falls under the first case, so 'book' at 5:1-9 is consistent with the published 'book' at 1:11 and 10:2 and with 'scroll' at 6:14. The 5:1 commentary states the physical form (an opisthograph roll, as in Ezek 2:9-10). The rule is now codified as overlay entry `biblion-book-scroll-rendering-revelation` (direct). The canon's French « livre » agrees, but it is recorded only in the reception note and is not the ground of the decision. The central `heavenly-tablets-...` entry stays background, under the scope rule.
- **5:2 *lysai*** keeps 'to loose' (ASV); the note gives 'break' as the sense.
- **5:5** keeps 'the Lion of the tribe of Judah, the Root of David, has conquered, so as to open'. Capitals mark the titles (ASV). 'conquered' follows the book's rendering of *nikaō* (6:2; 12:11; 13:7; 21:7). The central `yehudah-aryeh-...` entry is background.
- **5:6** keeps 'the seven spirits of God' in lower case (precedent 1:4, 4:5). The note covers the gender discord and the RP and TR readings.
- **5:7** keeps 'took it' (the object is supplied, as the ASV does with '[it]'). The note gives the perfect *eilēphen*.
- **5:8** keeps 'harp'. The note explains that the *kithara* was a lyre, and gives 'bowls' (precedent 16:1).
- **5:9** keeps 'purchased for God people from every tribe' (SBLGNT, ASV '[men]'). The Byzantine and TR *hēmas* reading is reported.
- **5:10** keeps 'a kingdom and priests ... they reign' (SBLGNT). The divergence from NA28 is stated. The central `segullah-...` entry is background: its 'a kingdom of priests' renders the Hebrew construct.
- **5:11** keeps 'ten thousand times ten thousand, and thousands of thousands' (ASV; precedent 9:16). The literal form is given in the note.
- **5:14** keeps the SBLGNT 'the elders fell down and worshiped'. The TR additions are reported as TR-only.

### 1 Thessalonians 5

- **5:1 *adelphoi*: 'brothers'** throughout (corpus precedent; the house style is the plain generic masculine). The inclusive sense is stated once, in the 5:1 note (BDAG 2a; Acts 17:4). Overlay entry `adelphoi-brothers-rendering-1-thessalonians`.
- **5:2 'the day of the Lord'** follows the ratified *kyrios* convention. The Hebrew *yôm YHWH* entries are background. Overlay entry `theos-kyrios-names-and-hebrew-scoped-entries-convention-1-thessalonians`.
- **5:3: line changed to 'Peace and security'.** See the line-change list and the founder-confirmation points below.
- **5:4** keeps 'like a thief' (SBLGNT, NA28, RP); WH's *kleptas* is reported.
- **5:5** keeps 'sons of light ... sons of the day' (ASV, literal); 'children' is given in the note.
- **5:6 and 5:10** keep the ASV: 'let us watch and be sober' and 'whether we wake or sleep'. The 'alive or dead' reading of 5:10 is explained in the note, not put in the line.
- **5:11 and 5:14** keep 'exhort' (ASV) for *parakaleō* and 'encourage' for *paramytheomai*.
- **5:12: line changed to 'to respect'.** 'are over you' is kept.
- **5:13** keeps 'among yourselves' (SBLGNT, NA28, RP).
- **5:14** keeps 'the disorderly' (ASV); the note gives the 'idle' reading (RSV, NRSV; Milligan).
- **5:19 and 5:23** keep 'the Spirit' and 'your spirit and soul and body'. Overlay entries `pneuma-spirit-capitalization-1-thessalonians` and `psyche-soul-1-thess-5-23`. **No reception note at 5:23.** The Translator pointed to LWTE-4:88 (« Il n'y a pas d'âme ... »), but that passage does not cite 1 Thess 5:23. Attaching a canon reading to an uncited verse would put the lens into the apparatus without a citation basis.
- **5:22** keeps 'every form of evil'; the KJV 'appearance' is explained as a lexical choice.
- **5:23** keeps 'coming' for *parousia*; the note covers the 'royal visit' sense (Deissmann).
- **5:27 and 5:28** keep the SBLGNT text. The Byzantine and TR *horkizō*, *hagiois* and *Amēn* are reported.

## English-line changes (Editor pass)

| refId | Draft | Now | Governing entry |
|---|---|---|---|
| 1TH-WOH-5:3 | When they are saying, "Peace and safety," then ... | When they are saying, "Peace and security," then ... | overlay `eirene-kai-asphaleia-peace-and-security-1-thess-5-3` (direct) |
| 1TH-WOH-5:12 | ... to know those who labor among you ... | ... to respect those who labor among you ... | overlay `eidenai-respect-1-thess-5-12` (direct) |

No Revelation 5 line was changed.

## Speculative entries requiring sign-off

None. All new and extended entries are `direct`.

## Founder decisions needing sign-off

None of these is blocking. They are flagged for confirmation.

1. **1 Thess 5:3 'Peace and security' (line change).** *asphaleia* supports both 'safety' and 'security' (BDAG). The rendering follows the RSV, NRSV and ESV and the *pax et securitas* reading (Koester; Weima). It now coincides with the canon's « paix » / « sécurité » and 'peace and security'. Please confirm the change, knowing that the agreement is recorded as an agreement and not as the ground of the decision. The reception note also states that the Greek reports what 'they' say and does not itself set peace against security. To revert to the ASV 'Peace and safety', replace the overlay entry.
2. **1 Thess 5:12 'to respect' (line change).** This follows BDAG's sense and the RSV and NRSV, against the ASV and KJV 'to know'. The literal 'know' is kept in the note.
3. **Rev 5 'book', not 'scroll'.** This follows the published rule at 10:2. A switch to 'scroll' would be a book-wide decision touching 1:11 and 10:2-10, and is not recommended in a single-chapter pass.
4. **1 Thess *adelphoi* 'brothers'.** This follows the house generic-masculine rule, with the inclusive sense in the commentary. NRSV 'brothers and sisters' was considered and declined.
5. **5:23 has no reception note**, for the reason given above. Confirm that the canon's statement on the soul (LWTE-4:88) should not be attached to 5:23.

## Glossary changes for review

### Central glossary (proposed in `wave-mc-nt-central-diff.json`; base 2.90.0 → recommended 2.91.0)

No new entries and no wohChoice changes. Five appliesTo-only modify ops; each `appliesTo` is the complete 2.90.0 array plus `appliesToAdded`:

- Modified: `chayyot`, + REV-WOH-5:6, 5:8, 5:11, 5:14
- Modified: `four-living-creatures-rev-4-6-8-ezek-1-chayyot-shiur-qomah-cross-corpus`, + REV-WOH-5:6, 5:8, 5:11, 5:14
- Modified: `sealed-book-dan-12-4-9-revelation-jubilees-cross-corpus`, + REV-WOH-5:1 (its rationale already names Rev 5:1 as the central reception)
- Modified: `christos-māšîaḥ-anointed-one-cross-corpus-greek-hebrew-aramaic`, + 1TH-WOH-5:9, 5:18, 5:23, 5:28
- Modified: `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus`, + 1TH-WOH-5:9, 5:18, 5:23, 5:28

The version op carries a concurrency note: re-base as the union with `appliesToAdded` if another MC diff from 2.90.0 is merged first.

These are cited as background only and not applied: `heavenly-tablets-1-enoch-81-...` (Rev 5:1), `yehudah-aryeh-...` (Rev 5:5), `segullah-mamleḵet-kohanim-...` (Rev 5:10), `daniel-7-throne-vision-...` and `jude-14-15-...` (Rev 5:11), `as-saa-the-hour-...` and `iqtaraba-...` (1 Thess 5:2, 5:23).

### Per-translation overlay: revelation-woh (1.2.0 → 1.3.0, applied)

- Added: `biblion-book-scroll-rendering-revelation` (claim_type: `direct`). Its appliesTo includes the published sites 1:11, 6:14, 10:2, 10:8-10, 13:8 and 21:27, plus 5:1-5, 5:8 and 5:9.
- Extended appliesTo: `sblgnt-base-text-variant-reporting-convention-revelation` (+5:1, 3, 4, 5, 6, 7, 9, 10, 13, 14); `theos-god-rendering-against-canon-english-yahweh-revelation` (+5:6, 9, 10); `greek-nt-proper-names-and-hebrew-scoped-entries-convention-revelation` (+5:5).
- The description now lists chapter 5 and has a v1.3.0 note.

### Per-translation overlay: 1-thessalonians-woh (new, 1.0.0)

All eight entries are `direct`:

- Added: `sblgnt-base-text-variant-reporting-convention-1-thessalonians` (keeps NA28, WH, Tregelles, Byzantine and TR apart)
- Added: `theos-kyrios-names-and-hebrew-scoped-entries-convention-1-thessalonians`
- Added: `adelphoi-brothers-rendering-1-thessalonians`
- Added: `eirene-kai-asphaleia-peace-and-security-1-thess-5-3`
- Added: `eidenai-respect-1-thess-5-12`
- Added: `pneuma-spirit-capitalization-1-thessalonians`
- Added: `psyche-soul-1-thess-5-23`
- Added: `raelian-canon-citation-reception-note-convention-1-thessalonians`

## Follow-ups for the orchestrator (files this pass was not allowed to write)

- The published Revelation chapters 1, 6, 10, 13 and 21 do not yet list `biblion-book-scroll-rendering-revelation` in `glossaryRefs` at 1:11, 6:14, 10:2, 10:8-10, 13:8 and 21:27. The overlay's appliesTo already includes them. Add the back-links on the next pass that is allowed to touch those files, or narrow the appliesTo.
- `revelation-woh/_meta.json` (chapter list) and a new `1-thessalonians-woh/_meta.json` plus catalog entry are needed before publication.
- Apply `wave-mc-nt-central-diff.json` at sign-off, then re-pin both chapters' `glossaryVersion` to 2.91.0.
