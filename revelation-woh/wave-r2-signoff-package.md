# Revelation wave R2 (chapters 7, 8, 9, 10, 12, 13, 16, 21) — human sign-off package

**Scope:** 146 verses from the SBLGNT (Holmes 2010; CC BY 4.0), the chapters *Let's Welcome the Extra-Terrestrials* (ch. 2) reads verse by verse. Builds on the published chapters 1, 4, 6.

| Chapter | Verses | Approve | Revise | Flag |
|---|---|---|---|---|
| Revelation 7 — The sealing of the servants: 144,000 + the great multitude | 17 | 17 | 0 | 0 |
| Revelation 8 — The seventh seal: silence in heaven + the first four trumpets | 13 | 12 | 1 | 0 |
| Revelation 9 — The fifth and sixth trumpets: the star, the abyss, the locusts + the horsemen from the Euphrates | 21 | 21 | 0 | 0 |
| Revelation 10 — The mighty angel with the little book + the seven thunders | 11 | 11 | 0 | 0 |
| Revelation 12 — The woman clothed with the sun + the dragon cast down | 18 | 18 | 0 | 0 |
| Revelation 13 — The beast from the sea, the beast from the earth + the number 666 | 18 | 18 | 0 | 0 |
| Revelation 16 — The seven bowls: Har-magedon + the great earthquake and hail | 21 | 20 | 1 | 0 |
| Revelation 21 — The new heaven and new earth + the new Jerusalem descending | 27 | 26 | 1 | 0 |

- Lens leakage: none (21 reception notes checked against LWTE ch. 2). English-line changes over the draft: 2 (16:3 'every living being'; 16:9 'authority'), both approved.
- Overlay 1.1.0 → 1.2.0: 9 new direct entries + 1 extension. Central 2.80.0 → 2.81.0: 12 appliesTo extensions only (gophrit 'sulfur' extended to Greek *theion*). No speculative or inferred entries.

## Founder decisions (Editor + Reviewer both endorse all)
A 'sulfur' (not 'brimstone') · B 'God' for *theos* (canon English has Yahweh/Elohim; canon French 'Dieu') · C translate the critical text, naming the KJV/TR wording the canon's English quotes · D Greek-NT names rule (Israel, Satan, abyss in English; Hebrew-only central forms not applied to Greek lines) · E *exousia* 'authority' (jurisdiction) / 'power' (capacity to harm, ch. 9) · F 'every living being' 16:3 · G 'servants' (canon French 'esclaves') · H 'the pit of the abyss' · I 'Har-magedon' · J SBLGNT numbering keeps 12:18 ('he stood upon the sand'; ASV 13:1a).

## Fixes applied at sign-off (commentary only)
- 8:7: the clause is in the Byzantine majority text too; the Textus Receptus/KJV omit it with a minority of manuscripts (probably homoeoteleuton).
- 16:18: correct the variant note (SBLGNT and TR both read the plural *anthrōpoi egenonto*; editions differ on the number) and name the TR order 'voices, and thunders, and lightnings' quoted by the canon's English.
- 21:3: add SBLGNT *ek tou thronou* 'from the throne' vs TR *ek tou ouranou* 'out of heaven' (canon English quotes the latter), in the variant note and the reception note.
- Overlay variant-reporting entry: same three fixes; names entry: state the scope rule (Hebrew central entries apply to Greek lines only where their English is also correct for the Greek word — chayyot 7:11, gophrit 'sulfur').
- Optional, applied: 16:3 name TR *zōsa*; 21:4 TR 'for' before 'the former things'.

---

## Editor report (inlined)

# Revelation Wave R2 Editor Report: chapters 7, 8, 9, 10, 12, 13, 16, 21

**Book / chapters:** `revelation-woh` 7 (17 verses), 8 (13), 9 (21), 10 (11), 12 (18), 13 (18), 16 (21), 21 (27). That is 146 verses.
**Editor pass:** 2026-11-01 (claude-opus-5-5, woh-editor role).
**Status at end of pass:**
- All eight chapters moved from `draft` to `editor-review`, version `0.1.0` to `1.0.0-rc1`.
- `glossaryVersion` 2.81.0, pending application of `wave-r2-central-diff.json`.
- `overlayGlossaryVersion` 1.2.0. The overlay was edited directly, as the brief allowed.
- `reviewer` left `pending`. `claude-opus-5-5 (editor)` added to `modelDrafts`.

