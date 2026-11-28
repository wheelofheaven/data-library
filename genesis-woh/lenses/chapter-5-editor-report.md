# Genesis 5 lens: editor report

Lens file: `genesis-woh/lenses/chapter-5.json`, 0.1.0 (draft) → 0.2.0 (editor-review).
Editor: claude-opus-5-5 (lens editor), 2026-11-27.
Layer 2 (`genesis-woh/chapter-5.json`), `canon-map.json` and all glossaries are untouched.
Validator: `python3 scripts/validate_genesis_lenses.py --core-catalog …/core/model/catalog.json` → 0 errors, 0 warnings; unit tests pass (37).

## Method

- Every assertion attributed to *The Book Which Tells the Truth* (TBWTT) was checked against the cited paragraph in the French original and the project's English text: 2:25, 2:27, 2:41, 2:42, 2:47, 2:48, 2:49, 2:53, 2:58, 3:129, 4:75, 7:13, 7:30.
- Every quotation in curly quotes was matched against the project's English text of TBWTT or the layer-2 English.
- TBWTT and ETTMTTP (all chapters) were grepped for Enoch / Hénoch / Mathusalem / Methuselah. The only hit is an apparatus `commentary` field in TBWTT chapter 2, not canon text, so the Messages are silent on Enoch and Methuselah.
- Hebrew claims were checked against the pointed text in layer 2 (`genesis-woh/chapter-4.json`, `chapter-5.json`, `chapter-6.json`).
- Septuagint figures and wording were checked against Rahlfs (1935) as published in the eliranwong/LXX-Rahlfs-1935 dataset. Samaritan figures were checked against Schorch's edition in the DT-UCPH/sp Text-Fabric dataset. Sanhedrin 108b, Rashi on Genesis 7:4 and the Hebrew of 2 Kings 2 were checked on Sefaria.
- Labels follow `content.md` and the chapter 1–3 convention. A sentence that reports canon content is `framework`. A sentence about what a text does or does not contain is `direct`. A reading the canon does not make of this verse is `inferred`.
- Lessons from the chapter 2–3 reviewers were applied:
  - quotations are verbatim, with the French given where it matters;
  - the house phrase "the project's English text" is used;
  - readings keep the verse's own point, with apparatus moved out of them;
  - silence markers are placed where the Messages do not comment;
  - scholars are named and introduced.
- The naming ruling (YHWH → "the creators" in layers 3–4) is applied.
- The tree-of-life and longevity handling matches the stable chapter 3, 3:22 E p2s4–p2s5.
- Claim 0076 material does not appear (it belongs only at 3:22).

## Changes made

### Metadata

- `lens.version` 0.1.0 → 0.2.0; `lens.status` draft → editor-review; "claude-opus-5-5 (lens editor)" added to `modelDrafts`.
- `lens.coreClaims` unchanged (0001 0.2.0, 0009 0.1.1, 0019 0.1.0; all match the catalog).
- `_lenses.json`: only row 5 was changed (editor-review / 0.2.0). The file was re-read immediately before writing, and row 4 was left as found.

### The record of Adam's line (5:1–2)

- **R 5:1: framework → inferred.** The `coreClaim` 0001 was dropped from the reading; the canon refs 2:25 and 2:27 are kept as context. See flag 4.
- **R 5:2.** "a single name" → "their name". "Single" was an addition; the Hebrew has *shemam*, "their name".
- **E p1s1.** "Many scholars take the chapter to draw on" → "think the chapter draws on". The meaning is unchanged.
- **E p1s2.** Glossed *shemam* as "their name".
- **E p1s3.**
  - "The verbs" → "The finite verbs". *Bero'* in 5:1 is an infinitive and has no number.
  - Added *vaybarech*.
- **E p2s1.** Added the French « créer un homme comme nous artificiellement ». Changed "the likeness" to "the likeness of Genesis 1", since TBWTT 2:25–27 comment on 1:26–27, not on this verse.
- **E p2s2 (inferred).** Now states the link openly: "The Messages cite Genesis 5 only for the lifespans, not for this verse." The pairing with 1:26–27 is the project's. Canon ref TBWTT-2:49 added.

### From Adam to Jared (5:3–20)

- **R 5:9–11.** "the third of the chiefs whom the Messages name" was apparatus. It now reads "He too was among the chiefs granted the “tree of life”" and stays framework, since TBWTT 2:49 names Enosh.
- **R 5:12–20.** Dropped "the longest life so far", which was apparatus.
- **E p1s2.**
  - Exact Hebrew: *bidmuto ketsalmo* against 1:26 *betsalmenu kidmutenu*. The order of the nouns *and* their prepositions are reversed.
  - "What humankind received … passes from father to son" is now attributed to commentators.
