# Isaiah wave I-1 (chapters 1–5) — sign-off package

**Status:** all five chapters `awaiting-human`, version `1.0.0-rc1`. Source: Westminster Leningrad
Codex via Sefaria ("Tanach with Ta'amei Hamikra", public domain), `source-he-1..5.json`.
Pipeline: Translator → Editor → independent Reviewer → post-review corrections (2026-11-26).
Model: claude-opus-5-5 in all three roles.

| Ch. | Title | Verses | Commentary | Reviewer verdicts | Overlay ops | Central ops |
|---|---|---:|---:|---|---:|---:|
| 1 | Hear, O skies: the rebellious children, the worthless offerings, and the faithful city | 31 | 22 | 29 approve · 1 revise (1:31) · 1 flag (1:29) | 9 | 10 |
| 2 | The mountain of the house of YHWH and the day against all that is lofty | 22 | 19 | 19 approve · 3 flag (2:9, 2:20, 2:22) | 11 | 7 |
| 3 | Jerusalem's leaders judged and the daughters of Zion stripped of their finery | 26 | 22 | 23 approve · 2 revise (notes, fixed) · 1 flag (3:1) | 11 | 2 |
| 4 | The branch of YHWH and the cloud and fire over Mount Zion | 6 | 6 | 3 approve · 2 revise (notes, fixed) · 1 flag (4:5) | 9 | 2 |
| 5 | The Song of the Vineyard and the six woes | 30 | 18 | 28 approve · 1 revise (5:14 note, fixed) · 1 flag (5:15) | 12 | 6 |
| | **Total** | **115** | **87** | | **52** | **27** |

No speculative glossary entries. No lens leakage in any English line (checked per verse by the
Reviewer). Every "revise" item that was not a founder decision has been applied; see the
"Post-review corrections" section of each `chapter-N-editor-report.md`.

## Decisions (reply "sign-off ok" to accept every recommended default, or name the ones to change)

1. **hā-ʾāḏôn** (1:24, 3:1; later 10:16, 10:33, 19:4) — the articular title, distinct from ʾăḏōnāy.
   - A: "the Lord", with a note at each site (Editors' recommendation).
   - **B: "the Sovereign" (NRSV, NJPS) — recommended**: the book keeps divine titles distinct, and B
     makes the distinction visible in the line. Merge the two proposed entries
     (`ha-adon-articular-title-isaiah`, `ha-adon-definite-title-isaiah`) into one.
2. **ʾāḏām / ʾîš pairs** (2:9, 2:11, 2:17, 2:22, 5:15) — synonymous parallelism, not ASV's "mean man / great man".
   - A: "humankind … man", as drafted.
   - **C1: "humankind is bowed down, and everyone is brought low" — recommended** (Reviewer): avoids
     pairing a neutral and a gendered word for two synonyms; 2:11/2:17 "the loftiness of all people",
     2:22 with plural pronouns. Requires an Editor pass on those five lines.
3. **1:31 ûp̄ōʿălô** — **adopt "its maker" (recommended)**: the MT pointing is the participle (cf. Job
   36:3; the noun would be פָּעֳלוֹ). Line: "And the strong shall become tinder, and its maker a spark;
   and both of them shall burn together, with none to quench them." Reverses ASV/NRSV "his work",
   which moves to commentary.
4. **2:20 "to the moles"** — **adopt the one-word reading (recommended)**: same consonants; the
   Leningrad Codex divides them as two words ("to dig holes"); ASV, NRSV and NJPS all read one word.
   Recorded in `mt-qere-textual-policy-isaiah` as a word-division exception.
5. **4:5 reception paragraph** (labelled speculative, commentary only) — **keep (recommended)**. It now
   quotes the canon's own wording (TBWTT 3:10–14: "we guided them"; the smoke as a curtain) and says
   carrying that reading to Zion is a project extension.
6. **Housekeeping, central glossary** — **fix (recommended)**: the existing `pillar-of-cloud-and-fire-…`
   entry places the canon's Exodus 13:21–22 reading in *Extra-Terrestrials Took Me To Their Planet*; the
   verified site is TBWTT ch. 3 (3:10–14).

## Verifications that could not be completed (disclosed, not blocking)

- 1:29: the reported 1QIsaᵃ second-person reading could not be checked (DJD XXXII not held); the note
  now cites only the MT shift and NRSV.
- Strong's numbers in the new chapter-3 entries are from model recall, marked "not concordance-verified".
- ASV/NRSV citations in commentary are unverified against texts; every NJPS citation in chapter 2 and
  the JPS 1917 citations in chapter 5 were checked against Sefaria.

## Merge work after sign-off (orchestrator)

- Apply the ten diff files to the overlay (1.6.1 → 1.7.0) and the central glossary (2.93.0 → 2.94.0),
  appliesTo merged as unions; one wave-wide `hoy-woe-isaiah` entry (1:4, 1:24; 5:8, 11, 18, 20, 21, 22;
  plus stable 29:1, 29:15, 45:9, 45:10); fold the per-chapter `lexical-cruxes-isaiah-N` entries or keep
  them per chapter; bump each chapter's glossary versions.
- Generate transliterations, promote the chapters to `stable` / `1.0.0`, update `_meta.json`.
- Open item for a later wave: stable 13:19 renders tip̄ʾereṯ "splendor", which now conflicts with
  `hadar-splendor-isaiah` (4:2 uses "honor").

## Files

`chapter-1..5.json`, `chapter-1..5-editor-report.md`, `wave-i1-ch1..5-overlay-diff.json`,
`wave-i1-ch1..5-central-diff.json`, `source-he-1..5.json` — all in `data-library/isaiah-woh/`.
