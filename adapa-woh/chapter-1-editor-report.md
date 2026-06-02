# Chapter 1 Editor Report — Adapa and the South Wind

## Overview

The Wheel of Heaven Translation Program's **first Akkadian-source text** and the project's most lens-risk-laden Mesopotamian composition to date. **79 preserved lines across 4 fragments** (A — Amarna EA 356 Old/Middle Babylonian; B — K.8214+ Neo-Assyrian Nineveh main narrative; C — Late Babylonian fragmentary; D — Late Babylonian preserving the catchline). The Translator submitted 35 `editorial_questions[]`; this Editor pass resolves every one (each folded into a glossary entry, surfaced in commentary, or flagged in this report) and clears the array.

This pass extends the Mesopotamian-pipeline conventions ratified at Enki and Ninmaḫ (project's first Sumerian text) and at Flood Story (project's second Sumerian text), and wires the project's **first cross-language sibling-clusters spanning the full three-way Akkadian-Sumerian-Hebrew matrix** with Akkadian as the source-side. Where prior Mesopotamian passes had Akkadian-side coverage in rationale only (with Sumerian-text refIds in `appliesTo`), this pass activates Akkadian-side `appliesTo` extensions across multiple existing entries and adds substantial new central entries on the **lost-immortality crux** that is the chapter's central payload.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.glossaryVersion`: `2.55.0` → `2.56.0`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0`

The chapter's `verificationStatus` field — *best-effort reconstruction; verification pending against Izre'el 2001* — is **preserved** unchanged. The lens-discipline and glossary work in this pass operates on the **sense-of-line** (well-attested across editions: Foster 2005, Heidel 1942, Picchioni 1981, Lambert 1976, Izre'el 2001's published commentary). A downstream verification-pass against Izre'el 2001's critical edition is requested for sign-level transliteration verification.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bump: 2.55.0 → 2.56.0.** `sourceLanguages` continues `["he", "sux", "akk"]` (akk was added at intake to this pass). Total terms: 600 → 613 (13 new central entries added).

