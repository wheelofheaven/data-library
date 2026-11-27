# Genesis 1 lens: editor report

Lens file: `genesis-woh/lenses/chapter-1.json`, 0.1.0 (draft) → 0.2.0 (editor-review).
Editor: claude-opus-5-5 (lens editor), 2026-11-27.
Layer 2 (`genesis-woh/chapter-1.json`) and all glossaries are untouched.
Validator: `python3 scripts/validate_genesis_lenses.py --core-catalog …/core/model/catalog.json` → 0 errors, 0 warnings; unit tests pass.

## Method

- Every assertion attributed to *The Book Which Tells the Truth* (TBWTT) was checked against the cited paragraph in the French original and the project English.
- Every quotation in curly quotes was matched against the TBWTT English and the layer-2 English. The only non-matches are deliberate non-canon quotes: the standard "When … began to create", the formula "evening and morning", and the standard "great sea creatures".
- Labels were checked against the `content.md` decision tree. Where a core claim governs a segment, its `public_label` decides the label.

## Changes made

### Metadata

- `lens.version` 0.1.0 → 0.2.0; `lens.status` draft → editor-review; added "claude-opus-5-5 (lens editor)" to `modelDrafts`.
- `lens.coreClaims`: added `woh-claim-0071` at 0.3.1 (the day 3 forward pointer).
- `_lenses.json`: row for chapter 1 updated to editor-review / 0.2.0.

### Day 1 (1:1–5)

- **R 1:2** (flag c). The old text, "the Elohim's reconnaissance moved above the waters", turned the Messages' juxtaposition into an equation. The new text says what the canon says: "Above the waters the Elohim carried out reconnaissance trips and placed what might be called artificial satellites around the planet…". **framework → inferred.**
- **R 1:3–4.** The opener "Next came the question of light" was cut as a filler line. The reading now gives the canon's reason for the light study: life could not be created there if the sun sent harmful rays (TBWTT 2:8).
- **R 1:5.** The reading now carries the canon's definition of the "day" (the sun rising under the same sign at the spring equinox). Before, it only restated the close of the day.
- **S Elohim gloss.**
  - "Genesis opens with *Elohim*" → "The subject of the first verse is *Elohim*". Genesis opens with *bereshit*, so the old wording was wrong.
  - "unjustly translated as 'God'" → "unjustly translated in some Bibles as 'God'", as TBWTT 2:5 has it.
  - "create simple forms of life in their laboratories" → "primitive forms of life, living cells in test tubes", as TBWTT 2:2 has it.
- **S etymology.** "Standard lexicons derive…" → "…is not the consensus etymology, which derives the word through *Eloah* and *El*". This follows the wording woh-claim-0009 requires.
- **S 1:2** (flag c). The paragraph is now split into three segments:
  - framework (TBWTT 2:6–7): the canon quotes the verse and follows the quotation at once with the reconnaissance;
  - inferred: the Messages do not state the equation, so it is an inference from where the comment stands;
  - direct: *ruach* means wind, breath or spirit; *merachefet* also describes the eagle in Deuteronomy 32:11; layer 2 renders the phrase "breath of the Elohim hovering".
- **S 0059.** "remains the primary one" → "is the one this reading follows".

### Day 2 (1:6–8)

- **R 1:8.** Canon refs widened from [2:10] to [2:10, 2:12], because the cloud/ocean reading of the "skies" comes from 2:12.
- **S missing "good".** Now notes that the Septuagint supplies the formula at 1:8.
- **S 2:1 inferred.** The draft only hinted at a reason. The segment now states the reason the Messages' sequence suggests: the verdict waits for day 3, where it comes twice. It also cites Rashi's comparable explanation that the work on the waters was not finished until the third day.

### Day 3 (1:9–13)

- **R 1:13.** Now adds "another span of about two thousand years".
- **S Pangaea** (flag a). The draft's mainstream date stood alone, with no Wheel of Heaven counterpart. Two segments are added after it:
  - framework, canon TBWTT 2:58: in the dictated text the single continent still exists at the Flood ("an immense tidal wave" over "the continent").
  - framework, `coreClaim` woh-claim-0071, canon TBWTT 2:14 and 2:58: the Wheel of Heaven reading dates the breakup to that strike, "(see Genesis 7)".
