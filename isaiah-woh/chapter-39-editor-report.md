# Chapter 39 Editor Report

Isaiah 39 (8 verses), wave I-6 (Isa 36–39, 41).
Editor: claude-opus-5-5 (editor), 2026-11-27.
Base: central glossary v5.0.0 and isaiah-woh overlay v4.0.0, both read-only, with `wave-i6-rulings.md` in force.
All glossary changes are in `wave-i6-ch39-overlay-diff.json` (proposed 4.1.0) and `wave-i6-ch39-central-diff.json` (proposed 5.1.0).

## Summary

- **Editorial questions:** all 11 are resolved and `editorial_questions[]` is empty. One (39:7 sārîsîm) is decided in the line and escalated as a founder decision. One (39:1, the name at 2 Kgs 20:12) is escalated as a cross-book recommendation.
- **English-line changes:** one verse changes, backed by the overlay `lexical-cruxes-isaiah-39`.
  - 39:2: "the precious oil" → "the fine oil". ASV uses "precious" for two different Hebrew words in this verse (nᵉḵōṯ and ṭôḇ). The change keeps "precious" for nᵉḵōṯ only.
- **Commentary:** all 8 verses have `notes.official`. Each records where the 2 Kgs 20:12–19 parallel differs (wave rule 3). No verse has a speculative paragraph.
- **glossaryRefs:** updated on every verse. The Translator's reference to `roeh-chozeh-seer-visionary-isaiah` at 39:3 is removed, because that entry is scoped to 30:10. `lexical-cruxes-isaiah-39`, `minchah-tribute-gift-of-appeasement`, `saris-court-official-eunuch-ambiguity` and `heikhal-temple-palace-isaiah` are added where they apply.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" is added to `modelDrafts`. `glossaryVersion` (5.0.0) and `overlayGlossaryVersion` (4.0.0) are unchanged; the orchestrator sets them on merge. No paragraph `translit` was added.
- **Lens audit:** no English line carries a project reading. The canon in data-library does not cite Isa 39 or 2 Kgs 20:12–19: there are no matches for Hezekiah, Merodach, eunuch or the Babylon embassy in TBWTT, ETTMTTP or LWTE (the only "Babylon" hit is LWTE 4:105, "The Epic of Gilgamesh, Sumarian-Babylonian"). No source supports a premise for a speculative note (wave rule 4), so none is written.
- **Verification (2026-11-27):**
  - ASV and KJV Isa 39, ASV 2 Kgs 20:12–19 and ASV Isa 56:3–4, all through bible-api.com.
  - JPS 1917 and NJPS of Isa 39, 2 Kgs 20:12–19 and Isa 56:3–4 through the Sefaria API v3. NJPS is "Tanakh: The Holy Scriptures, published by JPS" (1985), not the Gender-Sensitive Edition. The NJPS notes at 2 Kgs 20:12, 13 and 19 and at Isa 39:8 were checked too.
  - Everett Fox, *The Early Prophets* (2014), and the Metsudah Tanach at 2 Kgs 20:12–19, text and notes, through Sefaria.
  - The MT of 2 Kgs 20:12–19 (WLC through Sefaria) and of Isa 37:14 (source-he-37.json).
  - A search of the MT sources for Isa 36–38 and 41 found no sārîs.
  - Not verified, and marked "recalled" or "not verified" where they are mentioned: LXX, 1QIsaᵃ, NRSV, BDB/HALOT, the Akkadian *bīt nakkamti* etymology of nᵉḵōṯ, and Strong's numbers. Cogan and Tadmor, and the *ša rēši* etymology, are cited only through Fox's note and through the central entry.
  - No JPS 1917 reading is presented as ASV.

## Speculative entries requiring sign-off

None. The new entry `lexical-cruxes-isaiah-39` is `claim_type: direct`. The central `saris` entry stays `inferred`. No commentary paragraph is labelled speculative.

---

## Founder decision

### ISA-39:7 — sārîsîm "eunuchs": how far it reaches in Isaiah (central `saris-court-official-eunuch-ambiguity`)

**Issue:** the central entry's wohChoice is "an officer". It was chosen at Gen 37:36 and 39:1 because Potiphar has a wife, and the entry was later extended to Gen 40:2, 7 and 1 Kgs 22:9. Its rationale says the two senses "must be adjudicated context-by-context". The Translator left the entry unapplied and printed "eunuchs".

**Evidence (checked):**
- ASV, KJV and NJPS have "eunuchs" at Isa 39:7. JPS 1917 has "officers" here and at 2 Kgs 20:18.
- Isa 56:3–4 (ASV and JPS 1917 "the eunuch … a dry tree"; NJPS "a withered tree") makes the castration sense explicit.
- Isa 39:7 and 56:3–4 are the only sārîs sites in Isaiah. A consonant search of the wave sources confirms that 36–38 and 41 have none.

