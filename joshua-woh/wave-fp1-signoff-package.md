# Canon-cited program — former-prophets — human sign-off package

| Chapter | Verses | Approve | Revise | Flag |
|---|---|---|---|---|
| Joshua 5 — Circumcision at Gilgal and the captain of the host of YHWH before Yericho (Jericho) | 15 | 15 | 0 | 0 |
| Joshua 6 — The fall of Yericho (Jericho) | 27 | 27 | 0 | 0 |
| Joshua 10 — Great stones from the skies and the sun standing still at Giv'on (Gibeon) | 43 | 43 | 0 | 0 |
| Judges 6 — The call of Gid'on (Gideon): the fire from the rock and the fleece | 40 | 39 | 1 | 0 |
| Judges 13 — The messenger of YHWH and the birth of Shimshon (Samson) | 25 | 25 | 0 | 0 |
| 1 Samuel 3 — YHWH calls Shemu'el (Samuel) | 21 | 21 | 0 | 0 |
| 1 Samuel 5 — The ark of the Elohim among the Pelishtim (Philistines) | 12 | 12 | 0 | 0 |
| 1 Samuel 6 — The ark returned from the Pelishtim (Philistines) to Beit-Shemesh (Beth-shemesh) | 21 | 21 | 0 | 0 |
| 1 Samuel 17 — David and Golyat (Goliath) | 58 | 58 | 0 | 0 |

See the combined summary `canon-cited-final-signoff-summary.md` for decisions and fixes.

---

## Editor report (inlined)

# Former Prophets wave 1 — Editor Report

Chapters: Joshua 5, 6, 10 (`joshua-woh`); Judges 6, 13 (`judges-woh`); 1 Samuel 3, 5, 6, 17 (`1-samuel-woh`).
These are three new books. The wave has 262 verses and 79 editorial questions.
Editor pass: 2026-11-01, claude-opus-5-5.
Base: central glossary v2.83.0 (read-only) and the founder-ratified Kings overlays (1-kings-woh v1.2.0, read-only).

All nine chapters are now `status: editor-review`, `version: 1.0.0-rc1`, `glossaryVersion: 2.84.0` (the target of the central diff) and `overlayGlossaryVersion: 1.0.0`.
`editorial_questions` is empty, and "claude-opus-5-5 (editor)" has been added to `modelDrafts`.
220 of the 262 verses have commentary.
The 42 verses without commentary have no divergence and no new name.
14 verses carry a separately headed reception note.

## Speculative entries requiring sign-off

None.
Every new entry is `direct` except the shared `ruach-yhwh-transliteration-former-prophets`, which is `inferred`, as is its ratified Kings source.
No English line uses lens vocabulary.
The canon readings (a military adviser, an ultrasonic device, a bombardment, a feeding tube, telepathy, a transmitter in the ark, radiation) appear only in the 14 labelled reception notes:
Josh 5:14; 6:5; 10:11, 13; Judg 6:21; 13:3, 5, 9; 1 Sam 3:9, 10; 5:3, 6; 6:19; 17:26.

## Founder decisions

1. **1 Sam 6:18 — the only departure from the MT in the wave** (`even-ha-gedolah-the-great-stone-1-samuel-6-18`, 1-samuel-woh).
   The MT has *ʾāḇēl* ('meadow', masculine).
   It does not agree with the feminine *haggəḏôlâ* or with the feminine *ʿāleyhā*, and it contradicts vv 14-15, so it cannot be construed.
   The line reads 'the great stone', with *ʾeḇen* from many Hebrew manuscripts, the LXX and the Targum, which the ASV, NRSV and NJPS also follow.
   This creates a narrow exception to the ratified MT-baseline rule: the MT is set aside only where it is grammatically impossible and a Hebrew-manuscript reading supported by the versions restores the grammar.
   **Recommendation: ship.**
   The alternative is the MT reading 'unto Avel-ha-Gedolah (the great meadow)', with the problem explained in commentary.
