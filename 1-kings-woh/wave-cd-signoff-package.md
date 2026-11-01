# Kings waves C/D (1 Kings 6, 8; 2 Kings 4, 17) — human sign-off package

**Scope:** 1 Kings 6, 8 (`1-kings-woh`: the Temple built; the ark, the cloud, Shelomoh's prayer) and 2 Kings 4, 17 (`2-kings-woh`: Elisha's miracles; the fall of Shomron) — 189 verses. Canon-cited sites: 1 Kgs 6:1, 6:13, 8:10–13; 2 Kgs 4:32–37, 4:42–44, 17:16, 17:23.

**Status:** `awaiting-human`, 1.0.0-rc1. Builds on wave A (signed off, central 2.78.0) and wave B (awaiting sign-off; central → 2.79.0, overlays → 1.1.0). This wave: central → 2.80.0, overlays → 1.2.0.

## Summary

| Chapter | Verses | With commentary | Approve | Revise | Flag |
|---|---|---|---|---|---|
| 1 Kings 6 — Shelomoh (Solomon) builds the house for YHWH | 38 | 35 | 36 | 2 | 0 |
| 1 Kings 8 — The ark brought in, the cloud fills the house, the prayer of Shelomoh (Solomon) | 66 | 62 | 66 | 0 | 0 |
| 2 Kings 4 — Elisha: the widow's oil, the Shunammite's son raised, the pot and the twenty loaves | 44 | 40 | 43 | 1 | 0 |
| 2 Kings 17 — The fall of Shomron (Samaria) and the exile of Yisra'el (Israel) | 41 | 41 | 40 | 1 | 0 |

- **Lens leakage:** none. 1 Kgs 8:12 keeps *ʿărāp̄el* 'thick darkness' (as exodus-woh Ex 20:18) although the canon's French quotes « dans un nuage »; the canon reading sits in a labelled reception note.
- **Ketiv/Qere:** 22 readings in 19 verses (2 Kgs 17:31 has two), Qere translated everywhere.
- **Quotation marks:** balanced and nested in all four chapters. English names in titles per the wave-A ruling.
- **Central 2.79.0 → 2.80.0:** 5 new direct entries (Temple three-room plan; *šāḵan* 'dwell'; *ʿărāp̄el* 'thick darkness'; *bêṯ zəḇul* 'an exalted house'; *heʿānān* the cloud filling the sanctuary), host-of-the-heavens extended to the astral sense at 2 Kgs 17:16, 24 appliesTo-only extensions (no refIds lost).
- **Overlays 1.1.0 → 1.2.0:** 4 new direct entries (*gāhar* 'crouched', *tôrâ* 'law', *pəqāʿîm* 'gourds', *mišpāṭ* 'manner') + 8 extensions. Speculative / inferred entries: none.

## Items requiring decision (Reviewer + Editor agree on every recommendation)

1. **Temple rooms** — ʾûlām 'porch', hêkāl **'great hall'**, dəbîr **'inner sanctuary'** (ASV 'temple', 'oracle' — 'oracle' rests on a rejected etymology), 'the most holy place'. *Recommended: ratify* (a corpus-wide central entry).
2. **8:13 *bêṯ zəḇul*** 'an exalted house' (modern lexical consensus, after the Ugaritic *zbl*). *Ratify.*
3. **Mitzrayim** in Kings (the ratified tz rule) vs **Mitsrayim** in genesis-woh/exodus-woh English lines (81 + 38 occurrences). *Recommended: keep Mitzrayim in Kings now; normalise Genesis/Exodus in a separate mechanical pass if you want one corpus spelling.*
4. **8:23** "there is no **elohim** like you" (lower case: the class YHWH is compared with). *Ratify.*
5. **2 Kgs 17:26–27** "the **manner** of the **Elohim** of the land" (KJV 'manner'; capital as KJV/NJPS). *Ratify.*
6. **tôrâ = 'law'** in Kings (exodus-woh has 'torah'; reconcile at the next Exodus pass). *Keep.*
7. **'crouched'** at 2 Kgs 4:34–35 (lexical *gāhar*, as the signed-off 1 Kgs 18:42). *Ratify.*
8. **'mercy'** at 8:50 (the Gen 43:14 idiom) and **'kindness'** at 8:23. *Keep.*
9. **'the Shomronites'** at 2 Kgs 17:29 ('Samaritans' is anachronistic). *Ratify.*

## Fixes applied at sign-off (Reviewer revises; no other line changes)

- **6:20 line:** "And the interior of the inner sanctuary was twenty cubits in length, and twenty cubits in breadth, and twenty cubits in height; …"
- **17:4 line:** "as he had year by year".
- **6:1 note + MT-baseline overlay entry:** the LXX gives 6:1 (with 440) followed by 6:1a–d carrying MT 5:31–32 and 6:37–38 (Rahlfs, 3 Kgdms 6:1a–d).
- **4:38 note:** keep 'stew' and record that genesis-woh keeps the ASV 'pottage' at Gen 25:29.
- Overlay: Ketiv/Qere count 22; names entry corrected (Genesis/Exodus English lines print 'Mitsrayim'); Temple-rooms entry: drop the unverified Alter attribution (NJPS 'Great Hall' confirmed).
- Notes: 4:31 (18:29 renders the phrase 'no one paying heed' — say so); 4:39, 17:21 label the 1-kings-woh overlay entries they cite; 8:9 cite 'BDB s.v.' unless 1b checks; 8:35 'the Targum' for 'some versions'.
- When applying the central diff: merge, don't replace, `kavod-yhwh` appliesTo.

## Follow-ups (not blocking)
- Hosted ASV errors: 1 Kgs 8:15, 8:43 (known), 2 Kgs 17:34 'former manner' (probably 'the former manners'); backtick apostrophes; spacing at 2 Kgs 4:25.

---

## Editor's escalation report (inlined)

# Kings Waves C-D Editor Report: the Temple and its dedication; Elisha's miracles; the fall of Shomron

**Books / chapters:** `1-kings-woh` 6 (38 verses), 8 (66); `2-kings-woh` 4 (44), 17 (41). That is 189 verses.
**Editor pass:** 2026-11-01 (claude-opus-5-5, woh-editor role)
**Status at end of pass:** all four chapters `draft` → `editor-review`; version `0.1.0` → `1.0.0-rc1`; `glossaryVersion` 2.80.0 (pending application of the wave-A, wave-B and wave-C/D central diffs, in that order); `overlayGlossaryVersion` 1.2.0 (pending the wave-B and wave-C/D overlay diffs); `reviewer` left `pending`; `claude-opus-5-5 (editor)` added to `modelDrafts`.
**Editorial questions:** 84 received (21 of them Ketiv/Qere), 84 resolved, all arrays cleared. None is escalated as unresolvable. Nine resolutions are flagged below as open founder-preference points; a tenth (B, šāmayim) follows the rule already ratified at the wave-A sign-off.

**Files written (only these)**

- `1-kings-woh/chapter-6.json`, `1-kings-woh/chapter-8.json`
- `2-kings-woh/chapter-4.json`, `2-kings-woh/chapter-17.json`
- `1-kings-woh/wave-cd-overlay-diff.json` (proposed, not applied; sections for both overlays, 1.1.0 → 1.2.0)
- `1-kings-woh/wave-cd-central-diff.json` (proposed, not applied; 2.79.0 → 2.80.0)
- this report

No overlay, central glossary, wave-A or wave-B file was edited. Three follow-ups that touch read-only files are listed at the end for the orchestrator.

**Counts**

- Commentary (`notes.official`): 178 of 189 paragraphs (1 Kgs 6: 35/38; 1 Kgs 8: 62/66; 2 Kgs 4: 40/44; 2 Kgs 17: 41/41). The uncommented verses are plain narrative with no divergence from the ASV.
- Wheel of Heaven reception notes (separately headed, "reception note, not a translation claim"): 1 Kgs 6:1, 6:13, 8:10, 8:11, 8:12, 8:13; 2 Kgs 4:34 (covering 4:32-37), 4:42 (covering 4:42-44), 17:16, 17:23. Each was checked against `kings-canon-citations.md` (TBWTT ch. 3: 3:103-107, 3:134, 3:136-137, 3:140-141).
- Overlay diff: 4 new entries (2 shared and mirrored in both overlays; 1 for 1-kings-woh only; 1 for 2-kings-woh only) and 8 additive extensions (7 shared, 1 for 2-kings-woh only). All new entries are `direct`.
- Central diff: 5 new entries (all `direct`), 1 modification of the pending wave-B entry `tzeva-ha-shamayim-...`, and 24 appliesTo-only extensions.
- **English text changed at 55 verses** over the drafts, plus the chapter titles (see below). Every change is backed by a glossary entry (rule 7):
  - **Name normalization** (`hebrew-proper-name-transliteration-convention-kings`):
    - Mitsrayim → Mitzrayim (tz rule) at 1 Kgs 6:1; 8:9, 16, 21, 51, 53, 65; 2 Kgs 17:4, 7, 36.
    - Tsiyyon → Tziyyon (8:1).
    - Mosheh → Moshe (8:9, 53, 56), as wave B at 1 Kgs 2:3.
    - Shomeron → Shomron (2 Kgs 17:1, 5, 6, 24, 26, 28, and title), the wave-A form.
    - Gentilics: 'the Shomronim' → 'the Shomronites' (17:29); 'the Avvim' / 'the Sefarvim' → 'the Avvites' / 'the Sefarvites' (17:31).
  - **Temple plan** (new central `ulam-hekhal-devir-temple-three-room-plan-cross-corpus`): 'temple' → 'great hall' for *hêḵāl* (6:3, 5, 17, 33); 'oracle' → 'inner sanctuary' for *dəḇîr* (6:5, 16, 19, 20, 21, 22, 23, 31; 8:6, 8).
  - **'knops' → 'gourds'** (6:18): new overlay `peqaim-gourd-ornaments-1-kings-6`.
  - **'a house of habitation' → 'an exalted house'** (8:13): new central `beit-zevul-exalted-house-1-kgs-8-13-cross-corpus`.
  - ***šāmayim* 'skies' → 'heavens'** at the divine-realm sites:
    - 1 Kgs 8:22, 23, 27, 30, 32, 34, 36, 39, 43, 45, 49, 54 (central `shamayim`, numinous-register clause).
    - 2 Kgs 17:16 'all the host of the heavens' (central `shamayim` + `tzeva-ha-shamayim-...`).
    - 'skies' is kept at 1 Kgs 8:35 (rain).
  - **8:23 'no Elohim like you' → 'no elohim like you'**: `elohim-referent-and-article-conventions-kings`, new clause 5.
  - **8:23 'lovingkindness' → 'kindness'**: central `chesed-solitary-covenant-kindness`.
  - **8:50 'compassion' (twice) → 'mercy'**: central `rachamim-compassion-womb-root`.
  - **'soul' removed** (`nefesh-scope-and-spelling-kings`):
    - 1 Kgs 8:48 'with all their being'.
    - 2 Kgs 4:27 'for she is in bitter distress'.
    - 2 Kgs 4:30 'and as you yourself live'.
  - **'stretched himself out upon him' → 'crouched over him'** (2 Kgs 4:34, 35): new shared overlay `gahar-crouch-over-kings`.
  - **'the law of the Elohim of the land' → 'the manner of the Elohim of the land'** (2 Kgs 17:26 twice, 27): new overlay `mishpat-manner-custom-2-kings-17`.
  - **'served Baal' → 'served Ba'al'** (17:16): `habbaal-baal-hebrew-bible-rendering-kings`.
