# Chapter 3 Editor Report

Chapter: Isaiah 3 (26 verses), wave I-1 (Isa 1–5).
Editor: claude-opus-5-5 (editor), 2026-11-26.
Base: central glossary v2.93.0 and isaiah-woh overlay v1.6.1, both read-only in this wave. All glossary changes are in diff files.

## Summary

- **Editorial questions:** all 44 resolved, and `editorial_questions[]` is empty. 43 are folded into glossary entries and commentary. One (hā-ʾāḏôn, 3:1) is escalated, as the wave brief directs.
- **English-line changes:** 4. Each is backed by a new overlay entry.
  - 3:3: "the honored man" → "the man of rank" (`lexical-cruxes-isaiah-3`).
  - 3:18: "the cauls" → "the headbands" (`daughters-of-zion-finery-isaiah-3`).
  - 3:19: "the mufflers" → "the scarves" (same entry).
  - 3:24: "instead of a sash" → "instead of a girdle" (same entry).
- **Commentary:** 22 of 26 verses have `notes.official`. Verses 3:2, 3:5, 3:6 and 3:11 have none, because their renderings are standard. The 3:6 pun on *makšēlāh* is discussed under 3:8, and the *ʾôy* of 3:11 under 3:9.
- **glossaryRefs:** updated for every verse. The Genesis-scoped central `navi-first-occurrence-abraham` has been removed from 3:2. It was attached by the Translator, but no signed-off Isaiah chapter uses it.
- **Status:** `editor-review`, `1.0.0-rc1`, with "claude-opus-5-5 (editor)" added to `modelDrafts`. `glossaryVersion` (2.93.0) and `overlayGlossaryVersion` (1.6.1) are left at the base so the orchestrator can set them once, after merging the five parallel chapter diffs.
- **Lens audit:** no English line carries a project reading. The astral and magical identifications in the finery list (sun-discs, lunar amulets, amulet cases) appear only in commentary, labelled as interpretation.

---

## Speculative entries requiring sign-off

None. All 4 new overlay entries are `direct`. The 6 extensions leave the claim_type of their entries unchanged.

---

## Unresolved editorial questions (escalated)

### `ISA-3:1`: hā-ʾāḏôn

**Issue:** הָאָדוֹן is the singular *ʾāḏôn* "lord, master" with the article. It is a different word from the title *ʾăḏōnāy*, which the book renders "the Lord" (3:17, 18; 6:1). If both are "the Lord", the English hides a Hebrew distinction that the book's divine-name house style otherwise keeps. The same title appears at 1:24, 10:16, 10:33 and 19:4.
**Wave ruling applied:** the line reads "the Lord, YHWH of hosts", and commentary names the Hebrew *hā-ʾāḏôn*. A provisional entry, `ha-adon-definite-title-isaiah` (direct, provisional wohChoice), records this.
**Options considered:**
- A. "the Lord" (current). Familiar, but shares its English with *ʾăḏōnāy*.
- B. "the Sovereign". Distinct, and used by some modern versions.
- C. "the Master". The literal sense of the noun; distinct, but less natural as a divine title.

**Why escalating:** this is a book-level divine-name convention that needs a founder ruling. Whatever is chosen must be applied at all five sites at once. 1:24 belongs to the chapter-1 Editor in this same wave, so the two hā-ʾāḏôn entries must be merged into one.
**Editor recommendation:** A, with the commentary note, unless the founder wants the divine titles kept apart in English throughout the book. In that case choose B.

---

## Decisions on the Translator's questions