**Editorial questions:** 39 received, 39 resolved, all arrays emptied. None needed escalation. Ten resolutions are listed below as founder-preference points.

**Files written (only these)**

- `revelation-woh/chapter-{7,8,9,10,12,13,16,21}.json`
- `revelation-woh/_translation-glossary.json` (1.1.0 → 1.2.0)
- `revelation-woh/wave-r2-central-diff.json` (proposed, not applied; 2.80.0 → 2.81.0)
- this report

No central glossary file and no ezekiel-woh file was read for writing or written. `_meta.json` was not touched; see the follow-ups at the end.

## Counts

- **Commentary (`notes.official`):** 145 of 146 paragraphs. Only 8:6 is left blank: it is plain narrative with no divergence.
- **Wheel of Heaven reception notes:** 21. Each is a separately headed paragraph, "**Wheel of Heaven reading (reception note, not a translation claim).**", and each was checked against `revelation-canon-citations.md` (LWTE-2:155-228). The sites:
  - 7:3, covering 7:2-4
  - 8:1, a reading of the seventh seal; the canon does not quote the verse
  - 8:7
  - 8:8, covering 8:8-9
  - 8:10, covering 8:10-11
  - 8:12
  - 9:1, covering 9:1-2
  - 9:5, covering 9:3-6
  - 9:9, covering 9:7-10
  - 9:13
  - 9:18, covering 9:17-19
  - 10:4
  - 10:7
  - 12:12
  - 13:18, which also records the canon's identification of the beast
  - 16:18
  - 16:20
  - 16:21
  - 21:1
  - 21:2
  - 21:3, covering 21:3-4
- **English text changed at 2 verses.** Each change is backed by an overlay entry (rule 7):
  - **16:3** 'every living soul died' → 'every living being died' (`psyche-soul-life-living-being-rendering-revelation`). *psychē zōēs* is the Greek of *nep̄eš ḥayyâ* (Gen 1:20-21), used here of sea creatures. RSV and NRSV have 'every living thing'.
  - **16:9** 'who has the power over these plagues' → 'who has authority over these plagues' (`exousia-authority-power-rendering-revelation`). *exousia epi* + accusative is rendered 'authority over' at every site (6:8; 13:7; 16:9).
