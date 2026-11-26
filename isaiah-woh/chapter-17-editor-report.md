# Chapter 17 Editor Report

Isaiah wave I-4. Chapter 17 is the oracle concerning Damascus (17:1–11) followed by the roaring of the peoples (17:12–14).
Read base: overlay 2.0.0, central 3.0.0. Proposed merge targets: overlay 2.1.0, central 3.1.0.
`translation.status` is now `editor-review` and `translation.version` is `1.0.0-rc1`. `glossaryVersion` and `overlayGlossaryVersion` are left at the read base (3.0.0 / 2.0.0); the orchestrator updates them when the diffs are merged.

References checked on 2026-11-26:
- ASV and KJV through bible-api.com.
- JPS 1917 and NJPS through the Sefaria API v3 (`version=english|all`). NJPS here is "Tanakh: The Holy Scriptures, published by JPS" (1985), not the Gender-Sensitive Edition.

Several readings the Translator gave from memory were corrected after checking:
- NJPS 17:8 reads "incense stands", not "incense-altars".
- The LXX readings at 17:2 and 17:9 are now cited from NJPS's own notes. The LXX text itself was not checked.
- NRSV is still marked "recalled, not verified" wherever it is cited.

## Speculative entries requiring sign-off

None. No entry or commentary paragraph in this chapter is `speculative`.

The Wheel of Heaven canon does not cite Isaiah 17. The editor searched the data-library texts of *The Book Which Tells the Truth*, *Extraterrestrials Took Me to Their Planet* and *Let's Welcome the Extraterrestrials*; the only Isaiah "17" hit is XIV-17. For that reason the chapter has no speculative lens paragraph.

---

## Unresolved editorial questions

None of the 13 Translator questions is left open. Every one is resolved either into the new overlay entry `lexical-cruxes-isaiah-17` or into extensions of existing entries. The items below are decisions the founder or Reviewer may want to look at.

### `ISA-17:11` (line changed: two wording changes)

**Issue:** The Translator's line followed ASV throughout: "you hedge it in … the harvest flees away". The editor changed two phrases:
- "you make it grow" for *tᵉśaḡśēḡî*. This follows JPS 1917, KJV and NJPS, and the parallel with *taprîḥî* "you make blossom".
- "the harvest shall be a heap" for *nēḏ qāṣîr*. This keeps the Masoretic pointing: *nēḏ* is the noun "heap", as in Exod 15:8. KJV and JPS 1917 read the same way.

**Options considered:**
- A. ASV unchanged.
- B. "make it grow" only.
- C. Both changes. This was adopted.

**Why escalating:** C is grounded in the book's MT policy (`mt-qere-textual-policy-isaiah`), but "the harvest shall be a heap" is a harder English sense than ASV's "flees away". ASV, NJPS and (recalled) NRSV all read the verb *nwd*. **Recommendation:** ship C. Fall back to B if the founder prefers the majority modern sense over the strict MT pointing.

### `ISA-17:10` (Adonis plantings)

**Issue:** The reading "plantings of the Pleasant One (Adonis)" for *niṭʿê naʿămānîm* is a history-of-religions hypothesis.

**Decision:**
- The line keeps "pleasant plants" (ASV). JPS 1917 and NJPS also render the word as an adjective.
- The Adonis reading is given in a commentary paragraph labelled "Comparative note (history-of-religions reading, not adopted in the line)". That paragraph says plainly that the Hebrew names no god.
- The central `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus` entry is **not applied**. It is not in glossaryRefs and not in appliesTo. It is named in the note as the place where the comparative material is collected.

The editor's account of the scholarship is from memory and is labelled that way in the note.

**Why escalating:** for awareness only, because this material sits close to the lens. **Recommendation:** ship as is.

### `ISA-17:9` and `ISA-17:13` (concordance departures, recorded)

- 17:9: *ʾāmîr* is "mountain top" (ASV), although 17:6 has "uppermost bough".
- 17:13: *sûp̄āh* is "storm" (ASV, JPS 1917), although 5:28 and 29:6 have "whirlwind". This avoids "whirling dust before the whirlwind".

Neither word falls under a strict concordance rule. Both departures are recorded in `lexical-cruxes-isaiah-17`. **Recommendation:** ship.

### `ISA-17:7` ("humankind")

Under `adam-humankind-ish-man-isaiah`, *hāʾāḏām* is "humankind", and its singular suffixes take plural English pronouns.

