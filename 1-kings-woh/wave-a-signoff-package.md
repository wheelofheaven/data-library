# Kings wave A (Elijah cycle) — human sign-off package

**Scope:** 1 Kings 17, 18, 19 (`1-kings-woh`) and 2 Kings 1, 2 (`2-kings-woh`) — 134 verses. First wave of the canon-cited Bible program (all biblical chapters cited in *The Book Which Tells the Truth*, *Extra-Terrestrials Took Me to Their Planet* and *Let's Welcome the Extra-Terrestrials*, as whole chapters).

**Status:** all five chapters `awaiting-human`, version `1.0.0-rc1`. Source: MT, Tanach with Ta'amei Hamikra (Sefaria; WLC base; Public Domain). Reference: ASV (1901).

## Summary

| Chapter | Verses | With commentary | Approve | Revise | Flag |
|---|---|---|---|---|---|
| 1 Kings 17 — Eliyahu at the brook Kerit and the widow of Tzarfat | 24 | 16 | 24 | 0 | 0 |
| 1 Kings 18 — Eliyahu and the prophets of Ba'al on Mount Karmel | 46 | 33 | 46 | 0 | 0 |
| 1 Kings 19 — Eliyahu at Horeb and the call of Elisha | 21 | 20 | 20 | 1 | 0 |
| 2 Kings 1 — Achazyahu, Ba'al-Zevuv and the captains of fifty | 18 | 15 | 18 | 0 | 0 |
| 2 Kings 2 — Eliyahu taken up in the whirlwind; Elisha succeeds him | 25 | 23 | 22 | 3 | 0 |

- **Overlays (new, v1.0.0):** 13 entries each (9 shared, identical in substance), claim types per overlay: direct 12, inferred 1, speculative 0.
- **Central glossary:** proposed 2.77.0 → 2.78.0 — 1 add (`esh-yhwh-fire-of-yhwh`), 5 corrections (`esh-elohim` mis-cited 1 Kgs 18:38; `ruach-se'arah` / `min-ha-se-arah` scope conflict; `shamayim`; `tzet-nephesh` respelled "nefesh"), 18 coverage-only extensions.
- **Lens leakage:** none in any English line; Wheel of Heaven readings only in labelled "reception note" paragraphs, checked against TBWTT ch. 3.
- **Ketiv/Qere:** 6 sites, Qere translated, all noted.

## Items requiring decision

1. **Names (founder decision A).** Hebrew transliteration (Eliyahu, Ach'av, Izevel, Yisra'el), as in genesis-woh and exodus-woh narrative, versus the English forms the canon quotes (Elijah, Ahab, Jezebel). *Editor and Reviewer both recommend Hebrew forms*, with the English name added to each chapter title for findability (e.g. "Eliyahu (Elijah)"). This is the reviewer flag that holds all five chapters.
2. **2 Kgs 2:1, 11 — šāmayim (founder decision B).** "to the skies" (Editor, following the central entry) versus "to the heavens" (Reviewer). *Recommended: "to the heavens"* — genesis-woh already uses "heaven(s)" at 14 divine-realm sites (Gen 28:12, 22:11, 19:24 …) and "skies" at 25 physical ones; "skies" stays at 1 Kgs 18:45 (weather) and 2 Kgs 1:10, 12, 14 (fire from the sky, as in job-woh 1:16). Reviewer registers "skies" here as a lens-register concern at the canon's principal Kings citation.
3. **Fixes to apply at sign-off (Reviewer revises; orchestrator applies, no rendering reversed):**
   - 1 Kgs 19:12 commentary + `qol-demamah-daqqah` overlay entry: note that Dhorme's « brise légère » has versional support (LXX *phōnē auras leptēs*), and add Lust (VT 25, 1975) "roaring thunderous sound".
   - 2 Kgs 2:14 commentary + `mt-baseline-at-versional-cruxes-and-versification-kings`: the major disjunctive is on ʾēliyyāhû, so the accents support the line's reading (LXX *aphphō* is the alternative).
   - 1 Kgs 19:2 + `elohim-referent-and-article-conventions-kings`: replace Ruth 1:17 with 1 Sam 3:17; 14:44; 2 Sam 3:9.
   - 1 Kgs 18:26: cite 2 Sam 9:13 for adjectival *pissēaḥ*.
   - Central `shamayim`: rewrite the corpus note (genesis-woh context-scales skies/heaven(s) deliberately; not an Exodus drift).
   - Central `tzet-nephesh` respelling ships only together with Genesis 35:18 "nephesh" → "nefesh" (genesis-woh chapter 35, line change) in the same release.
   - If decision 2 = "heavens": update the quoted phrase in `min-ha-se-arah`.
4. **Semver.** 2.78.0 (house practice; Editor and Reviewer agree) rather than 3.0.0 (written rule). Reviewer suggests aligning the docs to practice later.

## Follow-ups (not blocking)

- Hosted ASV `data-library/1-kings` has wrong wording at 8:15 ("thy father" for "my father") and 8:43 ("my name" for "thy name"); audit that edition.
- `malakh-yhwh-messenger` lists some verses under two ID formats (`1KGS-19:7` and `1KI-WOH-19:7`).

---

## Editor's escalation report (inlined)

# Kings Wave A Editor Report: the Elijah cycle

**Books / chapters:** `1-kings-woh` 17 (24 verses), 18 (46), 19 (21); `2-kings-woh` 1 (18), 2 (25). That is 134 verses.
**Editor pass:** 2026-11-01 (claude-opus-5-5, woh-editor role)
**Status at end of pass:** all five chapters `draft` → `editor-review`; version `0.1.0` → `1.0.0-rc1`; `glossaryVersion` 2.78.0 (pending application of the central diff); `overlayGlossaryVersion` 1.0.0; `reviewer` left `pending`.
**Editorial questions:** 53 received, 53 resolved, all arrays cleared. Two of the resolutions are flagged below as founder-preference points.

**Files written**

- `1-kings-woh/chapter-{17,18,19}.json`, `2-kings-woh/chapter-{1,2}.json`
- `1-kings-woh/_translation-glossary.json` v1.0.0 (new, 13 entries)
- `2-kings-woh/_translation-glossary.json` v1.0.0 (new, 13 entries)
- `1-kings-woh/wave-a-central-diff.json` (proposed central diff, not applied)
- this report

**Counts**

- Overlay entries: 9 shared (identical text and appliesTo in both overlays) + 4 per book = 13 per overlay, 17 distinct. By claim_type, per overlay: direct 12, inferred 1, speculative 0.
- Central diff: 1 add, 5 corrections (rationale and/or wohChoice), 18 appliesTo-only extensions. Recommended version 2.77.0 → 2.78.0 (see "Glossary changes for review").
- Commentary (`notes.official`): 107 of 134 paragraphs (17: 16/24, 18: 33/46, 19: 20/21, 2 Kgs 1: 15/18, 2 Kgs 2: 23/25).
- English text changed at 9 verses, each backed by a glossary entry (rule 7):
  - 1 Kgs 17:21, 22: 'nephesh' → 'nefesh' (`nefesh-scope-and-spelling-kings`; central tzet-nephesh spelling fix)
  - 1 Kgs 18:12; 2 Kgs 2:16: 'the Spirit of YHWH' → 'the ruach of YHWH' (`ruach-yhwh-and-prophetic-ruach-transliteration-kings`)
  - 2 Kgs 2:9: 'spirit' → 'ruach'; 2 Kgs 2:15: 'The spirit of Eliyahu' → 'The ruach of Eliyahu' (same entry)
  - 2 Kgs 2:2, 4, 6: 'and as your soul lives' → 'and as you yourself live' (`nefesh-scope-and-spelling-kings`)
- All other lines are the Translator's draft, unchanged.

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry was created, either in the overlays or in the central diff. Nothing in this pass blocks advance on the speculative count.

The canon-cited sites are 1 Kgs 17:6, 17:23, 17:24, 18:38, 19:5-6, 19:11-12, and 2 Kgs 1:12, 1:15, 2:1, 2:11. At each of them the line renders the Hebrew lexically. The Raëlian reading appears only in a paragraph headed **"Wheel of Heaven reading (reception note, not a translation claim)"**. That paragraph states what *The Book Which Tells the Truth* (ch. 3) says and that the line does not encode it. It does not argue for the reading.

The one non-direct entry is `ruach-yhwh-and-prophetic-ruach-transliteration-kings`, which is **inferred** (details under "Lens-discipline records" below).

---

## Founder-preference points (resolved, flagged for confirmation)

Both of the following are resolved and applied. Either can be reversed mechanically if the founder prefers the alternative.

### A. Proper names: transliteration throughout (`hebrew-proper-name-transliteration-convention-kings`)

**Decision:** Hebrew transliteration throughout: Eliyahu, Ach'av, Izevel, Ovadyahu, Karmel, Ba'al, Yizre'el, Shomron, Yarden, Yisra'el. The short MT forms *ʾēliyyâ* / *ʾăḥazyâ* (2 Kgs 1:2, 3, 4, 8, 12) are normalized to Eliyahu / Achazyahu, and the MT spelling is noted in commentary. Moab, Aram, Damascus, Horeb, Gilgal, Asherah and 'Tishbite' stay in English.

**Why:** Kings is narrative Hebrew continuous with Genesis/Exodus. Both of those books render names by transliteration (exodus-woh: Yisra'el, Aharon, Ya'aqov). The KJV forms belong to the Latter-Prophets volumes (isaiah-woh, ezekiel-woh). Exodus's 'Moses'/'Pharaoh' is a grandfathered two-name exception. A hybrid surface ('Elijah ... Ach'av ... Izevel') would be less consistent than either pure option. Every chapter's commentary gives the English equivalents, and the entry's wohChoice carries a full equivalence table.

