# Independent review: Genesis 1–5 lens 3 "Reading" (decoded), Meaning naming, note consistency — 2026-11-28

Reviewer: claude-opus-5-5 acting as woh-reviewer. I read the builder's logs only after running my own diff.
Rules applied: decoding glossary 1.0.0 (stable, with founderRulings), `decoding-glossary-summary.md`, and the form-4 and form-5 rulings in `genesis-lens-plan.md` (2026-11-28).
Layer 2 (`genesis-woh/chapter-1..5.json`) and the chapter lens files were read only. Nothing in them was edited.
I ran the lens validator (`scripts/validate_genesis_lenses.py --core-catalog …`): 0 errors, 0 warnings.

## Counts

- Decoded units: 95. Their refs match the Meaning refs exactly in every passage.
- Verses covered: **138**, each exactly once, none missing (31 + 25 + 24 + 26 + 32). The brief said "160 verses"; Genesis 1–5 has 138.
- Word-level differences from layer 2: 128 diff hunks. All 128 are glossary swaps, glossary variants or logged agreement changes. **Violations: 0.**
- Glossary substitutions: 108, matching `substitutions.md`. Agreement changes: the 20 in `agreement-log.md`, plus one inside a glossary variant that the agreement log does not list: 1:7 "were" → "was" ("the ocean which was under the dome", the glossary's own variant text).
- No swaps were missed. The only literal forms left in scope are 2:15 "garden of Eden" (garden exception, 2:8–3:10) and 4:1 "YHWH himself!" (Q10 A). Every remaining "day", "tree" and "garden" is a listed exception.
- Layer-2 bracket glosses are kept (2:23 "[Woman]", "[Man]"). There are no visual marks. Every text holds `en` only.
- Meaning edits against HEAD (git diff): 22 units changed, all of them Elohim naming only (ch.1 15, ch.2 1, ch.3 2, ch.4 1, ch.5 3). No other Meaning text and no Meaning metadata changed.
- Note edits against HEAD: 9 sentence-level edits, matching `note-consistency-log.md` one for one. No other note text and no note metadata (claim, canon, coreClaim) changed.

## Verdicts

| Ch | Reading (lens 3) | Meaning naming | Notes | Overall |
|---|---|---|---|---|
| 1 | approve | revise (1:29–30) + founder (1:27) | n/a | revise (minor) |
| 2 | approve | approve | revise (2 sentences) | revise (minor) |
| 3 | approve | revise (3:2–3) | approve | revise (minor) |
| 4 | approve | approve | revise (wording, 1) | revise (minor) |
| 5 | approve | revise (5:3) | revise (1 regression) | revise (minor) |

The Reading text is clean in all five chapters. Every "revise" concerns lens 4 wording or a note sentence. Each fix below is minimal, and none changes a claim.

## Violations table (Reading, lens 3)

| Verse | Difference | Class | Verdict |
|---|---|---|---|
| — | — | — | **none** |

Classification of all 128 hunks: Elohim → Sky People (incl. bare 5:1 "of Elohim"); YHWH(-Elohim) → (T)the creators (scope 2:4–5:32, 4:1 excepted); yom 1:5–2:3 incl. variants "On/on the seventh day" → "In/in the seventh age" and 2:3 "on it" → "in it"; waters 1:6–7 (1:6 inferred variant, 1:7 "were" → "was"); yabbashah 1:9–10; etz-ha-daat 2:9, 2:17 + "from it" → "from them" ×2; etz-ha-chayyim 2:9, 3:22, 3:24; nachash 3:1, 2, 4, 13, 14; gan-eden 3:23–24; keruvim and lahat 3:24; minchah 4:3–5; 20 logged agreement changes. Capitalisation at sentence start is correct throughout.

## Agreement changes (item 3 of the brief)

All 20 approved.

- **Cross-verse antecedents (3:11, 3:16, 3:17, 3:24, 4:10).** Approve. Leaving "He" would leave a lone singular for the creators, and the glossary's own samples (3:24, 4:5) make the same change. In 3:11 and 4:10, "They said" follows a speech by the human or by Cain, and the content of the question makes the speaker clear. That reading is no worse than layer 2's "He said".
- **2:21 "while he slept, they took one of his sides".** Approve. The change in number actually tells the two referents apart more clearly than layer 2's "he … he … his".
- **3:16 / 3:17 / 4:10 "they said, 'I …'".** As ruled (Q2 A). 3:16 is the most abrupt, but no fix is possible inside the rules.
- **3:23 "So the creators sent him out of the creators' residence".** Approve. This is the glossary sample verbatim. "Their residence" would depart from the signed-off rendering.
- **3:1 "the small group of creators was shrewder … that the creators had made. They said to the woman".** Approve as specified, but see founder item F3. Because the subject took a singular verb, the nearest plural noun before "They" is "the creators". A cold reader can take "They said" as the creators speaking, not the group.

## Grammar and naturalness (item 2): no violations; observations

All 138 verses parse. The following read oddly, but each follows directly from a signed-off ruling, so I propose no fix:

- 2:9: "caused every tree … to sprout … the means of prolonging life and the scientific books" (the books "sprout"). This comes from the word-only swap.
- 2:17 "eat from them" and 3:22 "take also from the means of prolonging life, and eat". "Eat" stays by ruling (Q4, TBWTT 3:169).
- 3:2–3, 3:6, 3:11–12, 3:17: "the tree" returns after 2:9/2:17 said "the scientific books". This is the Q4 exception. The Meaning bridges it.
- Layer-2 punctuation carried into the Reading (not fixable in lens 3; see F4):
  - 3:17–19 never closes its quotation (3:19 lacks the closing ").
  - 4:10 closes the quotation, so 4:11–12 stands as unquoted speech. As its own card it reads like the narrator cursing Cain.
  - 4:13–14 closes the quotation after "too great to bear." and leaves 4:14's speech unquoted inside the same card.
- 1:14/1:15, 2:16/2:17 and 3:14/3:15 split one quotation across two cards. This is acceptable because the cards are consecutive.

## Meaning naming (item 4)

The first Elohim mention in each chapter is "those who came from the sky": 1:1, 2:2, 3:1, 4:25, 5:1. Later Elohim mentions are "the Sky People". The YHWH strand is "the creators". No naming change falls inside a verbatim canon quotation; the quotations in 1:21, 1:27, 2:7, 2:9, 2:23, 3:22 and 5:4–5 are untouched. Every edited sentence is grammatical.

Revise (Elohim verses whose Meaning still names the actor "the creators"):

| Unit | Now | Proposed |
|---|---|---|
| 1:29–30 | "For food the creators assigned the first humans …; … the Messages, which have the creators make meat-eaters, …" | "For food the Sky People assigned the first humans …; … the Messages, which have the Sky People make meat-eaters, …" |
| 3:2–3 | "the creators had said that they were not even to touch it" (the verse's speaker is *Elohim*; the Reading has "the Sky People have said") | "the Sky People had said that they were not even to touch it" |
| 5:3 | "The likeness the creators had given Adam passed to his son." (5:1 is Elohim) | "The likeness the Sky People had given Adam passed to his son." |

Left as is: generic Raëlian uses of "creators" ("team of creators", "their creators", 2:15 "the created would not surpass the creator", a TBWTT 2:28 phrase), and 5:21–23 "living in the creators' company" (an explanatory apposition).

Bookkeeping: `scratchpad/decoded/meaning-naming-log.md` reports "Total changes: 0", but the git diff shows 22 applied changes. The log looks like it was written by a second run, after the edits were already in place. Regenerate it from the HEAD diff so the audit trail lists the 22 changes.

## Note edits (item 5)

All 9 are consistency fixes. None introduces a claim, and no claim, canon or coreClaim metadata changed. Six are fine as they stand (gen-2-human-from-the-ground (0,3); gen-3-inquiry; gen-4-offerings; gen-4-killing-and-sign; gen-4-seth-and-the-name; and see below). Four need a wording fix:

| # | Passage / sentence | Problem | Proposed |
|---|---|---|---|
| N1 | gen-2-seventh-day (0,3) "The Reading and the Meaning render the subject in the plural, the Sky People, as the Messages read the word." | Inaccurate for the Meaning: Meaning 2:2 says "those who came from the sky" (first mention). | "The Reading (the Sky People) and the Meaning (those who came from the sky) render the subject in the plural, as the Messages read the word." |
| N2 | gen-2-human-from-the-ground (0,4) "The Meaning follows them and renders YHWH-Elohim as the creators of one team." | The edit to (0,3) moved the antecedent: "them" now reads as "the Reading and the Meaning", which makes the sentence circular. Originally it meant the Messages. | "The Meaning follows the Messages and renders YHWH-Elohim as the creators of one team." |
| N3 | gen-4-births (0,1) "here it keeps the Hebrew “YHWH himself!”." | "YHWH himself!" is the literal English with the transliterated name, not Hebrew. | "here it keeps the literal “YHWH himself!”." |
| N4 | gen-5-enoch (2,1) "verse 24 says that the Sky People took him," | A regression. The preceding sentence ends on Moses and Elijah, so "him" now points to Elijah. The old text said "Enoch". | "verse 24 says that the Sky People took Enoch," |

## Items for the founder

- **F1 (conflict with a ruling).** Meaning 1:27 still says "and each human race corresponds to a team of creators" (TBWTT 2:25). The form-4 ruling of 2026-11-28 keeps that statement OUT of the Genesis lens. Gen 1 was signed off on 11-27, before that ruling. Recommended: delete the clause, so the unit ends "…“the resemblance is striking”."
- **F2 (Meaning vs Reading vocabulary).**
  - Meaning 2:2–3 says the seventh "day" (2:2 puts it in quotation marks); the Reading says "age".
  - Meaning 1:28 says "of the fifth day", where 1:13–1:31 elsewhere use "period".
  - Meaning 4:3–4 and 4:5 say "offering"; the Reading says "food".
  - Recommended: align 1:28 to "fifth period". Keep 2:2–3 as is: the quoted "day" plus the note explains it. In 4:3–5, either use "food" or keep "offering", since the Meaning already glosses it as food. Your call.
- **F3 (3:1 ambiguity).** "was shrewder … They said". The glossary specifies the singular verb. Option: "the small group of creators were shrewder" (notional plural), which ties "They" to the group. This needs a glossary-variant change, so I did not apply it to the review. Recommended: keep as is unless you want the plural.
- **F4 (layer-2 errata to queue, `genesis-layer2-errata.md`).** These need the translation pipeline:
  - 3:19: missing closing quotation mark.
  - 4:10–11: closing quotation mark after 4:10 although the speech continues through 4:12.
  - 4:13–14: closing quotation mark after 4:13 although the speech continues through 4:14.
- **F5 (low).** Meaning 2:4 names the form ("the creators who worked there, whom it calls YHWH-Elohim"). This is consistent with "notes about the Hebrew may name the form", but it sits in the Meaning, not in a note. Recommended: keep it, because it explains the name change.
- **F6.** Confirm the form-5 Meaning naming interpretation ("those who came from the sky" at the first mention per chapter, then "the Sky People"), as the plan asks at sign-off. As applied, the word "Elohim" no longer appears anywhere in the Meaning of Gen 1–5. It remains in the notes.

## Method (reproducible)

- `scratchpad/rev-decoded/diff.py`: an independent token diff of every decoded unit against the layer-2 `i18n.en` verses its refs expand to, plus checks on ref parity and verse coverage.
- `scratchpad/rev-decoded/cmp.py`: compares the Meaning units and note sentences (text and metadata) against `git show HEAD`.
- A quote-balance scan over the decoded units.
- The validator, run with the core catalog: 0 errors.
