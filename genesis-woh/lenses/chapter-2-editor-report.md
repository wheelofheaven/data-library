# Genesis 2 lens: editor report

Lens file: `genesis-woh/lenses/chapter-2.json`, 0.1.0 (draft) → 0.2.0 (editor-review).
Editor: claude-opus-5-5 (lens editor), 2026-11-27.
Layer 2 (`genesis-woh/chapter-2.json`) and all glossaries are untouched.
Validator: `python3 scripts/validate_genesis_lenses.py --core-catalog …/core/model/catalog.json` → 0 errors, 0 warnings; unit tests pass (37).

## Method

- Every assertion attributed to *The Book Which Tells the Truth* (TBWTT) was checked against the cited paragraph in the French original and the project English (TBWTT 2:2–2:49, 3:169, 4:75).
- Every quotation in curly quotes was matched against the TBWTT English and the layer-2 English.
- Labels were checked against the `content.md` decision tree and the governing core records (0009 @0.1.1, 0018 @0.1.0, 0059 @0.1.0, 0076 @0.1.2).
- The Genesis 1 reviewer's lessons were applied: a canon link that is the project's pairing is labelled inferred; canon content is never presented as what the Hebrew says; nothing implies that the creators or Yahweh wrote Genesis.

## Changes made

### Metadata

- `lens.version` 0.1.0 → 0.2.0; `lens.status` draft → editor-review; added "claude-opus-5-5 (lens editor)" to `modelDrafts`.
- `lens.coreClaims`: removed `woh-claim-0076` (its only segment was dropped; see flag 4).
- `_lenses.json`: row 2 only, updated to editor-review / 0.2.0. Rows 1 and 3 untouched.

### Seventh day (2:1–3)

- **S *vayishbot*.** Recast without the antithesis: "means 'he ceased' and marks the end of an activity; the familiar 'he rested' is a looser rendering".
- **S selection rule (TBWTT 2:3).** The draft ended "and they do not say why". TBWTT 2:3 does give a general rule, so the segment now quotes both sentences ("Only the parts … important. The others, which are merely poetic chatter, I will not speak to you about.") and ends: "they do not say whether they count these verses among the others."
- **S 0059 (factual correction).** The draft said the Wheel of Heaven timeline "does not assign the seventh day an age". The timeline chapter `data-content/timeline/age-of-cancer.md` reads the seventh day as the Age of Cancer, "the Day of Rest", and 0059's statement runs "through the human synthesis and the rest". The segment is now split in two:
  - framework, `coreClaim` 0059, canon TBWTT 2:10: the timeline counts the seventh day as the Age of Cancer, within which the garden, the expulsion and the generations before the Flood fall;
  - direct, canon TBWTT 2:10: the canon defines a "day" as about two thousand Earth years but does not mention a seventh day; the Sabbath meaning is left to the text (0059 excludes the seventh-day theology).

### Second account (2:4–7)

- **R 2:4.** Rewritten from a restatement of the toledot formula into the meaning: "Here begins a second account … It narrows from the whole planet to one territory and to the creators who worked there, whom it calls YHWH-Elohim."
- **R 2:5–6.** "the land there bore no shrubs …" → "the territory had no cultivated plants …", so the reading conveys meaning and does not shadow layer 2.
- **R 2:7.** First sentence shortened (no longer restates the verse). The canon quotation is now integrated verbatim ("the Messages say of him that 'the man created there was the most intelligent'"). The draft's gloss "Of all the humans the teams made" was dropped. Stays framework (0018, TBWTT 2:28): the canon itself treats the man of the garden as "the man created there".
- **S p1s4.** "does not repeat the first: … it narrows" → a plain declarative (antithesis tic).
- **S *ed*.** "rests on little" → "has little support".
- **S 0076 (TBWTT 2:43) dropped.** See flag 4.

### The garden (2:8–15)

