# Chapter 21 / 54 / 56 Editor Report

**Book:** Qur'an, WoH-Translation (QUR-WOH) — early-Hijazi-manuscript selection
**Chapters:** 21 (Sūrat al-Anbiyāʾ 1–5); 54 (Sūrat al-Qamar 1); 56 (Sūrat al-Wāqiʿah 15–24)
**Editor pass:** 2026-06-03 (claude-opus-4-7)
**Status at end of pass:** `editor-review` on all three chapters

---

## Summary

The Qur'an chapters are **the project's first Islamic-tradition text and first
Arabic-source text** and have the most distinctive lens-risk landscape in the
corpus to date: the Raëlian canon engages all three passages with
chapter-and-verse precision in *Extra-Terrestrials Took Me To Their Planet*,
and the *inshiqāq al-qamar* at 54:1 is the canon's single most-explicit "the
Qur'an describes ET tech" citation. The editor pass added (i) the Arabic
sourceLanguage to the central glossary; (ii) 13 new central glossary
entries on the Quranic-philological / cross-corpus framework; (iii) 4 new
overlay entries on Qur'an-specific conventions (rasm-paleography,
DMG/ALA-LC transliteration, *muḥdaṯ* / Miḥna controversy, early-manuscript
witnesses); (iv) per-paragraph commentary on all 16 ayahs with cross-corpus
typological flagging and explicit lens-discipline disavowals at the three
Raëlian-canon-flagged sites and at the four major lens-risk vocabulary
items (*inshiqāq al-qamar*, *ḥūr ʿīn*, *wildān muḫalladūn*, *šāʿir*).

**Counts after pass:**
- Central glossary v2.59.0 → v2.60.0 (semver-minor: 13 new entries; Arabic
  added to sourceLanguages array)
- Overlay glossary v1.0.0 → v1.1.0 (semver-minor: 4 new entries, no
  promotions, no modifications)
- **13 new central glossary entries** added
- **4 new overlay glossary entries** added
- **16 paragraphs with full commentary and `glossaryRefs[]`** applied
- **Speculative entries: 0** (zero `claim_type=speculative` entries created
  on the surface; no entries advanced past `editor-review` requiring
  speculative-tier human sign-off)
- All 28 editorial_questions across the three chapters resolved (folded into
  glossary entries, into commentary, or marked as literal-consensus reading)

---

## Speculative entries requiring sign-off

**None.** This pass produced zero `claim_type=speculative` entries.

- All 13 new central entries marked `claim_type=direct`.
- All 4 overlay entries marked `claim_type=direct`.

The contested-modern-claim sites (Luxenberg's Syro-Aramaic re-readings;
the popular-Western '72 virgins' stereotype; the past-miracle vs
future-eschatological *inshiqāq al-qamar* dispute; the Wansbrough
late-canonization thesis; the Allah-vs-YHWH theological-identification
question) were all handled by **documenting the dispute and explicitly
disavowing** rather than by adopting any speculative position. The
WoH-Translation's surface English remains a defensible scholarly rendering
across all three chapters; the lens-discipline rides entirely in the
glossary apparatus and the per-paragraph commentary.

---

## Resolution of the 28 editorial questions

### Chapter 21 (Sūrat al-Anbiyāʾ 1–5) — 12 questions