2. **Gentilics across the corpus.**
   This wave applies the Kings '-ite' rule: 'the Emorites', 'the Kena'anites', 'the Ashdodites', 'the Eqronites', 'the Pelishtite'.
   The corpus is not uniform:
   - genesis-woh writes 'the Emori', 'the Kena'ani' (central `ten-nations-of-canaan`);
   - exodus-woh writes 'the Amorite', 'the Canaanite';
   - the plural 'Pelishtim' follows central `pelishtim-caphtor`, so the singular *happəlištî* ('the Pelishtite', about 30 times in 1 Sam 17) and the plural differ in form.

   **Recommendation:** keep the Kings rule for the Former Prophets and plan one mechanical pass over the corpus later.
   Founder choices: (a) the '-ite' rule everywhere ('the Pelishtites' for the plural too); (b) transliterated '-i' / '-im' everywhere ('the Pelishti', 'the Emori'); (c) the status quo.
3. **Judg 6:40, anarthrous *ʾĕlōhîm* as a narrative subject.**
   The orchestrator's brief and the draft question paraphrase the Kings rule as "'the Elohim' only where the Hebrew has the article".
   The ratified Kings entry does not say that.
   It states that "the narrative-subject article rule of the central entry is unaffected", and its article-less clause covers only predicates, genitives and subjects in direct speech.
   So I applied the Kings entry exactly: 'And the Elohim did so'.
   The new clause 6 of `elohim-referent-and-article-conventions-former-prophets` records this.
   There is no conflict with central `elohim-as-translation`.
   **Please confirm.**
   If the founder prefers 'And Elohim did so', change clause 6 and one line.
4. **Judg 6:34, 'the ruach of YHWH clothed Gid'on'.**
   The noun follows the ratified Kings transliteration, as the brief directs.
   The verb *lāḇəšâ* is now rendered literally ('clothed'; ASV 'came upon'), so that the distinct verbs Judges uses for the *rûaḥ YHWH* stay distinct.
   At 13:25 the ASV 'began to move him' is kept.
   **Recommendation: ship.**
5. **ḥērem in Joshua** (`herem-devoted-devote-to-destruction-joshua`).
   The noun is always 'devoted' / 'the devoted thing', and the Hiphil verb is always 'devote to destruction' (NRSV at 6:21).
   This replaces the ASV's mix of 'utterly destroyed' and 'accursed' in 8 lines.
   The rendering shows on the surface that the Josh 10 refrain carries out the *ḥērem*.
   It is lexical, but the conquest texts are morally weighted, so I am flagging it.
   **Recommendation: ship.**
6. **Promotion of 'shofar' to central** (`shofar-rams-horn-signal-instrument-cross-corpus`).
   The 1-kings-woh entry `shofar-coronation-signal-1-kings-1` names a third book as the trigger for promotion; Joshua and Judges are the third and fourth.
   Once the central entry is applied, the Kings overlay entry should be retired or reduced to a pointer.
   That is an orchestrator edit; I did not touch the Kings files.

## Unresolved editorial questions

None.
All 79 questions are resolved, either into a glossary entry or by applying an existing one.
The resolutions:

| Chapter | Question → resolution |
|---|---|
| Josh 5 | Q0 conventions → three overlays created, shared Kings conventions mirrored and cited; gentilics, see founder point 2. Q1 5:1 K/Q → Qere 'they'. Q2 5:3 → 'the hill of the foreskins' (names entry). Q3 5:14 title → 'the captain of the host of YHWH' (`sar-tzeva-yhwh-...`). Q4 5:14 → MT *lōʾ*, two clauses (MT entry). Q5 *wayyištāḥû* → 'bowed down' (central hishtachavah clause; **line changed**). |
| Josh 6 | Q0 → overlays. Q1 → 'shofar(s) of rams' horns', 'the ram's horn' (central shofar). Q2, Q4, Q5, Q6 K/Q → Qere. Q3 → ASV 'shout with a great shout' / 'fall down flat' (`teruah-...`). Q5, Q9 → subject left unexpressed, MT order (MT entry). Q7 ḥērem → consistent rendering (`herem-...`; **lines 6:18, 6:21 changed**). Q8 6:18 → MT *taḥărîmû*. Q10 6:26 → ASV 'with the loss of'; LXX plus not translated. |
| Josh 10 | Q0 → overlays; 'Azzah', 'the Negev'. Q1 10:10 → MT subject YHWH. Q2 10:11 → 'great stones from the skies ... hailstones' (`avne-barad-...`, central shamayim). Q3 10:12 → 'stand still' / 'stayed', prose layout (`shemesh-dom-...`). Q4 10:13 → 'the Book of Yashar' (`sefer-hayyashar-...`), 'skies'. Q5 10:15, 43 → MT translated. Q6 10:24 → ordinary verb (MT entry). Q7 → 'every person' (nefesh entry). ḥērem verb **changed in 10:1, 28, 35, 37, 39, 40**. |
| Judg 6 | Q0 → overlays. Q1 *miḥyâ* → 'sustenance' + central michyah clause. Q2 K/Q → Qere. Q3 → 'oak', as Kings 1 Kgs 13:14. Q4 → MT vocalizations and subject. Q5 → 'my present' (central minchah-tribute). Q6 → ASV wording (`mishenet-...`). Q7 → 'Forasmuch as' + piska. Q8 → 'YHWH-Shalom' (names entry). Q9 → one bull (ASV), alternatives in commentary. Q10 → 'the Asherah' (names entry). Q11 → 'in the orderly manner' (ASV). Q12 → 'the ruach of YHWH clothed' (ruach entry; **line changed**). Q13 → 'the Elohim' (elohim clause 6; founder point 3). |
| Judg 13 | Q0 → overlays. Q1 → 'you shall conceive' at vv 3, 5, 7 (`harah-...`). Q2 → 'a Nazirite to Elohim' (`nezir-elohim-...`). Q3 → 'The man of the Elohim' (ish entry). Q4 → ASV. Q5 K/Q → Qere 'your word'. Q6 → 'wonderful' (`peli-...`). Q7 → 'and he did wondrously', subject unexpressed. Q8 → 'toward the skies' (direction of the flame) / 'went up' (central `va-yaal-elohim-...` now cited). Q9 → 'we have seen Elohim' (clause 2; as genesis-woh Gen 32:31). Q10 → 'the ruach of YHWH began to move him' (**line changed**). |
| 1 Sam 3 | Q0 → overlays. Q1 → 'rare ... no widespread vision' (`yaqar-chazon-nifratz-...`; **line changed**). Q2 K/Q → Qere. Q3 → 'came and stood' (ASV). Q4 3:13 → MT (tiqqun soferim noted). |
| 1 Sam 5 | Q0 → overlays; new central `dagon-philistine-deity-hebrew-bible-cross-corpus`. Q1 5:4 → MT, no supplement. Q2 → 'tumors' (Qere; `ofalim-tehorim-...`). Q3 → 'lords' (`seranim-...`). Q4 5:12 → 'heavens' (register clause). |
| 1 Sam 6 | Q0 → overlays; 'guilt-offering' (central qorbanot). Q1 → 'tumors'. Q2 → 'mice' (ASV), with commentary. Q3 → 'made sport of' (`hitallel-made-sport-of-1-samuel-6-6`; **line changed**). Q4 → 'the great stone' (founder point 1). Q5 → MT 'seventy men, fifty thousand men', 'looked into'. |
| 1 Sam 17 | Q0 → overlays. Q1 → 'champion' (ASV). Q2 → MT 'six cubits and a span'; LXX / 4QSamᵃ / Josephus 'four' in commentary. Q3 → 'scale mail' / 'javelin'. Q4, Q8 K/Q → Qere. Q5 → 'the Pelishtite' (founder point 2). Q6 → full MT unmarked; 'advanced among men'. Q7 → 'the place of the wagons'; ASV placeholder → follow-up. Q9 → 'the armies of the living Elohim' (new elohim clause 7). Q10 → ASV 'Is there not a cause?'. Q11 → MT 'no man's heart'. Q12 → MT 'Gai'. |

