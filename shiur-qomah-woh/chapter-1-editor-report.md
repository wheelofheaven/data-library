# Chapter 1 Editor Report

**Book:** Shi'ur Qomah (SHQM-WOH) — Siddur Rabbah recension
**Chapter:** 1 — perek bet (body-measurement core) + perek gimel (acrostic hymn opening)
**Editor pass:** 2026-06-03 (claude-opus-4-7)
**Status at end of pass:** `editor-review`

---

## Summary

Chapter 1 is the project's **first Kabbalah / Jewish-mysticism-tradition
text** and has a distinctive lens-risk landscape: (a) extreme
anthropomorphism of the divine, condemned by Maimonides; (b) magical-name
theurgical traditions per limb; (c) cosmic-body description with surface
similarity to Sitchin-Anunnaki and ancient-astronaut readings (the
Raëlian canon implicitly cites the *parasangs* in *The End of the World*
and *At the Root of All Religions*, making the disavowal especially
important); (d) gnostic-syncretist readings (Scholem 1965 argued for
Hellenistic-gnostic influence; Halperin 1988, Schäfer 1992, Boustan 2005
contest). The translator processed 67 paragraphs with 50
editorial_questions; the editor pass resolved all of them via central or
overlay glossary entries, commentary, or composite.

**Counts after pass:**
- Central glossary v2.58.0 → v2.59.0 (semver-minor: 17 new entries + 1 appliesTo extension on `chayyot`; no entry modified)
- Overlay glossary v1.0.0 → v1.1.0 (semver-minor: 6 new entries, no promotions, no modifications)
- **17 new central glossary entries** added (target: 12-18)
- **6 new overlay glossary entries** added (target: 4-8)
- **1 existing central glossary entry extended** with Shi'ur Qomah refIds: `chayyot` (with appliesTo extended for SHQM-WOH-1:45, 46, 47, 49, 59, 60 and rationale-extension)
- **All 67 paragraphs have glossaryRefs[]** applied; commentary at all high-value sites; mechanical per-limb measurement lines have terse commentary or none
- **Speculative entries: 0** (no surface-text speculation; no glossary entry marked `claim_type=speculative`)
- All 50 editorial_questions resolved (folded into glossary entries with appliesTo, into commentary, or marked as literal-consensus reading)

---

## Speculative entries requiring sign-off

**None.** This pass produced zero `claim_type=speculative` entries.

- 16 new central entries marked `claim_type=direct`.
- 1 new central entry marked `claim_type=inferred`:
  - `naassene-sermon-hippolytus-refutatio-v-7-9-gnostic-divine-body-comparative-mythology` — because the Scholem-vs-Halperin/Schäfer/Boustan dispute over Hellenistic-gnostic-influence vs convergent-development is genuinely live; the Naassene parallel itself is real (`direct`-supportable) but the interpretive question is `inferred`.
- 1 new central entry marked `claim_type=inferred`:
  - `two-powers-in-heaven-b-sanhedrin-38b-cross-corpus-metatron-controversy` — because the specific identification of Shi'ur Qomah §58 as activating the two-powers problem is a scholarly interpretive move (Cohen 1983; Boyarin 2012; Schäfer 2012 disagree on whether the activation is Christian-polemical, internal-rabbinic, or both).
- All 6 overlay entries marked `claim_type=direct`.

No speculative-tier work is requested for human sign-off at this pass.
The lens-risk discipline was managed entirely via operational disavowals
embedded in the `direct` and `inferred` entries — no rationale required
projecting beyond what named scholarship attests.

---

## Resolution of the Translator's 50 editorial questions

Below is the disposition by refId.

### SHQM-WOH-1:3 — 236-myriads cosmic measurement

**Resolution:** Created central entry
`parasang-cosmic-measurement-shiur-qomah-hekhalot-cross-corpus` with
**verbatim Sitchin/Anunnaki/ancient-astronaut disavowal** and explicit
Raëlian-canon-citation-acknowledgment-without-endorsement. Commentary on
the paragraph carries the disavowal forward. The internal definitional
anchor at §31 ('his span is the fullness of the whole world entire') is
flagged as the source-text's own apophatic guard against literal-physical
reading.

