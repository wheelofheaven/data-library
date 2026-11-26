# Chapter 8 Editor Report

Isaiah wave I-3. Editor: claude-opus-5-5 acting as woh-editor, 2026-11-26.
`chapter-8.json` is now `editor-review`, version `1.0.0-rc1`. All 20 editorial questions are resolved and the array is empty.
Commentary: 19 of 23 verses. The four without commentary (8:5, 8:13, 8:15, 8:17) follow ASV and raise no lexical question.
Diffs: `wave-i3-ch8-overlay-diff.json` (1 version, 2 add, 8 modify, 1 note) and `wave-i3-ch8-central-diff.json` (1 version, 2 modify, 1 note).

## Speculative entries requiring sign-off

None. Both new entries are `direct`. The commentary contains no Wheel of Heaven reading.
The 8:19 note says that *ʾĕlōhîm* can denote the dead (1 Sam 28:13). That is a lexical fact, not a lens claim.

---

## Changes to the English line

There are two changes. Each is backed by a glossary entry:

- **8:19** "Seek those who have familiar spirits and the wizards, who chirp and who mutter" becomes "Seek the ghosts and the familiar spirits that chirp and mutter". The new overlay entry is `ob-yiddeoni-ghosts-familiar-spirits-isaiah`. The participles describe the spirits' voices, as at 29:4. JPS 1917 and NJPS have the same rendering (both verified).
- **8:22** "look to the land" becomes "look to the earth". The basis is the cosmic context clause of central `eretz`, here an above/below contrast with "upward" in 8:21. ASV, KJV and JPS 1917 all read "earth" (verified).

Every other line is the Translator's draft.

---

## Unresolved editorial questions (for the human reviewer)

### `ISA-8:19` — who speaks, and what *ʾĕlōhāyw* means

**Issue:** *hălôʾ-ʿam ʾel-ʾĕlōhāyw yiḏrōš, bᵉʿaḏ haḥayyîm ʾel-hammēṯîm* can be read two ways:
- as the prophet's retort, "should not a people seek their God?" (ASV, verified; KJV, whose unpunctuated rhetorical questions allow it; RSV, not verified);
- as the advisers' speech continuing through 8:20a. JPS 1917 punctuates it so, opening the quotation before "Seek" and closing it after "for instruction and for testimony?", while printing "their God" (verified, corrected post-review). NJPS also continues the quotation and takes *ʾĕlōhîm* as the dead: "for a people may inquire of its divine beings — of the dead on behalf of the living —", noted "the shades of the dead" (verified). NRSV is reported to have "their gods" (not verified).

The Translator's note said that NRSV supports the "God" reading. That is probably wrong.

**Options considered:**
- (A) Keep the line as it is, with "their God" and the quotation closing after "mutter". This is the Editor's recommendation. Post-review, its basis is ASV and KJV only; JPS 1917 does not support this punctuation.
- (B) NJPS construal: "… that chirp and mutter; for a people may inquire of its divine beings, of the dead on behalf of the living, for teaching and testimony." 8:20b would follow as the prophet's verdict, and 8:21 would read "his/their divine beings".
- (C) Keep (A), but render 8:21 lower case.

**Why escalating:** the Hebrew allows both readings, and this site decides whether *ʾĕlōhîm* is translated as "God" or as the spirits of the dead. That touches the project's word.
Under (B) the following would change:
- the lines of 8:19, 8:20 and 8:21;
- the punctuation of 8:20;
- the conditional clause in the `elohim-el-eloah-monotheistic-formula-isaiah` rationaleAppend.

### `ISA-8:22` against `ISA-5:30` — consistency

**Issue:** wave I-1 (pending sign-off) renders 5:30 *wᵉnibbaṭ lāʾāreṣ* "if one looks to the land". 8:22 now has "the earth" because of the explicit above/below contrast.