**English-line changes (13 lines, each backed by a glossary entry):**
- Josh 5:14 ('bowed down');
- Josh 6:18, 6:21 and 10:1, 28, 35, 37, 39, 40 (*ḥērem*);
- Judg 6:34, 13:25 ('ruach');
- 1 Sam 3:1 ('rare ... widespread');
- 1 Sam 6:6 ('made sport of').

All other lines are the Translator's.

## Glossary changes for review

### Central glossary

All central changes are in the proposal file `joshua-woh/wave-fp1-central-diff.json` (base 2.83.0 → recommended 2.84.0, minor).
Every modify op carries the complete appliesTo array plus `appliesToAdded`.
The parallel Torah and Isaiah diffs also target 2.83.0, so shared arrays (elohim-as-translation, shamayim, eretz, malakh-yhwh-messenger, olah ...) must be merged as unions.

Added:
- `shofar-rams-horn-signal-instrument-cross-corpus` (claim_type: `direct`).
  It is promoted from the 1-kings-woh overlay.
  Its Exodus refIds (EXO-WOH-19:16, 19; 20:18) are taken from the Kings entry and need checking against the exodus-woh numbering, which I did not read.
- `aron-ark-of-the-covenant-ark-of-the-elohim-cross-corpus` (claim_type: `direct`).
  Exodus 25 is in the parallel Torah wave, so this is a real collision risk: merge it with any ʾărôn entry the Exodus Editor creates.
- `dagon-philistine-deity-hebrew-bible-cross-corpus` (claim_type: `direct`).
  The Ugaritic `dagan-dagon-...` entry asks for this Hebrew sibling.

Modified:
- `hishtachavah-bow-down-obeisance-worship`.
  Was: 'made obeisance' (Yosef cycle).
  Now: the same, plus a Former Prophets clause, 'bowed down'.
  appliesTo + JOS-WOH-5:14 and the Kings 'bowed down' sites.
  Reason: brief ruling 3, aligning with the published Kings practice.
- `michyah-preservation-of-life-rare-noun`.
  Adds a Judg 6:4 'sustenance' clause, which the rationale already describes.
- `dagan-dagon-grain-deity-...`.
  One back-reference sentence appended to the rationale.
- appliesTo-only extensions for 43 central ids applied in the wave.

Removed citations:
- `va-yivez-esav-...` at 1 Sam 17:42 (a Genesis-specific entry);
- `eretz` at 10 verses where ʾereṣ is 'ground' or 'earth', not 'land'.

### Per-translation overlays (new, v1.0.0)

Shared verbatim in `joshua-woh`, `judges-woh` and `1-samuel-woh`, applying the ratified Kings entries of the same names:

- Added: `hebrew-proper-name-transliteration-convention-former-prophets` (claim_type: `direct`)
- Added: `elohim-referent-and-article-conventions-former-prophets` (claim_type: `direct`; new clauses 6 and 7)
- Added: `ish-ha-elohim-man-of-the-elohim-prophetic-title-former-prophets` (claim_type: `direct`)
- Added: `nefesh-scope-and-spelling-former-prophets` (claim_type: `direct`)
- Added: `ruach-yhwh-transliteration-former-prophets` (claim_type: `inferred`)
- Added: `ketiv-qere-qere-translated-former-prophets` (claim_type: `direct`; 15 readings)
- Added: `mt-baseline-at-versional-cruxes-former-prophets` (claim_type: `direct`)
- Added: `yhwh-tsevaot-yhwh-of-hosts-former-prophets` (claim_type: `direct`)
- Added: `habbaal-baal-hebrew-bible-rendering-former-prophets` (claim_type: `direct`)

The Kings `gahar` and `torah` entries have no sites in this wave and are not mirrored.

