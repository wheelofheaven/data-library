# Isaiah wave I2 Editor Report

Chapters: Isa 13, 14, 15, 29, 32, 40, 42, 43, 44, 45, 48, 54, 65 (308 verses).
Program: canon-cited chapters (every biblical chapter cited in Raël's first three books, translated as whole chapters).
Editor: claude-opus-5-5 (editor), 2026-11-01.
Base: central glossary v2.83.0 (read-only); isaiah-woh overlay v1.5.0 → **v1.6.0** (applied).

## Summary

- **Editorial questions:** all 90 resolved. 89 are folded into glossary entries or commentary, and one is escalated (bārāʾ, below). `editorial_questions[]` is empty in all 13 files.
- **English-line changes:** 35 verses, each backed by a glossary entry (listed below). Chapter titles adjusted where a ruling changed a word: 13, 15 ("oracle"), 29 ("scroll"), 43, 45, 48 ("create").
- **Commentary:** 148 verses now have `notes.official`, including 20 separately headed reception notes ("**Wheel of Heaven reading (reception note, not a translation claim).**") at the canon-cited verses: 13:5, 14:13, 14:14, 14:17, 15:8, 29:12, 29:20, 32:3, 32:6, 40:21, 42:1, 42:3, 43:5, 43:8, 43:10, 44:19, 45:9, 48:10, 54:7, 65:20. Each reception note reports what the canon says and how the line handles the verse; none of them argues the reading.
- **Overlay:** 13 new entries, 14 existing entries extended (appliesTo plus one appended rationale sentence each; no shipped wohChoice reversed). Version 1.5.0 → 1.6.0 (minor).
- **Central:** `wave-i2-central-diff.json` contains 20 appliesTo-only modify ops with complete arrays plus `appliesToAdded`, and no new entries. Recommended version **2.84.0**; renumber if the parallel Torah or Former-Prophets diff, also based on 2.83.0, is merged first.
- **Status:** all 13 chapters are at `editor-review`, `1.0.0-rc1`, `glossaryVersion` 2.84.0 (pending), `overlayGlossaryVersion` 1.6.0, with "claude-opus-5-5 (editor)" added to `modelDrafts`.
- **Lens audit:** no English line carries a project reading. Two Translator choices that leaned toward craft language were removed: bārāʾ "shape" (→ "create") and 45:18 "chaos". Three places where the canon's wording differs from the line were deliberately left at the standard reading, with the canon's wording reported in the apparatus: 40:21 (object reading), 44:19 (statements), 43:13 ("aujourd'hui aussi").

---

## Speculative entries requiring sign-off

None. Of the 13 new overlay entries, 12 are `direct` and 1 is `inferred` (`torah-teaching-isaiah`). The project lens appears only in the 20 reception notes, which make no translation claim.

---

## Founder decisions

### F1. bārāʾ: "create" in Isaiah, with the Genesis "shape" not extended (`bara-create-isaiah`)

**Source:** בָּרָא bārāʾ (Qal, participle bôrēʾ, Niphal niḇrāʾ) at 40:26, 28; 42:5; 43:1, 7, 15; 45:7, 8, 12, 18; 48:7; 54:16; 65:17, 18.
**Draft:** applied the central `bara` entry ("shape", `inferred`, scoped to Gen 1:1, 21, 27), giving "who shaped these?", "I am shaping new skies", and so on.
**Editor ruling:** "create" / "Creator" throughout Isaiah (ASV, NRSV, NJPS). The central entry is not extended.
**Why:**
1. **Range of objects.** In Isaiah, bārāʾ takes darkness and calamity (45:7), righteousness (45:8), new historical events (48:7), the smith and the destroyer (54:16), and Jerusalem "as a rejoicing" (65:18). None of these is a material that could be "shaped." Stuhlmueller (*Creative Redemption in Deutero-Isaiah*, 1970), Westermann (OTL 1969), Blenkinsopp (AB 19A, 2002) and the lexica (Bernhardt, TDOT 2; Schmidt, THAT 1) all describe the verb as sovereign, effortless bringing-about, with no material and no tool.
2. **"Create" keeps the verbs apart.** Isaiah pairs bārāʾ with yāṣar, the potter's verb (43:1, 7; 45:7, 18). English "shape" and "form" are near-synonyms in the same craft register, so the Hebrew contrast would disappear in translation.
3. **Lens risk.** "Shaping humankind" or "shaping new skies" reads as manufacture. That is a workshop reading the Hebrew of these verses does not support, so Rule 1 excludes it.
4. **The ex nihilo question stays open.** "Create" does not settle whether creation is from nothing, which Second Isaiah does not discuss (Westermann).

The canon itself quotes 43:7 as « créés, formés et faits », the standard triad.
**Founder question:** (a) Ratify "create" for Isaiah. (b) Separately, decide whether the Isaiah evidence should prompt a review of the Genesis "shape" decision. That decision is `inferred`, and its rationale rests partly on a Piel "cut out, fashion" that HALOT assigns to a separate homonym (brʾ II). The Editor did not touch the central `bara` entry.
**Recommendation:** ship "create" for Isaiah; put the Genesis review on the agenda for the next Genesis pass.

### F2. šāmayim at 65:17: "new skies and a new earth"

**Ruling:** the register rule ratified at the Kings wave-A sign-off, applied book-wide:
- "skies" for the physical and created sky: the horizon idiom of 13:5, 13:10, 13:13, 45:8 (rain), and the measured and stretched-out skies of the creation hymns (40:12, 22; 42:5; 44:23, 24; 45:12, 18; 48:13);
- "the heavens" for the divine-council realm of 14:12–13.

65:17 is the Gen 1:1 merism for the whole created order: the same verb and the same pair, rendered "the skies and the earth" at Gen 1:1. It is not YHWH's dwelling; compare 66:1, "the heavens are my throne." The line therefore reads "new skies and a new earth." The reception form "new heavens" (2 Pet 3:13; Rev 21:1, where revelation-woh renders "a new heaven" from the Greek singular) is recorded in commentary.
**Founder question:** accept "skies" (consistent with Gen 1:1), or make 65:17 an exception for reception continuity with Rev 21:1.
**Recommendation:** ship "skies".

### F3. hûʾ hā-ʾĕlōhîm "he is God" (45:18) vs 1 Kgs 18:39 "YHWH, he is the Elohim"

Isaiah renders ʾĕlōhîm "God" in every form, as the brief requested (`elohim-el-eloah-monotheistic-formula-isaiah`). The articular predicate of 45:18 is the same Deuteronomic identification formula that 1-kings-woh renders "he is the Elohim."
**Founder question:** live with the book-specific difference (the Isaiah practice was ratified at chs. 24–27 and 53), or harmonize one way in a later pass.
**Recommendation:** keep the Isaiah practice for this wave and record the divergence.

### F4. Divine rûaḥ: lower-case "spirit" in Isaiah vs "ruach" in Kings and Ezekiel

**Ruling:** lower-case "spirit" at 32:15, 40:13, 42:1, 44:3, 48:16 (NRSV, NJPS); "breath" at 40:7; human "spirit" at 42:5. No capital "Spirit."
Transliteration was declined. Kings and Ezekiel keep "ruach" where the rûaḥ acts as an agent that lifts or carries a prophet, and the wind/spirit ambiguity carries the narrative. Isaiah's poetry of endowment and outpouring does not need it.
**Consequence to note:** Isa 44:3 "I will pour my spirit" and Ezek 39:29 "my ruach" (the Ezekiel overlay's endowment clause) now differ.
**Founder question:** accept the genre-based split, or harmonize outpouring and endowment sites across books.
**Recommendation:** accept for now.

---

## Rulings on the brief's points

1. **bārāʾ:** see F1.
2. **šāmayim:** see F2. 13:5 "from the end of the skies" uses the horizon idiom (Deut 4:32; 30:4), physical register; ASV's singular "heaven" is adjusted. 40:12 and 40:22 are in the creation register, "skies". 14:12–13 are in the divine-realm register, "the heavens".
3. **ʾĕlōhîm / ʾēl / ʾĕlôah:** "God" consistently, at 13:19; 40:18; 42:5; 43:12; 44:6, 8; 45:5, 14, 15, 18, 21, 22. Lower-case "a god / gods" applies only where the word denotes an idol (42:17; 44:10, 15, 17; 45:20) and at 43:10 ("no god was formed"; nôṣar belongs to idol-making vocabulary, as in NRSV and NJPS). **44:8 changed** from "an Eloah" to "a God". ʾĕlôah is one of three synonyms in a single formula, so transliterating it alone would mark a distinction the text does not make. The central `shaddai-eloah` entry is extended only to the name **Shaddai at 13:6** (NJPS precedent; keeps the šōḏ/šadday pun).
4. **Divine rûaḥ:** see F4.
5. **The smaller items:**
   - **tōhû:** "emptiness" at 29:21; 40:17, 23; 44:9; "in vain" at 45:19. At **45:18, "a wasteland"** replaces the draft's "as chaos". The verse echoes Gen 1:2, which the central `tohu-vavohu` entry renders "wasteland and emptiness", and its antithesis is "to be inhabited" (ASV and NJPS "a waste"; Blenkinsopp). "The city of chaos" stays at 24:10 only (`tohu-bare-emptiness-wasteland-isaiah`).
   - **Potter (one ruling for 29:16, 45:9, 64:7):** "the potter" only for the free-standing hay-yôṣēr (29:16). The suffixed yōṣᵉrô is "the one who formed him / forms it" (29:16b; 45:9 ×2; 45:11) under central `yatsar` (`yotser-potter-clay-image-isaiah`).
   - **tôrāh:** "teaching" at 42:4, 21, 24 (NJPS; NRSV at 42:4, 21), consistent with "the teachings" at 24:5 (`torah-teaching-isaiah`, `inferred`). This changes three lines from ASV "law".
   - **14:12–14:** "O day star, son of the dawn" (common nouns; "Lucifer" and "Helel son of Shahar" go in commentary); "the stars of God"; "the mount of assembly"; **"in the far reaches of Zaphon"** (NRSV, NJPS; changed from "of the north"), keeping "far reaches" in both v13 and v15 so the mirror stays visible; "the Most High" (`helel-zaphon-elyon-taunt-isaiah-14`; central sapunu entry extended).
   - **45:7:** "who makes **well-being** and creates **calamity**" (NRSV and NJPS "weal … woe"; ESV). The antithesis with šālôm is non-moral. ASV "evil" and the Yotzer-blessing theodicy history are in commentary (`ra-calamity-shalom-well-being-isaiah-45-7`).
   - **Shaddai / Eloah:** see point 3.
   - **Quotation convention:** confirmed. "Thus says YHWH" introduces divine speech without quotation marks throughout the wave. Embedded speech keeps its marks: 14:4–21 taunt, 40:3, 6, 45:14, and the YHWH-to-the-directions command of 43:6–7. Recorded in `title-and-meta-conventions-isaiah`.
6. **Textual policy (`mt-qere-textual-policy-isaiah`):** MT and the qere stand in the line; the ketiv, the 1QIsaᵃ readings and the versions are in commentary.
   - The source marks 12 bracketed ketiv/qere pairs: 13:16, 29:11, 32:7, 32:15, 42:20, 42:24, 44:17, 44:24, 45:2, 54:16, 65:4, 65:7. The brief's figure of 13 presumably includes the puncta extraordinaria of 44:9; the Editor found no thirteenth bracketed pair.
   - **13:16:** the qere euphemism is rendered by its sense, **"ravished"**. The draft's "lain with" made the violence sound consensual.
   - **32:7:** qere "the poor" (the canon's French follows the same reading).
   - **44:24:** qere "by myself"; the ketiv "who was with me?" is in commentary.
   - **44:9:** dotted הֵמָּה kept in the source and translated.
   - 1QIsaᵃ and versional variants are reported, not adopted: 14:4, 14:30, 15:9, 40:6, 43:19, 45:2, 45:8, 48:1, 48:10, 48:11, 54:9, 54:13.

---

## Unresolved editorial questions

### `ISA-40:26` (and all bārāʾ sites)

**Issue:** whether the Genesis-scoped "shape" governs Isaiah.
**Options considered:** A, "shape" (draft); B, "create" (adopted); C, "fashion".
**Why escalating:** this is a cross-corpus lexical policy that could reopen a ratified Genesis decision. See F1.

No other question is left open. F2–F4 are rulings the Editor made and flags for confirmation; they are not unresolved.

---

## Disposition of the 90 Translator questions

- **Kept as drafted, with a commentary note (66):**
  - Q2 13:5 skies
  - Q4 Shaddai
  - Q5 constellations
  - Q7 13:19 God
  - Q8 wild goats
  - Q9 strongholds
  - Q11 day star
  - Q12 heavens
  - Q14 Most High
  - Q15 fiery flying serpent (seraphim entry extended with a context rule)
  - Q16 MT
  - Q17 undone
  - Q19 nobles / Eglath-shelishiyah
  - Q20 Dimon
  - Q21 Ariel
  - Q22 MT
  - Q24 visited
  - Q26 potter ruling (no line change; book-level entry)
  - Q27 emptiness
  - Q29 qere
  - Q30 a spirit / qere
  - Q31 God
  - Q33 ASV herald
  - Q34 skies
  - Q35 directed / spirit
  - Q36 emptiness
  - Q37 God
  - Q39 "from the foundations" (ASV; the object reading the canon uses is recorded)
  - Q40 circle
  - Q42 servant / spirit
  - Q44 God, YHWH
  - Q45 keep
  - Q46 ASV
  - Q47 qere
  - Q48 qere / MT person-shift
  - Q50 Cush
  - Q52 no god / I am he
  - Q53 ASV
  - Q54 ASV
  - Q55 MT
  - Q57 spirit
  - Q58 on his hand
  - Q59 God
  - Q61 dots
  - Q62 qere
  - Q63 questions
  - Q64 qere
  - Q65 MT
  - Q66 God / a god
  - Q69 yatsar
  - Q70 MT
  - Q72 MT
  - Q74 chosen
  - Q75 MT
  - Q76 ASV order
  - Q77 singular
  - Q78 MT
  - Q80 MT
  - Q81 ASV
  - Q83 MT / Here am I
  - Q84 qere
  - Q85 ASV
  - Q86 qere / former work
  - Q87 Fortune / Destiny
  - Q88 God of truth
  - Q90 sinner
- **Changed (24):**
  - Q1 burden → oracle (13:1; 14:28; 15:1)
  - Q3 13:9 land → earth
  - Q6 13:16 ravished
  - Q10 parable → taunt (madhēḇāh MT kept)
  - Q13 north → Zaphon
  - Q18 Bayith → the temple
  - Q23 familiar spirit → ghost
  - Q25 book → scroll (29:11, 12, 18; qere and literal idiom kept)
  - Q28 dim → smeared over (the 6:10 reversal)
  - Q32 goodliness → constancy (MT "he said" kept)
  - Q38 impoverished → sissoo wood (musukkannu)
  - Q41, Q49, Q51, Q73, Q82, Q89 bārāʾ → create
  - Q43 law → teaching
  - Q56 curse → the ban (ASV future kept: simple waw)
  - Q60 Eloah → God
  - Q67 evil → calamity, peace → well-being
  - Q68 shaped → created (skies / clouds kept)
  - Q71 he is God / chaos → a wasteland / in vain
  - Q79 fair colors → antimony

---

## English-line changes (35)

| refId | Draft | Now | Governing entry |
|---|---|---|---|
| 13:1, 14:28, 15:1 | burden | oracle (concerning) | `massa-oracle-superscription-isaiah` |
| 13:9 | the land | the earth | `eretz-cosmic-scope-isaiah-24` |
| 13:16 | lain with | ravished | `mt-qere-textual-policy-isaiah` |
| 14:4 | parable | taunt | `lexical-cruxes-wave-i2-isaiah` |
| 14:13 | the far reaches of the north | the far reaches of Zaphon | `helel-zaphon-elyon-taunt-isaiah-14` + central sapunu |
| 15:2 | Bayith | the temple | `lexical-cruxes-wave-i2-isaiah` |
| 29:4 | one who has a familiar spirit | a ghost | `ariel-ob-isaiah-29` |
| 29:11, 12, 18 | book | scroll | `sefer-sealed-scroll-isaiah-29` |
| 32:3 | shall not be dim | shall not be smeared over | `hashmen-hardening-commission-isaiah` (ext.) |
| 40:6 | goodliness | constancy | `lexical-cruxes-wave-i2-isaiah` |
| 40:20 | He who is too impoverished for an oblation | As an oblation he chooses sissoo wood | `lexical-cruxes-wave-i2-isaiah` + central qorbanot |
| 40:26, 28; 42:5; 43:1, 7, 15; 45:8, 12; 48:7; 54:16; 65:17, 18 | shape(d/s/ing) | create(d/ing) / the Creator | `bara-create-isaiah` |
| 42:4, 21, 24 | law | teaching | `torah-teaching-isaiah` |
| 43:28 | the curse | the ban | `lexical-cruxes-wave-i2-isaiah` |
| 44:8 | an Eloah | a God | `elohim-el-eloah-monotheistic-formula-isaiah` |
| 45:7 | shapes darkness … makes peace and shapes evil | creates darkness … makes well-being and creates calamity | `bara-create-isaiah`, `ra-calamity-shalom-well-being-isaiah-45-7` |
| 45:18 | shaped … as chaos | created … a wasteland | `bara-create-isaiah`, `tohu-bare-emptiness-wasteland-isaiah` |
| 54:11 | in fair colors | in antimony | `lexical-cruxes-wave-i2-isaiah` |

---

## Glossary changes for review

### Central glossary (`wave-i2-central-diff.json`, base 2.83.0 → recommended 2.84.0; NOT applied)

- **Modified (appliesTo only; complete arrays + `appliesToAdded`):**
  - `shamayim` (+15)
  - `yatsar` (+16)
  - `pesel-utemunah-…` (+10)
  - `asah` (+8)
  - `adam-adamah` (+5)
  - `avon-iniquity-…` (+5)
  - `eretz` (+3: 13:5, 14:20, 14:25)
  - `sheol-…` (+3)
  - `qorbanot-…` (+3)
  - `bor-pit-…` (+2)
  - `olah-burnt-offering` (+2)
  - `tachat-substitution-formula` (+2)
  - `chesed-solitary-covenant-kindness` (+2)
  - `shaddai-eloah` (+1, Shaddai only)
  - `mount-sapunu-tsafon-…` (+1)
  - `kavod-yhwh` (+1)
  - `brit-shalom-mishkan` (+1)
  - `hineni-prophetic-response-formula` (+1)
  - `nivrakhu-bekha-niphal-hithpael` (+1)
  - `bi-nishbati-divine-self-oath` (+1)
- **Added:** none.
- **Deliberate non-extensions** (recorded in the version op):
  - `bara`
  - `elohim-as-translation`
  - `shaddai-eloah` (for Eloah at 44:8)
  - `el-elyon`
  - `kokhvei-boqer`
  - `kimah-kesil-mazzarot-ayish`
  - `tohu-vavohu`
  - `tzedakah-u-mishpat-justice-pair` (removed from 32:16, a split pair)
  - `nachash-arum` (removed from 65:25, allusion only)
  - `chesed-solitary` at 40:6
- **Already listed, no op needed:** `mahapekhah-overthrowing-formula` (ISA-13:19), `tardemah-…` (ISA-29:10).
- **Concurrency:** the Torah (exodus/numbers/deuteronomy) and Former-Prophets diffs target the same base. The likely overlaps are `shamayim`, `eretz`, `yatsar`, `asah`, `olah`, `qorbanot`, `pesel`, `adam-adamah` and `avon`. Re-base each array as the merged array plus this diff's `appliesToAdded`.

### Per-translation overlay (`isaiah-woh/_translation-glossary.json`, 1.5.0 → 1.6.0, applied)

- **Added:**
  - `bara-create-isaiah` (direct)
  - `elohim-el-eloah-monotheistic-formula-isaiah` (direct)
  - `ruach-divine-spirit-lower-case-isaiah` (direct)
  - `tohu-bare-emptiness-wasteland-isaiah` (direct)
  - `yotser-potter-clay-image-isaiah` (direct)
  - `torah-teaching-isaiah` (**inferred**)
  - `helel-zaphon-elyon-taunt-isaiah-14` (direct)
  - `ra-calamity-shalom-well-being-isaiah-45-7` (direct)
  - `massa-oracle-superscription-isaiah` (direct)
  - `mt-qere-textual-policy-isaiah` (direct)
  - `sefer-sealed-scroll-isaiah-29` (direct)
  - `ariel-ob-isaiah-29` (direct)
  - `lexical-cruxes-wave-i2-isaiah` (direct; eight single-site decisions)
- **Extended** (appliesTo plus an appended "Wave I2 extension" sentence; the wohChoice was appended with a conditional clause only for `seraphim-burning-ones-isaiah`, at 14:29, and `eretz-cosmic-scope-isaiah-24`):
  - `title-and-meta-conventions-isaiah`
  - `yhwh-tzevaot-hosts-isaiah`
  - `eretz-cosmic-scope-isaiah-24`
  - `rephaim-shades-dead-isaiah-26`
  - `seraphim-burning-ones-isaiah`
  - `nidmeti-undone-isaiah` (15:1)
  - `adonai-standalone-title-isaiah`
  - `elohei-yisrael-god-of-israel-isaiah-24`
  - `hashmen-hardening-commission-isaiah` (32:3)
  - `elohai-elohenu-doxology-isaiah-25`
  - `adonai-yhwh-compound-isaiah-25`
  - `eved-servant-identity-isaiah` (42:1 etc.)
  - `yah-tzur-olamim-everlasting-rock-isaiah-26`
  - `heikhal-temple-palace-isaiah`
- `qiryat-tohu-city-of-chaos-isaiah-24` was removed from 45:18 and stays scoped to 24:10.

---

## Notes for the Reviewer and the orchestrator

- **Watch points for the Reviewer:**
  - 40:20: the musukkannu identification is a lexical identification, not an emendation.
  - 32:3: the šʿʿ derivation against MT's pointing.
  - 13:9: "earth".
  - 15:2: "the temple".
  - 43:28: the tense, read from the pataḥ of וַאֲחַלֵּל.
  - The 45:7 non-moral pair.
- **Not touched**, per the write scope: `isaiah-woh/_meta.json` still lists 6 chapters. Its `chapterFiles`, `chapterCount` and `paragraphCount` need the 13 new chapters at bundle time.
- **Glossary versions:** the chapters pin `glossaryVersion` 2.84.0 pending application of the central diff (as the Revelation R2 wave did) and carry a `translation.verificationStatus` line saying so.
- Nothing was committed or pushed.
