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