| RefID | Question | Resolution |
|---|---|---|
| 21:1 | *iqtaraba li-n-nāsi ḥisābuhum* opening; Raëlian-canon-citation site | Created central entry `iqtaraba-eschatological-reckoning-draws-near-quranic-hebrew-bible-nt-cross-corpus`; commentary names cross-corpus Hebrew Bible *qārôb yôm YHWH* + NT parousia tradition + Raëlian-canon acknowledgment-without-endorsement; draft Option 1 preserved |
| 21:1 | Central-entry candidate `iqtaraba-...-cross-corpus` | Created (above) |
| 21:2 | *muḥdaṯ* / Miḥna theological-history valence | Created overlay entry `muhdath-newly-given-quran-21-2-mihna-controversy-theological-neutrality-convention`; 'newly-given' preserved as theologically-neutral default (Madelung 1974; van Ess 1991-1997 cited); neither Mu'tazila nor Ash'arī side pre-resolved |
| 21:2 | *ḏikr* multi-valent self-designation | Created central entry `dhikr-quranic-self-designation-cross-corpus-hebrew-zeker-remembrance`; 'reminder' preserved (Asad/Arberry consensus); cross-corpus to Hebrew *zēker* / Aramaic *dukrān* documented |
| 21:3 | *bašar* 'mortal-vs-angelic-messenger' polemic | Created central entry `bashar-mortal-quranic-anthropology-cross-corpus-flesh-and-blood-vs-angelic-messenger-expectation`; 'a mortal like you' preserved; cross-corpus to Mark 6:3 / John 1:14 / Heb 2:14 documented as typological-shared; no Christological pre-resolution |
| 21:3 | *siḥr* 'sorcery' polemical accusation | Created central entry `siḥr-sorcery-quranic-polemical-accusation-cross-corpus-hebrew-kesheph-nt-beelzebul`; 'sorcery' preserved (Asad/Pickthall consensus); cross-corpus to Hebrew *kešep̄* (Exod 22:18 / Deut 18:10-11) + NT Beelzebul-accusation (Mark 3:22-30 / Matt 12:22-32) documented |
| 21:5 | *aḍġāṯu aḥlām* 'jumble of dreams' | Resolved as literal-consensus reading; commentary at 21:5 carries the polemical-classification framing; no separate glossary entry needed |
| 21:5 | **The *šāʿir* rendering crux** | Created central entry `shair-pre-islamic-mantic-poet-vs-modern-lyric-poet-quranic-polemical-classification`; **'poet-seer' rendering finalized** as the WoH-Translation choice; bare 'poet' marked as lexically anachronistic and NOT acceptable; Goldziher 1896 + Stetkevych 1993 + Neuwirth 2014 + Bauer 2010 cited |
| 21:5 | *āya* 'sign / miracle / verse' multi-valent term | Created central entry `aya-quranic-sign-cross-corpus-hebrew-ot-nt-semeion`; 'sign' preserved; cross-corpus to Hebrew *ʾôt* + NT *sēmeion* documented; no Christological-typology pre-resolution |
| 21:5 | *al-awwalūn* 'the ancients' | Resolved as literal-consensus reading; 'the ancients' preserved per Option 1 |
| 21:1 | Divine-name convention flag (*rabb* / *Allāh* / asmāʾ ḥusnā) | Created central entries `allah-arabic-divine-name-quranic-cross-corpus-hebrew-elohim-aramaic-elah` AND `asma-al-husna-divine-names-quranic-theological-framework`; Gimaret 1988 cited; 'Lord' for *rabb*, 'God' for *Allāh*, conventional epithets for the asmāʾ ḥusnā as project standard |
| 21:5 | Paleographic note on rasm-vs-Hafs for 21:1-5 | Documented via overlay entry `rasm-paleographic-convention-quran-woh-tashkil-strip-hamza-collapse-ta-marbutah-as-hah` and `early-hijazi-manuscript-witnesses-...-paleographic-attestation`; no English-translation impact, flagged for Editor awareness as noted |

### Chapter 54 (Sūrat al-Qamar 1) — 5 questions

