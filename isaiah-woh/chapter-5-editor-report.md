# Chapter 5 Editor Report — Isaiah 5 (the Song of the Vineyard and the six woes)

Wave I1 (Isa 1–5), chapter 5 Editor.

**Chapter advanced:** `translation.status` → `editor-review`; `translation.version` → `1.0.0-rc1`; `reviewer` left `pending`.
`overlayGlossaryVersion` and `glossaryVersion` left at the base versions (1.6.1 / 2.93.0); the orchestrator should bump them when the diffs are merged.

**Glossaries:** neither shared glossary was edited.
All changes are in `wave-i1-ch5-overlay-diff.json` and `wave-i1-ch5-central-diff.json`.

**Line changes (3), each backed by a new overlay entry:**

| refId | Draft | Now | Entry |
|---|---|---|---|
| ISA-5:7 | "justice (mishpāṭ), but behold, oppression (miśpāḥ); for righteousness (ṣᵉḏāqāh), but behold, an outcry (ṣᵉʿāqāh)" | "justice, but behold, bloodshed; for righteousness, but behold, an outcry" | `mishpach-tseaqah-wordplay-isaiah-5` |
| ISA-5:14 | "has enlarged its desire" | "has widened its throat" | `nefesh-throat-sheol-isaiah-5` |
| ISA-5:25 | "his anger has not turned back" | "his anger has not turned away" | `bekhol-zot-lo-shav-appo-refrain-isaiah` |

No other line was altered.

---

## Speculative entries requiring sign-off

None.
The four new overlay entries are `direct` (3) and `inferred` (1, `mishpach-tseaqah-wordplay-isaiah-5`, because *miśpāḥ* is a hapax with an uncertain derivation).
No lens reading is carried in any line of this chapter.

---

## Escalations

### `ISA-5:15` — the ʾāḏām / ʾîš pair (wave-wide escalation)

**Source:** וַיִּשַּׁח אָדָם וַיִּשְׁפַּל־אִישׁ (*wayyiššaḥ ʾāḏām wayyišpal-ʾîš*, as 2:9; cf. 2:11, 17)
**Current line:** "And humankind is bowed down, and man is brought low" (the wave ruling).
**Options considered:** (A) synonymous "humankind … man" (ruling; JPS 1917 "man … man"); (B) ASV social merism "the mean man … the great man"; (C) NRSV "people … everyone".
**Why escalating:** the wave brief marks this ruling ESCALATE.
The Editor applied it and recommends keeping A, because ASV's merism reads in a contrast the Hebrew does not mark.
"man" for *ʾîš* is gender-marked English, which a reviewer may want to weigh against C.
The same decision must hold at 2:9, 11, 17 (other Editors), so it needs one ruling.
No glossary entry was proposed, to avoid duplicates across the parallel Editors; `adam-adamah` is not applied.

### Orchestrator action — hôy entry

The wave ruling hôy → "Woe" is applied at ISA-5:8, 11, 18, 20, 21, 22.
No hôy entry was created here, to avoid five duplicates.
When the orchestrator creates the single wave entry, add these six refIds to its `appliesTo` and to the chapter's `glossaryRefs`.

---

## Editorial questions resolved (18 of 18)

R = Translator's default ratified; O = overruled.

1. **ISA-5:1 beloved / šîraṯ dôḏî** — R. "a song of my beloved concerning his vineyard" (ASV). NRSV "my love-song" needs the *dôḏîm* emendation. No quotation marks for the owner's speech in vv 3–6; the unmarked shift is the point of the juridical parable (commentary at 5:1 and 5:3).
2. **ISA-5:1 qeren ben-šāmen** — R. "on a very fruitful hill"; literal "a horn, a son of oil" given in commentary.
3. **ISA-5:2 bᵉʾušîm** — R. "wild grapes"; the root *bʾš* "stink" (BDB) is noted in commentary.
4. **ISA-5:5 lᵉḇāʿēr** — R, with a new entry. "it shall be eaten up" (*bʿr* II "graze"). `levaer-massevet-stump-isaiah` (6:13, "for burning") is not applied. The split is recorded in the new overlay entry `baar-graze-vineyard-isaiah-5` (direct) so that two renderings of one written form can be audited.
5. **ISA-5:7 miśpāḥ** — O. "bloodshed" (BDB; NRSV; it is also the gloss the central justice-pair rationale gives) replaces ASV "oppression". ASV's word is a guess from context; "bloodshed" has the etymological basis and matches the victims' cry in the parallel colon. New entry `mishpach-tseaqah-wordplay-isaiah-5` (inferred).
6. **ISA-5:7 wordplay presentation** — O. **Decision: the line carries plain English, and the pun is explained in commentary.** The parenthetical transliterations are removed: the corpus has almost no precedent for them (only matthew-woh 5:22 "Raca", a loanword), and they turn the line into apparatus. An English sound-echo was considered and rejected. NJPS "justice … injustice; equity … iniquity" keeps the sound but changes both second terms, and "outcry" becomes "iniquity", so accuracy-before-lens rules it out. The rule is written into the entry's `wohChoice` so later Isaianic puns can cite it.
   - **Scope sub-question:** `zaaqah-outcry-of-the-oppressed` is kept at 5:7 and extended centrally. Lexeme, referent and rendering all match, and its rationale treats *ṣᵉʿāqāh* as the same lexeme. `tzedakah-u-mishpat-justice-pair` is removed from 5:7 and 5:16: these are split pairs across parallel cola, the wave-I2 32:16 precedent removed the entry in the same case, and its `wohChoice` is the conjoined phrase. The rendering "justice / righteousness" is unchanged.
