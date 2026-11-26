# Chapter 31 Editor Report

Isaiah wave I-5. Base: central glossary 4.0.0 and overlay 3.0.0, both read-only.
Status: `editor-review`. Version: `1.0.0-rc1`.
All 9 editorial questions are resolved and the array is empty.
All 9 verses carry official commentary.
These sources were checked on 2026-11-26:

- Sefaria API v3 for JPS 1917 and NJPS (the 1985 "Tanakh: The Holy Scriptures, published by JPS", not the Gender-Sensitive Edition).
- bible-api.com for ASV (Isa 31; 29:7–8).
- The project's canon texts in data-library (TBWTT chs. 3 and 5; ETTMTTP; LWTE).

Lexica (BDB, HALOT) and commentators (Wildberger, Blenkinsopp, Childs) are cited as "recalled, not verified" wherever they appear.

## Speculative entries requiring sign-off

No glossary entry is speculative.
One commentary paragraph is labelled speculative under wave I-5 ruling 4.

### ISA-31:5 commentary, final paragraph ("Wheel of Heaven reading")

**Source:** *yērēḏ YHWH ṣᵉḇāʾôṯ* "YHWH of hosts will come down" (31:4); *kᵉṣippŏrîm ʿāp̄ôṯ* "Like birds hovering" (31:5); *ʾûr … tannûr* "fire … furnace" (31:9).
**WoH choice:** The lines are unchanged and philological (ASV; JPS 1917).
Only the commentary carries the reading.
**Why speculative:** The canon does not cite Isa 31.
TBWTT cites Isaiah only in chs. 3 and 5 (6, 13, 14, 15, 26, 27, 29, 32, 40, 42, 43, 44, 45, 48, 54, 65), ETTMTTP only 43:6, and LWTE none.
The paragraph quotes TBWTT 3:24, 26 on Exod 19:18 ("They came down in a flying craft") and says that applying it to Isa 31 goes beyond the canon.
It also states that the Hebrew is an explicit simile and that the furnace words differ (*tannûr* here, *kiḇšān* in Exod 19:18).
**Recommendation:** Ship as labelled, following the founder's practice at 4:5, 19:1 and elsewhere.

---

## Unresolved editorial questions

None blocks the chapter.
The Reviewer and the founder should check these judgement calls.

### `ISA-31:4` (*liṣbōʾ ʿal-har-ṣiyyôn*)

**Issue:** *ṣbʾ ʿal* means "fight against" elsewhere. The stable 29:8 prints the same phrase as "fight against Mount Zion", and NJPS reads 31:4 as "make war / Against the mount and the hill of Zion".
**Options considered:** (A) "to fight upon" (ASV, JPS 1917; taken). (B) "to fight against" (NJPS; concordant with 29:8). (C) "to fight for" (no lexical support).
**Decision:** (A). It renders *ʿal* by its spatial sense, which the same verse uses for the lion "over his prey", and leaves the threat or rescue question open.
**Why flagged:** If the founder prefers strict concordance with 29:8, the line becomes "to fight against Mount Zion and against its hill". The commentary already states both readings.

### `ISA-31:6` (person shift; line changed)

**Decision:** The line keeps MT's third person, following NJPS: "Turn, O children of Israel, to him from whom they have deeply revolted."
ASV and JPS 1917 change the clause to the second person.
**Why flagged:** This departs from the ASV baseline and moves the vocative forward. The alternative is to restore the ASV line and report MT's person in commentary.

### `ISA-31:8` (*lāmas*; cross-corpus)