**Options considered:**
- (A) Leave the two verses different, and say why in the `eretz` rationaleAppend. This is the recommendation.
- (B) Align 5:30 to "earth".
- (C) Revert 8:22 to "land".

**Why escalating:** 5:30 is in a signed-off-pending wave I-1 chapter that this Editor may not touch.

### `ob-yiddeoni-ghosts-familiar-spirits-isaiah` against `ariel-ob-isaiah-29` — one lemma, two entries

**Issue:** *ʾôḇ* is rendered "ghost" under two entries: the new one (8:19) and `ariel-ob-isaiah-29` (29:4).

**Recommendation:**
- Move ISA-29:4 into the new entry and trim `ariel-ob-isaiah-29` to the Ariel sites. This modifies a ratified entry, so it needed sign-off (given 2026-11-26).
- Promote the new entry to central when Lev 19–20, Deut 18 or 1 Sam 28 is translated. Central v2.93.0 has no entry for *ʾôḇ* or *yiddᵉʿōnî*. I searched ids, sources, wohChoice, rationale and the appliesTo of the necromancy verses.

### Wave rulings followed, with the dissenting evidence on record

- **8:8 "O Immanuel"** follows ruling 1, with ASV, KJV and JPS 1917 (verified). The Translator's note listed NJPS among the vocative readings. That is wrong: NJPS reads a clause, "But with us is God, whose wings are spread", and makes the wings God's (verified). The commentary records this. It is not escalated, because the ruling stands and the vocative is well attested.
- **8:7–8 pronouns:** the draft's "he … his" is kept. The Translator's note attributed it to ASV, but ASV reads "it … its" (verified). The basis is now KJV and JPS 1917 (verified). The commentary and `lexical-cruxes-isaiah-8` are corrected.

---

## Resolution of the 20 editorial questions

| # | refId | Resolution | Governing entry |
|---|---|---|---|
| 1 | 8:1 | ASV "large tablet … with the pen of a man" kept; "in common script" in commentary | `lexical-cruxes-isaiah-8` |
| 2 | 8:1, 3 | Name transliterated, *lᵉ-* "For" | `sign-names-isaiah-7-8` (modify) |
| 3 | 8:2 | MT cohortative kept; imperative variant reported | `mt-qere-textual-policy-isaiah` |
| 4 | 8:6 | MT "rejoices in" kept; *ûmāsôs* reported | `mt-qere-textual-policy-isaiah` |
| 5 | 8:7 | "he … his" kept (KJV, JPS 1917); "glory" by concordance | `lexical-cruxes-isaiah-8` |
| 6 | 8:8 | "O Immanuel" (ruling 1) | `sign-names-isaiah-7-8` |
| 7 | 8:9 | "Make an uproar … be shattered"; "earth" | `lexical-cruxes-isaiah-8`, `eretz-cosmic-scope-isaiah-24` |
| 8 | 8:10 | "for God is with us" (ruling 1) | `sign-names-isaiah-7-8`, `elohim-el-eloah-…` |
| 9 | 8:11 | "with a strong hand, and instructed me" | `lexical-cruxes-isaiah-8`, `mt-qere-…` |
| 10 | 8:12 | MT "conspiracy"; *qōdeš* conjecture reported | `mt-qere-…` |
| 11 | 8:14 | MT "sanctuary"; conjectures reported; NT use noted | `mt-qere-…` |
| 12 | 8:16 | "testimony" (also 8:20); "teaching"; "my" lower case | `lexical-cruxes-isaiah-8`, `torah-teaching-isaiah` |
| 13 | 8:18 | "signs and wonders" (as Deut 4:34); portent sense in commentary | `lexical-cruxes-isaiah-8` |
| 14 | 8:19 | "the ghosts and the familiar spirits" (line changed) | `ob-yiddeoni-ghosts-familiar-spirits-isaiah` (new) |
| 15 | 8:19 | "their God" kept; escalated above | `elohim-el-eloah-…` |
| 16 | 8:20 | exclamation; "dawn"; "for them" | `lexical-cruxes-isaiah-8`, `torah-teaching-isaiah` |
| 17 | 8:21 | plural "they … their"; "curse by" | `lexical-cruxes-isaiah-8` |
| 18 | 8:22 | "the earth" (line changed); "driven away" | central `eretz`, `lexical-cruxes-isaiah-8` |
| 19 | 8:23 | "But there shall be no gloom" | `lexical-cruxes-isaiah-8`, `mt-qere-…` |
| 20 | 8:23 | ASV reversal "made it glorious"; JPS 1917 / Emerton and NJPS readings in commentary | `lexical-cruxes-isaiah-8` |