joshua-woh:
- Added: `sar-tzeva-yhwh-captain-of-the-host-of-yhwh-joshua-5` (claim_type: `direct`)
- Added: `herem-devoted-devote-to-destruction-joshua` (claim_type: `direct`; promote to central if Deuteronomy or Numbers creates one)
- Added: `teruah-great-shout-wall-falls-flat-joshua-6` (claim_type: `direct`)
- Added: `avne-barad-great-stones-hailstones-joshua-10-11` (claim_type: `direct`)
- Added: `shemesh-dom-sun-stand-still-joshua-10-12-13` (claim_type: `direct`)
- Added: `sefer-hayyashar-book-of-yashar-joshua-10-13` (claim_type: `direct`)

judges-woh:
- Added: `mishenet-staff-fire-from-the-rock-judges-6-21` (claim_type: `direct`)
- Added: `nezir-elohim-nazirite-to-elohim-judges-13` (claim_type: `direct`)
- Added: `harah-you-shall-conceive-judges-13` (claim_type: `direct`)
- Added: `peli-wonderful-name-judges-13-18` (claim_type: `direct`)

1-samuel-woh:
- Added: `yaqar-chazon-nifratz-word-rare-vision-1-samuel-3-1` (claim_type: `direct`)
- Added: `ofalim-tehorim-tumors-1-samuel-5-6` (claim_type: `direct`)
- Added: `seranim-lords-of-the-pelishtim-1-samuel` (claim_type: `direct`)
- Added: `hitallel-made-sport-of-1-samuel-6-6` (claim_type: `direct`)
- Added: `even-ha-gedolah-the-great-stone-1-samuel-6-18` (claim_type: `direct`; founder point 1)

## Follow-ups

- **1 Sam 17:20:** the hosted ASV reference file has a placeholder ('dummy verses inserted by amos').
  The Translator supplied the printed ASV wording.
  The hosted file needs repair.
- **Ketiv/Qere count:** the source edition marks 15 readings in 15 verses, not the 19 in the brief.
  All 15 are recorded.
- **1 Sam 6:19:** the source text lacks the final sof pasuq.
  It is kept as delivered and noted.
- **malakh-yhwh-messenger:** the legacy refs JOSH-5:13-15 refer to the identification debate, but the Hebrew has no *malʾāḵ* there.
  The JOS-WOH refIds are not added.
  The orchestrator may annotate or drop the legacy refs.
- **Kings files (orchestrator):**
  - Kings paragraphs 1KI-WOH-22:54, 2KI-WOH-2:15, 17:35 and 17:36 can receive the `hishtachavah-bow-down-obeisance-worship` id.
  - The 1-kings-woh shofar entry can be retired in favour of the central id.
- **glossaryVersion:** the chapters carry 2.84.0.
  Renumber them if the merge order with the Torah and Isaiah diffs changes the version.
- **2 Sam 1:18:** when it is translated, use 'the Book of Yashar' (`sefer-hayyashar-...`).


---

## Reviewer report