- All other lines are the Translator's draft, unchanged. No lens vocabulary appears in any line; a script check found none of 'Elohim', 'Yahweh', 'craft', 'missile', 'atomic' or 'nuclear' in the English.
- **Quotation marks:** the drafts already follow the convention (double for speech, single nested; speech across verses opened once and closed where it ends: 7:14-17; 12:10-12; 21:3-4; 21:6-8). Double quotes are balanced in every chapter. 16:15 keeps the unattributed quotation marks (see question 16:15).
- **glossaryRefs:** rebuilt. A verse now carries an entry only if the entry governs its line and the verse is in that entry's (post-diff) `appliesTo`; a script confirmed this for every ref.
  - Translator refs that only name a verse as a cross-corpus comparison were removed from `glossaryRefs` and are cited in the commentary as "background", following the Kings precedent (e.g. 2 Kgs 2:11):
    - `four-corners-...` and `twelve-gates-four-winds-...` (7:1)
    - `seal-on-forehead-...` (7:3; 13:16)
    - `seven-archangels-...` (8:2)
    - `pillar-of-cloud-and-fire-...` (10:1, a simile)
    - `aya-quranic-sign-...` (12:1, 3; 13:13-14; 16:14)
    - `lotanu-leviathan-...` (12:3, 9; 13:1)
    - `mastema-...` (12:9)
    - `four-kingdoms-...` (13:1)
  - `plant-of-rejuvenation-...` was dropped at 12:9. Its Gilgamesh plant-and-serpent topos has no bearing on the line.

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` (or `inferred`) entry is created or extended in the overlay or the central diff. All nine new overlay entries are `direct`, and all 12 central ops are appliesTo extensions of `direct` entries. Nothing in this pass blocks advance on the speculative count.

---

## Resolution of the 39 editorial questions

| refId | Question | Resolution | Governing entry |
|---|---|---|---|
| 7:3 | doulos 'servants' vs canon FR 'esclaves' | 'servants' kept (God as master); 'slaves' in social pair (13:16) | overlay `doulos-servant-slave-rendering-revelation` (new) |
| 7:4 | Israel / tribe names; Hebrew-scoped central entry | Standard English names; Hebrew-text entries not applied to Greek | overlay `greek-nt-proper-names-and-hebrew-scoped-entries-convention-revelation` (new) |
| 7:15 | skēnōsei ep' autous | 'will spread his tabernacle over them' kept (ASV) | overlay `skene-skenoo-tabernacle-dwell-rendering-revelation` (new) |
| 8:3 | dative tais proseuchais | 'add it to the prayers' kept (ASV); range noted | commentary |
| 8:7 | omission of 'a third of the earth' (TR/KJV, canon EN) | SBLGNT clause kept (agrees with canon FR) | overlay `sblgnt-base-text-variant-reporting-convention-revelation` (new) |
| 8:9 | psychē (8:9; 16:3) | 8:9 'those that had life' kept; **16:3 'every living being'** | overlay `psyche-soul-life-living-being-rendering-revelation` (new) |
| 8:13 | eagle vs angel | 'an eagle' (SBLGNT) | textual convention |
| 9:1 | abyssos (9:1, 2, 11) | 'the pit of the abyss' / 'the angel of the abyss' kept; `tehom` not applied | overlay `abyssos-pit-of-the-abyss-rendering-revelation` (new) |
| 9:3 | exousia consistency | Context rule: 'authority' for conferred jurisdiction, 'power' for bodily capacity (ch. 9); **16:9 changed** | overlay `exousia-authority-power-rendering-revelation` (new) |
| 9:9 | thōrax (canon FR 'thorax') | 'breastplates' kept; anatomical sense in commentary and reception note | commentary |
| 9:13 | [four] horns; canon 'Yahweh' | 'the horns' (SBLGNT); 'God' kept | textual convention; overlay `theos-god-rendering-against-canon-english-yahweh-revelation` (new); central `qarnot-ha-mizbeach-...` (extended) |
| 9:17 | theion 'sulfur' vs 'brimstone' | 'sulfur'; central gophrit extended to Greek | central `gophrit-va-esh-destruction-formula` (extended) |
| 9:21 | porneia | 'fornication' kept (ASV; consistent with central apostolic-decree entry at Acts 15:29) | commentary |
| 10:4 | TR 'their voices ... unto me' | SBLGNT kept | textual convention; central `sealed-book-...` (extended) |
| 10:6 | chronos | 'delay' kept (ASV/RSV/NRSV; BDAG) | commentary |
| 10:7 | proleptic aorist; euēngelisen | Draft kept | commentary; overlay `doulos-...` |
| 10:11 | epi + dative | 'over' kept (range noted) | commentary |
| 12:5 | poimainō 'rule' | 'rule' kept (Ps 2:9 LXX), 'shepherd' at 7:17 | commentary |
| 12:9 | Devil / Satan vs `ha-satan` | 'the Devil and Satan' kept as names; `ha-satan` not applied to Greek | overlay names/scope convention |
| 12:12 | TR 'inhabiters of' | SBLGNT kept | textual convention |
| 12:17 | TR 'Jesus Christ' | SBLGNT kept | textual convention; central `iēsous-...` (extended) |
| 12:18 | 'he stood' and versification | SBLGNT text and verse division kept | textual convention (see follow-up 2) |
| 13:8 | attachment of 'from the foundation of the world' | ASV attachment ('written'), with 17:8 parallel | commentary |
| 13:10 | Alexandrinus reading vs ASV | SBLGNT kept | textual convention |
| 13:15 | pneuma 'breath' | 'breath' kept | commentary |
| 13:18 | 666/616; 'number of a man'; 'count' | All kept; 616 and Nero gematria in commentary | textual convention |
| 16:5 | TR 'shalt be'; overlay extension | SBLGNT kept; overlay apo-ho-on convention + central apo-ho-on and ehyeh extended to 16:5 | overlay `apo-ho-on-...-convention` (extended); central (extended) |
| 16:7 | TR 'another out of the altar' | SBLGNT kept | textual convention |
| 16:15 | unmarked speech | Quotation marks without attribution kept (program convention) | commentary |
| 16:16 | Har-magedon | ASV 'Har-magedon' kept | overlay names/scope convention |
| 16:21 | talent weight; canon FR 'lingots' | Draft kept (no supplied 'every stone'); canon wording in reception note | commentary |
| 21:2 | 'I John'; canon 'Yahweh' | SBLGNT kept; 'God' kept | textual convention; overlay `theos-...` |
| 21:3 | laoi; [autōn theos]; skēnē | SBLGNT kept; 'tabernacle ... dwell' kept | textual convention; overlay `skene-...` |
| 21:4 | TR 'God shall wipe' | SBLGNT kept | textual convention; central `paradise-by-negation-...` (extended) |
| 21:6 | Gegonan vs Gegone | 'They have come to pass' kept | textual convention |
| 21:16 | furlongs | 'furlongs' kept (symbolic 12 × 1,000; ~2,200 km in commentary) | commentary |
| 21:17 | measure of a man/angel | ASV literal kept | commentary |
| 21:20 | gem names | ASV names, 'carnelian' for sardion (4:3 precedent) | overlay `foundation-stones-gem-names-rev-21-19-20` (new) |
| 21:24 | TR 'of them which are saved' | SBLGNT kept | textual convention |

One correction to the Translator's note at 9:13. The draft attributed the bracketed *tessarōn* to "P47, Sinaiticus corr., the Byzantine text". On Metzger's account it is the other way round: P47, Alexandrinus and the corrector of Sinaiticus **omit** the word, and the first hand of Sinaiticus and the Byzantine text read it. The commentary states it that way. The Reviewer should verify this against the NA28 apparatus.

---

## Founder-preference points (resolved, flagged for confirmation)

All of these are applied. Each can be reversed mechanically.

### A. Greek *theion* 'sulfur', not 'brimstone' (central, corpus-wide)

- **Decision:** Extend `gophrit-va-esh-destruction-formula` ('sulfur and fire') to Greek *theion* at Rev 9:17 (twice), 9:18 and 21:8.
- **Why:** The entry's rationale already renders the Revelation 'lake of fire and sulfur' passages with 'sulfur'.
- **Canon:** The canon's English edition quotes 9:18 with the KJV 'brimstone'. Its French has 'soufre'.
- **Alternative:** 'brimstone' at these four sites, recorded as an overlay exception.

### B. *theos* = 'God', not the canon English edition's 'Yahweh' / 'Elohim'

- **Decision:** 'God' everywhere, as in chapters 1, 4 and 6 and the other Greek NT books of the corpus.
- **Canon:** The canon's English edition writes 'Yahweh' at 9:13, 21:2, 21:3 and 21:4 and 'their Elohim' at 21:3. Its French original has 'Dieu' at all of them. The English wording is quoted in the reception notes.
- **Why:** *theos* does not render the Tetragrammaton.
- **Governing entry:** overlay `theos-god-rendering-against-canon-english-yahweh-revelation`.

### C. Critical text over the KJV wording quoted by the canon

- **Decision:** SBLGNT throughout. The variants the canon's English edition quotes are named in commentary: 8:7, 9:13 'four horns', 10:4, 21:2 'I John', 21:3 'his people ... their God', 21:4.
- **Note:** At 8:7 the critical text agrees with the canon's French against its English.
- **Governing entry:** overlay `sblgnt-base-text-variant-reporting-convention-revelation`.

### D. Greek proper names, and the scope rule for Hebrew-text central entries

- **Decision:**
  - Standard English names: Israel, Judah, Jerusalem, Michael, Euphrates, Babylon.
  - ASV transliterations for the names the text marks as Hebrew: Abaddon, Har-magedon.
  - 'the Devil and Satan' as names at 12:9; 'the devil' at 12:12.
  - The Hebrew-text central entries (`shivtei-yisrael-...` 'Yisra'el', `ha-satan` 'the adversary', `tehom` 'the deep', `nefesh-chayah`) are not applied to Greek lines; they are cited as background.
- **Placement:** The rule is project-wide in effect: Matthew, Mark, Luke and Acts already follow it in practice. Following "when in doubt: overlay", it is housed in the revelation overlay.
- **Recommendation:** Promote it to a central Greek-NT convention entry at the next central pass.

### E. *exousia*: context rule, and the 16:9 line change

- **Decision:**
  - 'authority' for conferred jurisdiction (12:10; 13:2-12; 16:9; precedent 6:8).
  - 'power' for the locusts' and horses' bodily capacity to harm (9:3, 10, 19; RSV/NRSV at 9:10, 19; canon English 9:10 'their power').
- **Line change:** 16:9 now reads 'authority'.
- **Alternatives:**
  - 'authority' throughout, which changes 3 lines in ch. 9 and reads awkwardly at 9:10, 19.
  - ASV per site, which reverts 16:9.

### F. 16:3 'every living being'

- **Decision:** replaces the ASV 'every living soul'.
- **Alternative:** revert to the ASV.

### G. *doulos* 'servants' at 7:3 and 10:7

- **Canon:** The canon's French reads 'esclaves' at both.
- **Decision:** The 1:1 / 6:15 split is kept: 'servants' with God as master, 'slaves' in the social pair.
- **Alternative:** 'slaves' throughout. This would also touch the signed-off 1:1 and 6:11.

### H. 'the pit of the abyss' (ASV), not the KJV 'bottomless pit' quoted by the canon's English edition

- **Canon:** The canon's French 'le puits de l'abîme' matches the ASV.

### I. 'Har-magedon' (ASV), not 'Armageddon' (KJV) or 'Harmagedon'

- The ASV form shows the element *har* 'mountain' without deciding the etymology.

### J. Versification at 12:18

- **Decision:** The SBLGNT/NA28 verse 12:18 ('And he stood upon the sand of the sea') is kept.
- **Consequence:** This departs from the hosted ASV reference edition, which has 17 verses in ch. 12 and prints the clause at 13:1. See follow-up 2.

---

## Glossary changes for review

### Central glossary (proposed in `wave-r2-central-diff.json`; base 2.80.0 → recommended 2.81.0)

- **Added:** none.
- **Modified, appliesTo only, unless noted:**
  - `gophrit-va-esh-destruction-formula`: +REV-WOH-9:17, 9:18, 21:8. The `strongs` field is extended with G2303 *theion* and G2306 *theiōdēs*. wohChoice is unchanged.
  - `apo-ho-on-rev-1-4-greek-grammatical-solecism-divine-name-cross-corpus`: +16:5
  - `ehyeh-asher-ehyeh-divine-name-revelation-ex-3-14-cross-corpus`: +16:5
  - `four-living-creatures-rev-4-6-8-ezek-1-chayyot-shiur-qomah-cross-corpus`: +7:11
  - `chayyot`: +7:11
  - `cosmic-silence-shem-ha-mephorash-revelation-tradition-cross-corpus-shiur-qomah-revelation-8-1`: +8:1
  - `qarnot-ha-mizbeach-horns-of-the-altar-cross-corpus`: +9:13
  - `sealed-book-dan-12-4-9-revelation-jubilees-cross-corpus`: +10:4
  - `michael-as-israels-prince-angel-dan-10-13-21-12-1-cross-corpus`: +12:7
  - `christos-māšîaḥ-anointed-one-cross-corpus-greek-hebrew-aramaic`: +12:10
  - `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus`: +12:17
  - `paradise-by-negation-no-predation-no-illness-no-aging-cross-corpus`: +21:4
- **Version:** No wohChoice is changed and no decision is reversed, so a minor bump is recommended.
- **Concurrency:** The ezekiel-woh Editor is writing a central diff from the same 2.80.0 base.
  - Each op carries `appliesToAdded` beside the complete array, so the merge can be done as a union.
  - `chayyot` and `cosmic-silence-...` carry EZK refIds and are the likeliest overlaps.
  - If the Ezekiel diff is applied first, renumber this one (and the chapters' `glossaryVersion`) to the next minor.

### Per-translation overlay (`_translation-glossary.json`, 1.1.0 → 1.2.0, applied)

- **Added** (all `direct`):
  - `sblgnt-base-text-variant-reporting-convention-revelation` (17 refIds)
  - `theos-god-rendering-against-canon-english-yahweh-revelation` (31 refIds: every verse with *theos*)
  - `greek-nt-proper-names-and-hebrew-scoped-entries-convention-revelation` (16)
  - `doulos-servant-slave-rendering-revelation` (3)
  - `exousia-authority-power-rendering-revelation` (10)
  - `psyche-soul-life-living-being-rendering-revelation` (3)
  - `skene-skenoo-tabernacle-dwell-rendering-revelation` (4)
  - `abyssos-pit-of-the-abyss-rendering-revelation` (3)
  - `foundation-stones-gem-names-rev-21-19-20` (5)
- **Modified:** `apo-ho-on-rev-1-4-solecism-preservation-convention`. appliesTo gains 16:5, and one sentence is appended to the rationale on the two-membered formula. The decision is unchanged.
- **Description field:** updated to list chapters 1-21 of the wave.

The new conventions describe renderings that the stable chapters 1, 4 and 6 already use: 1:1 'servants', 6:8 'authority', 6:9 'souls', 6:15 'slave', 4:3 'carnelian'. To avoid touching signed-off files, their appliesTo arrays list only wave-R2 refIds. The rationales cite the earlier verses as precedent.

---

## Follow-ups for the orchestrator (files this pass was not allowed to write)

1. **`revelation-woh/_meta.json`** still describes three chapters (chapterCount 3, paragraphCount 48, subtitle and description "chapters 1, 4, 6"). It needs the eight new chapter files (146 paragraphs; total 11 chapters / 194 paragraphs) and updated subtitle/description at publication.
2. **Interlinear/reference alignment at 12:18 / 13:1.** The hosted ASV edition (`data-library/revelation/chapter-12.json`) has 17 verses, and its 13:1 begins with 'And he stood upon the sand of the sea'. Any parallel-column or reference-alignment tooling must map REV-WOH-12:18 to ASV 13:1a.
3. **Central merge order with ezekiel-woh** (see above).
4. **Optional:** promote the names/scope rule (D) to the central glossary, and backfill the overlay appliesTo with the matching refIds of the stable chapters 1, 4 and 6 at their next revision.


---

## Reviewer report

### Revelation 7 — The sealing of the servants: 144,000 + the great multitude



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception notes without entering the line."}, {"glossary_id": "greek-nt-proper-names-and-hebrew-scoped-entries-convention-revelation", "status": "approve", "citations": ["BDAG s.vv. diabolos, Satanas, Abaddōn, Harmagedōn", "Aune, WBC 52B, ad loc. 12:9"], "reasoning": "Direct is correct for a presentation and scope convention. Recommendation (non-blocking): state the scope criterion explicitly. Hebrew-text central entries are applied to a Greek line when their English choice is also a correct rendering of the Greek lexeme (chayyot 'living creatures' at 7:11; gophrit 'sulfur' for theion). They are background only where applying them would import a Hebrew-specific form or sense (Yisra'el, 'the adversary', 'the deep'). Without that sentence the 7:11 chayyot ref and the gophrit extension look like exceptions to rule (4)."}, {"glossary_id": "doulos-servant-slave-rendering-revelation", "status": "approve", "citations": ["BDAG s.v. doulos", "Amos 3:7; 2 Kgs 17:23 (ʿeḇeḏ 'servants the prophets')"], "reasoning": "Direct is
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "17 verdicts: 17 approve. No revise or flag. Reception note at 7:3 verified."

### Revelation 8 — The seventh seal: silence in heaven + the first four trumpets

- **REV-WOH-8:7** — revise: English line approved: chalaza kai pyr memigmena en haimati, kai eblēthē (sg.) ... to triton tēs gēs katekaē is exactly rendered. Commentary fix only: the note says 'The Byzantine text behind the Textus Receptus and the KJV omits it', but the SBLGNT apparatus registers no disagreement here from Robinson-Pierpont, so the Byzantine majority text has the clause and the omission is a Textus Receptus (minority) reading. Proposed wording: 'The Textus Receptus and the KJV omit it, with a minority of manuscripts; the clause stands in the Byzantine majority text as well, and its loss is probably a homoeoteleuton, since three successive clauses end in katekaē.' The reception note is accurate (LWTE-2:161-163) and confined to the labelled paragraph.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "13 verdicts: 12 approve, 1 revise (8:7 commentary: the Textus Receptus omission is not the Byzantine majority's, since the SBLGNT apparatus shows Robinson-Pierpont has the clause; the English line is approved)."

### Revelation 9 — The fifth and sixth trumpets: the star, the abyss, the locusts + the horsemen from the Euphrates



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "21 verdicts: 21 approve. The 9:13 tessarōn attribution matches the reviewer's reading of Metzger and the SBLGNT marker; printed-NA28 sigla not checked in-session."

### Revelation 10 — The mighty angel with the little book + the seven thunders



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "11 verdicts: 11 approve."

### Revelation 12 — The woman clothed with the sun + the dragon cast down



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "18 verdicts: 18 approve. 12:18 versification endorsed."

### Revelation 13 — The beast from the sea, the beast from the earth + the number 666



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "18 verdicts: 18 approve. Non-blocking style option at 13:3 ('slain to death')."

### Revelation 16 — The seven bowls: Har-magedon + the great earthquake and hail

- **REV-WOH-16:18** — revise: English line approved: astrapai kai phōnai kai brontai ... aph' hou anthrōpoi egenonto epi tēs gēs ... tēlikoutos seismos houtō megas is exactly rendered. Commentary fix: the note says the Textus Receptus has the singular; the TR and KJV have the plural ('since men were'), and the singular anthrōpos egeneto is the reading NA28 prints (with Alexandrinus) against the SBLGNT's plural, so the NA28 divergence the overlay convention requires is unreported and the TR attribution is inverted. Proposed: 'The SBLGNT reads the plural anthrōpoi egenonto; NA28 prints the singular anthrōpos egeneto; the Textus Receptus has the plural (KJV since men were upon the earth). The sense is the same.' Also name the TR order 'voices, and thunders, and lightnings', which the canon's English edition quotes. The reviewer's NA28 wording is from recollection: check it against the printed NA28 before applying. Reception note verified; no leakage.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "21 verdicts: 20 approve, 1 revise (16:18 commentary: the TR/NA28 attribution of the singular/plural variant is inverted, and the NA28 divergence is unreported; the English line is approved). Line changes at 16:3 and 16:9 approved."

### Revelation 21 — The new heaven and new earth + the new Jerusalem descending

- **REV-WOH-21:3** — revise: English line approved: ēkousa phōnēs megalēs ek tou thronou ... Idou hē skēnē tou theou meta tōn anthrōpōn, kai skēnōsei met' autōn, kai autoi laoi autou esontai is exactly rendered; laoi and the NA28 [autōn theos] are correctly reported. Commentary fix: the SBLGNT's ek tou thronou 'from the throne' against the Textus Receptus ek tou ouranou (KJV 'out of heaven') is not reported, although the canon's English edition quotes that KJV wording here; the overlay convention requires that such variants be named. Add: 'ek tou thronou from the throne (SBLGNT, NA28) against ek tou ouranou out of heaven (Textus Receptus, KJV)', and add 'out of heaven' to the list of English-edition readings in the reception note. Reception note otherwise verified; no leakage.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T12:25:02Z"
- glossaryReview: [{"glossary_id": "sblgnt-base-text-variant-reporting-convention-revelation", "status": "revise", "citations": ["SBLGNT (Holmes 2010) variant markers at Rev 16:18 and 21:3, and their absence at 8:7, 10:4, 12:17, 16:7, 21:2", "Metzger, A Textual Commentary on the Greek New Testament (2nd ed. 1994)", "KJV Rev 8:7; 16:18; 21:3"], "reasoning": "claim_type direct is right: the entry declares which text is translated and how variants are reported. Three accuracy fixes. (1) The 8:7 omission is a Textus Receptus (minority) reading, not that of the Byzantine majority text, which the SBLGNT apparatus shows agreeing with SBLGNT; rephrase wherever 'Byzantine' is said there. (2) Add 21:3 'out of heaven' (TR ek tou ouranou, quoted by the canon's English) to the wohChoice list of KJV-wording variants, and 16:18 (NA28 singular anthrōpos egeneto; TR order 'voices, thunders, lightnings'). (3) Add REV-WOH-16:18's NA28 divergence to the 'NA28 bracketed or divergent readings reported' sentence. The decision itself stands."}, {"glossary_id": "theos-god-rendering-against-canon-english-yahweh-revelation", "status": "approve", "citations": ["BDAG s.v. theos", "LXX usage: kyrios for the Tetragrammaton, theos for ʾĕlōhîm", "LWTE ch. 2 (FR 'Dieu' at 9:13, 21:2-4)"], "reasoning": "Direct is correct: theos never renders the Tetragrammaton in the LXX or NT, the canon's French reads 'Dieu' at every site, and published chapters 1, 4, 6 use 'God'. The canon's English 'Yahweh'/'Elohim' is recorded in reception 
- lens-leakage-flags: []
- lensLeakageCheck: "Every English line was checked: all 146 lines, and specifically the 21 reception-note sites (7:3, 8:1, 8:7, 8:8, 8:10, 8:12, 9:1, 9:5, 9:9, 9:13, 9:18, 10:4, 10:7, 12:12, 13:18, 16:18, 16:20, 16:21, 21:1, 21:2, 21:3). A script found no Elohim, Yahweh, YHWH, craft, missile, atomic, nuclear, planet, Eternals, loudspeaker or similar lens vocabulary in any line. The only hits were 'ship(s)' (8:9 ploia; worship) and 'Israel' (substring 'rael'), both benign. Each Wheel of Heaven reading sits in its own headed paragraph labelled 'reception note, not a translation claim'. Each was verified against LWTE ch. 2 (LWTE-2:155-228), FR and EN. No line resolves an ambiguity in the canon's direction: the visionary hōs/homoios markers are kept (8:8; 9:7-10), 'the number of a man' stays open (13:18), 'breastplates' is used rather than the canon's French 'thorax' (9:9), 'pit of the abyss' is kept (9:1), and theos is 'God' where the canon's English has 'Yahweh'/'Elohim' (9:13; 21:2-4). Where the line and the canon's English diverge, the line follows the Greek critical text, and at 8:7 that text agrees with the canon's French."
- escalationReportAdjustments: "Initial verdicts on all 146 verses, the 10 overlay entries touched and the 13 diff ops were formed from the chapters, the SBLGNT sources (including the sigla-bearing Rev.txt in the scratchpad), the overlay, the diff and the 2.80.0 base before opening wave-r2-editor-report.md. After reading the report, no verdict changed. The report's Founder point C lists the KJV-wording variants named in commentary (8:7, 9:13, 10:4, 21:2, 21:3 'his people ... their God', 21:4). It omits 21:3 'out of heaven', which confirms the reviewer's 21:3 revise. Its 9:13 request ('the Reviewer should verify this against the NA28 apparatus') was met as far as possible: the SBLGNT marker confirms a collated edition reads tessarōn, and the corrected attribution agrees with the reviewer's reading of Metzger. The printed NA28 apparatus was not available, so this is recorded as unverified at the sigla level, not as a defect. The report's 'All other lines are the Translator's draft, unchanged' was confirmed by diffing against the rev_r2 backup: only 16:3 and 16:9 differ."
- founderDecisionRecommendations: {"A-theion-sulfur": "Endorse. LXX theion = gophrit (Gen 19:24), BDAG 'sulfur', NRSV 'sulfur' at all four sites; the central entry already renders the Revelation lake passages 'sulfur'. The canon's English 'brimstone' (9:18) is recorded.", "B-theos-God-not-Yahweh-Elohim": "Endorse firmly. theos does not render the Tetragrammaton, the canon's own French has 'Dieu', and chapters 1, 4, 6 are signed off with 'God'. Writing 'Yahweh' would translate the canon's English edition, not the Greek.", "C-critical-text-over-KJV-wording": "Endorse. Complete the inventory: add 21:3 'out of heaven' (TR ek tou ouranou) and 16:18 (NA28 singular; TR order 'voices, thunders, lightnings'); correct 8:7 to say the omission is a TR reading, not the Byzantine majority's. Optionally name 16:3 zōsa and 21:4 hoti.", "D-names-and-scope-rule": "Endorse, and support promotion to a central Greek-NT convention. Add the explicit criterion (apply where the central English is also a correct rendering of the Greek lexeme; background where it imports a Hebrew-specific form), which explains chayyot at 7:11 and gophrit for theion.", "E-exousia": "Endorse. The context rule follows BDAG's sense division and RSV/NRSV practice; 16:9 'authority over' aligns with 6:8 and 13:7. Uniform 'authority' would read badly at 9:10, 19.", "F-16:3-living-being": "Endorse. 'soul' for sea creatures imports a personal sense; 'living being' keeps the noun and the nep̄eš ḥayyâ echo.", "G-doulos-servants": "Endorse. Keeps the signed-off 1:1
- summary: "27 verdicts: 26 approve, 1 revise (21:3 commentary: add the throne/heaven variant, ek tou thronou vs TR ek tou ouranou, quoted by the canon's English; the English line is approved)."
