# Chapter 37 Editor Report

Isaiah 37 (38 verses), wave I-6 (Isa 36–39, 41).
Editor: claude-opus-5-5 (editor), 2026-11-27.
Base: central glossary v5.0.0 and isaiah-woh overlay v4.0.0, both read-only, with `wave-i6-rulings.md` in force.
All glossary changes are in `wave-i6-ch37-overlay-diff.json` (proposes 4.1.0) and `wave-i6-ch37-central-diff.json` (proposes 5.1.0).

## Summary

- **Editorial questions:** all 26 are resolved and `editorial_questions[]` is empty. Two of them are escalated below as decisions for the founder: 37:16 and 37:36.
- **English-line changes:** three verses change. Each change is backed by the new overlay entry `lexical-cruxes-isaiah-37`.
  - 37:16: "who sits enthroned above the cherubim" → "who is enthroned on the cherubim". This matches the stable 2 Sam 6:2 and central `cherubim-ezek`. It departs from the wording given in rule 3 and is escalated.
  - 37:24: "to the innermost parts of Lebanon" → "to the far reaches of Lebanon". This matches 14:13 and 14:15 *yarkᵉṯê*.
  - 37:36: "when they arose early in the morning" → "when people arose early in the morning". The subject is supplied, as ASV and JPS 1917 supply "men", so that the clause cannot be read as the dead rising.