7. **ISA-5:7 kerem-vineyard** — R (not applied). This follows the 27:2 precedent: a bare-lexeme, Gen-9:20-scoped entry that is not a cross-corpus keyword. The rendering "vineyard" is identical either way. Its rationale naming Isaiah 5 is noted, but that alone does not justify a different book policy.
8. **ISA-5:9 elliptical oath** — R. "In my ears YHWH of hosts says" (ASV supplied verb); NRSV "has sworn" and 22:14 noted in commentary.
9. **ISA-5:13** — R. "have gone into exile" (perfect; prophetic-perfect reading noted); MT *mᵉṯê* "men of" kept: "its honored men are famished". LXX *nekrōn* / repointed *mēṯê* "dying of" reported, not adopted. `kevodo-kavod-suffixed-isaiah` not applied (*kāḇôḏ* = nobility). Site added to `mt-qere-textual-policy-isaiah`.
10. **ISA-5:14 nep̄eš / suffixes** — O on nep̄eš: "widened its throat" (HALOT physical sense; NJPS "gullet"; parallel "its mouth"; Hab 2:5 idiom) over ASV "enlarged its desire". New entry `nefesh-throat-sheol-isaiah-5` (direct). `nefesh-blessing-transfer` not applied. R on suffixes: "her" (with NRSV, which names the referent: "the nobility of Jerusalem and her multitude … all who exult in her"; ASV and JPS 1917 both smooth to "their … among them"), referent Jerusalem noted in commentary; She'ol "its". *(Corrected post-review; see below.)*
11. **ISA-5:15 ʾāḏām / ʾîš** — applied per the wave ruling; **ESCALATED** (above).
12. **ISA-5:16** — R. "God the Holy One is sanctified in righteousness" (ASV); attributive "the holy God" and "shows himself holy" (cf. Ezek 28:22) given in commentary. `elohim-el-eloah-monotheistic-formula-isaiah` extended (overlay).
13. **ISA-5:17 gārîm** — R. MT "sojourners" kept; LXX *arnes* "lambs" and the conjectures *kārîm* / *gᵉḏāyîm* (NRSV "kids") reported. Site added to `mt-qere-textual-policy-isaiah`.
14. **ISA-5:25 refrain / tense** — O on wording, R on tense. **Fixed refrain for 5:25 and Heb. 9:11, 16, 20; 10:4:** "For all this his anger has not turned away, and his hand is stretched out still." *šûḇ ʾap* is the idiom for anger subsiding (Gen 27:44–45; Hos 14:5), and "turn away" is its English equivalent (ASV, NRSV). The perfect becomes "has not"; *wᵉ* is "and", not ASV's "but". Verse kept in past narrative tense. New entry `bekhol-zot-lo-shav-appo-refrain-isaiah` (direct), with the four forward refIds listed in its rationale (the advisory `forwardAppliesTo` field was dropped post-review). **The ch. 9–10 Translator must use this wording verbatim.**
15. **ISA-5:26 number of the invader** — R. MT "nations" kept; MT's singular pronouns rendered as collective "them / they" (ASV, JPS 1917); emendation *lᵉḡôy mimmerḥāq* (NRSV; cf. Jer 5:15) reported, not adopted.
16. **ISA-5:29 ketiv/qere** — R. Qere translated; site added to `mt-qere-textual-policy-isaiah`.
17. **ISA-5:30 accent division** — R. ASV grouping; accent division, the *ʿărîp̄îm* hapax and *ṣar* "flint" (v 28) / "distress" given in commentary.
18. **ISA-5:8 ʾereṣ split** — R. "land" at 5:8 and 5:30 (central `eretz`, extended); "the end of the earth" at 5:26 under overlay `eretz-cosmic-scope-isaiah-24` (extended). That entry already governs 40:28 "the ends of the earth", so it covers universal-horizon idioms outside ch. 24. The orchestrator should update its `wohChoice` wording, which still says "throughout chapter 24".

