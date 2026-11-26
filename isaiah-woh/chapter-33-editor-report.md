# Chapter 33 Editor Report

Isaiah 33 (24 verses), wave I-5 (Isa 28, 30, 31, 33–35).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v4.0.0 and isaiah-woh overlay v3.0.0, both read-only.
`wave-i5-rulings.md` is binding, including ruling 7 (lʿg "stammering").
All glossary changes are in `wave-i5-ch33-overlay-diff.json` and `wave-i5-ch33-central-diff.json`.

## Summary

- **Editorial questions:** all 17 resolved. `editorial_questions[]` is empty.
- **Commentary:** 22 of 24 verses have `notes.official`. 33:10 and 33:13 have none, because they have no crux.
- **English-line changes:** five verses, each backed by a glossary entry.
  - 33:7: "the ambassadors of peace" becomes "the messengers of peace" (`lexical-cruxes-isaiah-33`; malʾāḵ "messenger" as at 14:32, 18:2, 42:19, 44:26).
  - 33:8: "he regards no one" becomes "he regards no mortal" (`enosh-mortal-isaiah`; ʾĕnôš "mortal" as at stable 13:12, 24:6).
  - 33:19: "of a strange tongue" becomes "of a stammering tongue" (ruling 7; `lag-stammering-isaiah`).
  - 33:21: "will be with us in majesty … no gallant ship" becomes "will be mighty for us … no mighty ship" (`addir-mighty-isaiah`).
  - 33:23: "Your tackle hangs loose" becomes "Your cords hang loose", and "the lame took the prey" becomes "the lame took the plunder" (`lexical-cruxes-isaiah-33`).
