# Kings wave B (1 Kings 1, 2, 13, 22) — human sign-off package

**Scope:** 1 Kings 1, 2, 13, 22 (`1-kings-woh`) — 187 verses. Second wave of the canon-cited Bible program. Canon-cited sites: 1:50 and 2:28 (the horns of the altar), 13:1–5, 9–10 (the man of the Elohim and the torn altar), 22:19–23 (Mikhayehu's vision of YHWH enthroned among the host of the heavens; the lying ruach).

**Status:** `awaiting-human`, version `1.0.0-rc1`. Source: MT (Sefaria, Tanach with Ta'amei Hamikra; WLC base; PD). Reference: ASV (1901). Conventions from the wave-A sign-off apply (Hebrew long-form names + English in titles; šāmayim by register; quotation marks).

## Summary

| Chapter | Verses | With commentary | Approve | Revise | Flag |
|---|---|---|---|---|---|
| 1 Kings 1 — Shelomoh (Solomon) made king; Adoniyahu (Adonijah) at the horns of the altar | 53 | 40 | 53 | 0 | 0 |
| 1 Kings 2 — David's charge and the securing of the throne of Shelomoh (Solomon) | 46 | 35 | 46 | 0 | 0 |
| 1 Kings 13 — The man of the Elohim from Yehudah and the torn altar at Beit-El (Bethel) | 34 | 28 | 33 | 1 | 0 |
| 1 Kings 22 — The vision of Mikhayehu (Micaiah): YHWH enthroned among the host of the heavens | 54 | 50 | 54 | 0 | 0 |

- The one revise (13:22 punctuation) is fixed; the Reviewer re-checked the quotation-mark pass (112 speech verses, punctuation only) and all fixes: nothing left to revise.
- **Overlay 1-kings-woh 1.0.0 → 1.1.0** (mirror to 2-kings-woh 1.1.0): 6 new entries (sōḵeneṯ 'attendant', shofar, the torn altar, the mauled lion, the threshing floor — direct; the ruach of 22:21–23 — inferred) + 8 extensions of shared wave-A entries.
- **Central 2.78.0 → 2.79.0:** 2 new direct entries (`qarnot-ha-mizbeach-horns-of-the-altar-cross-corpus`, `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus` — the Hebrew-side divine-council entry the Ugaritic council entry asked for), the Ugaritic entry's rationale back-references it, 22 appliesTo-only extensions, `qedeshah` wohChoice now 'qedeshah (fem.) / qadesh (masc.)'. Dry-run against published 2.78.0: clean, no refIds lost.
- **Lens leakage:** none; Wheel of Heaven readings only in labelled reception notes. **Speculative entries:** none.
- **Ketiv/Qere:** 7 readings (Qere translated). MT numbering kept at 22:21–22 and 22:43–54 (ASV equivalences noted).

## Items requiring decision (recommendations)

1. **22:21–24 ruach** (Reviewer flag, the only one): *"And the ruach came forth … 'I will be a lying ruach in the mouth of all his prophets' … the ruach of YHWH"* — keeps the Hebrew article and the transliteration used for *rûaḥ YHWH* in wave A. *Recommended: keep.* Alternative: 'a spirit / a lying spirit / the spirit of YHWH' throughout 21–24 (not a split).
2. **shofar** for ASV 'trumpet' (1:34, 39, 41), as exodus-woh. *Recommended: keep.*
3. **'the qadesh'** at 22:47 for ASV 'sodomites', as the central qedeshah entry requires. *Recommended: keep* (stiff but accurate).
4. **'with all their being'** for nefesh at 2:4 (to be reused at 1 Kgs 8:48). *Recommended: keep.*

Applied mechanically under the wave-A ruling: English names in the four chapter titles.

## Follow-ups (not blocking)
- '1:9 slew' vs '19:21 slaughtered' (same verb) — settle in a Kings consistency pass.
- Hosted ASV 1 Kings has capitalisation/backtick errors (22:8, 22:43, 22:50; backtick apostrophes in chs 1, 2, 13, 22) besides the 8:15/8:43 wording errors.

---

## Editor's escalation report (inlined)

# Kings Wave B Editor Report: the Solomonic succession, the man of the Elohim at Beit-El, Mikhayehu's council

**Book / chapters:** `1-kings-woh` 1 (53 verses), 2 (46), 13 (34), 22 (54). That is 187 verses.
**Editor pass:** 2026-11-01 (claude-opus-5-5, woh-editor role)
**Status at end of pass:** all four chapters `draft` → `editor-review`; version `0.1.0` → `1.0.0-rc1`; `glossaryVersion` 2.79.0 (pending application of the wave-A diff and then the wave-B central diff); `overlayGlossaryVersion` 1.1.0 (pending application of the wave-B overlay diff); `reviewer` left `pending`; `claude-opus-5-5 (editor)` added to `modelDrafts`.
**Editorial questions:** 53 received, 53 resolved, all arrays cleared. None escalated as unresolvable; seven resolutions are flagged below as founder-preference points.

**Files written (only these)**

- `1-kings-woh/chapter-{1,2,13,22}.json`
- `1-kings-woh/wave-b-overlay-diff.json` (proposed overlay diff, not applied; 1-kings-woh 1.0.0 → 1.1.0, with a mirror section for 2-kings-woh 1.0.0 → 1.1.0)
- `1-kings-woh/wave-b-central-diff.json` (proposed central diff, not applied; 2.78.0 → 2.79.0)
- this report

No overlay, central glossary or wave-A file was edited.

**Counts**

- Commentary (`notes.official`): 152 of 187 paragraphs (ch. 1: 40/53, ch. 2: 35/46, ch. 13: 28/34, ch. 22: 49/54). The uncommented verses are plain narrative with no divergence from the ASV.
- Overlay diff: 6 new entries (1-kings-woh only) + 8 additive extensions of shared wave-A entries (mirrored to 2-kings-woh). By claim_type, new entries: direct 5, inferred 1, speculative 0.
- Central diff: 2 new entries (both direct), 1 rationale back-reference update, 22 appliesTo-only extensions.
- English text changed at 34 verses over the draft. Each change is backed by a glossary entry (rule 7):
  - Name normalization (`hebrew-proper-name-transliteration-convention-kings`):
    - *tsade* = *tz*: Tseruyah → Tzeruyah (1:7; 2:5, 22), Tsadoq → Tzadoq (1:8, 26, 32, 34, 38, 39, 44, 45; 2:35), Tsidqiyahu → Tzidqiyahu (22:24), Etsyon-Gever → Etzyon-Gever (22:49).
    - Short theophoric forms: Adoniyah → Adoniyahu (1:5, 7, 18; 2:28); Tsidqiyah → Tzidqiyahu (22:11).
    - Gentilics: 'the Kerethi and the Pelethi' → 'the Kerethites and the Pelethites' (1:38, 44); 'the Gil'adi' → 'the Gil'adite' (2:7); 'the Binyamini' → 'the Binyaminite' (2:8).
  - 'cherish him' / 'cherished the king' → 'be his attendant' / 'became the king's attendant' (1:2, 4): new `sokhenet-attendant-1-kings-1`.
  - 'redeemed my soul' → 'redeemed my life' (1:29); 'with all their soul' → 'with all their being' (2:4): `nefesh-scope-and-spelling-kings`.
  - 'trumpet' → 'shofar' (1:34, 39, 41): new `shofar-coronation-signal-1-kings-1`.
  - 'torn' → 'mauled' for the lion's *šbr* (13:26, 28): new `shavar-the-lion-mauled-1-kings-13`.
  - 'in an open place' → 'at the threshing floor' (22:10): new `goren-threshing-floor-1-kings-22-10`.
  - 'the host of the skies' → 'the host of the heavens' (22:19): central `shamayim` (numinous-register clause) + new central `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus`.
  - 'a spirit' → 'the ruach' (22:21); 'a lying spirit' → 'a lying ruach' (22:22, 23): new `ha-ruach-ruach-sheqer-the-ruach-and-the-lying-ruach-1-kings-22` (inferred).
  - 'the spirit of YHWH' → 'the ruach of YHWH' (22:24): `ruach-yhwh-and-prophetic-ruach-transliteration-kings` (inferred, extended).
  - 'the sodomites' → 'the qadesh' (22:47): central `qedeshah-consecrated-woman-sacred-prostitution-crux`.
  - 'served the Ba'al' → 'served Ba'al' (22:54): `habbaal-baal-hebrew-bible-rendering-kings`.
  - Chapter 22 title: 'host of the skies' → 'host of the heavens' (follows the 22:19 line).
- All other lines are the Translator's draft, unchanged.

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry is created or extended, either in the overlay diff or in the central diff. Nothing in this pass blocks advance on the speculative count.

The canon-cited sites in this wave are:

- 1 Kgs 1:50 and 2:28 (the horns of the altar read as the levers of a transmitter-receiver)
- 13:1-5 (the altar torn and the hand dried up, read as an 'atomic disintegrator')
- 13:9-10 (the other way, read as concealment of a terrestrial camp)
- 22:19 (the host, read as a vision of the creators)
- 22:22 (the lying spirit, read as 'group telepathy')

At each of them the line renders the Hebrew lexically, and the Raëlian reading appears only in a paragraph headed **"Wheel of Heaven reading (reception note, not a translation claim)"**, as in wave A. Each such paragraph states what *The Book Which Tells the Truth* (ch. 3) says, and that the line does not encode it.

The one new non-direct entry is `ha-ruach-ruach-sheqer-the-ruach-and-the-lying-ruach-1-kings-22` (**inferred**). See founder point B and the lens records below.

---

## Founder-preference points (resolved, flagged for confirmation)

All seven are applied, and each can be reversed mechanically.

### A. Long and short name forms: normalized, against the wording of the brief

- **Decision:** The MT short forms *ʾăḏōniyyâ* (1:5, 7, 18; 2:28) and *ṣiḏqiyyâ* (22:11) are normalized to Adoniyahu and Tzidqiyahu. The MT spelling is recorded in commentary at each site.
- **Why:** The orchestrator's brief describes the wave-A convention as "keeping each verse's long/short form". The wave-A overlay entry that is in force (`hebrew-proper-name-transliteration-convention-kings`) does the opposite: it normalizes *ʾēliyyâ* → Eliyahu and *ʾăḥazyâ* → Achazyahu, and the wave-A Reviewer approved it ("short and long MT forms are normalized with a note"). Wave B's chapters cite that entry, so following the brief would have made the citation false and left the book internally inconsistent. The Translator's draft kept the MT alternation.
- **Reversal:** Revert five lines (1:5, 7, 18; 2:28; 22:11) to Adoniyah / Tzidqiyah, and add a clause to the shared names entry. Wave A would then need the same reversal at 2 Kgs 1:2-12 for consistency.

### B. *rûaḥ* in 1 Kgs 22:21-24: 'the ruach', 'a lying ruach', 'the ruach of YHWH' (inferred)

- **Decision:** The Hebrew article of *hārûaḥ* (22:21) is kept, as the brief asked for a ruling on it. The transliteration 'ruach' is extended through the chain 22:21-24.
- **Why:** Tzidqiyahu's retort at 22:24 ("Which way did the *rûaḥ-YHWH* pass from me ...?") falls under the shared wave-A ruach entry, and it only works if the reader sees the same noun as the council's *rûaḥ* and the *rûaḥ šeqer* of vv 21-23.
- **Precedent for the article:** GKC §126q-r allows the ASV's indefinite reading. The definite reading has standing in JPS 1917 ('there came forth the spirit') and in b. Sanh. 89a, and *haśśāṭān* in the council of Job 1:6 is likewise articular.
- **Risk:** 22:22 is canon-quoted ('a lying spirit' / 'un esprit de mensonge'), and the line now reads 'a lying ruach'. The change is lexical-concordance, not lens: the commentary describes no mechanism, and the canon's telepathy reading sits in the reception note.
- **Alternative:** The ASV wording at 22:21-23 ('a spirit', 'a lying spirit'), with the article noted in commentary, and 'the ruach of YHWH' only at 22:24. Or drop transliteration in ch. 22 entirely and use lower-case 'spirit'.

### C. 22:19 'the host of the heavens' (draft 'skies'), which depends on wave-A founder decision B

- **Decision:** 'the host of the heavens'. The draft applied central `shamayim` 'skies'. The wave-A Reviewer has since recommended 'heaven(s)' at divine-realm *šāmayim* sites (2 Kgs 2:1, 11), on the evidence that genesis-woh context-scales (e.g. GEN-WOH-28:12) and on the entry's own numinous-register clause. 22:19, YHWH's council around his throne, is the clearest divine-realm site in Kings.
- **Lens:** At a canon-cited site, 'skies' is the more lens-congenial register. 'Heavens' (plural, keeping the Hebrew form) is the safer and corpus-consistent choice.
- **Reversal:** If the founder upholds 'skies' at 2 Kgs 2:1, 11, 22:19 should follow. Revert one line plus the chapter title, and change the wohChoice of the new central `tzeva-ha-shamayim-...` entry. Its id would then read better as `...host-of-the-skies...`.
- 'host' (ASV) and 'standing by him' (ASV; *ʿal* of attendants, Gen 18:8; Judg 3:19; Zech 4:14) are kept, as the Translator drafted.

### D. *šôp̄ār* 'shofar' (1:34, 39, 41), against ASV 'trumpet'

- **Decision:** 'shofar', following exodus-woh at Sinai.
- **Why:** Kings also uses the metal *ḥăṣōṣərâ* at an accession (2 Kgs 11:14), so 'trumpet' would merge two instruments the book keeps apart. 'Shofar' is a standard English word.
- **Status:** Overlay entry, and a central-promotion candidate once a third book applies it.
- **Alternative:** 'trumpet' (ASV), or 'horn' (NJPS).

### E. *haqqāḏēš* 'the qadesh' (22:47), against ASV 'sodomites'

- **Decision:** 'the qadesh'. The central `qedeshah-consecrated-woman-sacred-prostitution-crux` (inferred) already names 1 Kgs 22:47 as a site it must govern "uniformly", and it transliterates. This op only adds the refId.
- **Why:** 'Sodomites' imports a link with Sodom and modern senses that the Hebrew lacks.
- **Readability:** The collective singular reads stiffly in English ('the remnant of the qadesh').
- **Alternative:** 'the qedeshim' (a plural not in the text), or 'the consecrated men' (over-resolves, per the central entry).

### F. 'being' for *nepeš* in the heart-and-nepeš pair (2:4), against ASV 'soul'

- **Decision:** 'with all their heart and with all their being'.
- **Why:** The shared nefesh entry keeps 'soul' out of the Kings line. 'Being' follows HALOT ('person, self') and Alter's Deut 6:5.
- **Coordination:** Wave C (1 Kgs 8:48) and later 2 Kgs 23:3, 25 should use the same pair. The extension records this.

### G. Quotation marks: superseded, applied in the rework pass (see the end of this report)

- **Issue:** Wave A's chapters (1 Kgs 17-19; 2 Kgs 1-2) and the wave-C/D drafts (1 Kgs 8) mark direct speech with quotation marks. The wave-B drafts follow the ASV/genesis-woh style without them. Exodus-woh uses quotes; genesis-woh does not.
- **Why not changed here:** It is a presentation convention with no glossary basis. Inserting quotes into roughly 120 speech verses, many with nested speech (e.g. 1:13, 1:30, 2:4, 2:42, 22:13-28), is a separate mechanical pass that should be scripted and proof-read once for the whole book.
- **Recommendation:** Adopt quotation marks book-wide, to match wave A, before the Kings books ship.

---

## Lens-discipline records (for the Reviewer)

1. **1:50; 2:28: horns of the altar** (new central `qarnot-ha-mizbeach-horns-of-the-altar-cross-corpus`, direct).
   - 'the horns of the altar', as in every major version.
   - The commentary gives the asylum custom (Ex 21:13-14) and the archaeology (Tel Be'er Sheva, Aharoni 1974).
   - The canon's 'levers of the transmitter-receiver' reading is confined to reception notes, and the entry's rationale states it claims nothing beyond the lexical, cultic and archaeological sense.
2. **13:1-5: the man of the Elohim at Beit-El.**
   - 'torn' (Niphal *qrʿ*; new `niqra-ha-mizbeach-the-altar-torn-1-kings-13`), chosen for the Yarov'am-narrative keyword (11:11-13, 30-31; 14:8). The canon's English 'rent' is the same sense.
   - 'dried up' (*yāḇēš*; ASV and canon).
   - 'sign' (*môp̄ēṯ*; ASV).
   - The commentary says explicitly that the Hebrew names neither a burn nor a device.
3. **13:9-10.** The prohibition is rendered as given. The reception note records the canon's concealment reading and that the text gives no reason.
4. **22:19.** See founder point C. The new central entry carries an explicit apparatus-only disavowal ("the line encodes neither a fleet nor personnel").
5. **22:21-23.** See founder point B. The inferred claim_type is assigned because the article and the transliteration leave open readings that the major versions close.
6. **22:24.** 'the ruach of YHWH' (lower case). The ASV capital is avoided for the doctrinal reason given in the shared entry, not for a lens reason.
7. **Non-extensions.** These central entries are cited in commentary but deliberately not applied, because their wohChoice does not govern the Kings line:
   - `eshet-yefat-mareh` (1:3-4, *naʿărâ yāp̄â* is not the full formula; the draft's citation is kept)
   - `qadad-bow-the-head-paired-prostration-formula` (1:16)
   - `haed-heid-solemn-warning-formula` (2:42, draft 'warn' vs entry 'did solemnly protest')
   - `pilegesh-concubine-status-class` (2:13, Avishag is never called *pîlegeš*)
   - `misped-lamentation-vocabulary-cross-corpus` (13:29)
   - `eshel-tamarisk-cultic-site` (13:14, *ʾēlâ* not *ʾešel*)
   - `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible` (22:19, Ugaritic; it receives a back-reference instead)
   - `hishtachavah-bow-down-obeisance-worship` (its Genesis wording 'made obeisance' is not imported)
   - `elohim-as-translation` keeps the draft's glossaryRefs but is not extended (wave-A practice).

---

## Unresolved editorial questions

**None.** All 53 questions are resolved as follows. "Draft kept" means the Translator's line is unchanged.

### 1 Kings 1 (16)

| refId | Question | Resolution |
|---|---|---|
| 1:2 | *sōḵeneṯ* 'cherish' | **Changed** to 'be his attendant' / 'became the king's attendant' (1:2, 4); `sokhenet-attendant-1-kings-1` |
| 1:5 | Adoniyah / Adoniyahu | Normalized to the long form (1:5, 7, 18; 2:28; also 22:11 Tzidqiyahu); names entry (Founder point A) |
| 1:7 | *ts* vs *tz*; Moshe; Hevron/Gihon/Ophir | **tz** per the wave-A names entry (Tzarfat, Tzidon) and genesis-woh Yitzchaq; Moshe kept (Exodus 'Moses' exception not extended); genesis-woh spellings kept |
| 1:9 | *zbḥ* | 'slew' kept; sacrificial-feast sense in commentary (wave A has 'slaughtered' at 19:21) |
| 1:12 | *nepeš* | 'life' kept (1:12; 2:23); ASV 'soul' replaced at 1:29 ('my life') and 2:4 ('being'); `nefesh-scope-and-spelling-kings` |
| 1:18 | MT *wəʿattâ* vs *wəʾattâ* | MT kept; versions in commentary; MT-baseline entry |
| 1:19 | *śar haṣṣāḇāʾ* | 'captain of the host' kept (lexical link with 22:19) |
| 1:27 | Ketiv/Qere | Qere 'your servant'; ASV follows the Ketiv; Ketiv/Qere entry |
| 1:29 | *ḥay-YHWH* | 'As YHWH lives' kept; central `chei-x-oath-by-the-life-formula` extended (1:29; 2:24; 22:14) |
| 1:34 | *šôp̄ār* | **Changed** to 'shofar' (1:34, 39, 41); `shofar-coronation-signal-1-kings-1` (Founder point D) |
| 1:35 | *nāḡîḏ* | 'prince' kept; 'leader-designate' sense in commentary |
| 1:37 | Ketiv/Qere | Qere, read optatively ('may he be'); Ketiv/Qere entry |
| 1:38 | Kerethi / Pelethi | **Changed** to 'the Kerethites and the Pelethites' (1:38, 44), gentilic '-ite' clause added to the names entry (also 2:7, 8) |
| 1:40 | *ʾereṣ*; LXX 'resounded' | 'the earth split' kept; central `eretz` not applied to the physical ground; LXX in commentary |
| 1:47 | Ketiv/Qere | Qere 'May Elohim make' kept; Ketiv/Qere + elohim-referent clause 2 |
| 1:50 | *qarnôṯ hammizbēaḥ* | 'the horns of the altar' kept; new central `qarnot-ha-mizbeach-horns-of-the-altar-cross-corpus`; reception note |

### 1 Kings 2 (7)

| refId | Question | Resolution |
|---|---|---|
| 2:2 | 'the way of all the earth' | ASV 'earth' kept; `eretz` not applied |
| 2:3 | *tôraṯ mōšeh*; Moshe | 'the law of Moshe' kept (Deuteronomistic law-book phrase); Moshe per names entry |
| 2:23 | oath formula with anarthrous *ʾĕlōhîm* | 'So may Elohim do to me, and more also' kept; elohim-referent clause 2 (contrast 19:2) |
| 2:24 | Ketiv/Qere (orthographic) | Qere; Ketiv/Qere entry |
| 2:28 | MT 'Avshalom' vs versions 'Shelomoh' | MT kept; MT-baseline entry |
| 2:28 | horns of the altar | As 1:50; reception note |
| 2:46 | LXX supplements 2:35a-o, 2:46a-l | MT only; supplements described in commentary at 2:35, 46 (and the LXX plus at 2:29); MT-baseline entry |

### 1 Kings 13 (14)

| refId | Question | Resolution |
|---|---|---|
| 13:1 | article in *ʾîš (hā)ʾĕlōhîm* | Shared convention applied: 'a man of Elohim' (13:1) / 'the man of the Elohim' (14 articular occurrences, vv 4-31). Draft kept. The construct-definiteness point is recorded in the entry and the commentary |
| 13:2 | *bāmôṯ* | 'high places' kept (13:2, 32, 33; 22:44); commentary |
| 13:3 | *môp̄ēṯ* | 'sign' kept |
| 13:3 | Niphal *qrʿ* | 'torn' kept; `niqra-ha-mizbeach-the-altar-torn-1-kings-13` |
| 13:4 | *wattîḇaš yāḏô* | 'dried up' kept; reception note |
| 13:6 | *ḥal-nāʾ ʾeṯ-pənê YHWH* | ASV kept in both places; literal in commentary |
| 13:11 | MT 'his son' | MT kept; MT-baseline entry |
| 13:12 | MT Qal 'had seen' | MT kept; MT-baseline entry |
| 13:18 | *malʾāḵ* | 'a messenger' kept; central `malakh-yhwh-messenger` extended |
| 13:20 | mid-verse (פ) | No English break (wave-A practice at 2 Kgs 1:17); central `piska-b-emtza-pasuq-masoretic-paragraph-break` extended |
| 13:21 | *mārîṯā pî YHWH* | 'disobeyed the mouth of YHWH' kept |
| 13:22 | *nəḇēlâ* | 'body' kept; 'corpse' sense in commentary |
| 13:24 | lion episode; 'donkey' | 'met' kept; *šbr* **changed** 'torn' → 'mauled' (13:26, 28) to keep 'torn' for *qrʿ*; `shavar-the-lion-mauled-1-kings-13`; 'donkey' kept |
| 13:33 | *millēʾ ʾeṯ-yāḏô* | 'he consecrated him' kept; 'filled his hand' in commentary |

### 1 Kings 22 (16)

| refId | Question | Resolution |
|---|---|---|
| 22:6 | MT *ʾăḏōnāy* | 'the Lord' kept; MSS 'YHWH' in commentary; MT-baseline entry |
| 22:10 | *bəḡōren* | **Changed** to 'at the threshing floor'; `goren-threshing-floor-1-kings-22-10` |
| 22:11 | Tzidqiyah / Tzidqiyahu | Normalized to Tzidqiyahu (Founder point A); 'horns of iron' literal |
| 22:13 | Ketiv/Qere | Qere; Ketiv/Qere entry |
| 22:19 | host / skies / 'standing by' | 'host' and 'standing by him' kept; *šāmayim* **changed** to 'heavens' (Founder point C); new central `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus`; reception note |
| 22:20 | Piel *pth* | 'entice' kept |
| 22:21 | *hārûaḥ* article; *rûaḥ*; versification | **Changed** to 'And the ruach came forth' (article kept; Founder point B); MT verse division kept, ASV equivalence noted |
| 22:22 | *rûaḥ šeqer* | **Changed** to 'a lying ruach' (22:22, 23); same entry; reception note |
| 22:24 | *rûaḥ-YHWH* | **Changed** to 'the ruach of YHWH' (lower case); shared ruach entry extended |
| 22:28 | 'Hear, you peoples, all of you' | MT translated in full; probable addition (Mic 1:2; absent from LXX) noted |
| 22:38 | *wəhazzōnôṯ rāḥāṣû* | 'washed themselves' kept (intransitive Qal); LXX in commentary |
| 22:43 | MT vs English numbering | MT numbering kept; MT = ASV equivalence noted at every verse 22:43-54 |
| 22:47 | *haqqāḏēš* | **Changed** to 'the qadesh'; central `qedeshah-...` extended (Founder point E) |
| 22:48 | *niṣṣāḇ meleḵ* | 'a deputy was king' kept |
| 22:49 | two Ketiv/Qere | Qere both ('made', 'were broken'); Ketiv/Qere entry |
| 22:54 | *habbaʿal* | **Changed** to 'served Ba'al' (no English article, wave-A rule); `habbaal-baal-hebrew-bible-rendering-kings` |

---

## Glossary changes for review

### Per-translation overlay (`1-kings-woh/wave-b-overlay-diff.json`, not applied)

The file is a JSON object. It targets `1-kings-woh/_translation-glossary.json` 1.0.0 → **1.1.0** (semver-minor: additions and additive extensions only). Its `mirror` section targets `2-kings-woh/_translation-glossary.json` 1.0.0 → 1.1.0.

Shared-entry ops use **op=extend**, which is additive only: strings in `appendToFields` are appended to the current field, and refIds in `addToAppliesTo` are added. This lets the diff apply cleanly on top of the wave-A Reviewer's pending revisions of the shared entries (e.g. the Ruth 1:17 fix in `elohim-referent-and-article-conventions-kings`). Each extend op carries `mirrorTo: ["2-kings-woh/_translation-glossary.json"]`, so the nine shared entries stay identical.

**Added (1-kings-woh only):**

- `sokhenet-attendant-1-kings-1` (claim_type: `direct`): 1:2, 4
- `shofar-coronation-signal-1-kings-1` (claim_type: `direct`): 1:34, 39, 41; central-promotion candidate
- `niqra-ha-mizbeach-the-altar-torn-1-kings-13` (claim_type: `direct`): 13:3, 5
- `shavar-the-lion-mauled-1-kings-13` (claim_type: `direct`): 13:26, 28
- `goren-threshing-floor-1-kings-22-10` (claim_type: `direct`): 22:10
- `ha-ruach-ruach-sheqer-the-ruach-and-the-lying-ruach-1-kings-22` (claim_type: `inferred`): 22:21, 22, 23

**Extended (shared, mirrored; no existing text or refId changed):**

- `hebrew-proper-name-transliteration-convention-kings`: wohChoice and rationale appended (wave-B equivalence table; short-form normalization; tsade = tz; gentilic '-ite'; Moshe). appliesTo +137 refIds (every wave-B verse with a transliterated name).
- `nefesh-scope-and-spelling-kings`: wohChoice and rationale appended ('life' at 1:12, 29; 2:23; 'being' at 2:4). appliesTo +4.
- `ish-ha-elohim-man-of-the-elohim-prophetic-title-kings`: wohChoice and rationale appended (13:1 anarthrous, 14 articular; construct-definiteness note). appliesTo +13.
- `elohim-referent-and-article-conventions-kings`: wohChoice appended (clause 2: 1:47, 2:23). appliesTo +2. The rationale is untouched, so the Reviewer's Ruth fix applies independently.
- `ketiv-qere-qere-translated-kings`: wohChoice and rationale appended (seven readings; ASV follows the Ketiv at 1:27, 47). appliesTo +6.
- `mt-baseline-at-versional-cruxes-and-versification-kings`: wohChoice appended (ten cruxes, the LXX pluses and supplements, versification at 22:21-22 and 22:43-54). appliesTo +27.
- `habbaal-baal-hebrew-bible-rendering-kings`: wohChoice appended (22:54). appliesTo +1.
- `ruach-yhwh-and-prophetic-ruach-transliteration-kings` (inferred): wohChoice and rationale appended (prophetic-inspiration sense, 22:24; pointer to the new 22:21-23 entry). appliesTo +1.

Not extended: `yhwh-tsevaot-yhwh-of-hosts-kings` (no occurrence in wave B).

### Central glossary (`1-kings-woh/wave-b-central-diff.json`, not applied)

The file uses the same format as `wave-a-central-diff.json`. It is a JSON list. Its first element is `{"op":"version","from":"2.78.0","to":"2.79.0", ...}` and carries a ready-to-paste `scopeNoteAddendum`. The remaining elements are add/modify ops, where modify `changes` replace the field outright and appliesTo values are complete arrays.

**Base:** the 2.77.0 export plus the wave-A diff. The wave-A diff must be applied first. For the nine entries that wave A also extends (`chei-x-oath`, `navi`, `darash-yhwh`, `davar-yhwh`, `malakh-yhwh-messenger`, `shamayim`, `adam-adamah`, `piska`, `bethel-luz`), the arrays start from the wave-A arrays.

**Version recommendation: 2.79.0** (minor). The diff contains additions and appliesTo extensions, plus one rationale cross-reference. No wohChoice is changed and no decision is reversed, so the result is minor under both the role-doc rule and house practice.

- **Added:**
  - `qarnot-ha-mizbeach-horns-of-the-altar-cross-corpus` (claim_type: `direct`): 1KI-WOH-1:50, 1:51, 2:28. Canon-cited; reception in apparatus only.
  - `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus` (claim_type: `direct`): 1KI-WOH-22:19. Canon-cited. This is the Hebrew-side divine-council entry that the Ugaritic `divine-council-phr-mad-...` entry asked for. Its wohChoice depends on Founder point C.
- **Modified (rationale cross-reference only):**
  - `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible`: the sentence "Future Hebrew Editor pass on Ps 82, Job 1, or 1 Kgs 22 should produce the Hebrew central entry ..." is replaced by a pointer to the new entry. The text notes that a *sôḏ*/*ʿēḏâ* entry is left for Psalms/Jeremiah. wohChoice and appliesTo are unchanged.
- **Modified (appliesTo extensions only; 22 entries):**
  - Formulas and recurring phrases:
    - `chei-x-oath-by-the-life-formula`: 1:29; 2:24; 22:14
    - `shakhav-im-avotav-death-formula`: 1:21; 2:10; 22:40, 51
    - `mishmeret-mitzvot-chuqim-torot-fourfold-covenant`: 2:3
    - `hithallekh-lefanai-patriarchal-walking-before-elohim-covenantal-formula`: 2:4
    - `elohim-imkha-divine-presence-formula`: 1:37
    - `darash-yhwh-seeking-oracle`: 22:5, 7, 8
    - `davar-yhwh-prophetic-formula`: 13:20
    - `mot-tamut`: 2:37, 42
    - `elohei-yisrael`: 1:30, 48; 22:54
  - Lexemes:
    - `navi-first-occurrence-abraham`: 23 refIds
    - `malakh-yhwh-messenger`: 13:18
    - `shamayim`: 22:19, under its numinous-register clause
    - `adam-adamah`: 13:2, 34
    - `eretz`: 22:36, 47
    - `saris-court-official-eunuch-ambiguity`: 22:9
    - `sheol-underworld-realm-of-the-dead`: 2:6, 9
    - `chesed-solitary-covenant-kindness`: 2:7
    - `zonah-prostitute-status-vocabulary-cross-corpus`: 22:38
    - `qedeshah-consecrated-woman-sacred-prostitution-crux`: 22:47. The rendering changes to 'the qadesh', as the entry's rationale already required.
  - Names and text features:
    - `adonai-yhwh-divine-name`: 2:26
    - `piska-b-emtza-pasuq-masoretic-paragraph-break`: 13:20
    - `bethel-luz-name-etymology`: 13:1, 4, 10, 11, 32

**Dependencies:**

- If neither diff is applied, the chapters point at seven entries that do not yet exist: six overlay entries plus `qarnot-...` and `tzeva-...`.
- If the wave-A Reviewer's revision of central `shamayim` changes its rationale, the wave-B op on that entry is appliesTo-only and can be applied after it unchanged.

---

## Notes for the Reviewer

- **Wave-A Reviewer findings that bear on wave B** (read in `wave-a-signoff-package.md` after the draft notes were written):
  - The 'heavens' recommendation was adopted at 22:19 (Founder point C).
  - The `elohim-referent` Ruth 1:17 fix is untouched by this diff.
  - The proposed English forms in chapter titles ('Eliyahu (Elijah)') were not applied to wave-B titles. If the founder adopts that recommendation, apply it to all Kings titles in one pass.
- **Scholarly authorities cited:**
  - Kings commentaries: Cogan, *1 Kings* (AB 10, 2001); Gray, *I & II Kings* (OTL); Sweeney, *I & II Kings* (OTL, 2007); De Vries, *1 Kings* (WBC 12, 1985); Noth
  - Lexica and grammars: BDB, HALOT, GKC, Joüon-Muraoka
  - Other works:
    - Aharoni, *BA* 37 (1974)
    - Vaughan, *The Meaning of 'bāmâ'* (1974)
    - von Rad, *Studies in Deuteronomy* (1953)
    - Wolff (1974)
    - Bird (1997); Budin (2008)
    - Roberts, VTSup 40 (1988)
    - Moberly, *HTR* 96 (2003)
    - Crowfoot and Crowfoot (1938)
    - Mullen (1980); Handy (1994); Smith (2001)
    - Braun (2002)
    - KTU 1.17 V 6-8
    - b. Sanh. 89a
- **Claims worth spot-checking:**
  - The versional claims (most were already in the Translator's questions; verify at the Reviewer's discretion): the LXX first-person suffixes at 2:5, the LXX plus at 2:29, the Lucianic 'companions' at 1:8, and NJPS 'became rigid' at 13:4.
  - Page numbers are omitted throughout.
- **Verse numbering** follows the MT. The divergences are 22:21-22 (one clause) and 22:43-54 (MT one verse ahead), noted at each verse.
- **Masoretic section marks** are kept in the Hebrew text and noted where structurally relevant. 13:20 has the mid-verse *pisqa*.
- **'man of the Elohim':** the Hebrew has 14 articular occurrences in ch. 13 (not 15 as the draft question said), verified in the source.
- **Coordination with wave C (1 Kgs 8):** use 'being' for *nap̄šām* in the heart-and-nepeš pair at 8:48. Quotation marks are already used there (Founder point G).

---

## Rework pass after review (2026-11-01)

The Reviewer approved 186 of 187 verses. Its requests were applied as follows; status stays `awaiting-human` and `reviewerReport` is untouched.

1. **Quotation marks (blocking).** Wave-A style is now applied throughout the wave: double quotes for direct speech, single quotes for speech inside speech, and double quotes again at the third level (13:22, 22:27). A speech that runs across verses is opened once and closed at its end with no reopening at verse starts, as in 17:13-14 and 18:9-14. Punctuation only: a script checked that every changed line keeps the reviewed wording word for word, and that quotes balance per chapter. Speech verses changed:
   - ch. 1: 32
   - ch. 2: 28
   - ch. 13: 21
   - ch. 22: 31
   - total: 112
2. **13:22.** The quoted ban now closes at *māyim*: `... he said to you, "Eat no bread and drink no water"; your body shall not come to the grave of your fathers.'"` This is the third quote level inside the oracle of v 21.
3. **Notes.**
   - Process language removed at 1:5, 1:7, 1:9, 1:38, 2:40, 13:1, 13:20, 13:26, 22:19 and 22:54; verse references are used instead.
   - The book is named where notes said "the English edition of the canon" (13:1, 3, 4; 22:19, 22).
   - New note at 22:37: the Hebrew verb is active, and 'was brought' is a sense rendering.
   - 2:28: the "after Shelomoh" reading is now attributed to "Greek witnesses, the Syriac and the Vulgate". I could not verify whether the main LXX text has it as well as the Lucianic.
   - 22:19: the BDB citation is now "BDB s.v. *ʿal*". The 22:19 note also no longer grounds 'heavens' in the numinous-register clause.
4. **Diffs.**
   - Central `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus`: wohChoice and the rationale's Rendering paragraph now ground 'heavens' in the wave-A Reviewer's recommendation for divine-realm *šāmayim*, pending founder decision B, with an explicit reversion path to 'the host of the skies'. The `shamayim` op's reason says the same.
   - Central `qedeshah-consecrated-woman-sacred-prostitution-crux`: wohChoice is now "qedeshah (fem.) / qadesh (masc.) (transliterated; ...)". This is the one wohChoice edit in the central diff. It extends the same decision, so 2.79.0 (minor) is still recommended.
   - Overlay Ba'al extension: the "draft ... aligned" remark moved from the appended wohChoice text to the op's reason.


---

## Reviewer report (non-approve verdicts and report fields)

### 1 Kings 1 — Shelomoh (Solomon) made king; Adoniyahu (Adonijah) at the horns of the altar



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:54:32Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "approve", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice and wave-A overlay v1.0.0 (checked in the data)"], "reasoning": "Op=extend, additive and mirrored. The base entries are verified identical in both Kings overlays (v1.0.0), so the mirrored append keeps them in sync. The equivalence table is checked against every wave-B line. Short-form normalization (ʾăḏōniyyâ 1:5, 7, 18; 2:28; ṣiḏqiyyâ 22:11) follows the rule in force for ʾēliyyâ/ʾăḥazyâ, with the MT spelling noted at each site. tz for tsade matches Tzarfat/Tzidon and genesis-woh. The gentilic '-ite' rule is consistent. Content approved; the base entry remains under the open founder decision A from wave A."}, {"glossary_id": "nefesh-scope-and-spelling-kings", "status": "approve", "citations": ["HALOT s.v. nepeš", "Wolff, Anthropology of the Old Testament (1974), ch. on nepeš", "Alter, The Five Books of Moses (2004), Deut 6:5"], "reasoning": "'Life' at 1:12, 29; 2:23 and 'being' in the heart-and-nepeš pair at 2:4 are lexically sound and keep the dualist 'soul' out of the line, consistent with central nefesh-chayah. The coordination note for 1 Kgs 8:48 and 2 Kgs 23:3, 25 is useful."}, {"glossary_id": "elohim-referent-and-article-conventions-kings", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "GKC §17 (Qere and Ketiv)"], "reasoning": "1:47 (Qere ʾĕlōhîm, YHWH referent, anarthrous) an
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 53 English lines: no lens leakage. 1:50-51 'horns of the altar' is literal, as in every major version. The canon reading (TBWTT ch. 3 ¶100: levers of a transmitter-receiver; verified in data-library) appears only in the labelled reception note at 1:50. 'Shofar', 'attendant' and the transliterated names are lexical and presentation choices with no interpretive content."
- chapterLevelRevisions: [{"item": "quotation-marks", "status": "revise", "reasoning": "The wave-B English lines have no quotation marks. Wave A (1 Kgs 17-19; 2 Kgs 1-2) and the wave-C/D drafts mark direct speech with double quotes, nested single quotes, and speeches that stay open across verses. The book cannot ship with two conventions. Before founder sign-off, the Editor should add quotation marks book-wide in wave-A style. A script may propose them, but each speech verse must be proofread by hand: the chapters have multi-verse speeches (1:17-21, 1:24-27, 2:2-9, 2:42-45) and triple nesting at 22:19-23 (Mikhayehu > YHWH > the ruach). The wording itself is approved; after the pass, the Reviewer re-checks only the punctuation."}]
- nonBlockingFixes: ["Notes at 1:5, 1:7, 1:9, 1:38: replace process language ('wave A', 'the draft's ts ... throughout the wave') with verse references.", "1:9: unify the rendering of zbḥ across the book ('slew' 1:9, 19, 25 vs 'slaughtered' 19:21) in a later concordance pass."]
- escalationReportAdjustments: "The initial verdicts on all verses, overlay ops and central ops were formed from the chapters, the source, the overlays and the diffs (with mechanical checks of the appliesTo bases, the shared-entry identity across the two Kings overlays, the Qere inventory, the section marks, the versification and the TBWTT ch. 3 citations) before wave-b-editor-report.md was opened. After reading it, no verdict changed. The report confirms the quotation-mark gap (its point G), which matches the Reviewer's independent chapter-level finding, and it states that 22:19 and the tzeva entry depend on founder decision B, which supports the revise on that entry's rationale. The report's spot-check items were reviewed: NJPS 'became rigid' (13:4) agrees with the Reviewer's recollection; the 2:5 LXX first-person suffixes and the 2:29 LXX plus are plausible and described with appropriate hedging. The Lucianic attribution at 2:28 remains a non-blocking query."
- founderDecisionRecommendations: {"A-proper-names": "Retain transliteration with long-form normalization of the MT short forms (Adoniyahu, Tzidqiyahu), tz for tsade and English '-ite' gentilics. This is the rule already in force in the wave-A overlay and approved by the wave-A Reviewer. Following the brief's 'keep each verse's form' would have made the chapters cite an entry that says the opposite. The choice is mechanically reversible. As wave A recommended, add the English form to chapter titles for discoverability.", "B-ruach-22:21-24": "Keep as drafted: 'the ruach' (article kept), 'a lying ruach', 'the ruach of YHWH'. The v 24 retort depends on the noun staying visible, the article has standing (JPS 1917; b. Sanh. 89a; GKC §126q), and the entry is honestly inferred. If the founder prefers conventional English, use lower-case 'spirit' consistently at 21-24 (with the article recorded in the note); do not split 'spirit' (21-23) from 'ruach' (24).", "C-heavens-22:19": "Adopt 'the host of the heavens'. It is consistent with the wave-A Reviewer's decision-B recommendation ('heavens' for divine-realm šāmayim, 'skies' for weather and fire), the corpus precedent at GEN-WOH-28:12, and the canon French 'l'armée des cieux'. If decision B goes to 'skies' everywhere, revert 22:19, the chapter-22 title and the tzeva entry together.", "D-shofar": "Adopt 'shofar'. It is lexically exact, it keeps šôp̄ār apart from ḥăṣōṣərâ (2 Kgs 11:14), and it matches exodus-woh. Promote to central when a third book applies it.", "E-the-
- summary: "53 verdicts: 53 approve, 0 revise, 0 flag-for-human. Chapter-level revise: add quotation marks in wave-A style (Founder point G). Status awaiting-human: quotation-mark pass, founder decisions A (names) and B (šāmayim) from wave A, and the glossary revisions."
- recheckAddendum: {"reviewer": "claude-opus-5-5 acting as woh-reviewer", "recheckedAt": "2026-11-01T11:02:36Z", "scope": "Editor rework of the wave-B findings, diffed against the pre-rework copies (scratchpad/waveb/pre-rework).", "findings": "Diffed all English lines: 32 changed, and the only change is quotation marks; wording is identical and the Hebrew text and glossaryRefs are untouched. A stack simulation over the chapter finds every quote balanced: multi-verse speeches stay open across verses and close correctly, and nothing is left open at the chapter end. The style matches wave A (double quotes, nested single quotes, a speech opening after 'saying,'). No unquoted direct speech remains. Note fixes verified: process language removed, The Book Which Tells the Truth named, BDB s.v. ʿal at 22:19, and the 22:37 note added. Chapter-level quotation-mark revise: RESOLVED.", "titleRecommendation": {"current": "1 Kings 1 — Shelomoh made king; Adoniyahu at the horns of the altar", "proposed": "1 Kings 1 — Shelomoh (Solomon) made king; Adoniyahu (Adonijah) at the horns of the altar", "reason": "Founder decision A (ratified with wave A) adds the English name in parentheses, following the wave-A titles ('Eliyahu (Elijah) ...'). Title not edited by the Reviewer."}, "remaining": ["Chapter title needs the English-name parenthetical (proposed above)."]}

### 1 Kings 2 — David's charge and the securing of the throne of Shelomoh (Solomon)



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:54:32Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "approve", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice and wave-A overlay v1.0.0 (checked in the data)"], "reasoning": "Op=extend, additive and mirrored. The base entries are verified identical in both Kings overlays (v1.0.0), so the mirrored append keeps them in sync. The equivalence table is checked against every wave-B line. Short-form normalization (ʾăḏōniyyâ 1:5, 7, 18; 2:28; ṣiḏqiyyâ 22:11) follows the rule in force for ʾēliyyâ/ʾăḥazyâ, with the MT spelling noted at each site. tz for tsade matches Tzarfat/Tzidon and genesis-woh. The gentilic '-ite' rule is consistent. Content approved; the base entry remains under the open founder decision A from wave A."}, {"glossary_id": "nefesh-scope-and-spelling-kings", "status": "approve", "citations": ["HALOT s.v. nepeš", "Wolff, Anthropology of the Old Testament (1974), ch. on nepeš", "Alter, The Five Books of Moses (2004), Deut 6:5"], "reasoning": "'Life' at 1:12, 29; 2:23 and 'being' in the heart-and-nepeš pair at 2:4 are lexically sound and keep the dualist 'soul' out of the line, consistent with central nefesh-chayah. The coordination note for 1 Kgs 8:48 and 2 Kgs 23:3, 25 is useful."}, {"glossary_id": "elohim-referent-and-article-conventions-kings", "status": "approve", "citations": ["BDB s.v. ʾĕlōhîm", "GKC §17 (Qere and Ketiv)"], "reasoning": "1:47 (Qere ʾĕlōhîm, YHWH referent, anarthrous) an
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 46 English lines: no lens leakage. 2:28 'horns of the altar' is literal, with the canon reading confined to a labelled reception note. 'With all their being' (2:4) is a lexical choice, not a lens one."
- chapterLevelRevisions: [{"item": "quotation-marks", "status": "revise", "reasoning": "The wave-B English lines have no quotation marks. Wave A (1 Kgs 17-19; 2 Kgs 1-2) and the wave-C/D drafts mark direct speech with double quotes, nested single quotes, and speeches that stay open across verses. The book cannot ship with two conventions. Before founder sign-off, the Editor should add quotation marks book-wide in wave-A style. A script may propose them, but each speech verse must be proofread by hand: the chapters have multi-verse speeches (1:17-21, 1:24-27, 2:2-9, 2:42-45) and triple nesting at 22:19-23 (Mikhayehu > YHWH > the ruach). The wording itself is approved; after the pass, the Reviewer re-checks only the punctuation."}]
- nonBlockingFixes: ["2:28 note: 'the Lucianic Greek' should probably read 'the LXX (both main traditions)'; verify against Rahlfs/BHS.", "2:40 note: 'throughout the wave' should read 'throughout 1 Kings'."]
- escalationReportAdjustments: "The initial verdicts on all verses, overlay ops and central ops were formed from the chapters, the source, the overlays and the diffs (with mechanical checks of the appliesTo bases, the shared-entry identity across the two Kings overlays, the Qere inventory, the section marks, the versification and the TBWTT ch. 3 citations) before wave-b-editor-report.md was opened. After reading it, no verdict changed. The report confirms the quotation-mark gap (its point G), which matches the Reviewer's independent chapter-level finding, and it states that 22:19 and the tzeva entry depend on founder decision B, which supports the revise on that entry's rationale. The report's spot-check items were reviewed: NJPS 'became rigid' (13:4) agrees with the Reviewer's recollection; the 2:5 LXX first-person suffixes and the 2:29 LXX plus are plausible and described with appropriate hedging. The Lucianic attribution at 2:28 remains a non-blocking query."
- founderDecisionRecommendations: {"A-proper-names": "Retain transliteration with long-form normalization of the MT short forms (Adoniyahu, Tzidqiyahu), tz for tsade and English '-ite' gentilics. This is the rule already in force in the wave-A overlay and approved by the wave-A Reviewer. Following the brief's 'keep each verse's form' would have made the chapters cite an entry that says the opposite. The choice is mechanically reversible. As wave A recommended, add the English form to chapter titles for discoverability.", "B-ruach-22:21-24": "Keep as drafted: 'the ruach' (article kept), 'a lying ruach', 'the ruach of YHWH'. The v 24 retort depends on the noun staying visible, the article has standing (JPS 1917; b. Sanh. 89a; GKC §126q), and the entry is honestly inferred. If the founder prefers conventional English, use lower-case 'spirit' consistently at 21-24 (with the article recorded in the note); do not split 'spirit' (21-23) from 'ruach' (24).", "C-heavens-22:19": "Adopt 'the host of the heavens'. It is consistent with the wave-A Reviewer's decision-B recommendation ('heavens' for divine-realm šāmayim, 'skies' for weather and fire), the corpus precedent at GEN-WOH-28:12, and the canon French 'l'armée des cieux'. If decision B goes to 'skies' everywhere, revert 22:19, the chapter-22 title and the tzeva entry together.", "D-shofar": "Adopt 'shofar'. It is lexically exact, it keeps šôp̄ār apart from ḥăṣōṣərâ (2 Kgs 11:14), and it matches exodus-woh. Promote to central when a third book applies it.", "E-the-
- summary: "46 verdicts: 46 approve, 0 revise, 0 flag-for-human. Chapter-level revise: add quotation marks in wave-A style (Founder point G). Status awaiting-human: quotation-mark pass, founder decisions A (names) and B (šāmayim) from wave A, and the glossary revisions."
- recheckAddendum: {"reviewer": "claude-opus-5-5 acting as woh-reviewer", "recheckedAt": "2026-11-01T11:02:36Z", "scope": "Editor rework of the wave-B findings, diffed against the pre-rework copies (scratchpad/waveb/pre-rework).", "findings": "Diffed all English lines: 28 changed, and the only change is quotation marks; wording is identical and the Hebrew text and glossaryRefs are untouched. A stack simulation over the chapter finds every quote balanced: multi-verse speeches stay open across verses and close correctly, and nothing is left open at the chapter end. The style matches wave A (double quotes, nested single quotes, a speech opening after 'saying,'). No unquoted direct speech remains. 2:28 note now reads 'Greek witnesses, the Syriac and the Vulgate', which is accurate as stated and resolves the query. Note fixes verified: process language removed, The Book Which Tells the Truth named, BDB s.v. ʿal at 22:19, and the 22:37 note added. Chapter-level quotation-mark revise: RESOLVED.", "titleRecommendation": {"current": "1 Kings 2 — David's charge and the securing of Shelomoh's throne", "proposed": "1 Kings 2 — David's charge and the securing of the throne of Shelomoh (Solomon)", "reason": "Founder decision A (ratified with wave A) adds the English name in parentheses, following the wave-A titles ('Eliyahu (Elijah) ...'). Title not edited by the Reviewer."}, "remaining": ["Chapter title needs the English-name parenthetical (proposed above)."]}

### 1 Kings 13 — The man of the Elohim from Yehudah and the torn altar at Beit-El (Bethel)

- **1KI-WOH-13:22** — revise: The line joins the quoted prohibition and the following curse with a comma ('Eat no bread and drink no water, your body shall not come ...'). With no quotation marks, the curse reads as part of the earlier command, whereas the athnach on māyim closes the ban and lōʾ-ṯāḇôʾ niḇlāṯəḵā begins the sentence. Proposed: '... in the place of which he said to you, "Eat no bread and drink no water"; your body shall not come to the grave of your fathers.' (or with a semicolon and no quotes if quotation marks are not adopted). The wording is otherwise approved.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:54:32Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "approve", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice and wave-A overlay v1.0.0 (checked in the data)"], "reasoning": "Op=extend, additive and mirrored. The base entries are verified identical in both Kings overlays (v1.0.0), so the mirrored append keeps them in sync. The equivalence table is checked against every wave-B line. Short-form normalization (ʾăḏōniyyâ 1:5, 7, 18; 2:28; ṣiḏqiyyâ 22:11) follows the rule in force for ʾēliyyâ/ʾăḥazyâ, with the MT spelling noted at each site. tz for tsade matches Tzarfat/Tzidon and genesis-woh. The gentilic '-ite' rule is consistent. Content approved; the base entry remains under the open founder decision A from wave A."}, {"glossary_id": "ish-ha-elohim-man-of-the-elohim-prophetic-title-kings", "status": "approve", "citations": ["GKC §127a", "Joüon-Muraoka §139a", "Cogan, I Kings (AB 10; 2001), ad loc."], "reasoning": "The count of 1 anarthrous + 14 articular occurrences in ch. 13 is verified in the source. The rationale honestly records that the articular genitive makes the chain definite, so 'the man of Elohim' would also be correct English; the house rule of following the article is a declared convention."}, {"glossary_id": "mt-baseline-at-versional-cruxes-and-versification-kings", "status": "approve", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "Burney, Notes on the Hebrew Text of the Books
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 34 English lines: no lens leakage. 13:3, 5 'torn' and 13:4 'dried up' render the verbs lexically and encode no mechanism. The canon's 'atomic disintegrator' and 'terrestrial camp' readings (TBWTT ch. 3 ¶107-109, verified) are confined to labelled notes at 13:1, 4, 5, 9. The unlabelled mentions of 'the English edition of the canon' at 13:1, 3, 4 only compare wording (they quote the canon's biblical text) and assert no reading. Non-blocking: name The Book Which Tells the Truth there, so that a cold reader can identify the source."
- chapterLevelRevisions: [{"item": "quotation-marks", "status": "revise", "reasoning": "The wave-B English lines have no quotation marks. Wave A (1 Kgs 17-19; 2 Kgs 1-2) and the wave-C/D drafts mark direct speech with double quotes, nested single quotes, and speeches that stay open across verses. The book cannot ship with two conventions. Before founder sign-off, the Editor should add quotation marks book-wide in wave-A style. A script may propose them, but each speech verse must be proofread by hand: the chapters have multi-verse speeches (1:17-21, 1:24-27, 2:2-9, 2:42-45) and triple nesting at 22:19-23 (Mikhayehu > YHWH > the ruach). The wording itself is approved; after the pass, the Reviewer re-checks only the punctuation."}]
- nonBlockingFixes: ["Notes at 13:1, 13:20, 13:26: remove process language ('as wave A does', 'The draft's 'torn' ...').", "13:1, 3, 4: name The Book Which Tells the Truth instead of 'the English edition of the canon'."]
- escalationReportAdjustments: "The initial verdicts on all verses, overlay ops and central ops were formed from the chapters, the source, the overlays and the diffs (with mechanical checks of the appliesTo bases, the shared-entry identity across the two Kings overlays, the Qere inventory, the section marks, the versification and the TBWTT ch. 3 citations) before wave-b-editor-report.md was opened. After reading it, no verdict changed. The report confirms the quotation-mark gap (its point G), which matches the Reviewer's independent chapter-level finding, and it states that 22:19 and the tzeva entry depend on founder decision B, which supports the revise on that entry's rationale. The report's spot-check items were reviewed: NJPS 'became rigid' (13:4) agrees with the Reviewer's recollection; the 2:5 LXX first-person suffixes and the 2:29 LXX plus are plausible and described with appropriate hedging. The Lucianic attribution at 2:28 remains a non-blocking query."
- founderDecisionRecommendations: {"A-proper-names": "Retain transliteration with long-form normalization of the MT short forms (Adoniyahu, Tzidqiyahu), tz for tsade and English '-ite' gentilics. This is the rule already in force in the wave-A overlay and approved by the wave-A Reviewer. Following the brief's 'keep each verse's form' would have made the chapters cite an entry that says the opposite. The choice is mechanically reversible. As wave A recommended, add the English form to chapter titles for discoverability.", "B-ruach-22:21-24": "Keep as drafted: 'the ruach' (article kept), 'a lying ruach', 'the ruach of YHWH'. The v 24 retort depends on the noun staying visible, the article has standing (JPS 1917; b. Sanh. 89a; GKC §126q), and the entry is honestly inferred. If the founder prefers conventional English, use lower-case 'spirit' consistently at 21-24 (with the article recorded in the note); do not split 'spirit' (21-23) from 'ruach' (24).", "C-heavens-22:19": "Adopt 'the host of the heavens'. It is consistent with the wave-A Reviewer's decision-B recommendation ('heavens' for divine-realm šāmayim, 'skies' for weather and fire), the corpus precedent at GEN-WOH-28:12, and the canon French 'l'armée des cieux'. If decision B goes to 'skies' everywhere, revert 22:19, the chapter-22 title and the tzeva entry together.", "D-shofar": "Adopt 'shofar'. It is lexically exact, it keeps šôp̄ār apart from ḥăṣōṣərâ (2 Kgs 11:14), and it matches exodus-woh. Promote to central when a third book applies it.", "E-the-
- summary: "34 verdicts: 33 approve, 1 revise, 0 flag-for-human. Revise: 13:22 punctuation (the comma joins the quoted ban and the curse; use a semicolon or a closing quote after 'drink no water'). Chapter-level revise: add quotation marks in wave-A style (Founder point G). Status awaiting-human: quotation-mark pass, founder decisions A (names) and B (šāmayim) from wave A, and the glossary revisions."
- recheckAddendum: {"reviewer": "claude-opus-5-5 acting as woh-reviewer", "recheckedAt": "2026-11-01T11:02:36Z", "scope": "Editor rework of the wave-B findings, diffed against the pre-rework copies (scratchpad/waveb/pre-rework).", "findings": "Diffed all English lines: 21 changed, and the only change is quotation marks (plus the 13:22 punctuation); wording is identical and the Hebrew text and glossaryRefs are untouched. A stack simulation over the chapter finds every quote balanced: multi-verse speeches stay open across verses and close correctly, and nothing is left open at the chapter end. The style matches wave A (double quotes, nested single quotes, a speech opening after 'saying,'). No unquoted direct speech remains. 13:22 revise RESOLVED: the ban now closes at māyim ('...\"Eat no bread and drink no water\"; your body shall not come ...'), nested correctly inside the YHWH oracle of 13:21-22 (three levels). Note fixes verified: process language removed, The Book Which Tells the Truth named, BDB s.v. ʿal at 22:19, and the 22:37 note added. Chapter-level quotation-mark revise: RESOLVED.", "titleRecommendation": {"current": "1 Kings 13 — The man of the Elohim from Yehudah and the torn altar at Beit-El", "proposed": "1 Kings 13 — The man of the Elohim from Yehudah and the torn altar at Beit-El (Bethel)", "reason": "Founder decision A (ratified with wave A) adds the English name in parentheses, following the wave-A titles ('Eliyahu (Elijah) ...'). Title not edited by the Reviewer."}, "remaining"

### 1 Kings 22 — The vision of Mikhayehu (Micaiah): YHWH enthroned among the host of the heavens



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T10:54:32Z"
- glossaryReview: [{"glossary_id": "hebrew-proper-name-transliteration-convention-kings", "status": "approve", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "genesis-woh / exodus-woh name practice and wave-A overlay v1.0.0 (checked in the data)"], "reasoning": "Op=extend, additive and mirrored. The base entries are verified identical in both Kings overlays (v1.0.0), so the mirrored append keeps them in sync. The equivalence table is checked against every wave-B line. Short-form normalization (ʾăḏōniyyâ 1:5, 7, 18; 2:28; ṣiḏqiyyâ 22:11) follows the rule in force for ʾēliyyâ/ʾăḥazyâ, with the MT spelling noted at each site. tz for tsade matches Tzarfat/Tzidon and genesis-woh. The gentilic '-ite' rule is consistent. Content approved; the base entry remains under the open founder decision A from wave A."}, {"glossary_id": "ketiv-qere-qere-translated-kings", "status": "approve", "citations": ["GKC §17 (Qere and Ketiv)"], "reasoning": "All seven wave-B Qere readings are verified in the source (1:27, 37, 47; 2:24; 22:13; 22:49 ×2), and none is missing. The two ASV-follows-Ketiv sites (1:27, 47) are correctly identified."}, {"glossary_id": "mt-baseline-at-versional-cruxes-and-versification-kings", "status": "approve", "citations": ["Cogan, I Kings (AB 10; 2001), ad loc.", "Burney, Notes on the Hebrew Text of the Books of Kings (1903), ad loc.", "BHS apparatus at 1 Kgs 1:18; 22:6"], "reasoning": "Every listed crux keeps a construable MT and records the versional reading. The LXX pluses and sup
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 54 English lines: no lens leakage. 22:19 'the host of the heavens' renders ṣəḇāʾ haššāmayim as the major versions do (the plural follows the Hebrew; 'heavens' is the less lens-congenial register than 'skies'). 22:21-23 'the ruach' / 'a lying ruach' is transliteration, not interpretation: it closes no reading and names no mechanism. The canon's 'vision of the creators' and 'group telepathy' (TBWTT ch. 3 ¶121-123, verified) are confined to labelled notes. The unlabelled canon wording comparisons at 22:19, 22 quote, they do not interpret."
- chapterLevelRevisions: [{"item": "quotation-marks", "status": "revise", "reasoning": "The wave-B English lines have no quotation marks. Wave A (1 Kgs 17-19; 2 Kgs 1-2) and the wave-C/D drafts mark direct speech with double quotes, nested single quotes, and speeches that stay open across verses. The book cannot ship with two conventions. Before founder sign-off, the Editor should add quotation marks book-wide in wave-A style. A script may propose them, but each speech verse must be proofread by hand: the chapters have multi-verse speeches (1:17-21, 1:24-27, 2:2-9, 2:42-45) and triple nesting at 22:19-23 (Mikhayehu > YHWH > the ruach). The wording itself is approved; after the pass, the Reviewer re-checks only the punctuation."}]
- nonBlockingFixes: ["22:19 note: remove '(draft 'skies')' and 'of wave A'; cite 'BDB s.v. ʿal' unless the locator 'II 1c' is verified.", "22:37: add a one-sentence note that MT wayyāḇôʾ is active ('and he came'; LXX 'they came') and that 'was brought' is a sense rendering.", "22:54 note: remove 'the draft's 'the Ba'al' is aligned with wave A'.", "22:19, 22: name The Book Which Tells the Truth instead of 'the English edition of the canon'.", "Overlay op habbaal-baal-hebrew-bible-rendering-kings: move the 'draft ... aligned' remark from the appended wohChoice into the op's reason."]
- escalationReportAdjustments: "The initial verdicts on all verses, overlay ops and central ops were formed from the chapters, the source, the overlays and the diffs (with mechanical checks of the appliesTo bases, the shared-entry identity across the two Kings overlays, the Qere inventory, the section marks, the versification and the TBWTT ch. 3 citations) before wave-b-editor-report.md was opened. After reading it, no verdict changed. The report confirms the quotation-mark gap (its point G), which matches the Reviewer's independent chapter-level finding, and it states that 22:19 and the tzeva entry depend on founder decision B, which supports the revise on that entry's rationale. The report's spot-check items were reviewed: NJPS 'became rigid' (13:4) agrees with the Reviewer's recollection; the 2:5 LXX first-person suffixes and the 2:29 LXX plus are plausible and described with appropriate hedging. The Lucianic attribution at 2:28 remains a non-blocking query."
- founderDecisionRecommendations: {"A-proper-names": "Retain transliteration with long-form normalization of the MT short forms (Adoniyahu, Tzidqiyahu), tz for tsade and English '-ite' gentilics. This is the rule already in force in the wave-A overlay and approved by the wave-A Reviewer. Following the brief's 'keep each verse's form' would have made the chapters cite an entry that says the opposite. The choice is mechanically reversible. As wave A recommended, add the English form to chapter titles for discoverability.", "B-ruach-22:21-24": "Keep as drafted: 'the ruach' (article kept), 'a lying ruach', 'the ruach of YHWH'. The v 24 retort depends on the noun staying visible, the article has standing (JPS 1917; b. Sanh. 89a; GKC §126q), and the entry is honestly inferred. If the founder prefers conventional English, use lower-case 'spirit' consistently at 21-24 (with the article recorded in the note); do not split 'spirit' (21-23) from 'ruach' (24).", "C-heavens-22:19": "Adopt 'the host of the heavens'. It is consistent with the wave-A Reviewer's decision-B recommendation ('heavens' for divine-realm šāmayim, 'skies' for weather and fire), the corpus precedent at GEN-WOH-28:12, and the canon French 'l'armée des cieux'. If decision B goes to 'skies' everywhere, revert 22:19, the chapter-22 title and the tzeva entry together.", "D-shofar": "Adopt 'shofar'. It is lexically exact, it keeps šôp̄ār apart from ḥăṣōṣərâ (2 Kgs 11:14), and it matches exodus-woh. Promote to central when a third book applies it.", "E-the-
- summary: "54 verdicts: 54 approve, 0 revise, 0 flag-for-human. Chapter-level revise: add quotation marks in wave-A style (Founder point G). Glossary items not approved: ha-ruach-ruach-sheqer-the-ruach-and-the-lying-ruach-1-kings-22, central-diff:tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus (add), central-diff:qedeshah-consecrated-woman-sacred-prostitution-crux (appliesTo). Status awaiting-human: quotation-mark pass, founder decisions A (names) and B (šāmayim) from wave A, Editor points B-G, and the glossary revisions."
- asvTextErrors: ["1KI-22:8 (hosted ASV): 'said unto Jehoshaphat, there is yet one man' has a lower-case 'there'; the 1901 ASV capitalizes the speech ('There').", "1KI-22:43 (hosted ASV): '...Asa his father; He turned not aside' has a capital 'He' after a semicolon; the 1901 ASV has 'he'.", "1KI-22:50 (hosted ASV): '...David his father; And Jehoram his son' has a capital 'And' after a semicolon; the 1901 ASV has 'and'.", "Systemic: backtick (`) used for the apostrophe at 1KI-1:9, 25, 28, 38, 44, 47; 2:15, 19, 31; 13:2, 6; 22:26, 42 (e.g. 'king`s', 'father`s').", "No wording errors of the 8:15 / 8:43 kind were found in chs. 1, 2, 13, 22; the MT/ASV versification of ch. 22 (53 ASV verses) is as expected."]
- recheckAddendum: {"reviewer": "claude-opus-5-5 acting as woh-reviewer", "recheckedAt": "2026-11-01T11:02:36Z", "scope": "Editor rework of the wave-B findings, diffed against the pre-rework copies (scratchpad/waveb/pre-rework).", "findings": "Diffed all English lines: 31 changed, and the only change is quotation marks; wording is identical and the Hebrew text and glossaryRefs are untouched. A stack simulation over the chapter finds every quote balanced: multi-verse speeches stay open across verses and close correctly, and nothing is left open at the chapter end. The style matches wave A (double quotes, nested single quotes, a speech opening after 'saying,'). No unquoted direct speech remains. Nesting at 22:19-23 verified: Mikhayehu's speech in double quotes from v 19 to v 23, and the words of YHWH and the ruach in single quotes; 22:27 has three levels, which is correct. Diff fixes verified: the tzeva-ha-shamayim wohChoice and the shamayim op's reason now ground 'heavens' in the divine-realm recommendation (revise RESOLVED); the qedeshah wohChoice now reads 'qedeshah (fem.) / qadesh (masc.)' (revise RESOLVED); the Ba'al wohChoice no longer contains process history. The ruach entry (flag-for-human) remains a founder-preference point. Note fixes verified: process language removed, The Book Which Tells the Truth named, BDB s.v. ʿal at 22:19, and the 22:37 note added. Chapter-level quotation-mark revise: RESOLVED.", "titleRecommendation": {"current": "1 Kings 22 — Mikhayehu's vision of YHWH enthron