- **E p2s1.**
  - The context of TBWTT 2:47–48 is restored: the Messages read the offerings of 4:3–4 as food brought to the exiled creators.
  - The 2:49 quotation is now complete, including "(in Genesis V, 1-11)".
  - Canon refs: 2:47, 2:48, 2:49.
- **E p2s2.** Reworded to stay close to 2:48: "showing that the humans would stay loyal to their makers" (FR « bons et ne se retourneraient jamais contre leurs pères »). Added ref 2:42, the canon's quotation of 3:22.
- **E p3s1.** Nested quotation marks normalised (see flag 1).
- **E p3s2.** "The shortest life is Lamech's 777" was false as worded, because Enoch's 365 is shorter. It now reads "Of the men who die, Lamech has the shortest life".
- **E p5s1.**
  - Added the Samaritan Flood year (1307). In the SP figures Jared, Methuselah and Lamech all die in that year.
  - All the numbers are now verified (see the table).

### Enoch (5:21–24)

- **R 5:24.** The apparatus was trimmed to one clause: "Unlike the others in the list, he is not said to have died." "The verse does not say where he was taken" moved out of the reading. The explanation already makes the point.
- **E p1s1 (marker).** "what follows is" → "what follows on him is". This is the chapter 2 form for a partial silence; the passage's map coverage is `alludes`.
- **E p1s2.**
  - Removed "*YHWH-Elohim*" (naming ruling). The text now says that 3:8 uses the same reflexive form of *halach* "for the walking about in the garden".
  - Added that 6:9 again has *ha-elohim* with the article, which the layer-2 Hebrew confirms.
- **E p1s4 (Enmeduranki), rewritten.**
  - Jude 14 is quoted ("the seventh from Adam").
  - The comparison with En-men-dur-ana is attributed to scholars. The figure is the seventh king before the flood in WB 444, ruling at Sippar, the city of Shamash.
  - The later Babylonian text is attributed to its editor, "the Assyriologist W. G. Lambert in 1967". It has Shamash and Adad receive Enmeduranki into their assembly and teach him divination.
  - The draft's "admits to the assembly of the gods" was too broad.
  - A closing sentence respects 0019's exclusion: "The comparison is the scholars'; this reading does not identify the patriarch with the king."
- **E p3s1.** Nested quotation marks normalised.
- **E p3s2.** "Read with the Messages' Elohim, the creators" → "With the Messages' reading of the Elohim as the creators". Grammar fix; inferred and 0009 kept.
- **E p3s3 (speculative).** Opening reworded to "A further Wheel of Heaven reading goes beyond this". The substance is unchanged.

### From Methuselah to Noah (5:25–32)

- **R 5:25–27.** Dropped "the longest life in the line", which was apparatus.
- **R 5:30–31.** Dropped "the shortest of the long lives in the list", which was apparatus and also inaccurate (see E p3s2 above). The reading now ends like the verse: "He reached seven hundred and seventy-seven years, and then he died."
- **E p1s1.** Rabbinic tradition is now attributed exactly. In Sanhedrin 108b Rav reads the seven days of 7:10 as mourning for Methuselah, and Rashi repeats it on 7:4.
- **E p1s2 (inferred).** "Carried down the line" could suggest that the grant was inherited, which TBWTT 2:53 denies. It now reads: "each granted the “tree of life” in his own right, since the Messages say longevity was not inherited". Added ref 2:53.
- **E p1s3.**
  - The quotation of 4:24 is now verbatim from layer 2 ("seventy-and-seven"; the draft had "seventy and sevenfold").
  - "echo" → "recall".
- **E p2 (new marker).** "The Messages do not comment on Noah's naming; what follows on it is a Wheel of Heaven reading."
- **E p2s2 (was p2s1).**
  - "The ground “which YHWH cursed”" was not verbatim (layer 2 has "has cursed") and conflicted with the naming ruling. It became "The cursed ground takes up 3:17".
  - The divine name is kept once, as a philological fact: 5:29 is the only verse of the chapter with *YHWH*. This follows the chapter 3 precedent of one direct segment that names the Hebrew form.
  - Added the Septuagint's "he will give us rest" (διαναπαύσει ἡμᾶς). It supports the *nuach* observation.
- **E p3s2.** The sentence was ungrammatical ("the man whom the exiles … had asked Noah"). It was rebuilt around the verbatim fragment "forewarned of the matter, had asked Noah to build a rocket that was to orbit the Earth during the cataclysm" (2:58).

## Label changes

| Unit | Old | New | Reason |
|---|---|---|---|
| R 5:1 | framework (synthesis, 0001) | inferred (synthesis, canon refs as context) | The canon does not read 5:1; it comments on 1:26–27 (2:25–27) and cites 5:1–11 only for lifespans (2:49). The pairing is the project's. 0001 stays bound in E p2s1. |
| E 5:25–32 p2s1 (marker) | — | direct (new) | Silence marker |