- **R 2:9** (flag 3). See below. Canon refs widened to TBWTT 2:28, 2:30, 2:42, 2:43, 2:49. "In the middle of the garden" → "Within the garden", in line with layer 2.
- **R 2:15** (flag 2). **framework → inferred**; `coreClaim` 0018 removed from the reading. Text tightened so it no longer reads as two stapled clauses: "There they educated him while keeping him in ignorance of the great scientific secrets, so that the created would not surpass the creator and his intelligence could be measured."
- **S expulsion pointer (TBWTT 2:44–45).** "the guarded way into the garden becomes 'the entrance to the creators' residence'" → "the guards are placed 'at the entrance to the creators' residence'". This is what 2:45 says; equating the way with the residence was a step the canon does not take in so many words.
- **S "good and bad".** The merism is now "often read as" one: it is the majority view, not the only one, so a direct label needs the hedge.
- **S trees (TBWTT 2:30, 2:37, 2:42, 2:43, 2:49).**
  - "read the tree as the creators' scientific knowledge" → "read eating from the tree of knowledge as touching 'the scientific books'", the canon's own words (2:30, 2:37).
  - The tree-of-life link is now located where the canon makes it: commenting on Genesis 3:22 (2:42), the canon says "there is a scientific means" of prolonging human lives "for a very long time" (2:43, verbatim). The draft's "far beyond the human span" was a paraphrase in quotation-adjacent position.
- **Rivers paragraph** (flag 5). The direct segment "The Wheel of Heaven reading does not try to solve the rivers as a map …" now comes before the speculative one. The speculative segment is reworded (see flag 5).
- **S verse 15.** "worker and watchman, not owner" → "he is the garden's worker and watchman" (antithesis tic; "owner" was a straw figure).
- **S TBWTT 2:28 measures** (flag 2). Split into:
  - framework (0018, TBWTT 2:28): the verbatim quotation, introduced as "In the Messages, the team's measures concern the man's education";
  - inferred (TBWTT 2:28, 2:29): "Setting these measures beside verse 15 is a Wheel of Heaven reading. The Messages state them of the garden as a whole and go on at once to the prohibition of 2:16–17."

### The forbidden tree (2:16–17)

- **S TBWTT 3:169.** Now gives the context: the remark is made "commenting on Ezekiel's eating of a scroll".
- **S French tree name** (flag 1). Rewritten; see below.
- Readings R 2:16 and R 2:17 checked against TBWTT 2:30: faithful, framework kept.

### Naming the animals (2:18–20)

- **S *ezer kenegdo*.** "not a subordinate 'helpmeet'" → "the old English 'helpmeet' fuses the King James Version's 'an help meet for him' into one word". Same point, stated as the history of the word instead of a rebuttal.
- Other segments verified: TBWTT 2:31 and 2:32 quoted verbatim; the naming-authority difference (human names in Genesis, creators teach in the Messages) and the order difference stay direct and visible.

### The woman (2:21–25)

- **S the operation** (flag 5). "Read as a creators' report" → "Read as a compressed report of the creators' work" (avoids implying the creators wrote the record); "Nothing in the canon states this" now stands as its own sentence; "simply" removed before the Messages' image, which read as dismissive of the canon.
- **S verse 24 aside (inferred).** The draft opposed "the people who kept the record" to "the creators' report", which implied the creators authored Genesis. Now grounded in what the canon actually says: it "speaks of 'the original document' behind parts of Genesis (TBWTT 2:41) and of copyists who distorted the traces of the truth (TBWTT 2:2)", so the aside is "the voice of those who handed the record down". Canon refs added: TBWTT 2:2, 2:41.

## Label changes (summary)

| Unit | Old | New | Reason |
|---|---|---|---|
| R 2:15 | framework (0018) | inferred | Attaching 2:28's measures to verse 15 is the project's pairing |
| Eden S measures | framework (one segment) | framework + inferred | Canon quotation separated from the pairing with verse 15 |
| Seventh day S timeline | direct (0059) | framework (0059) + direct | Timeline assignment is 0059's framework content; the canon note is a textual fact |
| Second account S 2:43 chosen people | framework (0076) | dropped | See flag 4 |

## Writer's flags

