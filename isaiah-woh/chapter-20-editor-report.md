# Chapter 20 Editor Report

Isaiah 20 (6 verses), wave I-4 (Isa 16–23).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v3.0.0 and isaiah-woh overlay v2.0.0, both read-only. `wave-i4-rulings.md` (rules 1–12) and the coordinator's addendum on `cush-names-isaiah` are in force.
All glossary changes are in `wave-i4-ch20-overlay-diff.json` and `wave-i4-ch20-central-diff.json`.

## Summary

- **Editorial questions:** all 14 resolved and folded into glossary ops. None needed escalation as an open question. `editorial_questions[]` is empty.
- **English-line changes:** two lines and the chapter title.
  - 20:1 "Tartan" → "the Tartan". It is the Assyrian title *turtānu*, and the wording follows NJPS.
  - 20:3 "upon Egypt and upon Cush" → "concerning Egypt and concerning Cush". The draft's wording was JPS 1917's, mislabelled as ASV; the new wording is ASV's.
  - Title: "a sign against Egypt and Cush" → "a sign concerning Egypt and Cush", to match the 20:3 line.
  - Every other line is the Translator's.
- **Commentary:** all 6 verses have `notes.official`. There is no speculative paragraph, because the canon does not cite Isa 20. TBWTT ch. 3 and 5 cite Isa 6, 13–15, 26–27, 29, 32, 40, 42–45, 48, 54 and 65, and the ETTMTTP mention is general. The chapter has no lens-salient content.
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` are left for the orchestrator.
- **"Ethiopia"** appears in no English line. It is used only in commentary and glossary text, as ASV and JPS 1917 wording.
- **Glossary refs to entries that exist only after merge:**
  - `lexical-cruxes-isaiah-20` is added in this chapter's diff.
  - `cush-names-isaiah` at 20:3–5 is added in the chapter 18 Editor's diff, per the coordinator.
- **Verification:**
  - ASV Isa 20, 2 Kgs 18:17, 2 Sam 10:4 and Isa 5:27 were checked via bible-api.com.
  - JPS 1917 and NJPS 1985 ("Tanakh: The Holy Scriptures, published by JPS") Isa 20, with their footnotes, were checked via the Sefaria API v3. The Gender-Sensitive Edition was seen and not used.
  - Checks against the Translator's attributions:
    - The quotation extent 20:3–6, with an inner quotation at 20:6, is confirmed for both JPS editions.
    - NJPS "Nubia", "a sign and a portent" and "their boast" are confirmed.
    - "upon" (20:3) and "ashamed" (20:5) are JPS 1917, not ASV. ASV has "concerning" and "confounded".
  - Not verified, and marked so in commentary:
    - CAD T s.v. *turtānu*.
    - The wording of Sargon II's inscriptions and the Tang-i Var inscription on Yamani.
    - The BDB sense "scantily clad" for *ʿārôm*.
    - The GKC treatment of *ḥăśûp̄ay*.
    - The LXX of 20:3.
    - Strong's numbers.

## Speculative entries requiring sign-off

None. No speculative glossary entry and no speculative commentary.

---

## Unresolved editorial questions

None open. Two items are flagged for the orchestrator or founder. Neither blocks the chapter.

### `ISA-20:1` — "the Tartan" sets a rule for 2 Kgs 18:17

**Issue:** The line supplies the article to show that *tartān* is a title, with NJPS. ASV and JPS 1917 print a bare name. 2 Kgs 18:17 has the same title together with *rab-sārîs* and *rab-šāqēh* (ASV "Tartan and Rab-saris and Rabshakeh"). When 2-kings-woh 18 is drafted, it should follow the same rule.
**Options considered:** A. "the Tartan" (adopted). B. "Tartan" (ASV, JPS 1917). C. "the commander-in-chief" (title translated).
**Why flagging:** this is a cross-book consequence. It is recorded in the `lexical-cruxes-isaiah-20` rationale. If the founder prefers the ASV name form, revert the 20:1 line and drop the item. Nothing else depends on it.

### `ISA-20:5` — the *tip̄ʾereṯ* default sits inside a ṣemaḥ entry

**Issue:** The book default "honor" for *tip̄ʾereṯ* (ruling 2) is recorded only in `tsemach-yhwh-branch-isaiah-4`. This diff extends that entry to 20:5. The stable 13:19 still prints "splendor", which remains unreconciled.
**Recommendation:** at merge, split out a dedicated book-wide *tip̄ʾereṯ* entry covering 4:2, 10:12 (the departure "boasting"), 13:19 (reconcile) and 20:5. **Ruled 2026-11-26: adopted** (see the final section).

---

## Decisions on the Translator's questions

| # | refId | Question | Decision | Entry |
|---|---|---|---|---|
| 1 | 20:1 | *tartān* name or title | "the Tartan" (NJPS); line changed | `lexical-cruxes-isaiah-20` |
| 2 | 20:2 | *bᵉyaḏ* | "spoke by Isaiah" kept (ASV, JPS 1917). NJPS "Previously … had spoken to Isaiah" (note "Lit. 'At that time'") given in commentary | `lexical-cruxes-isaiah-20` |
| 3 | 20:2 | sandal number | "your sandals from your feet" kept (collective; NJPS; 5:27; cf. Josh 5:15) | `lexical-cruxes-isaiah-20` |
| 4 | 20:2 | *ʿārôm* | "naked and barefoot" kept in all 3 verses (ASV, JPS 1917, NJPS); "stripped" sense given in commentary | `lexical-cruxes-isaiah-20` |
| 5 | 20:3 | *ʾôṯ ûmôp̄ēṯ* | "for a sign and a wonder" kept; 8:18 concord | `lexical-cruxes-isaiah-8` (extended) |
| 6 | 20:3 | placement of "three years" | ASV order kept; *ʾaṯnāḥ* construal (JPS 1917) given in commentary | `lexical-cruxes-isaiah-20` |
| 7 | 20:3 | Cush / Ethiopia | "Cush" per ruling 12; ASV/JPS 1917 "Ethiopia" and NJPS "Nubia" given in commentary | `cush-names-isaiah` (ch. 18 diff) |
| 8 | 20:3 | *ʿal* | "concerning" (ASV); line changed from JPS 1917 "upon" | `lexical-cruxes-isaiah-20` |
| 9 | 20:3 | quotation span | 20:3–6 with inner quotation at 20:6; verified in both JPS editions | `title-and-meta-conventions-isaiah` (extended) |
| 10 | 20:4 | *waḥăśûp̄ay šēṯ* | "with buttocks uncovered" kept (ASV, JPS 1917); the form discussed in commentary | `lexical-cruxes-isaiah-20` |
| 11 | 20:4 | *ʿerwaṯ miṣrāyim* | "to the shame of Egypt" kept (all three references); central `ervat-aviv` not extended | `lexical-cruxes-isaiah-20` |
| 12 | 20:5 | *tip̄ʾartām* | "their honor" (book default); NJPS "boast" and ASV "glory" given in commentary | `tsemach-yhwh-branch-isaiah-4` (extended) |
| 13 | 20:5 | *mabbāṭ* | "expectation" in 20:5 and 20:6 (ASV, JPS 1917) | `lexical-cruxes-isaiah-20` |
| 14 | 20:6 | *ʾî*, *yōšēḇ* | "the inhabitant of this coastland" kept | `lexical-cruxes-isaiah-11` (extended) |

---

## Glossary changes for review

### Central glossary

- No ops. The version op is for the audit trail only.
- Deliberate non-extensions: `ervat-aviv` (20:4) and `mitsrayim` (20:3–5).
- The Torah translations print "Kush" (GEN-WOH-10:6–8) and Isaiah prints "Cush". The split is recorded for a possible future central entry.

### Per-translation overlay (proposed 2.0.0 → 2.1.0)

- Added: `lexical-cruxes-isaiah-20` (claim_type: `direct`).
- Modified, appliesTo plus rationaleAppend only (no wohChoice or claim_type changed):
  - `aram-names-isaiah` (+20:1, 3, 4, 5, 6)
  - `title-and-meta-conventions-isaiah` (+20:1, 2, 3, 6)
  - `lexical-cruxes-isaiah-8` (+20:3)
  - `tsemach-yhwh-branch-isaiah-4` (+20:5)
  - `lexical-cruxes-isaiah-11` (+20:6)
- Dependency: `cush-names-isaiah` comes from the chapter 18 Editor. Make sure its appliesTo includes ISA-20:3, 20:4 and 20:5.

## Post-review corrections

- 2026-11-26: the `standardEnglish` of `lexical-cruxes-isaiah-20` (overlay diff) now lists three more JPS 1917 differences: "came into Ashdod" (20:1), "Like as My servant Isaiah" (20:3), and 20:6 "and how shall we escape?" without "and we". This is a documentation fix only: no line, decision, status or reviewerReport changed.

---

## Founder rulings applied (sign-off 2026-11-26)

The founder (zarazinsfuss) signed off wave I-4 on 2026-11-26, choosing every recommended option in `wave-i4-signoff-package.md`. `translation.status` and the `reviewerReport` block are unchanged; the orchestrator promotes the chapter. Statements above marked pending, staged or escalated are settled as follows.

- **Decision 9, tip̄ʾereṯ:** the book-wide overlay entry `tiferet-honor-isaiah` (direct) is created at merge through `wave-i4-orchestrator-ops.json` (`overlay.add`). It governs 4:2 and 20:5 ("honor") and records the departures 3:18 "finery", 10:12 "boasting", 13:19 "splendor" and 44:13 "beauty". The tsemach-yhwh-branch-isaiah-4 extension to 20:5 is withdrawn from `wave-i4-ch20-overlay-diff.json` (its reasoning is carried by the new entry), the 20:5 glossaryRef is changed to `tiferet-honor-isaiah`, and the 20:5 note cites it. No English line changes.
- **20:1 "the Tartan":** the recommended default stands.
