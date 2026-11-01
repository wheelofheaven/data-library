# Canon-cited program — isaiah — human sign-off package

| Chapter | Verses | Approve | Revise | Flag |
|---|---|---|---|---|
| Isaiah 13 — The oracle concerning Babylon: the host from the end of the skies and the day of YHWH | 22 | 22 | 0 | 0 |
| Isaiah 14 — Israel restored and the taunt over the king of Babylon: the day star fallen from the heavens | 32 | 32 | 0 | 0 |
| Isaiah 15 — The oracle concerning Moab: the lament over the cities laid waste in a night | 9 | 7 | 2 | 0 |
| Isaiah 29 — Woe to Ariel: the sealed scroll and the reversal of the deaf and the blind | 24 | 24 | 0 | 0 |
| Isaiah 32 — The king who reigns in righteousness: the noble and the fool, and the spirit poured from on high | 20 | 20 | 0 | 0 |
| Isaiah 40 — Comfort my people: the voice in the wilderness and the one who measured the skies | 31 | 31 | 0 | 0 |
| Isaiah 42 — The first Servant Song: my chosen one and the new song from the end of the earth | 25 | 25 | 0 | 0 |
| Isaiah 43 — You are my witnesses: created for my glory, the ransom of Israel and the new thing | 28 | 28 | 0 | 0 |
| Isaiah 44 — I am the first and the last: the idol-maker's block of wood, and Cyrus my shepherd | 28 | 27 | 0 | 1 |
| Isaiah 45 — Cyrus the anointed: the one who forms light and creates darkness, and the clay and the one who forms it | 25 | 24 | 0 | 1 |
| Isaiah 48 — Refined in the furnace of affliction: the new things created now, and the exodus from Babylon | 22 | 21 | 1 | 0 |
| Isaiah 54 — Sing, O barren one: the everlasting kindness and the covenant of peace | 17 | 17 | 0 | 0 |
| Isaiah 65 — I was found by those who did not seek me: the servants and the forsakers, and the new skies and the new earth | 25 | 24 | 1 | 0 |

See the combined summary `canon-cited-final-signoff-summary.md` for decisions and fixes.

---

## Editor report (inlined)

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


---

## Reviewer report