| # | Ref | Question | Decision | Governing entry |
|---|---|---|---|---|
| 1 | 3:1 | hā-ʾāḏôn | "the Lord"; Hebrew named in commentary. **Escalated** (above) | `ha-adon-definite-title-isaiah` (new) |
| 2 | 3:1 | mašʿēn ûmašʿēnāh | "support and staff" kept; merism explained in commentary | `lexical-cruxes-isaiah-3` (new) |
| 3 | 3:3 | ḥăḵam ḥărāšîm | "the expert craftsman" kept (Masoretic vowels; cf. 2 Kgs 24:14, 16); "magician" reported | `lexical-cruxes-isaiah-3` |
| 4 | 3:3 | nᵉḇôn laḥaš | "the skilled enchanter" kept; one lemma entry covers 3:3 and 3:20; the 26:16 phrase ruling is untouched | `lachash-charm-amulet-isaiah` (new) |
| 5 | 3:3 | nᵉśûʾ p̄ānîm | **changed** to "the man of rank", because the draft used "honored" for two different Hebrew words (3:3, 3:5) | `lexical-cruxes-isaiah-3` |
| 6 | 3:4 | taʿălûlîm | "babes" kept; abstract "caprice" (cf. 66:4) reported | `lexical-cruxes-isaiah-3` |
| 7 | 3:7 | yiśśāʾ | "lift up his voice" kept (ellipsis as at 42:2); oath reading reported | `lexical-cruxes-isaiah-3` |
| 8 | 3:7 | ḥōḇēš | "a healer" kept (ḥbš of wounds, 1:6; 30:26; 61:1); turban reading reported | `lexical-cruxes-isaiah-3` |
| 9 | 3:8 | kāšᵉlāh | "has stumbled" kept; pun on makšēlāh (3:6) noted | `lexical-cruxes-isaiah-3` |
| 10 | 3:8 | ʿênê kᵉḇôḏô | "the eyes of his glory" kept, literal; defective spelling noted | `kevodo-kavod-suffixed-isaiah` (extended) |
| 11 | 3:9 | hakkāraṯ pᵉnêhem | "the look of their faces" kept; "partiality" (Deut 1:17; 16:19) reported | `lexical-cruxes-isaiah-3` |
| 12 | 3:9 | nep̄eš | "Woe to their soul!" kept (Isaiah default, 15:4; 26:9; 29:8; 44:20); not used in the object name at 3:20 | `lexical-cruxes-isaiah-3` |
| 13 | 3:10 | ʾimrû vs ʾašrê | MT kept; the conjectural emendation and the different Old Greek text reported | `mt-qere-textual-policy-isaiah` (extended) |
| 14 | 3:12 | mᵉʿôlēl | "children are their oppressors" kept (MT vocalisation); "glean" (Old Greek sense) reported | `lexical-cruxes-isaiah-3`, `mt-qere-…` |
| 15 | 3:12 | nāšîm vs nōšîm | MT "women" kept; "creditors" reported | `mt-qere-textual-policy-isaiah` |
| 16 | 3:12 | billēʿû | "have destroyed" kept; blʿ "confuse" (19:3; 28:7; cf. 9:15) reported | `lexical-cruxes-isaiah-3` |
| 17 | 3:13 | ʿammîm vs ʿammô | MT "the peoples" kept; Old Greek and Syriac "his people" reported | `mt-qere-textual-policy-isaiah` |
| 18 | 3:14 | biʿartem | "have eaten up" kept; bʿr "graze" (Exod 22:4; Isa 5:5), not bʿr "burn" (6:13) | `lexical-cruxes-isaiah-3` |
| 19 | 3:15 | ketiv mlkm / qere mah-lāḵem | qere translated | `mt-qere-textual-policy-isaiah` |
| 20 | 3:15 | nᵉʾum ʾăḏōnāy YHWH ṣᵉḇāʾôṯ | "says the Lord YHWH of hosts" (combined entries; nᵉʾum "says" as at 14:22–23) | `adonai-yhwh-compound-isaiah-25`, `yhwh-tzevaot-hosts-isaiah` (extended) |
| 21 | 3:16 | ketiv nṭwwt / qere nᵉṭûyôṯ | qere translated, "outstretched necks" | `mt-qere-textual-policy-isaiah` |
| 22 | 3:16 | mᵉśaqqᵉrôṯ | "wanton eyes" kept; "painted eyes" reported | `daughters-of-zion-finery-isaiah-3` (new) |
| 23 | 3:16 | ṭāp̄ōp̄ / tᵉʿakkasnāh | "mincing … jingling with their feet" kept | `daughters-of-zion-finery-isaiah-3` |
| 24 | 3:17 | śippaḥ | "strike with scabs" kept; Old Greek "humble" and "make bald" reported | `daughters-of-zion-finery-isaiah-3` |
| 25 | 3:17 | pōṯ | "secret parts" kept; Akkadian pūtu "forehead" reading reported | `daughters-of-zion-finery-isaiah-3` |
| 26 | 3:18 | ʿăḵāsîm / tip̄ʾereṯ | "the finery of the anklets" kept | `daughters-of-zion-finery-isaiah-3` |
| 27 | 3:18 | šᵉḇîsîm | **changed** to "headbands" ("cauls" is opaque to modern readers); the "little suns" reading reported as uncertain and not adopted | `daughters-of-zion-finery-isaiah-3` |
| 28 | 3:18 | śahărōnîm | "crescents" kept; the protective lunar function is reported as interpretation, not carried in the line | `daughters-of-zion-finery-isaiah-3` |
| 29 | 3:19 | šêrôṯ | "bracelets" kept; "chains" reported | `daughters-of-zion-finery-isaiah-3` |
| 30 | 3:19 | rᵉʿālôṯ | **changed** to "scarves" ("mufflers" is archaic; "veils" is reserved for rᵉḏîḏîm, 3:23) | `daughters-of-zion-finery-isaiah-3` |
| 31 | 3:20 | ṣᵉʿāḏôṯ | "ankle chains" kept (ṣʿd "step"); "armlets" (2 Sam 1:10) reported | `daughters-of-zion-finery-isaiah-3` |
| 32 | 3:20 | qiššurîm | "sashes" kept (Jer 2:32) | `daughters-of-zion-finery-isaiah-3` |
| 33 | 3:20 | bāttê han-nep̄eš | "perfume boxes" kept; "amulet cases" reported | `daughters-of-zion-finery-isaiah-3` |
| 34 | 3:20 | lᵉḥāšîm | "amulets" kept | `lachash-charm-amulet-isaiah` |
| 35 | 3:22 | maʿăṭāp̄ôṯ | "mantles" kept | `daughters-of-zion-finery-isaiah-3` |
| 36 | 3:22 | maḥălāṣôṯ / ḥărîṭîm | "festal robes … purses" kept (Zech 3:4; 2 Kgs 5:23) | `daughters-of-zion-finery-isaiah-3` |
| 37 | 3:23 | gilyōnîm | "hand mirrors" kept (Vulgate); "garments of gauze" (Old Greek, textile context) reported | `daughters-of-zion-finery-isaiah-3` |
| 38 | 3:23 | rᵉḏîḏîm | "veils" kept (Song 5:7) | `daughters-of-zion-finery-isaiah-3` |
| 39 | 3:24 | nip̄qāh | "a rope" kept | `daughters-of-zion-finery-isaiah-3` |
| 40 | 3:24 | maʿăśeh miqšeh | "well-set hair" kept; literal "turned/hammered work" in commentary | `daughters-of-zion-finery-isaiah-3` |
| 41 | 3:24 | pᵉṯîḡîl | "a robe" kept | `daughters-of-zion-finery-isaiah-3` |
| 42 | 3:24 | kî noun vs 1QIsaᵃ bwšt | MT "branding instead of beauty" kept; 1QIsaᵃ "for instead of beauty, shame" reported. Also changed on Editor review, not in response to a question: ḥăḡôrāh "sash" → "girdle", to avoid a clash with qiššurîm "sashes" and keep the root ḥgr audible in "girding" | `mt-qere-…`, `daughters-of-zion-finery-isaiah-3`, central `tachat-substitution-formula` (extended) |
| 43 | 3:25 | gᵉḇûrāṯēḵ | "your mighty in battle" kept (abstract used for the concrete) | `lexical-cruxes-isaiah-3` |
| 44 | 3:26 | wᵉniqqāṯāh | "emptied" kept (nqh "be cleaned out", Zech 5:3) | `lexical-cruxes-isaiah-3` |

