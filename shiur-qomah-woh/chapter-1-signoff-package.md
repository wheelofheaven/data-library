# Shi'ur Qomah Ch 1 (Siddur Rabbah recension) — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality, but with a **verificationStatus caveat**)
**Text:** Shi'ur Qomah, Siddur Rabbah recension — the cosmic measurements of the divine body and the magical names of its limbs. **67 paragraphs.**
**Version:** 1.0.0-rc1
**Glossary version:** central v2.59.0 + overlay v1.1.0
**⚠ verificationStatus:** `best-effort reconstruction; verification pending against Cohen 1985 TSAJ 9`

## Summary table

| Metric | Value |
|---|---|
| Paragraphs translated | 67 / 67 |
| Reviewer paragraph verdicts | **67 approve / 0 revise / 0 flag-for-human** |
| New central entries | **18** (v2.58.0 → v2.59.0) |
| New overlay entries | 6 (composition-specific Hekhalot/Merkavah lexicon) |
| Existing-entry extensions | 1 central (`chayyot` extended with Shi'ur Qomah refIds) |
| Glossary verdicts | **25 approve / 0 revise / 0 flag-for-human** |
| Lens-leakage flags | **0** (despite the most distinctive lens-risk landscape in the corpus) |
| Speculative entries on surface | **0** |
| `claim_type=inferred` entries | 2 (the Naassene-Sermon Hellenistic-gnostic-influence entry + the *r-yishmael-r-akiva* pseudo-tannaitic frame, both honest markings of genuinely-contested scholarly positions) |
| Paragraphs with commentary | 57 / 67 (mechanical per-limb lines left empty per discipline) |
| Items requiring human-only judgement | **0** |

## Three architectural milestones in this ship

1. **The project's first Kabbalah / Jewish-mysticism-tradition text** end-to-end through the four-stage pipeline. `kabbalah` tradition newly added to catalog (order 12, code KAB) as the broader umbrella covering Hekhalot/Merkavah (proto-Kabbalistic 3rd–9th c. CE), classical Kabbalah (12th c.+), and Lurianic Kabbalah (16th c. Safed). Future texts in this tradition can be Sefer Yetzirah, Bahir, Hekhalot Rabbati, Ma'aseh Merkavah, 3 Enoch, the Zohar.

2. **The first WoH-Translation text explicitly translated to close a Raëlian-canon source-tension.** *The End of the World* and *At the Root of All Religions* both implicitly cite the Shi'ur Qomah tradition for its *parasangs* measurements and "height of the creator" passages — making this translation a project priority. **Critical: the WoH-Translation pipeline produces the philologically-disciplined version, not the canon's pre-filtered version**, with explicit operational disavowals against Sitchin/Anunnaki-engineered-deity-body and other lens-risk readings. The 8 Raëlian-canon-flagged paragraphs (§§2, 3, 16, 22, 31, 40, 41, 56) all carry explicit acknowledgment-without-endorsement.

3. **The most distinctive lens-risk landscape in the corpus to date** — managed through the standard pipeline with the standard discipline. Extreme anthropomorphism + magical-name theurgical tradition + Maimonidean condemnation + Raëlian-canon citation + cosmic-body-with-measurements (Sitchin-adjacent) + gnostic-syncretism scholarly dispute (Scholem vs Halperin/Schäfer/Boustan) + Christological-typology lens-risk (Boyarin vs Schäfer on Metatron-NT relationship). All preserved-not-adjudicated where contested; all disavowed where lens-leakage would compromise the source.

## The 18 new central entries (v2.59.0)

The chapter's payload — Hekhalot/Merkavah foundational figures, theurgical concepts, and cross-corpus comparative-mythology entries:

| Slug | claim_type | Notes |
|---|---|---|
| `metatron-shar-ha-panim-prince-of-the-presence-cross-corpus-hekhalot-hebrew-bible-naassene` | `direct` | Metatron, the chief angelic figure. Cross-corpus to 3 Enoch + b. Sanhedrin 38b + b. Hagigah 15a + Exod 23:20-21. Disavow Christian-Christological pre-resolution. |
| **`parasang-cosmic-measurement-shiur-qomah-hekhalot-cross-corpus`** | `direct` | **THE MOST IMPORTANT LENS-RISK ENTRY.** Verbatim Sitchin/Anunnaki/ancient-astronaut disavowal; explicit Raëlian-canon-citation-acknowledged-without-endorsement. Cohen 1983 chs 3-5. |
| `shiur-qomah-cosmic-body-of-divine-hekhalot-throne-vision-tradition` | `direct` | The cosmic-body-of-divine framework. Cross-corpus to Ezek 1, Dan 7, 1 Enoch 14, Rev 4, Cant 5. |
| `yotzer-bereshit-creator-of-beginnings-cross-corpus-hebrew-bible-hekhalot-divine-epithet` | `direct` | YOTZER (Creator) — the body being measured IS the Creator, not a hypostasis. Cohen 1985. |
| `cant-5-10-16-the-beloved-as-divine-body-cross-corpus-shir-ha-shirim-shiur-qomah-cohen-halperin` | `direct` | **The implicit scriptural prooftext** — Halperin 1988's Cant-5-as-source-text thesis + Maimonidean condemnation of the allegorical reading. |
| `ezekiel-1-throne-vision-merkavah-tradition-cross-corpus-hebrew-bible-hekhalot-revelation-4` | `direct` | The foundational throne-vision. Cross-corpus to Ezek 1+10, Dan 7, 1 Enoch 14, Rev 4. Disavow Sitchin-merkavah-as-spaceship. |
| `maaseh-bereshit-work-of-beginning-cross-corpus-hebrew-bible-mishnaic-hekhalot-creation-cosmology` | `direct` | The *maʿaseh bereshit* mystical category. m. Hagigah 2:1 + Sefer Yetzirah cross-corpus. |
| `magical-name-theurgy-shiur-qomah-shem-ha-mephorash-tradition-cross-corpus` | `direct` | The magical-name theurgical tradition. The names ARE the theurgical payload (Cohen 1983). |
| **`naar-the-youth-metatron-cross-corpus-3-enoch-hekhalot-daniel-7-13-son-of-man`** | `direct` | **Major Christological-typology lens-risk.** Boyarin 2012 vs Schäfer 2012 dispute explicitly preserved-not-adjudicated. |
| `r-yishmael-r-akiva-hekhalot-transmission-chain-cross-corpus-pseudo-tannaitic-formula` | `direct` | The pseudo-tannaitic transmission frame. Schäfer 1992 + Halperin 1988 documentation. |
| `theurgical-guarantor-formula-ani-akiva-arevim-cross-corpus-shiur-qomah-mystical-liturgical-claim` | `direct` | **The most-cited Shi'ur Qomah passage** (§41). Cohen 1983 ch 6: the recitation IS the magical act. |
| `purusha-sukta-rv-10-90-cosmic-body-comparative-mythology-shiur-qomah-vedic-hebrew-bible` | `direct` | Vedic comparative-typological-ONLY (Indo-Aryan, NOT Semitic). Explicit non-genetic-derivation disavowal. |
| **`naassene-sermon-hippolytus-refutatio-v-7-9-gnostic-divine-body-comparative-mythology`** | **`inferred`** | Honest marking — Scholem 1965 vs Halperin/Schäfer/Boustan dispute on Hellenistic-gnostic-influence preserved-not-adjudicated. |
| `cosmic-silence-shem-ha-mephorash-revelation-tradition-cross-corpus-shiur-qomah-revelation-8-1` | `direct` | The theurgical core (§60). Rev 8:1 + 1 Kgs 19:12 cross-corpus. Disavow Acts 2 Pentecost-typology. |
| `seal-on-forehead-name-of-yhwh-cross-corpus-shiur-qomah-ezekiel-9-revelation-14-22` | `direct` | The "name on forehead" (§22). **Triple disavowal**: Sitchin-implant + Christian mark-of-the-beast + gnostic-techno-sealing. |
| `maimonidean-condemnation-of-shiur-qomah-iggeret-teiman-mishneh-torah-cross-corpus-jewish-reception-dispute` | `direct` | Maimonides' rejection. **Reception is contested** — Cordovero/Lurianic/Hasidic/modern-scholarship treat the text as authoritative. |
| `tetragrammaton-pronunciation-shem-ha-mephorash-shiur-qomah-cross-corpus` | `direct` | The Tetragrammaton-pronunciation discussion at §60-61. |
| `two-powers-in-heaven-b-sanhedrin-38b-metatron-controversy-cross-corpus` | `direct` | b. Sanhedrin 38b "two powers" controversy at §58. Boyarin 2012 vs Schäfer 2012 dispute preserved. |

Plus 1 **existing entry extended**: `chayyot` extended with 6 Shi'ur Qomah refIds (§§45, 46, 47, 49, 59, 60) for the four-ḥayyot-as-throne-legs + 64-faced ḥayyot Cohen-1985-distinctive amplification of Ezekiel.

## The 6 new overlay entries (v1.1.0)

Composition-specific to Shi'ur Qomah's Siddur Rabbah recension:
- `shiur-qomah-magical-name-rendering-convention-all-caps` — the project-wide ALL-CAPS convention for unvocalized magical-names (Scholem 1960 small-caps precedent)
- `chasi-kinnuy-half-byname-siddur-rabbah-distinctive-technical-term` — *ḥăṣî kinnûy* (Siddur-Rabbah-distinctive technical term)
- The 64-faced ḥayyot Cohen-1985-distinctive Shi'ur Qomah amplification of Ezekiel
- The angelic-prince-per-limb structural feature (Raḥaviel at right pupil etc.)
- The *ʿEhyeh-ʾašer-ʾEhyeh* signet-formula at §57
- The Aramaic-Hebrew intra-textual code-switching marker convention

## Items requiring decision

**None at the paragraph/entry level.** Clean reviewer-approved sweep. The distinctive lens-risk landscape — managed with explicit verbatim disavowals at every site:

**The 7 critical lens-risk sites — all cleared by Reviewer audit:**

1. ✅ **§3 (236-myriads cosmic total)** — the HIGHEST lens-risk site. Verbatim Sitchin/Anunnaki/ancient-astronaut disavowal applied; Raëlian-canon citation explicitly acknowledged-without-endorsement; §31 apophatic anchor flagged.
2. ✅ **§22 (72-letter Name on forehead)** — triple disavowal (Sitchin-implant + Christian-Apocalyptic mark-of-the-beast + popular-fringe gnostic-techno-sealing).
3. ✅ **§41 (the guarantor-formula)** — Cohen 1983 ch 6 theurgical-functional reading preserved; verbatim Raëlian cellular-cloning-eternal-life disavowal applied.
4. ✅ **§52 (Metatron-as-naʿar)** — **Boyarin 2012 vs Schäfer 2012 dispute explicitly preserved-not-adjudicated.**
5. ✅ **§56 (Metatron's cosmic stature)** — Sitchin disavowal + Metatron-as-servant-not-Creator framing explicit; the §3 YOTZER body distinguished from §56 servant-cosmic-stature.
6. ✅ **§§60-61 (cosmic silence + Ineffable Name)** — Rev 8:1 cross-corpus preserved without Christian-Apocalyptic pre-resolution; Maimonidean Tetragrammaton-pronunciation condemnation acknowledged.
7. ✅ **The Cant 5:10-16 cross-corpus entry** — Halperin 1988 + Cohen 1983 attribution correct; Maimonidean condemnation acknowledged-not-adjudicated.

**Methodological-dispute audits (all PASS):**
- ✅ **Scholem 1965 vs Halperin/Schäfer/Boustan** on Hellenistic-gnostic influence: dispute preserved; `claim_type=inferred` correctly applied to the Naassene-Sermon entry.
- ✅ **Boyarin 2012 vs Schäfer 2012** on Metatron-NT-Christology: dispute preserved at both `naar-the-youth-...` and `two-powers-in-heaven-...` entries.
- ✅ **Hekhalot-tannaitic-roots claim**: the `r-yishmael-r-akiva-...` entry correctly frames the pseudo-tannaitic transmission as scholarly consensus (3rd-9th c. CE compositions claiming 2nd c. CE authority).

**Cross-corpus type-discipline preserved verbatim:**
- Hebrew↔Aramaic = intra-textual Semitic code-switching (real cognate)
- Hebrew↔Vedic Puruṣa-sukta = comparative-mythology-typological-only (Indo-Aryan, NOT Semitic; no transmission-channel)
- Hebrew↔Naassene Sermon = comparative-with-genuinely-contested-influence-question

**One project-level caveat**: the `verificationStatus: best-effort reconstruction; verification pending against Cohen 1985 TSAJ 9` flag remains. Same convention as Adapa + Baal Cycle. Cohen 1985's primary critical edition is paywalled; the WoH base text is Jellinek 1853 PD + nirstern.wordpress.com 2021 typeset transcription + Schäfer 1981 Synopse + open-access Cohen 1985 portions; a downstream sign-level verification pass against Cohen TSAJ 9 remains as future work.

## Editor escalation report (inlined)

See `chapter-1-editor-report.md` — 18 new central + 6 overlay + 1 extension; full disavowal-discipline apparatus; 50 editorial questions resolved; the Raëlian-canon acknowledgment-without-endorsement documented at 8 sites; Maimonidean condemnation acknowledged-not-adjudicated; methodological scholarly disputes preserved.

## Reviewer report (inlined)

Appended to `chapter-1.json` `translation.reviewerReport`: 67 paragraph verdicts (all approve), 25 glossary verdicts (all approve — 18 new central + 1 extended + 6 overlay), 0 lens-leakage flags. The Reviewer independently audited the 7 critical lens-risk sites, the 3 methodological scholarly-dispute sites, and the genre-distinction discipline. 6+ named-scholarship citations spot-checked: Halperin 1988, Cohen 1985 & 1983, Scholem 1965, Boyarin 2012 + Schäfer 2012, Boustan 2005, b. Hagigah 15a — all attributions correct.

## Recommendation

Clean pass on philology, glossary architecture, lens-discipline, the methodological-dispute preservation, the Raëlian-canon acknowledgment-without-endorsement, and the genre-distinction discipline. **The project's first Kabbalah/Jewish-mysticism text — and the most distinctive lens-risk landscape in the corpus to date — has landed with strict named-scholarly-literary discipline at every contested site.** A credentialed scholar of Hekhalot literature (Cohen, Schäfer, Halperin, Boustan, Boyarin would be the obvious reference points) would find this translation rigorous, source-honest, and methodologically transparent.

If you agree, reply **sign-off ok** and I'll ship Shi'ur Qomah Ch 1:
- **First Kabbalah-tradition text** live (new tradition `kabbalah` order 12)
- **First text translated specifically to close a Raëlian-canon source-tension** (the *parasangs* citation in *The End of the World* and *At the Root of All Religions*)
- **18 new central glossary entries** including the Sitchin/Anunnaki-disavowal-anchor `parasang-cosmic-measurement` and the Christological-typology-dispute-preserving `naar-the-youth-metatron` entries
- **First overlay→central candidate**: the `chasi-kinnuy` (Siddur-Rabbah-distinctive technical term) and the `64-faced-hayyot` (Cohen-1985-distinctive amplification) — both flagged for promotion when subsequent Hekhalot texts arrive

The verification-pass against Cohen 1985 TSAJ 9 remains as future work.
