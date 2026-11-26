# Chapter 19 Editor Report

Isaiah wave I-4. Base: central glossary 3.0.0 and overlay 2.0.0, both read-only.
Status: `editor-review`. Version: `1.0.0-rc1`.
All 20 editorial questions are resolved and the array is empty.
All 25 verses carry official commentary.
These sources were checked on 2026-11-26:

- Sefaria API v3 for JPS 1917, NJPS (the 1985 "Tanakh: The Holy Scriptures"), and Koren.
- bible-api.com for ASV.
- The project's own canon and Baal Cycle texts in data-library.

Citations not checked in this pass are marked "recalled" or "not checked" in the commentary.

## Speculative entries requiring sign-off

No glossary entry is speculative.
One commentary paragraph is labelled speculative under wave I-4 ruling 9.

### ISA-19:1 commentary, final paragraph ("Wheel of Heaven reading")

**Source:** *hinnēh YHWH rōḵēḇ ʿal-ʿāḇ qal* "Behold, YHWH rides on a swift cloud".
**WoH choice:** The line is unchanged and philological (ASV, JPS 1917, NJPS).
Only the commentary carries the reading.
**Why speculative:** The canon does not cite Isa 19.
I searched the data-library texts of TBWTT, ETTMTTP and LWTE.
TBWTT cites Isaiah 6, 13, 14, 15, 26, 27, 29, 32, 40, 42, 43, 44, 45, 48, 54 and 65, but not chapter 19.
The paragraph quotes two places where TBWTT reads a cloud as a craft:

- TBWTT 3:107 on 1 Kgs 8:12: "That he dwells in a cloud — that is, in a craft in orbit around the Earth, above the clouds".
- TBWTT 3:259–260 on Job 37:18: "«solid clouds», in reality metallic flying craft".

Applying those readings to Isa 19:1 is a project extension.
The paragraph also says that the central rider-of-the-clouds entry rejects the vehicle reading of the Ugaritic epithet.
**Recommendation:** Ship as labelled, following the founder's practice at 4:5, 7:14, 9:5 and 11:12. The founder must confirm it by name.

---

## Unresolved editorial questions

None of these blocks the chapter.
The Reviewer and the founder should check the following judgement calls.

### `ISA-19:12` (ruling 13)

**Issue:** *ḥăḵāmêḵā* is rendered "your wise men", against NJPS "your sages".
**Decision:** I kept "wise men".
The noun names a specific body, Pharaoh's court sages, which are the "counselors of Pharaoh" of v11.
Under ruling 13 that body keeps "men", and the stable 29:14 has "its wise men".
The generic plural of v11, *ben-ḥăḵāmîm*, stays neutral as "a son of the wise".
**Why flagged:** This applies ruling 13 to a professional class rather than a military group.
If the founder reads ruling 13 narrowly, the alternative is "your sages".

### `ISA-19:3` (*hāʾiṭṭîm*)

**Issue:** This hapax keeps ASV "the charmers".
The alternatives are JPS 1917 "the whisperers" and NJPS "the shades", which follows Akkadian *eṭemmu* "spirit of the dead" (HALOT, recalled).
**Options considered:** (A) "the charmers" (taken). (B) "the shades", which collides with *rᵉp̄āʾîm*. (C) "the spirits of the dead", which collides with "ghosts" for *ʾōḇôṯ*.
**Why flagged:** "Charmers" makes one item of the list a practitioner while the others are spirits. Each alternative causes a collision.

### `ISA-19:2` (Egypt / Egyptians convention)

**Decision:** The line has "Egyptians against Egyptians" only at v2.
Everywhere else it has "Egypt" where the Hebrew has the name. ASV has "the Egyptians" at vv. 4, 16, 21 and 23.
The chapter 18 and 20 Editors may want the same convention.

### `ISA-19:24` (*ʾereṣ*)

**Decision:** "in the midst of the earth", under overlay `eretz-cosmic-scope-isaiah-24`, not the central `eretz` default "land".
This agrees with ASV, JPS 1917 and NJPS. Koren's "land" is recorded in the commentary.

---

## Line changes (each governed by a glossary entry)

1. **19:3**: "shall fail" became "shall be emptied". The verb is the Niphal of *bqq*, as at 24:3, and "fail" is kept for *nšt* in v5. Entry: `lexical-cruxes-isaiah-19`.
2. **19:7–8**: "the river" became "the Nile" for singular *yᵉʾôr* (four times). This applies wave I-4 ruling 15, and the change keeps *yᵉʾôr* distinct from bare *nāhār* "the river" in 19:5. Entry: central `yeor-nile-egyptian-loanword`, appliesTo only.
3. **19:13**: "they have led Egypt astray, the cornerstone of her tribes" became "those who are the cornerstone of her tribes have led Egypt astray". This follows the ASV construal, because the draft's word order made the phrase seem to describe Egypt. Entry: `lexical-cruxes-isaiah-19`.

All other lines are the Translator's draft, unchanged.
That includes 19:1 "rides on a swift cloud" and 19:18 "the City of Destruction" (MT, ruling 5).

---

## Glossary changes for review

### Central glossary (`wave-i4-ch19-central-diff.json`, proposed 3.0.0 to 3.1.0, minor)

No central entry was added.
All 8 central changes add `appliesTo` sites, and most append one rationale sentence. None has a `changes` field.