**Alternative:** KJV forms throughout (Elijah, Ahab, Jezebel ...), which is how the English canon quotes these chapters. Switching would be a scripted substitution from the table plus the chapter titles. No other glossary change would be needed.

### B. *šāmayim* at the canon's central Kings site: 'to the skies' (central `shamayim`)

**Decision:** 'skies' at 1 Kgs 18:45; 2 Kgs 1:10, 12, 14; 2:1, 11 ('in the whirlwind to the skies'), per the central direct entry. This matches genesis-woh, job-woh and ezekiel-woh. The commentary at 2 Kgs 2:1 states that *šāmayim* also names YHWH's dwelling (1 Kgs 8:30), so the rendering does not narrow the destination.

**Risk noted:** at the canon's central Kings citation, 'skies' is the rendering more congenial to the canon's reading than ASV 'into heaven'. It is applied because the central lexeme decision predates this wave and holds across the corpus, not because of the lens.

**Alternative:** 'into the heavens', which the entry's own "numinous register" clause allows and which exodus-woh uses (see the drift note in the central diff).

---

## Lens-discipline records (for the Reviewer)

1. **`ruach-yhwh-and-prophetic-ruach-transliteration-kings` (inferred).**
   - Where *rûaḥ YHWH* carries a prophet away (1 Kgs 18:12; 2 Kgs 2:16), the line reads 'the ruach of YHWH', and the prophet's *rûaḥ* at 2 Kgs 2:9, 15 also stays 'ruach'. Physical wind is still 'wind' (1 Kgs 19:11).
   - The precedent is ezekiel-woh, which renders Ezek 37:1 'by the ruach of YHWH', together with the central `ruach-chayyot` (also inferred).
   - The entry is inferred because it deliberately leaves the spirit/wind ambiguity unresolved, and the 'wind' reading is a minority view.
   - The Reviewer should confirm that leaving the word untranslated is not itself lens-leaning. The commentary gives both readings and does not choose.
2. **2 Kgs 2:11 (`rekhev-esh-susei-esh-chariot-and-horses-of-fire-2-kings-2-11`).**
   - The construct chains are literal, the plural verb is kept, and the ASV's supplied 'there appeared' is not added. No technical vocabulary is used.
   - The commentary points out that in the Hebrew the *storm* (not the chariot) is the vehicle of ascent.
   - The canon's craft reading is confined to the labelled reception note.
3. **1 Kgs 19:12 (`qol-demamah-daqqah-still-small-voice-1-kings-19-12`).**
   - ASV/KJV 'a still small voice' is kept, because every word of it is a recognized sense of the Hebrew. The literal 'a sound of thin silence' and NRSV/NJPS/Dhorme are in commentary.
   - Dhorme's 'brise légère', which the French canon quotes, is not adopted because the breeze is not in *dəmāmâ*'s range.