---

## Glossary changes for review

### Central glossary (`wave-i3-ch8-central-diff.json`, propose 2.95.0)

- Modified: `eretz`. appliesTo gains ISA-8:8, 8:22, 8:23. A rationaleAppend explains the 8:22 above/below use; claim_type is unchanged.
- Modified: `shakhan-dwell-divine-presence-verb-cross-corpus`. appliesTo gains ISA-8:18.
- Recorded but not extended:
  - `sealed-book-dan-12-…` at 8:16
  - `elohim-imkha-divine-presence-formula` at 8:8 and 8:10
  - `elohim-as-translation`
  - `nichesh-laban-divination`
  - `onen-soothsayer-cross-corpus`

### Per-translation overlay (`wave-i3-ch8-overlay-diff.json`, propose 1.8.0)

- Added: `ob-yiddeoni-ghosts-familiar-spirits-isaiah` (claim_type: `direct`)
- Added: `lexical-cruxes-isaiah-8` (claim_type: `direct`). It may be folded into a wave-level crux entry.
- Modified, appliesTo only, plus rationaleAppend where given:
  - `sign-names-isaiah-7-8` (+8:1, 8:3, 8:8, 8:10; apply after the chapter 7 add)
  - `title-and-meta-conventions-isaiah` (+8:1)
  - `adonai-standalone-title-isaiah` (+8:7)
  - `yhwh-tzevaot-hosts-isaiah` (+8:13, 8:18)
  - `elohim-el-eloah-monotheistic-formula-isaiah` (+8:10, 8:19, 8:21; conditional append)
  - `torah-teaching-isaiah` (+8:16, 8:20)
  - `eretz-cosmic-scope-isaiah-24` (+8:9)
  - `mt-qere-textual-policy-isaiah` (+8:2, 8:6, 8:11, 8:12, 8:14, 8:23)
- Not applied: `kevodo-kavod-suffixed-isaiah` at 8:7, `sefer-sealed-scroll-isaiah-29` at 8:16, `ariel-ob-isaiah-29` at 8:19.

---

## Verification

- **Verified:**
  - ASV 1901, Isa 8:1–23 (bible-api.com, ASV text);
  - KJV Isa 8:6–8;
  - JPS 1917 and NJPS ("Tanakh: The Holy Scriptures, published by JPS"), Isa 8:1–23, on Sefaria. This includes NJPS footnotes: 8:1 "meaning uncertain", 8:12 and 8:14 emendations, 8:19 "shades of the dead", 8:23 "So 1QIsa".