- All other lines are the Translator's draft, unchanged.
- **Quotation marks** (coordinator check, wave-A convention: double for direct speech, single nested, double at a third level; a speech running across verses is opened once and closed where it ends). The drafts already conform, so no punctuation was changed. Script check: double and single quotes balanced in every chapter, no single quote outside an open double. 1 Kgs 6: 1 speech (6:12-13). 1 Kgs 8: 4 speeches (8:12-13; blessing 8:15-21; prayer 8:23-53; blessing 8:56-61) with nested YHWH-words at 8:16, 18-19, 25, 29 and the confession at 8:47. 2 Kgs 4: 38 double-quote pairs, nested at 4:13, 26, 28, 43. 2 Kgs 17: 5 speeches (17:12, 13, 26, 27, 35-39).
- **Chapter titles** (ratified at the wave-A sign-off: English form of the principal name in parentheses):
  - 1 Kings 6 — Shelomoh (Solomon) builds the house for YHWH
  - 1 Kings 8 — The ark brought in, the cloud fills the house, the prayer of Shelomoh (Solomon)
  - 2 Kings 4 — unchanged (Elisha needs no gloss)
  - 2 Kings 17 — The fall of Shomron (Samaria) and the exile of Yisra'el (Israel)

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry is created or extended in either diff, and no `inferred` entry is created. Nothing in this pass blocks advance on the speculative count.

### Canon-cited sites in waves C-D

At each of these, the line renders the Hebrew lexically, and the Raëlian reading appears only in a paragraph headed **"Wheel of Heaven reading (reception note, not a translation claim)"**.

| Site | Canon (TBWTT ch. 3) | Line |
|---|---|---|
| 1 Kgs 6-8 (6:1) | Solomon's 'sumptuous residence to receive the creators' (3:103) | 'house' (*bayiṯ*) |
| 1 Kgs 6:13 | 'I will dwell among the children of Israel' (3:106) | 'dwell in the midst of' (`shakhan-...`) |
| 1 Kgs 8:10 | 'The cloud filled the house of Yahweh' (3:105) | 'the cloud' (`he-anan-...`) |
| 1 Kgs 8:11 | 'The glory of Yahweh had filled the house' (3:105) | 'the glory of YHWH' (`kavod-yhwh`) |
| 1 Kgs 8:12 | FR 'il réside dans un nuage' (3:104); 'a craft in orbit' (3:107) | **'the thick darkness'** (`arafel-...`) |
| 1 Kgs 8:13 | 'an house to dwell in' (3:104) | 'an exalted house' (`beit-zevul-...`) |
| 2 Kgs 4:32-37 | 'resurrection', mouth-to-mouth, heart massage (3:134) | plain sense; 'crouched over him' |
| 2 Kgs 4:42-44 | 'The multiplication of the loaves' (3:136-137) | ASV sense |
| 2 Kgs 17:16 | 'worshipped metal idols' (3:140, summary) | 'molten images' |
| 2 Kgs 17:23 | 'Israel was carried away out of their own land' (3:141) | ASV sense |

---

## Founder-preference points (resolved, flagged for confirmation)

All are applied. A and C-J await confirmation and can each be reversed mechanically; B follows a ratified rule.

### A. Temple architecture: 'great hall' / 'inner sanctuary' (central, corpus-wide)

- **Decision:**
  - *ʾûlām* 'porch' (ASV).
  - *hêḵāl* 'great hall' (NJPS, Alter; ASV 'temple').
  - *dəḇîr* 'inner sanctuary' (NRSV; ASV 'oracle').
  - *qōḏeš haqqŏḏāšîm* 'the most holy place' (ASV).
  - *habbayiṯ happənîmî* 'the inner house' (literal).
  - Context rule: *hêḵāl* = 'temple'/'palace' where it means the whole building.
- **Why:**
  - In 1 Kgs 6 the whole building is the *bayiṯ*, so 'the temple of the house' (6:3) misleads.
  - 'Oracle' rests on the discredited derivation of *dəḇîr* from *dbr* 'speak' (Vulgate *oraculum*; HALOT 'back room').
  - The Translator asked for a corpus-wide decision, so it is central.
- **Alternatives:**
  - ASV throughout ('temple', 'oracle'): revert 13 lines.
  - Transliteration ('hekhal', 'devir').
  - NRSV 'nave'.

### B. *šāmayim* 'heavens' in Shelomoh's prayer and at 2 Kgs 17:16 (follows ratified decision B; no confirmation needed)