### Joshua 5 — Circumcision at Gilgal and the captain of the host of YHWH before Yericho (Jericho)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "ruach-yhwh-transliteration-former-prophets", "status": "approve", "citations": ["BDB s.v. lāḇēš; s.v. rûaḥ", "Block, Judges, Ruth (NAC 6; 1999), ad loc.", "Webb, The Book of Judges (NICOT; 2012), ad loc."], "reasoning": "Inferred is correct, as for its Kings source: transliteration leaves the recognized ambiguity open, and Block and Webb support the reading of rûaḥ YHWH as the empowering force in Judges. The literal 'clothed' (Judg 6:34) is lexically exact (cf. 1 Chr 12:19; 2 Chr 24:20) and keeps Judges' four distinct verbs distinct. Founder point 4: recommend ship."}, {"glossary_id": "ketiv-qere-qere-translated-former-prophets", "status": "revise", "cita
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 15 lines. No line uses lens vocabulary. 5:13-15 render ʾîš, śar-ṣəḇāʾ-YHWH and wayyištāḥû in their ordinary senses ('a man', 'the captain of the host of YHWH', 'bowed down'), and no malʾāḵ is imported. The TBWTT ch. 3 'military adviser' reading is confined to the labelled reception note at 5:14, which quotes the canon accurately."
- ketivQereInventory: ["JOS-WOH-5:1 K ʿbrnw / Q ʿoḇrām (ASV follows K)"]
- nonBlockingFixes: []
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "15 verdicts: 15 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 4 approve, 4 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### Joshua 6 — The fall of Yericho (Jericho)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "ketiv-qere-qere-translated-former-prophets", "status": "revise", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "MT Judg 6:5 (Ketiv יבאו)"], "reasoning": "Rule and inventory verified: the source marks exactly 15 Ketiv/Qere readings in 15 verses, and all 15 are translated as Qere with the Ketiv recorded; the three ASV-Ketiv sites (Josh 5:1; 6:7; Judg 13:17) are correctly identified. One factual fix: the Judg 6:5 Ketiv is written *yʾbw*; the consonants of יבאו are *ybʾw* (imperfect yāḇōʾû). Correct the entry in all three overlays and the JDG-WOH-6:5 note."}, {"glossary_id": "mt-baseline-at-versional-cruxes-former-
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 27 lines. 'shofar' is a lexical choice (ḥăṣōṣərâ vs šôp̄ār), not a lens choice; 'shout with a great shout' and 'fall down flat' are the ASV wording. The ultrasound reading of TBWTT ch. 3 is confined to the 6:5 reception note (cross-referenced at 6:20). 'devoted to destruction' renders ḥrm lexically and does not reframe the conquest."
- ketivQereInventory: ["JOS-WOH-6:5 K bšmʿkm / Q kəšomʿăḵem", "JOS-WOH-6:7 K wyʾmrw / Q wayyōʾmer (ASV follows K)", "JOS-WOH-6:9 K tqʿw / Q tōqəʿê", "JOS-WOH-6:13 K hwlk / Q hālôḵ"]
- nonBlockingFixes: []
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "27 verdicts: 27 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 6 approve, 3 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### Joshua 10 — Great stones from the skies and the sun standing still at Giv'on (Gibeon)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 43 lines. 10:11 renders both 'great stones' and 'hailstones' literally, so the narrator's identification of the stones as hail stays visible; 10:12-13 keep 'stand still / stayed' with the alternatives in commentary. The canon's 'bombardment' and 'lightning war' readings are confined to the reception notes at 10:11 and 10:13."
- ketivQereInventory: []
- nonBlockingFixes: []
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "43 verdicts: 43 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 8 approve, 2 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### Judges 6 — The call of Gid'on (Gideon): the fire from the rock and the fleece