4. **1 Kgs 17:4, 6 (`orvim-ravens-mt-vocalization-1-kings-17`).** MT 'ravens' is kept. The 'Arabs' revocalization is rejected for lack of textual support. The canon's 'carrier ravens' presupposes the MT and lives only in the reception note.
5. **1 Kgs 18:38 (central `esh-yhwh-fire-of-yhwh`, new).** 'the fire of YHWH fell' (ASV wording; definite construct). The meteorological and canon readings appear only in commentary.
6. **Non-extensions** (central entries cited in commentary but deliberately not applied to wave-A refIds, because their wohChoice does not govern the Kings line):
   - `elohim-as-translation`: a global convention whose appliesTo has only ever listed Gen 1. The Kings application is in the overlay.
   - `elohim-aherim-other-gods-monolatry-vs-monotheism-scholarly-dispute-cross-corpus`: precedent for lower-case 'elohim'. The glossaryRefs are kept, but the wohChoice is the Ex 20:3 phrase.
   - `anokhi-elohei-X-avikha-ancestral-god-formula`: removed from 1 Kgs 18:36 refs and replaced by `elohei-avraham-yitzchaq-veyaakov-patriarchal-god-formula-cross-corpus`.
   - `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus`: its wohChoice 'ascent to heaven' would conflict with `shamayim`. Cited as comparative background at 2 Kgs 2:11.
   - `cosmic-silence-shem-ha-mephorash-revelation-tradition-cross-corpus-shiur-qomah-revelation-8-1`: a commentary term.
   - `she-erit-remnant-cross-corpus-theological-keyword`: rules on the noun; 1 Kgs 19:18 has the verb.
   - `veh-einennu-laqach`: the Gen 5:24 parallel, cited at 2 Kgs 2:3.
   - `sinai-theophany-ex-19-elohim-craft-descent-disavowals-volcanic-hypothesis-cross-corpus`: Horeb typology is in commentary only.

---

## Unresolved editorial questions

**None.** All 53 questions are resolved as follows. "Draft kept" means the Translator's line is unchanged.

### 1 Kings 17 (8)

| refId | Question | Resolution |
|---|---|---|
| 17:1 | Name convention for the wave | Transliteration throughout (see Founder point A); `hebrew-proper-name-transliteration-convention-kings` |
| 17:1 | *mittōšāḇê* vs LXX 'from Tishbe' | MT kept; LXX in commentary; `mt-baseline-at-versional-cruxes-and-versification-kings` |
| 17:3 | *ʿal-pənê hayyardēn* | Draft kept ('before'); the 'east of' sense in commentary |
| 17:4 | ravens / Arabs | MT 'ravens'; `orvim-ravens-mt-vocalization-1-kings-17` |
| 17:14 | Ketiv/Qere | Qere; `ketiv-qere-qere-translated-kings` |
| 17:15 | Ketiv/Qere; *yāmîm* | Qere 'she and he'; 'for days' kept; same entry |
| 17:18 | 'man of God' article | Follow the Hebrew article; `ish-ha-elohim-man-of-the-elohim-prophetic-title-kings` |
| 17:21 | nefesh scope and spelling | 'nefesh' only at 17:21-22; idiomatic elsewhere; spelling 'nefesh'; `nefesh-scope-and-spelling-kings` + central tzet-nephesh fix |

### 1 Kings 18 (16)

| refId | Question | Resolution |
|---|---|---|
| 18:4 | fifty / fifties | Draft kept; MT vs LXX in commentary; MT-baseline entry |
| 18:12 | *rûaḥ YHWH* | 'the ruach of YHWH'; `ruach-yhwh-and-prophetic-ruach-transliteration-kings` (inferred) |
| 18:15 | Tseva'ot | 'YHWH of hosts' as in isaiah-woh; `yhwh-tsevaot-yhwh-of-hosts-kings` |
| 18:19 | Ba'al article | No English article, 'the Ba'als'; `habbaal-baal-hebrew-bible-rendering-kings` |
| 18:19 | Asherah | 'the Asherah' kept; `nevie-ha-asherah-prophets-of-the-asherah-1-kings-18-19` |
| 18:21 | *pōsəḥîm ʿal-štê hassəʿippîm* | ASV kept; literal sense in commentary |
| 18:24 | lower-case elohim | Lower case for non-YHWH referents, the article/predicate rule; `elohim-referent-and-article-conventions-kings` |
| 18:26 | singular verbs; *wayəpassəḥû* | Impersonal ASV construal (MT-baseline entry); 'limped about' kept for the *psḥ* echo |
| 18:27 | *śîaḥ / śîḡ* | ASV kept; euphemism reading in commentary (Rendsburg 1988) |
| 18:29 | *wayyiṯnabbəʾû*; *minḥâ* | 'prophesied' and 'offering' kept; ecstatic and afternoon-offering senses in commentary |
| 18:34 | versification | MT division kept; ASV equivalence in commentary at vv 33-34; MT-baseline entry |
| 18:36 | Ketiv/Qere | Qere; Ketiv/Qere entry |
| 18:37 | 'turned their heart back' | Majority construal kept; minority reading in commentary |
| 18:38 | *ʾēš-YHWH* | 'the fire of YHWH fell' kept; new central `esh-yhwh-fire-of-yhwh`; `esh-elohim` corrected |
| 18:41 | *hămôn* | Draft 'rushing' kept; ASV 'abundance' in commentary |
| 18:42 | Ketiv/Qere | Qere; Ketiv/Qere entry |

### 1 Kings 19 (12)

| refId | Question | Resolution |
|---|---|---|
| 19:2 | Izevel's plural oath | 'So may the elohim do' (plural, lower case, no supplied 'to me'); elohim-referent entry |
| 19:2 | nepeš sites in ch. 19 | ASV 'life' / 'himself' kept; `nefesh-scope-and-spelling-kings` |
| 19:3 | *wayyarʾ* vs 'was afraid' | MT kept; versions in commentary; MT-baseline entry |
| 19:4 | Ketiv/Qere; *rōṯem* | Qere; 'broom tree'; `rotem-broom-tree-1-kings-19-4` |
| 19:5 | malʾāḵ definiteness | 'a messenger' (v 5) / 'the messenger of YHWH' (v 7), not harmonized; central malakh extended |
| 19:6 | *ʿuggaṯ rəṣāpîm* | Draft 'hot stones' kept; ASV in commentary |
| 19:10 | *qannōʾ qinnēʾṯî* | ASV 'very jealous' kept; 'zealous' sense in commentary |
| 19:11 | participle, *rûaḥ*, *raʿaš*, 'but' | Draft kept ('was passing by', 'wind', 'earthquake', ASV 'but') |
| 19:12 | *qôl dəmāmâ daqqâ* | 'a still small voice' kept; `qol-demamah-daqqah-still-small-voice-1-kings-19-12` |
| 19:18 | *wəhišʾartî* | 'Yet I will leave' kept; Rom 11:4 past reading in commentary |
| 19:20 | *meh-ʿāśîṯî lāḵ* | ASV kept; three readings in commentary |
| 19:21 | *zbḥ* | 'slaughtered' kept; sacrificial possibility in commentary |