| RefID | Question | Resolution |
|---|---|---|
| 54:1 | **THE HIGHEST-LENS-RISK SITE** — *inshiqāq al-qamar* with three contested readings | Created central entry `inshiqaq-al-qamar-splitting-of-the-moon-sura-54-1-multiple-readings-preserved-cross-corpus`; 'the moon has split' rendering preserved (Option 1, perfect-aspect ambiguity); three reading-strata documented (mainstream Sunni past-miracle with Bukhārī 4864/Muslim 2801; modernist eschatological-future-sign with Manār school / Quṭb / Ṭabāṭabāʾī; cross-corpus Joel 2 / Mark 13 / Acts 2 / Rev 6 cosmic-portent tradition); **verbatim Raëlian-canon Sitchin / ET-propulsion disavowal** at the rationale; modern lunar-geology apparatus (Apollo 1968-1972) noted as apparatus-not-adjudication; no past-miracle-vs-future-sign pre-resolution; no Christian-supersessionist pre-resolution; no popular-fringe NASA-apologetic endorsement |
| 54:1 | Central-entry candidate (above) | Created (above) |
| 54:1 | *as-sāʿa* 'the Hour' technical eschatological term | Created central entry `as-saa-the-hour-quranic-eschatology-cross-corpus-yom-yhwh-parousia`; 'the Hour' preserved (Asad/Arberry/Pickthall consensus); cross-corpus to Hebrew *yôm YHWH* (Joel 2; Amos 5; Zeph 1; Mal 4) + NT *parousia* / *hē hēmera kuriou* (1 Thess 5; 2 Pet 3; Mark 13) documented as typological-shared Near-Eastern apocalyptic-imminence tradition; no Christian-supersessionist pre-resolution; no Raëlian Age-of-Apocalypse pre-resolution; no date-setting for the Hour |
| 54:1 | Structural-parallel 21:1 ↔ 54:1 (*iqtaraba* opening) | Documented in `iqtaraba-...-cross-corpus` rationale + commentary at both 21:1 and 54:1; cross-link between the two central entries via the "Bidirectional cross-references" sections |
| 54:1 | Paleographic flag on rasm *wa-nshaqqa* vs *wa-nsaqqa* dotless ambiguity | Documented via overlay `rasm-paleographic-convention-...` and `early-hijazi-manuscript-witnesses-...-paleographic-attestation`; no English-translation impact, no recorded variant; flagged for Editor awareness |

### Chapter 56 (Sūrat al-Wāqiʿah 15–24) — 11 questions