- **JDG-WOH-6:5** — revise: The line is correct: the Qere ûḇāʾû (perfect consecutive, frequentative 'they would come') is translated. But the note transcribes the Ketiv יבאו as *yʾbw*; the consonants are y-b-ʾ-w, so read *ybʾw* (imperfect yāḇōʾû). Same correction needed in the shared `ketiv-qere-qere-translated-former-prophets` entry (all three overlays). Note-only fix; English line approved.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 40 lines. 6:20-21 keep 'staff', 'rock', 'fire went up', 'departed from his sight'; the feeding-tube reading of TBWTT ch. 3 is confined to the 6:21 reception note. 'the ruach of YHWH clothed Gid'on' (6:34) is literal for lāḇəšâ and transliterates under the ratified Kings convention; it adds nothing."
- ketivQereInventory: ["JDG-WOH-6:5 K ybʾw / Q ûḇāʾû (note misprints K as yʾbw)"]
- nonBlockingFixes: ["JDG-WOH-6:5 note: Ketiv *yʾbw* -> *ybʾw* (the revise item).", "JDG-WOH-6:31 note: add one sentence that v 31 takes the 3ms subject of nāṯaṣ as indefinite ('someone'; GKC §144d), whereas v 32 renders the identical clause 'he'.", "JDG-WOH-6:37 note: delete the leftover '(`eretz`)' (citation removed from glossaryRefs because ʾereṣ is 'ground')."]
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "40 verdicts: 39 approve, 1 revise, 0 flag-for-human (revise: JDG-WOH-6:5 - note-only Ketiv transcription fix; the English line is approved). Glossary/op reviews: 8 approve, 4 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### Judges 13 — The messenger of YHWH and the birth of Shimshon (Samson)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 25 lines. 13:3, 5, 9 render the announcement and the husband's absence exactly; nothing implies a physical union, and the canon's reading (13:3, 5, 9 reception notes; hair as antennas at 13:5) stays in labelled notes. The future construal of hārâ at 13:5, 7 is the major-version consensus, and its bearing on the canon reading is disclosed in the harah entry."
- ketivQereInventory: ["JDG-WOH-13:17 K dbryk / Q dəḇārəḵā (ASV follows K)"]
- nonBlockingFixes: ["JDG-WOH-13:12: align line and note on maʿăśēhû (line 'what shall be done for him' vs note 'his conduct or task')."]
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "25 verdicts: 25 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 9 approve, 3 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### 1 Samuel 3 — YHWH calls Shemu'el (Samuel)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 21 lines. 3:9-10 render the call and Eli's instruction literally; 'YHWH came and stood' is the ASV rendering of the Hebrew anthropomorphism. The telepathy and radio-amateur reading is confined to the reception notes at 3:9-10. 'rare ... widespread' (3:1) is lexical."
- ketivQereInventory: ["1SA-WOH-3:2 K wʿynw / Q wəʿênāyw"]
- nonBlockingFixes: ["1SA-WOH-3:5 note: *hinnəḵî* -> *hinnənî* (source הִנְנִי)."]
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "21 verdicts: 21 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 6 approve, 2 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### 1 Samuel 5 — The ark of the Elohim among the Pelishtim (Philistines)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 12 lines. 'the ark of the Elohim' follows the Hebrew article; 5:3-4 render Dagon's fall literally; 'tumors' translates the Qere neutrally. The transmitter-receiver, electrical discharge and radiation-burn readings are confined to the reception notes at 5:3 and 5:6."
- ketivQereInventory: ["1SA-WOH-5:6 K bʿplym / Q baṭṭəḥōrîm", "1SA-WOH-5:9 K ʿplym / Q ṭəḥōrîm", "1SA-WOH-5:12 K bʿplym / Q baṭṭəḥōrîm"]
- nonBlockingFixes: []
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "12 verdicts: 12 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 9 approve, 2 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### 1 Samuel 6 — The ark returned from the Pelishtim (Philistines) to Beit-Shemesh (Beth-shemesh)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 21 lines. 6:19 renders the striking of the men of Beit-Shemesh literally; the reception note there states that TBWTT does not quote the verse. 'the great stone' (6:18) is a textual-critical decision, not a lens choice."
- ketivQereInventory: ["1SA-WOH-6:4 K ʿply / Q ṭəḥōrê", "1SA-WOH-6:5 K ʿplykm / Q ṭəḥōrêḵem"]
- nonBlockingFixes: ["even-ha-gedolah entry and 1SA-WOH-6:18 note: 'many Hebrew manuscripts' -> 'some Hebrew manuscripts' unless a count is cited."]
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "21 verdicts: 21 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 8 approve, 2 revise, 2 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."