### 2 Kings 1 (6)

| refId | Question | Resolution |
|---|---|---|
| 1:2 | Ba'al-Zevuv form; elohim of Eqron | MT form kept, zbl hypothesis in commentary; lower-case elohim; `baal-zevuv-elohei-eqron-2-kings-1` |
| 1:3 | short name forms | Normalized; noted in commentary; names entry |
| 1:8 | *ʾîš baʿal śēʿār* | 'A hairy man' kept; garment reading in commentary |
| 1:10 | fire / esh-elohim / skies / ʾîš-ʾēš | Bare 'fire' at 1:10, 14; 'fire of Elohim came down' at 1:12 (verb as written); 'skies'; article alternation kept |
| 1:13 | *šəlišîm* | ASV kept; MT-baseline entry |
| 1:13 | nepeš 'my life' | Kept; nefesh-scope entry |

### 2 Kings 2 (11)

| refId | Question | Resolution |
|---|---|---|
| 2:1 | *bassĕʿārâ* entry conflict | 'in the whirlwind' under central `min-ha-se-arah` (bare noun); `ruach-se'arah` corrected to the compound only |
| 2:1 | *šāmayim* 'skies' vs 'heaven' | 'to the skies' (Founder point B); exodus-woh drift recorded in central diff |
| 2:2 | *ḥê-napšəḵā* | **Changed** to 'and as you yourself live'; nefesh-scope entry |
| 2:3 | *bənê-hannəḇîʾîm* | 'the sons of the prophets' kept; membership sense in commentary; `bene-ha-neviim-sons-of-the-prophets-kings` |
| 2:9 | *pî-šənayim*; *rûaḥ* | 'a double portion' (`pi-shenayim-double-portion-2-kings-2-9`); 'ruach' (ruach entry) |
| 2:11 | chariot/horses of fire; plural verb | Draft kept; `rekhev-esh-susei-esh-chariot-and-horses-of-fire-2-kings-2-11` |
| 2:12 | *rekeḇ* number; *pārāšîm* | ASV kept; identity of lexeme with 2:11 noted |
| 2:14 | *ʾap̄-hûʾ* | ASV construal kept; accent and LXX readings in commentary; MT-baseline entry |
| 2:16 | Ketiv/Qere; *rûaḥ YHWH* | Qere; 'the ruach of YHWH' |
| 2:19 | *məšakkāleṯ* | ASV kept |
| 2:23 | ages of *nəʿārîm* | 'young lads' / 'children' kept; range in commentary |

---

## Glossary changes for review

### Central glossary: proposed diff (`1-kings-woh/wave-a-central-diff.json`, not applied)

The file is a JSON list. Its first element is `{"op":"version","from":"2.77.0","to":"2.78.0", ...}` and carries a ready-to-paste `scopeNoteAddendum`. The remaining 24 elements are add/modify operations. Each modify `changes` value replaces the field outright. appliesTo values are complete arrays that keep every existing refId.

**Version recommendation: 2.78.0.** Under the role doc's strict rule, any modification of an existing entry is semver-major (3.0.0). House practice, however, labels rationale corrections as "semver-major corrections" in the changelog while incrementing the minor number (e.g., the GEN-21:17 `malakh-yhwh-messenger` correction stayed in 2.x). No wohChoice decision is reversed: tzet-nephesh changes spelling only. If the strict rule is applied instead, use 3.0.0.

- **Added:** `esh-yhwh-fire-of-yhwh` (claim_type `direct`). 'the fire of YHWH' at 1 Kgs 18:38; cross-corpus Num 11:1, 3, with Lev 9:24 / 10:2 and Num 16:35 as related forms.
- **Modified (corrections):**
  - `esh-elohim`: the rationale wrongly claimed 1 Kgs 18:38 (MT *ʾēš-YHWH*) and 2 Kgs 1:10 (bare *ʾēš*). It is now scoped to the construct, with the verb rendered per site, and appliesTo adds 2KI-WOH-1:12. wohChoice is unchanged. (Translator item 1.)
  - `ruach-se'arah`: the rationale wrongly said the compound occurs at 2 Kgs 2:11 and Jer 23:19 / 30:23. It now gives the real occurrences (Ezek 13:11, 13; Ps 107:25; 148:8) and states the scope split from `min-ha-se-arah`. wohChoice and appliesTo are unchanged. (Translator item 2.)
  - `min-ha-se-arah`: the rationale is extended with a "bare *sĕʿārâ*" convention ('whirlwind', with the lexical caveat), and appliesTo adds 2KI-WOH-2:1, 2:11. (Translator item 2.)
  - `shamayim`: the rationale drops the inaccurate 'grammatically dual' claim (*šāmayim* is a plural with a dual-like form; GKC §88d, Joüon-Muraoka §91f) and records that exodus-woh renders 'heavens' at Ex 16:4; 17:14; 20:4, 11, 19 without citing the entry, for reconciliation at the next Exodus pass. appliesTo adds 6 Kings refIds. wohChoice is unchanged. (Translator item 3.)
  - `tzet-nephesh-departure-at-death-formula`: wohChoice and rationale are re-spelled 'nephesh' → 'nefesh'. The id is unchanged for stability. appliesTo adds 1KI-WOH-17:21, 22. (Translator item 4.) **Downstream:** GEN-WOH-35:18 in `genesis-woh/chapter-35.json` reads 'nephesh' and should be re-spelled by the genesis-woh owner. Not touched here.
- **Modified (appliesTo extensions only):**
  - `chei-x-oath-by-the-life-formula`, `davar-yhwh-prophetic-formula`, `malakh-yhwh-messenger`, `yonah-orev`, `al-tira-fear-not-divine-encouragement-formula`, `darash-yhwh-seeking-oracle`
  - `olah-burnt-offering`, `yad-yhwh`, `har-sinai-horev-the-mountain-of-Elohim-divine-mountain-cross-corpus`, `minchah-shaah`, `doubled-name-call-theophanic-formula`, `bethel-luz-name-etymology`
  - `be-er-sheva-folk-etymology`, `ad-ha-yom-ha-zeh-aetiological-formula`, `adam-adamah`, `navi-first-occurrence-abraham`, `piska-b-emtza-pasuq-masoretic-paragraph-break`, `elohei-avraham-yitzchaq-veyaakov-patriarchal-god-formula-cross-corpus`

Chapter files already reference `esh-yhwh-fire-of-yhwh` and pin `glossaryVersion` 2.78.0. If the diff is not applied, 1KI-WOH-18:38 points at an entry that does not exist.

### Per-translation overlays (new, v1.0.0)