The context may mean only the survivors of Israel (17:4–6). The commentary leaves the scope open, as the Hebrew does. **Recommendation:** ship. The house rule governs here.

---

## Glossary changes for review

### Central glossary (`wave-i4-ch17-central-diff.json`)

- Version: 3.0.0 → 3.1.0 (minor).
- Modified: `asah`, appliesTo + ISA-17:7, ISA-17:8. A rationale addendum covers "Maker" against human "made / work"; wohChoice is unchanged.
- Deliberately not extended (recorded in the version note):
  - `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus` (17:10)
  - `refaim-giant-peoples` (17:5, toponym)
  - `athirat-asherah-mother-goddess-cross-corpus-ugaritic-hebrew-bible` (17:8, cult object)
  - `mizbeach-olah` (17:8)

### Per-translation overlay (`wave-i4-ch17-overlay-diff.json`)

- Version: 2.0.0 → 2.1.0 (minor).
- Added: `lexical-cruxes-isaiah-17` (claim_type: `direct`). appliesTo: 17:1–6 and 17:9–14.
- Modified, appliesTo only or with a rationale addendum. No wohChoice or claim_type was changed.
  - `massa-oracle-superscription-isaiah`: + 17:1. The Translator had applied it beyond its appliesTo; this extends it properly.
  - `aram-names-isaiah`: + 17:1, 17:3.
  - `title-and-meta-conventions-isaiah`: + 17:1. The Translator's ref at 17:6 was dropped.
  - `yhwh-tzevaot-hosts-isaiah`: + 17:3.
  - `elohei-yisrael-god-of-israel-isaiah-24`: + 17:6, 17:10. The 17:10 extension covers the construct epithet "the God of your salvation".
  - `adam-humankind-ish-man-isaiah`: + 17:7, 17:8. This extends the Translator's use properly; the pronoun rule carries into 17:8.
  - `asherim-chammanim-cult-purge-isaiah-27`: + 17:8. This extends the Translator's use properly. The addendum corrects the NJPS citation to "incense stands".
  - `yah-tzur-olamim-everlasting-rock-isaiah-26`: + 17:10. This extends the Translator's use properly, for lower-case "rock" only.
  - `maoz-shalom-refuge-peace-isaiah-27`: + 17:9, 17:10. This extends the Translator's use properly, with a context clause for "strong cities" at 17:9.
  - `hoy-woe-isaiah`: + 17:12.
  - `mt-qere-textual-policy-isaiah`: + 17:2, 17:3, 17:9, 17:10, 17:11.
- Deliberately not extended: `rephaim-shades-dead-isaiah-26` (17:5, toponym).
- Concurrency: the Editors for chapters 16 and 18–23 work from the same base. The likely overlaps are listed in the version op; merge them as a union.

---

## Post-review corrections

The Reviewer returned the chapter on 2026-11-26 with status `awaiting-human`. The Editor applied the following after reading the `reviewerReport`. `translation.status`, the `reviewerReport` block and the shared glossaries were not changed.

1. **ISA-17:10, the Reviewer's revise.** The comparative paragraph no longer states that *Naʿămān* is "a Phoenician epithet of Adonis". It now reads: "They take *Naʿămān* as an epithet of Adonis, an inference from Ugaritic *nʿmn* 'gracious' and the Arabic name of the anemone, and see here …". It remains marked as recalled from memory. It now names Wildberger and Blenkinsopp on 17:10 as the editions that were not checked. A human should check one of them before publication.
2. **ISA-17:2, line change.** "and they shall lie down" → "which shall lie down" (ASV, JPS 1917). The masculine *wᵉrāḇᵉṣû* refers to the flocks, not the feminine cities. The change is recorded in the `lexical-cruxes-isaiah-17` add op in `wave-i4-ch17-overlay-diff.json` (wohChoice, standardEnglish and a rationale addendum), and the verse note explains it.
3. **Note refinements:**
   - 17:3: added the fronted-subject (casus pendens) reading of the athnach clause, and removed the claim that the accents necessarily join the remnant to the list.
   - 17:7: named the 2:8 / 2:20 echo as the reason for "humankind", said the word leans universal, and gave "people" as the narrower option.
   - 17:9: said that *ʾāmîr* means only "top, summit" and that "mountain" is ASV's addition.
   - 17:11: NJPS "you see it grow" is now described as taking the word as growth but not as causative. The support is restated as JPS 1917 and KJV.

Line changes after review: one (17:2). The chapter total is now two verses, 17:2 and 17:11.