- **Not verified**, and marked so in commentary:
  - every NRSV wording;
  - Septuagint readings (8:8 *meth' hēmōn ho theos*, 8:9 *gnōte*);
  - the 1QIsaᵃ readings at 8:2 and 8:11;
  - Emerton's conclusion on 8:23 (the bibliographic details, *JSS* 14 [1969] 151–175, were verified via Crossref post-review);
  - Strong's numbers in both new entries.
- **Corrected attributions from the draft:**
  - ASV 8:7–8 ("it … its", not "he … his");
  - NJPS 8:8 (a clause, not "O Immanuel");
  - NRSV 8:19 (reported to continue the quotation with "their gods", not to read "their God").

---

## Post-review corrections (2026-11-26)

These follow the Reviewer's report (status `awaiting-human`). No English line was changed. `translation.status`, the reviewerReport block and both shared glossaries are untouched.

1. **8:16, note revised.** The note no longer argues from the lower-case "my", since house style lower-cases all divine pronouns. It now says that v 16 is the prophet's because the line closes YHWH's speech at the end of v 15; this is the Reviewer's wording. The 8:16 item in `lexical-cruxes-isaiah-8` (overlay diff) is aligned.
2. **8:19, JPS 1917 attribution corrected.** The change is made in the note, in this report and in the `elohim-el-eloah-monotheistic-formula-isaiah` rationaleAppend. JPS 1917 opens the quotation before "Seek" and closes it after "for instruction and for testimony?" (v 20), so it reads 19b–20a as the advisers' words while printing "God". Construal (A), kept in the line, rests on ASV and KJV. JPS 1917 and NJPS both continue the quotation. The 8:20 note now ties the JPS 1917 / NJPS attachment to that continued quotation.
3. **8:19b–21, alternate (B) staged** (withdrawn 2026-11-26: the founder kept reading A; see the final section). The (B) wording was staged in the wohChoice of `lexical-cruxes-isaiah-8`, marked "PENDING FOUNDER RULING". It continues the quotation to 8:20a, with "its divine beings" at 8:19 and "their divine beings" at 8:21. If (B) is ruled, the 8:20 exclamation item lapses and ISA-8:19 and 8:21 leave `elohim-el-eloah-monotheistic-formula-isaiah`. A sentence noting the contingency was appended to the entry's rationale.
4. **8:23, Emerton.** Crossref confirms the bibliographic record: J. A. Emerton, "Some Linguistic and Historical Problems in Isaiah VIII. 23", *JSS* 14 (1969) 151–175 (doi:10.1093/jss/14.2.151). His conclusion could not be checked. The note and the crux-entry rationale therefore no longer say he argued the JPS 1917 judgment reading; they say the construal is "discussed" there, conclusion not checked.
5. **8:22, cross-reference added** (optional item): "Contrast 5:30 'the land', where no upward/downward pairing is present."

Not acted on: the Reviewer's minor remark that 29:4 renders *ṣpṣp* "whisper" while 8:19 has "chirp". Changing either would mean changing an English line. It is left for the orchestrator or a later pass.

## Founder rulings applied (2026-11-26)

The founder signed off wave I-3 with every recommended default ("Sign-off ok", 2026-11-26; `wave-i3-signoff-package.md`), together with wave I-1 decisions 1 and 2. `translation.status` and the `reviewerReport` block are unchanged. Statements above marked pending or provisional are settled as follows.

- **8:19b–21:** reading A, the prophet's reply, stands. The staged (B) wording was removed from the `lexical-cruxes-isaiah-8` wohChoice and replaced by one sentence recording A as kept and B as reported in commentary. The rationale's post-review sentence and the `elohim-el-eloah-monotheistic-formula-isaiah` rationaleAppend and note no longer describe the choice as escalated. The 8:19 note's "listed for review in the editor's report" now reads "the JPS 1917 and NJPS construal is the alternative reported above". Lines are unchanged.
- **ʾôḇ consolidation:** ISA-29:4 is added to `ob-yiddeoni-ghosts-familiar-spirits-isaiah` (source, translit, wohChoice, rationale, appliesTo), which now notes that 29:4 renders ṣpṣp "whisper" against 8:19 "chirp". `ariel-ob-isaiah-29` is trimmed to 29:1, 2, 7 through `wave-i3-orchestrator-ops.json` overlay.set. The 29:4 glossaryRef is added through refsAdd, and chapter 29 is in extraChapters. The stale `ariel-ob-isaiah-29` ref at 29:4 is left for a chapter-29 Editor pass.
- **8:22 against 5:30** (above) was not part of the sign-off decisions and stays as recommended option A.