- **Commentary:** 33 of the 38 verses have `notes.official`. Every verse with a 2 Kgs 19 difference of substance records it. No note was written for 37:1, 5, 28, 33 or 37 (identical or trivial in Kings, and no crux). One note (37:36) ends with a separately headed reception paragraph labelled speculative.
- **Status:** `editor-review`, `1.0.0-rc1`, and "claude-opus-5-5 (editor)" is added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 5.0.0 and 4.0.0; the orchestrator sets them on merge. No paragraph `translit` was added.
- **Lens audit:** no English line carries a project reading. The canon in data-library (TBWTT) does not cite Isa 37 or 2 Kgs 19. The 37:12 Eden/Bit-Adini point appears in commentary only, with no lens. The 37:36 speculative note rests on TBWTT 3:72–73, which identifies the *malʾaḵ YHWH* of Judg 6:21 as "one of the creators", and on 3:75, which explains the rout of the camp in Judg 7 by technical means. The note says plainly that the canon does not cite this verse.
- **Verification (2026-11-27):**
  - ASV of Isa 37 through bible-api.com.
  - JPS 1917 and NJPS of Isa 37 through the Sefaria API v3. NJPS is "Tanakh: The Holy Scriptures, published by JPS", not the Gender-Sensitive Edition. Its footnotes at 37:3, 7, 12, 18, 20, 24, 25, 27, 30 and 36 were read.
  - The MT of 2 Kgs 19 (Tanach with Ta'amei Hamikra), aligned verse by verse with Isa 37 through the Sefaria API v3.
  - MT cross-references checked: Deut 5:23; 1 Sam 4:4; 17:26; Jer 10:10; Amos 1:5; 6:1; Ezek 27:23; Gen 2:8; Ps 80:2; 99:1; 123:4; Exod 25:22; 1 Kgs 22:22; Isa 4:2; 9:6; 10:20; 14:8, 13, 32; 16:8; 18:2; 20:5; 22:15; 31:3, 5; 32:18; 33:4, 20; 36:19; 39:1; 45:18.
  - ASV of Amos 6:1 and Ps 123:4.
  - Not verified, and labelled so in the commentary: lexica, 1QIsaᵃ, NRSV, LXX, and the Assyriological and Egyptological identifications (Bit-Adini, Taharqa, Urartu, Nisroch).
- **Translator claim corrected:** the draft's 37:2 question gave NJPS as "the secretary". NJPS 37:2 reads "Shebna, the scribe", so all three versions agree on "the scribe".

## Speculative entries requiring sign-off

No speculative glossary entry is proposed. The new entry and every extension are `claim_type: direct`.

One commentary paragraph is labelled speculative (a reception note, which founder policy keeps):

### ISA-37:36 reception note (*malʾaḵ YHWH*)

**Source:** מַלְאַךְ יְהוָה *malʾaḵ YHWH*
**WoH reading (commentary only):** the messenger who strikes the Assyrian camp read as an envoy of the Elohim acting by technical means.
**Why speculative:** the canon does not cite Isa 37:36 or 2 Kgs 19:35. The note carries over two canon readings of other passages: TBWTT 3:72–73, where the *malʾaḵ YHWH* of Judg 6:21 is "one of the creators", and TBWTT 3:75, where the Judg 7 camp is routed by amplified sound. The premise is in the canon. The application to this verse is the project's, and the note says so.
**Recommendation:** ship as a labelled reception note, or drop it if the founder prefers no reception note on a mass-casualty verse.

---

## Decisions for the founder

### ISA-37:16: *yōšēḇ hakkᵉrūḇîm* "who is enthroned on the cherubim" (departs from rule 3 wording)

**Issue:** rule 3 gives "who sits enthroned above the cherubim". The corpus already prints "who is enthroned on the cherubim" for the same fixed title at the stable 2 Sam 6:2 (2-samuel-woh overlay `yoshev-hakkeruvim-enthroned-on-the-cherubim-2-samuel-6-2`), and central `cherubim-ezek` lists 2SA-WOH-6:2.
**Evidence (checked):**
- The Hebrew has no preposition.
- ASV prints "[above]" in brackets, as a supplied word. JPS 1917 has "sittest upon" and NJPS "enthroned on the Cherubim".
- The same title occurs at 1 Sam 4:4, Ps 80:2, 99:1 and the parallel 2 Kgs 19:15.
- Exod 25:22 (*mēʿal hakkappōreṯ mibbên šᵉnê hakkᵉrūḇîm*) is the basis for "above". It is reported in commentary.

**Decision taken in the line:** "who is enthroned on the cherubim", so that the title has one English form in the corpus. The central diff extends `cherubim-ezek` to ISA-37:16 and recommends the same wording for 1 Sam 4:4, Ps 80:2, 99:1 and 2 Kgs 19:15.
**Options:**
- (A) Accept. This is the recommendation.
- (B) Revert to rule 3's "who sits enthroned above the cherubim". That leaves Isaiah and 2 Samuel with different English for one title, so the 2 Samuel wording would also have to be revisited.

### ISA-37:36: *malʾaḵ YHWH* "the messenger of YHWH" (rule 3 asks for escalation)

**Issue:** `lexical-cruxes-isaiah-33` left 37:36 open. Central `malakh-yhwh-messenger` already lists ISA-37:36 and 2KGS-19:35 with "messenger of YHWH".
**Evidence (checked):** ASV and JPS 1917 have "the angel", and NJPS "an angel". Isaiah renders *malʾāḵ* as "messenger" at 14:32, 18:2, 33:7, and in this chapter at 37:9 and 37:14, where they are Sennacherib's messengers.
**Decision taken in the line:** keep the central entry. I found no strong reason to depart from it. Keeping it keeps one noun through the book, and the entry's rationale already explains that the rendering takes no side on what kind of being is meant. The decision is recorded in `lexical-cruxes-isaiah-37`, with a rationale addendum on the central entry (empty appliesToAdded).
**Options:**
- (A) Ship "the messenger of YHWH". This is the recommendation.
- (B) "the angel of YHWH" with ASV. That needs a context clause on the central entry, and 63:9 would also have to be revisited.

---

## Unresolved editorial questions

None. Lower-level calls the Reviewer may wish to check:

### `ISA-37:17`

**Issue:** *ʿênᵉḵā* is written without the yod of the plural, where Kings has *ʿênêḵā*. NJPS reads a singular, "open Your eye", which matches the singular "your ear" earlier in the verse.
**Options considered:** "your eyes" (ASV, JPS 1917, defective plural); "your eye" (NJPS).
**Resolution:** the line keeps "eyes", because the segol vowel under the nun points to the defective plural. The Reviewer may prefer the NJPS singular.

### `ISA-37:2` (resolved by coordination)

**Issue:** "who was over the house" applies the 22:15 wording.
**Resolution:** the chapter 36 Editor extended `lexical-cruxes-isaiah-22` to 36:3 and 36:22. On the coordinator's instruction, this diff extends that entry to ISA-37:2 and cites it there. ISA-37:2 is not part of `lexical-cruxes-isaiah-37`.

---

## Glossary changes for review

### Central glossary (`wave-i6-ch37-central-diff.json`, 5.0.0 → 5.1.0, minor)

- Modified: `malakh-yhwh-messenger`: rationale addendum only. ISA-37:36 is already listed, and the decision is recorded there.
- Modified: `cherubim-ezek`: + ISA-37:16 ("who is enthroned on the cherubim", the 2 Sam 6:2 wording).
- Modified: `cherem-devote-to-destruction-cross-corpus`: + ISA-37:11.
- Modified: `shamayim`: + ISA-37:16 ("the skies and the earth").
- Modified: `yeor-nile-egyptian-loanword`: + ISA-37:25 ("all the rivers of Egypt", Isaiah clause).
- Modified: `yatsar`: + ISA-37:26 (the site the entry's rationale already names).
- Modified: `she-erit-remnant-cross-corpus-theological-keyword`: + ISA-37:4, 37:32.
- Deliberately not extended:
  - `pleitah-deliverance-escape-remnant-tradition-cross-corpus` at 37:31–32. Its wohChoice is the Gen 45:7 "deliverance", and it is cited, as at 4:2.
  - `harei-ararat` at 37:38.

### Per-translation overlay (`wave-i6-ch37-overlay-diff.json`, 4.0.0 → 4.1.0, minor)

- Added: `lexical-cruxes-isaiah-37` (claim_type: `direct`). It covers 21 verses and backs the three line changes.
- Modified (appliesTo extensions with rationale addenda; no wohChoice changed):
  - `lexical-cruxes-isaiah-22` (+37:2, "who was over the house"; per coordinator, following the chapter 36 extension to 36:3, 22).
  - `rabshakeh-title-isaiah` (+37:4, 37:8). **Depends on the chapter 36 Editor's add op**, which must be applied first.
  - `cush-names-isaiah` (+37:9). The entry's "expected site" sentence may now be dropped.
  - `mt-qere-textual-policy-isaiah` (+37:17, 18, 20, 25, 27, 30). The orchestrator should add "37:30" to the qere list in wohChoice.
  - `elohim-el-eloah-monotheistic-formula-isaiah` (+37:4, 12, 16, 17, 19, 38).
  - `elohai-elohenu-doxology-isaiah-25` (+37:4, 10, 20).
  - `elohei-yisrael-god-of-israel-isaiah-24` (+37:16, 21).
  - `yhwh-tzevaot-hosts-isaiah` (+37:16, 32).
  - `eretz-cosmic-scope-isaiah-24` (+37:16, 20).
  - `adonai-standalone-title-isaiah` (+37:24).
  - `adam-humankind-ish-man-isaiah` (+37:19).
  - `ruach-divine-spirit-lower-case-isaiah` (+37:7).
  - `title-and-meta-conventions-isaiah` (15 sites; the Translator's title is kept).
- Cited in glossaryRefs, not extended, because they bind only their own sites:
  - `lexical-cruxes-isaiah-4`, `-20`, `-31`, `-33`
  - `helel-zaphon-elyon-taunt-isaiah-14`
  - `sefer-sealed-scroll-isaiah-29`

## Post-review corrections (2026-11-27)

These are commentary-only corrections made after the Reviewer's pass, on the coordinator's instruction. `translation.status` (awaiting-human), the reviewerReport block, every English line and both shared glossaries are unchanged. The added Kings readings were checked against the MT of 2 Kgs 19 on Sefaria (Tanach with Ta'amei Hamikra).

1. **ISA-37:4:** deleted "although the words are reported from the Assyrian side". The note now says the words are Hezekiah's own message to Isaiah, describing the purpose of the Rabshakeh's mission.
2. **ISA-37:24:** "2 Kgs 19:23 differs in four places" → "five places". Added the cohortative *wᵉʾāḇôʾāh* (Kings) against Isaiah's *wᵉʾāḇôʾ*.
3. **ISA-37:7 (optional item):** added 2 Kgs 19:7 *lᵉʾarṣô* against Isaiah's *ʾel-ʾarṣô*, with no difference of sense.
4. **ISA-37:27 (optional item):** added 2 Kgs 19:26 *wayyēḇōšû* against Isaiah's *wāḇōšû*.
5. **ISA-37:36 (optional item):** added 2 Kgs 19:35 *wayyaḵ* against Isaiah's *wayyakkeh*, and the absence of *waw* before *šᵉmōnîm* in Kings.