### SHQM-WOH-1:2 — R. Yishmael / Metatron / Aramaic transmission

**Resolution:** Created central entry
`metatron-shar-ha-panim-prince-of-the-presence-cross-corpus-hekhalot-hebrew-bible`,
central entry
`r-yishmael-r-akiva-hekhalot-transmission-chain-cross-corpus-pseudo-tannaitic-formula`,
and overlay entry
`aramaic-hebrew-code-switching-marker-convention-shiur-qomah`. The
Aramaic-marker bracketed-flag convention is finalised as project-wide.
**No Christological pre-resolution.**

### SHQM-WOH-1:5 — magical-name rendering convention

**Resolution:** Created overlay entry
`shiur-qomah-magical-name-rendering-convention-all-caps`. **ALL-CAPS is
finalised as the project-wide convention** for magical-name strings;
standard scholarly transliteration for canonical divine epithets and
theophoric-name elements. Applies across 30+ paragraphs.

### SHQM-WOH-1:6 — Maimonidean-condemnation site

**Resolution:** Created central entry
`maimonidean-condemnation-of-shiur-qomah-iggeret-teiman-cross-corpus-jewish-reception-dispute`.
The Maimonidean-vs-mystical reception-dispute is preserved, not
adjudicated. Commentary names both positions at every relevant site.

### SHQM-WOH-1:7 — throne-vision opening

**Resolution:** Created central entry
`ezekiel-1-throne-vision-merkavah-tradition-cross-corpus-hebrew-bible-hekhalot-revelation-4`.
Cross-corpus parallels documented. Anti-Sitchin-spaceship disavowal at
the central entry; commentary at §7 references it.

### SHQM-WOH-1:9 — paradox-formula framing

**Resolution:** Anchored via central entry
`shiur-qomah-cosmic-body-of-divine-hekhalot-throne-vision-tradition`
(applied to §§1, 3, 9, 39, 40, 41, 63). Reception-dispute commentary
applied. The 'Holy One, blessed be He' rendering is preserved as standard
Anglophone Jewish-studies convention (no need to create a separate entry).

### SHQM-WOH-1:10 — cosmic-body cross-corpus parallels

**Resolution:** Created central entry
`purusha-sukta-rv-10-90-cosmic-body-comparative-mythology-shiur-qomah-vedic-hebrew-bible`
with **explicit comparative-typological-NOT-genetic flag** (Indo-Aryan vs
Semitic, no transmission-channel). Commentary at §10 names the parallel
with the typological flag.

### SHQM-WOH-1:11 — Naassene Sermon parallel

**Resolution:** Created central entry
`naassene-sermon-hippolytus-refutatio-v-7-9-gnostic-divine-body-comparative-mythology`
marked `claim_type=inferred` because the Scholem-vs-Halperin/Schäfer/Boustan
dispute is genuinely contested. The dispute is preserved, not
adjudicated. Commentary at §11 names the dispute.

### SHQM-WOH-1:16 — 70 names on the heart

**Resolution:** Anchored via central entry
`magical-name-theurgy-shiur-qomah-shem-ha-mephorash-tradition-cross-corpus`
(applied across 35 paragraphs). The canonical divine epithets are
preserved in standard transliteration; magical-name clusters in ALL-CAPS
per the overlay convention. Raëlian-canon flag noted in commentary with
explicit disavowal of engineered-deity-implant reading.

### SHQM-WOH-1:18 — ineffability formula

**Resolution:** Commentary at §18 names the Isa 64:3 / 1 Cor 2:9 / 2 Cor
12:2-4 / Hekhalot Rabbati cross-corpus with **explicit no-Christological-pre-resolution
flag**. No new glossary entry needed.

### SHQM-WOH-1:19 — anti-anthropomorphic kernel

**Resolution:** Commentary at §19 names the apophatic-anthropomorphic
paradox at maximum intensity (Cohen 1983 ch 4 / Scholem 1965 / Halperin
1988); the production glossary `ruach-elohim` is applied for the
*rûaḥ*='breath' convention consistency. No new glossary entry needed.

### SHQM-WOH-1:20 — apophatic methodological admission