**Issue:** The line has "forced labor" (the draft's choice; ASV "taskwork").
The central `mas-oved-corvee-labor-institutional-vocabulary-cross-corpus` prints "taskwork" for *mas ʿōḇēḏ* at Gen 49:15 (genesis-woh).
**Decision:** I kept "forced labor" and did not extend the central entry, because it is scoped to the compound.
**Why flagged:** The corpus now has two English words for *mas*. The founder may want a central ruling when Kings (1 Kgs 5:27; 9:15, 21) reaches the library.

### `ISA-31:3` (*rûaḥ* scope)

**Decision:** Lower-case "spirit" under `ruach-divine-spirit-lower-case-isaiah`, extended to a third context: the divine order of being set against flesh.
"Breath" was rejected because horses breathe.
**Why flagged:** This is a scope extension of an existing entry. The wohChoice text is unchanged, and the addendum records the new context.

---

## Line changes (each governed by a glossary entry)

1. **31:6**: "Turn to him from whom you have deeply revolted, O children of Israel." became "Turn, O children of Israel, to him from whom they have deeply revolted." Entry: `lexical-cruxes-isaiah-31`.
2. **31:7**: "shall cast away" became "shall reject" for *yimʾāsûn* (*mʾs*), with NJPS and concordant with 5:24. "Cast away" stays reserved for *hišlîḵ* (2:20). Entry: `lexical-cruxes-isaiah-31`.
3. **31:9**: "for terror" became "by reason of terror" (ASV, JPS 1917). Entry: `lexical-cruxes-isaiah-31`.

All other lines are the Translator's draft, unchanged.

## Editorial questions: resolutions

- 31:1 *pārāšîm*: "horsemen" kept (book usage 21:7; 22:6–7). `lexical-cruxes-isaiah-31`.
- 31:2 *wayyāḇēʾ rāʿ*: ASV future "will bring evil" kept. JPS 1917 present, NJPS past and NJPS "misfortune" are in commentary. The 45:7 "calamity" entry is not extended.
- 31:3: "the Egyptians are human, and not God … flesh, and not spirit" kept. Extends `adam-humankind-ish-man-isaiah`, `elohim-el-eloah-monotheistic-formula-isaiah` and `ruach-divine-spirit-lower-case-isaiah`.
- 31:4: "fight upon" kept (see above).
- 31:5: ASV kept. The Passover echo of *psḥ* is in commentary only.
- 31:6: changed (see above).
- 31:7: "reject" adopted; "everyone … their" and "as a sin" kept. Extends `adam-humankind-ish-man-isaiah` and central `elilim-idols-cross-corpus`.
- 31:8: "a sword not of a human … not of humankind", "Assyria" and "forced labor" kept. NJPS *nss*/*mss* readings are in commentary.
- 31:9: "his rock", "signal" (extends `nes-signal-isaiah`), "fire" and "furnace" kept. "for terror" changed.

## Glossary changes for review

### Central glossary (`wave-i5-ch31-central-diff.json`, proposed 4.0.0 → 4.1.0)

- Modified: `elilim-idols-cross-corpus` (appliesTo + ISA-31:7; rationale addendum; no field changed).

### Per-translation overlay (`wave-i5-ch31-overlay-diff.json`, proposed 3.0.0 → 3.1.0)

- Added: `lexical-cruxes-isaiah-31` (claim_type: `direct`).
- Modified (appliesTo + rationale addendum only): `hoy-woe-isaiah` (31:1), `title-and-meta-conventions-isaiah` (31:1, 4, 9), `yhwh-tzevaot-hosts-isaiah` (31:4, 5), `adam-humankind-ish-man-isaiah` (31:3, 7, 8), `elohim-el-eloah-monotheistic-formula-isaiah` (31:3), `ruach-divine-spirit-lower-case-isaiah` (31:3), `nes-signal-isaiah` (31:9).

## Post-review corrections

These follow the Reviewer's report (2026-11-26T19:03:04Z, verdicts in `chapter-31.json`).
No English line, `translation.status` (`awaiting-human`) or `reviewerReport` was changed, and no shared glossary was edited.

1. **ISA-31:5 commentary (Reviewer: revise).** The speculative paragraph said "The Hebrew uses the common verbs of descent and flight inside an explicit simile". Only the flight verb is inside a simile; *yērēḏ* is the main clause of v. 4. The sentence now uses the Reviewer's wording: "The verb of flight stands inside an explicit simile (*kᵉ-* “like”); the verb of descent completes the lion simile of v. 4 and is the ordinary verb of a divine descent (Exod 19:20; Mic 1:3); and the furnace of v. 9 (*tannûr*) is a different word from the *kiḇšān* of Exod 19:18."
2. **ISA-31:6 commentary (Reviewer: revise).** The note gave ASV's wording as the shared text of ASV and JPS 1917. It now reads: “Turn ye unto him from whom ye have deeply revolted, O children of Israel” (ASV; JPS 1917 “Against whom ye have deeply rebelled”).
3. **`lexical-cruxes-isaiah-31` rationale (overlay diff; Reviewer: revise).** The closing sentence claimed every rendering is attested in ASV, JPS 1917 or NJPS. It now names the two exceptions: "… except 31:8 lāmas 'forced labor' and 31:1 'lean on', which give the standard lexical sense (BDB, HALOT) of the noun and verb; no reading is added." claim_type stays `direct`.
4. **Central diff: new modify op on `mas-oved-corvee-labor-institutional-vocabulary-cross-corpus` (Reviewer: flag-for-human).** This op only appends to the rationale. It cross-refers Isa 31:8 "forced labor" (*mas* alone) to the entry's "taskwork" for the Gen 49:15 compound *mas ʿōḇēḏ*. appliesTo and wohChoice are unchanged (`appliesToAdded: []`).
   - The op is marked `requiresFounderApproval: true`, and the central version note says so.
   - **Founder decision needed:** approve the cross-reference, which keeps "forced labor" at Isa 31:8. Alternatively, rule for "taskwork" concordance: drop the op and change the 31:8 line through `lexical-cruxes-isaiah-31`.

## Founder rulings applied (sign-off 2026-11-26)

The founder (zarazinsfuss) signed off wave I-5 on 2026-11-26 through an interactive form and chose every recommended option. No English line changes as a result; only notes and glossary-diff wording were updated. The wave merges as overlay 4.0.0 and central 5.0.0.

- **31:8 "forced labor":** accepted. The central `mas-oved-corvee-labor-institutional-vocabulary-cross-corpus` cross-reference op no longer carries `requiresFounderApproval`, and its note and rationaleAppend now record the approval. The rationaleAppend is kept. The corpus-wide question about bare *mas* is still open for Kings.
- **31:4 "to fight upon"** stands (option A).
- **31:6, 31:3:** the current lines stand.
- **31:5 speculative reception paragraph:** kept as labelled (founder sign-off 2026-11-26).