**Shared.** These 9 entries are in both `1-kings-woh/_translation-glossary.json` and `2-kings-woh/_translation-glossary.json`, with identical text and appliesTo spanning both books. Extend both files together.

- Added: `hebrew-proper-name-transliteration-convention-kings` (claim_type: `direct`; appliesTo 92 refIds)
- Added: `elohim-referent-and-article-conventions-kings` (claim_type: `direct`)
- Added: `ish-ha-elohim-man-of-the-elohim-prophetic-title-kings` (claim_type: `direct`)
- Added: `nefesh-scope-and-spelling-kings` (claim_type: `direct`)
- Added: `ruach-yhwh-and-prophetic-ruach-transliteration-kings` (claim_type: `inferred`)
- Added: `ketiv-qere-qere-translated-kings` (claim_type: `direct`)
- Added: `mt-baseline-at-versional-cruxes-and-versification-kings` (claim_type: `direct`)
- Added: `yhwh-tsevaot-yhwh-of-hosts-kings` (claim_type: `direct`; sibling of isaiah-woh `yhwh-tzevaot-hosts-isaiah`)
- Added: `habbaal-baal-hebrew-bible-rendering-kings` (claim_type: `direct`)

**1-kings-woh only**

- Added: `orvim-ravens-mt-vocalization-1-kings-17` (claim_type: `direct`)
- Added: `nevie-ha-asherah-prophets-of-the-asherah-1-kings-18-19` (claim_type: `direct`)
- Added: `rotem-broom-tree-1-kings-19-4` (claim_type: `direct`)
- Added: `qol-demamah-daqqah-still-small-voice-1-kings-19-12` (claim_type: `direct`)

**2-kings-woh only**

- Added: `baal-zevuv-elohei-eqron-2-kings-1` (claim_type: `direct`)
- Added: `bene-ha-neviim-sons-of-the-prophets-kings` (claim_type: `direct`)
- Added: `pi-shenayim-double-portion-2-kings-2-9` (claim_type: `direct`)
- Added: `rekhev-esh-susei-esh-chariot-and-horses-of-fire-2-kings-2-11` (claim_type: `direct`)

**Central-promotion candidates** (left in the overlays for now):

- `elohim-referent-and-article-conventions-kings` and `ruach-yhwh-and-prophetic-ruach-transliteration-kings`, once Samuel or the Latter Prophets apply them.
- `nefesh-scope-and-spelling-kings`, if the *ḥê-napšəḵā* oath recurs in 1 Samuel.

---

## Notes for the Reviewer

- Scholarly authorities cited in commentary and rationales:
  - Kings commentaries: Cogan, *1 Kings* (AB 10, 2001); Cogan and Tadmor, *II Kings* (AB 11, 1988); Gray, *I & II Kings* (OTL); Sweeney, *I & II Kings* (OTL, 2007); Burney, *Notes on the Hebrew Text of the Books of Kings* (1903)
  - Lexica and grammars: BDB, HALOT, GKC, Joüon-Muraoka
  - Other works: Tov 2012; Zohary 1982; Mettinger 1982; Day 2000; Smith 2002; Hadley 2000; Olyan 1988; Wilson 1980; Wolff 1974; Rendsburg 1988 (*CBQ* 50); Patai 1939 (*HUCA* 14); Thiele 1983
- Page numbers were deliberately omitted wherever they could not be verified.
- Verse numbering follows the MT throughout. The only English-numbering divergence in the wave is 1 Kgs 18:33-34, which is noted at both verses.
- 2 Kgs 1:17 has a Masoretic mid-verse *pisqa* (פ), which is present in the source and noted.


---

## Reviewer report (non-approve verdicts and report fields, per chapter)

### 1 Kings 17 — Eliyahu at the brook Kerit and the widow of Tzarfat



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:28:10Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "flag-for-human", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice (Avraham, Ya'aqov, Beit-El; Yisra'el, Aharon) vs isaiah-woh / ezekiel-woh / daniel-woh English forms (checked in the data)"], "reasoning": "The rendering is philologically sound: forms are transliterated, short and long MT forms are normalized with a note, and the equivalence table is complete. claim_type direct is right for a presentation convention with no interpretive content. It is flagged only because it is the open founder decision A. Reviewer recommendation: retain transliteration, which continues the Torah-narrative volumes and keeps the 'my El is Yah' / 18:39 wordplay visible; add the English form to each chapter title (e.g. 'Eliyahu (Elijah) ...') for discoverability."}, {"glossary_id": "ish-ha-elohim-man-of-the-elohim-prophetic-title-kings", "status": "approve", "citations": ["BDB s.v. ʾîš", "Cogan & Tadmor, II Kings (AB 11; 1988), ad loc."], "reasoning": "Articles re-checked in the source: articular at 1 Kgs 17:18 and 2 Kgs 1:9, 11, 12, 13; anarthrous at 1 Kgs 17:24 and 2 Kgs 1:10. The rendering follows them exactly, and the ʾîš/ʾēš play noted for 2 Kgs 1 is standard. Direct confirmed."}, {"glossary_id": "nefesh-scope-and-spelling-kings", "status": "approve", "citations": ["HALOT s.v. nepeš", "Wolff, Anthropology of the Old Testament (1974)"], "reasoning": "Scope is correc
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 24 lines against the re-parsed MT. No English line carries a Wheel of Heaven reading: 'ravens' is the MT/versional reading, 'nefesh' (17:21-22) is the corpus anthropological convention, and 'messenger' does not occur. The canon readings (17:6 'carrier ravens'; 17:23 medical resuscitation) appear only in labelled reception notes, each verified against TBWTT ch. 3."
- escalationReportAdjustments: "Initial verdicts on all verses, overlay entries and central ops were formed from the chapters, source, overlays and diff before opening wave-a-editor-report.md. After reading it, no verdict changed. The report's Founder point B says 'skies' 'matches genesis-woh, job-woh and ezekiel-woh' and holds 'across the corpus'. A corpus check shows genesis-woh uses 'heaven(s)' at about 13 divine-realm sites (e.g. GEN-WOH-19:24, 28:12), which strengthens the reviewer's 'revise' at 2 Kgs 2:1, 11 and on the central shamayim op. The report's confirmation that 1KI-WOH-18:38 depends on applying esh-yhwh-fire-of-yhwh is recorded in that op's reasoning."
- founderDecisionRecommendations: {"A-proper-names": "Retain Hebrew transliteration (continuity with genesis-woh/exodus-woh narrative volumes; theophoric wordplay at 1 Kgs 18:39 stays visible; mechanically reversible). Add the English form to chapter titles for discoverability.", "B-shamayim-at-2-Kgs-2:1,11": "Render 'to the heavens' at 2 Kgs 2:1, 11 (corpus precedent GEN-WOH-28:12 etc.; central shamayim's numinous-register clause; central human-ascent entry). Keep 'skies' at 1 Kgs 18:45 and 2 Kgs 1:10, 12, 14 (meteorological / Job 1:16 precedent)."}
- summary: "24 verdicts: 24 approve, 0 revise, 0 flag. Disputed verses (17:1 MT tōšāḇê; 17:14-15 K/Q; 17:18/24 article on 'man of (the) Elohim'; 17:21-22 nefesh) are all defensible and cited. Status is awaiting-human only because the book-wide name convention (founder decision A) is flagged in glossaryReview."