`editorial_questions[]` is now empty.

---

## Commentary written (notes.official)

18 verses: 5:1, 2, 3, 5, 7, 8, 9, 10, 13, 14, 15, 16, 17, 24, 25, 26, 29, 30.
Two of these are short notes on sites the Translator did not query: 5:10 (measures) and 5:24 (*tôrāh* "teaching").
The other 12 are left empty because the line matches the standard PD reading: 5:4, 6, 11, 12, 18, 19, 20, 21, 22, 23, 27, 28.

---

## Glossary changes for review

### Per-translation overlay (`wave-i1-ch5-overlay-diff.json`; proposed 1.6.1 → 1.7.0, union-merge with the other wave-I1 diffs)

- Added: `mishpach-tseaqah-wordplay-isaiah-5` (claim_type: `inferred`) — ISA-5:7
- Added: `nefesh-throat-sheol-isaiah-5` (claim_type: `direct`) — ISA-5:14
- Added: `baar-graze-vineyard-isaiah-5` (claim_type: `direct`) — ISA-5:5
- Added: `bekhol-zot-lo-shav-appo-refrain-isaiah` (claim_type: `direct`) — ISA-5:25 (forward sites 9:11, 16, 20; 10:4 listed in the rationale)
- appliesTo extended: `yhwh-tzevaot-hosts-isaiah` (+5:7, 5:9, 5:16, 5:24); `elohim-el-eloah-monotheistic-formula-isaiah` (+5:16); `torah-teaching-isaiah` (+5:24); `eretz-cosmic-scope-isaiah-24` (+5:26); `mt-qere-textual-policy-isaiah` (+5:13, 5:17, 5:29)
- Notes: hôy entry deferred to the orchestrator; non-applications recorded.

### Central glossary (`wave-i1-ch5-central-diff.json`; CENTRAL — apply by orchestrator; proposed 2.93.0 → 2.94.0, one bump for the whole wave)

- appliesTo extended: `zaaqah-outcry-of-the-oppressed` (+ISA-5:7); `eretz` (+ISA-5:8, 5:30); `sheol-underworld-realm-of-the-dead` (+ISA-5:14); `avon-iniquity-cross-corpus-keyword` (+ISA-5:18)
- Deliberately not extended: `tzedakah-u-mishpat-justice-pair` (5:7, 5:16; split pair), `kerem-vineyard` (5:1–10), `nefesh-blessing-transfer` (5:14), `adam-adamah` (5:15)
- No new central entries; no existing wohChoice, rationale or claim_type modified.

---

## Post-review corrections

The Reviewer returned the chapter at `awaiting-human`.
These are non-decision corrections only.
`translation.status`, the `reviewerReport` block, the 5:15 line and the shared glossaries are untouched.

1. **ISA-5:14 commentary (Reviewer: revise, commentary only).** The note wrongly said the line keeps "her" with JPS 1917. JPS 1917 reads "their glory … among them", as ASV does. The note now cites NRSV, which names the referent ("the nobility of Jerusalem and her multitude … all who exult in her"), and says ASV and JPS 1917 both smooth to "their". Item 10 above is corrected to match. The line is unchanged.
2. **ISA-5:13 line (optional style, Reviewer-approved).** "its honored men … its multitude" → "their honored men … their multitude". The 3ms suffixes refer to the collective *ʿammî* "my people", so "their" matches the verse's own "my people have" (ASV, JPS 1917). This changes pronoun agreement only: no lexical decision changes, so there is no glossary entry. The 5:13 commentary now records the choice.
3. **`wave-i1-ch5-overlay-diff.json`.**
   - The advisory `forwardAppliesTo` field is dropped from `bekhol-zot-lo-shav-appo-refrain-isaiah`; the forward list (ISA-9:11, 9:16, 9:20, 10:4) stays in the rationale.
   - The `eretz-cosmic-scope-isaiah-24` modify op now also rewords `wohChoice`. It no longer says "throughout chapter 24"; it names ch. 24, 13:9–13, chs. 40–65 and the "end(s) of the earth" idiom (5:26; 40:28). The rendering and the existing sites are unchanged.
   - Version note: this strictly modifies a field of an existing entry. The Editor recommends a minor bump because no rendering changes; the orchestrator decides.