The wave rulings were applied as follows:
- *hôy* → "Woe": there is no *hôy* in Isaiah 3, and the *ʾôy* of 3:9 and 3:11 is rendered "Woe" to match.
- MT kept and qere translated: 3:15 and 3:16.
- Finery hapaxes: each has a conventional rendering, uncertainty is stated in commentary, and astral and magical readings are confined to commentary.

On attribution: following the brief, commentary does not cite named English translations (ASV, NRSV, NJPS, KJV) for any reading. It names only the ancient versions (Old Greek, Syriac, Vulgate, 1QIsaᵃ) and the lexica and commentaries. The Reviewer should check these ancient-version claims: Old Greek at 3:10 ("let us bind the righteous"), 3:12 ("glean" / exactors), 3:13 ("his people", with the Syriac), 3:17 ("humble") and 3:23 (transparent garments); Vulgate *specula* at 3:23; 1QIsaᵃ *bwšt* at 3:24.

---

## Glossary changes for review

### Per-translation overlay (`wave-i1-ch3-overlay-diff.json`; base 1.6.1, recommended 1.7.0 shared across the wave)

- Added: `ha-adon-definite-title-isaiah` (claim_type: `direct`; wohChoice provisional, escalated). appliesTo ISA-3:1.
- Added: `lachash-charm-amulet-isaiah` (claim_type: `direct`). appliesTo ISA-3:3, 3:20.
- Added: `daughters-of-zion-finery-isaiah-3` (claim_type: `direct`). appliesTo ISA-3:16–24.
- Added: `lexical-cruxes-isaiah-3` (claim_type: `direct`). appliesTo ISA-3:1, 3, 4, 7, 8, 9, 11, 12, 14, 25, 26.
- Extended: `mt-qere-textual-policy-isaiah` +ISA-3:10, 3:12, 3:13, 3:15, 3:16, 3:24.
- Extended: `yhwh-tzevaot-hosts-isaiah` +ISA-3:1, 3:15.
- Extended: `adonai-standalone-title-isaiah` +ISA-3:17, 3:18.
- Extended: `adonai-yhwh-compound-isaiah-25` +ISA-3:15.
- Extended: `kevodo-kavod-suffixed-isaiah` +ISA-3:8.
- Extended: `title-and-meta-conventions-isaiah` +ISA-3:1 (title ratified; *ʾôy* "Woe").

