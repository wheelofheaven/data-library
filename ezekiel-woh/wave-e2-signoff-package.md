# Ezekiel wave E2 (chapters 2, 3, 8, 11, 40, 42, 43, 44) — human sign-off package

**Scope:** 207 verses from the MT (Sefaria, WLC base, PD) — the chapters *The Book Which Tells the Truth* (ch. 3) reads closely. Builds on the published chapters 1, 10, 37.

| Chapter | Verses | Approve | Revise | Flag |
|---|---|---|---|---|
| Ezekiel 2 — The commission and the written scroll | 10 | 10 | 0 | 0 |
| Ezekiel 3 — The scroll eaten, the ruach lifts the prophet, the watchman | 27 | 27 | 0 | 0 |
| Ezekiel 8 — Carried by a lock of hair to the abominations in the temple | 18 | 18 | 0 | 0 |
| Ezekiel 11 — The caldron oracle and the glory leaves the city | 25 | 23 | 1 | 1 |
| Ezekiel 40 — The man of bronze measures the gates and the courts | 49 | 49 | 0 | 0 |
| Ezekiel 42 — The priests' chambers and the outer wall measured | 20 | 20 | 0 | 0 |
| Ezekiel 43 — The glory returns by the east gate; the altar | 27 | 27 | 0 | 0 |
| Ezekiel 44 — The shut east gate and the Zadokite priests | 31 | 30 | 1 | 0 |

- Lens leakage: none (16 reception notes checked against TBWTT ch. 3). 29 English lines refined over the draft, all approved. Ketiv/Qere: 48 readings in 24 verses, Qere translated (3:15 the only sense-changing pair).
- New overlay ezekiel-woh v1.0.0: 17 entries (14 direct; inferred: ruach rule, ʾêlām 'vestibule', harʾēl 'altar hearth'). Central 2.80.0 → next: 1 new direct entry (`qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus`), 4 additive text changes, 22 appliesTo extensions. No speculative entries.

