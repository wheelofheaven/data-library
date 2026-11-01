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