- Modified: `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany`, +ISA-19:1. The appended note records the clause-not-epithet rendering and the project's Baal Cycle line references.
- Modified: `elilim-idols-cross-corpus`, +ISA-19:1, 19:3.
- Modified: `yeor-nile-egyptian-loanword`, +ISA-19:6, 19:7, 19:8. This is appliesTo only, under ruling 15. The chapter 23 Editor owns the `changes.wohChoice` context clause.
- Modified: `adam-adamah`, +ISA-19:17 ("the ground of Judah").
- Modified: `eretz`, +ISA-19:18, 19:19, 19:20 ("the land of Egypt").
- Modified: `mizbeach-olah`, +ISA-19:19.
- Modified: `matzevah-sacred-pillar-patriarchal-religion`, +ISA-19:19.
- Modified: `qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus`, +ISA-19:21.

### Per-translation overlay (`wave-i4-ch19-overlay-diff.json`, proposed 2.0.0 to 2.1.0, minor)

- Added: `rokhev-al-av-qal-swift-cloud-isaiah-19` (claim_type: `direct`). It is a dedicated audit entry for the lens-salient site.
- Added: `ir-haheres-city-of-destruction-isaiah-19` (claim_type: `direct`). MT goes in the line. The variants (*ḥeres* "sun", 1QIsaᵃ as reported, the Vulgate, the LXX *asedek*, and the Targum as NJPS reports it) are recorded in the entry without a ruling.
- Added: `lexical-cruxes-isaiah-19` (claim_type: `direct`). It covers the single-site decisions of vv. 2–25.
- Modified (appliesTo, some with a rationaleAppend):
  - `massa-oracle-superscription-isaiah` (+19:1)
  - `ha-adon-articular-title-isaiah` (+19:4)
  - `ob-yiddeoni-ghosts-familiar-spirits-isaiah` (+19:3)
  - `yhwh-tzevaot-hosts-isaiah` (+19:4, 12, 16, 17, 18, 20, 25)
  - `mt-qere-textual-policy-isaiah` (+19:9, 10, 18)
  - `eretz-cosmic-scope-isaiah-24` (+19:24)
  - `title-and-meta-conventions-isaiah` (+19:1)

### Notes for the orchestrator

- The new overlay entries include `translit` fields because the op schema lists them. Paragraph-level `translit` was not added or edited. Drop the entry `translit` fields if the orchestrator generates them.
- Strong's numbers in the new entries come from recall and are marked as not concordance-verified.
- `glossaryRefs` at 19:24 now point to `eretz-cosmic-scope-isaiah-24` instead of central `eretz`.
- 19:1 now also references `rokhev-al-av-qal-swift-cloud-isaiah-19`.
- Reception at 19:18–25 appears only in labelled "Reception" paragraphs (19:19, 19:25) and in the variant discussion of 19:18. It covers Josephus on the Onias temple, m. Menaḥ. 13:10, and the LXX of 19:25, all marked as recalled. None of it touches the lines.

---

## Post-review corrections

These follow the Reviewer's report of 2026-11-26.
`translation.status` stays `awaiting-human`, and the `reviewerReport` block is untouched.
No English line changed, and no shared glossary was edited.

1. **19:18 commentary.** The sentence now reads "Others hold that MT is original (not verified)."
   I removed the names of Wildberger and Blenkinsopp because I could not check either commentary in this pass.
2. **`lexical-cruxes-isaiah-19` rationale (overlay diff).** The closing claim now has an exception: "except 19:16 'waving … waves', which follows the book's concordance with 11:15 (Hiphil nûp̄, BDB 'wave, brandish')."
3. **19:9 commentary and the `mt-qere-textual-policy-isaiah` rationaleAppend.** "NJPS reads/repoints as a verb" is softened.
   NJPS prints "chagrined" and notes only "Meaning of Heb. uncertain". Its rendering appears to take the word as a verb.
4. **19:12.** The line keeps "your wise men".
   `lexical-cruxes-isaiah-19` wohChoice now stages "your sages" (NJPS) under the marker "PENDING FOUNDER RULING". The founder needs to decide whether ruling 13 extends to a professional class.
5. **Central housekeeping (founder-gated, staged only).** I checked every KTU site of `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany` against the `baal-cycle-woh` edition, which covers KTU 1.1–1.4.
   - *rkb ʿrpt* is printed only at 1.2-iv:6, 1.3-ii:40, 1.3-iv:23 and 1.4-vi:10.
   - 1.3-iv:4 reads "She enters to Baʿlu on the heights of Ṣapunu".
   - 1.4-iii:11 reads "[…] Baʿlu, the noble ones confront".
   - 1.4-v:7 reads "[Eight, or fi]ve years".
   - 1.5-ii:7 lies outside the edition and is not verified.
   - 1.4-vii:32 has *b ʿrpt* "in the clouds". It is not an epithet site, but the Baal Cycle line cites the entry.

   The corrected full values for `partOfSpeech`, `rationale` and `appliesTo` are in `wave-i4-orchestrator-ops.json` under `central.set`.
   `appliesTo` drops 1.4-iii:11 and 1.4-v:7. It keeps 1.4-vii:32, and the rationale now explains why.
   A `_pendingFounder` note in that file names the change, which is a modification of existing fields (major if strictly applied). The central glossary itself was not edited.
