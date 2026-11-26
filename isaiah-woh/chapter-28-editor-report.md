# Chapter 28 Editor Report

Isaiah 28 (29 verses), wave I-5 (Isa 28, 30, 31, 33–35).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v4.0.0 and isaiah-woh overlay v3.0.0, both read-only.
`wave-i5-rulings.md` (rules 1–7) is in force.
All glossary changes are in `wave-i5-ch28-overlay-diff.json` and `wave-i5-ch28-central-diff.json`.

## Summary

- **Editorial questions:** all 21 resolved; `editorial_questions[]` is empty. Nothing in them needs founder judgement; two smaller items are flagged for confirmation below.
- **English-line changes (4 verses), each backed by a glossary entry:**
  - 28:2 "cast down to the earth" → "cast down to the ground" (`lexical-cruxes-isaiah-28`; the book's falling idiom at 14:12, 21:9, 25:12, 26:5).
  - 28:15 "We have made a covenant with death" → "We have cut a covenant with death" (central `karat-brit-cut-covenant`, which governs *kāraṯ bᵉrîṯ* corpus-wide and names this verse).
  - 28:25 "fitches" → "black cumin"; "in its appointed place" → "in the appointed place" (`lexical-cruxes-isaiah-28`; BDB *qeṣaḥ* = *Nigella sativa*; *nisman* has no suffix).
  - 28:27 "fitches" (×2) → "black cumin" (same entry).
  - Every other line is the Translator's.
- **Commentary:** all 29 verses have `notes.official`. 28:16 ends with one paragraph labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`; "claude-opus-5-5 (editor)" added to `modelDrafts`. `glossaryVersion` (4.0.0) and `overlayGlossaryVersion` (3.0.0) are left for the orchestrator to set on merge. No paragraph `translit` was added.
- **Forward commitments (rule 2) kept:** 28:10, 13 "line upon line" (no revisit of 18:2, 7 needed); 28:22 "a full end, and that determined"; 28:16 NT reception in commentary only.
- **Rule 7:** overlay `lag-stammering-isaiah` added and cited at 28:11; the chapter 33 Editor appends ISA-33:19.
- **Verification (2026-11-26):**
  - NJPS ("Tanakh: The Holy Scriptures, published by JPS", 1985, not the Gender-Sensitive Edition), JPS 1917 and Koren for all of Isa 28 were checked on Sefaria API v3, with the footnotes.
  - ASV and KJV for Isa 28 and the LXX for Isa 28 were checked on getbible.net. The ASV NT for Rom 9:33, 10:11, 1 Cor 14:21, Eph 2:20 and 1 Pet 2:6–8 was checked on the same site.
  - These BDB articles were checked through Sefaria's lexicon: *laʿaḡ*, *lāʿaḡ* (Niphal at 33:19), *lāʿēḡ*, *ṣaw*, *qaw*, *ḥārûṣ*, *ḥūš*, *yāsaḏ* (Cheyne's participle at 28:16), *bōḥan*, *ḥōzeh*, *ḥāzûṯ*, *rāḡaz*, *qeṣaḥ*, *śôrāh* and *sāman*.
  - Not verified, and marked so in the commentary: NRSV, 1QIsaᵃ (28:16), HALOT, the alphabet-recitation view of 28:10, the emendation of *kuppar* (28:18) and the Mesopotamian *Farmer's Instructions* parallel (28:26). Strong's numbers are from recall.
- **Canon check:** `the-book-which-tells-the-truth`, `extraterrestrials-took-me-to-their-planet` and `lets-welcome-the-extraterrestrials` were searched. **None cites Isa 28.** TBWTT cites Isaiah 6, 13, 14, 15, 26, 27, 29 (ch. 3) and 29, 32, 40, 42–44, 54, 65 (ch. 5).
- **Lens audit:** no English line carries a project reading. The stone of 28:16 is not identified, and "death" stays lower-case.

## Speculative entries requiring sign-off

No speculative glossary entry is proposed. One commentary paragraph is labelled speculative.

### ISA-28:16 reception paragraph (commentary, not a glossary entry)

**Source:** הִנְנִי יִסַּד בְּצִיּוֹן אָבֶן
**WoH reading (commentary only):** The canon calls Solomon's Temple on Zion "the first residence for the reception of the Elohim" (TBWTT 3:102–103) and asks for a new residence, an embassy (TBWTT 6:21–22). The paragraph says a reader may set the foundation stone YHWH lays in Zion beside that theme. It states that the canon does not cite Isa 28, that the link is the project's synthesis, and that in context the stone is the opposite of the scoffers' "refuge of lies."
**Why speculative:** it connects a verse the canon does not cite with a canon theme. No single source makes that connection.
**Recommendation:** ship, following the 18:1 precedent. If the founder prefers silence at verses the canon does not cite, delete the final paragraph of the 28:16 note. Nothing else depends on it.

---

## Unresolved editorial questions

None require escalation. Two decisions are flagged for founder confirmation; they do not block the chapter.

### `ISA-28:4`, `ISA-28:24–28`: pronouns resuming a generic participle

**Issue:** wave I-4 rule 13 makes generic human nouns gender-neutral. It does not say what to do with the pronouns that resume them. The line renders the nouns neutrally ("the one who looks upon it", "the one who plows") and keeps the Hebrew 3ms pronouns ("his hand … he swallows it"; "his ground", "his cart"), as ASV and NJPS do.
**Options considered:** A. keep "he/his" (adopted, recorded in `lexical-cruxes-isaiah-28`); B. singular "they"; C. recast to avoid pronouns.
**Why flagged:** it settles a scope question in a founder rule. Confirm A, or rule B or C for the book.

### `ISA-28:10, 13`: "precept upon precept … line upon line"

**Issue:** the binding ruling is kept. ASV, KJV, Koren and JPS 1917 support it, and BDB lists it as one of three views. Many modern scholars, and NJPS ("mutter upon mutter, murmur upon murmur"), read the syllables as meaningless sound-play. The 28:10 commentary states this plainly, gives the transliteration, and keeps the claim `inferred`.
**Why flagged:** for awareness only. There is no departure, so 18:2, 7 are not reopened.

---

## Decisions on the Translator's questions

1. **28:1 *hôy* vocative.** "Woe, the crown of pride …" → `hoy-woe-isaiah` + ISA-28:1. The singular "crown" is kept, and the 28:3 plural verb is noted.
2. **28:1, 4 *ṣᵉḇî tip̄ʾartô*.** "the beauty of its honor" (literal construct, book defaults; it keeps the word-link with 28:5) → `tsevi-beauty-isaiah`, `tiferet-honor-isaiah` + 28:1, 4, 5. No departure.
3. **28:1, 4 *gêʾ-šᵉmānîm*.** "the rich valley" (Koren) is kept; ASV "fat valley" and NJPS "men bloated" are in commentary → `lexical-cruxes-isaiah-28`.
4. **28:2 *hinnîaḥ lāʾāreṣ bᵉyāḏ*.** **Line change** to "to the ground" (book idiom; NJPS). "with the hand" (ASV) is kept. The central `eretz` ref is removed from 28:2 → `lexical-cruxes-isaiah-28`, `adonai-standalone-title-isaiah`.
5. **28:4 pronouns / *qayiṣ*.** "his" kept (flagged above); "summer" (ASV) → `lexical-cruxes-isaiah-28`.
6. **28:7.** ASV is kept: "swallowed up by wine" (*blʿ*, echoing 28:4), "err in vision, stumble in judgment". JPS 1917 "reel in vision" and NJPS are in commentary.
7. **28:8.** "so that there is no place clean" (ASV).
8. **28:9 speaker.** No quotation marks (ASV); the NJPS attribution is in commentary.
9. **28:10 *ṣaw lāṣāw*.** "precept upon precept … line upon line" (rule 2). `qav-qav-line-isaiah` is extended to 28:10, 13, 17, and one sentence is appended to its wohChoice recording the settlement and *ṣaw* = "precept". No new entry is created for *ṣaw*, since the qav entry's source already covers the phrase. No escalation is needed.
10. **28:11 *laʿăḡê śāp̄āh*.** "For with stammering lips and with another tongue" → **new overlay `lag-stammering-isaiah` (direct)**. 1 Cor 14:21 is noted as reception.
11. **28:14 *mōšᵉlê*.** "who rule" (ASV); *mšl* II (JPS 1917 "ballad-mongers", NJPS note) is in commentary.
12. **28:15 ketiv/qere.** qere *šôṭ*, *yaʿăḇōr* → `mt-qere-textual-policy-isaiah` + ISA-28:15.
13. **28:15, 18 death / She'ol / *ḥōzeh*.** Lower-case "death" (as 25:8); "She'ol" (central `sheol-…`); "agreement". The Mot comparison is in commentary only (central `mot-mavet-…` + 28:15, 18). **Line change** to "cut a covenant" under central `karat-brit-cut-covenant` (see Summary).
14. **28:16 the cornerstone.** The ASV line is kept with "tested stone". MT *yissaḏ*, BDB's participle note, *yāḥîš* and the LXX and NT reception are all in commentary → **new overlay `even-bochan-tested-cornerstone-isaiah-28` (direct)**. The quotation runs from 16 to 19 (NJPS).
15. **28:18 *kuppar*.** "annulled". `kupar-atonement-isaiah` is deliberately not applied; this is recorded in `lexical-cruxes-isaiah-28`.
16. **28:21.** "Mount Perazim", "the valley of Gibeon", "rage", and the appositive syntax with distinct word pairs are kept. 2 Sam 5:20, 25, 1 Chr 14:16 and Josh 10 are cited.
17. **28:22.** "a full end, and that determined" → central `kalah-venecheratzah-…` + ISA-28:22. "upon the whole earth" (ASV), consistent in scope with 10:23 → `eretz-cosmic-scope-isaiah-24` + ISA-28:22. JPS 1917 and NJPS read "land", reported in commentary.
18. **28:25 parable crops.** **Line change** to "black cumin" and "the appointed place". "spelt" (NJPS "emmer"), "in rows" (BDB dittography view) and "in its border" are kept. *ḥārûṣ* at 28:27 is "threshing sledge", a homonym, and is not added to the kalah entry.
19. **28:26.** ASV construal is kept; the JPS 1917 and NJPS division is in commentary → `elohai-elohenu-doxology-isaiah-25` + ISA-28:26.
20. **28:28.** ASV construal; *dqq* "crush" twice. The NJPS *lû* reading and the Koren/JPS 1917 question form are in commentary.
21. **28:29.** ASV relative clause; "sound wisdom". The 9:5 / 25:1 echo is noted, and the hymn entry is not applied.

### Corrections to the Translator's attributions

- 28:11: the draft gave "stammering lips" as KJV only. JPS 1917 and Koren print it too.
- 28:10: JPS 1917 is "precept by precept … line by line", as the draft said. Koren has "precept upon precept" (ASV wording).

## Glossary changes for review

### Central glossary (`wave-i5-ch28-central-diff.json`, proposed 4.0.0 → 4.1.0)

- Modified (appliesTo + rationaleAppend only): `kalah-venecheratzah-decreed-full-end-cross-corpus` (+28:22)
- Modified (appliesTo + rationaleAppend only): `karat-brit-cut-covenant` (+28:15)
- Modified (appliesTo + rationaleAppend only): `sheol-underworld-realm-of-the-dead` (+28:15, 18)
- Modified (appliesTo + rationaleAppend only): `mot-mavet-death-personified-cross-corpus-ugaritic-hebrew-bible` (+28:15, 18; apparatus only)
- Modified (appliesTo + rationaleAppend only): `adam-adamah` (+28:24)
- Deliberate non-extensions: `eretz` (28:2 idiom; 28:22 governed by the overlay); kalah at 28:27 (homonym).

### Per-translation overlay (`wave-i5-ch28-overlay-diff.json`, proposed 3.0.0 → 3.1.0)

- Added: `lag-stammering-isaiah` (claim_type: `direct`): 28:11; the chapter 33 Editor appends 33:19.
- Added: `even-bochan-tested-cornerstone-isaiah-28` (claim_type: `direct`): 28:16.
- Added: `lexical-cruxes-isaiah-28` (claim_type: `direct`): 17 sites.
- Modified: `qav-qav-line-isaiah` (+28:10, 13, 17). One sentence is appended to wohChoice (`changes.wohChoice` = old text + the sentence; `wohChoiceAppend` repeats it). The claim_type stays `inferred`. If an append counts as a modification, bump the overlay to 4.0.0.
- Modified (appliesTo only, some with rationaleAppend):
  - `hoy-woe-isaiah`, `title-and-meta-conventions-isaiah`: 28:1
  - `geut-majesty-isaiah`: 28:1, 3
  - `tsevi-beauty-isaiah`, `tiferet-honor-isaiah`: 28:1, 4, 5
  - `adonai-standalone-title-isaiah`: 28:2
  - `yhwh-tzevaot-hosts-isaiah`: 28:5, 22, 29
  - `ruach-divine-spirit-lower-case-isaiah`: 28:6
  - `mt-qere-textual-policy-isaiah`: 28:15
  - `adonai-yhwh-compound-isaiah-25`: 28:16, 22
  - `eretz-cosmic-scope-isaiah-24`: 28:22
  - `elohai-elohenu-doxology-isaiah-25`: 28:26

Every `glossaryRefs` entry in chapter 28 is governed after merge, either by existing appliesTo or by these ops. This was checked by script.

### Merge notes for the orchestrator

- The chapter 33 Editor extends `lag-stammering-isaiah`, which exists only in this diff. Apply this add before their modify.
- Concurrent extensions of `hoy-woe-isaiah`, `yhwh-tzevaot-hosts-isaiah`, `mt-qere-textual-policy-isaiah` and the other book-level entries should be merged as a union.
- The chapter title still reads "Woe to the crown of pride …" (descriptive title), while the line has "Woe, the crown …". The title was left as drafted.

## Post-review corrections

These were applied on 2026-11-26 after the Reviewer's verdicts (`translation.reviewerReport`), on coordinator instruction.
`translation.status` (awaiting-human), the `reviewerReport` block and the shared glossaries are unchanged.

1. **28:26 line (Reviewer revise, accent-based).** The line is now "For he instructs him aright; his God teaches him." It was "For his God instructs him aright; he teaches him." The MT accents divide the verse after *lammišpāṭ* (*ṭip̄ḥā*) and join *ʾĕlōhāyw* to *yôrennû* (*mērᵊḵā*). JPS 1917, NJPS and Koren follow that division. The sense is unchanged. The 28:26 note is rewritten. It also corrects my earlier statement in that note, which presented JPS 1917 and NJPS as a different construal, when in fact they follow the accents. The 28:26 item of `lexical-cruxes-isaiah-28` (wohChoice and rationale) is updated in the overlay diff. This brings the total English-line changes to five verses.
2. **הִנְנִי = *hinᵉnî*.** The long form is now transliterated as *hinᵉnî* in `even-bochan-tested-cornerstone-isaiah-28` (translit, partOfSpeech, wohChoice and rationale, with a correction note) and in the 28:16 note. *hinnîaḥ* at 28:2 is a different word and is unchanged.
3. **`eretz-cosmic-scope-isaiah-24` op (+28:22).** The rationaleAppend now states that the worldwide reading at 28:22, as at 10:23, is a consistency choice made to agree with ASV and the "full end" wording, and is not the consensus reading. JPS 1917 and Koren have "the whole land", and NJPS has "all the land". At these sites the scope has inferred strength, and the territorial reading is in the commentary. The line is unchanged.
4. **28:16 speculative paragraph.** It now says that the canon has Solomon build the residence "on Earth" (TBWTT 3:103) under the heading "The first residence for the reception of the Elohim" (3:102). The identification of that residence with the Temple on Zion is marked as the Editor's (standard) identification, not the canon's wording.
5. **Chapter title.** It now matches the 28:1 line: "Isaiah 28 — Woe, the crown of pride of Ephraim: line upon line, the covenant with death, and the tested cornerstone".
6. **Pronouns at 28:4 and 28:24–28.** The lines keep option A ("he/his"). The singular-"they" alternative (option B) is staged in the wohChoice of `lexical-cruxes-isaiah-28` and marked **PENDING FOUNDER RULING**:
   - 28:4: "… while it is still in their hand, they swallow it."
   - 28:24: "Do they open and harrow their ground?"
   - 28:25: "When they have leveled its surface, do they not …"
   - 28:26: "For he instructs them aright; their God teaches them."
   - 28:27: no change.
   - 28:28: "for they will not go on threshing it forever; and though the wheel of their cart and their horses scatter it, they do not crush it."

   If the founder rules for B, apply those lines and drop the staging text.

Both JSON files still validate, and every glossaryRef is still governed.

## Founder rulings applied (sign-off 2026-11-26)

The founder (zarazinsfuss) signed off wave I-5 on 2026-11-26 through an interactive form and chose every recommended option. No English line changes as a result; only notes and glossary-diff wording were updated. The wave merges as overlay 4.0.0 and central 5.0.0.

- **ISA-28:4, 28:24–28 pronouns:** option A stands, with "he/his". The ruling is *neutral noun, Hebrew pronoun*: the generic participle takes a neutral noun phrase, and the resuming 3ms pronouns follow the Hebrew. The staged singular-"they" lines (option B) are **rejected**. The PENDING block has been removed from `lexical-cruxes-isaiah-28`, and the entry's wohChoice and rationale now record the ruling.
- **ISA-28:10, 13** "precept upon precept … line upon line" stands (binding commitment; 18:2, 7 unchanged).
- **ISA-28:16 speculative reception paragraph:** kept as labelled (founder sign-off 2026-11-26).