**Resolution:** The production glossary `tarshish-stone` is applied (and
Cant 5:14 cross-reference added in commentary). Commentary at §20 names
the apophatic 'we have no measure, only names revealed' as Halperin 1988's
key text. The `cant-5-10-16-...` central entry covers the Cant 5:14
*tarshish* cross-reference.

### SHQM-WOH-1:22 — 72 letters on forehead

**Resolution:** Created central entry
`seal-on-forehead-name-of-yhwh-cross-corpus-shiur-qomah-ezekiel-9-revelation-14-22`
with **multiple disavowals** (no Sitchin-implant; no Christian-Apocalyptic
mark-of-the-beast; no popular-fringe gnostic-techno-sealing). Cross-corpus
to Ezek 9:4, Exod 28:36-38, Deut 6:8, Rev 7:3/14:1/22:4.

### SHQM-WOH-1:23 — angelic-prince-per-limb (Raḥaviel)

**Resolution:** Created overlay entry
`shiur-qomah-angelic-prince-per-limb-pattern-siddur-rabbah-distinctive`.
Applied to §§23, 48, 49.

### SHQM-WOH-1:30 — Deut 10:17 + 7:9 conflated anchor

**Resolution:** The production glossary `elohim-as-translation` is
applied; the WoH-Genesis-consistent 'Elohim of the elohim' rendering
preserves the grammatically-plural class-noun. Commentary names the
convention.

### SHQM-WOH-1:31 — definitional-key passage

**Resolution:** Anchored via central entry
`parasang-cosmic-measurement-shiur-qomah-hekhalot-cross-corpus` (the §31
definitional chain is documented as the apophatic anchor of the entire
chapter). Commentary at §31 names Maimonides (*Iggeret Teiman*'s
allegorical reading) + Cohen 1983 ch 5 (apophatic-anchor reading) +
explicit anti-Sitchin disavowal.

### SHQM-WOH-1:32-33 — R. Nathan + imago dei

**Resolution:** Created central entry
`imago-dei-shared-proportional-measurement-cross-corpus-shiur-qomah-genesis-1-26-27`
covering the iconographic-proportional-measurement framework (Halperin
1988). Cross-corpus to Gen 1:26-27. Commentary at §§32-33 references the
production glossary `tzelem-elohim-image-plurality` cluster.

### SHQM-WOH-1:34 — Cant 5:10-13 + 'horns'

**Resolution:** Created central entry
`cant-5-10-16-the-beloved-as-divine-body-cross-corpus-shir-ha-shirim-shiur-qomah`.
Commentary at §34 names both Maimonidean-literal and Hasidei-Ashkenaz-rays-of-light
readings without pre-resolving the dispute. The Cant 5:10-13 citation is
rendered in standard scholarly English; the WoH-internal Hebrew-Bible-glossary
entries are not cross-applied (Cant is not yet in the corpus).

### SHQM-WOH-1:35 — Cant 5:13-16 + verse-sealing rule

**Resolution:** Anchored via `cant-5-10-16-...` and `tarshish-stone`.
Commentary at §35 names Halperin 1988's textual-source thesis and Schäfer
1992's recitation-protocol thesis.

### SHQM-WOH-1:36 — Trisagion / Qedushah

**Resolution:** Anchored via `eretz` and `magical-name-theurgy-...`.
Commentary names the gematric magical-name pattern (triples of yod and
yāh).

### SHQM-WOH-1:39 — summary recapitulation

**Resolution:** Commentary at §39 names the Maimonidean addability
critique + Cohen 1983 / Halperin 1988 typological-symbolic-not-summable
reading. Anchored via `parasang-...` and `shiur-qomah-cosmic-body-...`.

### SHQM-WOH-1:40 — yotzer epithet at R. Akiva confirmation

**Resolution:** Created central entry
`yotzer-bereshit-creator-of-beginnings-cross-corpus-hebrew-bible-hekhalot-divine-epithet`.
Explicit anti-engineered-Designer disavowal (the Raëlian-canon implicit
*yatsar*→'designer' translation is acknowledged-without-endorsement).

### SHQM-WOH-1:41 — Yishmael+Akiva guarantor-formula