- **Decision:**
  - 'heavens' at the 12 divine-dwelling sites of 1 Kgs 8 (22, 23, 27, 30, 32, 34, 36, 39, 43, 45, 49, 54), under the šāmayim-by-register rule ratified at the wave-A sign-off (YHWH's realm 'heaven(s)', physical sky 'skies').
  - 8:27 reads 'the heavens and the heavens of the heavens', as the brief specified.
  - 'skies' at 8:35, where the sky withholds rain.
  - 2 Kgs 17:16 'all the host of the heavens'. This resolves the wave-B `tzeva-ha-shamayim` entry's open sentence ("later passes may use 'skies'") in favour of one rendering for both the council sense and the astral sense.
- **Lens:** 'skies' would be the more lens-congenial register at the canon-adjacent 8:10-13 context. 'Heavens' is the corpus-consistent choice (genesis-woh 28:12; exodus-woh 20:4, 11, 19).
- **Status:** settled by the ratified rule; listed here only so the Reviewer can audit the 13 lines.

### C. Mitzrayim / Tziyyon (tz) against the corpus 'Mitsrayim'

- **Decision:** The Kings tsade rule (wave B: Tzadoq, Tzidqiyahu, Etzyon-Gever; wave A: Tzarfat, Tzidon) is applied to the first Kings occurrences of these names.
- **Conflict:** genesis-woh writes 'Mitsrayim' 206 times (and 'Mitzrayim' 18 times), and exodus-woh writes 'Mitsrayim' throughout.
- **Recommendation:** One corpus normalization pass for this name, either Kings → 'Mitsrayim' (10 lines here) or Genesis/Exodus → 'Mitzrayim'.

### D. 1 Kgs 8:23 'there is no elohim like you' (lower case)

- **Decision:** New clause 5 of the shared `elohim-referent-...` entry. In the incomparability formula *ʾên-kāmôḵā ʾĕlōhîm*, the noun names the class compared with YHWH, so it is written in lower case. The draft had a capital, which reads as a name and would make YHWH be compared with himself.
- **Neutrality:** The commentary states that the case does not decide between the monotheistic reading (Deut 4:39; ASV 'no God like thee') and the reading that presupposes other divine beings.
- **Alternative:** Keep 'Elohim' with a note.

### E. 2 Kgs 17:26-27 'the manner of the Elohim of the land'

- **Two decisions here:**
  1. *mišpāṭ* = 'manner'. This follows the KJV and keeps the passage's keyword concordant (17:26, 27, 33, 34, 40 'manner'), so that 'law' is reserved for *tôrâ*. The ASV/NRSV have 'law'.
  2. Capital 'Elohim'. The narrator has YHWH send the lions (17:25), so the referent rule gives a capital. The ASV 'the god of the land' expresses the settlers' perspective, and the commentary records it.
- **Alternatives:** 'law' (ASV), and/or lower-case 'elohim' (perspective rather than referent).

### F. *tôrâ* 'law' in Kings against 'torah' in exodus-woh

- **Decision:** New shared overlay entry `torah-law-deuteronomistic-kings` records the Kings choice ('law', ASV). It covers 2 Kgs 17:13, 34, 37 and also 1 Kgs 2:3 (wave B), where 'the law of Moshe' already stands.
- **Conflict:** exodus-woh transliterates 'torah' (Ex 13:9; 16:4) without an entry.
- **Recommendation:** A central entry at the next Exodus/Deuteronomy pass, deciding whether Kings should transliterate or Exodus should translate.

### G. 1 Kgs 8:13 'an exalted house' at a canon-cited verse

- **Decision:** *zəḇul* is rendered by the modern lexical consensus, from Ugaritic *zbl* 'prince' (HALOT; RSV/NRSV 'exalted house'; NJPS 'stately House').
- **Effect on the canon citation:** The English canon quotes the KJV 'an house to dwell in'. The change is lens-neutral, since it neither helps nor hinders the canon's 'residence' reading. It is flagged only because the line now diverges from the canon's quotation.
- **Alternative:** Keep the ASV 'a house of habitation' with a note.

### H. 'crouched over him' (2 Kgs 4:34-35), concordant with wave-A 1 Kgs 18:42

- **Decision:** *gāhar* occurs only at these three sites. Wave A already renders 18:42 'he crouched down', and its commentary points to 2 Kgs 4:34-35. The shared entry `gahar-crouch-over-kings` makes the three sites uniform.
- **Alternative:** ASV 'stretched himself upon him'.

### I. 1 Kgs 8:50 'mercy' and 8:23 'kindness' (central entries applied over the ASV)

- **'mercy' (8:50):** 8:50 has the exact idiom of Gen 43:14 (*nāṯan raḥămîm lip̄nê*), where the corpus has 'mercy'. The ASV itself is inconsistent here ('compassion').
- **'kindness' (8:23):** Solitary *ḥeseḏ* is 'kindness' under the central entry, as at 1 Kgs 2:7 (wave B). 'keeping the covenant and the kindness' is less idiomatic than ASV 'lovingkindness' or NRSV 'steadfast love'.
- **Alternative:** Revert both to the ASV and record the central entries in commentary only.

### J. 'the Shomronites' (2 Kgs 17:29)

- **Decision:** The gentilic rule of wave B gives 'the Shomronites'. This avoids the ASV's anachronistic 'the Samaritans', because the word here means the Israelite inhabitants, not the later Samaritan community.
- **Alternatives:** The Translator's 'the Shomronim', or 'the people of Shomron'.

---

## Lens-discipline records (for the Reviewer)

1. **1 Kgs 8:12 *ʿărāp̄el*.** The canon's French says 'dans un nuage' and reads it as an orbiting craft. The Hebrew is *ʿărāp̄el* 'thick darkness', not *ʿānān*. Accuracy rules: the line keeps 'the thick darkness' (exodus-woh 20:18 precedent; new central `arafel-...`), and the commentary states the lexical difference explicitly.
2. **1 Kgs 8:10-11.** 'the cloud' and 'the glory of YHWH' (ASV). The new central `he-anan-...` entry ties the scene to Ex 40:34-35 and states that the line encodes neither a craft nor a natural phenomenon (cf. the disavowals of `pillar-of-cloud-...` and `sinai-theophany-...`).
3. **1 Kgs 6:13 / 8:12 *šāḵan*.** 'dwell' (consensus). 'in the midst of' (*bəṯôḵ*, literal; canon EN 'among') is the Translator's choice, and it matches Ex 25:8 / 29:45.
4. **2 Kgs 4:34-35.** No medical vocabulary is used. 'sneezed' (*zrr*, traditional sense; LXX alternative noted). The only line change ('crouched') is concordance-driven.
5. **2 Kgs 4:42-44.** ASV sense. *karmel* 'fresh ears of grain' and *ṣiqlôn* 'sack' are kept; the infinitives absolute are kept as 'They shall eat and have some left over'.
6. **'heavens' (point B)** is the less lens-congenial register and is corpus-consistent.
7. **Non-extensions.** These central entries are cited in commentary but deliberately not applied (their wohChoice does not govern the Kings line):
   - `elohim-aherim-other-gods-...`: the draft glossaryRefs at 2 Kgs 17:7, 35, 37, 38 are kept, as in wave A.
   - `hishtachavah-bow-down-obeisance-worship`: 'made obeisance' is not imported (2 Kgs 4:37; 17:16, 35, 36).
   - `pillar-of-cloud-...` and `sinai-theophany-...`: cross-referenced from `he-anan-...` only.
   - `house-like-the-gods-...`: 1 Kgs 8:13 comparative note.
   - `brit-shalom-mishkan`: cited in the `shakhan` rationale.
   - `minchah-shaah` / `minchah-tribute-...`: 8:64 'meal-offering'; 17:3 'tribute'.
   - `mishmeret-mitzvot-...`: the triads of 8:58 and 17:37 are not the fourfold formula.
   - `chamesh-esreh-amah`: cubits, commentary only.
   - `athirat-asherah-...`: Ugaritic vocalization; 'Asherim'/'Asherah' kept in English.
   - `adam-adamah`: the 'land' lines at 8:34, 40 and 17:23 do not match its 'the ground'.
   - `hevel`: the name Abel, not the *hebel* of 17:15.

---

## Unresolved editorial questions

**None.** All 84 are resolved as follows. "Draft kept" means the Translator's line is unchanged. "K/Q" means the Qere is translated, the Ketiv is recorded in commentary, and `ketiv-qere-qere-translated-kings` is extended.

### 1 Kings 6 (22)

| refId | Question | Resolution |
|---|---|---|
| 6:1 | MT 480 vs LXX 440 | MT kept; schematic 12×40 noted; MT-baseline entry |
| 6:1 | Ziv/Bul/Etanim; 'built' vs 'began to build' | Transliterated (names table, with later month names in commentary); plain 'built' kept, ingressive sense noted |
| 6:3 | *hêḵāl/dəḇîr/ʾûlām/qōḏeš haqqŏḏāšîm* | **Changed** to 'great hall' / 'inner sanctuary' (13 lines); new central `ulam-hekhal-devir-...` (point A) |
| 6:2 | *ʾammâ* | 'cubit(s)' kept; metric equivalents and royal cubit (2 Chr 3:3) in commentary; no entry (no divergence) |
| 6:4 | *ḥallônê šəqūp̄îm ʾăṭūmîm* | ASV kept; NRSV/NJPS/Busink alternatives noted |
| 6:5 | *yāṣîaʿ / ṣəlāʿôt*; 6:6 *miḡrāʿôṯ*; 6:10 subject | ASV 'stories' / 'side-chambers' kept; annex architecture explained |
| 6:8 | *lûllîm*; MT 'middle' vs LXX 'lowest' | 'winding stairs' kept, 'trapdoors/shafts' noted; MT kept (MT-baseline) |
| 6:11 | LXX lacks 6:11-14 | MT translated; MT-baseline; reception note at 6:13 |
| 6:13 | *šāḵan*; *bəṯôḵ* | 'dwell' / 'in the midst of' kept; new central `shakhan-...` |
| 6:15 | *bərôšîm*; walls/rafters; *ʿăṣê-šemen* | 'fir', 'olive-wood' (ASV) kept, Zohary and Neh 8:15 noted; MT 'walls' kept (MT-baseline) |
| 6:17 | *lip̄nāy* | ASV sense kept ('in front'); hêḵāl → 'great hall' |
| 6:20 | *lip̄nê haddəḇîr*; altar; *zāhāḇ sāḡûr* | ASV sense kept; MT 'covered' kept (LXX 'made', MT-baseline); 'pure gold' kept |
| 6:23 | cherubim | Central `cherubim-ezek` extended (11 refIds; its rationale already cites 1 Kgs 6:23-28) |
| 6:18 | knops / open flowers / palm-trees | **Changed** 'knops' → 'gourds'; overlay `peqaim-gourd-ornaments-1-kings-6`; others kept |
| 6:31 | 'fifth part' / 'fourth part' | ASV kept; pentagonal / recessed-frame alternatives recorded |
| 6:34 | MT *qəlāʿîm* | 'leaves' kept: BDB construes the MT so; no emendation (MT-baseline) |
| 6:5, 6, 10, 16, 21, 38 | K/Q (6 sites) | Qere; ASV follows the Ketiv at 6:38 (noted) |

### 1 Kings 8 (21)

| refId | Question | Resolution |
|---|---|---|
| 8:1 | LXX shorter 8:1-5 | MT; MT-baseline (8:1, 4, 5 noted) |
| 8:9 | Mosheh/Moses; Horeb | **Moshe** (wave-B form; 8:9, 53, 56); Horeb kept (names table) |
| 8:9 | elided *bərîṯ* | 'a covenant' supplied (BDB *kāraṯ* 1b ellipsis); central `karat-brit-cut-covenant` extended (8:9, 21; 2 Kgs 17:15, 35, 38) |
| 8:10 | the cloud | 'the cloud' kept; new central `he-anan-cloud-fills-the-sanctuary-cross-corpus`; reception note |
| 8:11 | *kəḇôḏ-YHWH* | Kept; central `kavod-yhwh` extended; reception note |
| 8:12 | *ʿărāp̄el* | 'thick darkness' kept; new central `arafel-...` (Ex 20:18 + 1 Kgs 8:12); reception note |
| 8:12 | LXX 8:53a | MT order/wording; 'book of the song' noted; MT-baseline |
| 8:13 | *bêṯ zəḇul*; *māḵôn ləšiḇtəḵā* | **Changed** to 'an exalted house' (point G); 'a place for you to dwell in forever' kept; *yāšaḇ*/*māḵôn* refrain explained |
| 8:15 | *ʾĕlōhê yiśrāʾēl* with 'Yisra'el' | Confirmed (wave-B practice); central `elohei-yisrael` extended; vocative 8:26 without article |
| 8:16 | LXX/Chr plus | MT (homoioteleuton noted); MT-baseline |
| 8:23 | *ʾên-kāmôḵā ʾĕlōhîm* | **Changed** to lower-case 'elohim' (point D); clause 5 of the elohim-referent entry |
| 8:23 | *ḥeseḏ* | **Changed** to 'kindness'; central `chesed-solitary-...` extended (point I) |
| 8:27 | *šāmayim* / *šəmê haššāmayim* | **Changed** to 'heavens' (point B); 8:35 keeps 'skies' |
| 8:31 | *ûḇāʾ ʾālâ* | ASV 'and he comes and swears' kept: *ʾālâ* is pointed identically as noun and Qal perfect, so it is a construal of the MT, not an emendation |
| 8:37 | 'land of his gates' | ASV 'land of their cities' kept (synecdoche); LXX noted; ASV crop/locust terms kept |
| 8:48 | *nap̄šām* | **Changed** to 'being' (wave B 2:4); nefesh entry |
| 8:50 | *raḥămîm* | **Changed** to 'mercy' (Gen 43:14 idiom); central `rachamim-...` extended (point I) |
| 8:63 | peace-offerings / meal-offering | ASV kept (exodus-woh 20:21 'peace-offerings'); central `olah` extended (8:64) |
| 8:65 | 14 vs 7 days; Lebo-Chamat; Brook | MT kept (MT-baseline); 'entrance of Chamat' kept, toponym reading noted; central `seven-day-banquet-...` extended (8:65-66) |
| 8:26, 8:48 | K/Q | Qere |

### 2 Kings 4 (21)

| refId | Question | Resolution |
|---|---|---|
| 4:7 | 'the man of the Elohim' | Confirmed: shared `ish-ha-elohim-...` extended (10 articular sites, anarthrous 4:9) |
| 4:12 | *naʿar* split; *məšārēt* | ASV split kept ('servant' / 'child'); 'attendant' for *məšārēt* kept; shared noun noted |
| 4:12 | Gechazi, Karmel, Shunem, Ba'al-Shalishah | Confirmed; names table; orthographic *gēḥăzî*/*gêḥăzî* noted |
| 4:13 | *śar haṣṣāḇāʾ* | 'captain of the host' kept (wave-B practice, 17:16 link) |
| 4:16 | *kāʿēṯ ḥayyâ* | Central `ka-et-chayah-time-of-life` extended (4:16, 17); its rationale already names 2 Kgs 4 |
| 4:23 | *šālôm* | ASV renderings kept; the single word recorded in commentary (vv 23, 26) |
| 4:27 | *nap̄šāh mārâ-lāh* | **Changed** to 'she is in bitter distress'; nefesh entry |
| 4:30 | *ḥay-YHWH wəḥê-nap̄šəḵā* | 'As YHWH lives' kept (central `chei-x-oath` extended); **changed** to 'as you yourself live' (as 2 Kgs 2:2, 4, 6) |
| 4:34 | *gāhar*, *zrr*, the walk | **Changed** to 'crouched over him' (point H); 'sneezed seven times' kept; plain sense; reception note |
| 4:37 | *wattištaḥû* | 'bowed herself' kept; `hishtachavah` not imported |
| 4:39 | botanical; *ʾāsûḵ* | ASV kept; colocynth and the *pqʿ* root link to 1 Kgs 6:18 noted |
| 4:42 | first-fruits, *karmel*, *ṣiqlôn*, infinitives | ASV sense kept; reception note |
| 4:2, 3, 5, 7 (×2), 16, 23 (×2), 34 | K/Q (9 readings) | Qere; archaic 2fs forms noted (Rendsburg 2002); 4:5 bracket cosmetics kept as delivered |

### 2 Kings 17 (20)

| refId | Question | Resolution |
|---|---|---|
| 17:1 | Name forms | Transliteration confirmed; **Shomeron → Shomron**; Mitzrayim; Par'oh; Madai; Kutah/Kut both kept; names table extended |
| 17:4 | So | 'So' kept; Osorkon IV / Sais noted |
| 17:7 | 'other elohim' | Confirmed (elohim-referent clause 4); `elohim-aherim` refs kept, not extended |
| 17:9 | *ḥpʾ*; *bāmôṯ* | 'did secretly', 'high places' kept |
| 17:10 | Asherim / Asherah; pillars; *gillûlîm* | ASV kept; central `matzevah-...` extended |
| 17:13 | *tôrâ* | 'law' kept; new shared `torah-law-deuteronomistic-kings` (point F) |
| 17:15 | *hebel* | ASV 'vanity ... vain' kept (paronomasia) |
| 17:16 | host / *hishtachavah* | **Changed** to 'host of the heavens' (point B; `tzeva-ha-shamayim` modify); 'worshipped' kept |
| 17:16 | *massēḵâ*; *habbaʿal* | 'molten images, two calves' kept (collective singular noted); **'Ba'al'** (Kings spelling) |
| 17:17 | *qsm* / *nḥš* | Draft kept; central `nichesh-laban-divination` gets the WoH refId (legacy '2KI-17:17' kept) |
| 17:21 | subject of *qāraʿ* | 'he tore' kept; links to wave-B *qrʿ* entry |
| 17:26 | 'the Elohim of the land'; *mišpāṭ* | Capital kept (referent rule); **'law' → 'manner'** (point E); new 2 Kings overlay `mishpat-manner-custom-2-kings-17` |
| 17:29 | Shomronim | **Changed** to 'the Shomronites' (point J) |
| 17:30 | deity names | Hebrew forms kept; names table extended with ASV equivalents |
| 17:32 | *ʿōśîm* | 'who sacrificed for them' kept (*ʿśh* 'offer', BDB) |
| 17:41 | *pəsîlîm* | Central `pesel-utemunah-...` extended |
| 17:13, 16, 21, 31 | K/Q | Qere; 17:31 bracket cosmetics kept as delivered |

---

## Glossary changes for review

### Per-translation overlays (`1-kings-woh/wave-cd-overlay-diff.json`, not applied)

The file is a JSON object with a `sections` map. Each section targets its overlay 1.1.0 → **1.2.0** (semver-minor: additions and additive extensions only).

- **Base:** each overlay at v1.0.0 plus the pending `wave-b-overlay-diff.json` (including its 2-kings-woh mirror section), which must be applied first.
- **Shared ops:** marked `shared: true` and repeated identically in both sections, so the shared entries stay identical.
- **op=extend:** append-only, so it applies on top of wave-B extensions and any wave-A Reviewer revision.

**Added (shared, both overlays):**

- `gahar-crouch-over-kings` (claim_type: `direct`): 1KI-WOH-18:42; 2KI-WOH-4:34, 35
- `torah-law-deuteronomistic-kings` (claim_type: `direct`): 1KI-WOH-2:3; 2KI-WOH-17:13, 34, 37

**Added (1-kings-woh only):**

- `peqaim-gourd-ornaments-1-kings-6` (claim_type: `direct`): 1 Kgs 6:18

**Added (2-kings-woh only):**

- `mishpat-manner-custom-2-kings-17` (claim_type: `direct`): 2 Kgs 17:26, 27, 33, 34, 37, 40

**Extended (shared, append-only):**

- `hebrew-proper-name-transliteration-convention-kings`: waves C-D equivalence table; tz applied to Mitzrayim/Tziyyon with the corpus conflict recorded; Par'oh; Shomronites. appliesTo + every wave-C/D verse with a transliterated name.
- `elohim-referent-and-article-conventions-kings`: sites under clauses 1-4 and new **clause 5** (generic class in comparison, 1 Kgs 8:23), plus rationale.
- `ish-ha-elohim-man-of-the-elohim-prophetic-title-kings`: 2 Kgs 4 (9 verses).
- `nefesh-scope-and-spelling-kings`: 1 Kgs 8:48; 2 Kgs 4:27, 30, plus rationale.
- `ketiv-qere-qere-translated-kings`: 21 readings in 19 verses, plus rationale (ASV Ketiv at 6:38; archaic 2fs; bracket cosmetics).
- `mt-baseline-at-versional-cruxes-and-versification-kings`: 1 Kgs 6 and 8 cruxes and LXX pluses/minuses; 2 Kgs 17:27.
- `habbaal-baal-hebrew-bible-rendering-kings`: 2 Kgs 17:16.

**Extended (2-kings-woh only):** `bene-ha-neviim-sons-of-the-prophets-kings`: 2 Kgs 4:1, 38 (appliesTo only).

**Not extended:** `ruach-yhwh-...` and `yhwh-tsevaot-...` (no occurrences); the 1 Kings wave-A/B single-text entries.

### Central glossary (`1-kings-woh/wave-cd-central-diff.json`, not applied)

The file uses the same format as `wave-a-central-diff.json`: a JSON list whose first element is `{"op":"version","from":"2.79.0","to":"2.80.0", ...}`, with a ready-to-paste `scopeNoteAddendum`.

- **Base:** 2.77.0 + wave-A diff + wave-B diff, applied in that order. appliesTo arrays start from the latest pending array (wave B, else wave A, else 2.77.0).
- **Version recommendation: 2.80.0** (minor). The diff has additions and appliesTo extensions. The one modification is of an entry that is itself still pending (wave-B `tzeva-ha-shamayim`), and it resolves an explicitly open sentence rather than reversing a decision.

**Added:**

- `ulam-hekhal-devir-temple-three-room-plan-cross-corpus` (claim_type: `direct`): 1 Kgs 6:3-33; 8:6, 8, 10 (15 refIds)
- `shakhan-dwell-divine-presence-verb-cross-corpus` (claim_type: `direct`): 1 Kgs 6:13; 8:12 (canon-cited)
- `arafel-thick-darkness-divine-presence-cross-corpus` (claim_type: `direct`): EXO-WOH-20:18; 1 Kgs 8:12 (canon-cited)
- `beit-zevul-exalted-house-1-kgs-8-13-cross-corpus` (claim_type: `direct`): 1 Kgs 8:13 (canon-cited)
- `he-anan-cloud-fills-the-sanctuary-cross-corpus` (claim_type: `direct`): 1 Kgs 8:10, 11 (canon-cited)

**Modified:**

- `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus` (pending wave-B entry):
  - wohChoice: appended (astral sense).
  - rationale: the sentence "In the astral sense ... later passes may use 'skies'; that choice is left to them." is replaced by the decision to keep one rendering for both senses.
  - appliesTo: + 2KI-WOH-17:16.

**Modified (appliesTo only; 24 entries):**

- Formulas: `karat-brit-cut-covenant`, `ka-et-chayah-time-of-life`, `chei-x-oath-by-the-life-formula`, `davar-yhwh-prophetic-formula`, `elohim-imkha-divine-presence-formula`, `hithallekh-lefanai-...`, `ad-ha-yom-ha-zeh-aetiological-formula`, `seven-day-banquet-...`
- Lexemes:
  - `cherubim-ezek`, `kavod-yhwh`, `elohei-yisrael`, `olah-burnt-offering`, `navi-first-occurrence-abraham`, `malakh-yhwh-messenger`, `matzevah-...`, `pesel-utemunah-...`, `nichesh-laban-divination`, `eretz`
  - `shamayim`: 1 Kgs 8 under the numinous clause, 8:35 under 'skies'; 2 Kgs 17:16.
  - `rachamim-compassion-womb-root`: line now 'mercy'.
  - `chesed-solitary-covenant-kindness`: line now 'kindness'.
- Names: `adonai-yhwh-divine-name`, `har-sinai-horev-...`, `bethel-luz-name-etymology`

**Dependencies:**

- If none of the pending diffs are applied, the chapters cite these entries that do not yet exist:
  - 5 new central entries.
  - `tzeva-ha-shamayim-...` (wave B).
  - 4 new overlay entries.
- The `elohim-referent` clause 5 text arrives only with this overlay diff.

---

## Notes for the Reviewer and orchestrator

### Follow-ups touching read-only files (not done)

1. Add `gahar-crouch-over-kings` to `glossaryRefs` of 1KI-WOH-18:42 (wave A) when the overlay diff is applied.
2. Add `torah-law-deuteronomistic-kings` to `glossaryRefs` of 1KI-WOH-2:3 (wave B) when the overlay diff is applied.
3. Corpus 'Mitsrayim' / 'Mitzrayim' normalization (point C).

### Other notes

- **Hosted ASV errors:** The hosted ASV edition (`data-library/1-kings`) misreads 8:15 ('thy father') and 8:43 ('my name'). This was already flagged by wave A, and the commentary at both verses notes the MT reading.
- **Text-field cosmetics:** At 2 Kgs 4:5 and 17:31, the Hebrew `text` field has the sof pasuq inside the bracketed Qere. This is identical to `source-he-*.json` (Sefaria encoding) and is left untouched, so the text stays identical to the source. If the renderer should show it outside the bracket, that is a pipeline-wide display fix, not a per-verse edit.
- **Chapter titles:** The wave-A recommendation to add English forms to titles ('Eliyahu (Elijah)') was not applied here, as in wave B. The only title change is 'Shomeron' → 'Shomron'.
- **Authorities cited:**
  - Kings commentaries: Cogan, *1 Kings* (AB 10, 2001); Cogan and Tadmor, *II Kings* (AB 11, 1988); Gray (OTL); Noth; Burney (1903)
  - Lexica and grammars: BDB, HALOT, DCH, GKC
  - Temple and archaeology: Busink 1970; Monson, *BAR* 26/3 (2000); King and Stager 2001
  - Theology: Mettinger 1982; Cross 1973; Weinfeld 1972; von Rad 1953; Wolff 1974
  - Botany and language: Zohary 1982; Rendsburg 2002
  - Assyrian period and Egypt: Thiele 1983; Tadmor, *JCS* 12 (1958); Becking 1992; Kitchen 1973; Goedicke, *BASOR* 171 (1963); Cogan, *Imperialism and Religion* (1974)
  - Inscriptions: KAI 14:1 (Bul)
- **Claims worth spot-checking:** Page numbers are omitted throughout. Recommended checks:
  - NJPS 'Great Hall' / 'stately House' / 'thick cloud' at 1 Kgs 6:3; 8:12-13.
  - The LXX 8:53a wording.
  - The LXX rendering of 2 Kgs 4:35.
  - The Aquila/Symmachus *chrēmatistērion* for *dəḇîr*.
- **Verse numbering:** MT = ASV throughout waves C-D. No versification divergence.
- **Masoretic section marks** are noted where structurally relevant (6:10, 13; 8:11, 21, 32-36, 53; 2 Kgs 4:7, 37, 41, 44; 17:6, 23, 41).


---

## Reviewer report (non-approve verdicts and report fields)

### 1 Kings 6 — Shelomoh (Solomon) builds the house for YHWH

- **1KI-WOH-6:1** — revise: Re-parsed: bišmônîm šānâ wəʾarbaʿ mēʾôṯ šānâ ... wayyiḇen habbayiṯ; 'that he built' keeps the plain wayyiqtol (ASV 'began to build' interprets by 6:37-38), and the long Hebrew word order of the date is kept, so the English line is approved. Commentary fix only: the LXX does not 'place the verse after its additional material at 5:32'; it gives 6:1 (with 440) and then 6:1a-d, which carry the material of MT 5:31-32 and 6:37-38. Rephrase the note and the matching mt-baseline wohChoice clause.
- **1KI-WOH-6:20** — revise: The Hebrew wəlip̄nê haddəḇîr ʿeśrîm ʾammâ ʾōreḵ ... is a nominal clause whose subject is the interior space (the ASV supplies '[a space of]'); the line drops that supply and reads 'And within the inner sanctuary was twenty cubits in length ... and twenty cubits its height', which is not grammatical English and mixes two constructions. Proposed line, following the note's own explanation of pənê as 'interior': 'And the interior of the inner sanctuary was twenty cubits in length, and twenty cubits in breadth, and twenty cubits in height; and he overlaid it with pure gold; and he covered the altar with cedar.' Altar note (LXX 'made an altar') is correct.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T11:36:30Z"
- glossaryReview: [{"glossary_id": "ulam-hekhal-devir-temple-three-room-plan-cross-corpus", "layer": "central add (direct)", "status": "flag-for-human", "citations": ["HALOT s.v. hêḵāl; s.v. dəḇîr", "NJPS 1 Kgs 6:3 (\"Great Hall\"); NRSV 1 Kgs 6:5, 16 (\"inner sanctuary\")", "Cogan, I Kings (AB 10; 2001), ad loc.", "Monson, BAR 26/3 (2000)"], "reasoning": "Philologically sound and correctly direct: hêḵāl < Sumerian é.gal via Akkadian ekallu, dəḇîr 'back room', the dbr 'speak' > 'oracle' derivation (Aquila/Symmachus chrēmatistērion, Vulgate oraculum) rejected by modern lexica; the context clause for hêḵāl = whole temple/palace is necessary and present. Reviewer verified NJPS 'Great Hall' but could not verify the attribution to Alter; drop 'Alter' or confirm it. Flagged only because it is founder point A and a corpus-wide central rendering; reviewer recommends ratifying."}, {"glossary_id": "shakhan-dwell-divine-presence-verb-cross-corpus", "layer": "central add (direct)", "status": "approve", "citations": ["BDB s.v. šāḵan", "HALOT s.v. šāḵan", "Ex 25:8; 29:45 (MT)"], "reasoning": "Consensus rendering 'dwell'; the entry is an audit hub for two canon-cited sites and states that the line does not encode the canon's residence reading. Direct is correct."}, {"glossary_id": "cherubim-ezek", "layer": "central appliesTo extension", "status": "approve", "citations": [], "reasoning": "Superset verified; the rationale already cites 1 Kgs 6:23-28."}, {"glossary_id": "davar-yhwh-prophetic-formula", "layer": 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 38 English lines: no lens leakage. bayiṯ 'house', šāḵan 'dwell' and bəṯôḵ 'in the midst of' (6:13) render the Hebrew lexically; 'great hall', 'inner sanctuary' and 'gourds' are lexical corrections of the ASV with no interpretive content. The canon's 'sumptuous residence to receive the creators' (TBWTT 3:103) and its 6:13 quotation (3:106), both verified in data-library, are confined to labelled reception notes at 6:1 and 6:13."
- quotationCheck: "Double quotes balanced: one speech 6:12-13."
- ketivQereInventory: "Bracketed Ketiv/Qere in the source: 22 readings in 19 verses (1 Kgs 6:5, 6, 10, 16, 21, 38; 8:26, 48; 2 Kgs 4:2, 3, 5, 7 x2, 16, 23 x2, 34; 17:13, 16, 21, 31 x2). The Qere is translated at every site. The Editor's '21' counts 17:31 as one reading."
- nonBlockingFixes: ["6:1 note: rephrase the LXX ordering (see 6:1 verdict).", "6:3 / central ulam entry: confirm or drop 'Alter' as a source for 'great hall' (NJPS confirmed).", "6:1 English: the date phrase '..., in the month of Ziv, which is the second month, of Shelomoh's reign over Yisra'el' follows the Hebrew order; optional smoothing 'in the fourth year of Shelomoh's reign over Yisra'el, in the month of Ziv, which is the second month' (ASV order)."]
- asvEditionErrors: ["1 Kgs 8:15: hosted ASV 'thy father'; ASV 1901 and MT read 'my father' (known).", "1 Kgs 8:43: hosted ASV 'is called by my name'; ASV 1901 and MT read 'thy name' (known).", "2 Kgs 17:34 (probable, verify against a printed ASV 1901): hosted ASV 'after the former manner'; the ASV, following the KJV, reads 'the former manners' (MT plural kammišpāṭîm hāriʾšōnîm).", "2 Kgs 4:25: formatting artifact, a run of five spaces inside the verse ('mount Carmel.     And it came to pass').", "Throughout (e.g. 1 Kgs 6:1 'Solomon`s', 8:1 'fathers`', 8:41 'name`s', 2 Kgs 17:41 'children`s'): backtick for apostrophe, an encoding artifact of the hosted edition.", "1 Kgs 8:50: hosted ASV ends without the verse-final semicolon (trivial)."]
- escalationReportAdjustments: "Initial verdicts on all 189 verses, 15 overlay ops and 30 central ops were formed from the chapters, the MT source, the ASV, the glossaries and the diffs, with mechanical checks (Hebrew text identical to source-he-*.json in every paragraph; bracketed Qere inventory; glossaryRefs resolution against central 2.78.0 + wave-B + wave-C/D and both overlays; appliesTo superset check of every central modify op against 2.78.0 + wave-B; double-quote balance; genesis-woh / exodus-woh / signed-off Kings lines for every cross-reference). Only then was wave-cd-editor-report.md read. No verdict changed. The report added three things the reviewer recorded: (1) its genesis-woh count ('Mitsrayim' 206x, 'Mitzrayim' 18x) does not match the English lines (81 / 0; the 8 'Mitzrayim' are in notes), corrected in the names-entry review and founder point C; (2) its 'Other notes' bullet says English forms were not added to chapter titles, but the files carry 'Shelomoh (Solomon)' and 'Shomron (Samaria) ... Yisra'el (Israel)' as its own 'Chapter titles' section says, so that bullet is stale; (3) its founder lettering (A, C-J) is used in the recommendations, with B confirmed as settled. The report's spot-check list was checked: NJPS 'Great Hall' / 'stately House' / 'thick cloud' confirmed; LXX 8:53a and LXX 4 Kgdms 4:35 descriptions confirmed; Aquila/Symmachus chrēmatistērion for dəḇîr confirmed."
- founderDecisionRecommendations: {"A-temple-rooms": "Ratify 'porch' / 'great hall' / 'inner sanctuary' / 'the most holy place', with the context clause (hêḵāl = 'temple'/'palace' for a whole building). 'Oracle' rests on a rejected etymology and 'the temple of the house' (6:3) misleads in a chapter where the building is the 'house'. Confirm or drop the 'Alter' attribution in the central entry.", "C-Mitzrayim-vs-Mitsrayim": "Keep Kings on 'Mitzrayim' (the tz rule ratified at wave A covers Tzidon, Tzarfat, Tzadoq; Kings would be internally inconsistent otherwise). Corpus facts: genesis-woh English lines read 'Mitsrayim' 81x and 'Mitzrayim' 0x (8 'Mitzrayim' only in notes); exodus-woh lines 'Mitsrayim' 38x. The report's '206 / 18' and the overlay's '(mostly)' overstate the mix. If one corpus spelling is wanted, normalize genesis-woh/exodus-woh to 'Mitzrayim' in a separate mechanical pass rather than making Kings an exception to its own tsade rule.", "D-8:23-lower-case-elohim": "Ratify clause 5. In ʾên-kāmôḵā ʾĕlōhîm the noun is the class compared, so a capital would make YHWH be compared with himself; the commentary keeps the monotheistic and incomparability readings open. This is consistent with 'there is no Elohim in Yisra'el' (2 Kgs 1:3), where the referent is YHWH.", "E-17:26-27-manner-and-Elohim-of-the-land": "Ratify both. 'Manner' is an attested sense of mišpāṭ (KJV throughout vv 26-40) and keeps the keyword concordant while reserving 'law' for tôrâ. The capital follows the referent rule with the narrator'
- summary: "38 verdicts: 36 approve, 2 revise, 0 flag-for-human (6:1 revise; 6:20 revise). Glossary ops relevant to this chapter: 9 (5 approve, 2 revise, 2 flag-for-human). No lens leakage. Flags are founder-confirmation points only (A, C-J); the reviewer recommends ratifying all of them. Status awaiting-human."

### 1 Kings 8 — The ark brought in, the cloud fills the house, the prayer of Shelomoh (Solomon)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T11:36:30Z"
- glossaryReview: [{"glossary_id": "ulam-hekhal-devir-temple-three-room-plan-cross-corpus", "layer": "central add (direct)", "status": "flag-for-human", "citations": ["HALOT s.v. hêḵāl; s.v. dəḇîr", "NJPS 1 Kgs 6:3 (\"Great Hall\"); NRSV 1 Kgs 6:5, 16 (\"inner sanctuary\")", "Cogan, I Kings (AB 10; 2001), ad loc.", "Monson, BAR 26/3 (2000)"], "reasoning": "Philologically sound and correctly direct: hêḵāl < Sumerian é.gal via Akkadian ekallu, dəḇîr 'back room', the dbr 'speak' > 'oracle' derivation (Aquila/Symmachus chrēmatistērion, Vulgate oraculum) rejected by modern lexica; the context clause for hêḵāl = whole temple/palace is necessary and present. Reviewer verified NJPS 'Great Hall' but could not verify the attribution to Alter; drop 'Alter' or confirm it. Flagged only because it is founder point A and a corpus-wide central rendering; reviewer recommends ratifying."}, {"glossary_id": "shakhan-dwell-divine-presence-verb-cross-corpus", "layer": "central add (direct)", "status": "approve", "citations": ["BDB s.v. šāḵan", "HALOT s.v. šāḵan", "Ex 25:8; 29:45 (MT)"], "reasoning": "Consensus rendering 'dwell'; the entry is an audit hub for two canon-cited sites and states that the line does not encode the canon's residence reading. Direct is correct."}, {"glossary_id": "arafel-thick-darkness-divine-presence-cross-corpus", "layer": "central add (direct)", "status": "approve", "citations": ["BDB s.v. ʿărāp̄el", "HALOT s.v. ʿărāp̄el", "EXO-WOH-20:18 (verified \"the thick darkness\")"], "reasoning": 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 66 English lines: no lens leakage. 8:10-11 'the cloud' and 'the glory of YHWH' as in all versions; 8:12 keeps 'the thick darkness' for ʿărāp̄el and declines the canon's French 'dans un nuage' (TBWTT 3:104, verified), the lens-congenial option; 8:13 'an exalted house' is the lexical consensus and is neutral toward the canon's residence reading. 'heavens' at the divine-dwelling sites is the less lens-congenial register. All canon material (3:103-107, verified) is in labelled reception notes at 8:10, 11, 12, 13."
- quotationCheck: "Double quotes balanced: 8:12-13, 8:15-21, 8:23-53, 8:56-61; single-quote nesting at 8:16, 18-19, 25, 29, 47 correct."
- ketivQereInventory: "Bracketed Ketiv/Qere in the source: 22 readings in 19 verses (1 Kgs 6:5, 6, 10, 16, 21, 38; 8:26, 48; 2 Kgs 4:2, 3, 5, 7 x2, 16, 23 x2, 34; 17:13, 16, 21, 31 x2). The Qere is translated at every site. The Editor's '21' counts 17:31 as one reading."
- nonBlockingFixes: ["8:9 note and karat-brit reason line: check the BDB sub-section '1b' for the ellipsis of bərîṯ.", "8:35 note: 'some versions read \"because you answer them\"' is Targumic; say 'the Targum' or 'some interpreters'.", "Central kavod-yhwh op: merge, do not replace, if EXO-WOH-16:7, 10 have been added by a separate pending exodus-woh diff."]
- asvEditionErrors: ["1 Kgs 8:15: hosted ASV 'thy father'; ASV 1901 and MT read 'my father' (known).", "1 Kgs 8:43: hosted ASV 'is called by my name'; ASV 1901 and MT read 'thy name' (known).", "2 Kgs 17:34 (probable, verify against a printed ASV 1901): hosted ASV 'after the former manner'; the ASV, following the KJV, reads 'the former manners' (MT plural kammišpāṭîm hāriʾšōnîm).", "2 Kgs 4:25: formatting artifact, a run of five spaces inside the verse ('mount Carmel.     And it came to pass').", "Throughout (e.g. 1 Kgs 6:1 'Solomon`s', 8:1 'fathers`', 8:41 'name`s', 2 Kgs 17:41 'children`s'): backtick for apostrophe, an encoding artifact of the hosted edition.", "1 Kgs 8:50: hosted ASV ends without the verse-final semicolon (trivial)."]
- escalationReportAdjustments: "Initial verdicts on all 189 verses, 15 overlay ops and 30 central ops were formed from the chapters, the MT source, the ASV, the glossaries and the diffs, with mechanical checks (Hebrew text identical to source-he-*.json in every paragraph; bracketed Qere inventory; glossaryRefs resolution against central 2.78.0 + wave-B + wave-C/D and both overlays; appliesTo superset check of every central modify op against 2.78.0 + wave-B; double-quote balance; genesis-woh / exodus-woh / signed-off Kings lines for every cross-reference). Only then was wave-cd-editor-report.md read. No verdict changed. The report added three things the reviewer recorded: (1) its genesis-woh count ('Mitsrayim' 206x, 'Mitzrayim' 18x) does not match the English lines (81 / 0; the 8 'Mitzrayim' are in notes), corrected in the names-entry review and founder point C; (2) its 'Other notes' bullet says English forms were not added to chapter titles, but the files carry 'Shelomoh (Solomon)' and 'Shomron (Samaria) ... Yisra'el (Israel)' as its own 'Chapter titles' section says, so that bullet is stale; (3) its founder lettering (A, C-J) is used in the recommendations, with B confirmed as settled. The report's spot-check list was checked: NJPS 'Great Hall' / 'stately House' / 'thick cloud' confirmed; LXX 8:53a and LXX 4 Kgdms 4:35 descriptions confirmed; Aquila/Symmachus chrēmatistērion for dəḇîr confirmed."
- founderDecisionRecommendations: {"A-temple-rooms": "Ratify 'porch' / 'great hall' / 'inner sanctuary' / 'the most holy place', with the context clause (hêḵāl = 'temple'/'palace' for a whole building). 'Oracle' rests on a rejected etymology and 'the temple of the house' (6:3) misleads in a chapter where the building is the 'house'. Confirm or drop the 'Alter' attribution in the central entry.", "C-Mitzrayim-vs-Mitsrayim": "Keep Kings on 'Mitzrayim' (the tz rule ratified at wave A covers Tzidon, Tzarfat, Tzadoq; Kings would be internally inconsistent otherwise). Corpus facts: genesis-woh English lines read 'Mitsrayim' 81x and 'Mitzrayim' 0x (8 'Mitzrayim' only in notes); exodus-woh lines 'Mitsrayim' 38x. The report's '206 / 18' and the overlay's '(mostly)' overstate the mix. If one corpus spelling is wanted, normalize genesis-woh/exodus-woh to 'Mitzrayim' in a separate mechanical pass rather than making Kings an exception to its own tsade rule.", "D-8:23-lower-case-elohim": "Ratify clause 5. In ʾên-kāmôḵā ʾĕlōhîm the noun is the class compared, so a capital would make YHWH be compared with himself; the commentary keeps the monotheistic and incomparability readings open. This is consistent with 'there is no Elohim in Yisra'el' (2 Kgs 1:3), where the referent is YHWH.", "E-17:26-27-manner-and-Elohim-of-the-land": "Ratify both. 'Manner' is an attested sense of mišpāṭ (KJV throughout vv 26-40) and keeps the keyword concordant while reserving 'law' for tôrâ. The capital follows the referent rule with the narrator'
- summary: "66 verdicts: 66 approve, 0 revise, 0 flag-for-human. Glossary ops relevant to this chapter: 25 (19 approve, 2 revise, 4 flag-for-human). No lens leakage. Flags are founder-confirmation points only (A, C-J); the reviewer recommends ratifying all of them. Status awaiting-human."

### 2 Kings 4 — Elisha: the widow's oil, the Shunammite's son raised, the pot and the twenty loaves

- **2KI-WOH-4:38** — revise: Line approved: 'boil stew' renders nāzîḏ accurately (modern versions 'stew'). Commentary fix: the note says 'nāzîḏ "stew" (as Gen 25:29)', but genesis-woh prints 'pottage' at Gen 25:29, so the cross-reference implies a concordance that does not exist. Either change the note to 'nāzîḏ "stew" (Gen 25:29, where genesis-woh keeps the ASV "pottage")', or, if concordance is wanted, render 'pottage' at 4:38, 39, 40; the reviewer recommends the first (the Kings pass already replaces archaic ASV words, e.g. 'knops').

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T11:36:30Z"
- glossaryReview: [{"glossary_id": "ka-et-chayah-time-of-life", "layer": "central appliesTo extension", "status": "approve", "citations": ["GEN-WOH-18:10, 14 (verified)"], "reasoning": "The rationale names 2 Kgs 4:16-17; line wording identical to genesis-woh."}, {"glossary_id": "chei-x-oath-by-the-life-formula", "layer": "central appliesTo extension", "status": "approve", "citations": [], "reasoning": "Superset verified; 'As YHWH lives' at 4:30."}, {"glossary_id": "navi-first-occurrence-abraham", "layer": "central appliesTo extension", "status": "approve", "citations": [], "reasoning": "Superset verified; 'prophet(s)' at 2 Kgs 4:1, 38; 17:13, 23."}, {"glossary_id": "eretz", "layer": "central appliesTo extension", "status": "approve", "citations": [], "reasoning": "Superset verified; only the 'land' sites are added and the cosmic-merism 'earth' sites (8:23, 27, 43, 53, 60) are correctly excluded."}, {"glossary_id": "gahar-crouch-over-kings", "layer": "overlay add, shared (direct)", "status": "approve", "citations": ["HALOT s.v. gāhar", "BDB s.v. gāhar", "1KI-WOH-18:42 (wave A, verified \"crouched down\")"], "reasoning": "Three occurrences, all in Kings; 'bend down, crouch' is the lexical sense, and uniform rendering is a concordance decision with no interpretive content. Direct is correct (founder point H: reviewer recommends keeping)."}, {"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "layer": "overlay extend, shared", "status": "flag-for-human", "citations": ["genesis-w
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 44 English lines: no lens leakage. 4:32-37 render the Hebrew plainly ('mouth on his mouth', 'crouched over him', 'sneezed seven times') with no medical vocabulary, and the death is stated without softening; 4:42-44 keep the ASV sense. The canon's resuscitation and dehydrated-food readings (TBWTT 3:134, 3:136-139, verified) are confined to labelled reception notes at 4:34 and 4:42."
- quotationCheck: "Double quotes balanced (76 marks); single-quote nesting at 4:13, 26, 28, 43 correct; speeches spanning 4:3-4 and 4:25-26 opened and closed once."
- ketivQereInventory: "Bracketed Ketiv/Qere in the source: 22 readings in 19 verses (1 Kgs 6:5, 6, 10, 16, 21, 38; 8:26, 48; 2 Kgs 4:2, 3, 5, 7 x2, 16, 23 x2, 34; 17:13, 16, 21, 31 x2). The Qere is translated at every site. The Editor's '21' counts 17:31 as one reading."
- nonBlockingFixes: ["4:31: concordance with signed-off 1 Kgs 18:29 ('no one paying heed'), or say in the note that 18:29 is rendered differently.", "4:39 note: label `peqaim-gourd-ornaments-1-kings-6` as a 1-kings-woh overlay entry (or make the entry shared).", "4:8 note: Shunem to el-Muhraqa is about 25-30 km."]
- asvEditionErrors: ["1 Kgs 8:15: hosted ASV 'thy father'; ASV 1901 and MT read 'my father' (known).", "1 Kgs 8:43: hosted ASV 'is called by my name'; ASV 1901 and MT read 'thy name' (known).", "2 Kgs 17:34 (probable, verify against a printed ASV 1901): hosted ASV 'after the former manner'; the ASV, following the KJV, reads 'the former manners' (MT plural kammišpāṭîm hāriʾšōnîm).", "2 Kgs 4:25: formatting artifact, a run of five spaces inside the verse ('mount Carmel.     And it came to pass').", "Throughout (e.g. 1 Kgs 6:1 'Solomon`s', 8:1 'fathers`', 8:41 'name`s', 2 Kgs 17:41 'children`s'): backtick for apostrophe, an encoding artifact of the hosted edition.", "1 Kgs 8:50: hosted ASV ends without the verse-final semicolon (trivial)."]
- escalationReportAdjustments: "Initial verdicts on all 189 verses, 15 overlay ops and 30 central ops were formed from the chapters, the MT source, the ASV, the glossaries and the diffs, with mechanical checks (Hebrew text identical to source-he-*.json in every paragraph; bracketed Qere inventory; glossaryRefs resolution against central 2.78.0 + wave-B + wave-C/D and both overlays; appliesTo superset check of every central modify op against 2.78.0 + wave-B; double-quote balance; genesis-woh / exodus-woh / signed-off Kings lines for every cross-reference). Only then was wave-cd-editor-report.md read. No verdict changed. The report added three things the reviewer recorded: (1) its genesis-woh count ('Mitsrayim' 206x, 'Mitzrayim' 18x) does not match the English lines (81 / 0; the 8 'Mitzrayim' are in notes), corrected in the names-entry review and founder point C; (2) its 'Other notes' bullet says English forms were not added to chapter titles, but the files carry 'Shelomoh (Solomon)' and 'Shomron (Samaria) ... Yisra'el (Israel)' as its own 'Chapter titles' section says, so that bullet is stale; (3) its founder lettering (A, C-J) is used in the recommendations, with B confirmed as settled. The report's spot-check list was checked: NJPS 'Great Hall' / 'stately House' / 'thick cloud' confirmed; LXX 8:53a and LXX 4 Kgdms 4:35 descriptions confirmed; Aquila/Symmachus chrēmatistērion for dəḇîr confirmed."
- founderDecisionRecommendations: {"A-temple-rooms": "Ratify 'porch' / 'great hall' / 'inner sanctuary' / 'the most holy place', with the context clause (hêḵāl = 'temple'/'palace' for a whole building). 'Oracle' rests on a rejected etymology and 'the temple of the house' (6:3) misleads in a chapter where the building is the 'house'. Confirm or drop the 'Alter' attribution in the central entry.", "C-Mitzrayim-vs-Mitsrayim": "Keep Kings on 'Mitzrayim' (the tz rule ratified at wave A covers Tzidon, Tzarfat, Tzadoq; Kings would be internally inconsistent otherwise). Corpus facts: genesis-woh English lines read 'Mitsrayim' 81x and 'Mitzrayim' 0x (8 'Mitzrayim' only in notes); exodus-woh lines 'Mitsrayim' 38x. The report's '206 / 18' and the overlay's '(mostly)' overstate the mix. If one corpus spelling is wanted, normalize genesis-woh/exodus-woh to 'Mitzrayim' in a separate mechanical pass rather than making Kings an exception to its own tsade rule.", "D-8:23-lower-case-elohim": "Ratify clause 5. In ʾên-kāmôḵā ʾĕlōhîm the noun is the class compared, so a capital would make YHWH be compared with himself; the commentary keeps the monotheistic and incomparability readings open. This is consistent with 'there is no Elohim in Yisra'el' (2 Kgs 1:3), where the referent is YHWH.", "E-17:26-27-manner-and-Elohim-of-the-land": "Ratify both. 'Manner' is an attested sense of mišpāṭ (KJV throughout vv 26-40) and keeps the keyword concordant while reserving 'law' for tôrâ. The capital follows the referent rule with the narrator'
- summary: "44 verdicts: 43 approve, 1 revise, 0 flag-for-human (4:38 revise). Glossary ops relevant to this chapter: 10 (8 approve, 1 revise, 1 flag-for-human). No lens leakage. Flags are founder-confirmation points only (A, C-J); the reviewer recommends ratifying all of them. Status awaiting-human."

### 2 Kings 17 — The fall of Shomron (Samaria) and the exile of Yisra'el (Israel)

- **2KI-WOH-17:4** — revise: The So note is accurate. English-line fix: 'and had not brought up tribute to the king of Ashur as year by year' is a calque of kəšānâ bəšānâ that is not English; propose 'and had not brought up tribute to the king of Ashur as he had year by year' (cf. ASV 'as he had done year by year'), which supplies only what the comparative kə- implies.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T11:36:30Z"
- glossaryReview: [{"glossary_id": "tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus", "layer": "central modify (pending wave-B entry)", "status": "approve", "citations": ["BDB s.v. ṣāḇāʾ", "Mullen, The Divine Council in Canaanite and Early Hebrew Literature (1980)", "Handy, Among the Host of Heaven (1994)"], "reasoning": "Resolves the wave-B open sentence in favour of one English form for both senses, under the ratified register rule; the appliesTo array is a verified superset of the wave-B array. The astral sense is stated in commentary at 2 Kgs 17:16, so nothing is hidden. Approve."}, {"glossary_id": "shamayim", "layer": "central appliesTo extension", "status": "approve", "citations": ["BDB s.v. šāmayim", "wave-A sign-off decision B (2026-11-01)"], "reasoning": "Verified superset of the wave-B array. The twelve 1 Kgs 8 divine-dwelling sites take 'heavens' under the numinous clause (the entry's own rationale cites 8:30), 8:35 keeps 'skies' (rain), and 17:16 'heavens' follows the tzeva entry. Consistent with the ratified rule."}, {"glossary_id": "karat-brit-cut-covenant", "layer": "central appliesTo extension", "status": "approve", "citations": ["BDB s.v. kāraṯ"], "reasoning": "Superset verified; 'cut' at 8:9, 21; 17:15, 35, 38. The '1b' sub-section locator for the ellipsis in the reason line should be checked."}, {"glossary_id": "ad-ha-yom-ha-zeh-aetiological-formula", "layer": "central appliesTo extension", "status": "approve", "citations": [], "reasoning": "Superset verifi
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 41 English lines: no lens leakage. 17:16 'molten images' and 'the host of the heavens' are the ASV sense (no 'metal', no fleet); 17:23 follows the ASV. The canon's 'metal idols' summary (TBWTT 3:140) and its 17:23 quotation (3:141), both verified, are confined to labelled reception notes at 17:16 and 17:23. The capital 'Elohim of the land' (17:26-27) is a case convention by referent, not a lens choice."
- quotationCheck: "Double quotes balanced: 17:12, 13, 26, 27, 35-39."
- ketivQereInventory: "Bracketed Ketiv/Qere in the source: 22 readings in 19 verses (1 Kgs 6:5, 6, 10, 16, 21, 38; 8:26, 48; 2 Kgs 4:2, 3, 5, 7 x2, 16, 23 x2, 34; 17:13, 16, 21, 31 x2). The Qere is translated at every site. The Editor's '21' counts 17:31 as one reading."
- nonBlockingFixes: ["17:21 note: label `niqra-ha-mizbeach-the-altar-torn-1-kings-13` as a 1-kings-woh overlay entry.", "17:31 note: present the Ketiv/Qere as two readings (ʾlh → ʾĕlōhê; sprym → səp̄arwāyim).", "17:17: 'practised divination and divined' repeats the root in English; acceptable under the central nichesh entry, optional 'and sought omens' for nḥš."]
- asvEditionErrors: ["1 Kgs 8:15: hosted ASV 'thy father'; ASV 1901 and MT read 'my father' (known).", "1 Kgs 8:43: hosted ASV 'is called by my name'; ASV 1901 and MT read 'thy name' (known).", "2 Kgs 17:34 (probable, verify against a printed ASV 1901): hosted ASV 'after the former manner'; the ASV, following the KJV, reads 'the former manners' (MT plural kammišpāṭîm hāriʾšōnîm).", "2 Kgs 4:25: formatting artifact, a run of five spaces inside the verse ('mount Carmel.     And it came to pass').", "Throughout (e.g. 1 Kgs 6:1 'Solomon`s', 8:1 'fathers`', 8:41 'name`s', 2 Kgs 17:41 'children`s'): backtick for apostrophe, an encoding artifact of the hosted edition.", "1 Kgs 8:50: hosted ASV ends without the verse-final semicolon (trivial)."]
- escalationReportAdjustments: "Initial verdicts on all 189 verses, 15 overlay ops and 30 central ops were formed from the chapters, the MT source, the ASV, the glossaries and the diffs, with mechanical checks (Hebrew text identical to source-he-*.json in every paragraph; bracketed Qere inventory; glossaryRefs resolution against central 2.78.0 + wave-B + wave-C/D and both overlays; appliesTo superset check of every central modify op against 2.78.0 + wave-B; double-quote balance; genesis-woh / exodus-woh / signed-off Kings lines for every cross-reference). Only then was wave-cd-editor-report.md read. No verdict changed. The report added three things the reviewer recorded: (1) its genesis-woh count ('Mitsrayim' 206x, 'Mitzrayim' 18x) does not match the English lines (81 / 0; the 8 'Mitzrayim' are in notes), corrected in the names-entry review and founder point C; (2) its 'Other notes' bullet says English forms were not added to chapter titles, but the files carry 'Shelomoh (Solomon)' and 'Shomron (Samaria) ... Yisra'el (Israel)' as its own 'Chapter titles' section says, so that bullet is stale; (3) its founder lettering (A, C-J) is used in the recommendations, with B confirmed as settled. The report's spot-check list was checked: NJPS 'Great Hall' / 'stately House' / 'thick cloud' confirmed; LXX 8:53a and LXX 4 Kgdms 4:35 descriptions confirmed; Aquila/Symmachus chrēmatistērion for dəḇîr confirmed."
- founderDecisionRecommendations: {"A-temple-rooms": "Ratify 'porch' / 'great hall' / 'inner sanctuary' / 'the most holy place', with the context clause (hêḵāl = 'temple'/'palace' for a whole building). 'Oracle' rests on a rejected etymology and 'the temple of the house' (6:3) misleads in a chapter where the building is the 'house'. Confirm or drop the 'Alter' attribution in the central entry.", "C-Mitzrayim-vs-Mitsrayim": "Keep Kings on 'Mitzrayim' (the tz rule ratified at wave A covers Tzidon, Tzarfat, Tzadoq; Kings would be internally inconsistent otherwise). Corpus facts: genesis-woh English lines read 'Mitsrayim' 81x and 'Mitzrayim' 0x (8 'Mitzrayim' only in notes); exodus-woh lines 'Mitsrayim' 38x. The report's '206 / 18' and the overlay's '(mostly)' overstate the mix. If one corpus spelling is wanted, normalize genesis-woh/exodus-woh to 'Mitzrayim' in a separate mechanical pass rather than making Kings an exception to its own tsade rule.", "D-8:23-lower-case-elohim": "Ratify clause 5. In ʾên-kāmôḵā ʾĕlōhîm the noun is the class compared, so a capital would make YHWH be compared with himself; the commentary keeps the monotheistic and incomparability readings open. This is consistent with 'there is no Elohim in Yisra'el' (2 Kgs 1:3), where the referent is YHWH.", "E-17:26-27-manner-and-Elohim-of-the-land": "Ratify both. 'Manner' is an attested sense of mišpāṭ (KJV throughout vv 26-40) and keeps the keyword concordant while reserving 'law' for tôrâ. The capital follows the referent rule with the narrator'
- summary: "41 verdicts: 40 approve, 1 revise, 0 flag-for-human (17:4 revise). Glossary ops relevant to this chapter: 18 (12 approve, 2 revise, 4 flag-for-human). No lens leakage. Flags are founder-confirmation points only (A, C-J); the reviewer recommends ratifying all of them. Status awaiting-human."