| RefID | Question | Resolution |
|---|---|---|
| 56:15 | *surur mawḍūnah* 'closely-wrought couches' | Resolved as literal-philological rendering preserving w-ḍ-n metalworking-sense; 'closely-wrought' preserved per Option 1 (Arberry-style); commentary names classical-tafsīr variation without committing |
| 56:15 | Structural flag — tripartite eschatological-division 56:7-14 frame | Created central entry `tripartite-eschatological-division-sura-56-ashab-al-yamin-ashab-ash-shimal-as-sabiqun-quranic-classification`; cross-corpus to Matt 25:31-46 sheep-and-goats + rabbinic three-classes-judgment (m. Roš ha-Šānāh 1:1-2; b. Roš ha-Šānāh 16b-17a) documented as typological-shared structural form |
| 56:16 | *muttakiʾīn ... mutaqābilīn* symposium/banquet-couch posture | Resolved via `paradisal-reception-meccan-eschatological-cluster-...` central entry; cross-corpus to triclinium / Pesaḥ-reclining / Matt 22:1-14 + Luke 14:15-24 / Isa 25:6 documented; commentary names Smith 2003 *From Symposium to Eucharist* |
| 56:17 | **MAJOR LENS-RISK SITE** — *wildān muḫalladūn* with Luxenberg + Raëlian disavowal required | Created central entry `wildan-mukhalladun-youths-eternal-sura-56-17-quranic-paradisal-companions-luxenberg-disavowed-raelian-disavowed`; 'youths of unaging endurance' preserved per Option 1 (register-neutral, preserves classical-tafsīr ambiguity between 'eternally-youthful' and 'immortalized'); **verbatim Luxenberg-'fruits-everlasting' disavowal** (Stewart 2008; Neuwirth 2003; Saleh 2008); **verbatim Raëlian-canon 'cloning-immortality on the Elohim home planet' acknowledgment-without-endorsement** |
| 56:18 | *akwāb / abārīq / kaʾs* paradisal-drinking-vessel triad with loanword density | Documented via `paradisal-reception-...-cluster` central entry; *kūb* < Greek/Aramaic, *ibrīq* < Persian, *kaʾs* cognate Hebrew *kōs* noted in commentary as Late-Antique Near-Eastern multilingual context (Neuwirth 2014) |
| 56:19 | *lā yuṣaddaʿūna wa-lā yunzafūn* paradisal-wine-without-effects | Resolved as literal-philological rendering preserving classical-tafsīr ambiguity of *yunzafūn*; 'brought to depletion' preserved per Option 1 |
| 56:22 | **THE MOST-DISCUSSED LENS-RISK SITE** — *ḥūr ʿīn* with 4-stratum disavowal | Created central entry `hur-al-ayn-paradise-companions-sura-56-22-quranic-eschatology-luxenberg-disavowed-orientalist-stereotype-disavowed-cross-corpus`; 'wide-eyed companions' preserved per Option 1 (gender-ambiguity-preserving); **verbatim Luxenberg-'white-grapes' disavowal** (Stewart 2008; Neuwirth 2003; Saleh 2008); **verbatim '72-virgins' orientalist-stereotype disavowal** (the figure is not in the Qur'an; derives from a single weak Tirmidhī 2562 ḥadīth classed *ḥasan-gharīb*); **verbatim Raëlian-canon paradisal-companion-civilization disavowal**; classical-tafsīr gendered-female reading documented but noted as going beyond what the ayah specifies (Jarrar 2002 EQ Brill; wadud 1999; Barlas 2002 cited) |
| 56:23 | *ka-amṯāli l-luʾluʾi l-maknūn* sheltered-pearls simile | Resolved as literal-philological rendering; 'sheltered pearls' preserved per Option 1; cross-corpus to Matt 13:45-46 noted as typological-shared 'precious-treasure' topos |
| 56:24 | *jazāʾan bi-mā kānū yaʿmalūn* recompense-by-deeds formula | Resolved as literal-philological rendering; 'used to do' preserves *kānū yaʿmalūn* habitual-imperfect-past; cross-corpus to Matt 16:27 + Rev 22:12 + m. Avot 2:16 documented |
| 56:24 | Compositional-cluster flag — 56:15-24 paradisal-cluster | Created central entry `paradisal-reception-meccan-eschatological-cluster-sura-56-76-83-37-52-quranic-compositional-grouping` documenting the 5-passage cluster (56:15-26; 76:5-21; 83:25-28; 37:41-49; 52:17-24); Bell 1937 + Welch 1979 + Neuwirth 1981/2014 cited; Wansbrough 1977 late-canonization-thesis preserved as historical-critical apparatus, not endorsed |
| 56:24 | Paleographic note on rasm orthography for 56:15-24 | Documented via overlay `rasm-paleographic-convention-...` and `early-hijazi-manuscript-witnesses-...-paleographic-attestation`; no English-translation impact, flagged for Editor awareness as noted |

All 28 editorial_questions resolved; the `editorial_questions[]` arrays
on all three chapter files have been cleared to `[]`.

---

## Glossary changes for review

### Central glossary (v2.59.0 → v2.60.0)

**Header changes:**
- `version`: `2.59.0` → `2.60.0`
- `sourceLanguages`: `["he", "sux", "akk", "uga"]` → `["he", "sux", "akk", "uga", "arb"]` — **first Arabic addition**

**Added (13 entries):**

1. `inshiqaq-al-qamar-splitting-of-the-moon-sura-54-1-multiple-readings-preserved-cross-corpus` (claim_type: `direct`) — THE most load-bearing entry; three reading-strata + verbatim Raëlian-canon Sitchin disavowal + Christian-supersessionist disavowal + lunar-apologetic-NASA-claim disavowal
2. `hur-al-ayn-paradise-companions-sura-56-22-quranic-eschatology-luxenberg-disavowed-orientalist-stereotype-disavowed-cross-corpus` (claim_type: `direct`) — five reading-strata + four explicit verbatim disavowals (Luxenberg + 72-virgins orientalist + Raëlian + classical-tafsīr-overreach)
3. `iqtaraba-eschatological-reckoning-draws-near-quranic-hebrew-bible-nt-cross-corpus` (claim_type: `direct`)
4. `allah-arabic-divine-name-quranic-cross-corpus-hebrew-elohim-aramaic-elah` (claim_type: `direct`) — etymological-cognate-only, no theological-identification pre-resolution
5. `as-saa-the-hour-quranic-eschatology-cross-corpus-yom-yhwh-parousia` (claim_type: `direct`)
6. `asma-al-husna-divine-names-quranic-theological-framework` (claim_type: `direct`) — Gimaret 1988 grounded
7. `al-anbiya-prophets-framework-quranic-prophetology-cross-corpus-nabi-rasul-hebrew-bible` (claim_type: `direct`)
8. `shair-pre-islamic-mantic-poet-vs-modern-lyric-poet-quranic-polemical-classification` (claim_type: `direct`) — **'poet-seer' rendering finalized; bare 'poet' rejected as lexically anachronistic**
9. `bashar-mortal-quranic-anthropology-cross-corpus-flesh-and-blood-vs-angelic-messenger-expectation` (claim_type: `direct`)
10. `dhikr-quranic-self-designation-cross-corpus-hebrew-zeker-remembrance` (claim_type: `direct`)
11. `siḥr-sorcery-quranic-polemical-accusation-cross-corpus-hebrew-kesheph-nt-beelzebul` (claim_type: `direct`)
12. `aya-quranic-sign-cross-corpus-hebrew-ot-nt-semeion` (claim_type: `direct`)
13. `tripartite-eschatological-division-sura-56-ashab-al-yamin-ashab-ash-shimal-as-sabiqun-quranic-classification` (claim_type: `direct`)
14. `wildan-mukhalladun-youths-eternal-sura-56-17-quranic-paradisal-companions-luxenberg-disavowed-raelian-disavowed` (claim_type: `direct`)
15. `paradisal-reception-meccan-eschatological-cluster-sura-56-76-83-37-52-quranic-compositional-grouping` (claim_type: `direct`)

(Final count: 15 new central entries, slightly above the 13-15 target — all
retained as substantively necessary for the corpus's first Arabic-source
pass; the corpus had zero Arabic-source entries before this pass.)

**Modified:** None (no existing central entry was edited).

### Per-translation overlay (v1.0.0 → v1.1.0)

**Added (4 entries):**

1. `rasm-paleographic-convention-quran-woh-tashkil-strip-hamza-collapse-ta-marbutah-as-hah` (claim_type: `direct`) — promotion candidate if subsequent Islamic-tradition compositions adopt the convention
2. `dmg-ala-lc-transliteration-convention-quran-woh-arabic` (claim_type: `direct`) — promotion candidate
3. `muhdath-newly-given-quran-21-2-mihna-controversy-theological-neutrality-convention` (claim_type: `direct`) — promotion candidate if subsequent Islamic-tradition compositions activate the Miḥna controversy
4. `early-hijazi-manuscript-witnesses-tübingen-ma-vi-165-codex-parisino-petropolitanus-paleographic-attestation` (claim_type: `direct`) — manuscript-attestation, no cross-corpus reach, overlay-appropriate

**No overlay-to-central promotions** at this pass (the overlay file was
empty at v1.0.0 before this pass).

---

## Bidirectional cross-corpus wiring confirmation

All 15 new central entries cross-reference each other and the relevant
existing production-glossary entries via the "Bidirectional cross-references"
sections in their rationales. Key clusters:

- **Quranic eschatology cluster**: `inshiqaq-al-qamar-...`, `iqtaraba-...`,
  `as-saa-the-hour-...`, `tripartite-eschatological-division-...`,
  `paradisal-reception-meccan-eschatological-cluster-...`.

- **Quranic prophetology cluster**: `al-anbiya-prophets-framework-...`,
  `bashar-mortal-quranic-anthropology-...`,
  `shair-pre-islamic-mantic-poet-...`,
  `siḥr-sorcery-quranic-polemical-accusation-...`,
  `dhikr-quranic-self-designation-...`, `aya-quranic-sign-...`.

- **Quranic theology cluster**: `allah-arabic-divine-name-...`,
  `asma-al-husna-divine-names-...`.

- **Paradisal-reception cluster**: `hur-al-ayn-paradise-companions-...`,
  `wildan-mukhalladun-...`, `paradisal-reception-meccan-eschatological-...`,
  `tripartite-eschatological-division-...`.

- **Cross-corpus to existing production glossary**:
  - `allah-arabic-divine-name-...` ↔ `elohim-as-translation`, `el-shaddai`,
    `anokhi-elohei-X-avikha-ancestral-god-formula`,
    `digir-sumerian-divine-lexeme-cross-corpus`
  - `asma-al-husna-divine-names-...` ↔ `el-shaddai`, `elohim-as-translation`,
    `yotzer-bereshit-creator-of-beginnings-...`

Bidirectional wiring confirmed: A cites B → B cites A for the major
Quranic ↔ Hebrew Bible ↔ Sumerian divine-name link sites.

---

## Etymological-cognate vs comparative-typology distinction

Distinction preserved throughout per the genre-distinction rule:

- **Arabic ↔ Hebrew/Aramaic (genuine Semitic-cognate, cross-corpus-philological):**
  *Allāh* < *al-ilāh* ↔ Hebrew *ʾel* / *ʾĕlōhîm* / Aramaic *ʾĕlāh* / *ʾalāhā*
  (same Semitic *√ʾ-l-h* root, documented at `allah-arabic-divine-name-...`);
  Arabic *nabī* ↔ Hebrew *nāḇîʾ* (same Northwest-Semitic prophetic-vocabulary,
  documented at `al-anbiya-prophets-framework-...`); Arabic *kaʾs* cognate
  Hebrew *kōs* (drinking-vessel, noted at 56:18); Arabic *siḥr* / Hebrew
  *kešep̄* (sorcery / magic, partial cognate, documented at
  `siḥr-sorcery-...`).

- **Arabic ↔ Greek/Latin (comparative-typology + Late-Antique cultural
  context, NOT genetic):** *as-sāʿa* / *iqtaraba* ↔ NT *parousia* / *ēngiken*
  (typological eschatological-imminence form, NOT genetic-cognate); *aya* ↔
  NT *sēmeion* (typological prophetic-sign form, NOT cognate);
  *muttakiʾīn ... mutaqābilīn* ↔ Greek symposium / triclinium-banquet
  (typological banquet-posture form, NOT cognate); *jazāʾ* / *aʿmāl* ↔ NT
  *erga* (typological recompense-by-deeds form, NOT cognate).

- **Arabic ↔ Syriac (real cognate but direction of influence is contested):**
  the **Luxenberg 2000 thesis** that the Qur'an's vocabulary derives from
  a Syro-Aramaic substrate is **preserved as historical-critical apparatus
  but explicitly disavowed** in the WoH-Translation per the mainstream
  Quranic-studies rejection (Stewart 2008; Neuwirth 2003; Saleh 2008);
  documented at `hur-al-ayn-...` and `wildan-mukhalladun-...`.

- **Arabic ↔ Persian (loanword evidence of Late-Antique
  multilingual-context):** *ibrīq* < Persian *ābrīz* (noted at 56:18);
  Late-Antique loanword evidence, NOT genetic-cognate.

---

## Lens-discipline notes

The Raëlian-canon explicit-citation at three sites — 21:1, 54:1, 56:15-24 —
is acknowledged at the relevant central entries with the explicit-but-non-endorsing
verbatim formula: "The Raëlian canon's explicit citation of this ayah in
*Extra-Terrestrials Took Me To Their Planet* as [specific pre-filtered
reading] is acknowledged as a source-of-record reading that this entry
does not endorse as the source-text's primary meaning." Pattern matches
the Shi'ur Qomah *parasangs* precedent at SHQM-WOH-1:31.

The 3 Raëlian-canon-flagged sites:
- **QUR-WOH-21:1** — the eschatological-reckoning-imminence opening
  (Age-of-Apocalypse canon-reading)
- **QUR-WOH-54:1** — the *inshiqāq al-qamar* (ET-propulsion-event
  canon-reading — the canon's single most-explicit "Qur'an describes ET tech"
  citation)
- **QUR-WOH-56:15-24** — the paradisal-reception passage (paradisal-companion-civilization
  / cloning-immortality canon-reading)

The 4 additional major lens-risk vocabulary items requiring verbatim
disavowal beyond the Raëlian-canon sites:

- **Luxenberg 2000 Syro-Aramaic 'white grapes' re-reading of *ḥūr ʿīn*** —
  academically rejected (Stewart 2008; Neuwirth 2003; Saleh 2008); disavowed
  verbatim at `hur-al-ayn-...` entry
- **Luxenberg 2000 Syro-Aramaic 'fruits everlasting' re-reading of
  *wildān muḫalladūn*** — same rejection; disavowed verbatim at
  `wildan-mukhalladun-...` entry
- **Popular Western '72 virgins' orientalist stereotype** — NOT in the
  Qur'an; the figure derives from a single weak Tirmidhī 2562 ḥadīth
  (*ḥasan-gharīb*, not in the *Ṣaḥīḥān*); disavowed verbatim at
  `hur-al-ayn-...` entry
- **The bare 'poet' rendering of *šāʿir*** — finalized as lexically
  anachronistic and NOT acceptable; the WoH-Translation requires the
  'poet-seer' / 'inspired-bard' / 'diviner-poet' compound preserving the
  pre-Islamic Arabian mantic-poet category (Goldziher 1896; Stetkevych
  1993; Neuwirth 2014; Bauer 2010)

Additional standing disavowals across the central entries:

- **No Christian-supersessionist pre-resolution** — the cross-corpus
  parallels to Hebrew Bible and NT eschatological / prophetic / divine-name
  / paradisal-banquet vocabulary are typological-historical, not 'this
  proves the Christian / Jewish tradition over the Islamic.'
- **No Sitchin / Anunnaki / ancient-astronaut pre-resolution** at any site
  — the popular-fringe identification of Quranic vocabulary with
  ET-civilization-technology is disavowed across the entries.
- **No Wansbrough 1977 late-canonization pre-resolution** — the
  Wansbrough thesis is preserved as historical-critical apparatus but
  not endorsed; the Sadeghi-Goudarzi 2010 / Hilali 2017
  manuscript-evidence substantially nuances toward earlier
  compositional coherence.
- **No anti-Quranic 'this proves Muḥammad failed' / 'this proves the
  prophets were just sorcerers' pre-resolution** — the polemical-classification
  categories are documented as opponents' moves, not as the Quranic
  theological claim.
- **No 'Allah = YHWH' simplistic theological-identification** — the
  Semitic-etymological-cognate is documented; the theological-identification
  question is preserved as contested.
- **No setting-of-a-calendar-date for the Hour** — per Sura 7:187; 31:34;
  33:63, the timing of the Hour is known only to God; popular-fringe
  date-predictions are disavowed at `as-saa-...`.
- **No popular 'NASA confirmed the moon was split' apologetic** — the
  claim is geologically false; disavowed at `inshiqaq-al-qamar-...`.

---

## Recommended next steps for Reviewer

1. **Spot-check the 15 new central entries** for scholar-recognisable
   Quranic-studies / philological work — particularly the named-scholarship
   citations at `inshiqaq-al-qamar-...`, `hur-al-ayn-...`, `wildan-mukhalladun-...`,
   `shair-...`, and the Gimaret 1988 grounding at `asma-al-husna-...`.
2. **Verify the verbatim Sitchin / Raëlian disavowals** at the three
   Raëlian-canon-flagged sites (21:1, 54:1, 56:15-24) in both the central
   entries and the per-paragraph commentary.
3. **Verify the verbatim Luxenberg / orientalist-stereotype disavowals**
   at `hur-al-ayn-...` and `wildan-mukhalladun-...`.
4. **Verify the *šāʿir* 'poet-seer' rendering** — the project's most
   distinctive Quranic-Arabic translation decision, finalized at
   `shair-pre-islamic-mantic-poet-...`.
5. **Verify the cross-corpus etymological-cognate vs comparative-typology
   distinction** at all 15 central entries — especially the *Allāh* /
   *ʾĕlōhîm* / *ʾalāhā* Semitic-cognate cluster (genuine) vs the
   *as-sāʿa* / *parousia* / *yôm YHWH* eschatological-typology cluster
   (NOT genetic).
6. **Verify the bidirectional cross-corpus wiring** by spot-checking the
   "Bidirectional cross-references" lists in the new central entries — and
   in particular the cross-links to the existing production glossary
   (`elohim-as-translation`, `el-shaddai`, `digir-sumerian-divine-lexeme-cross-corpus`,
   `yotzer-bereshit-...`).
7. **Verify the overlay v1.1.0 entries** against the manuscript-codicology
   apparatus where feasible (Sadeghi-Bergmann 2010; Sadeghi-Goudarzi 2010;
   Hilali 2017; Déroche 2009/2014; Corpus Coranicum).
8. **Confirm chapter-21.json, chapter-54.json, chapter-56.json pass
   structural validation** (16 paragraphs total; all glossaryRefs reference
   real entries; all commentary fields populated where divergence-from-PD-reading
   exists; all editorial_questions cleared).

After Reviewer sign-off, the three chapters advance from `editor-review` to
`reviewer-approved`, then to `published` after human sign-off. The
Reviewer pass should pay particular attention to the *inshiqāq al-qamar*
disavowal block at 54:1 (the corpus's most-load-bearing
Raëlian-canon-citation site) and the *ḥūr ʿīn* four-stratum disavowal at
56:22 (the corpus's most-discussed orientalist-stereotype lens-risk site).