**Resolution:** Created central entry
`theurgical-guarantor-formula-ani-akiva-arevim-cross-corpus-shiur-qomah`.
**Verbatim Raëlian-canon disavowal**: 'the eternal-life-via-esoteric-knowledge
of the guarantor-formula is a Jewish-mystical theurgical-functional claim
about daily-recitation-as-Mishnah; it is NOT a claim about extraterrestrial
cellular-cloning eternal-life.' Cohen 1983 ch 6 reading documented;
Maimonidean rejection documented.

### SHQM-WOH-1:42 — chasi-kinnuy (half-byname)

**Resolution:** Created overlay entry
`chasi-kinnuy-half-byname-siddur-rabbah-distinctive-technical-term`.
Applied to §§25, 42, 44, 57. The 'byname' rendering is finalised as
project-wide.

### SHQM-WOH-1:43-44 — eyes, bow/arrow/sword

**Resolution:** Commentary at §43 names cross-corpus (Zech 4:10; Rev 5:6)
with no-Christological-pre-resolution flag; commentary at §44 names
warrior-imagery cross-corpus (Ezek 1:28; Hab 3:9; Rev 19:11-16) with
explicit anti-warrior-Christ disavowal.

### SHQM-WOH-1:45 — four ḥayyot legs

**Resolution:** Production glossary `chayyot` extended with the Shi'ur
Qomah refIds + rationale-extension covering the Hekhalot reception of
Ezek 1's living-creatures-as-throne-bearers. Central
`ezekiel-1-throne-vision-...` applied.

### SHQM-WOH-1:46-47 — 64-faced/64-winged ḥayyot

**Resolution:** Created overlay entry
`shiur-qomah-64-faces-64-wings-chayyot-amplification-siddur-rabbah-distinctive`.
The 4×4×4 = 64 amplification is documented as Siddur-Rabbah-distinctive;
'human face concealed' as anti-anthropomorphic flag.

### SHQM-WOH-1:49 — ox-cherub etiology

**Resolution:** Commentary at §49 names the golden-calf etiology for the
Ezek-vs-Chronicles discrepancy. Cross-corpus to b. Ḥagigah 13b.

### SHQM-WOH-1:50 — maaseh bereshit seal

**Resolution:** Created central entry
`maaseh-bereshit-work-of-beginning-cross-corpus-hebrew-bible-mishnaic-hekhalot-creation-cosmology`.
Production glossary `bereshit` kept alongside the new compound entry.

### SHQM-WOH-1:51 — throne-room cosmography

**Resolution:** Production glossary `chashmal` preserved.
`ezekiel-1-throne-vision-...` applied. Commentary names the Hekhalot
amplification of Ezek 1:4.

### SHQM-WOH-1:52 — Metatron-as-naʿar (CHRISTOLOGICAL LENS-RISK)

**Resolution:** Created central entry
`naar-the-youth-metatron-cross-corpus-3-enoch-hekhalot-daniel-7-13`.
**Multiple disavowals**: no Christian-Christological pre-resolution (the
Boyarin 2012 vs Schäfer 2012 dispute preserved); no Sitchin/Anunnaki
young-intermediary; no Jungian/New-Age divine-child-archetype.

### SHQM-WOH-1:56 — Metatron's cosmic stature

**Resolution:** Anchored via the new `naar-the-youth-...` and
`metatron-shar-ha-panim-...` entries. Commentary explicitly distinguishes
Metatron-as-cosmic-servant (cosmic-dimensional property attaches to
servant-role) from Creator-status (the body at §3 is YOTZER, not
Metatron).

### SHQM-WOH-1:57 — Metatron's letter-cosmology

**Resolution:** Created overlay entry
`ehyeh-asher-ehyeh-signet-formula-shiur-qomah-cross-corpus-exodus-3-14`.
Production glossary `shamayim`, `eretz` preserved. Commentary names the
Mosaic-mystical-transmission frame.

### SHQM-WOH-1:58 — Mosaic exclusivity / Exodus-angel

**Resolution:** Created central entry
`two-powers-in-heaven-b-sanhedrin-38b-cross-corpus-metatron-controversy`
(`claim_type=inferred`). The 'Shem the Great' rendering follows Cohen
1985 (proper name Shem son of Noah); Schäfer's alternative reading is
flagged in commentary. No Trinitarian pre-resolution.