No other label changed. The single speculative segment is unchanged in substance.

## Writer's flags resolved

1. **Nested quotation marks.**
   - Convention adopted: double curly quotes outside, single curly quotes inside, whatever the project's English text prints inside. It prints “…” at 2:49 and 2:53, and «…» at 4:75 and 7:13.
   - Only the marks change; the words are verbatim.
   - French quotations keep French guillemets, as in chapter 3.
   - Affected segments: 3–20 E p2s1, E p2s3, E p3s1; 21–24 E p3s1.
2. **MT, SP and LXX numbers.** All are verified (see the table). The draft's figures were correct. The SP Flood year (1307) was added.
3. **Scholarship.**
   - Verified on Sefaria: Sanhedrin 108b / Rashi, and 2 Kings 2.
   - Verified against Rahlfs: LXX 5:24 and 5:29.
   - Verified against the data-library text: Hebrews 11:5, first clause.
   - Enmeduranki: softened and attributed (Lambert 1967); see the table.
4. **Labels.**
   - Readings 5:4–5, 5:6–8 and 5:9–11 are framework, basis canon. **Confirmed.** TBWTT 2:49 names Adam (930), Seth (912) and Enosh (905).
   - The "etc." extension (5:12–20, 5:25–27, 5:30–31) is inferred. **Confirmed.**
   - 5:1 is now inferred (see above).
5. **Enoch's speculative segment.**
   - Kept. It is labelled, it states "Nothing in the canon says this of Enoch", and it rests only on the Messages' explicit account of Elijah (3:129, 4:75), cited as such.
   - 0019's exclusions are respected:
     - E 3–20 p4s3 disclaims chronology and king-matching;
     - the MT, SP and LXX arithmetic is reported as a fact about the texts, not used as a dating;
     - the Enmeduranki comparison is attributed to scholars and explicitly not adopted.

## Verification table

| Item | Status | Basis |
|---|---|---|
| MT ages and the 1656 Flood year; Methuselah dies in the Flood year | verified | Layer-2 Hebrew/English 5:3–32; 7:6 |
| SP: Jared 62/785/847, Methuselah 67/653/720, Lamech 53/600/653; Flood year 1307 | verified | Schorch SP (DT-UCPH/sp, `g_cons_utf8.tf`); arithmetic recomputed |
| LXX: +100 for Adam (230), Seth (205), Enosh (190), Kenan (170), Mahalalel (165), Enoch (165); Jared 162 unchanged; Methuselah 167/802/969; Lamech 188/565/753; Flood 2242 | verified | Rahlfs 1935 (eliranwong dataset); arithmetic recomputed; Methuselah dies in 2256, 14 years after the Flood |
| LXX alternative 2262 (Methuselah at 187) | editor's knowledge | Codex Alexandrinus and other witnesses read 187; standard (e.g. Hendel 1998; Klein, *HTR* 67, 1974). Not checked against a manuscript |
| 930 / 912 / 905 identical in MT, SP, LXX | verified | All three texts above |
| LXX 5:24 εὐηρέστησεν … οὐχ ηὑρίσκετο ὅτι μετέθηκεν αὐτὸν ὁ θεός | verified | Rahlfs |
| LXX 5:29 διαναπαύσει ἡμᾶς | verified | Rahlfs |
| Hebrews 11:5 "By faith Enoch was translated that he should not see death" | verified | `hebrews/chapter-11.json` v. 5 (identical in KJV/ASV) |
| Jude 14 "the seventh from Adam" | editor's knowledge | KJV; `jude/chapter-1.json` has no text to check against |
| Sanhedrin 108b (Rav, on 7:10) and Rashi on 7:4: mourning for Methuselah | verified | Sefaria API |
| *laqach* in 2 Kings 2:3, 5, 9, 10 | verified | Sefaria Hebrew |
| *hithallech et-ha-elohim* in 5:22, 5:24 and 6:9; *mithallech* in 3:8 | verified | Layer-2 Hebrew |
| *bidmuto ketsalmo* (5:3) vs *betsalmenu kidmutenu* (1:26) | verified | Layer-2 Hebrew |
| *sefer toledot* unique to 5:1 | editor's knowledge | Standard (concordance) |
| *YHWH* only at 5:29 in Gen 5 | verified | Layer-2 Hebrew 5:1–32 |
| *itsavon* at 3:17 and 5:29 | verified | Layer-2 Hebrew |
| 4:24 "seventy-and-seven"; Cain's line 4:17–18 | verified | Layer-2 English/Hebrew |
| SKL WB 444: 8 kings, 5 cities, 241,200 years; Alulim 28,800; En-men-dur-ana 7th, at Sippar | editor's knowledge | Jacobsen, *The Sumerian King List* (1939); standard |
| Berossus: 10 kings, 432,000 years, Xisouthros; 3rd century BCE | editor's knowledge | Standard (Burstein 1978; Verbrugghe & Wickersham 1996) |
| Lambert, "Enmeduranki and Related Matters", *JCS* 21 (1967): 126–138: Shamash and Adad, assembly, oil and liver divination | editor's knowledge | Not checked against the article; wording kept to the core of the text. Reviewer may spot-check |
| Abraham 175 (25:7); Moses 120 (Deut 34:7) | editor's knowledge | Standard |
| TBWTT quotations (2:25, 2:27, 2:41, 2:48, 2:49, 2:53, 2:58, 3:129, 4:75, 7:13, 7:30) | verified | French original and the project's English text, word for word (inner quotation marks normalised) |
| Canon silent on Enoch / Methuselah | verified | Grep of TBWTT and ETTMTTP, all chapters |