## Decisions (recommendations; Editor and Reviewer agree unless noted)
1. **11:19 'a new spirit'** (Reviewer's flag): *rûaḥ ḥăḏāšâ* beside 'one heart' is the people's renewed mind (cf. 18:31 'make yourselves a new spirit'), so the ruach rule's 'spirit' (human disposition) category applies, not the transliteration. *Recommended: 'a new spirit'*, narrowing the rule's gift clause.
2. **Quotation marks** (Kings convention) for this wave; punctuation-only pass on published ch. 37 later. *Ratify.*
3. **English proper names** in Ezekiel (Israel, Zadok), as published Ezekiel/Isaiah/Daniel; Genesis/Exodus/Kings transliterate — record the split centrally. *Keep.*
4. **ruach rule**: transliterated where it moves or is given to the prophet; 'spirit' in human idioms; 'side' (42:16–20). Merge with the Kings entries into one central entry at the next consolidation. *Ratify (inferred).*
5. **'vestibule'** (ʾêlām) and **'altar hearth'** (harʾēl), as inferred. *Ratify.*
6. **'guilt-offering'** (as isaiah-woh 53:10) and **'dash'** for zāraq. *Ratify (direct).*
7. hêkāl **'temple'** at 8:16, 42:8 (the whole building there; Kings' 'great hall' is the room, kept for 41:1–4). *Ratify.*

## Fixes applied at sign-off
- 11:23 reception note: TBWTT lists 11:23–24 among Ezekiel's journeys in the creators' craft; it identifies the glory with the creators' ship only at 43:2.
- 44:24 note: the line 'they shall stand to judge' reproduces the Ketiv *lišpōṭ*; say so (Qere *ləmišpāṭ* 'for judgment' recorded).
- Central `eretz` wohChoice seam: 'land. Context clause (…)'.
- Unverified citations softened: 43:3 ('some Hebrew manuscripts and versions') and the LXX figure at 40:14.

## Follow-ups (not blocking)
- Punctuation pass on published Ezekiel 37 (and a check of 1, 10); 37:1, 5–14 cite `ruach-chayyot` where the new rule applies.
- Central refIds mix `EZK-n:v` (older) and `EZK-WOH-n:v`; one normalization pass.
- exodus-woh 20:21 and 1-kings-woh 8:63–64 should carry the new `qorbanot` glossaryRef at their next pass.

---

## Editor report (inlined)

# Ezekiel wave E2 Editor Report (Ezek 2, 3, 8, 11, 40, 42, 43, 44)

**Editor:** claude-opus-5-5 acting as woh-editor, 2026-11-01.
**Status at end of pass:** all eight chapters `draft` → `editor-review`; version `0.1.0` → `1.0.0-rc1`; `glossaryVersion` 2.81.0 (pending application of `wave-e2-central-diff.json`; becomes 2.82.0 if the parallel Revelation diff is applied first); `overlayGlossaryVersion` 1.0.0 (new overlay `_translation-glossary.json`); `reviewer` left `pending`; `claude-opus-5-5 (editor)` added to `modelDrafts`. The brief said to set "glossaryVersion and overlayGlossaryVersion 1.0.0". I followed the Kings editor precedent instead: the chapter pins the pending central version, and only the overlay is 1.0.0. Adjust if the brief meant otherwise.

**Scope:** 207 verses and 83 editorial questions, all resolved: 79 into glossary entries or commentary, 4 also raised as founder points. Every verse now has `notes: {official, community: []}` (the draft `commentary` key was dropped). 200 verses have commentary; 7 verses have none because they do not diverge from the reference reading (8:13, 8:15, 11:11, 40:27, 40:32, 40:35, 42:11). There are 16 labelled reception notes at canon-cited verses. No English line carries the lens.

**Mechanical checks (scripts in the editor's scratchpad):** every Hebrew `text` matches `source-he-{N}.json`; a quotation-mark stack simulation finds every chapter balanced (111 speech verses); every `glossaryRef` resolves to central 2.80.0, the new overlay, or the new central entry; overlay `appliesTo` and verse `glossaryRefs` agree in both directions; every central ref used in the chapters lists the citing verse once the diff is applied (the diff was test-applied in memory to 2.80.0); every overlay entry has all required fields and a rationale of at least three sentences.

---

## Speculative entries requiring sign-off

None. No entry in this wave is `speculative`. The three `inferred` entries are listed under founder decisions C and D.

---

## Founder decisions (escalated)

### A. Quotation marks book-wide (`direct-speech-quotation-marks-convention-ezekiel`)

**Issue:** The signed-off Ezekiel chapters are inconsistent. 10:2, 6 and 37:3, 4, 9, 11, 18 quote dialogue, but 37:5, 12-14, 16, 19 and 21-28 leave "Thus says the Lord YHWH: ..." unquoted, and 37:4 and 37:9 do not nest the inner message.
**Decision taken:** The Kings convention, ratified at Kings waves A/B, is adopted for this wave: double quotes, nested single quotes, a speech opened once and closed in its last verse, and 'declares the Lord YHWH' kept inside the speech. One boundary is a judgement call: at 43:7-17 the speech stays open to v 17 because no new speaker is introduced before 'He said to me' (43:18).
**Recommendation:** Ratify, and schedule a punctuation-only pass on ch. 37 (and a check of chs. 1 and 10) so the book ships with one convention, as the Kings Reviewer required for Kings.

### B. Proper names: English forms in Ezekiel vs transliteration in Kings (`proper-names-english-forms-convention-ezekiel`)

**Issue:** ezekiel-woh 1/10/37 use English names (Israel, Judah, Joseph, Ephraim, David, Jacob), with Hebrew forms only where central entries rule (Kebar, Kasdim). The Kings overlays transliterate under founder decision A (Yisra'el, Yehudah, Tzadoq), so the corpus now has two practices.
**Decision taken:** This wave follows the book's own precedent (Jaazaniah, Pelatiah, Tammuz, Tel-abib, Zadok, Levites, Jerusalem, Israel), because a mixed book would be worse than either practice.
**Recommendation:** Founder to decide whether decision A extends to the Latter Prophets. If it does, the change is one overlay entry plus a mechanical pass over all eleven Ezekiel chapters, including 1/10/37.

### C. The ruach transliteration: book rule now, central promotion next (`ruach-agent-gift-and-side-ezekiel`, inferred)

**Decision taken:** 'ruach' where rûaḥ enters, lifts or carries the prophet (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), 'the ruach of YHWH' (11:5), 'the ruach of Elohim' (11:24b), and 'a new ruach' for the rûaḥ YHWH gives (11:19, as 37:5-6, 14). 'Spirit' is used in the human idioms (3:14b; 11:5b) and 'side' for the compass sense (42:16-20). This follows EZK-WOH-37:1 and the Kings overlays; the ASV capital 'Spirit' and the option 'a wind' are recorded in commentary.
**Why escalated:** (1) The entry is `inferred`. (2) The Kings overlays set a condition for promoting the transliteration to central: "once Samuel or the Latter Prophets apply them". Ezekiel now applies it.
**Recommendation:** Ratify the overlay entry. At the next central consolidation, merge `ruach-yhwh-and-prophetic-ruach-transliteration-kings` (both Kings overlays) and `ruach-agent-gift-and-side-ezekiel` into one central entry. I did not propose that merge in this diff because the Kings overlays are read-only for this pass.

### D. Two inferred Temple-vision renderings that depart from the ASV

- **`elam-vestibule-gate-element-ezekiel-40`:** ʾêlām / ʾêlammôṯ is rendered 'vestibule(s)' (ASV 'arches', which has no lexical support; BDB/HALOT treat it as a by-form of ʾûlām; NRSV 'vestibule'). The line keeps 'porch' for ʾûlām so the spelling difference stays visible. It is inferred because the plural forms, especially 40:30, are disputed. 12 lines changed in ch. 40.
- **`harel-ariel-altar-hearth-ezekiel-43`:** harʾēl (43:15a) and ʾăriʾêl (43:15b, 16) are both rendered 'altar hearth' (NRSV), replacing the ASV 'upper altar' at 43:15a. It is inferred because it takes two Masoretic vocalizations as one word; 'mountain of El' is recorded in commentary. 1 line changed.

**Recommendation:** Ship both as inferred.

### E. Sacrificial vocabulary: two modernizations in a new central entry (`qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus`, direct)

The new entry takes the ASV set (sin-offering, meal-offering, peace-offerings, sacrifice, make atonement, cleanse, purify, consecrate) and changes two terms: ʾāšām 'guilt-offering', not 'trespass-offering' (as isaiah-woh 53:10 already has), and zāraq 'dash', not 'sprinkle' (zāraq vs hizzâ; NRSV, NJPS). qorbān becomes 'offering' and tərûmâ stays 'oblation', so the ASV no longer uses one word for both lexemes. Milgrom's 'purification/reparation offering' is recorded in commentary but not adopted. The entry's appliesTo also lists the existing consistent lines EXO-WOH-20:21 and 1KI-WOH-8:63-64. The answer to the translator's question is no: `minchah-shaah` is not extended, and the cultic minḥâ in lists is governed by the new entry.
**Recommendation:** Ratify. The Torah's tərûmâ ('heave-offering') is to be reviewed when Leviticus and Numbers enter the corpus.

### F. Ezekiel refId prefix in central (orchestrator item)

Central 2.80.0 records the signed-off Ezekiel sites as `EZK-n:v` (133 occurrences), while the chapter files use `EZK-WOH-n:v`. The new sites in this diff use `EZK-WOH-`, and the legacy refIds are preserved untouched, so some entries now mix both forms (e.g. `kavod-yhwh`: EZK-1:28 + EZK-WOH-3:12 ...). **Recommendation:** a one-time normalization of `EZK-` to `EZK-WOH-` in central at a later pass (the same issue exists for `GEN-` vs `GEN-WOH-`).

---

## Unresolved editorial questions

None require human judgement beyond points A-F. These resolved readings deserve the Reviewer's attention:

- **3:12** The MT `bārûḵ` is kept against the widely adopted `bərûm`; 'his place' is kept, not 'its place'.
- **8:6** The subjectless infinitive is rendered 'so that I go far' (ASV), with NRSV's causative reading noted.
- **11:7** The MT `hôṣîʾ` is rendered with the ASV impersonal passive.
- **40:14** The verse is translated literally and left obscure.
- **42:12** The hapax hăḡînâ is now translated, 'the corresponding wall'; the ASV omits it.
- **44:8** 'them' is supplied as the object, as the draft had it; this is recorded in the MT-baseline rule on supplied words.

---

## English-line changes (29 lines, each backed by a glossary entry)

| Decision | Entry | Lines |
|---|---|---|
| raʿaš 'rushing' → 'rumbling' | overlay `raash-gadol-great-rumbling-ezekiel-3` | 3:12, 3:13 |
| nep̄eš 'soul' → 'life' | overlay `nefesh-scope-ezekiel` | 3:19, 3:21 |
| śārîm 'princes' → 'officials' | overlay `sar-and-nasi-officials-and-prince-ezekiel` | 11:1 |
| tāʾ 'lodge(s)' → 'guardroom(s)' | overlay `ta-guardroom-gate-chambers-ezekiel-40` | 40:7, 10, 12, 13, 16, 21, 29, 33, 36 |
| ʾêlām 'arches' → 'vestibule(s)' | overlay `elam-vestibule-gate-element-ezekiel-40` | 40:16, 21, 22, 24, 25, 26, 29, 30, 31, 33, 34, 36 (with tāʾ in several) |
| ʾāšām 'trespass-offering' → 'guilt-offering' | central `qorbanot-…` (new) | 40:39, 42:13, 44:29 |
| qorbān 'oblation' → 'offering' | central `qorbanot-…` (new) | 40:43 |
| zāraq 'sprinkling' → 'dashing' | central `qorbanot-…` (new) | 43:18 |
| hapax hăḡînâ translated ('corresponding') | overlay `mt-baseline-at-versional-cruxes-ezekiel` | 42:12 |
| toḵnîṯ 'pattern' → 'plan' | overlay `tabnit-toknit-tekhunah-pattern-plan-arrangement-ezekiel` | 43:10 |
| harʾēl 'upper altar' → 'altar hearth' | overlay `harel-ariel-altar-hearth-ezekiel-43` | 43:15 |

No other wording changed. Quotation marks, names, ruach and the Qere readings were already as drafted, and the Translator's defaults were kept wherever the question resolved to the draft.

---

## Disposition of the 83 editorial questions

- **Ch. 2 (5):**
  - 2:1 quotes → A.
  - 2:2 ruach → C.
  - 2:3 MT 'nations' kept (MT baseline).
  - 2:6 'briers and thorns' kept (commentary).
  - 2:10 scroll front/back kept (new overlay entry; reception note).
- **Ch. 3 (6):**
  - 3:9 'adamant' kept (commentary).
  - 3:12 MT doxology kept (MT baseline).
  - 3:12 raʿaš → 'rumbling' (overlay).
  - 3:15 Qere, 'Tel-abib', 'stunned' (Ketiv/Qere, names).
  - 3:16 mid-verse pisqa kept in `text` only (MT baseline; commentary).
  - 3:19 nep̄eš → 'life' (overlay).
- **Ch. 8 (8):**
  - 8:2 MT 'fire' (MT baseline).
  - 8:3 'pattern of a hand', 'between the land and the skies', 'court' supplied, 'lock of my head' (tabnîṯ entry; central shamayim/eretz extensions; reception note).
  - 8:6 Qere; ASV subject reading (commentary).
  - 8:10 'pattern', 'idols', 'a detestable thing' kept (tabnîṯ entry; commentary).
  - 8:11 names → B.
  - 8:14 'Tammuz' without the article (names entry).
  - 8:16 hêḵāl 'temple' by context clause; ʾûlām 'porch' (central Temple-plan extension with an Ezekiel paragraph).
  - 8:17 MT 'their nose' (MT baseline).
- **Ch. 11 (8):**
  - 11:1 'officials' (overlay).
  - 11:3 statement (MT baseline).
  - 11:7 ASV passive (MT baseline).
  - 11:15 MT 'kindred', imperative (MT baseline).
  - 11:16 'I have been ... for a little while' kept (commentary).
  - 11:19 MT 'one heart', 'within you'; 'a new ruach' (MT baseline; C).
  - 11:21 ASV construal (MT baseline).
  - 11:24 'to Kasdim', 'by the ruach of Elohim' (central eretz-kasdim extension; C).
- **Ch. 40 (26):**
  - 40:1 literal date kept.
  - 40:2 MT 'on it' (MT baseline; reception note).
  - 40:3 'bronze', 'a cord of flax' kept; flax/linen split by object (measures entry; reception note).
  - 40:5 units (new measures entry).
  - 40:6, 40:8, 40:14, 40:37, 40:44, 40:48 MT kept (MT baseline).
  - 40:7 tāʾ → 'guardroom' (overlay).
  - 40:9 ʾayil 'post' (overlay).
  - 40:16 ʾêlām → D.
  - 14 Ketiv/Qere questions resolved under the Ketiv/Qere entry.
  - 40:39 sacrificial cluster → E.
  - 40:43 'hooks' kept, qorbān 'offering' (E).
- **Ch. 42 (10):**
  - 42:1 ASV terms kept (commentary).
  - 42:4 and 42:10 MT kept (MT baseline).
  - 42:6 'ground' (central eretz context clause).
  - 42:8 'temple' (central Temple-plan context clause).
  - 42:9, 42:14 and 42:16 Qere (Ketiv/Qere; MT 'reeds'; ruach 'side').
  - 42:12 hăḡînâ now translated (MT baseline).
  - 42:13 → E.
  - 42:14 'holy' (new qōḏeš entry; reception note).
- **Ch. 43 (11):**
  - 43:2 'his sound ... the land shone' (central qol-mayim-rabbim and eretz).
  - 43:3 and 43:7 MT (MT baseline; 43:7 speech extent → A).
  - 43:10 'plan' (overlay).
  - 43:11, 43:16 and 43:26 Qere (Ketiv/Qere; units not supplied).
  - 43:13 ASV altar terms (overlay).
  - 43:15 → D.
  - 43:18 nested quotes (A) and 'dash' (E).
  - 43:27 mid-verse setumah (MT baseline).
- **Ch. 44 (9):**
  - 44:3 ASV construal, 'prince', pointing anomaly (overlay; MT baseline; reception note).
  - 44:5 Qere, 'set your heart'.
  - 44:7 MT 'they broke'.
  - 44:8 'them' supplied.
  - 44:17 'with what causes sweat' (commentary; reception note at 44:18).
  - 44:19 repetition kept.
  - 44:24 Qere.
  - 44:28 MT literal.
  - 44:30 ASV terms, 'the first' (E; reception note).

**Ketiv/Qere count:** the Translator's draft counted 46 readings in 25 verses. A script over `source-he-*.json` finds **48 readings in 24 verses** (3:15; 8:6; 40:6, 9, 15, 21, 22, 24, 25, 26, 29, 31, 33, 34, 36, 37; 42:9, 14, 16; 43:11, 16, 26; 44:5, 24), and the overlay entry uses that count. Only 3:15 changes the sense; the ASV follows the Ketiv there.

---

## Glossary changes for review

### Central glossary (`wave-e2-central-diff.json`; base 2.80.0 → recommended 2.81.0, minor)

- Added: `qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus` (claim_type: `direct`).
- Modified (text, additive; no decision reversed):
  - `ulam-hekhal-devir-temple-three-room-plan-cross-corpus`: an Ezekiel application paragraph added to the rationale, with 12 refIds.
  - `eretz`: 'ground' context clause added to wohChoice and rationale (42:6; 43:14), with 8 refIds.
  - `eretz-kasdim`: directional 'to Kasdim' (11:24).
  - `qol-mayim-rabbim`: the 43:2 site.
- Modified (appliesTo only): adonai-yhwh (+18), ben-adam (+24), biq'ah-ha-atzamot (+3), chashmal, chayyot, cherubim-ezek, davar-yhwh-prophetic-formula (+2), elohei-yisrael (+4), elohim-as-translation, the Ezekiel-1 merkavah entry (+3), kavod-yhwh (+9), kavod-yhwh-departure, mar'eh-demut (+3), mar'ot-elohim (+2), navi-first-occurrence-abraham, nehar-kevar (+3), olah-burnt-offering (+7), qarnot-ha-mizbeach (+2), shakhan-dwell (+2), shamayim, toevah (+11), yad-yhwh (+4).
- **Sequencing with the Revelation diff (also based on 2.80.0):** if it is applied first, this diff becomes 2.81.0 → 2.82.0. Merge appliesTo as a set union for any entry both diffs modify (likely chayyot, the merkavah entry, kavod-yhwh, qol-mayim-rabbim), and apply the text appends to the then-current fields. Each op's `reason` lists exactly the refIds it adds, to make the merge mechanical.

### Per-translation overlay (`ezekiel-woh/_translation-glossary.json`, new, v1.0.0, 17 entries)

- Added (conventions): `direct-speech-quotation-marks-convention-ezekiel` (direct), `ruach-agent-gift-and-side-ezekiel` (**inferred**), `proper-names-english-forms-convention-ezekiel` (direct), `ketiv-qere-qere-translated-ezekiel` (direct), `mt-baseline-at-versional-cruxes-ezekiel` (direct).
- Added (text-specific):
  - `raash-gadol-great-rumbling-ezekiel-3` (direct)
  - `megillat-sefer-scroll-written-front-and-back-ezekiel-2-3` (direct)
  - `nefesh-scope-ezekiel` (direct)
  - `tabnit-toknit-tekhunah-pattern-plan-arrangement-ezekiel` (direct)
  - `sar-and-nasi-officials-and-prince-ezekiel` (direct)
  - `ta-guardroom-gate-chambers-ezekiel-40` (direct)
  - `elam-vestibule-gate-element-ezekiel-40` (**inferred**)
  - `ayil-post-architectural-pier-ezekiel-40` (direct)
  - `measures-cubit-handbreadth-span-reed-ezekiel` (direct)
  - `altar-structure-terms-heq-gab-gevul-azarah-ezekiel-43` (direct)
  - `harel-ariel-altar-hearth-ezekiel-43` (**inferred**)
  - `qodesh-holy-chambers-and-garments-ezekiel-42-44` (direct)
- Promotion candidates: the ruach entry (founder point C) and the quotation-mark convention (if the founder wants a corpus-wide rule).

---

## Divergences of the signed-off chapters 1, 10, 37 from the new overlay (not retro-edited)

1. **Quotation marks (ch. 37):** 37:5, 12-14, 16, 19 and 21-28 leave the messenger formula and oracle unquoted, and 37:4 and 37:9 do not nest the inner message ('dry bones, hear ...'; 'thus says the Lord YHWH: from the four ruchot ...'). Chapters 1 and 10 use double quotes only (10:2, 6) and appear compatible.
2. **ruach references:** 37:1 ('by the ruach of YHWH', a transport site) and 37:5-6, 8, 10, 14 cite the central `ruach-chayyot`, or no ruach entry at all. Under the new overlay the transport and gift uses belong to `ruach-agent-gift-and-side-ezekiel`; `ruach-chayyot` should keep only 1:12, 20-21 and 10:17.
3. **Typography of ruach:** 10:17 italicizes *ruach*; 1:12, 20-21, 37 and this wave use roman 'ruach'.
4. **raʿaš:** 37:7 'a rattling' is consistent with the overlay entry by context (bones). It needs no change, but it could be added to that entry's appliesTo at the next pass.
5. **Schema gaps:** some paragraphs in chs. 1 and 37 lack `notes` or `glossaryRefs` keys.
6. **Commentary register:** the 2026-05 notes in chs. 1, 10 and 37 use bold headings and interpretive wording ('staging-area', 'integrated control architecture'). 37:6 carries the canon reading in the official note without the reception-note label. Recommend relabelling at the next Ezekiel pass, to match the Kings and wave-E2 practice.
7. **Central refId prefix:** see F.

---

## Points for the Reviewer to spot-check

I have stated the citations below in hedged form; the Reviewer should verify them:

- NJPS 'Temple' at 8:16.
- NRSV at 40:44 (LXX 'south gate'), 42:1 ('temple yard'), 42:3 ('in three stories') and 43:15 ('altar hearth' twice).
- The LXX figure at 40:14.
- 'Six manuscripts, Theodotion and the Vulgate' at 43:3 (taken from the Translator).
- The versional 'house' at 2:7.
- BDB/HALOT on hăḡînâ ('fitting, corresponding', tentative).
- Albright 1942 on harʾēl/arallû and the ziggurat comparison.
- Yadin, *IEJ* 8 (1958) for the six-chamber gates.


---

## Reviewer report

### Ezekiel 2 — The commission and the written scroll



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "ruach-agent-gift-and-side-ezekiel", "status": "revise", "citations": ["BDB s.v. rûaḥ", "Block, 'The Prophet of the Spirit: The Use of rwḥ in the Book of Ezekiel', JETS 32 (1989)", "Ezek 18:31; 36:26-27 (MT)", "Greenberg, Ezekiel 1-20 (AB 22, 1983), ad loc."], "reasoning": "inferred is the right claim type: transliteration leaves an acknowledged wind/spirit ambiguity open, and the agent/transport sites (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), the idiom 'spirit' (3:14b; 11:5b) and the compass 'side' (42:16-20) are all correctly classified and applied. One clause needs revision: the 'gift' criterion sweeps in 11:19 rûaḥ ḥăḏāšâ, which, paired with lēḇ, is the people's renewed disposition (18:31 has Israel make it themselves; 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "10 verdicts: 10 approve, 0 revise, 0 flag-for-human. Glossary: 9 items reviewed, ruach-agent-gift-and-side-ezekiel revise. No lens-leakage flags."

### Ezekiel 3 — The scroll eaten, the ruach lifts the prophet, the watchman



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "ruach-agent-gift-and-side-ezekiel", "status": "revise", "citations": ["BDB s.v. rûaḥ", "Block, 'The Prophet of the Spirit: The Use of rwḥ in the Book of Ezekiel', JETS 32 (1989)", "Ezek 18:31; 36:26-27 (MT)", "Greenberg, Ezekiel 1-20 (AB 22, 1983), ad loc."], "reasoning": "inferred is the right claim type: transliteration leaves an acknowledged wind/spirit ambiguity open, and the agent/transport sites (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), the idiom 'spirit' (3:14b; 11:5b) and the compass 'side' (42:16-20) are all correctly classified and applied. One clause needs revision: the 'gift' criterion sweeps in 11:19 rûaḥ ḥăḏāšâ, which, paired with lēḇ, is the people's renewed disposition (18:31 has Israel make it themselves; 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "27 verdicts: 27 approve, 0 revise, 0 flag-for-human. Glossary: 18 items reviewed, ruach-agent-gift-and-side-ezekiel revise. No lens-leakage flags."

### Ezekiel 8 — Carried by a lock of hair to the abominations in the temple



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "ruach-agent-gift-and-side-ezekiel", "status": "revise", "citations": ["BDB s.v. rûaḥ", "Block, 'The Prophet of the Spirit: The Use of rwḥ in the Book of Ezekiel', JETS 32 (1989)", "Ezek 18:31; 36:26-27 (MT)", "Greenberg, Ezekiel 1-20 (AB 22, 1983), ad loc."], "reasoning": "inferred is the right claim type: transliteration leaves an acknowledged wind/spirit ambiguity open, and the agent/transport sites (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), the idiom 'spirit' (3:14b; 11:5b) and the compass 'side' (42:16-20) are all correctly classified and applied. One clause needs revision: the 'gift' criterion sweeps in 11:19 rûaḥ ḥăḏāšâ, which, paired with lēḇ, is the people's renewed disposition (18:31 has Israel make it themselves; 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "18 verdicts: 18 approve, 0 revise, 0 flag-for-human. Glossary: 20 items reviewed, ruach-agent-gift-and-side-ezekiel revise, central-diff:eretz (modify) revise. No lens-leakage flags."

### Ezekiel 11 — The caldron oracle and the glory leaves the city

- **EZK-WOH-11:19** — flag-for-human: Re-parsed: wənāṯattî lāhem lēḇ ʾeḥāḏ wərûaḥ ḥăḏāšâ ʾettēn bəqirbəḵem; MT 'one heart' and 'within you' are correctly kept. The question is 'a new ruach': the overlay transliterates every rûaḥ YHWH 'gives', but here rûaḥ ḥăḏāšâ is paired with lēḇ as the people's renewed disposition (at 18:31 Israel must 'make yourselves a new heart and a new rûaḥ', and 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'), which is the overlay's own 'spirit' (human mind) category. Reviewer recommends 'and I will put a new spirit within you', reserving 'ruach' for YHWH's own rûaḥ and the life-breath (36:27; 37:5-6, 14); this is a project-stance call on the scope of the gift clause (founder point C).
- **EZK-WOH-11:23** — revise: English line approved: wayyaʿal kəḇôḏ YHWH ... wayyaʿămōḏ ʿal-hāhār is exact. The reception note overstates the canon: TBWTT ch. 3 quotes 11:23-24 in the run it sums up as 'so many journeys for Ezekiel in one of the creators' flying craft', but it identifies the glory with the creators' large ship explicitly only at 43:2. Proposed note wording: 'quotes 11:23-24 ... among the passages it calls "so many journeys for Ezekiel in one of the creators' flying craft"; the identification of the glory with the creators' large ship is made explicitly at 43:2.' Non-blocking.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "ruach-agent-gift-and-side-ezekiel", "status": "revise", "citations": ["BDB s.v. rûaḥ", "Block, 'The Prophet of the Spirit: The Use of rwḥ in the Book of Ezekiel', JETS 32 (1989)", "Ezek 18:31; 36:26-27 (MT)", "Greenberg, Ezekiel 1-20 (AB 22, 1983), ad loc."], "reasoning": "inferred is the right claim type: transliteration leaves an acknowledged wind/spirit ambiguity open, and the agent/transport sites (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), the idiom 'spirit' (3:14b; 11:5b) and the compass 'side' (42:16-20) are all correctly classified and applied. One clause needs revision: the 'gift' criterion sweeps in 11:19 rûaḥ ḥăḏāšâ, which, paired with lēḇ, is the people's renewed disposition (18:31 has Israel make it themselves; 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "25 verdicts: 23 approve, 1 revise, 1 flag-for-human. Non-approve: EZK-WOH-11:19 flag-for-human; EZK-WOH-11:23 revise. Glossary: 17 items reviewed, ruach-agent-gift-and-side-ezekiel revise, central-diff:eretz (modify) revise. No lens-leakage flags."

### Ezekiel 40 — The man of bronze measures the gates and the courts



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "proper-names-english-forms-convention-ezekiel", "status": "approve", "citations": ["ASV forms (Jaazaniah, Pelatiah, Tammuz, Tel-abib, Zadok)", "Zimmerli, Ezekiel 1 (Hermeneia, 1979), ad loc. (tēl ʾāḇîḇ < til abūbi)", "isaiah-woh / daniel-woh English name forms (checked in the data by the Kings reviewer)"], "reasoning": "direct is correct: the entry records the book's existing practice (signed-off chs. 1, 10, 37) and keeps it consistent within the book; Kebar/Kasdim correctly deferred to central. The cross-book question (Kings transliterates) is a founder decision (point B) and does not affect the soundness of the entry."}, {"glossary_id": "ketiv-qere-qere-translated-ezekiel", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "49 verdicts: 49 approve, 0 revise, 0 flag-for-human. Glossary: 17 items reviewed, central-diff:eretz (modify) revise. No lens-leakage flags."

### Ezekiel 42 — The priests' chambers and the outer wall measured



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "ruach-agent-gift-and-side-ezekiel", "status": "revise", "citations": ["BDB s.v. rûaḥ", "Block, 'The Prophet of the Spirit: The Use of rwḥ in the Book of Ezekiel', JETS 32 (1989)", "Ezek 18:31; 36:26-27 (MT)", "Greenberg, Ezekiel 1-20 (AB 22, 1983), ad loc."], "reasoning": "inferred is the right claim type: transliteration leaves an acknowledged wind/spirit ambiguity open, and the agent/transport sites (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), the idiom 'spirit' (3:14b; 11:5b) and the compass 'side' (42:16-20) are all correctly classified and applied. One clause needs revision: the 'gift' criterion sweeps in 11:19 rûaḥ ḥăḏāšâ, which, paired with lēḇ, is the people's renewed disposition (18:31 has Israel make it themselves; 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "20 verdicts: 20 approve, 0 revise, 0 flag-for-human. Glossary: 10 items reviewed, ruach-agent-gift-and-side-ezekiel revise, central-diff:eretz (modify) revise. No lens-leakage flags."

### Ezekiel 43 — The glory returns by the east gate; the altar



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "ruach-agent-gift-and-side-ezekiel", "status": "revise", "citations": ["BDB s.v. rûaḥ", "Block, 'The Prophet of the Spirit: The Use of rwḥ in the Book of Ezekiel', JETS 32 (1989)", "Ezek 18:31; 36:26-27 (MT)", "Greenberg, Ezekiel 1-20 (AB 22, 1983), ad loc."], "reasoning": "inferred is the right claim type: transliteration leaves an acknowledged wind/spirit ambiguity open, and the agent/transport sites (2:2; 3:12, 14a, 24; 8:3; 11:1, 24; 43:5), the idiom 'spirit' (3:14b; 11:5b) and the compass 'side' (42:16-20) are all correctly classified and applied. One clause needs revision: the 'gift' criterion sweeps in 11:19 rûaḥ ḥăḏāšâ, which, paired with lēḇ, is the people's renewed disposition (18:31 has Israel make it themselves; 36:26-27 distinguishes 'a new rûaḥ' from 'my rûaḥ'
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "27 verdicts: 27 approve, 0 revise, 0 flag-for-human. Glossary: 24 items reviewed, ruach-agent-gift-and-side-ezekiel revise, central-diff:eretz (modify) revise. No lens-leakage flags."

### Ezekiel 44 — The shut east gate and the Zadokite priests

- **EZK-WOH-44:24** — revise: Both Ketiv/Qere pairs verified in the source. The note says the Qere is translated, but the English 'they shall stand to judge' reproduces the Ketiv infinitive lišpōṭ rather than the Qere noun ləmišpāṭ 'for judgment'. Either render the Qere ('In a dispute they shall take their stand for judgment') or, preferably to avoid the English ambiguity of 'stand for judgment', keep the line and amend the note: "'to judge' renders the purpose expressed by the Qere ləmišpāṭ; it coincides in wording with the Ketiv lišpōṭ, and the sense is the same." Non-blocking.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:41:10Z"
- glossaryReview: [{"glossary_id": "direct-speech-quotation-marks-convention-ezekiel", "status": "approve", "citations": ["NRSV and NJPS (quotation marks in Ezekiel; the ASV has none)", "1KI-WOH/2KI-WOH reviewer reports, waves A-B (convention ratified)", "Reviewer's independent stack simulation: all eight chapters balance; multi-verse speeches open once and close in their last verse"], "reasoning": "direct is right for a punctuation convention with no lexical content. Speech boundaries follow the Hebrew formulas; the one judgement call (43:7-17 kept open to v 17 because no new speaker is introduced before 43:18) is defensible and recorded. Ratify (founder point A) and schedule the ch. 37 punctuation pass."}, {"glossary_id": "proper-names-english-forms-convention-ezekiel", "status": "approve", "citations": ["ASV forms (Jaazaniah, Pelatiah, Tammuz, Tel-abib, Zadok)", "Zimmerli, Ezekiel 1 (Hermeneia, 1979), ad loc. (tēl ʾāḇîḇ < til abūbi)", "isaiah-woh / daniel-woh English name forms (checked in the data by the Kings reviewer)"], "reasoning": "direct is correct: the entry records the book's existing practice (signed-off chs. 1, 10, 37) and keeps it consistent within the book; Kebar/Kasdim correctly deferred to central. The cross-book question (Kings transliterates) is a founder decision (point B) and does not affect the soundness of the entry."}, {"glossary_id": "ketiv-qere-qere-translated-ezekiel", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012), on
- lens-leakage-flags: []
- lensLeakageCheck: "Checked every English line, with particular attention to the 16 reception-note sites (2:1, 2:10, 3:3, 3:12, 8:3, 11:1, 11:23, 40:2, 40:3, 42:14, 43:2, 44:2, 44:3, 44:15, 44:18, 44:30). No line carries the canon reading: kāḇôḏ stays 'glory' (11:23; 43:2), the bronze man keeps the Hebrew simile (40:3), qōḏeš stays 'holy' against the canon's 'healthful' (42:14), ʾûlām stays 'porch' against the 'airlock' reading (44:3), and yezaʿ is rendered by its accepted sense (44:18). Each reception note was checked against the TBWTT ch. 3 quotation file and is accurate and labelled, except that 11:23 slightly overstates the canon (verdict revise, notes only). Two features a cold reader might query were judged not to be leakage: 'ruach' (an inferred overlay convention that leaves an acknowledged ambiguity open and replaces the ASV's doctrinal capital) and 'between the land and the skies' at 8:3 (the ratified eretz default and shamayim physical register, identical to GEN-WOH 1:1, with the Hebrew's 'in visions of Elohim' kept). The sacrificial and architectural modernizations ('guilt-offering', 'dash', 'guardroom', 'vestibule', 'altar hearth') follow NRSV/NJPS and the lexica and carry no interpretive content."
- escalationReportAdjustments: "Initial verdicts on all 207 verses, the 17 overlay entries and the 27 central-diff ops were formed from the chapters, sources, overlay, central diff and the 2.80.0 base before opening wave-e2-editor-report.md. After reading it no verdict changed. The report raises nothing on 11:19 (a new ruach), 11:23 (reception-note wording) or 44:24 (Ketiv wording in the line), so those stand. Spot-checks the report requested: NRSV 8:16 'temple', 42:1 'temple yard', 42:3 'in three stories', 43:15-16 'altar hearth', Yadin IEJ 8 (1958), the Mesha line-12 ʾrʾl, and Albright 1942 (ziggurat; arallû) are consistent with the reviewer's knowledge; the '43:3 six manuscripts' count and the exact LXX figure at 40:14 could not be confirmed independently and should be checked against BHS or worded as 'some manuscripts' / 'a different figure' (non-blocking). The report's Ketiv/Qere count (48 readings in 24 verses) matches the reviewer's independent count of 50 bracketed tokens."
- founderDecisionRecommendations: {"A-quotation-marks": "Ratify the Kings convention for Ezekiel. The reviewer's own stack simulation confirms all eight chapters balance and the 43:7-17 boundary is defensible. Schedule a punctuation-only pass on ch. 37 (37:4-5, 9, 12-14, 16, 19, 21-28) and a check of chs. 1 and 10 so the book ships with one convention.", "B-proper-names": "Keep English forms in Ezekiel for this wave: a mixed book would be worse than either practice, and the three signed-off chapters already use English. Recommendation for the corpus decision: the Latter Prophets volumes (isaiah-woh, ezekiel-woh, daniel-woh) already share English forms while genesis/exodus/Kings transliterate; record that genre split explicitly in a central convention note rather than converting Ezekiel, unless the founder wants decision A extended corpus-wide, in which case the mechanical pass over all eleven chapters is straightforward.", "C-ruach": "Ratify the overlay rule for agent/transport rûaḥ, 'spirit' for human idioms and 'side' for the compass sense, and support merging it with the Kings ruach entries into one central entry. Before promotion, narrow the 'gift' clause: rûaḥ ḥăḏāšâ paired with lēḇ (11:19; later 18:31; 36:26a) is the human disposition and should be 'a new spirit', while YHWH's own rûaḥ and the breath of life (36:27; 37:5-6, 14) stay 'ruach'. Verse flag at EZK-WOH-11:19.", "D-inferred-temple-terms": "Ship both as inferred. ʾêlām 'vestibule' (NRSV) and harʾēl/ʾăriʾêl 'altar hearth' (NRSV) are lexically su
- summary: "31 verdicts: 30 approve, 1 revise, 0 flag-for-human. Non-approve: EZK-WOH-44:24 revise. Glossary: 15 items reviewed, all approve. No lens-leakage flags."