### 1 Kings 18 — Eliyahu and the prophets of Ba'al on Mount Karmel



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:28:10Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "flag-for-human", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice (Avraham, Ya'aqov, Beit-El; Yisra'el, Aharon) vs isaiah-woh / ezekiel-woh / daniel-woh English forms (checked in the data)"], "reasoning": "The rendering is philologically sound: forms are transliterated, short and long MT forms are normalized with a note, and the equivalence table is complete. claim_type direct is right for a presentation convention with no interpretive content. It is flagged only because it is the open founder decision A. Reviewer recommendation: retain transliteration, which continues the Torah-narrative volumes and keeps the 'my El is Yah' / 18:39 wordplay visible; add the English form to each chapter title (e.g. 'Eliyahu (Elijah) ...') for discoverability."}, {"glossary_id": "elohim-referent-and-article-conventions-kings", "status": "revise", "citations": ["BDB s.v. ʾĕlōhîm", "1 Sam 3:17; 14:44; 2 Sam 3:9 (MT)", "Cogan, I Kings (AB 10; 2001), ad loc."], "reasoning": "Direct is defensible: case is a declared editorial device, the article and number follow the Hebrew, and the Ex 20:3 precedent exists. One factual fix: the rationale cites Ruth 1:17 as the 'same oath in Israelite mouths' with singular verbs, but Ruth is a Moabite and the subject there is YHWH, not ʾĕlōhîm. Replace it with 1 Sam 3:17; 14:44; 2 Sam 3:9 (kōh yaʿăśeh ʾĕlōhîm, singular), keep 1 Kgs 2:23, 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 46 lines. No lens content in any English line. 18:12 'ruach of YHWH' leaves the Hebrew ambiguity open and is not a lens choice (see glossaryReview). 18:38 'the fire of YHWH fell' is the exact construct, and the TBWTT 'ray from a ship hidden in the clouds' reading is confined to a labelled note. 18:45 'skies' is meteorological."
- escalationReportAdjustments: "Initial verdicts on all verses, overlay entries and central ops were formed from the chapters, source, overlays and diff before opening wave-a-editor-report.md. After reading it, no verdict changed. The report's Founder point B says 'skies' 'matches genesis-woh, job-woh and ezekiel-woh' and holds 'across the corpus'. A corpus check shows genesis-woh uses 'heaven(s)' at about 13 divine-realm sites (e.g. GEN-WOH-19:24, 28:12), which strengthens the reviewer's 'revise' at 2 Kgs 2:1, 11 and on the central shamayim op. The report's confirmation that 1KI-WOH-18:38 depends on applying esh-yhwh-fire-of-yhwh is recorded in that op's reasoning."
- founderDecisionRecommendations: {"A-proper-names": "Retain Hebrew transliteration (continuity with genesis-woh/exodus-woh narrative volumes; theophoric wordplay at 1 Kgs 18:39 stays visible; mechanically reversible). Add the English form to chapter titles for discoverability.", "B-shamayim-at-2-Kgs-2:1,11": "Render 'to the heavens' at 2 Kgs 2:1, 11 (corpus precedent GEN-WOH-28:12 etc.; central shamayim's numinous-register clause; central human-ascent entry). Keep 'skies' at 1 Kgs 18:45 and 2 Kgs 1:10, 12, 14 (meteorological / Job 1:16 precedent)."}
- summary: "46 verdicts: 46 approve. Versification at 18:33-34 verified (MT division followed, ASV equivalence noted). K/Q at 18:36, 18:42 verified. Non-blocking commentary fix at 18:26 (cite 2 Sam 9:13 for adjective pissēaḥ). Status awaiting-human because of founder decision A (names) and the glossary revisions."

### 1 Kings 19 — Eliyahu at Horeb and the call of Elisha

