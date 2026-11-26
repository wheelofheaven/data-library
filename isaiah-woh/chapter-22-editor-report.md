# Chapter 22 Editor Report

Isaiah 22 (25 verses), wave I-4 (Isa 16–23).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v3.0.0 and isaiah-woh overlay v2.0.0, both read-only. `wave-i4-rulings.md` (rules 1–13) is in force.
All glossary changes are in `wave-i4-ch22-overlay-diff.json` and `wave-i4-ch22-central-diff.json`.

## Summary

- **Editorial questions:** all 21 resolved and folded into glossary ops. None is escalated as an open question. `editorial_questions[]` is empty.
- **English-line changes:** three lines. The chapter title and every other line are the Translator's.
  - 22:5 "For it is a day of tumult … from the Lord YHWH of hosts, in the valley of vision" → "For the Lord YHWH of hosts has a day of tumult … in the valley of vision". The *lᵉ* is read as possessive, as in NJPS and the stable 2:12.
  - 22:23 "as a nail" → "as a peg".
  - 22:25 "the nail" → "the peg".
- **Commentary:** 24 of 25 verses have `notes.official`. 22:10 has none, because it has no crux or divergence. There is no speculative paragraph. The canon (TBWTT, ETTMTTP in data-library) does not cite Isa 22; I grepped for "Isaiah"/"Isaïe" with XXII, "key of David", "valley of vision", Shebna and Eliakim. The chapter has no lens-salient content.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` are left for the orchestrator. The paragraph `translit` fields are untouched.
- **Rulings applied:**
  - Rule 7: "the valley of vision" in lower case at 22:1 and 22:5. The Rev 3:7 parallel is in the 22:22 commentary.
  - Rule 2: "glory" for *kāḇôḏ* at 22:18, 23, 24.
  - Rule 13: "chariots of men" at 22:6.
  - Rule 10: NJPS is the 1985 edition; the Gender-Sensitive Edition was not used. Its 22:21 "the men of Judah" differs from the gender-sensitive "house of Judah".
- **Verification:**
  - ASV Isa 22 (bible-api.com) and JPS 1917 / NJPS 1985 Isa 22 with footnotes (Sefaria API v3) were checked from the Translator's fetches in `scratchpad/ref22/`.
  - ASV Rev 3:7 and 1 Cor 15:32 were checked against data-library `revelation/chapter-3.json` and `1-corinthians/chapter-15.json`.
  - The stable Isaiah lines cited in commentary were read from the chapter files: 1:8, 1:20, 2:12, 3:24, 5:9, 5:12, 9:3, 9:5, 10:3, 10:18, 10:27, 11:5, 13:3, 14:11, 14:25, 15:2–3, 29:16, 32:13, 42:5, 44:3, 48:19, 54:2, 54:5 and 65:23.
  - Not verified, and marked so in commentary: NRSV 22:5; the LXX of 22:13 and 22:22; the Targum's "second death" at 22:14; HALOT on *skn* and on *ʿṭh* II; Avigad 1953 on the Silwan inscription; Strong's numbers.

## Speculative entries requiring sign-off

None. No speculative glossary entry and no speculative commentary.

---

## Unresolved editorial questions

None open. Four items are flagged for the orchestrator or founder. None blocks the chapter.

### `ISA-22:5` — departure from ASV / JPS 1917 ("has a day")

**Issue:** The line now reads the *lᵉ* as possessive, "For the Lord YHWH of hosts has a day of tumult …". This follows NJPS and makes the verse concordant with the stable 2:12 ("there is a day of YHWH of hosts"). ASV and JPS 1917 read "from the Lord".
**Options considered:**
- A. Possessive (adopted).
- B. ASV "from the Lord" (the draft).
**Why flagging:** this is the chapter's only grammatical departure from the ASV baseline. It is recorded in `lexical-cruxes-isaiah-22`, and reverting it means changing one line.

### `ISA-22:23, 25` — *yāṯēḏ* "peg", with "stake" at 54:2

**Issue:** The new entry `yated-peg-stake-isaiah` splits the word by context:
- "peg" where the object is driven in and carries a load (22:23, 25; JPS 1917, NJPS);
- "stake(s)" for tent pegs (stable 54:2, unchanged; 33:20 when drafted).

ASV "nail" is retired.
**Options considered:**
- A. "peg" with a context clause for "stake" (adopted).
- B. "stake" everywhere. This gives full concordance with 54:2, but "a stake … hung with cups and flagons" is unnatural English.
- C. ASV "nail".

**Orchestrator action:** add the id to ISA-54:2 `glossaryRefs` at merge.

### `ISA-22:18, 23, 24` — non-divine *kāḇôḏ* has no book-wide entry

**Issue:**
- The strict "glory" rule (ruling 2) for non-divine *kāḇôḏ* is recorded chapter by chapter in the `lexical-cruxes-isaiah-N` entries (10, 11, 17, and now 22).
- `kevodo-kavod-suffixed-isaiah` covers only the divine 3:8 and 6:3.

**Recommendation:** at merge, consider one book-wide *kāḇôḏ* concordance entry, parallel to the *tip̄ʾereṯ* split the chapter 20 Editor recommended. **Ruled 2026-11-26: adopted** (`kavod-nondivine-glory-isaiah`).

### `ISA-22:15` — *sōḵēn* "treasurer" against "steward"

**Issue:**
- ASV "treasurer" is kept as the public-domain baseline.
- JPS 1917, NJPS and the cognates (Ugaritic and Phoenician *skn* "prefect"; recalled) favour "steward".

**Recommendation:** keep the line. If the founder prefers "steward", change the line and the wohChoice clause together. **Ruled 2026-11-26: "steward"** (see the final section).

---

## Decisions on the Translator's questions

| # | refId | Question | Decision | Entry |
|---|---|---|---|---|
| 1 | 22:1 | case of *gêʾ ḥizzāyôn* | "the valley of vision", lower case (ASV; ruling 7); same at 22:5 | `lexical-cruxes-isaiah-22`; `massa-oracle-superscription-isaiah` (ext.) |
| 2 | 22:3 | *miqqešeṯ ʾussārû* | "bound by the archers" kept (ASV); the privative reading of JPS 1917 / NJPS is in commentary | `lexical-cruxes-isaiah-22` |
| 3 | 22:4 | *baṯ-ʿammî*; tense of *ʾāmartî* | "the daughter of my people"; "I said" (ASV, JPS 1917); appositional sense and NJPS present tense in commentary; central promotion recommended when Jeremiah or Lamentations is drafted | `lexical-cruxes-isaiah-22` |
| 4 | 22:5 | "from" or possessive *lᵉ* | possessive (NJPS; 2:12); **line changed** | `lexical-cruxes-isaiah-22`; `adonai-yhwh-compound-isaiah-25` (ext.) |
| 5 | 22:5 | *qir* / *šôaʿ* | common nouns, singular as MT; Kir / Shoa as peoples in commentary | `lexical-cruxes-isaiah-22` |
| 6 | 22:6 | *rekeḇ ʾāḏām*, gender scope | "chariots of men and horsemen" (ruling 13); "and" supplied, as ASV | `lexical-cruxes-isaiah-22`; `adam-humankind-ish-man-isaiah` (scope note) |
| 7 | 22:8 | subject of *wayᵉḡal*; *bêṯ hayyaʿar* | "he took away" (ASV); "the house of the forest", lower case | `lexical-cruxes-isaiah-22` |
| 8 | 22:11 | *ʿōśêhā … yōṣᵉrāh* | "the one who made it … the one who formed it long ago"; plural-in-form participle and open referent in commentary | central `asah`, `yatsar` (ext.); `yotser-potter-clay-image-isaiah` (ext.) |
| 9 | 22:13 | cohortative; 1 Cor 15:32 | "Let us eat and drink, for tomorrow we shall die" (ASV, JPS 1917); Pauline parallel in commentary, LXX not verified | `lexical-cruxes-isaiah-22`; `title-and-meta-conventions-isaiah` (ext.) |
| 10 | 22:14 | *niḡlāh*; *kpr* | "revealed himself in my ears"; "atoned for" (as 6:7; 27:9); no quotation marks | `kupar-atonement-isaiah` (ext.); central `avon-iniquity-cross-corpus-keyword` (ext.); `title-and-meta-conventions-isaiah` (ext.) |
| 11 | 22:15 | *sōḵēn*; *ʾăšer ʿal-habbāyiṯ*; "[and say]" | "treasurer" (ASV; "steward" flagged); "who is over the house"; nothing supplied | `lexical-cruxes-isaiah-22` |
| 12 | 22:16 | person shift; tomb / sepulchre | third person kept (ASV alone; JPS 1917 and NJPS use the second person — corrected post-review); "tomb" | `lexical-cruxes-isaiah-22` |
| 13 | 22:17 | *gāḇer*; *ʿṭh* | ASV construal, brackets dropped; alternatives in commentary | `lexical-cruxes-isaiah-22` |
| 14 | 22:18 | *ṣnp*; *kāḇôḏ*; *ʾăḏōneyḵā* | "wind you round and round, like a ball"; "the chariots of your glory"; "your lord", lower case | `lexical-cruxes-isaiah-22`; central `eretz` (ext.) |
| 15 | 22:19 | person shift | passive kept (all three references); MT third person in commentary | `lexical-cruxes-isaiah-22` |
| 16 | 22:21 | girdle / sash; government / authority | ASV "robe", "girdle", "government" kept; collisions with 3:24, 11:5 and 9:5 stated in commentary | `lexical-cruxes-isaiah-22` |
| 17 | 22:22 | key / keys; Rev 3:7 | "the key of the house of David"; Rev 3:7 and Matt 16:19 in commentary; central Gen 48:22 entry not applied | `lexical-cruxes-isaiah-22` |
| 18 | 22:23 | *yāṯēḏ* | "peg"; **lines changed** at 22:23 and 22:25; Eliakim / Shebna referent of v. 25 in commentary | `yated-peg-stake-isaiah` (new) |
| 19 | 22:23 | *kissēʾ ḵāḇôḏ* | "a throne of glory" (ruling 2; ASV; 1 Sam 2:8) | `lexical-cruxes-isaiah-22` |
| 20 | 22:24 | offspring / sprouts; vessels | "the offspring and the issue"; "cups … flagons"; repeated *kᵉlê* kept; *nēḇel* II against *nēḇel* I in commentary | `lexical-cruxes-isaiah-22` |
| 21 | 22:25 | *maśśāʾ* I "burden" | "the burden" kept; the oracle entry's commentary-only clause does not reach *maśśāʾ* I (scope note added) | `massa-oracle-superscription-isaiah` (ext.); `lexical-cruxes-isaiah-22` |

---

## Glossary changes for review

### Central glossary (proposed 3.0.0 → 3.1.0)

- Modified, appliesTo plus rationaleAppend only (no wohChoice or claim_type changed):
  - `asah` (+22:11)
  - `yatsar` (+22:11)
  - `avon-iniquity-cross-corpus-keyword` (+22:14)
  - `eretz` (+22:18)
- Deliberate non-extensions:
  - `shekhem-achad-polysemy-historical-redactional-crux` (22:22)
  - `kavod-yhwh` (22:18, 23, 24)

### Per-translation overlay (proposed 2.0.0 → 2.1.0)

- Added:
  - `lexical-cruxes-isaiah-22` (claim_type: `direct`)
  - `yated-peg-stake-isaiah` (claim_type: `direct`; lists stable ISA-54:2 with no line change)
- Modified, appliesTo plus rationaleAppend only (no wohChoice or claim_type changed):
  - `title-and-meta-conventions-isaiah` (+22:1, 4, 13, 14, 15, 17)
  - `massa-oracle-superscription-isaiah` (+22:1; scope note on *maśśāʾ* I)
  - `yhwh-tzevaot-hosts-isaiah` (+22:5, 12, 14, 15, 25)
  - `adonai-yhwh-compound-isaiah-25` (+22:5, 12, 14, 15)
  - `kupar-atonement-isaiah` (+22:14)
  - `yotser-potter-clay-image-isaiah` (+22:11)
  - `adam-humankind-ish-man-isaiah` (rationale-only scope note under ruling 13; no appliesTo added)

---

## Post-review corrections

The Reviewer returned the chapter as `awaiting-human`. These corrections need no founder decision. `translation.status`, the `reviewerReport` block, every English line and both shared glossaries are unchanged.

1. **22:16, person attribution (factual correction).**
   - The draft claim was that the third person is kept "with ASV and JPS 1917". That was wrong: JPS 1917 uses the second person ("Thou that hewest thee out a sepulchre on high, And gravest a habitation for thyself in the rock"), as NJPS does.
   - The third person is kept with ASV alone.
   - Corrected in three places:
     - the 22:16 `notes.official`;
     - the `lexical-cruxes-isaiah-22` wohChoice clause and rationale sentence in `wave-i4-ch22-overlay-diff.json`;
     - row 12 of the decisions table above.
2. **22:15, "treasurer" or "steward" (staged for the founder; ruled "steward" 2026-11-26, see the final section).**
   - The line stays "treasurer".
   - The alternative line "Go, get you to this steward, to Shebna, who is over the house:" was staged in the `lexical-cruxes-isaiah-22` wohChoice for the founder. If it is adopted, the line and that clause change together.
   - The rationale now records the Reviewer's recommendation of "steward" and the probable LXX origin of "treasurer" (recalled, not verified).

---

## Founder rulings applied (sign-off 2026-11-26)

The founder (zarazinsfuss) signed off wave I-4 on 2026-11-26, choosing every recommended option in `wave-i4-signoff-package.md`. `translation.status` and the `reviewerReport` block are unchanged; the orchestrator promotes the chapter. Statements above marked pending, staged or escalated are settled as follows.

- **Decision 5, 22:15:** the line is now "Thus says the Lord YHWH of hosts: Go, get you to this steward, to Shebna, who is over the house:". The 22:15 note gives "steward" (JPS 1917, NJPS) and reports ASV "treasurer"; the `lexical-cruxes-isaiah-22` wohChoice and rationale record the ruling (two items now depart from ASV: 22:5 and 22:15), and the PENDING marker is gone.
- **Decision 9, non-divine kāḇôḏ:** the book-wide overlay entry `kavod-nondivine-glory-isaiah` (direct) is created at merge through `wave-i4-orchestrator-ops.json` (`overlay.add`). This chapter's sites 22:18, 22:23 and 22:24 carry it in glossaryRefs, and the `lexical-cruxes-isaiah-22` wohChoice points to it.