**13 new central entries** (the chapter's lost-immortality cross-corpus payload):

1. `nemequ-napishtu-dariti-wisdom-but-not-immortality-paradigm-sage-cross-corpus` (claim_type: `direct`) — the foundational paradigm-sage-mortal-by-design line at Adapa A:10 (*nēmequ id-din-šu, napišta dāriti ul id-din-šu* 'wisdom he gave him; eternal life he did not give him'). Cross-corpus Hebrew Gen 3:22 inverse-pattern; Gilgamesh X.301-322 (Siduri's wisdom-about-mortality speech); Atrahasis lifespan-limit; Eccl 3:11 and Job 28 wisdom-traditions. Bidirectional Hebrew-side wiring to `etz-chayim-daat`, `ke-achad-mimmennu`, and `gan-be-eden`.
2. `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus` (claim_type: `direct`) — the food-and-water of life immortality-substance pair. Cross-corpus Hebrew *etz ha-chayyim* (Gen 2:9, 3:22; Prov 3:18; Ezek 47:12; Rev 22:1-2). The inverse-parallel between Adapa (refuses divine food, loses immortality) and Eden (eats divine food, loses immortality) documented as named-scholarship comparative-mythology (Heidel 1942; Buccellati 1973; Hallo 1969; Kvanvig 2011). Explicit operational disavowals against Christian-Johannine *bread-of-life* / *living-water* pre-resolution and against Sitchin-corpus *engineered-immortality-substance* readings.
3. `ea-warning-deception-misadvice-test-crux-cross-corpus` (claim_type: `direct`) — the central interpretive crux of the composition. Three named-scholarship readings: (a) deliberate-deception (Lambert; Kvanvig 2011); (b) unintentional-misadvice (Buccellati 1973; Bing 2000); (c) strategic-test (Izre'el 2001). **No adjudication.** Cross-corpus Gen 3 *lo mot temutun* / *mot tamut* warning-crux as structural-parallel-with-inverse-trust-relations. Explicit operational disavowals against Christian-Adamic-Fall pre-resolution and against Sitchin-tradition Ea-as-Anunnaki-rebel readings.
4. `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` (claim_type: `direct`) — the speech-act-efficacy thesis (Izre'el 2001's monograph-subtitle thesis-line: *Language Has the Power of Life and Death*). Cross-corpus Marduk-creation-by-speech (Enuma Elish IV.19-26); Hebrew creation-by-speech (Gen 1 *va-yomer Elohim*); Isa 55:11; Prov 18:21 (arguably the closest Hebrew parallel to Izre'el's subtitle); Hebrew curse-and-blessing speech-act tradition (Gen 27, Num 22-24, Deut 27-28). Explicit operational disavowals against Christian-Johannine *Logos* pre-resolution and against Sitchin-corpus *sonic-frequency-weapon* readings.
5. `shutu-cardinal-winds-akkadian-four-winds-divinized-cross-corpus` (claim_type: `direct`) — the four named cardinal winds of Akkadian meteorology, divinized. Cross-corpus Hebrew *arba ruchot ha-shamayim* four-winds-of-heaven tradition (Jer 49:36; Ezek 37:9; Zech 2:10, 6:1-8; Dan 7:2; Rev 7:1). The Mesopotamian → Hebrew de-divinization-of-the-winds shift documented. Distinct from the *imhullu* destructive-storm-wind cluster (existing central entry).
6. `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus` (claim_type: `direct`) — the human-ascent-to-heaven motif. Cross-corpus Mesopotamian Etana (Old Babylonian *Etana Epic*); Hebrew Hanokh/Enoch (Gen 5:24 + 1 Enoch's ascent); Eliyahu/Elijah (2 Kgs 2:11); Isaiah-Ezekiel throne-visions (Isa 6, Ezek 1); Hekhalot-merkavah tradition; Pauline ascent (2 Cor 12:1-4). Explicit operational disavowals against Sitchin-corpus *ascent-as-space-flight* readings and against Christian-Pauline-soteriology pre-resolution.
7. `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus` (claim_type: `direct`) — Dumuzi and Gizzida as heaven-gate-keepers and dying-and-rising vegetation-deities. **Direct etymological cognate** to Hebrew Tammuz (Ezek 8:14). Cross-corpus Greek Adonis (West-Semitic *adon* 'lord'); Phoenician Eshmun; Egyptian Osiris. Named-scholarship critique of Frazer's collapsed *dying-and-rising god* archetype documented (Mettinger 2001; J. Z. Smith 1990). Explicit operational disavowals against Christian-resurrection-typology pre-resolution and against Sitchin-corpus *engineered-immortal-prototype* readings.
8. `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus` (claim_type: `direct`) — Anu's theodicy-question at B:50 ('why did Ea reveal heaven and earth to a son of humankind?'). Cross-corpus Hebrew Gen 3:22 (existing entry `ke-achad-mimmennu`); 1 Enoch 6-11 Watchers tradition + underlying Gen 6:1-4; Greek Prometheus (Hesiod; Aeschylus). The apkallu-to-Watchers conceptual-link (Kvanvig 1988, 2011) documented. Explicit operational disavowals against Sitchin-corpus *Ea-leaked-genetic-tech* readings and against Christian Eden-Fall typology.
9. `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus` (claim_type: `direct`) — Adapa as the first of the seven antediluvian apkallu-sages of Mesopotamian tradition; the *māru ša Eridu* 'son of Eridu' standing-epithet. Cross-corpus Berossus' Oannes; the Uruk apkallu-list; the apkallu-iconography (fish-cloaked figures); the apkallu-to-Watchers conceptual-link (Kvanvig); the Hebrew antediluvian-genealogy Gen 5 (with the En-men-dur-Ana / Hanokh comparison). The Egyptian Imhotep functional-parallel. Explicit operational disavowal against Sitchin-corpus *apkallu-as-Anunnaki-civilizing-mission-personnel* readings.
10. `divine-laughter-anu-laughs-sahaq-tsachu-cross-corpus` (claim_type: `direct`) — Anu's laughter at B:58. Cross-corpus Hebrew *sahaq / tzachaq* divine-laughter (Ps 2:4; Ps 37:13; Ps 59:8; the Yitzchaq/Isaac name-etymology pericopes). The Akkadian *ṣâḫu* and Hebrew *sahaq / tzachaq* are **direct Semitic cognates**. Greek *gelōs* (Homeric divine-laughter; Halliwell 2008). The semantic-openness of *ṣâḫu* between derisive / amused / ironic-cosmic readings documented; no adjudication.
11. `return-to-the-earth-mortality-verdict-adapa-genesis-cross-corpus` (claim_type: `direct`) — Anu's *ana erṣeti-šu utīrā-šu* 'return him to his earth' at B:61. Cross-corpus Hebrew Gen 3:19 *el afar tashuv* 'to dust you shall return'; the wider Hebrew dust-mortality vocabulary (Ps 90:3; Ps 103:14; Ps 104:29; Eccl 3:20, 12:7; Job 10:9, 34:15). Both narratives close with the explicit divine-decree of human-return-to-the-earth.
12. `shedu-lamassu-tutelary-spirit-akkadian-hebrew-shedim-cross-corpus` (claim_type: `direct`) — Adapa's challenge to the South Wind to show its *šēdu* (tutelary-spirit / demon-form) at B:9. **Direct Akkadian → Hebrew loanword** *shedim* (Deut 32:17, Ps 106:37). The Mesopotamian *lamassu* / *šēdu* tutelary-pair iconography (Neo-Assyrian winged-bull colossi). Greek *daimōn* and the *tutelary-spirit-vocabulary domesticated-and-narrowed-to-demon* cross-cultural pattern.
13. `mourning-garb-dishevelled-hair-sackcloth-cross-corpus` (claim_type: `direct`) — Adapa's mourning-garb at B:20, 37-38 (*qarrāda* dishevelled hair + *kāspa* mourning-garment). Cross-corpus Hebrew *sak ve-efer* sackcloth-and-ashes tradition (Gen 37:34, 2 Sam 3:31, Esth 4:1, Dan 9:3, Jonah 3:5-8; Anderson 1991, Olyan 2004).

**10 existing central entries received either `appliesTo` extension to Akkadian-side Adapa refIds, rationale-appended cross-corpus back-references, or both:**

- `digir-sumerian-divine-lexeme-cross-corpus` — extended with 31 Adapa refIds (every (d)PN attestation); rationale appended with Akkadian-side-activation note documenting the project's first Akkadian-text DINGIR-prose-drop deployment.
- `abzu-engur-sumerian-subterranean-deep-cross-corpus` — extended with 7 Adapa refIds (Eridu / Ea's domain attestations); rationale appended with Adapa Akkadian-side-activation note; *māru ša Eridu* 'son of Eridu' epithet as apkallu-paradigm-link.
- `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus` — extended with ADP-WOH-A:13 (the restored *ṣalmāt qaqqadi* line). Akkadian-side activation completes the bidirectional Sumerian-Akkadian sibling-cluster on the lexeme.
- `an-enlil-enki-ninhursaga-flood-council-quartet-cross-corpus` — extended with 11 Adapa refIds (Anu and Ea attestations); rationale appended noting the Anu-Ea axis foregrounded in Adapa, with Enlil and Ninhursaĝa absent from the surviving fragments.
- `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` — **flag-only** (no appliesTo extension); rationale appended noting the conceptual-cluster (Adapa serves Ea at Eridu) is present but the diagnostic *dullu* keyword does not survive. Atrahasis is the proper attestation locus for Akkadian-side activation; deferred.
- `im-hul-imhullu-destructive-storm-wind-mesopotamian-storm-vocabulary-cross-corpus` — **flag-only** (no appliesTo extension); rationale appended noting *Šūtu* is **not** *imhullu* and the cardinal-winds cluster is distinct. Cross-reference to new entry `shutu-cardinal-winds-akkadian-four-winds-divinized-cross-corpus`.
- `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus` — extended with ADP-WOH-B:12 (the seven-day South-Wind cessation); rationale appended with the seven-day-cosmic-marker structural-numeral note (the Mesopotamian-7 vs Hebrew-7/40 transformation not implicated at this Adapa-internal attestation).
- `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` — extended with 18 Adapa refIds (all lacuna-marked lines).
- `ke-achad-mimmennu` — rationale appended with cross-corpus back-reference to Adapa B:50 (Anu's divine-secret-leak recognition); cross-references to new central entries `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus` and `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus`.
- `gan-be-eden` — rationale appended with cross-corpus back-reference to Adapa B:51-52 food-of-life and the inverse-parallel pattern documentation.
- `etz-chayim-daat` — rationale appended with cross-corpus back-reference to Adapa A:10 wisdom-not-immortality and B:51-52 food-of-life; explicit named-scholarship-comparative-mythology framing with Adapa-not-Adam identity-claim disavowal.
- `zi-da-ri-balatu-daru-eternal-life-cross-corpus` — extended with ADP-WOH-A:10 (the *napišta dāriti* attestation); rationale appended documenting the *napištu dārītu* ↔ *balāṭu dārû* lexical-pair and grounding the entry's first Akkadian-text deployment.

**Bidirectional cross-references verified.** Each new Akkadian-source central entry that references an existing Hebrew central entry by id has had the corresponding back-reference added to the Hebrew entry's rationale prose in the same edit. Each new central entry's `appliesTo` lists are populated with the relevant Adapa refIds; the existing-entry `appliesTo` extensions are applied as documented above.

### Per-translation overlay glossary (`data-library/adapa-woh/_translation-glossary.json`)

**Version bump: 1.0.0 → 1.1.0**.

**9 new overlay entries** (composition-specific philological detail and Adapa-singular vocabulary; cross-corpus foundational vocabulary went to the central glossary):

1. `title-and-meta-conventions-adapa` (claim_type: `direct`) — chapter-title-and-subtitle convention.
2. `verification-pending-disclosure-adapa-akkadian` (claim_type: `direct`) — verification-pending disclosure convention for the project's first Akkadian-source text.
3. `me-qadishuti-pure-cult-waters-akkadian-eridu-temple-service` (claim_type: `direct`) — *mê qadišūti* 'the pure waters' at B:3 (Adapa's daily cult-service vocabulary).
4. `bit-nuni-house-of-the-fish-belly-of-the-deep-adapa` (claim_type: `direct`) — *bīt nūni* 'house of the fish' poetic-kenning at B:8 / B:47; cross-corpus Jonah belly-of-the-fish.
5. `ilabrat-sukkallu-anu-vizier-adapa` (claim_type: `direct`) — Ilabrat the *sukkallu* of Anu at B:13/B:15. **Flagged for future central promotion** at Inana's Descent (where Ninshubur as the parallel-figure is more central).
6. `kappi-wing-of-shutu-the-wing-breaking-image-adapa` (claim_type: `direct`) — *kappī* 'wing' + the wing-breaking image at B:10-11.
7. `ea-instruction-coaching-speech-form-adapa` (claim_type: `direct`) — the master-to-disciple coaching-speech genre at B:21-34.
8. `anointing-and-garment-non-deadly-accompaniments-adapa` (claim_type: `direct`) — the garment and oil as non-deadly accompaniments at B:32-33, B:53-54, B:57; the selective-warning as evidence-point for the deliberate-deception reading of the Ea-warning crux.
9. `catchline-and-fragmentary-fragments-cd-disclosure-adapa` (claim_type: `direct`) — Fragment-C-and-D conservative-rendering convention for the small fragmentary Adapa fragments.

## Resolution of the 35 editorial_questions

The Translator submitted 35 editorial questions; all are resolved as follows.

**Major central candidates ratified (8 of 8 mandatory):**
- ADP-WOH-A:10 (wisdom-but-not-immortality) → `nemequ-napishtu-dariti-wisdom-but-not-immortality-paradigm-sage-cross-corpus` (CENTRAL)
- ADP-WOH-A:13 (ṣalmāt qaqqadi black-headed people) → existing `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus` extended with Akkadian-side appliesTo
- ADP-WOH-B:7 (Šūtu South Wind) → `shutu-cardinal-winds-akkadian-four-winds-divinized-cross-corpus` (CENTRAL)
- ADP-WOH-B:10 (speech-act efficacy / wing-breaking) → `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` (CENTRAL) + overlay `kappi-wing-of-shutu-the-wing-breaking-image-adapa`
- ADP-WOH-B:22 (heavenly ascent) → `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus` (CENTRAL)
- ADP-WOH-B:23 (Dumuzi-Gizzida dying-and-rising vegetation deities) → `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus` (CENTRAL)
- ADP-WOH-B:30 (Ea-warning food-of-death) → `ea-warning-deception-misadvice-test-crux-cross-corpus` (CENTRAL) — three readings documented without adjudication
- ADP-WOH-B:50 (divine-secret-leak / Anu's theodicy-question) → `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus` (CENTRAL)
- ADP-WOH-B:51 (food-of-life / water-of-life) → `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus` (CENTRAL)
- ADP-WOH-B:55 (Adapa refuses) → subsumed under B:51 central candidate with explicit inverse-parallel framing in the rationale

**Major overlay / extension resolutions:**
- ADP-WOH-A:1 (foreshadow of Adapa-as-speech-organ) → folded into commentary; cross-references new `speech-act-efficacy-...` central entry
- ADP-WOH-A:3 (bitter-mouth obscure reading) → commentary documents three named-scholarship readings; verification pending flagged
- ADP-WOH-A:4 (sense uncertain) → commentary documents the editions' disagreement; verification pending flagged
- ADP-WOH-A:7 (heart of the diadem of heaven metaphor) → commentary documents three readings; metaphor preserved untranslated
- ADP-WOH-B:1 (Adapa-as-apkallu-paradigm) → `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus` (CENTRAL) — promoted to central given recurrence across Mesopotamian texts and the apkallu-to-Watchers conceptual link
- ADP-WOH-B:3 (mê qadišūti pure cult-waters) → overlay `me-qadishuti-pure-cult-waters-akkadian-eridu-temple-service`
- ADP-WOH-B:8 (bīt nūni house-of-the-fish kenning) → overlay `bit-nuni-house-of-the-fish-belly-of-the-deep-adapa`
- ADP-WOH-B:9 (šēdu tutelary-spirit / demon-form) → `shedu-lamassu-tutelary-spirit-akkadian-hebrew-shedim-cross-corpus` (CENTRAL)
- ADP-WOH-B:12 (seven-day cosmic marker) → existing `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus` extended with ADP-WOH-B:12
- ADP-WOH-B:13 (Ilabrat the sukkallu) → overlay `ilabrat-sukkallu-anu-vizier-adapa` (flagged for future central promotion at Inana's Descent)
- ADP-WOH-B:19 (Ea apkal Eridu) → folded into central `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus`
- ADP-WOH-B:20 (mourning-garb dishevelled hair + kāspa) → `mourning-garb-dishevelled-hair-sackcloth-cross-corpus` (CENTRAL)
- ADP-WOH-B:26 (seasonal disappearance of vegetation-gods) → subsumed under B:23 Dumuzi-Gizzida central candidate
- ADP-WOH-B:33 (anointing with oil cult-rite) → overlay `anointing-and-garment-non-deadly-accompaniments-adapa`; cross-corpus Hebrew mashach tradition flagged for future Hebrew Editor pass
- ADP-WOH-B:34 (master-disciple binding-instruction) → overlay `ea-instruction-coaching-speech-form-adapa`
- ADP-WOH-B:35 (second ascent) → subsumed under B:22 central candidate
- ADP-WOH-B:58 (Anu's laughter) → `divine-laughter-anu-laughs-sahaq-tsachu-cross-corpus` (CENTRAL); tone-adjudication AVOIDED
- ADP-WOH-B:59 (Anu's confirm-it-was-life question) → cross-referenced to B:30/B:51 central candidates in commentary
- ADP-WOH-B:61 (return-to-the-earth verdict) → `return-to-the-earth-mortality-verdict-adapa-genesis-cross-corpus` (CENTRAL)
- ADP-WOH-B:62-64 (broken closing) → conservative broken-marker preserved; verification pending
- ADP-WOH-C:1 (Fragment C fragmentary) → overlay `catchline-and-fragmentary-fragments-cd-disclosure-adapa`; conservative default preserved
- ADP-WOH-D:1 (Fragment D catchline) → overlay `catchline-and-fragmentary-fragments-cd-disclosure-adapa`; conservative default preserved

**Project-wide cross-language sibling-cluster activation (ADP-WOH-A:1 — flagged-as-project-wide):**
- Akkadian-side appliesTo activation across `digir-sumerian-divine-lexeme-cross-corpus`, `abzu-engur-sumerian-subterranean-deep-cross-corpus`, `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus`, `an-enlil-enki-ninhursaga-flood-council-quartet-cross-corpus`, `lacuna-bracket-convention-sumerian-mesopotamian-project-standard`, `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus`, and `zi-da-ri-balatu-daru-eternal-life-cross-corpus`. Akkadian-side activation **flag-only** (no appliesTo extension) for `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` (the *dullu* keyword does not survive in Adapa) and `im-hul-imhullu-destructive-storm-wind-mesopotamian-storm-vocabulary-cross-corpus` (Šūtu is not *imhullu*).

**Project-wide lens-discipline disavowals (ADP-WOH-A:1 — flagged-as-project-wide):**
- **Adapa-as-Adam identity claim** — explicit disavowal documented in the rationale of `nemequ-napishtu-dariti-wisdom-but-not-immortality-paradigm-sage-cross-corpus`, `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus`, `ea-warning-deception-misadvice-test-crux-cross-corpus`, `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus`, and `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus`. The names are etymologically unrelated (*Adapa* possibly from Akkadian root *adap-* / *adb-* 'wise'; *Adam* from Hebrew *adamah* 'earth'); the older Cyrus Gordon 1958 identity-equation is no longer the scholarly consensus; modern consensus (Izre'el 2001; Foster 2005; Buccellati 1973; Hallo 1969; Mettinger 2007) is structural-comparative-mythology, not identity.
- **Sitchin-corpus disavowals** — explicit disavowals at every major central-candidate rationale: (i) *no Adapa-as-Anunnaki-genetic-engineering-product* (at the apkallu and wisdom-grant entries); (ii) *no heavenly-ascent-as-space-flight* (at the ascent entry); (iii) *no food-of-life-as-engineered-immortality-substance* (at the food-of-life entry); (iv) *no Ea-as-Anunnaki-rebel-keeping-humanity-mortal* (at the Ea-warning-crux entry); (v) *no Anunnaki-leaked-genetic-tech-to-humans* (at the divine-secret-leak entry); (vi) *no Anunnaki-engineered-atmospheric-disturbance-technology* (at the Šūtu entry); (vii) *no sonic-frequency-weapon* (at the speech-act-efficacy entry).
- **Christian-soteriological pre-resolution disavowals** — explicit at the relevant entries: no Johannine *bread-of-life* / *living-water* / *Logos* pre-resolution at the food-of-life and speech-act entries; no Eden-Fall typology pre-resolution at the wisdom-without-immortality, Ea-warning, and divine-secret-leak entries; no resurrection-typology pre-resolution at the Dumuzi-Tammuz-Adonis entry; no Pauline-third-heaven typology pre-resolution at the ascent entry.

## Speculative entries requiring sign-off

**None.** This Editor pass produced **zero** `claim_type=speculative` entries.

The Editor's working principle on this Akkadian composition — the project's most lens-risk-laden text to date — was the project's *accuracy-above-lens* discipline. Every divergence from the standard scholarly reading is documented as named-scholarship (Izre'el 2001; Foster 2005; Lambert 1976; Heidel 1942; Picchioni 1981; Buccellati 1973; Hallo 1969; Kvanvig 1988 + 2011; Westermann; Wenham; Levenson; Sarna; Mettinger 2001; Halliwell 2008; J. Z. Smith 1990; Anderson 1991; Olyan 2004; Wiggermann 1992 + 2007; Heidel; etc.); no WoH-distinctive synthesis is surfaced in the translation surface or glossary entry rationales. The translation's surface reads as a defensible scholarly modern-English rendering in the Foster / Izre'el register. The Wheel of Heaven lens is reserved for the wiki and methodology pages.

**Seven places where the Editor could have introduced speculative readings but did not, with explicit operational disavowals documented in glossary-entry rationales:**

1. **Ea-as-Anunnaki-rebel-keeping-humanity-mortal reading (the Sitchin Ea-deception interpretation).** The Sitchin-corpus interpretation reads Adapa B:30-31 as evidence for an Anunnaki-political-rivalry in which Ea, the rebellious-scientist faction, deceives Adapa to prevent humanity from gaining the Anunnaki-engineered immortality-treatment. The Editor's choice was to surface the three named-scholarship readings (deliberate-deception per Lambert/Kvanvig; unintentional-misadvice per Buccellati/Bing; strategic-test per Izre'el 2001) without preferring any one, and to **explicitly disavow** the Sitchin interpretation in the entry's rationale. The Akkadian source-text does not document Ea's motive; the three scholarly readings each work without recourse to extraterrestrial-political-rivalry.

2. **Food-of-life as Anunnaki-engineered-immortality-substance reading.** The Sitchin-corpus reading of *akāl balāṭi* / *mê balāṭi* as the Anunnaki-engineered life-extension-substance / genetic-immortality-treatment is heavily-deployed in popular-fringe literature. The Editor's choice was to surface the standard scholarly philological-and-comparative-mythology analysis — the food-and-water-of-life is the immortality-substance of Mesopotamian theological-mythology, with cross-corpus reach to the Hebrew tree-of-life — and to **explicitly disavow** the engineering-substance reading. The named-scholarship treatment (Izre'el 2001; Heidel 1942; Buccellati 1973; Hallo 1969; Kvanvig 2011) treats the substance-pair as theological-aetiological, not technological.

3. **Heavenly-ascent as space-flight reading.** The Sitchin-tradition reading of Adapa's ascent — and Etana's, Enoch's, Elijah's — as literal-physical-transportation to Anunnaki-orbital-installations via rocket or shuttle is **explicitly disavowed** at the ascent central entry. The Akkadian *elû ana šamê* 'ascend to heaven' is the standard Mesopotamian cosmographic-ascent vocabulary in the theological-mythological register; no technological-engineering vocabulary is present. The cross-corpus tradition (Etana, Enoch, Elijah, Isaiah, Ezekiel, Paul, Hekhalot) is uniformly mythological-apocalyptic, not technological.

4. **Apkallu as Anunnaki-civilizing-mission-personnel reading.** The Sitchin-reading of the seven antediluvian apkallu as the Anunnaki engineering-team that taught humans the foundations of civilization is **explicitly disavowed** at the apkallu central entry. The Mesopotamian source-texts deploy *nēmequ* (wisdom), *āšipūtu* (incantation-craft), *bârūtu* (divination-craft) — theological-mythological vocabularies of sage-craft and cult-foundation, not engineering-protocol vocabulary.

5. **Dumuzi-as-engineered-immortal-prototype reading.** The Sitchin-corpus reading of the dying-and-rising-god cluster (Dumuzi, Tammuz, Adonis, Osiris) as evidence of Anunnaki-engineered-resurrection-prototypes or first-genetic-immortality-experiments is **explicitly disavowed** at the Dumuzi central entry. The Mesopotamian source-texts deploy seasonal-vegetation-cycle theological-mythological vocabulary; no engineering vocabulary is present. The Editor additionally documents the named-scholarship critique of Frazer's collapsed *dying-and-rising god* archetype (Mettinger 2001; J. Z. Smith 1990).

6. **Adapa-as-Adam identity claim.** The older Cyrus Gordon 1958 and pre-1970 comparative-mythology tradition treated Adapa and Adam as the-same-figure-told-two-ways. Modern scholarly consensus (Izre'el 2001; Foster 2005; Buccellati 1973; Hallo 1969; Mettinger 2007) treats them as **structural-comparative-mythology parallel**, not identity. The names are etymologically unrelated; the comparative-mythology framing is explicitly named-scholarship in this pass's glossary rationales. Explicit disavowal documented at five of the new central entries.

7. **Christian-soteriological pre-resolution.** The Christian reception-history of the food-of-life, water-of-life, *Logos*, bread-of-life, living-water, ascent-to-third-heaven, dying-and-rising-vegetation-god, and Eden-Fall traditions is the downstream theological layer that the Editor does **not** pre-resolve the Akkadian or Hebrew source-material to. The typological readings are reserved for the wiki and broader-corpus discussions; the glossary apparatus surfaces the source-attestations in their own register.

## Unresolved editorial questions

**None.** All 35 editorial questions are resolved. The `editorial_questions[]` array is empty in the chapter-1.json output.

## Verification-pending status

The chapter's `translation.verificationStatus` field — *best-effort reconstruction; verification pending against Izre'el 2001 (MC 10, Winona Lake 2001)* — is **preserved** unchanged. The following lines are specifically flagged as containing transliteration-reconstruction risk:

- **ADP-WOH-A:1** — *ina [pān(?)] Anu it-bi* — Knudtzon 1915 reading restored; pending verification.
- **ADP-WOH-A:3** — *ma-ru-uš (d)Ea [pi-i] mar-tu-šu ub-bi-[il]-am-ma* — bracketed *[pi-i]* restoration follows Foster 2005; reading is debated.
- **ADP-WOH-A:4** — *ki-i e-ru-na uš-bi-ʾu* — sense uncertain; Izre'el 2001 and Foster 2005 differ.
- **ADP-WOH-A:8** — *ru-ub-bi-iš-šu i[g]-ga-ar-[X] ta-na-am-ma* — bracketed restoration; verification pending.
- **ADP-WOH-A:11** — *ina ūmīšu-ma […] mār Ea ūmišammi(?)* — *ūmišammi(?)* with editorial query; verification pending.
- **ADP-WOH-A:12** — *ašar (d)Ea ina qereb Eridu(KI) ina ramāni-šu(?) ibšû* — *ramāni-šu(?)* with editorial query.
- **ADP-WOH-A:13** — *(d)Adapa [šarru(?) ša ṣalmāt qaqqadi]* — bracketed restoration; *šarru(?)* with editorial query; the *ṣalmāt qaqqadi* portion is the key cross-corpus link for the Sumerian-Akkadian sibling-cluster.
- **ADP-WOH-B:6** — *[X X] elippa-šu nāru ina(?) mê i-šat-tu* — bracketed restoration at the beginning of the line.
- **ADP-WOH-B:9** — *Šūtu (d)X X [le-e]q-e (d)Šūta lūmur šēd-ki* — multiple editorial queries and brackets.
- **ADP-WOH-B:42** — *Anu pānu-šu damqu uš-pe-l-am-ma* — *uš-pe-l-am-ma* (causative form) — verification pending.
- **ADP-WOH-B:62-64** — broken closing of Fragment B; Foster 2005's supplementation rests on parallel-text logic and is not secure.
- **ADP-WOH-C:1** — Fragment C is too fragmentary for confident per-line reconstruction; conservative bracketed editorial-note-line.
- **ADP-WOH-D:1** — Fragment D catchline specifics pending verification.

The Editor's lens-discipline work on glossary entries and commentary is **independent** of the sign-by-sign transliteration verification: the sense-of-line is well-attested across editions (Foster 2005; Heidel 1942; Picchioni 1981; Lambert 1976; Izre'el 2001's published commentary), and the lens-discipline operates on the sense, not on the sign-level reconstruction. A downstream verification-pass against Izre'el 2001's critical edition (the modern critical edition, *Mesopotamian Civilizations* 10, Winona Lake 2001) is requested to confirm transliteration accuracy.

## Items flagged for future cross-corpus wiring (not blocking this pass)

These are wiring-tasks for future Editor passes; they do not block the current pass's sign-off.

1. **Hebrew central entries on cross-corpus cluster heads.** Several Hebrew lexemes referenced in this pass's new central entries do not yet have dedicated Hebrew central entries:
   - *Tammuz* (Ezek 8:14) — the Hebrew side of the Dumuzi-Tammuz-Adonis cluster.
   - *Hanokh* / *vayithallech* (Gen 5:24) — the Hebrew side of the ascent-to-heaven cluster.
   - *Eliyahu* / *vayaal ba-se'arah ha-shamayim* (2 Kgs 2:11) — Elijah's whirlwind-ascent.
   - *Sak ve-efer* (Gen 37:34, Esth 4:1, Dan 9:3) — the Hebrew side of the mourning-garb cluster.
   - *Shedim* (Deut 32:17, Ps 106:37) — the Hebrew side of the šēdu loanword cluster (Akkadian → Hebrew direct cognate).
   - *Sahaq / tzachaq* (Ps 2:4 etc.; Yitzchaq name-etymology pericopes) — the Hebrew side of the divine-laughter cluster (Akkadian-Hebrew Semitic cognate).
   - *Mashach / mashiach / shemen* (1 Sam 16:13; Ex 30:22-33) — the Hebrew side of the anointing-with-oil cult-rite cluster.
   - *Arba ruchot ha-shamayim* (Jer 49:36; Ezek 37:9; Zech 6; Dan 7) — the Hebrew side of the four-winds tradition.
   - *Bnei Adam* (Gen 11:5 etc.) — the Hebrew patronymic-humanity self-designation as functional-parallel to *ṣalmāt qaqqadi* / *saĝ gig-ga*.
   Future Hebrew Editor passes on the relevant pericopes should produce these Hebrew central entries with bidirectional back-references to the corresponding Akkadian and Sumerian central entries.

2. **Atrahasis and Enuma Elish foundational entries.** When the project translates Atrahasis (next major Akkadian text in the roadmap) and Enuma Elish, the foundational Akkadian vocabulary will receive further appliesTo extensions and possibly new entries:
   - *dullu* (Akkadian *dullu* — divine-toil-relieved-by-humans; central entry already exists) — Atrahasis will be the major Akkadian-side activation.
   - *abūbu* (Akkadian flood; central entry exists with Sumerian-side primary; Akkadian-side activation at Atrahasis and Gilgamesh XI).
   - *eleppu* (Akkadian boat; central entry exists; Akkadian-side activation at Atrahasis and Gilgamesh XI).
   - *kīma ilāni* (like the gods; central entry exists with Sumerian-side; Akkadian-side activation at Gilgamesh XI and Adapa? — not in surviving Adapa fragments, but Atrahasis and Gilgamesh).
   - *Marduk's word* (Enuma Elish IV.19-26) — the new central entry `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` will receive Akkadian-side appliesTo extensions at Enuma Elish.

3. **Inana's Descent — the central locus for *sukkallu* divine-vizier promotion.** The overlay entry `ilabrat-sukkallu-anu-vizier-adapa` is flagged for future central promotion at Inana's Descent (ETCSL 1.4.1), where Ninshubur's *sukkallu* role is more central to the narrative.

4. **Etana — the central locus for the ascent-to-heaven cluster expansion.** The new central entry `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus` will receive appliesTo extensions when the project translates the Etana Epic (the cross-corpus closest-parallel to Adapa's ascent).

5. **Sumerian King List — the apkallu and antediluvian-king tradition.** The new central entry `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus` will receive appliesTo extensions at the Sumerian King List (ETCSL 2.1.1), where the apkallu-tradition is paired with the antediluvian-king-list.

## Cross-corpus bidirectional sibling-cluster summary

This Editor pass wires the project's **first cross-language three-way sibling-clusters with Akkadian as the source-side** and complements the Sumerian-source clusters established at Enki and Ninmaḫ and Flood Story. The bidirectional links are verified in both directions on every cross-corpus central entry that references an existing Hebrew central entry by id.

### Three-way Akkadian-Sumerian-Hebrew clusters new at this pass

- **Wisdom-but-not-immortality paradigm** — Akkadian *nēmequ id-din-šu napišta dāriti ul id-din-šu* (Adapa A:10) ↔ Sumerian wisdom-tradition (the *me*-cluster; the apkallu-tradition) ↔ Hebrew Gen 3:22 + Eccl 3:11 + Job 28. The new central entry `nemequ-napishtu-dariti-wisdom-but-not-immortality-paradigm-sage-cross-corpus`.
- **Food-of-life / water-of-life immortality-substance** — Akkadian *akāl balāṭi* / *mê balāṭi* (Adapa B:51-52) ↔ Sumerian Dilmun-tradition (paradise-by-negation-of-mortality) ↔ Hebrew *etz ha-chayyim* + Ezek 47:12 + Rev 22:1-2. The new central entry `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus`, with inverse-parallel-pattern documentation.
- **Speech-act efficacy** — Akkadian *amat pī-šu* / Marduk's word in Enuma Elish IV ↔ Sumerian destiny-decree (*nam tar*) and divine-assembly-decree (*di-til-la inim puḫrum*) ↔ Hebrew *va-yomer Elohim* / Isa 55:11 / Prov 18:21. The new central entry `speech-act-efficacy-language-power-of-life-and-death-cross-corpus`.
- **Divine-secret-leak / forbidden-knowledge** — Akkadian Anu-Ea-Adapa (Adapa B:50) ↔ Sumerian apkallu-civilizing-mission ↔ Hebrew Gen 3:22 + 1 Enoch Watchers + Greek Prometheus. The new central entry `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus`.
- **Return-to-the-earth mortality-verdict** — Akkadian *ana erṣeti-šu utīrā-šu* (Adapa B:61) ↔ Sumerian return-to-the-earth in Inana's Descent ↔ Hebrew Gen 3:19 *el afar tashuv* + Ps 90:3 + Eccl 12:7. The new central entry `return-to-the-earth-mortality-verdict-adapa-genesis-cross-corpus`.

### Direct Semitic-cognate Akkadian-Hebrew clusters

These are the loci where Akkadian and Hebrew are **direct Semitic cognates** (not merely thematic-parallels) — the strongest cross-corpus linkages.

- **Šēdu ↔ shedim** — Akkadian *šēdu* tutelary-spirit/demon-form (Adapa B:9) ↔ Hebrew *shedim* (Deut 32:17; Ps 106:37). **Direct Akkadian → Hebrew loanword.** The new central entry `shedu-lamassu-tutelary-spirit-akkadian-hebrew-shedim-cross-corpus`.
- **Dumuzi ↔ Tammuz** — Akkadian *Dumuzi* (Adapa B:23 etc.) ↔ Hebrew *Tammuz* (Ezek 8:14; the month-name). **Direct etymological cognate** with regular Semitic phonological development. The new central entry `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus`.
- **Ṣâḫu ↔ sahaq** — Akkadian *ṣâḫu* 'to laugh' (Adapa B:58) ↔ Hebrew *sahaq / tzachaq* (Ps 2:4 etc.). **Direct Semitic cognate** (proto-Semitic *√ṣḥq). The new central entry `divine-laughter-anu-laughs-sahaq-tsachu-cross-corpus`.
- **Šamnu ↔ shemen** — Akkadian *šamnu* 'oil' (Adapa B:33) ↔ Hebrew *shemen*. Direct Semitic cognate; the anointing-with-oil cult-rite shared across both traditions. Documented in overlay `anointing-and-garment-non-deadly-accompaniments-adapa`.
- **Qadišu ↔ qadosh** — Akkadian *qadišu* 'pure, holy' (in Adapa B:3 *mê qadišūti*) ↔ Hebrew *qadosh* 'holy'. Direct Semitic cognate. Documented in overlay `me-qadishuti-pure-cult-waters-akkadian-eridu-temple-service`.
- **Awīlūtu ↔ no direct Hebrew cognate, but functional-parallel** — Akkadian *awīlūtu* 'humankind' (Adapa B:50 *mār ša awīluti*) is functional-parallel to Hebrew *bnei Adam* 'sons of Adam'. Documented in the rationale of `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus`.

### Akkadian-Sumerian internal sibling clusters new at this pass

- **Šūtu / IM.U18.LU** — Akkadian *Šūtu* and the Sumerian logographic-equivalent *IM.U18.LU* (Sumerian *u18-lu* 'south'). The four-cardinal-winds tradition is Sumerian-Akkadian shared. The new central entry `shutu-cardinal-winds-akkadian-four-winds-divinized-cross-corpus`.
- **Apkallu / abgal** — Akkadian *apkallu* is the Sumerian-loanword from *abgal* 'great sage'. The seven-antediluvian-sages tradition is Sumerian-Akkadian shared. The new central entry `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus`.
- **Ṣalmāt qaqqadi / saĝ gig-ga** — Akkadian *ṣalmāt qaqqadi* is the word-by-word semantic-calque of Sumerian *saĝ gig-ga* (both 'black-headed people'). Existing central entry `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus` extended with Akkadian-side activation at ADP-WOH-A:13.

### Project-wide Akkadian-pipeline conventions ratified at this pass

- **The DINGIR-prefix prose-drop convention extends to Akkadian.** Existing central entry `dingir-prefix-prose-drop-convention` already governs Akkadian (per the rationale documenting the project-wide application); this pass confirms the convention's deployment across 31 Akkadian Adapa-text DINGIR-attestations.
- **The lacuna-bracket convention extends to Akkadian.** Existing central entry `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` is here extended with 18 Adapa-text refIds.
- **The verification-pending disclosure convention is new at this pass** for Akkadian-source texts where best-effort reconstruction precedes the verification-pass against the modern critical edition. Documented in overlay `verification-pending-disclosure-adapa-akkadian`. The convention will scale to subsequent Akkadian texts where the critical-edition verification is similarly pending.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible scholarly modern-English rendering in the Foster / Izre'el / Heidel register. The lens lives in the apparatus (commentary + glossary entries), not in the translated English. Every glossary entry has all required fields, correct claim_type, and rationale that a scholar of Akkadian (or Sumerian, or Hebrew, where the cross-corpus links apply) would recognize as serious work. The bidirectional sibling-cluster wiring establishes the project's first comprehensive Akkadian-source cross-corpus apparatus.

The 13 new central entries + 9 new overlay entries collectively constitute the project's foundational **Akkadian-source lost-immortality vocabulary base**, with cross-corpus reach into Sumerian (apkallu, abzu/Apsû, ṣalmāt qaqqadi / saĝ gig-ga, IM.U18.LU / Šūtu, DINGIR / ilum, an-enlil-quartet / Anu-Ea axis, seven-day-cosmic-marker, zi da-ri2 / napištu dārītu) and Hebrew (Gen 2-3 Eden inverse-parallel, Ezek 8:14 Tammuz, Deut 32:17 shedim, Ps 2:4 sahaq, Num 6:25 favor-face, Gen 5:24 Hanokh ascent, 2 Kgs 2:11 Elijah ascent, Gen 3:19 dust-mortality verdict). The conventions ratified at Enki and Ninmaḫ and Flood Story (lacuna-bracket; DINGIR-prefix-prose-drop; sh-digraph anglicization; manuscript-variant-inline-rendering) extend to Akkadian without modification; the **verification-pending disclosure convention** is new at this pass for Akkadian-source texts.

The composition has **zero `claim_type=speculative` entries**; this Editor pass does not require human sign-off on speculative claims. Standard human Reviewer sign-off applies. The Editor's working principle on the eight major lens-risk concentrations identified at intake (Ea-deception crux; food-of-life cross-corpus; wisdom-but-not-immortality; speech-act efficacy; ascent-to-heaven; Adapa-as-Adam DISAVOW; Dumuzi-Tammuz-Adonis dying-and-rising-god cross-corpus; wind/cardinal-direction vocabulary) was the **accuracy-above-lens** discipline with explicit operational disavowals at each high-risk concentration. The disavowals are surfaced in the rationale of the respective central entries — most prominently in `ea-warning-deception-misadvice-test-crux-cross-corpus`, `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus`, `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus`, `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus`, `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus`, `nemequ-napishtu-dariti-wisdom-but-not-immortality-paradigm-sage-cross-corpus`, and `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus`.

The chapter's verification-pending status is preserved unchanged; the Reviewer agent and downstream verification-pass should re-check sign-level transliteration against Izre'el 2001's critical edition. The lens-discipline and glossary work is independent of and complementary to the sign-level verification — both pipelines should converge at the Reviewer pass.