- **1KI-WOH-19:12** — revise: The English line ('a still small voice') is approved, since each word is a recognized sense of qôl dəmāmâ daqqâ. The commentary and overlay rationale need correcting. (1) Dhorme's 'brise légère', which the French canon quotes, comes from the LXX's phōnē auras leptēs, so the commentary should say it has versional support rather than calling it Dhorme's interpretation. (2) Lust's reading of dəmāmâ from dmm II, 'a roaring, thunderous sound', is a documented scholarly alternative and must be listed. Without it the commentary implies the only options are kinds of quiet. _Citations: LXX 3 Kgdms 19:12 (phōnē auras leptēs); Lust, 'A Gentle Breeze or a Roaring Thunderous Sound? Elijah at Horeb: 1 Kings XIX 12', VT 25 (1975); HALOT s.v. dəmāmâ; BDB s.v. dəmāmâ_

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:28:10Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "flag-for-human", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice (Avraham, Ya'aqov, Beit-El; Yisra'el, Aharon) vs isaiah-woh / ezekiel-woh / daniel-woh English forms (checked in the data)"], "reasoning": "The rendering is philologically sound: forms are transliterated, short and long MT forms are normalized with a note, and the equivalence table is complete. claim_type direct is right for a presentation convention with no interpretive content. It is flagged only because it is the open founder decision A. Reviewer recommendation: retain transliteration, which continues the Torah-narrative volumes and keeps the 'my El is Yah' / 18:39 wordplay visible; add the English form to each chapter title (e.g. 'Eliyahu (Elijah) ...') for discoverability."}, {"glossary_id": "elohim-referent-and-article-conventions-kings", "status": "revise", "citations": ["BDB s.v. ʾĕlōhîm", "1 Sam 3:17; 14:44; 2 Sam 3:9 (MT)", "Cogan, I Kings (AB 10; 2001), ad loc."], "reasoning": "Direct is defensible: case is a declared editorial device, the article and number follow the Hebrew, and the Ex 20:3 precedent exists. One factual fix: the rationale cites Ruth 1:17 as the 'same oath in Israelite mouths' with singular verbs, but Ruth is a Moabite and the subject there is YHWH, not ʾĕlōhîm. Replace it with 1 Sam 3:17; 14:44; 2 Sam 3:9 (kōh yaʿăśeh ʾĕlōhîm, singular), keep 1 Kgs 2:23, 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 21 lines. 19:5-7 'messenger' applies a central direct entry. 19:11-12 render the theophany vocabulary in its ordinary sense. The canon's 'landing of a craft' reading of 19:11-12 is confined to labelled notes, and the French Dhorme quotation was verified in TBWTT ch. 3 ('le son d'une brise légère')."
- escalationReportAdjustments: "Initial verdicts on all verses, overlay entries and central ops were formed from the chapters, source, overlays and diff before opening wave-a-editor-report.md. After reading it, no verdict changed. The report's Founder point B says 'skies' 'matches genesis-woh, job-woh and ezekiel-woh' and holds 'across the corpus'. A corpus check shows genesis-woh uses 'heaven(s)' at about 13 divine-realm sites (e.g. GEN-WOH-19:24, 28:12), which strengthens the reviewer's 'revise' at 2 Kgs 2:1, 11 and on the central shamayim op. The report's confirmation that 1KI-WOH-18:38 depends on applying esh-yhwh-fire-of-yhwh is recorded in that op's reasoning."
- founderDecisionRecommendations: {"A-proper-names": "Retain Hebrew transliteration (continuity with genesis-woh/exodus-woh narrative volumes; theophoric wordplay at 1 Kgs 18:39 stays visible; mechanically reversible). Add the English form to chapter titles for discoverability.", "B-shamayim-at-2-Kgs-2:1,11": "Render 'to the heavens' at 2 Kgs 2:1, 11 (corpus precedent GEN-WOH-28:12 etc.; central shamayim's numinous-register clause; central human-ascent entry). Keep 'skies' at 1 Kgs 18:45 and 2 Kgs 1:10, 12, 14 (meteorological / Job 1:16 precedent)."}
- summary: "21 verdicts: 20 approve, 1 revise (19:12 commentary: add LXX auras leptēs as the source of Dhorme's 'breeze', and Lust's 'roaring thunderous sound'; the English line is approved). Non-blocking: 19:2 commentary cites Ruth 1:17 wrongly (Moabite speaker, YHWH subject); use 1 Sam 3:17; 14:44; 2 Sam 3:9."

### 2 Kings 1 — Achazyahu, Ba'al-Zevuv and the captains of fifty



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:28:10Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "flag-for-human", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice (Avraham, Ya'aqov, Beit-El; Yisra'el, Aharon) vs isaiah-woh / ezekiel-woh / daniel-woh English forms (checked in the data)"], "reasoning": "The rendering is philologically sound: forms are transliterated, short and long MT forms are normalized with a note, and the equivalence table is complete. claim_type direct is right for a presentation convention with no interpretive content. It is flagged only because it is the open founder decision A. Reviewer recommendation: retain transliteration, which continues the Torah-narrative volumes and keeps the 'my El is Yah' / 18:39 wordplay visible; add the English form to each chapter title (e.g. 'Eliyahu (Elijah) ...') for discoverability."}, {"glossary_id": "elohim-referent-and-article-conventions-kings", "status": "revise", "citations": ["BDB s.v. ʾĕlōhîm", "1 Sam 3:17; 14:44; 2 Sam 3:9 (MT)", "Cogan, I Kings (AB 10; 2001), ad loc."], "reasoning": "Direct is defensible: case is a declared editorial device, the article and number follow the Hebrew, and the Ex 20:3 precedent exists. One factual fix: the rationale cites Ruth 1:17 as the 'same oath in Israelite mouths' with singular verbs, but Ruth is a Moabite and the subject there is YHWH, not ʾĕlōhîm. Replace it with 1 Sam 3:17; 14:44; 2 Sam 3:9 (kōh yaʿăśeh ʾĕlōhîm, singular), keep 1 Kgs 2:23, 
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 18 lines. 'fire ... from the skies' (1:10, 12, 14) follows the corpus's closest parallel (JOB-WOH-1:16) and is a normal lexical sense. 'messenger' per central entry. The TBWTT 'protection' reading of 1:12, 15 appears only in labelled notes."
- escalationReportAdjustments: "Initial verdicts on all verses, overlay entries and central ops were formed from the chapters, source, overlays and diff before opening wave-a-editor-report.md. After reading it, no verdict changed. The report's Founder point B says 'skies' 'matches genesis-woh, job-woh and ezekiel-woh' and holds 'across the corpus'. A corpus check shows genesis-woh uses 'heaven(s)' at about 13 divine-realm sites (e.g. GEN-WOH-19:24, 28:12), which strengthens the reviewer's 'revise' at 2 Kgs 2:1, 11 and on the central shamayim op. The report's confirmation that 1KI-WOH-18:38 depends on applying esh-yhwh-fire-of-yhwh is recorded in that op's reasoning."
- founderDecisionRecommendations: {"A-proper-names": "Retain Hebrew transliteration (continuity with genesis-woh/exodus-woh narrative volumes; theophoric wordplay at 1 Kgs 18:39 stays visible; mechanically reversible). Add the English form to chapter titles for discoverability.", "B-shamayim-at-2-Kgs-2:1,11": "Render 'to the heavens' at 2 Kgs 2:1, 11 (corpus precedent GEN-WOH-28:12 etc.; central shamayim's numinous-register clause; central human-ascent entry). Keep 'skies' at 1 Kgs 18:45 and 2 Kgs 1:10, 12, 14 (meteorological / Job 1:16 precedent)."}
- summary: "18 verdicts: 18 approve. The article alternation of ʾîš (hā)ʾĕlōhîm in 1:9-13, the anarthrous ʾēš-ʾĕlōhîm in 1:12 and the mid-verse pisqa in 1:17 were all verified in the source. Status awaiting-human because of founder decision A and the glossary revisions."

### 2 Kings 2 — Eliyahu taken up in the whirlwind; Elisha succeeds him