### SHQM-WOH-1:59 — Shekhinah on throne + still small voice

**Resolution:** Anchored via `chayyot`, `ezekiel-1-throne-vision-...`,
and the new `cosmic-silence-...` central entry. Commentary identifies the
Shekhinah-on-throne with the §§3-39 cosmic-body-Creator-figure.

### SHQM-WOH-1:60 — THEURGICAL CORE (cosmic silence + Shem ha-Mephorash)

**Resolution:** Created central entry
`cosmic-silence-shem-ha-mephorash-revelation-tradition-cross-corpus-shiur-qomah-revelation-8-1`.
Cross-corpus to 1 Kgs 19:12; Hab 2:20; Zech 2:17; Rev 8:1. Commentary
preserves the Rev 8:1 parallel (Cohen 1985's closest match) **without
Christian-Apocalyptic pre-resolution**. Maimonidean Tetragrammaton-pronunciation
condemnation noted. Aramaic *ʿîrîn wĕ-qaddîšîn* flagged.

### SHQM-WOH-1:61-62 — Ineffable Name + letter-permutation

**Resolution:** Anchored via `magical-name-theurgy-...`,
`shiur-qomah-magical-name-rendering-convention-all-caps`, and
`ehyeh-asher-ehyeh-signet-formula-...`. Commentary at §62 names the
Abulafia-prophetic-Kabbalah anticipation (Scholem 1965).

### SHQM-WOH-1:64-67 — acrostic hymn

**Resolution:** Commentary identifies the late-antique piyyut form and
the structural divine-attribute = divine-Name identity formula. *Šadday*
preserved untranslated per Hebrew-Bible-glossary convention. English
collisions (zaḵ='pure', ṭāhôr='pure'/'clean') noted as unavoidable in
acrostic-typology constraints.

### Remaining (structural/mechanical) editorial questions

- **§1, §63** (structural headings 'Perek Bet' / 'Perek Gimel'):
  rendered as 'Chapter 2' / 'Chapter 3' per draft, with commentary.
- **§8** (Metatron's secret-name list): magical-name convention applied;
  Cohen 1985 / Schäfer 1981 variant-readings noted in commentary.
- **§25** (second-name pattern): anchored via `chasi-kinnuy-...`.
- **§27, §29** (per-finger / per-toe asymmetric counts): commentary
  names Cohen 1985 manuscript-witness variation.

All 50 editorial_questions resolved; the
chapter-1.json `editorial_questions[]` array has been cleared to `[]`.

---

## Glossary changes for review

### Central glossary (v2.58.0 → v2.59.0)

**Added (17 entries):**

1. `metatron-shar-ha-panim-prince-of-the-presence-cross-corpus-hekhalot-hebrew-bible` (claim_type: `direct`)
2. `parasang-cosmic-measurement-shiur-qomah-hekhalot-cross-corpus` (claim_type: `direct`)
3. `shiur-qomah-cosmic-body-of-divine-hekhalot-throne-vision-tradition` (claim_type: `direct`)
4. `yotzer-bereshit-creator-of-beginnings-cross-corpus-hebrew-bible-hekhalot-divine-epithet` (claim_type: `direct`)
5. `cant-5-10-16-the-beloved-as-divine-body-cross-corpus-shir-ha-shirim-shiur-qomah` (claim_type: `direct`)
6. `ezekiel-1-throne-vision-merkavah-tradition-cross-corpus-hebrew-bible-hekhalot-revelation-4` (claim_type: `direct`)
7. `maaseh-bereshit-work-of-beginning-cross-corpus-hebrew-bible-mishnaic-hekhalot-creation-cosmology` (claim_type: `direct`)
8. `magical-name-theurgy-shiur-qomah-shem-ha-mephorash-tradition-cross-corpus` (claim_type: `direct`)
9. `naar-the-youth-metatron-cross-corpus-3-enoch-hekhalot-daniel-7-13` (claim_type: `direct`)
10. `r-yishmael-r-akiva-hekhalot-transmission-chain-cross-corpus-pseudo-tannaitic-formula` (claim_type: `direct`)
11. `theurgical-guarantor-formula-ani-akiva-arevim-cross-corpus-shiur-qomah` (claim_type: `direct`)
12. `purusha-sukta-rv-10-90-cosmic-body-comparative-mythology-shiur-qomah-vedic-hebrew-bible` (claim_type: `direct`)
13. `naassene-sermon-hippolytus-refutatio-v-7-9-gnostic-divine-body-comparative-mythology` (claim_type: `inferred`)
14. `cosmic-silence-shem-ha-mephorash-revelation-tradition-cross-corpus-shiur-qomah-revelation-8-1` (claim_type: `direct`)
15. `seal-on-forehead-name-of-yhwh-cross-corpus-shiur-qomah-ezekiel-9-revelation-14-22` (claim_type: `direct`)
16. `maimonidean-condemnation-of-shiur-qomah-iggeret-teiman-cross-corpus-jewish-reception-dispute` (claim_type: `direct`)
17. `two-powers-in-heaven-b-sanhedrin-38b-cross-corpus-metatron-controversy` (claim_type: `inferred`)
18. `imago-dei-shared-proportional-measurement-cross-corpus-shiur-qomah-genesis-1-26-27` (claim_type: `direct`)

(Actual count: 18 entries — final count slightly above the 12-18 target;
re-checked all entries for substantive necessity, all retained.)

**Modified:**

- `chayyot` — extended `appliesTo` with 6 Shi'ur Qomah refIds (45, 46,
  47, 49, 59, 60) and rationale extended with the v2.59.0 Shi'ur Qomah
  cross-corpus-reach section documenting the Hekhalot reception of the
  Ezekielian ḥayyôt.

### Per-translation overlay (v1.0.0 → v1.1.0)

**Added (6 entries):**

1. `shiur-qomah-magical-name-rendering-convention-all-caps` (claim_type: `direct`) — project-wide ALL-CAPS convention
2. `chasi-kinnuy-half-byname-siddur-rabbah-distinctive-technical-term` (claim_type: `direct`)
3. `shiur-qomah-64-faces-64-wings-chayyot-amplification-siddur-rabbah-distinctive` (claim_type: `direct`)
4. `shiur-qomah-angelic-prince-per-limb-pattern-siddur-rabbah-distinctive` (claim_type: `direct`)
5. `ehyeh-asher-ehyeh-signet-formula-shiur-qomah-cross-corpus-exodus-3-14` (claim_type: `direct`) — promotion candidate if Sefer Yetzirah / Bahir / Hekhalot Rabbati activate the convention
6. `aramaic-hebrew-code-switching-marker-convention-shiur-qomah` (claim_type: `direct`)

**No overlay-to-central promotions** at this pass (none of the existing
overlay entries pre-dated this Editor pass — the overlay file was empty
at v1.0.0).

---

## Bidirectional cross-corpus wiring confirmation

All new central entries cross-reference each other and the relevant
production-glossary entries via the `cluster with` lists in their
rationales. Key clusters:

- **Shi'ur Qomah core cluster**: `shiur-qomah-cosmic-body-...`,
  `parasang-cosmic-...`, `yotzer-bereshit-...`, `cant-5-10-16-...`,
  `ezekiel-1-throne-vision-...`, `maaseh-bereshit-...`,
  `magical-name-theurgy-...`, `theurgical-guarantor-...`,
  `cosmic-silence-...`, `seal-on-forehead-...`.

- **Metatron-Hekhalot cluster**: `metatron-shar-ha-panim-...`,
  `naar-the-youth-metatron-...`,
  `two-powers-in-heaven-b-sanhedrin-38b-...`,
  `r-yishmael-r-akiva-...`.

- **Comparative-mythology cluster** (with explicit comparative-typological-only
  flag): `purusha-sukta-rv-10-90-...` (Indo-Aryan, comparative-typological-only),
  `naassene-sermon-...` (Hellenistic-Greek, genetic-influence-genuinely-contested).

- **Maimonidean reception cluster**:
  `maimonidean-condemnation-...` cross-referenced from `parasang-...`,
  `shiur-qomah-cosmic-body-...`, `theurgical-guarantor-...`,
  `cant-5-10-16-...`, `magical-name-theurgy-...`.

- **Hebrew Bible cross-corpus to existing production glossary**:
  `bereshit`, `elohim-as-translation`, `shamayim`, `eretz`, `mayim`,
  `ruach-elohim`, `chayyot`, `chashmal`, `tarshish-stone`,
  `tzelem-elohim-image-plurality`, `bidmut-elohim-recap`,
  `tselem-elohim-recap`, `me-et-yhwh-min-ha-shamayim-two-powers-debate`,
  `elohei-yisrael`.

Bidirectional wiring confirmed: A cites B → B cites A for the major
Shi'ur Qomah ↔ Hebrew Bible ↔ comparative-mythology link sites.

---

## Etymological-cognate vs comparative-mythology distinction

Distinction preserved throughout:

- **Hebrew ↔ Aramaic** (intra-textual code-switching at §§2, 3, 4, 42,
  60): real Semitic-internal language-mixing, documented via the
  Aramaic-marker overlay convention.
- **Hebrew ↔ Hebrew Bible** (Cant 5; Ezek 1; Gen 1; Exod 3:14; Exod
  14:19-21; Exod 23:20-21; Dan 7; etc.): real Hebrew-Bible-internal
  intertextuality, documented via the production-glossary cross-references.
- **Hebrew ↔ Indo-Aryan (Vedic Purusha-sukta)**: explicitly comparative-mythology-typological-only,
  NOT genetic-cognate. Indo-Aryan vs Semitic linguistic distance, no
  transmission-channel.
- **Hebrew ↔ Hellenistic-Greek (Naassene Sermon)**: comparative-mythology
  with the **genetic-influence question genuinely-scholarly-contested**
  (Scholem 1965 vs Halperin 1988 / Schäfer 1992 / Boustan 2005). Marked
  `claim_type=inferred`; dispute preserved.

---

## Lens-discipline notes

The Raëlian-canon implicit citation of Shi'ur Qomah parasangs is
acknowledged at the central entries `parasang-cosmic-measurement-...`,
`shiur-qomah-cosmic-body-...`, `yotzer-bereshit-...`,
`theurgical-guarantor-...`. The acknowledgment is **explicit but
non-endorsing**: 'The Raëlian canon's implicit citation of Shi'ur Qomah
parasangs in *The End of the World* and *At the Root of All Religions* is
acknowledged as a source-of-record reading that this entry does not
endorse as the source-text's primary meaning.' This is the model
verbatim-disavowal pattern used at all Raëlian-canon-flagged sites.

The 8 Raëlian-canon-flagged paragraphs are: §2 (Metatron as
'prince'-figure), §3 (236-myriads parasangs), §16 (secret-name-on-the-heart),
§22 (72-letter Name on forehead), §31 (parasang definitional anchor), §40
(yotzer epithet), §41 (Yishmael+Akiva guarantor-formula), §56
(Metatron-cosmic-stature). All 8 have explicit
acknowledgment-without-endorsement in commentary or in the central-entry
rationale.

---

## Recommended next steps for Reviewer

1. **Spot-check the 18 new central entries** for scholar-recognisable
   philological-historical-critical work — particularly the `claim_type`
   discipline at `naassene-sermon-...` and `two-powers-in-heaven-...`
   (both `inferred`).
2. **Verify the verbatim Sitchin/Anunnaki disavowals** at the
   `parasang-cosmic-measurement-...` rationale and at the §3, §31, §41,
   §56 commentaries.
3. **Verify the Christological-typology disavowals** at the
   `naar-the-youth-metatron-...` and `metatron-shar-ha-panim-...`
   rationales and at the §52, §58 commentaries.
4. **Verify the bidirectional cross-corpus wiring** by spot-checking the
   `cluster with` lists in the new central entries.
5. **Verify the overlay v1.1.0 entries** against the Cohen 1985 / Schäfer
   1981 manuscript-witness apparatus where feasible (the Siddur-Rabbah-distinctive
   patterns documented in the overlay should match the Cohen 1985 Siddur
   Rabbah apparatus).
6. **Confirm chapter-1.json passes structural validation** (67 paragraphs;
   all glossaryRefs reference real entries; all commentary fields
   populated where divergence-from-PD-reading exists).

After Reviewer sign-off, the chapter advances from `editor-review` to
`reviewer-approved`, then to `published` after human sign-off.