1. **French « arbre de la science ».** Kept, reframed. It is accurate: TBWTT 2:29 quotes the verse as « l'arbre de la science du bien et du mal », and the canon's French Bible uses *science* again at 3:22 (TBWTT 2:42, « grâce à la science »). The draft said the Messages quote "the traditional wording" and pointed to the English, which is the project's own KJV-style rendering of a French quotation. The segment now says the Messages quote the verses in French, traces *science* back through the Vulgate's *lignum scientiae boni et mali* in its older sense of knowledge, and gives the Hebrew *da'at* ("knowing"). It does not argue that the canon's reading rests on the French word (which would undercut it), nor that the Hebrew means "science" (which would overclaim). Label direct, canon TBWTT 2:29.
2. **R 2:15 framework placement of TBWTT 2:28.** Relabelled inferred. TBWTT 2:28 comments on the garden as a whole; the canon map attaches it to 2:8–15, and 2:28 leads straight into the quotation of 2:16–17 (2:29). Pairing the measures with verse 15 specifically is the project's. The canon content itself stays framework in the explanation, with the pairing stated as an inferred segment.
3. **R 2:9, both trees attributed to the Messages.** Checked; the attribution stands, with the wording tightened to the canon's terms.
   - Tree of knowledge: TBWTT 2:30 reads the prohibition as "do not touch the scientific books"; 2:37 repeats "forbidden them to touch the scientific books"; 3:169 calls the eating "intellectual «food»". The reading now says "whose fruit they read as the scientific books the creators kept from the human".
   - Tree of life: 2:43 does not name the tree, but it is the canon's comment on its quotation of Genesis 3:22 (2:42, "the tree of life, and eat, and live for ever"), and 2:49 and 4:75 name the "tree of life" explicitly as the longevity the chiefs and Moses and Elijah benefited from. The reading says the Messages "tie" the tree to "a scientific means" of prolonging life (verbatim).
   - Framework kept: the canon explicitly interprets these named trees, and the canon map attaches 2:28 to the verse. If the reviewer prefers, the identification could be marked inferred on the ground that the canon's comments sit on 2:16–17 and 3:22, not on 2:9; I judged that the trees are the same trees and the identification is the canon's.
4. **Optional 0076 "chosen people" segment.** Dropped. Reasons:
   - The canon places the election clause in its comment on Genesis 3:22 (TBWTT 2:43), and the canon map attaches 2:43 to 3:22, not to Genesis 2.
   - The chapter 3 lens (draft, being edited in parallel) uses TBWTT 2:43 only for the longevity sentences and does not carry the election clause or 0076. Carrying it in chapter 2 alone would put the clause one chapter ahead of where the canon introduces it, with no matching treatment where it belongs.
   - Genesis 2 already carries the canon's own comment on this territory and this man: "one of the most brilliant, if not the most brilliant" team, and "the man created there was the most intelligent" (TBWTT 2:28). The election clause concerns "the people of Israel" at a later competition, which shifts the subject from the first human to a people.
   - 0076 is a sensitive record (its scope excludes any ranking the corpus endorses). If it is used anywhere in Genesis 1–11, it should be introduced once, with its full scope wording, at Genesis 3:22. See escalation 2.
5. **Speculative segments.** Both kept, labelled speculative.
   - Rivers: the draft's closing "Nothing in the canon states this" was ambiguous, since the single continent *is* in the canon (2:28). New wording: "The canon places the territory on 'the single continent' of that time. One Wheel of Heaven reading takes this to mean that the rivers of verses 10–14 need not match a modern map. The canon does not draw that conclusion." It stays inside 0018's exclusions (no map solution, no modern site), and it does not date the continental breakup (the Genesis 1 founder ruling treats that dating as speculative and non-canon).
   - The operation: wording changes listed above.
6. **Visual.** None added (`visual` stays absent on all passages).

## Notes for the orchestrator (outside this editor's write scope)

- No canon-map change is needed for this chapter. The new refs (TBWTT 2:2, 2:37, 2:41, 2:42, 2:49) all exist in the canon files; each reading with `basis: "canon"` still cites a ref the map attaches to its verses (validator rule 7).
- Layer-2 errata are already queued; none added here.

## Escalations for the founder

### 1. Seventh day = Age of Cancer (0059)

**Issue.** The draft denied that the timeline assigns the seventh day an age; the timeline does (Age of Cancer, "the Day of Rest"). The corrected segment is framework through 0059. The canon itself is silent on the seventh day and gives the "day" as about two thousand years.

**Options.** A. Ship as corrected (framework, 0059). B. Drop the timeline segment and keep only the direct canon note.

**Editor's recommendation.** A. It states the project's own timeline accurately and labels it.

### 2. Where, if anywhere, the election clause (TBWTT 2:43, 0076) enters the Genesis lens