- Neither segment rests on LWTE. The Terrusse essay is not cited at all, and the breakup segment is attributed to the Wheel of Heaven reading, not to the Messages. The framework label comes from 0071's `public_label`. See escalation 1.

### Day 4 (1:14–19)

- **R 1:17–18.** "With the sky mapped…" quietly rendered "set" as "charted". The reading now renders only what TBWTT 2:18 says: the lights were used to measure days, months and years and to regulate the Elohim's lives.
- **S vocabulary.** Now names *otot* ("signs") next to *moadim*.
- **S "functional, calendrical vocabulary".** **inferred → framework**, with `coreClaim` woh-claim-0039 and canon TBWTT 2:18. This is exactly 0039's "vocabulary as observational" scope, and 0039's public label is framework.
- **S "signs" echo** (kept speculative). Now says plainly that the echo works only in English and French: Hebrew *otot* means signs or marks in general, not zodiacal signs. Accuracy above lens.

### Day 5 (1:20–23)

- **R 1:22** (flag d). The old reading replaced the blessing with the courtship-dance story and was labelled framework. The new reading keeps the verse's intent (the creatures are to breed and fill their domains) and adds the canon's courtship dances. **framework → inferred.**
- **New S, inferred.** The Messages do not comment on the blessing; setting it beside the courtship dances is a Wheel of Heaven reading.
- **S TBWTT 5:63.** Adds "their 'amorous demonstrations'". This is the canon's own link between the birds' courtship and design.
- **S dragons quote.** The quotation is now verbatim, with the dropped ", and so on." restored.
- **S tanninim.** Now gives the standard "great sea creatures", the layer-2 "great dragons", and its source in Dhorme's *grands dragons*.

### Day 6 (1:24–31)

- **R 1:27.** "'The resemblance is striking,' the Messages say" → "The Messages note that 'the resemblance is striking'". The quotation is now lower case and verbatim, and "one team" → "a team", as in 2:25.
- **R 1:28.** Rewritten from a restatement of the verse into the creators' design for the new population. It stays inferred / synthesis.
- **R 1:29 and R 1:30** were merged into **R 1:29–30**, because both restated the food grant. The merged reading is inferred / synthesis.
- **S TBWTT 5:62** (flag b). The draft listed "fish, amphibians, mammals and primates" and silently dropped the birds. 5:62 actually reads "the fish, the batrachians, the mammals, the birds, the primates, and finally man", which is now quoted verbatim.
- **New S, direct**, canon TBWTT 2:22, 2:24 and 5:62. The 5:62 list puts the birds after the mammals, while chapter 2 (and Genesis 1) has the birds straight after the fish, before any land animal. The Messages do not reconcile the two sequences.
- **S food tension** (flag e). The draft had one speculative segment that mixed a textual fact with a harmonisation. It is now two segments:
  - direct, canon TBWTT 2:20 and 2:24: the tension with the Messages' predators;
  - speculative: the "diet set for the first humans … in the creators' care" reading, now ending "Nothing in the canon states this."
- **S article on "the sixth day".** "this day alone" → "Of the six days, … only this one". Seventh-day references in 2:2–3 also carry the article.

## Label changes (summary)

| Unit | Old | New | Reason |
|---|---|---|---|
| R 1:2 | framework | inferred | Equation of the Spirit with the reconnaissance is not stated in the canon |
| R 1:22 | framework | inferred | Blessing ↔ courtship dances not canon-explicit |
| Day 1 S "Spirit" | framework (one segment) | framework + inferred + direct | Canon content, the inference and the philology separated |
| Day 4 S vocabulary | inferred | framework (0039) | Governed by woh-claim-0039, public label framework |
| Day 6 S food | speculative (one segment) | direct + speculative | Tension is a textual fact; harmonisation is speculative |
| Day 3 breakup (new) | — | framework (0071) | Record's public label |
| Day 5 blessing note (new) | — | inferred | |
| Day 6 creation-order note (new) | — | direct | Textual fact about the canon |

## Writer's flags