Each extension carries a `rationaleAppend` sentence. No shipped wohChoice is changed.

### Central glossary (`wave-i1-ch3-central-diff.json`; base 2.93.0, CENTRAL — apply by orchestrator)

- Extended: `tachat-substitution-formula` +ISA-3:24 (complete array given, plus `appliesToAdded`).
- Not extended (recorded): `navi-first-occurrence-abraham` (3:2) and `sodom-as-sodomy-reception-vs-inhospitality` (3:9).

### Notes for the orchestrator

1. **Concurrency.** The ch. 1, 2, 4 and 5 Editors are working from the same bases. When merging:
   - Take appliesTo as the union of the base array and every diff's `appliesToAdded`.
   - Merge `ha-adon-definite-title-isaiah` with any chapter-1 entry for hā-ʾāḏôn at 1:24, keeping one entry per lemma.
2. **nep̄eš.** Isaiah has no overlay entry for *nep̄eš*. Precedent is context-sensitive: "soul" in most places, "life" at 53:10, 12, and "desire" in the 5:14 draft. A book-level entry may be worth creating once the wave is merged. The Editor did not create one, because two parallel chapters (1:14, 5:14) would create it too.
3. **Strong's numbers.** The numbers in the new entries were assigned from memory without a concordance. The finery and lexical-cruxes entries flag this in their `strongs` fields (H113 and H3908 are secure). The Reviewer should verify them.

---

## Post-review corrections (2026-11-26)

These corrections apply the Reviewer's non-decision revisions recorded in the `reviewerReport` block of chapter-3.json.
No English line, `translation.status` (still `awaiting-human`) or `reviewerReport` content was changed, and the shared glossaries were not touched.

1. **3:15 commentary.** The ketiv *mlkm*, read as one word, cannot mean "your king" (that would be *mlkkm*).
   The note now reads: the consonants could be taken as *malkām* "their king", but that is not the received reading.
2. **3:12 commentary.** The "glean" reading needs no change of vowels.
   *mᵉʿôlēl* is now described as the Poel participle of *ʿll* "act as a child", singular and rendered as a collective.
   The alternative is derived from the homonym *ʿll* "deal severely, glean" (Lam 1:22; 2:20), the sense of the Old Greek.
   The same fix is made in `lexical-cruxes-isaiah-3` (overlay diff): the rationale and wohChoice now say "Masoretic reading" instead of "Masoretic vocalisation" / "MT vocalisation".
3. **`daughters-of-zion-finery-isaiah-3` source field.** The first item, יְשַׂקְּרוֹת, is corrected to מְשַׂקְּרוֹת (MT 3:16).
4. **Strong's notes.** In `daughters-of-zion-finery-isaiah-3` and `lexical-cruxes-isaiah-3`, "Reviewer to verify" is replaced with "(checked from Reviewer recall 2026-11-26; not concordance-verified)".
   The numbers themselves are unchanged.
   The note under "Notes for the orchestrator", item 3, still stands: a concordance check before `stable` is advisable.

The escalation on ISA-3:1 (hā-ʾāḏôn) still awaits a founder ruling.
The Reviewer adds that option B, "the Sovereign", has strong modern precedent, and confirms the five-site list (10:16 included).

---

## Founder rulings applied (sign-off 2026-11-26)

The founder accepted every recommended default in `wave-i1-signoff-package.md` ("Sign-off ok", 2026-11-26). `translation.status` and the `reviewerReport` block are untouched; the orchestrator promotes the chapter.

1. **Decision 1, hā-ʾāḏôn, option B.** ISA-3:1 now reads "For behold, the Sovereign, YHWH of hosts, …"; commentary updated, and the verse's glossaryRef renamed to `ha-adon-articular-title-isaiah` (the merged id). The `ha-adon-definite-title-isaiah` add op records the ruling and is marked as superseded at merge; the two `rationaleAppend` texts that named it now point at the merged entry.