- **Status:** `editor-review`, `1.0.0-rc1`. "claude-opus-5-5 (editor)" has been added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 4.0.0 and 3.0.0 for the orchestrator to set on merge. `i18n.he` is unchanged. No paragraph `translit` was added.
- **Lens audit:** no English line carries a project reading. The canon texts in data-library (*The Book Which Tells the Truth*, *Extraterrestrials Took Me to Their Planet*, *Let's Welcome the Extraterrestrials*) cite no verse of Isaiah 33; their Isaiah citations are to chapters 6, 13, 14, 15, 29, 32, 40, 43, 45, 48, 54 and 65. There is one labelled speculative reception paragraph, at 33:14 (see below).
- **References checked on 2026-11-26.**
  - NJPS ("Tanakh: The Holy Scriptures, published by JPS", 1985) and JPS 1917 on Sefaria, `/api/v3/texts/Isaiah.33?version=english|all`. The Gender-Sensitive Edition was not used.
  - ASV 1901 on bible-api.com.
  - 1 Cor 1:20 Greek from the corpus `1-corinthians` file. Exod 24:17 from `exodus-woh`; TBWTT ch. 3 from data-library.
  - 1QIsaᵃ at 33:8 is known only from the NJPS note. The lexicons (BDB, HALOT), NRSV, LXX and other emendations are cited from memory and marked "recalled" or "not verified".

## Speculative entries requiring sign-off

No glossary entry is speculative. The four new overlay entries are `direct`, and the central ops only extend appliesTo.

### Speculative commentary paragraph at `ISA-33:14`

**Source:** *ʾēš ʾôḵēlāh* "devouring fire".
**Content:** a paragraph labelled "Wheel of Heaven reading (speculative; reception note, not a translation claim)". It says plainly that the canon does not cite Isa 33. It reports that TBWTT ch. 3 quotes Exod 24:17 ("like devouring fire") and reads the glory there as the vehicle of the Elohim. It notes that the same phrase occurs at 33:14, and it says the connection is the Editor's, not the canon's.
**Why speculative:** the link from Exod 24:17 to Isa 33:14 is the Editor's synthesis. No canon text makes it.
**Recommendation:** ship under the founder policy that keeps such notes, or drop the paragraph if the founder prefers reception notes only where the canon cites the verse. The rest of the 33:14 note is unaffected either way.

---

## Unresolved editorial questions

None are blocked. These decisions are flagged for the Reviewer and the founder.

### `ISA-33:17`: yōp̄î "beauty" shared with ṣᵉḇî

**Issue:** ruling 1 lists "beauty" = ṣᵉḇî (`tsevi-beauty-isaiah`). 33:17 has a different noun, yōp̄î.
**Decision:** keep "the king in his beauty" and record the shared English in a new entry, `yofi-beauty-isaiah`, with a rationale sentence added to `tsevi-beauty-isaiah`. Reasons: yōp̄î is the plain Hebrew word for beauty, and ASV, JPS 1917 and NJPS all have "beauty". The stable 3:24 already prints yōp̄î "beauty". The two nouns never share an Isaiah verse.
**Options considered:** a shared word with a recorded note (taken); "loveliness" or "fairness" for yōp̄î. That option would also require revising stable 3:24.
**Why flagged:** the decision qualifies the ṣᵉḇî reservation in ruling 1. The entry stages "loveliness" or "fairness" as the fallback if a later verse puts both nouns together.

### `ISA-33:21`: ʾaddîr "mighty"

**Decision:** "YHWH will be mighty for us … no mighty ship". One English word for both occurrences, matching stable 10:34 "a mighty one" and NJPS "mighty craft". "Majesty" is reserved for gāʾôn.
**Options considered:** "majesty … gallant" (ASV, which collides with gāʾôn and splits the word); "the Mighty One, YHWH"; "great" (which would collide with gāḏôl).
**Why flagged:** "mighty" also renders gibbôr ("Mighty God" at 9:5 and 10:21, "mighty men"). The two words never meet in one verse, and the overlap is recorded in the entry. "for us" replaces ASV's "with us" (*lānû*).

### `ISA-33:19`: provisional entry id

**Decision:** "a stammering tongue" (ruling 7). No `wave-i5-ch28-overlay-diff.json` existed when this Editor wrote its diff, so the modify op uses the provisional id `lag-stammering-isaiah`. **Orchestrator:** apply the chapter-28 add first, then rename this op and the 33:19 glossaryRef if the chapter-28 id differs. (Superseded at review: the Reviewer confirmed that `wave-i5-ch28-overlay-diff.json` uses the same id, so no rename is needed; see the final section.)

### `ISA-33:2` and `ISA-33:6`: MT over ASV (confirmed)

**Verification:** ASV has "be thou our arm" (33:2) and "the fear of Jehovah is thy treasure" (33:6). MT has *zᵉrōʿām* "their arm" and *ʾôṣārô* "his treasure". JPS 1917 has "their arm" and "His treasure". NJPS has "their arm" (with the note "Emendation yields 'You have been our help'") and "her treasure" (with the note "Heb. 'his'"). All were checked 2026-11-26.
**Decision:** the line translates MT. The departure is recorded in the `mt-qere-textual-policy-isaiah` rationaleAppend, with an instruction to add both sites to the entry's MT-over-ASV list.

### `ISA-33:8`: correction to the Translator's note

The draft question said a 1QIsaᵃ reading "witnesses" was reported in an NJPS note. The NJPS note actually reads "1QIsa reads 'A pact.'" The commentary gives the NJPS wording. "Witnesses" (*ʿēḏîm*) is given as a modern emendation, recalled and not verified.

### `ISA-33:23`: "cords" for ship's rigging

**Decision:** "Your cords hang loose", the same English as the tent's cords at 33:20, so that the contrast in the passage stays visible. The other versions have "tacklings" (ASV, JPS 1917) and "ropes" (NJPS). If the Reviewer finds "cords" too odd for a ship, the fallback is "ropes" in both 33:20 and 33:23. That would change stable vocabulary nowhere, since both verses are in this chapter.

---

## Decisions on the Translator's questions

1. **33:1 bgd/šdd, kannᵉlōṯᵉḵā, bô.** The ASV structure is kept in the bgd family, and `bgd-shdd-treachery-destroyer-isaiah` is extended to 33:1. "made an end" (klh) is used, with JPS 1917 "weary" (lʾh) in commentary. "with whom" handles the third-person suffix. → bgd-shdd, hoy, mt-qere, crux entry.
2. **33:2 zᵉrōʿām.** MT "their arm" (see above).
3. **33:4 ḥāsîl / šqq / tense.** ASV is kept, with an indefinite "they" and the future tense. NJPS's "amassed" and the uncertainty notes are in commentary. → crux entry.
4. **33:6 ʾĕmûnāh / ʾôṣārô.** "stability" (ASV) and MT "his treasure". The antecedent question is in commentary. → crux entry, mt-qere.
5. **33:7 ʾerʾellām.** MT/ASV "their valiant ones". NJPS "the Arielites" and the repointing are in commentary. `ariel-ob-isaiah-29` is deliberately not applied. → crux entry, mt-qere.
6. **33:7 malʾăḵê šālôm.** Changed to "the messengers of peace" for book concordance. → crux entry.
7. **33:8 ʿārîm / ʾĕnôš / subject.** MT "cities". ʾĕnôš is "no mortal" (a line change). "He" is unspecified. `adam-humankind-ish-man-isaiah` is deliberately not extended to ʾĕnôš; the new `enosh-mortal-isaiah` governs it.
8. **33:9 ʿărāḇāh / nōʿēr / heḥpîr.** "like a desert" (the common noun, as at 35:1, 6 and 40:3), "shake off their leaves" (ASV), "is ashamed". The Arabah reading and NJPS "stripped bare" are in commentary. → crux entry.
9. **33:11 rûḥăḵem.** MT "your breath". The NJPS emendation is in commentary.
10. **33:14 gûr / môqᵉḏê ʿôlām.** "dwell" (all three versions; 11:6 precedent) and "everlasting burnings". The gûr/šāḵan distinction and the "burnings" overlap with v. 12 are recorded. Central `megurim-…` (the Genesis sojourner self-designation) is deliberately not extended. → crux entry.
11. **33:17 yōp̄î / meleḵ.** "the king in his beauty". `yofi-beauty-isaiah` is new. `ha-melekh-divine-title-isaiah` is deliberately not applied (no article, no divine name). The identity of the king is left open in commentary.
12. **33:18 sōp̄ēr / [the tribute] / hgh.** "the one who counted … the one who weighed", with no supplied object. The scribe-title sense and NJPS "throat" are in commentary. → crux entry.
13. **33:19 nôʿāz / nilʿaḡ.** "the fierce people" (ASV) and "a stammering tongue" (ruling 7). NJPS "barbarian" is in commentary. → crux entry, lag-stammering.
14. **33:20 môʿăḏēnû / šaʾănān.** "the city of our appointed feasts" (1:14) and "a quiet habitation" (32:18 "quiet" for šaʾănān). → crux entry, yated.
15. **33:21 ʾaddîr / rᵉḥăḇê yāḏāyim.** "mighty … mighty" (see above). ASV's "broad rivers and streams" is kept. → addir entry, central yeor.
16. **33:22 mᵉḥōqēq.** ASV "lawgiver". NJPS "prince" and the staff/commander sense are in commentary. → crux entry.
17. **33:23 ḥeḇel / ʿaḏ-šālāl / baz.** "cords" and "the lame took the plunder" are line changes. "the prey of a great spoil" (ASV) is kept. The NJPS emendation and verse reordering are in commentary. → crux entry, nes (sail exception), mt-qere.

Deliberate non-applications: `ariel-ob-isaiah-29` (33:7), `ha-melekh-divine-title-isaiah` (33:17), `adam-humankind-ish-man-isaiah` (33:8), central `megurim-…` (33:14), central `brit-olam` (33:14 ʿôlām without bᵉrîṯ; 33:8 bᵉrîṯ without ʿôlām), and central `shakhan-…` for the noun šāḵēn at 33:24.

---

## Glossary changes for review

### Central glossary (proposed 4.0.0 → 4.1.0; `wave-i5-ch33-central-diff.json`)

- Modified: `sa-na-pesha-nasa-avon-forgiveness-formula-cross-corpus`, appliesTo += ISA-33:24 (the first Isaiah site).
- Modified: `avon-iniquity-cross-corpus-keyword`, appliesTo += ISA-33:24.
- Modified: `shakhan-dwell-divine-presence-verb-cross-corpus`, appliesTo += ISA-33:5, ISA-33:16.
- Modified: `tzedakah-u-mishpat-justice-pair`, appliesTo += ISA-33:5.
- Modified: `eretz`, appliesTo += ISA-33:9, ISA-33:17.
- Modified: `yeor-nile-egyptian-loanword`, appliesTo += ISA-33:21.

### Per-translation overlay (proposed 3.0.0 → 3.1.0; `wave-i5-ch33-overlay-diff.json`)

- Added: `lexical-cruxes-isaiah-33` (claim_type: `direct`)
- Added: `addir-mighty-isaiah` (claim_type: `direct`; appliesTo includes stable ISA-10:34, line unchanged)
- Added: `yofi-beauty-isaiah` (claim_type: `direct`; appliesTo includes stable ISA-3:24, line unchanged)
- Added: `enosh-mortal-isaiah` (claim_type: `direct`; appliesTo includes stable ISA-13:12 and ISA-24:6, lines unchanged)
- Modified (appliesTo, plus a rationale sentence):
  - `bgd-shdd-treachery-destroyer-isaiah` (33:1)
  - `hoy-woe-isaiah` (33:1)
  - `title-and-meta-conventions-isaiah` (33:1)
  - `mt-qere-textual-policy-isaiah` (33:1, 2, 6, 7, 8, 11, 12, 17, 23; the orchestrator updates the wohChoice lists on merge)
  - `nes-signal-isaiah` (33:23, sail exception)
  - `yated-peg-stake-isaiah` (33:20, tent clause)
  - `lag-stammering-isaiah` (33:19; id confirmed against the chapter-28 add, which is applied first)
- Modified (rationale sentence only): `tsevi-beauty-isaiah`, which records the shared "beauty" with yōp̄î.
- Orchestrator: the stable chapters 3, 10, 13 and 24 need the new ids added to the glossaryRefs of ISA-3:24, ISA-10:34, ISA-13:12 and ISA-24:6 when the diff is merged. Their English lines are unchanged.

Strong's numbers in the new entries come from memory and are marked as not checked against a concordance.

---

## Post-review corrections

The Reviewer's verdicts (`translation.reviewerReport`, 2026-11-26T19:09:14Z) were applied as listed below. Only commentary, this report and the Editor's own overlay diff were changed. No English line, `translation.status` (still `awaiting-human`), the `reviewerReport` block or any shared glossary was touched. The central diff is unchanged.

1. **`lexical-cruxes-isaiah-33` (revise).**
   - The malʾāḵ sentence now reads "at every Isaiah site translated so far (14:32; 18:2 …; 30:4 draft; 42:19; 44:26); 37:36 and 63:9 are not bound by this choice."
   - The claim sentence now reads "Every rendering is a standard lexical gloss (BDB; HALOT; recalled); most are the wording of at least one of ASV, JPS 1917 and NJPS, and the three concordance changes are argued above." The old wording was not true of "the base of their mast", "cords" or "plunder" at 33:23.
   - The strongs field for *nôʿāz* now gives H5810 ʿāzaz "be strong, be insolent", the root named in the 33:19 note. It adds that some concordances list the form under H3267 yāʿaz.
2. **`addir-mighty-isaiah` (revise).** The rationale now adds: "'Mighty One' also renders ʾăḇîr in the title ʾăḇîr yiśrāʾēl / yaʿăqōḇ (1:24 stable; 49:26; 60:16); the roots do not share a verse."
3. **`enosh-mortal-isaiah` (advisory, applied).** The wohChoice now lists 51:7, 51:12 and 56:2 as expected later sites. They are not added to appliesTo.
4. **33:14 speculative paragraph (optional, applied).** The paraphrase "reads that glory as the vehicle of the Elohim" is replaced by a direct quotation of TBWTT 3:33: "There you have the description of the «glory» — in reality the flying craft — of the creators". The rest of the paragraph is unchanged, including the statement that the canon does not cite Isa 33 and that the connection is the Editor's.
5. **Provisional id resolved.** The Reviewer confirmed that `lag-stammering-isaiah` matches the add in `wave-i5-ch28-overlay-diff.json`. The version-op note and the modify op's rationaleAppend now say so; the 33:19 glossaryRef is unchanged.

Still for the human: whether to keep the 33:14 speculative paragraph; the shared "beauty" (yōp̄î / ṣᵉḇî); the "mighty" overlaps (gibbôr, ʾăḇîr); and "cords" for the ship's rigging at 33:23, which the Reviewer accepted.