- **2KI-WOH-2:1** — revise: Re-parse: bəhaʿălôṯ YHWH ʾeṯ-ʾēliyyāhû bassəʿārâ haššāmāyim. 'When YHWH was about to take ... up' (NRSV/NJPS) and 'in the whirlwind' (article kept) are approved. Proposed change: 'to the skies' -> 'to the heavens'. Here haššāmayim is the destination of a divine taking-up, and the central shamayim entry's own clause scales the rendering toward a numinous register in such contexts. genesis-woh already does this (GEN-WOH-28:12 'reached to the heavens', 19:24, 22:11), and the central human-ascent entry reads 'ascent to heaven'. At the canon's central Kings citation the more physical 'skies' is the lens-congenial choice, so the corpus's own precedent should decide. This is founder decision B. _Citations: HALOT s.v. šāmayim; BDB s.v. šāmayim; Cogan & Tadmor, II Kings (AB 11; 1988), ad loc.; GEN-WOH-28:12 / 19:24 / 22:11 (corpus precedent: 'heaven(s)' for the divine realm)_
- **2KI-WOH-2:11** — revise: Re-parse: verbless presentative wəhinnēh rekeḇ-ʾēš wəsûsê ʾēš, plural wayyaprîḏû bên šənêhem, wayyaʿal ʾēliyyāhû bassəʿārâ haššāmāyim. Everything except the last phrase is approved as exact, and better than ASV, which supplies 'there appeared'. The commentary's point that the storm, not the chariot, carries Eliyahu up is accurate and cuts against the canon's reading. Proposed change as at v 1: 'to the skies' -> 'to the heavens' (founder decision B). _Citations: Cogan & Tadmor, II Kings (AB 11; 1988), ad loc.; HALOT s.v. səʿārâ; HALOT s.v. šāmayim; The Book Which Tells the Truth (TBWTT) ch. 3 (text verified in data-library/the-book-which-tells-the-truth/chapter-3.json)_
- **2KI-WOH-2:14** — revise: The English line is approved. The commentary states the Masoretic accentuation backwards. In the source the etnaḥta falls on ʾēliyyāhû, so the first half-verse ends with the question 'Where is YHWH, the Elohim of Eliyahu?'. ʾap̄-hûʾ (munaḥ + paseq, i.e. legarmeh) opens the second half, which is the construal the translation adopts ('And when he too had struck the waters'). Rewrite: the accents support the adopted reading; LXX aphphō and the alternative 'even he?' are the departures. Make the matching fix in the mt-baseline overlay entry. _Citations: Wickes, A Treatise on the Accentuation of the Twenty-One So-called Prose Books of the Old Testament (1887), on legarmeh/paseq; GKC §15 (accents); Cogan & Tadmor, II Kings (AB 11; 1988), ad loc.; LXX 4 Kgdms 2:14 (aphphō)_

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:28:10Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "flag-for-human", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice (Avraham, Ya'aqov, Beit-El; Yisra'el, Aharon) vs isaiah-woh / ezekiel-woh / daniel-woh English forms (checked in the data)"], "reasoning": "The rendering is philologically sound: forms are transliterated, short and long MT forms are normalized with a note, and the equivalence table is complete. claim_type direct is right for a presentation convention with no interpretive content. It is flagged only because it is the open founder decision A. Reviewer recommendation: retain transliteration, which continues the Torah-narrative volumes and keeps the 'my El is Yah' / 18:39 wordplay visible; add the English form to each chapter title (e.g. 'Eliyahu (Elijah) ...') for discoverability."}, {"glossary_id": "nefesh-scope-and-spelling-kings", "status": "approve", "citations": ["HALOT s.v. nepeš", "Wolff, Anthropology of the Old Testament (1974)"], "reasoning": "Scope is correct: the word is transliterated only where nepeš names the returning life (17:21-22) and rendered idiomatically in fixed idioms. 'as you yourself live' for ḥê-napšəḵā is accurate (cf. NJPS). The spelling unification depends on the central tzet-nephesh op shipping together with the GEN-WOH-35:18 respelling."}, {"glossary_id": "ruach-yhwh-and-prophetic-ruach-transliteration-kings", "status": "approve", "citations": ["BDB s.v. rû
- lens-leakage-flags: [{"refId": "2KI-WOH-2:1", "concern": "'to the skies' for haššāmayim as the destination of YHWH's taking-up. The lexeme supports 'sky', but at the Raëlian canon's central Kings citation the most physical register is the lens-congenial option, and the corpus elsewhere (GEN-WOH-28:12, 19:24, 22:11; central human-ascent entry) uses 'heaven(s)' for the divine realm. The ambiguity is declared in commentary, so this is a register concern, not an interpolation. Recommend 'to the heavens' (founder decision B)."}, {"refId": "2KI-WOH-2:11", "concern": "Same as 2:1 ('went up in the whirlwind to the skies'). The rest of the verse is literal (no 'there appeared', no technical vocabulary), and the commentary correctly says the storm, not the chariot, is the vehicle."}]
- lensLeakageCheck: "Checked all 25 lines. Two register flags: 2:1, 2:11 'to the skies' (see lens-leakage-flags). Otherwise 2:11 is literal ('chariot of fire', 'horses of fire', 'whirlwind', plural verb, nothing supplied), and the canon's craft reading is confined to a labelled note. The 'ruach' transliteration at 2:9, 15, 16 is a declared inferred convention with both readings in commentary, and is not leakage."
- escalationReportAdjustments: "Initial verdicts on all verses, overlay entries and central ops were formed from the chapters, source, overlays and diff before opening wave-a-editor-report.md. After reading it, no verdict changed. The report's Founder point B says 'skies' 'matches genesis-woh, job-woh and ezekiel-woh' and holds 'across the corpus'. A corpus check shows genesis-woh uses 'heaven(s)' at about 13 divine-realm sites (e.g. GEN-WOH-19:24, 28:12), which strengthens the reviewer's 'revise' at 2 Kgs 2:1, 11 and on the central shamayim op. The report's confirmation that 1KI-WOH-18:38 depends on applying esh-yhwh-fire-of-yhwh is recorded in that op's reasoning."
- founderDecisionRecommendations: {"A-proper-names": "Retain Hebrew transliteration (continuity with genesis-woh/exodus-woh narrative volumes; theophoric wordplay at 1 Kgs 18:39 stays visible; mechanically reversible). Add the English form to chapter titles for discoverability.", "B-shamayim-at-2-Kgs-2:1,11": "Render 'to the heavens' at 2 Kgs 2:1, 11 (corpus precedent GEN-WOH-28:12 etc.; central shamayim's numinous-register clause; central human-ascent entry). Keep 'skies' at 1 Kgs 18:45 and 2 Kgs 1:10, 12, 14 (meteorological / Job 1:16 precedent)."}
- summary: "25 verdicts: 22 approve, 3 revise (2:1 and 2:11 'to the skies' -> 'to the heavens', founder decision B; 2:14 commentary reverses the Masoretic accentuation: etnaḥta on ʾēliyyāhû puts ʾap̄-hûʾ with the second half, which supports the adopted line). The changed lines at 2:2, 4, 6 ('as you yourself live') and 2:9, 15, 16 ('ruach') are approved. K/Q at 2:16 verified."