**Decision taken in the line:** "and they shall be eunuchs in the palace of the king of Babylon".

**Staged ops:**
- appliesTo ISA-39:7 on the central entry.
- A `changes.wohChoice` that appends a context clause and leaves the existing sentence as it is: "eunuch(s)" in Isaiah where the context favours the castration sense, which means 39:7 and, as a forward commitment, 56:3–4. 2 Kgs 20:18 will follow Isa 39:7.
- claim_type stays `inferred`.

**Why escalate:** the clause makes "eunuch" a book rule for Isaiah and binds 56:3–4, a chapter not yet drafted. It also binds 2 Kgs 20:18 under rule 3. That reaches past this chapter.

**Options:**
- (A) Accept the context clause (recommended).
- (B) Keep "eunuchs" at 39:7 on context alone, with no book rule. Keep the appliesTo extension and drop `changes`; 56:3–4 is then decided by its own Editor.
- (C) Apply the central default and print "officials" at 39:7, as JPS 1917 does ("officers"). The line and the 39:7 commentary would then change.

**Semver:** minor if treated like the earlier context clauses (eretz, yeor, goel pāḏâ); major if any wohChoice edit counts as a modification.

---

## Unresolved editorial questions

### `ISA-39:1` — the royal name at the 2 Kgs 20:12 parallel

**Issue:** Isaiah's MT has *mᵉrōḏaḵ*; 2 Kgs 20:12 has *bᵉrōʾḏaḵ*. ASV, JPS 1917 and NJPS print "Berodach-baladan" in Kings, and NJPS adds a note citing "Merodach" in several manuscripts and Isa 39:1. The Akkadian name is Marduk-apla-iddina (II).
**Decided for Isaiah:** "Merodach-baladan son of Baladan" (MT Isaiah, ASV).
**Options for Kings:** (A) "Berodach-baladan", the Kings MT and ASV Kings, with a note referring to Isa 39:1. This is recommended: it follows rule 3's "render each verse on its own Hebrew" and the ASV-spelling rule. (B) "Merodach-baladan", which harmonises with Isaiah against the Kings MT.
**Why escalating:** rule 3 makes Isaiah set the shared wording, but the two books have different consonants here. The Editor cannot decide for a book that is not yet in the corpus.

### `ISA-37:14` — coordination (not blocking)

At 39:1 the line has "letters" for sᵉp̄ārîm, keeping the plural. At 37:14 the same plural is read with a singular suffix (*wayyiqrāʾēhû*), which shows that one letter is meant. The chapter 37 Editor should give hassᵉp̄ārîm the same rendering ("the letters", with the suffix noted) or ask for 39:1 to be revised.

---

## How each editorial question was resolved

| # | refId | Question | Resolution |
|---|---|---|---|
| 1 | 39:1 | Royal name | "Merodach-baladan son of Baladan" kept; the Kings form is escalated (above). `lexical-cruxes-isaiah-39`. |
| 2 | 39:1 | sᵉp̄ārîm ûminḥāh | "letters and a present" kept (ASV). sēp̄er is "letter", outside `sefer-sealed-scroll-isaiah-29`. Central `minchah` extended to ISA-39:1. |
| 3 | 39:2 | Ketiv/qere nᵉḵōṯô | The qere is followed. `mt-qere-textual-policy-isaiah` is extended to ISA-39:2, and the orchestrator adds "39:2" to its wohChoice list. "the house of his precious things" kept (ASV). |
| 4 | 39:2 | wayyiśmaḥ vs Kings wayyišmaʿ | "was glad of them" kept (MT Isaiah, ASV, JPS 1917). Kings, NJPS and Fox are in commentary. |
| 5 | 39:2 | haššemen haṭṭôḇ | **Line change:** "the fine oil" (Fox, Metsudah at 2 Kgs 20:13). |
| 6 | 39:2 | bêṯ kēlāyw | "all the house of his armor" kept (ASV). The wider sense of kᵉlî is in commentary. |
| 7 | 39:6–7 | fathers / sons | Kept, because these are specific male groups (wave I-4 rule 13). NJPS "ancestors" is in commentary. |
| 8 | 39:7 | yiqqāḥû | "they shall take away" kept (pausal Qal impf. 3mp, impersonal). The ketiv/qere at 2 Kgs 20:18 was checked and is recorded. |
| 9 | 39:7 | sārîsîm | "eunuchs" kept. Central context clause staged; **founder decision** (above). |
| 10 | 39:7 | hêḵal | "palace" kept. Context clause added to the overlay `heikhal-temple-palace-isaiah` (changes.wohChoice + appliesTo). Central `ulam-hekhal` extended to ISA-39:7. |
| 11 | 39:8 | Closing clause | ASV construal kept. The inner-speech, optative and Kings-question readings are in commentary. ʾĕmeṯ "truth", as at 10:20, 16:5, 42:3 and 48:1; šālôm "peace". The central `chesed-v-emet` and the overlay `ra-calamity-shalom` are not applied. |