**Issue.** Dropped from chapter 2 (flag 4). The chapter 3 lens does not carry it either.

**Options.** A. Introduce it once at Genesis 3:22, in 0076's scope wording (framework), in the chapter 3 lens. B. Leave it out of the Genesis 1–11 lens entirely and let the wiki carry it.

**Editor's recommendation.** A founder choice; the chapter 3 editor should be told whichever is chosen. If A, the segment should quote the canon verbatim and carry the record's exclusion that the clause is the canon's account of a self-understanding, not a ranking the corpus endorses.

### 3. Speculative segments for sign-off

- **Rivers / single continent** (Eden passage). Recommendation: ship.
- **The operation under anaesthesia** (woman passage). Recommendation: ship. It is the chapter's boldest reading and says plainly that the canon does not state it.

## Post-review corrections (2026-11-27)

The reviewer's report is in `lens.reviewerReport`: 75 approve, 4 revise, no flag-for-human.
All four revise items are applied in the reviewer's proposed wording.
`lens.status` (awaiting-human), `lens.version` (0.2.0) and `reviewerReport` are unchanged; the `_lenses.json` row 2 already matched and was not touched.
Validator: 0 errors, 0 warnings; unit tests pass (37).

### Revise items

1. **Seventh day, E p2s3 (Age of Cancer; stays framework, 0059, TBWTT-2:10).** The old wording put the garden after "the work of making is over", which contradicted Genesis 2 itself and the Cancer timeline chapter. It now says the creation program closes at the end of the sixth age with the first humans already in the garden; the disclosure, the expulsion and the generations before the Flood fall within the seventh; and the second account from verse 4 goes back over the making of the human, the garden and the woman. The following direct segment (the canon does not mention a seventh day) is unchanged.
2. **Eden, E p1s3 (stays direct).** "The Hebrew says 'a garden in Eden'" was true of verse 8 only. It now reads: "In verse 8 the Hebrew says 'a garden in Eden' … From verse 15 the text also says 'the garden of Eden' (*gan-eden*)." This matches layer 2 at 2:8 and 2:15.
3. **R 2:19 (stays canon / framework, TBWTT-2:31, 2:32).** The reading had let the canon's teaching replace the verse's own point. It now keeps 2:19b, "whatever he called each one became its name", and then gives the canon's "The creators taught him the name and the powers of everything that lived around him."
4. **Naming, E p2s2 (stays direct).** "quote only the second half of the verse" was inaccurate. TBWTT-2:31 quotes the middle clause. The segment now says the Messages leave out both the forming of the animals (2:19a) and the closing clause, "whatever the human called each living being, that became its name", which is where the two accounts differ.

### Founder rulings (2026-11-27)

- **YHWH-Elohim = "the creators" in layers 3–4.** Checked every reading and segment. Readings use "the creators" or "the team" throughout; R 2:4 says "the creators who worked there, whom it calls YHWH-Elohim"; E p1s4 says the Reading renders YHWH-Elohim "as the creators of one team". The name appears bare only in layer-4 statements about the Hebrew text (the seam at 2:4; "Neither YHWH-Elohim nor the human speaks" at 2:24). No change needed.
- **TBWTT-2:43 election statement (0076) only at Genesis 3:22.** Genesis 2 keeps it out, as in 0.2.0; 0076 is not in `lens.coreClaims`.

### Optional reviewer suggestions (taken)

- **The canon's speaker named.** New direct segment after E p1s3 in the second-account passage, canon ETTMTTP-2:50: "The dictated Messages do give their speaker's name: 'My name is Yahweh and I am the president of the council of the eternals' (ETTMTTP 2:50). The Reading still renders YHWH-Elohim as the creators, the team at work in this account." This names Yahweh without equating him with the compound, so it stays within ruling 2. The chapter 3 lens should treat the name the same way.
- **Verse-24 aside (stays inferred).** Support changed from TBWTT-2:41 (a phrase "preserved almost intact") to TBWTT-2:3, which fits an added aside better: the canon says the text "became laden with mystical and useless phrases over the millennia". Canon refs are now TBWTT-2:3 only.

Not taken: the reviewer's note that TBWTT-4:75 is not needed concerns the editor report only; no lens unit cites it.