### 1 Samuel 17 — David and Golyat (Goliath)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:36:44Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-former-prophets", "status": "flag-for-human", "citations": ["1-kings-woh hebrew-proper-name-transliteration-convention-kings (ratified 2026-11-01)", "genesis-woh / exodus-woh / 1-kings-woh gentilic practice (checked in the data)"], "reasoning": "Verified identical in all three overlays and identical in substance to the ratified Kings entry (long forms, tz, apostrophes, '-ite' gentilics, English chapter-title forms, which all nine titles carry). Every equivalence in the table was checked against the MT names in these chapters. Flagged only for founder point 2 (gentilics across the corpus, esp. 'the Pelishtite' beside central 'the Pelishtim'); the entry itself is philologically sound and claim_type direct is right for a presentation convention."}, {"glossary_id": "elohim-referent-and-article-conventions-former-prophets", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "1-kings-woh elohim-referent-and-article-conventions-kings (ratified text)", "central elohim-as-translation (\"the Elohim (with article in narrative)\")"], "reasoning": "Clauses 1-5 reproduce the ratified Kings clauses. Clause 6 (Judg 6:40) applies the ratified text exactly: the Kings entry says 'the narrative-subject article rule of the central entry is unaffected', and the central rule is 'the Elohim' in narrative. Clause 7 (1 Sam 17:26, 36) supplies a determiner English grammar requires and records the anarthrous Hebrew. Every listed site wa
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 58 lines. 'the armies of the living Elohim' (17:26, 36) renders ʾĕlōhîm ḥayyîm with only the English determiner supplied; the 'palpable God' reading of TBWTT ch. 3 is confined to the 17:26 reception note. MT Goliath height kept; no other lens-sensitive site."
- ketivQereInventory: ["1SA-WOH-17:7 K wḥṣ / Q wəʿēṣ", "1SA-WOH-17:23 K mmʿrwt / Q mimmaʿarḵôṯ"]
- nonBlockingFixes: ["1SA-WOH-17:26 note (and elohim entry clause 7): cite Deut 5:23 [ET 5:26].", "1SA-WOH-17:47 note: *hazzeh haqqāhāl* -> *haqqāhāl hazzeh*."]
- escalationReportAdjustments: "Initial verdicts on all 262 verses, the overlay entries and the 50 central-diff ops were formed from the chapters, sources, overlays and diff before opening wave-fp1-editor-report.md. After reading it, no verdict changed. The report confirms it did not check the shofar Exodus refIds (the reviewer did: EXO-WOH-20:15, not 20:18) and names the ark collision risk (the reviewer checked exodus-woh chapter-25 and the Torah diff: no ʾărôn entry exists there; six Ex 25 refIds should join the central entry). The report's note that the Torah diff touches no entry this diff modifies is contradicted by the data (hishtachavah), which strengthens the revise on that op. The report's statement that NJPS follows 'stone' at 1 Sam 6:18 was not verifiable from the shelf and is not relied on."
- founderDecisionRecommendations: {"1-1Sam-6:18-great-stone": "Ship. ʾāḇēl cannot be construed (two failed agreements, contradiction with vv 14-15); ʾeḇen with LXX, Targum and some Hebrew MSS is the standard correction (Driver 1913; McCarter 1980). Ratify the exception exactly as narrowly worded (MT grammatically impossible + Hebrew-manuscript reading supported by the versions).", "2-gentilics": "Keep the Kings '-ite' rule in the Former Prophets now (option c); it maps one-to-one to the ASV and is already ratified for Kings. For the later corpus pass, the reviewer prefers (a) '-ite' throughout, with the central pelishtim-caphtor plural becoming 'the Pelishtites', because 'the Pelishtite' beside 'the Pelishtim' is the one jarring pair. No philological issue either way; it is a presentation choice.", "3-Judg-6:40-the-Elohim": "Confirm. The ratified Kings text explicitly leaves the central narrative-subject rule ('the Elohim') in force and limits the article-less form to predicates, genitives and direct-speech subjects; the brief's paraphrase was inaccurate. Clause 6 applies the ratified text exactly.", "4-Judg-6:34-clothed": "Ship. lāḇəšâ is literally 'clothed' (BDB; same idiom 1 Chr 12:19; 2 Chr 24:20; Block), and keeping Judges' four verbs distinct is a gain in accuracy.", "5-herem": "Ship. 'devote(d) to destruction' is the standard modern rendering (NRSV; HALOT) and the only consistent one; it makes the Josh 6 / Josh 10 connection visible without moral editorializing.", "6-shofar-promotion": "Approve the pro
- summary: "58 verdicts: 58 approve, 0 revise, 0 flag-for-human. Glossary/op reviews: 6 approve, 2 revise, 1 flag-for-human. No lens-leakage flags. Status awaiting-human because of wave-level glossary revises (ketiv-qere overlay; central version note, shofar refIds, hishtachavah merge) and flags (proper-name convention, founder point 2; even-ha-gedolah, founder point 1)."