---

## Glossary changes for review

### Central glossary (proposed 5.0.0 → 5.1.0)

- Modified: `saris-court-official-eunuch-ambiguity`: appliesTo + ISA-39:7; wohChoice gains an Isaiah context clause ("eunuch(s)" at 39:7 and, as a forward commitment, 56:3–4); rationale addendum. claim_type unchanged (`inferred`). **Founder decision.**
- Modified: `minchah-tribute-gift-of-appeasement`: appliesTo + ISA-39:1, with a rationale addendum.
- Modified: `ulam-hekhal-devir-temple-three-room-plan-cross-corpus`: appliesTo + ISA-39:7 (under the existing palace context clause), with a rationale addendum.

### Per-translation overlay (proposed 4.0.0 → 4.1.0)

- Added: `lexical-cruxes-isaiah-39` (claim_type: `direct`).
- Modified: `title-and-meta-conventions-isaiah`: appliesTo + 39:1, 5, 6, 7, 8. The title is ratified, and the quotation-mark span 39:5–7 is recorded.
- Modified: `yhwh-tzevaot-hosts-isaiah`: appliesTo + 39:5; records the Kings difference.
- Modified: `mt-qere-textual-policy-isaiah`: appliesTo + 39:2; rationale addendum. The orchestrator adds "39:2" to the qere list in wohChoice.
- Modified: `heikhal-temple-palace-isaiah`: appliesTo + 39:7. `changes.wohChoice` appends the palace context clause and leaves the existing sentence as it is; rationale addendum.

Deliberate non-extensions: `sefer-sealed-scroll-isaiah-29`, `roeh-chozeh-seer-visionary-isaiah`, `ra-calamity-shalom-well-being-isaiah-45-7`, `adam-humankind-ish-man-isaiah`, and central `chesed-v-emet-steadfast-love-and-truth`.

---

## Post-review corrections

Applied 2026-11-27 after the Reviewer's report (status `awaiting-human`). `translation.status`, the `reviewerReport` block, every English line and the shared glossaries are unchanged. Only commentary and this wave's diff files were edited.

1. **ISA-39:2 note (Reviewer: revise).** The cross-reference now quotes the project's 22:8 line, "the armor of the house of the forest". It also notes that the noun there is *nešeq*, not *kᵉlî*, so "armor" renders both nouns, as in ASV. This replaces the earlier wording "the weapons of the house of the forest", which the project does not print.
2. **ISA-39:7 note and the central `saris-court-official-eunuch-ambiguity` rationaleAppend (Reviewer: revise / flag-for-human).**
   - Both now record that at 2 Kgs 20:18 Fox ("officials", with hêḵāl "the Great-Hall") and the Metsudah Tanach ("officers") join JPS 1917 for the court-official reading. That makes three checked versions.
   - The hêḵāl paragraph of the note adds Fox's "the Great-Hall".
   - The closing sentence of the central addendum now cites JPS 1917, Fox and Metsudah.
   - The founder decision on the context clause stands as escalated above.
3. **`lexical-cruxes-isaiah-39` rationale (Reviewer: revise).** "except one" is now "except two": the partitive "some of your sons" (39:7; NJPS, Fox, Metsudah, against ASV and JPS 1917 "of thy sons") and "the fine oil" (39:2; Fox, Metsudah).
4. **Orchestrator ruling on 37:14 / 39:1 sᵉp̄ārîm.** Both verses use one noun, "letter", and the number follows each verse's grammar: 37:14 "the letter", with its singular suffixes, and 39:1 "letters".
   - The ruling is recorded in the wohChoice and rationale of `lexical-cruxes-isaiah-39`, in the overlay version note, and in the 39:1 commentary.
   - It supersedes the "ISA-37:14 — coordination" item under Unresolved editorial questions.

## Founder rulings applied (sign-off 2026-11-27)

The founder signed off wave I-6 on 2026-11-27, choosing every recommended option.

- **ISA-39:7 *sārîsîm* (option A).** The central `saris-court-official-eunuch-ambiguity` context clause is accepted as the Isaiah book rule: "eunuch(s)" at 39:7 and 56:3–4, with 2 Kgs 20:18 following Isa 39:7. The "FOUNDER DECISION … if declined" text in the `wave-i6-ch39-central-diff.json` version note is replaced by the ruling. In the 39:7 note, "staged in this wave and awaiting founder sign-off" is removed; it now reads "The central entry's Isaiah context clause gives “eunuch” at both sites." The line is unchanged.
- **Open item, not decided now:** the name at 2 Kgs 20:12. "Berodach-baladan" (the Kings MT and ASV Kings, with a note referring to Isa 39:1) remains the recommendation, to be ruled when 2 Kings is translated. The `lexical-cruxes-isaiah-39` wording ("is escalated") is left as it is.
- `translation.status` and the reviewerReport were not touched.