### Isaiah 13 — The oracle concerning Babylon: the host from the end of the skies and the day of YHWH



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:23:15Z"
- glossaryReview: [{"glossary_id": "overlay:elohim-el-eloah-monotheistic-formula-isaiah", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm, ʾēl, ʾĕlôah", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "NRSV/NJPS at 43:10; 44:6-8; 45:5-22"], "reasoning": "direct verified: absolute, articular and indefinite ʾĕlōhîm, ʾēl and ʾĕlôah alternate inside one denial formula (44:6, 8; 45:21-22), so one English word is the accurate rendering, and capital/lower-case follows referent (YHWH vs idol), as ASV/NRSV do. The 45:18 vs 1 Kgs 18:39 divergence is handled as a verse-level flag (F3), not as a defect of the entry."}, {"glossary_id": "overlay:massa-oracle-superscription-isaiah", "status": "approve", "citations": ["HALOT s.v. maśśāʾ II", "Weis, A Definition of the Genre Maśśāʾ in the Hebrew Bible (diss., 1986)", "Wildberger, Isaiah 13–27 (Continental, 1997), ad loc.", "Blenkinsopp, Isaiah 1–39 (AB 19, 2000), ad loc."], "reasoning": "direct verified: maśśāʾ II 'pronouncement' in headings is the lexical consensus and NRSV/NJPS practice; 'burden' (maśśāʾ I) is kept in commentary with the Jer 23:33-38 pun honestly reported."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "Ulrich & Flint, Qumran Cave 1.II: The Isaiah Scrolls (DJD 32, 2010), ad loc.", "Yeivin, Introduction to the Tiberian Masorah (1980), on the extraordinary points
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 22 lines. 13:4-5 (canon-cited) are rendered with the standard vocabulary; 'skies' at 13:5 applies the ratified physical-register rule and does not tilt toward or against the canon's 'confins du ciel'. The reception note at 13:5 is labelled and accurate. No line reads as exegesis."
- escalationReportAdjustments: "Initial verdicts were formed from the chapter, source, overlay and central diff before opening wave-i2-editor-report.md. No verdict changed after reading it."
- founderDecisionRecommendations: {}
- summary: "22 verdicts: 22 approve. Glossary items reviewed: 12 (12 approve). Status → reviewer-approved. "

### Isaiah 14 — Israel restored and the taunt over the king of Babylon: the day star fallen from the heavens



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:23:59Z"
- glossaryReview: [{"glossary_id": "overlay:helel-zaphon-elyon-taunt-isaiah-14", "status": "approve", "citations": ["Clifford, The Cosmic Mountain in Canaan and the Old Testament (1972)", "Day, Yahweh and the Gods and Goddesses of Canaan (2000)", "Craigie, ZAW 85 (1973) on Isa 14:12-15", "KTU 1.6 i 53-65 (ʿAṯtaru on Ṣapunu)", "Wildberger, Isaiah 13–27 (Continental, 1997), ad loc.", "NRSV/NJPS 14:13 “Zaphon”"], "reasoning": "direct verified: 'day star, son of the dawn' (common nouns), 'the stars of God', 'mount of assembly', 'Zaphon' as the mountain's name and 'the Most High' are each NRSV/consensus values; the line names no myth and no speaker beyond the king of Babylon. Mirroring 'far reaches' in vv. 13 and 15 is a literal gain. Minor: the central sapunu entry suggests 'Ṣaphon'; 'Zaphon' (NRSV) is fine for an English line."}, {"glossary_id": "overlay:massa-oracle-superscription-isaiah", "status": "approve", "citations": ["HALOT s.v. maśśāʾ II", "Weis, A Definition of the Genre Maśśāʾ in the Hebrew Bible (diss., 1986)", "Wildberger, Isaiah 13–27 (Continental, 1997), ad loc.", "Blenkinsopp, Isaiah 1–39 (AB 19, 2000), ad loc."], "reasoning": "direct verified: maśśāʾ II 'pronouncement' in headings is the lexical consensus and NRSV/NJPS practice; 'burden' (maśśāʾ I) is kept in commentary with the Jer 23:33-38 pun honestly reported."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qer
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 32 lines. The canon-cited vow (14:13-14, 17) is rendered with the standard vocabulary of the Hebrew myth ('day star', 'stars of God', 'mount of assembly', 'Zaphon', 'the Most High'). 'The heavens' at 14:12-13 is the divine-realm register of the ratified šāmayim rule. No line names the speaker as anything but the king of Babylon, and the reception notes at 13-14 and 17 are labelled and accurate."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. No change after reading it."
- founderDecisionRecommendations: {}
- summary: "32 verdicts: 32 approve. Glossary items reviewed: 16 (16 approve). Status → reviewer-approved. "

### Isaiah 15 — The oracle concerning Moab: the lament over the cities laid waste in a night

- **ISA-15:2** — revise: English line approved: ʿālāh habbayiṯ wᵉḏîḇōn habbāmôṯ liḇeḵî has the article, so 'the temple' (of Kemosh) is the natural reading and needs no emendation. The commentary needs a factual fix: the baṯ-dîḇôn 'Daughter Dibon' emendation is RSV's, while NRSV reads 'Dibon has gone up to the temple' with a minor emendation of the conjunction. Correct the attribution (and cite NRSV as further support for 'the temple'); check the NJPS wording quoted while doing so.
- **ISA-15:5** — revise: bᵉrîḥehā ʿaḏ-ṣōʿar: proposed line 'her fugitives flee to Zoar' (NRSV), in place of ASV 'her nobles flee'. Re-parsed: the MT vowels (segol before -hā, no yod) are irregular for both 'her bar' (expected bᵉrîḥāh) and a plural 'her fugitives' (expected -êhā), so the pointing does not decide between them. The lexica, KJV, NRSV, NJPS, Wildberger and Blenkinsopp take the word as 'fugitives'. ASV's 'nobles' (bars = defenders) is the more interpretive choice, and with it the supplied verb 'flee' has no basis in the noun. The note's claim that 'fugitives' requires repointing ('Repointed as bᵉrîḥehā', the same form as MT) is inaccurate and should be removed. If adopted, add 15:5 to overlay lexical-cruxes-wave-i2-isaiah and record ASV 'nobles' in the commentary. 'Eglath-shelishiyah' as a place name is fine.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:24:28Z"
- glossaryReview: [{"glossary_id": "overlay:massa-oracle-superscription-isaiah", "status": "approve", "citations": ["HALOT s.v. maśśāʾ II", "Weis, A Definition of the Genre Maśśāʾ in the Hebrew Bible (diss., 1986)", "Wildberger, Isaiah 13–27 (Continental, 1997), ad loc.", "Blenkinsopp, Isaiah 1–39 (AB 19, 2000), ad loc."], "reasoning": "direct verified: maśśāʾ II 'pronouncement' in headings is the lexical consensus and NRSV/NJPS practice; 'burden' (maśśāʾ I) is kept in commentary with the Jer 23:33-38 pun honestly reported."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "Ulrich & Flint, Qumran Cave 1.II: The Isaiah Scrolls (DJD 32, 2010), ad loc.", "Yeivin, Introduction to the Tiberian Masorah (1980), on the extraordinary points", "LXX Isa 48:11 (τὸ ἐμὸν ὄνομα βεβηλοῦται)"], "reasoning": "direct verified: all 12 bracketed Ketiv/Qere pairs in the source (13:16; 29:11; 32:7, 15; 42:20, 24; 44:17, 24; 45:2; 54:16; 65:4, 7) are read as qere, and the 44:9 puncta are kept and translated. Every 1QIsaᵃ variant listed is reported, not adopted. One factual fix belongs with the 48:11 commentary (see ISA-48:11): the LXX does not support the first person there; it supplies 'my name'."}, {"glossary_id": "overlay:lexical-cruxes-wave-i2-isaiah", "status": "approve", "citations": ["CAD M/2 s.v. musukkannu", "HALOT s.v. mᵉsukkān, pûḵ", "BDB s.v. ḥeseḏ, ḥērem, māšāl", "Lohfink, TDOT 5, s.v
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 9 lines. The canon-cited 15:8-9 are rendered as the Hebrew lament; the canon's 'nuclear explosion' reading stays in a labelled reception note. Neither revise concerns lens: 15:2 is a commentary attribution error, and 15:5 prefers the lexically better-supported noun."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. The report lists 15:5 among items 'kept as drafted' (Q19 nobles) and 15:2 among the Reviewer watch points. Neither verdict changed after reading it."
- founderDecisionRecommendations: {}
- summary: "9 verdicts: 7 approve, 2 revise. Glossary items reviewed: 7 (7 approve). Status → awaiting-human. Revise items: 15:2 (commentary attribution only; line approved) and 15:5 (line: 'her fugitives flee to Zoar'; fix the note's repointing claim)."

### Isaiah 29 — Woe to Ariel: the sealed scroll and the reversal of the deaf and the blind



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:24:57Z"
- glossaryReview: [{"glossary_id": "overlay:tohu-bare-emptiness-wasteland-isaiah", "status": "approve", "citations": ["BDB s.v. tōhû", "HALOT s.v. tōhû", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc. (45:18 “a formless waste”)", "ASV/NJPS 45:18 “a waste”"], "reasoning": "direct verified: the range concrete 'waste' → abstract 'nothingness' is in both lexica; 'emptiness' for the worthlessness sites, adverbial 'in vain' at 45:19 and concrete 'a wasteland' at 45:18 (opposed to lā-šeḇeṯ, echoing the corpus's Gen 1:2 'wasteland and emptiness') are each the standard sense in context. Declining 'chaos' at 45:18 removes a mythic overtone the antithesis does not need."}, {"glossary_id": "overlay:yotser-potter-clay-image-isaiah", "status": "approve", "citations": ["BDB s.v. yāṣar (ptc. yôṣēr “potter”)", "HALOT s.v. yṣr", "Jer 18:2-6"], "reasoning": "direct verified: 'the potter' for articular hay-yôṣēr (29:16) and verbal 'the one who formed him / forms it' for suffixed yōṣᵉrô (29:16b; 45:9, 11) is a literal, consistent rule that keeps yāṣar visible against bārāʾ/ʿāśāh; NRSV's 'potter' at 45:9b is recorded as the idiomatic alternative."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "Ulrich & Flint, Qumran Cave 1.II: The Isaiah Scrolls (DJD 32, 2010), ad loc.", "Yeivin, Introduction to the Tiberian Masorah (1980), on the extraordinary points", "LXX Isa 48:11 (τὸ ἐμὸν ὄνομα βεβηλ
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 24 lines. The canon-cited 29:12 keeps the physical 'scroll' and the literal 'knows writing' without pointing to any writing; 29:20-21 keep the court setting. Reception notes are labelled and accurate (TBWTT 3 and 5)."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. No change after reading it."
- founderDecisionRecommendations: {}
- summary: "24 verdicts: 24 approve. Glossary items reviewed: 12 (12 approve). Status → reviewer-approved. Non-blocking: cross-reference 29:9 (same root šʿʿ) in the 32:3 note."

### Isaiah 32 — The king who reigns in righteousness: the noble and the fool, and the spirit poured from on high



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:25:21Z"
- glossaryReview: [{"glossary_id": "overlay:ruach-divine-spirit-lower-case-isaiah", "status": "approve", "citations": ["BDB s.v. rûaḥ", "HALOT s.v. rûaḥ", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Wildberger, Isaiah 28–39 (Continental, 2002), ad loc. (32:15)"], "reasoning": "direct verified: lower-case 'spirit' for YHWH's endowed or outpoured rûaḥ (32:15; 40:13; 42:1; 44:3; 48:16) is NRSV/NJPS practice and imports neither the ASV capital nor a transliteration; 'breath' at 40:7 (the desert wind withering grass) is correctly distinguished. The cross-book difference from Ezekiel's 'ruach' is a stance question flagged at 44:3 (F4)."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "Ulrich & Flint, Qumran Cave 1.II: The Isaiah Scrolls (DJD 32, 2010), ad loc.", "Yeivin, Introduction to the Tiberian Masorah (1980), on the extraordinary points", "LXX Isa 48:11 (τὸ ἐμὸν ὄνομα βεβηλοῦται)"], "reasoning": "direct verified: all 12 bracketed Ketiv/Qere pairs in the source (13:16; 29:11; 32:7, 15; 42:20, 24; 44:17, 24; 45:2; 54:16; 65:4, 7) are read as qere, and the 44:9 puncta are kept and translated. Every 1QIsaᵃ variant listed is reported, not adopted. One factual fix belongs with the 48:11 commentary (see ISA-48:11): the LXX does not support the first person there; it supplies 'my name'."}, {"glossary_id": "overlay:title-an
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 20 lines. The canon-cited 32:3, 5-8 are rendered as the Hebrew wisdom saying; 'smeared over' at 32:3 is justified by the lexical link to 6:10, not by the canon's 'englués', and the note says so. 'a spirit' at 32:15 is indefinite and lower-case as the Hebrew requires."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. The report's watch point on 32:3 (the šʿʿ derivation against MT's pointing) matches the Reviewer's non-blocking request. No verdict changed."
- founderDecisionRecommendations: {"F4-divine-ruach": "See ISA-44:3 (chapter 44). 32:15 'a spirit from on high' is approved and is not affected by the F4 outcome unless the founder opts to harmonize every outpouring site across books."}
- summary: "20 verdicts: 20 approve. Glossary items reviewed: 6 (6 approve). Status → reviewer-approved. Non-blocking: chapter title 'the spirit poured' → 'a spirit poured'; 32:3 note should state the revocalization and cross-refer 29:9."

### Isaiah 40 — Comfort my people: the voice in the wilderness and the one who measured the skies



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:26:27Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:elohim-el-eloah-monotheistic-formula-isaiah", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm, ʾēl, ʾĕlôah", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "NRSV/NJPS at 43:10; 44:6-8; 45:5-22"], "reasoning": "direct verified: absolute, articular and indefinite ʾĕlōhîm, ʾēl and ʾĕlôah alternate inside one denial formula (44:6, 8; 45:21-22), so one English word is the accurate rendering, and capital/lower-case follows referent (YHWH vs idol), as 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 31 lines. The canon-cited 40:21 keeps the ellipsis reading that does not favour the canon's quotation. 40:22 renders ḥûḡ as 'circle' with no claim about shape. 40:26 'who created these?' replaces the draft's craft verb 'shaped', removing a workshop overtone. 'sissoo wood' at 40:20 is lexical, not lens."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. The report's F1 adds that HALOT assigns the Piel to a separate homonym, which agrees with the Reviewer's view. No verdict changed."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale.", "F4-divine-ruach": "Accept the genre-based split: lower-case 'spirit' in Isaiah's endowment/outpouring poetry and 'ruach' in Kings/Ezekiel agent narratives. The weak point is Ezekiel's own endowment/outpouring verses: 37:14 'I will put my ruach in you' is published, a
- summary: "31 verdicts: 31 approve. Glossary items reviewed: 18 (17 approve, 1 flag-for-human). Status → awaiting-human. Awaiting human only for founder decision F1 (bara-create-isaiah flagged for ratification). Every line is approved."

### Isaiah 42 — The first Servant Song: my chosen one and the new song from the end of the earth



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:26:53Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:elohim-el-eloah-monotheistic-formula-isaiah", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm, ʾēl, ʾĕlôah", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "NRSV/NJPS at 43:10; 44:6-8; 45:5-22"], "reasoning": "direct verified: absolute, articular and indefinite ʾĕlōhîm, ʾēl and ʾĕlôah alternate inside one denial formula (44:6, 8; 45:21-22), so one English word is the accurate rendering, and capital/lower-case follows referent (YHWH vs idol), as 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 25 lines. The canon-cited 42:1, 3 keep the servant unidentified and the reed/wick images as given. 'teaching' for tôrāh is lexical, not lens. 'created the skies' at 42:5 removes the draft's craft register."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. No change after reading it."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale.", "F4-divine-ruach": "Accept the genre-based split: lower-case 'spirit' in Isaiah's endowment/outpouring poetry and 'ruach' in Kings/Ezekiel agent narratives. The weak point is Ezekiel's own endowment/outpouring verses: 37:14 'I will put my ruach in you' is published, a
- summary: "25 verdicts: 25 approve. Glossary items reviewed: 11 (10 approve, 1 flag-for-human). Status → awaiting-human. Awaiting human only for founder decision F1. Every line is approved."

### Isaiah 43 — You are my witnesses: created for my glory, the ransom of Israel and the new thing



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:27:22Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:elohim-el-eloah-monotheistic-formula-isaiah", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm, ʾēl, ʾĕlôah", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "NRSV/NJPS at 43:10; 44:6-8; 45:5-22"], "reasoning": "direct verified: absolute, articular and indefinite ʾĕlōhîm, ʾēl and ʾĕlôah alternate inside one denial formula (44:6, 8; 45:21-22), so one English word is the accurate rendering, and capital/lower-case follows referent (YHWH vs idol), as 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 28 lines. The canon-cited 43:5-13 are rendered as the Hebrew trial and ingathering. 'I am he' (not the canon's 'le même') and ASV's retrospective 43:13 are kept, and the 43:7 triad 'created, formed, made' coincides with the canon's French because it is the standard rendering."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. The report's watch point on the 43:28 tense agrees with the Reviewer's parse. No change."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale."}
- summary: "28 verdicts: 28 approve. Glossary items reviewed: 14 (13 approve, 1 flag-for-human). Status → awaiting-human. Awaiting human only for founder decision F1. Every line is approved."

### Isaiah 44 — I am the first and the last: the idol-maker's block of wood, and Cyrus my shepherd

- **ISA-44:3** — flag-for-human: Line approved as translation: kî ʾeṣṣāq-mayim ʿal-ṣāmēʾ ... ʾeṣṣōq rûḥî ʿal-zarʿeḵā ûḇirḵāṯî: lower-case 'my spirit' parallel to water and blessing is exact (NRSV/NJPS). Flagged only for founder decision F4 (Isaiah 'spirit' vs Ezekiel's 'ruach' at the shared outpouring/endowment image). Reviewer recommends accepting the split with reciprocal cross-references; see founderDecisionRecommendations.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:27:52Z"
- glossaryReview: [{"glossary_id": "overlay:elohim-el-eloah-monotheistic-formula-isaiah", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm, ʾēl, ʾĕlôah", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "NRSV/NJPS at 43:10; 44:6-8; 45:5-22"], "reasoning": "direct verified: absolute, articular and indefinite ʾĕlōhîm, ʾēl and ʾĕlôah alternate inside one denial formula (44:6, 8; 45:21-22), so one English word is the accurate rendering, and capital/lower-case follows referent (YHWH vs idol), as ASV/NRSV do. The 45:18 vs 1 Kgs 18:39 divergence is handled as a verse-level flag (F3), not as a defect of the entry."}, {"glossary_id": "overlay:ruach-divine-spirit-lower-case-isaiah", "status": "approve", "citations": ["BDB s.v. rûaḥ", "HALOT s.v. rûaḥ", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Wildberger, Isaiah 28–39 (Continental, 2002), ad loc. (32:15)"], "reasoning": "direct verified: lower-case 'spirit' for YHWH's endowed or outpoured rûaḥ (32:15; 40:13; 42:1; 44:3; 48:16) is NRSV/NJPS practice and imports neither the ASV capital nor a transliteration; 'breath' at 40:7 (the desert wind withering grass) is correctly distinguished. The cross-book difference from Ezekiel's 'ruach' is a stance question flagged at 44:3 (F4)."}, {"glossary_id": "overlay:tohu-bare-emptiness-wasteland-isaiah", "status": "approve", "citations": ["BDB s.v. tōhû", "HALOT s.v. tōhû", "Blenkinsopp, Isaiah 40–55 (
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 28 lines. The canon-cited 44:19 keeps the standard question reading, while the canon reads statements. 44:8 'a God' removes a transliteration that would have marked a false distinction. The idol polemic uses lower-case 'god' consistently."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. Reading it confirmed that F4 is a founder-level cross-book question, so 44:3 is recorded as flag-for-human, not as a defect. No other change."
- founderDecisionRecommendations: {"F4-divine-ruach": "Accept the genre-based split: lower-case 'spirit' in Isaiah's endowment/outpouring poetry and 'ruach' in Kings/Ezekiel agent narratives. The weak point is Ezekiel's own endowment/outpouring verses: 37:14 'I will put my ruach in you' is published, and 36:27 and 39:29 are not yet translated in this data. These share Isaiah's sense rather than the 'agent that lifts' sense that justifies transliteration. At the next Ezekiel pass, decide whether those few sites should move to 'my spirit' or stay 'ruach' for in-book consistency. Either way, add reciprocal cross-references 44:3 ↔ Ezek 37:14 now, and to 39:29 once it is translated. Do not transliterate in Isaiah."}
- summary: "28 verdicts: 27 approve, 1 flag-for-human. Glossary items reviewed: 15 (15 approve). Status → awaiting-human. Flag 44:3 for founder decision F4 (line approved as translation)."

### Isaiah 45 — Cyrus the anointed: the one who forms light and creates darkness, and the clay and the one who forms it

- **ISA-45:18** — flag-for-human: Line approved as translation: bôrēʾ haššāmayim hûʾ hāʾĕlōhîm yōṣēr hāʾāreṣ wᵉʿōśāh hûʾ kônᵉnāh lōʾ-ṯōhû ḇᵉrāʾāh lāšeḇeṯ yᵉṣārāh: 'created … he is God … formed … made … established', and 'a wasteland' opposite 'to be inhabited', are all exact. Flagged only for founder decision F3 (cross-book rendering of the identification formula). Reviewer recommends keeping 'he is God' with reciprocal cross-references; see founderDecisionRecommendations.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:28:22Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:elohim-el-eloah-monotheistic-formula-isaiah", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm, ʾēl, ʾĕlôah", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "NRSV/NJPS at 43:10; 44:6-8; 45:5-22"], "reasoning": "direct verified: absolute, articular and indefinite ʾĕlōhîm, ʾēl and ʾĕlôah alternate inside one denial formula (44:6, 8; 45:21-22), so one English word is the accurate rendering, and capital/lower-case follows referent (YHWH vs idol), as 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 25 lines. The canon-cited 45:9-10 keep the potter/clay and father/child images as the Hebrew gives them. 45:7 'calamity' is the lexical non-moral sense, not a softening for lens purposes. 45:18 'a wasteland' (not 'chaos') removes a mythic overtone. 'created' throughout removes the draft's craft register."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. Reading it confirmed that F3 is a founder-level cross-book question, so 45:18 is recorded as flag-for-human, not as a defect. No other change."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale.", "F3-he-is-God": "Keep 'he is God' at 45:18 and do not harmonize Isaiah toward 'the Elohim'. In Second Isaiah the articular predicate sits inside the denial formula ('I am YHWH, and there is no other'), and a capitalized plural 'the Elohim' there would read as a projec
- summary: "25 verdicts: 24 approve, 1 flag-for-human. Glossary items reviewed: 18 (17 approve, 1 flag-for-human). Status → awaiting-human. Awaiting human for founder decisions F1 (bara entry) and F3 (45:18; line approved as translation)."

### Isaiah 48 — Refined in the furnace of affliction: the new things created now, and the exodus from Babylon

- **ISA-48:11** — revise: English line approved: lᵉmaʿănî lᵉmaʿănî ʾeʿĕśeh kî ʾêḵ yēḥāl, 'for how should it be profaned?', keeps MT without a supplied subject. The commentary's versional claim needs correcting. The LXX does not read the first person; it reads 'for my name is profaned', which supports ASV's supplied 'my name' (as does NRSV, after the Greek). Only 1QIsaᵃ attests the first person. Rewrite: 'ASV and NRSV supply "my name" from v. 9, with the LXX; the Great Isaiah Scroll reads the first person, "how should I be profaned?"'.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:28:51Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:ruach-divine-spirit-lower-case-isaiah", "status": "approve", "citations": ["BDB s.v. rûaḥ", "HALOT s.v. rûaḥ", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Wildberger, Isaiah 28–39 (Continental, 2002), ad loc. (32:15)"], "reasoning": "direct verified: lower-case 'spirit' for YHWH's endowed or outpoured rûaḥ (32:15; 40:13; 42:1; 44:3; 48:16) is NRSV/NJPS practice and imports neither the ASV capital nor a transliteration; 'breath' at 40:7 (the deser
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 22 lines. The canon-cited 48:10-11 keep MT 'chosen' (the canon's French has 'éprouvé'), and the apparatus explains both. No line carries a project reading."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. No change after reading it."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale.", "F4-divine-ruach": "Accept the genre-based split: lower-case 'spirit' in Isaiah's endowment/outpouring poetry and 'ruach' in Kings/Ezekiel agent narratives. The weak point is Ezekiel's own endowment/outpouring verses: 37:14 'I will put my ruach in you' is published, a
- summary: "22 verdicts: 21 approve, 1 revise. Glossary items reviewed: 13 (12 approve, 1 flag-for-human). Status → awaiting-human. Revise 48:11 (commentary versional claim only; line approved). F1 also pending."

### Isaiah 54 — Sing, O barren one: the everlasting kindness and the covenant of peace



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:29:17Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "Ulrich & Flint, Qumran Cave 1.II: The Isaiah Scrolls (DJD 32, 2010), ad loc.", "Yeivin, Introduction to the Tiberian Masorah (1980), on the extraordinary points", "LXX Isa 48:11 (τὸ ἐμὸν ὄνομα βεβηλοῦται)"], "reasoning": "direct verified: all 12 bracketed Ketiv/Qere pairs in the source (13:16; 29:11; 32:7, 15; 42:20, 24; 44:17, 24; 45:2; 54:16; 65:4, 7) are read
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 17 lines. The canon-cited 54:7 is rendered as addressed to Zion. 'antimony' at 54:11 is lexical. No line carries a project reading."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. No change after reading it."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale."}
- summary: "17 verdicts: 17 approve. Glossary items reviewed: 12 (11 approve, 1 flag-for-human). Status → awaiting-human. Awaiting human only for founder decision F1. Every line is approved."

### Isaiah 65 — I was found by those who did not seek me: the servants and the forsakers, and the new skies and the new earth

- **ISA-65:17** — revise: English line approved: kî-hinnî ḇôrēʾ šāmayim ḥăḏāšîm wāʾāreṣ ḥăḏāšāh, 'I am creating new skies and a new earth', follows the creation-register rule and the participle after hinnî. The commentary needs a factual fix (the same sentence appears in the shamayim op reason and editor report F2). The corpus renders Gen 1:1 'the skies and the land', not 'the skies and the earth'. Rewrite to say that 65:17 echoes the Gen 1:1 merism and verb, that the line keeps 'skies' with Gen 1:1, and that it uses 'earth' (cosmic register) where Gen 1:1 has 'land'. The register choice itself is founder decision F2; Reviewer recommends 'skies' (see founderDecisionRecommendations).

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:29:45Z"
- glossaryReview: [{"glossary_id": "overlay:bara-create-isaiah", "status": "flag-for-human", "citations": ["BDB s.v. bārāʾ (Qal/Niphal never with an accusative of material)", "HALOT s.v. brʾ I (Piel “cut down, clear” listed under a separate homonym)", "Bernhardt, TDOT 2, s.v. bārāʾ", "Schmidt, THAT 1, s.v. brʾ", "Stuhlmueller, Creative Redemption in Deutero-Isaiah (AnBib 43, 1970)", "Westermann, Isaiah 40–66 (OTL, 1969), ad loc.", "Blenkinsopp, Isaiah 40–55 (AB 19A, 2002), ad loc.", "TBWTT ch. 5 (Isa 43:7 « créés, formés et faits »)"], "reasoning": "Re-parsed all 14 sites (Qal pf/ptc, Niphal pf at 48:7). claim_type direct is correct: 'create' is the lexical and versional consensus, and the objects in Isaiah (darkness, calamity, events, the smith, Jerusalem-as-joy) cannot take a craft verb. Flagged only because it is the open founder decision F1; Reviewer recommends ratifying it, and separately reviewing the Genesis 'shape' entry (see founderDecisionRecommendations)."}, {"glossary_id": "overlay:mt-qere-textual-policy-isaiah", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on Ketiv/Qere", "Ulrich & Flint, Qumran Cave 1.II: The Isaiah Scrolls (DJD 32, 2010), ad loc.", "Yeivin, Introduction to the Tiberian Masorah (1980), on the extraordinary points", "LXX Isa 48:11 (τὸ ἐμὸν ὄνομα βεβηλοῦται)"], "reasoning": "direct verified: all 12 bracketed Ketiv/Qere pairs in the source (13:16; 29:11; 32:7, 15; 42:20, 24; 44:17, 24; 45:2; 54:16; 65:4, 7) are read
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 25 lines. 'new skies' at 65:17 applies the ratified register rule; it is a register choice, not a cosmological claim, and it is flagged to the founder. The canon-cited 65:20 is rendered as the Hebrew promise. No line carries a project reading."
- escalationReportAdjustments: "Initial verdicts were formed before opening wave-i2-editor-report.md. The report's F2 repeats the Gen 1:1 'the skies and the earth' statement, which confirms the 65:17 revise (the corpus has 'the skies and the land'). No verdict changed."
- founderDecisionRecommendations: {"F1-bara": "Ratify 'create' / 'Creator' for all 14 Isaiah sites (overlay bara-create-isaiah). Yes, the Genesis 'shape' should be reviewed at the next Genesis pass. Reasons: (1) the Qal/Niphal never takes an accusative of material and the lexica gloss it 'create' (BDB; HALOT brʾ I; Bernhardt TDOT 2; Schmidt THAT 1). (2) The central bara rationale's 'Piel \"cut out, fashion\"' is the separate homonym 'cut down, clear (forest)' (Josh 17:15, 18; Ezek 23:47; HALOT). Its '(Gesenius §17)' locator is wrong as a GKC reference, since GKC §17 treats Qere/Ketiv. (3) The central yatsar entry glosses yāṣar 'form, shape, fashion (as a potter)', so 'shape' for bārāʾ already collides with the potter's verb even in Genesis. (4) The canon itself uses 'créés, formés et faits' (Isa 43:7). Corpus finding: AMO-WOH-4:13 already renders bôrēʾ rûaḥ 'shapes the wind', an extension of the Genesis 'shape' outside the central appliesTo that is now inconsistent with Isaiah. Review it together with the Genesis decision. Options for the Genesis review: re-render 'create' and keep the bārāʾ/ʿāśāh/yāṣar distinction as create/make/form (the Isaiah model), or keep 'shape' but downgrade the central entry to speculative with a corrected rationale.", "F2-65:17-skies": "Accept 'new skies and a new earth' at 65:17. The verse is the creation-register merism, so the ratified šāmayim rule gives 'skies', and 'the heavens' stays for YHWH's dwelling (66:1). For reception continuity, keep 2 Pet 3:13 / Rev 21:1 ('a new heav
- summary: "25 verdicts: 24 approve, 1 revise. Glossary items reviewed: 11 (10 approve, 1 flag-for-human). Status → awaiting-human. Revise 65:17 (commentary fact only; line approved); founder decisions F1 and F2 pending."