- **(a) Day 3 and the breakup.** Resolved with a forward pointer to Genesis 7. The segment is labelled framework through `woh-claim-0071` and grounded in dictated text (TBWTT 2:14 and 2:58). LWTE is not cited. Open standing question: escalation 1.
- **(b) TBWTT 5:62 vs 2:22.** Resolved. The draft's omission of the birds is corrected, and the discrepancy is stated as a direct observation, without harmonising it.
- **(c) 1:2 "Spirit of Elohim" as reconnaissance.** Resolved. The reading is now inferred, and the explanation says outright that the canon does not state the equation.
- **(d) 1:22 blessing and courtship dances.** Resolved. Relabelled inferred, with an explicit note that this is a Wheel of Heaven reading. The canon's own courtship link (5:63, "amorous demonstrations") is now cited.
- **(e) 1:28–30 plant-only food.** Resolved. The tension is direct and visible; the harmonisation is speculative and marked as not in the canon.

## Notes for the orchestrator (outside this editor's write scope)

- `canon-map.json`, entry 1:20–23: the note on the TBWTT-5:62 ref reads "Creation sequence fish, birds". 5:62 actually runs fish → batrachians → mammals → birds. Suggest rewording the note to "Creation sequence; places birds after mammals".
- The local core checkout has woh-claim-0001 at 0.2.0 in `catalog.json`. Memory records a 0.2.1 scope note (LWTE-1:15). If the catalog is updated, re-pin `lens.coreClaims`.

## Escalations for the founder

### 1. `woh-claim-0071` as the label authority for the day 3 breakup

**Issue.** The day 3 forward pointer is labelled framework because woh-claim-0071's public label is framework.

- The dictated canon says only two things here: the single continent was raised and its pieces later drifted (TBWTT 2:14), and "the continent" was still single when the Flood struck (2:58).
- The breakup *at* the strike comes from the Terrusse essay (LWTE ch. 4). ADR 0018 places that essay outside the canon, and 0071 is listed there as awaiting review.

**Options.**

- **A.** Keep framework through 0071 as it stands, in line with the 2026-09-10 ruling that the Flood rewrote the geology.
- **B.** Wait for the 0071 review under ADR 0018 and relabel the segment to whatever 0071 becomes.
- **C.** Label the segment inferred now, as a reading of 2:14 together with 2:58.

**Editor's recommendation.** A, since the record is still accepted with label framework and the segment cites only dictated text. The lens should be re-checked when 0071 is revised.

### 2. The day 4 "signs" echo (speculative)

**Issue.** The echo between Genesis' "signs" and the canon's zodiacal "sign" exists only in translation. The segment now says so.

**Options.** Ship as a transparent speculative note, or drop it.

**Editor's recommendation.** Ship. It is honest as written, but it is the thinnest segment in the chapter.

No other speculative units are new. The existing speculative segments are the 0073 dragons signature, whose label is controlled by the record, and the food-grant harmonisation. They go to sign-off with the chapter as usual.

## Post-review corrections (2026-11-27)

The reviewer's report is in `lens.reviewerReport`: 73 approve, 9 revise, 2 flag-for-human.
All nine revise items are applied in the reviewer's proposed wording.
`lens.status` (awaiting-human), `lens.version` (0.2.0) and `reviewerReport` are unchanged.
Validator: 0 errors, 0 warnings; unit tests pass.

1. **Day 1, E p2s2 (bereshit; stays direct).** "The Hebrew of 1:1 begins with a construct form…" became "The first word, *bereshit*, has no article and can be read as a construct…; many modern translations follow this with 'When … began to create', while others keep 'In the beginning'…". The construct reading is now presented as one scholarly position.
2. **Day 1, E p3s1 (1:2).** The first sentence is now "In the Messages' account, the Earth at this point was covered entirely by water and thick mists." Verse 1:2 has no mists, so the canon content is no longer presented as the verse's.
3. **Day 1, E p4s2 (claim 0059; stays framework).** The segment now says that the canon's own definition already is a precessional age. The step beyond the canon is the ~2,160-year figure and the assignment of days to named ages. Added canon ref TBWTT-2:10.
4. **Day 2, R 1:8.** Relabelled framework → inferred, consistent with R 1:16. The text is unchanged.
5. **Day 4, E p3s2.** "a report written by people measuring time" became "a compressed report of people measuring time". The old wording implied that the Elohim wrote Genesis.
6. **Day 6, R 1:25.** Dropped the Yahweh sentence and now ends "so that here too the species would keep one another in check."
7. **Day 6, R 1:29–30.** New wording keeps the tension visible in the reading itself. The verse gives the green plants to the animals, "a grant the Messages, which have the creators make meat-eaters, do not take up."
8. **Day 6, E p1s3 (stays direct, claim 0009).** The segment now names the singular verb and suffix of 1:27 (*betsalmo*, "in his image"). It also says the Wheel of Heaven translation renders that verse in the plural, so lens 2 and lens 4 no longer appear to contradict each other.
9. **Day 6, E p1s6 (stays direct).** "the account of chapter 2" became "the Messages' own creation account (TBWTT 2:22–24)", which avoids confusion with Genesis 2. I also took the reviewer's optional softening, "names the birds after the mammals", because 5:62 is a list and may not be meant as a strict sequence.