## Notes for the reviewer and the orchestrator

- **TBWTT 3:129 typo.** The project's English text reads "In II Kings, II Elijah …". The French « Dans II Rois, II Elie » means "2 Kings, chapter 2". The quotation keeps the printed text. A translation-track erratum could render it "In II Kings II, Elijah …".
- **Chapter 4 overlap.** E 3–20 p2s1 now cites TBWTT 2:47–48, the reading of Cain's and Abel's offerings as food for the exiled creators. The chapter 4 editor, working in parallel, should treat 4:3–4 compatibly.
- **Scope.** No layer-2, canon-map or glossary edits were made, and no errata were added to the queue.

## Founder escalations

### 1. Speculative segment: Enoch taken alive (5:21–24 E p3s3)

**Text:** "A further Wheel of Heaven reading goes beyond this: Enoch left with the creators alive, as the Messages say Elijah did. Nothing in the canon says this of Enoch."

**Why speculative:** The Messages speak of Elijah being taken alive and of his survival through the tree of life (3:129, 4:75). They never mention Enoch. Transferring their account to Enoch rests on the shared verb *laqach*, which is the project's synthesis.

**Recommendation:** Ship as labelled.

### 2. R 5:1 relabelled framework → inferred

**Issue:** The draft labelled the reading framework, bound to 0001. The canon's likeness statements (2:25–27) gloss 1:26–27, and 2:49 cites 5:1–11 only for the lifespans.

**Recommendation:** Confirm inferred. The framework claim 0001 stays bound in E p2s1, where the canon is quoted.

### 3. Enmeduranki comparison kept (5:21–24 E p1s4)

**Issue:** The segment is direct scholarship and explicitly does not identify Enoch with the king, in line with 0019's exclusion.

**Options:**

- **A.** Keep.
- **B.** Cut, if the founder thinks any king comparison in the reader invites matching.

**Recommendation:** A.

## Post-review corrections (2026-11-27)

The reviewer's report is in `lens.reviewerReport` (48 approve, 3 revise).
The coordinator asked for revise items 2 and 3, plus the optional article note.
`lens.status` (awaiting-human), `lens.version` (0.2.0), `reviewerReport` and the `_lenses.json` row are unchanged.
Validator: 0 errors, 0 warnings.

1. **5:1–2 E p1s2, applied with the reviewer's proposed text.** *Adam* already names the man at 4:25, so "only from verse 3 on" was false. The segment now says that in verse 2 *adam* is the name of humankind, and that in verse 3 it is again one man's name, "as it already was at 4:25".
2. **5:3–20 E p3s2, applied with the reviewer's proposed text.** The 750–1,200 range now holds explicitly "in the Masoretic figures". The Septuagint stays inside it (Lamech 753). In the Samaritan figures, Methuselah (720) and Lamech (653) fall below it. Both Samaritan figures were already verified against Schorch's edition (see the verification table).
3. **Optional item, added as 5:21–24 E p1s3 (direct, new).**
   - The article is in *et-ha-elohim* (5:22, 5:24a), against bare *elohim* in "for Elohim took him" (5:24b). This is verified in the layer-2 Hebrew.
   - The quotation of *Jubilees* is verbatim from Charles's translation in `book-of-jubilees/chapter-4.json`: "was moreover with the angels of God these six jubilees of years". It is cited as 4:21, Charles's standard numbering. The data-library file merges verses, and `jubilees-woh` numbers the verse differently.
   - I did not attribute the reading to VanderKam, because I could not check his wording.
   - The segment reports how the phrase has been read. The lens does not draw on *Jubilees* as a source, as E p2s1 states.
4. **Not changed: R 5:1 label (revise item 1).** It stays inferred, pending the founder's ruling. The reviewer prefers framework with 0001; the alternative is inferred with "men like themselves" removed.