**Day 3, E p1s4 (continental breakup): founder ruling pending.**

- The current text and label stay as they are: framework, claim 0071, TBWTT-2:14 and 2:58.
- The segment now carries a `pendingFounderRuling` object with:
  - the issue;
  - the current state;
  - the reviewer's alternative wording, labelled speculative, with inferred as the editor's option C;
  - its canon refs, TBWTT-2:14 and 2:76.
- The alternative says the Messages do not date the drift. It says the dating comes from Marcel Terrusse's essay printed in *Let's Welcome the Extraterrestrials*, not from the dictated Messages. It also notes that the Messages still speak of "the whole continent" at Babel (TBWTT-2:76, FR « sur tout le continent »).
- If the founder adopts the alternative, the preceding framework segment (2:58, "the continent" at the Flood) should be reconsidered with it.

The schema's segment definition does not forbid extra keys, so the validator accepts the field. Before the reader templates are built, it may need an entry in `schema.json` and to be ignored by the reader.

**Outside scope, for the layer-2 errata queue (reviewer notes).**

- The GEN-WOH-1:1 note claims that "In the beginning" would require the article. Absolute *reshit* without the article occurs in Isaiah 46:10.
- Layer 2 renders 1:27 in the plural while its own note calls the forms singular.

## Founder rulings applied (2026-11-27)

### 1. Day 3, E p1s4: continental breakup

The founder adopted the reviewer's alternative wording, labelled **speculative**, with canon refs TBWTT-2:14 and 2:76:

> The Messages say the continents later drifted apart but do not say when. The Wheel of Heaven reading dates the breakup to the Flood strike (see Genesis 7); that dating comes from Marcel Terrusse's essay printed in *Let's Welcome the Extraterrestrials*, not from the dictated Messages, which still speak of "the whole continent" at Babel.

- The segment no longer has a framework label, and its `woh-claim-0071` binding is dropped.
- No other segment cites 0071, so it is also removed from `lens.coreClaims`.
- The `pendingFounderRuling` object is removed.
- The preceding TBWTT-2:58 segment (framework) was narrowed to a verbatim quotation of 2:58: "In the Messages' account of the Flood, 'the continent was submerged by an immense tidal wave that destroyed all life on its surface'." The old wording, "the single continent is still there at the Flood", inferred more than 2:58 says.

### 2. ETTMTTP chapter 3 ("The Keys") is not canon

- In `canon-map.json`, the standingRules entry for ETTMTTP chapter 3 goes from `check` to `author-opinion`.
  - All 11 ETTMTTP-3 refs now carry standing `author-opinion` and relation `opinion`, and their notes record the ruling.
  - The single entry that rested only on such a ref (3:19) changes its relation from `check` to `opinion`.
  - `canonPolicy` is updated.
  - The map version is 1.0.0 → 1.1.0.
- `basedOn.canonMapVersion` in `chapter-1.json` and `canonMapVersion` in `_lenses.json` are now 1.1.0.
- In `README.md`:
  - the standing table now lists ETTMTTP chapter 3 under `author-opinion`, and `check` is reserved with no passages at present;
  - the ref-relation text and validator rules 1 and 6 are updated to match.
- `scripts/validate_genesis_lenses.py` had only allowed relation `opinion` on LWTE refs. It now ties `opinion` to author-opinion standing, so ETTMTTP-3 refs are accepted and must carry `opinion`. This is a minimal change, made so the ruling validates. The Genesis 1 lens cites no ETTMTTP-3 paragraph.

Both rulings are also recorded in `lens.reviewerReport.founderRulings`. The schema forbids new keys on `lens`, so this is the only place in the lens file that can hold them.
`lens.status` stays `awaiting-human`, because the Genesis 1 content sign-off is a separate step.
Validator: 0 errors, 0 warnings; unit tests pass.
