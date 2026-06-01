# Chapter 1 Editor Report — The Flood Story (ETCSL 1.7.4)

## Overview

The Wheel of Heaven Translation Program's **second Mesopotamian text** and the foundational Sumerian flood-narrative bridging the Mesopotamian and Hebrew flood-traditions. **89 preserved lines across 5 segments (A-E)** separated by 4 inter-segment lacunae and an opening lacuna (~173 lines lost; ~34% of the composition preserved). The Translator submitted 44 `editorial_questions[]`; this Editor pass resolves every one (either folded into a glossary entry or surfaced in commentary) and clears the array.

This pass extends the Sumerian-source conventions ratified at Enki and Ninmah (the project's first Mesopotamian text) and wires the project's **most-developed three-way Sumerian-Akkadian-Hebrew cross-corpus sibling-clusters** to date — including the flood-vocabulary cluster, the flood-vessel cluster, the boat-window cluster, the oath-by-life-of-heaven-and-earth cluster, the apotheosis-of-the-flood-survivor cluster, the antediluvian-cities cluster, the kingship-descended-from-heaven cluster, the post-flood-thanksgiving-sacrifice cluster, the Dilmun-eastern-paradise cluster, and several others. The pass is the project's **most cross-corpus-rich Mesopotamian Editor pass** to date.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.glossaryVersion`: `2.52.0` → `2.53.0`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0`

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bump: 2.52.0 → 2.53.0.** `sourceLanguages` continues `["he", "sux"]` (extended at the Enki and Ninmah pass). Total terms: 566 → 592 (26 new central entries added).

**26 new central entries** (all foundational cross-corpus flood-narrative vocabulary with Hebrew↔Sumerian↔Akkadian three-way reach):

1. `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus` (claim_type: `direct`) — the foundational five-tradition flood-survivor-name-cluster (Sumerian *Ziusudra* / Akkadian *Atra-ḫasīs* / Akkadian *Ūta-napishtim* / Greek *Xisouthros* / Hebrew *Noach*); five distinct etymological roots for the same character; bidirectional sibling-links to the existing Hebrew Noah-cluster entries.
2. `a-ma-ru-abubu-mabbul-great-flood-vocabulary-cross-corpus` (claim_type: `direct`) — the three-way flood-vocabulary cluster; Akkadian *abūbu* and Hebrew *mabbul* are arguably etymologically-cognate Semitic (Driver / Westermann / Tsumura) — debate documented; the Sumerian *a-ma-ru* is comparative-thematic.
3. `ma-gur-eleppu-tevah-flood-vessel-cross-corpus` (claim_type: `direct`) — the three-way flood-vessel cluster; the three lexemes are **not** philologically cognate (Sumerian *ma2*, Akkadian *eleppu* Sumerian-loanword, Hebrew *tevah* Egyptian-loanword); three distinct hull-form-specifications.
4. `ab-bur-aptu-chalon-ha-tevah-flood-boat-window-cross-corpus` (claim_type: `direct`) — the boat-window aperture-trope; cross-corpus Gilgamesh XI.135-136 (*aptu*) and Gen 8:6 (*chalon ha-tevah*).
5. `nam-lugal-an-ta-ed-de-a-ba-kingship-descended-from-heaven-cross-corpus` (claim_type: `direct`) — THE Sumerian King List opening-formula; the foundational antediluvian-kingship Mesopotamian-tradition keyword. Will recur in the next major project translation (the Sumerian King List ETCSL 2.1.1).
6. `five-antediluvian-cities-eridug-bad-tibira-larag-zimbir-shuruppag-cross-corpus` (claim_type: `direct`) — the canonical Sumerian antediluvian-cities pentad; cross-corpus the Sumerian King List antediluvian-section, the Berossus-tradition, and the Apkallu-tradition. **Architectural decision**: housed as a single central entry rather than per-city; per-city detail (Pabilsaĝ, Šuruppag) sits in overlay entries.
7. `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus` (claim_type: `direct`) — the Sumerian self-designation for humanity; the corpus-wide ethnonymic-counterpart to the abstract-collective `nam-lu2-ulu3`.
8. `im-hul-imhullu-destructive-storm-wind-mesopotamian-storm-vocabulary-cross-corpus` (claim_type: `direct`) — the Sumerian-Akkadian destructive-storm vocabulary (one of the diagnostic Sumerian → Akkadian loanwords); cross-corpus Enuma Elish IV.96 (Marduk's evil-wind weapon) and Hebrew *ruach ra'ah*.
9. `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus` (claim_type: `direct`) — **one of the most-cited cross-corpus Mesopotamian-Hebrew flood-tradition diagnostics** — the Mesopotamian-7 vs Hebrew-40 transformation; the Hebrew tradition multiplies the Mesopotamian seven by approximately six.
10. `zi-an-na-zi-ki-a-nish-ilim-oath-by-life-of-heaven-and-earth-cross-corpus` (claim_type: `direct`) — the three-way Sumerian-Akkadian-Hebrew oath-formula cluster; bidirectional sibling-links to the existing Hebrew central entry `chei-x-oath-by-the-life-formula`. Reception-history extends through Matt 5:34-35.
11. `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus` (claim_type: `direct`) — the Mesopotamian apotheosis-of-the-flood-survivor; cross-corpus Hebrew Hanokh-translation (Gen 5:24) and Eliyahu-whirlwind-ascent (2 Kgs 2:11); the Mesopotamian-apotheosis is conspicuously absent at the Hebrew flood-narrative (Noah dies a natural death).
12. `dilmun-eastern-paradise-cross-corpus` (claim_type: `direct`) — Dilmun as the eastern-paradise destination of Ziusudra; cross-corpus the Enki-and-Ninhursag composition (ETCSL 1.1.1 — the Dilmun-paradise-text); cross-corpus Hebrew Gan-Eden Gen 2:8 (*mi-qedem* — in the east). **Explicit operational disavowals** against (i) Christian Eden-typology pre-resolution; (ii) the Sitchin-corpus *Dilmun-as-spaceport* and *Anunnaki-installation* readings.
13. `di-til-la-puhrum-irrevocability-of-divine-assembly-decree-cross-corpus` (claim_type: `direct`) — the foundational Sumerian-Akkadian divine-assembly-decree irrevocability formula; cross-corpus Atrahasis I.iv, Enuma Elish III-IV; Hebrew *sod YHWH* (Jer 23:18, Job 1:6, Ps 89:8) and Isa 14:24-27.
14. `iz-zi-da-kikkish-talking-through-the-wall-to-keep-an-oath-flood-trope-cross-corpus` (claim_type: `direct`) — the **most-cited cross-corpus Mesopotamian-flood-tradition diagnostic** — the through-the-wall-warning-to-keep-the-oath-of-silence trope; cross-corpus Atrahasis III.i.20 and Gilgamesh XI.21-22 (*kikkiš kikkiš igâru igâru*).
15. `post-flood-thanksgiving-sacrifice-trope-cross-corpus` (claim_type: `direct`) — the post-flood thanksgiving-sacrifice; **one of the most-cited Mesopotamian-Hebrew comparative-mythology parallels** with direct Hebrew-Akkadian lexical-cognation (*reiach ha-nichoach* ↔ *erīša ṭāba* 'sweet savor').
16. `divine-decree-to-destroy-humankind-flood-trope-cross-corpus` (claim_type: `direct`) — the divine-decree-to-destroy-humankind cross-corpus; the Mesopotamian-Hebrew shift (demographic / noise cause → moral / ethical cause) documented.
17. `utu-shamash-sun-god-justice-divinity-cross-corpus` (claim_type: `direct`) — the Sumerian-Akkadian sun-god; cross-corpus Hebrew *shemesh*, *Beit Shemesh*, *Ein Shemesh* cult-names. The project's **first central glossary entry on a specific Sumerian-Akkadian divinity** (the existing `an-enlil-nudimmud-cosmic-triad-cross-corpus` is a triad-noun-phrase, not a single-divinity entry); the pattern scales to subsequent Mesopotamian texts.
18. `giri-ki-su-ub-appa-labanu-prostration-gesture-cross-corpus` (claim_type: `direct`) — the three-way prostration-gesture cluster (Sumerian *giri17 ki su-ub* / Akkadian *appa labānu* / Hebrew *shachah apayim artzah*); all three deploy the *nose / face at the ground* body-part metaphor.
19. `nu-gig-high-status-woman-sacred-class-cross-corpus` (claim_type: `direct`) — the Sumerian high-status / sacred-class woman; bidirectional sibling-cluster with the existing Hebrew central entries `qedeshah-consecrated-woman-sacred-prostitution-crux` and `zonah-prostitute-status-vocabulary-cross-corpus`. The Mesopotamian-Hebrew shared modern-scholarly deprecation of the older 'sacred prostitute' translation documented; the project follows the revisionist reading (Assante 1998, Budin 2008).
20. `an-enlil-enki-ninhursaga-flood-council-quartet-cross-corpus` (claim_type: `direct`) — the Mesopotamian flood-decision divine-council quartet; cross-corpus Atrahasis I.i and Gilgamesh XI.14-19; complements the existing `an-enlil-nudimmud-cosmic-triad-cross-corpus` (the triad-context). The Mesopotamian-quartet → Hebrew-singular shift documented.
21. `nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-cross-corpus` (claim_type: `direct`) — **promoted to central** from the prior Enki-and-Ninmaḫ overlay-entry (`ninmah-ninhursaga-nintud-birth-goddess-epithet-cluster`). The cluster recurs across multiple Mesopotamian texts; the multi-text recurrence is the architectural-criterion for the central placement.
22. `ma-mu-nu-me-a-not-a-dream-waking-revelation-cross-corpus` (claim_type: `direct`) — the waking-revelation / not-a-dream trope; cross-corpus Atrahasis III.i.13-15, Gilgamesh XI.20-31, and Hebrew Num 12:6-8 (Yahweh's prophetic-revelation hierarchy).
23. `enki-deliberates-in-his-own-heart-wisdom-god-private-deliberation-cross-corpus` (claim_type: `direct`) — Enki's private-deliberation trope; cross-corpus Hebrew Yahweh-deliberations at Gen 6:6 (*va-yit'atzev el libbo*) and Gen 18:17 (*ha-mekhasse ani me-Avraham*).
24. `inana-laments-her-people-flood-divine-feminine-lament-cross-corpus` (claim_type: `direct`) — Inana's lament-for-her-people; cross-corpus the wider Sumerian city-lament tradition (ETCSL 2.2.x); cross-corpus Hebrew Jer 31:15 (Rachel-weeping-for-her-children) and Matt 2:18.
25. `preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus` (claim_type: `direct`) — Ziusudra's preservation-aitia; cross-corpus Atrahasis III.vi (*zēr napišti*), Gilgamesh XI.193-195, Hebrew Gen 7:3 and 9:1-7 (the *peru u-revu* post-flood-blessing); the Mesopotamian apotheosis-reward → Hebrew mortal-blessing-reward transformation documented.
26. `zi-da-ri-balatu-daru-eternal-life-cross-corpus` (claim_type: `direct`) — the eternal-life formula; Sumerian *da-ri2* is the direct source of the Akkadian-loanword *dārû*; cross-corpus Hebrew *chayei olam* (Dan 12:2) and the wider *olam* eternal-modifier (`brit-olam`).

**16 existing Hebrew central entries received bidirectional sibling-references** to the new Sumerian central entries (modifications appended to existing entries' rationale prose; no `wohChoice` or `appliesTo` changes):

- `tevah` — back-reference to `ma-gur-eleppu-tevah-flood-vessel-cross-corpus`, `ab-bur-aptu-chalon-ha-tevah-flood-boat-window-cross-corpus`, `preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus`.
- `mabbul` — back-reference to `a-ma-ru-abubu-mabbul-great-flood-vocabulary-cross-corpus`, `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus`, `divine-decree-to-destroy-humankind-flood-trope-cross-corpus`.
- `noach-vayithallech` — back-references to `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus`, `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus`, `enki-deliberates-in-his-own-heart-wisdom-god-private-deliberation-cross-corpus`.
- `noah-yenachmenu` — back-reference to `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus`.
- `vayisha-er-noach` — back-references to `post-flood-thanksgiving-sacrifice-trope-cross-corpus`, `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus`.
- `peru-urevu-postflood` — back-references to `preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus`, `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus`.
- `ish-ha-adamah-noach` — back-references to `post-flood-thanksgiving-sacrifice-trope-cross-corpus`, `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus`.
- `vayyiqetz-noach` — back-reference to `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus`.
- `chei-x-oath-by-the-life-formula` — back-reference to `zi-an-na-zi-ki-a-nish-ilim-oath-by-life-of-heaven-and-earth-cross-corpus`.
- `gan-be-eden` — back-reference to `dilmun-eastern-paradise-cross-corpus`.
- `eretz-nod-qidmat-eden` — back-reference to `dilmun-eastern-paradise-cross-corpus`.
- `eretz` — back-reference to the existing `kalam-ka-na-ag-the-land-cross-corpus` (Enki and Ninmaḫ Editor pass had established the cross-corpus link; this pass surfaces the back-reference on the Hebrew side).
- `qedeshah-consecrated-woman-sacred-prostitution-crux` — back-reference to `nu-gig-high-status-woman-sacred-class-cross-corpus`.
- `zonah-prostitute-status-vocabulary-cross-corpus` — back-reference to `nu-gig-high-status-woman-sacred-class-cross-corpus`.
- `havah-li-banim-rachel-cry` — back-reference to `inana-laments-her-people-flood-divine-feminine-lament-cross-corpus`.
- `brit-olam` — back-reference to `zi-da-ri-balatu-daru-eternal-life-cross-corpus`.

**Bidirectional cross-references verified.** Each new Sumerian central entry that references an existing Hebrew central entry by id has had the corresponding back-reference added to the Hebrew entry's rationale prose in the same edit.

### Per-translation overlay glossary (`data-library/flood-story-woh/_translation-glossary.json`)

**Version bump: 1.0.0 → 1.1.0**.

**12 new overlay entries** (all composition-specific philological cruxes and Flood-Story-singular vocabulary; cross-corpus foundational vocabulary went to the central glossary):

1. `men-gu-za-nam-lugal-crown-and-throne-of-kingship-regalia-formula` (claim_type: `direct`) — the regalia-couplet at FLS-WOH-B:7; functional-parallel to Hebrew *keter* + *kisse melekh*.
2. `kab-dug-ga-ba-hal-hal-la-allotment-by-gauged-measure-city-founding-formula` (claim_type: `direct`) — the city-foundation inclusio formula at FLS-WOH-B:10 and B:16.
3. `pabilsag-bowman-deity-larag-founder-divinity` (claim_type: `direct`) — Larag's tutelary deity (associated with the late-Mesopotamian zodiacal-Sagittarius).
4. `shuruppag-ziusudras-city` (claim_type: `direct`) — Ziusudra's home-city; cross-corpus Gilgamesh XI.11 and the Sumerian Instructions of Shuruppak (ETCSL 5.6.1).
5. `gudug-priest-mesopotamian-temple-office` (claim_type: `direct`) — the Mesopotamian priestly-office; the priest-king dual-office parallels Hebrew Melchizedek (Gen 14:18-20).
6. `si-si-ig-gale-wind-storm-vocabulary` (claim_type: `direct`) — the gale-wind paired with *im-ḫul* in the storm-vocabulary at FLS-WOH-D:1.
7. `dub-shade-refresh-vs-tremble-crux` (claim_type: `direct`) — the *dub2* lexical-crux at FLS-WOH-A:5 (refresh-vs-tremble).
8. `ki-eshbar-place-of-divine-decision` (claim_type: `direct`) — the oracular-decision-place at FLS-WOH-A:7.
9. `dag-me-a-our-dwelling-places-c22-crux` (claim_type: `direct`) — the partially-obscure *DAG-me-a* sign-cluster at FLS-WOH-C:22.
10. `me-te-edin-fitting-attribute-of-open-country` (claim_type: `direct`) — the fittingness-aesthetic-cosmology formula at FLS-WOH-A:14.
11. `numun-nam-lu-ulu-seed-of-humankind-c23` (claim_type: `direct`) — the seed-of-humankind phrase at FLS-WOH-C:23 and E:10.
12. `title-and-meta-conventions-flood-story` (claim_type: `direct`) — the chapter-title-and-subtitle convention.

## Resolution of the 44 editorial_questions

The Translator submitted 44 editorial_questions; all are resolved as follows.

**Convention questions (already-ratified Enki-and-Ninmaḫ overlay conventions applied):**
- FLS-WOH-A:0 (lacuna-bracket convention for multi-segment fragmentary texts) → `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (overlay; ratified at Enki and Ninmaḫ; extended without modification to this composition's five inter-segment lacunae)
- FLS-WOH-B:13 (manuscript-variant «ḫur» rendering) → `manuscript-variant-inline-rendering-convention` (overlay; ratified at Enki and Ninmaḫ; applied silently per convention)
- FLS-WOH-A:0 (chapter-title convention) → `title-and-meta-conventions-flood-story` (overlay)

**Foundational central-glossary cross-corpus entries (the project's most cross-corpus-rich Mesopotamian Editor pass):**
- FLS-WOH-A:3 (Nintur birth-goddess epithet-cluster) → `nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-cross-corpus` (CENTRAL — promoted from overlay)
- FLS-WOH-A:5 (dub2 refresh-vs-tremble crux) → `dub-shade-refresh-vs-tremble-crux` (overlay)
- FLS-WOH-A:7 (ki-eš-bar restoration) → `ki-eshbar-place-of-divine-decision` (overlay)
- FLS-WOH-A:9 (ĝarza me maḫ creation-summary) → folded into commentary; uses existing `me-sumerian-divine-offices-cosmic-functions` central entry
- FLS-WOH-A:11 (divine quartet An, Enlil, Enki, Ninhursaĝa) → `an-enlil-enki-ninhursaga-flood-council-quartet-cross-corpus` (CENTRAL)
- FLS-WOH-A:12 (saĝ gig2-ga black-headed people) → `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus` (CENTRAL)
- FLS-WOH-A:14 (me-te fitting attribute of open country) → `me-te-edin-fitting-attribute-of-open-country` (overlay)
- FLS-WOH-B:4 (du-lum toil-relief) → folded into commentary; uses existing `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` central entry
- FLS-WOH-B:6 (nam-lugal an-ta ed3-de3 kingship descended) → `nam-lugal-an-ta-ed-de-a-ba-kingship-descended-from-heaven-cross-corpus` (CENTRAL)
- FLS-WOH-B:7 (men maḫ ĝišgu-za regalia) → `men-gu-za-nam-lugal-crown-and-throne-of-kingship-regalia-formula` (overlay)
- FLS-WOH-B:10 (kab dug4-ga allotment-by-gauged-measure) → `kab-dug-ga-ba-hal-hal-la-allotment-by-gauged-measure-city-founding-formula` (overlay)
- FLS-WOH-B:11 (five antediluvian cities pentad) → `five-antediluvian-cities-eridug-bad-tibira-larag-zimbir-shuruppag-cross-corpus` (CENTRAL)
- FLS-WOH-B:11 (Nudimmud Enki-epithet) → folded into commentary; uses existing `an-enlil-nudimmud-cosmic-triad-cross-corpus` central entry
- FLS-WOH-B:12 (nu-gig high-status woman) → `nu-gig-high-status-woman-sacred-class-cross-corpus` (CENTRAL)
- FLS-WOH-B:13 (Pabilsaĝ) → `pabilsag-bowman-deity-larag-founder-divinity` (overlay)
- FLS-WOH-B:14 (Zimbir/Sippar/Utu) → `utu-shamash-sun-god-justice-divinity-cross-corpus` (CENTRAL)
- FLS-WOH-B:15 (Šuruppag/Sud) → `shuruppag-ziusudras-city` (overlay)
- FLS-WOH-C:7 (Inana laments her people) → `inana-laments-her-people-flood-divine-feminine-lament-cross-corpus` (CENTRAL)
- FLS-WOH-C:8 (Enki private deliberation) → `enki-deliberates-in-his-own-heart-wisdom-god-private-deliberation-cross-corpus` (CENTRAL)
- FLS-WOH-C:11 (Ziusudra-Atrahasis-Utnapishtim-Noach name cluster) → `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus` (CENTRAL)
- FLS-WOH-C:11 (gudug-priest) → `gudug-priest-mesopotamian-temple-office` (overlay)
- FLS-WOH-C:15 (ma-mu2 nu-me-a not-a-dream) → `ma-mu-nu-me-a-not-a-dream-waking-revelation-cross-corpus` (CENTRAL)
- FLS-WOH-C:19 (iz-zi-da/kikkiš talking-through-the-wall trope) → `iz-zi-da-kikkish-talking-through-the-wall-to-keep-an-oath-flood-trope-cross-corpus` (CENTRAL)
- FLS-WOH-C:22 (DAG-me-a sign-crux) → `dag-me-a-our-dwelling-places-c22-crux` (overlay)
- FLS-WOH-C:23 (divine-decree-to-destroy-humankind) → `divine-decree-to-destroy-humankind-flood-trope-cross-corpus` (CENTRAL) + `numun-nam-lu-ulu-seed-of-humankind-c23` (overlay)
- FLS-WOH-C:24 (di-til-la/puḫrum irrevocability) → `di-til-la-puhrum-irrevocability-of-divine-assembly-decree-cross-corpus` (CENTRAL)
- FLS-WOH-D:1 (im-ḫul/imḫullu destructive storm) → `im-hul-imhullu-destructive-storm-wind-mesopotamian-storm-vocabulary-cross-corpus` (CENTRAL)
- FLS-WOH-D:1 (si-si-ig gale-wind) → `si-si-ig-gale-wind-storm-vocabulary` (overlay)
- FLS-WOH-D:3 (seven-day flood vs forty-day) → `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus` (CENTRAL)
- FLS-WOH-D:5 (ma2 gur4-gur4/eleppu/tevah flood-vessel) → `ma-gur-eleppu-tevah-flood-vessel-cross-corpus` (CENTRAL)
- FLS-WOH-D:6 (Utu's post-storm sunrise) → folded into commentary; uses `utu-shamash-sun-god-justice-divinity-cross-corpus` central entry
- FLS-WOH-D:7 (ab-BUR2/aptu/chalon ha-tevah window) → `ab-bur-aptu-chalon-ha-tevah-flood-boat-window-cross-corpus` (CENTRAL)
- FLS-WOH-D:10 (giri17 ki su-ub/appa labanu prostration) → `giri-ki-su-ub-appa-labanu-prostration-gesture-cross-corpus` (CENTRAL)
- FLS-WOH-D:11 (post-flood thanksgiving sacrifice) → `post-flood-thanksgiving-sacrifice-trope-cross-corpus` (CENTRAL)
- FLS-WOH-E:1 (oath by life of heaven and earth) → `zi-an-na-zi-ki-a-nish-ilim-oath-by-life-of-heaven-and-earth-cross-corpus` (CENTRAL)
- FLS-WOH-E:7 (til3 diĝir-gin7 apotheosis) → `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus` (CENTRAL)
- FLS-WOH-E:8 (zi da-ri2/balāṭu dārû eternal life) → `zi-da-ri-balatu-daru-eternal-life-cross-corpus` (CENTRAL)
- FLS-WOH-E:10 (preservation aitia for apotheosis) → `preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus` (CENTRAL)
- FLS-WOH-E:11 (Dilmun eastern paradise) → `dilmun-eastern-paradise-cross-corpus` (CENTRAL)
- FLS-WOH-E:12 (closing-fragment, possible doxology) → folded into commentary; uses existing `za-mi-doxological-praise-formula-sumerian-cross-corpus` central entry

**Minor commentary-only resolutions:**
- FLS-WOH-A:1 (subject of im-ĝa2-ĝa2) → surface keeps the vague-subject reading; commentary explains the unrecoverable subject
- FLS-WOH-A:2 (verbal continuation unrecoverable) → surface preserves divine first-person-resolve; commentary frames the *ḫa-lam* foreshadowing of FLS-WOH-C:23
- FLS-WOH-A:0 (lacuna-rendering convention) → ratified at Enki and Ninmaḫ; extended to this composition's five lacunae without modification

## Speculative entries requiring sign-off

**None.** This Editor pass produced zero `claim_type=speculative` entries.

The Editor's working principle on this composition was the project's *accuracy-above-lens* discipline. Every divergence from the standard scholarly reading is documented as named-scholarship (Foster, Civil, Jacobsen, Lambert-Millard, George, Hallo, Wenham, Sarna, Westermann, Heidel, Cassuto, Tsumura, Walton, Cross, Smith, Heiser, etc.); no WoH-distinctive synthesis is surfaced in the translation or glossary entry rationales. The translation's surface reads as a defensible scholarly modern-English rendering in the Foster / Civil / Black et al. register. The Wheel of Heaven lens is reserved for the wiki and methodology pages.

**Five places where the Editor could have introduced speculative readings but did not, with explicit operational disavowals:**

1. **Ziusudra-as-Sitchin-style-spaceship-pilot reading.** The flood-survivor-name-cluster (Sumerian *Ziusudra* / Akkadian *Atra-ḫasīs* / Akkadian *Ūta-napishtim* / Hebrew *Noach*) has been heavily-deployed in Sitchin-corpus and successor-literature with interpretive overlays asserting a literal-extraterrestrial-rescue narrative. The Editor's choice was to surface the standard scholarly philological-analysis of the names as comparative-mythology cluster — *thematic-and-narrative* parallel across traditions, not *etymological-cognate* sibling-cluster — and to explicitly note in the entry's rationale that the names are *conceptually-related across traditions, not lexically-cognate*. No WoH-distinctive synthesis on the surface or in the glossary rationale.

2. **Dilmun-as-spaceport reading.** The Dilmun-eastern-paradise complex is heavily-deployed in popular-fringe and ancient-astronaut literature (the Sitchin *DUR.AN.KI as launch-facility* reading; the *Anunnaki installation* reading; the *Dilmun-as-Eden-and-Eden-as-extraterrestrial-base* readings). The Editor's choice was to surface the standard scholarly philological-archaeological-and-comparative-mythology analysis — Dilmun is the Bahrain archipelago in the historical-archaeological geography; *the place where Utu rises* is the cosmographic-eastern-orientation; the Edenic-paradise readings are the comparative-mythology tradition documented in named-scholarship. The new central entry `dilmun-eastern-paradise-cross-corpus` carries **explicit verbatim operational disavowals** against the popular-fringe readings.

3. **Apotheosis-as-literal-translation-to-spaceship reading.** The *til3 diĝir-gin7* and *zi da-ri2* apotheosis-trope at FLS-WOH-E:7-8 has the same popular-fringe reception (the *Anunnaki-took-the-king-up-to-the-spaceship* reading; the Hanokh-as-pilot reading). The Editor's choice was to present the apotheosis-trope as **divinely-granted-immortality of a uniquely-righteous-or-favored human** — the *taken-up-to-the-gods'-realm* spatial-language as theological-mythological, not literal-physical-translation. The new central entry `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus` carries **explicit operational disavowals**.

4. **Five-antediluvian-cities-as-pre-flood-civilization-evidence reading.** The five-cities-pentad has been deployed in lost-civilization literature as evidence for a pre-flood global civilization. The Editor's choice was to present the pentad as the canonical Sumerian-tradition antediluvian-cities-list with archaeological-historical identifications (Eridu = Tell Abu Shahrein; Sippar = Tell Abu Habbah; Šuruppak = Tell Fara) and as cross-corpus comparative-mythology against the Hebrew Cainite-cities Gen 4:17-22 and the Berossus-tradition. No pre-flood-global-civilization synthesis.

5. **Anuna / Anunnaki ancient-astronaut popular-tradition.** As at the Enki-and-Ninmaḫ Editor pass, the popular *Anunnaki*-as-extraterrestrial-civilization-readings are deployed in Sitchin-corpus and successor-literature. The Editor's choice continues the prior pass's discipline: the popular *Anunnaki* form-variation is documented; the ancient-astronaut interpretive overlays are reserved for the wiki and broader-corpus discussions, not preempted by the translation-glossary entry. The lens lives in the apparatus, not in the translation-glossary-rationale prose.

## Unresolved editorial questions

**None.** All 44 editorial questions are resolved. The `editorial_questions[]` array is empty in the chapter-1.json output.

## Items flagged for future cross-corpus wiring (not blocking this pass)

These are wiring-tasks for future Editor passes; they do not block the current pass's sign-off.

1. **Akkadian foundational entries (Atraḫasīs / Enūma Eliš / Gilgameš XI).** When the project translates Atraḫasīs and Enūma Eliš, the foundational Akkadian vocabulary will receive central entries: *abūbu* (flood); *eleppu* (boat); *aptu* (window); *kīma ilāni* (like the gods); *balāṭu dārû* (eternal life); *nīš ilī* (oath by the life of the gods); *puḫru ilāni* (divine assembly); *imḫullu* (destructive wind); *kikkiš igâru* (reed-wall, wall); *erīša ṭāba* (sweet savor); *ṣalmāt qaqqadi* (black-headed people); *Anu* / *Ea* / *Šamaš* / *Bēlet-ilī* (divinity-names). Each should be wired bidirectionally to (i) the Sumerian-source central entries from this pass; (ii) the Hebrew-source central entries on the corresponding lexemes; (iii) the existing Genesis-WoH central entries where applicable. The architecture established here generalizes directly.

2. **Sumerian King List (ETCSL 2.1.1) — next project priority.** The foundational central entry `nam-lugal-an-ta-ed-de-a-ba-kingship-descended-from-heaven-cross-corpus` is established here for the Sumerian King List's opening formula; the King List's antediluvian-cities-section will deploy the existing `five-antediluvian-cities-eridug-bad-tibira-larag-zimbir-shuruppag-cross-corpus` central entry; the King List's antediluvian-kings (the long-lived antediluvian rulers — Alulim, Alalgar, Etana, etc.) will need new central entries on the apkallu-and-antediluvian-king tradition. Cross-corpus to Hebrew Gen 5 antediluvian-genealogy.

3. **Hebrew *goral* central entry.** As flagged at Enki and Ninmaḫ — the cross-corpus link between Sumerian *nam / nam tar* and Hebrew *goral* (lot, portion) is documented at `nam-sumerian-destiny-fate-cross-corpus`; the Hebrew *goral* lexeme does not yet have its own central entry. The present pass also leaves the cross-corpus link between the Sumerian *kab dug-ga* allotment-by-gauged-measure formula and the Hebrew *goral* tradition flagged. Future Genesis-WoH or Job-WoH Editor pass should produce the *goral* central entry with bidirectional back-reference.

4. **Hebrew *sod YHWH* central entry.** The cross-corpus link between Sumerian *pu-uḫ2-ru-um* / Akkadian *puḫru ilāni* and Hebrew *sod YHWH* (Jer 23:18; Ps 89:8) is documented in this pass at `di-til-la-puhrum-irrevocability-of-divine-assembly-decree-cross-corpus`; the Hebrew *sod YHWH* lexeme does not yet have its own central entry. Future Editor pass on a prophetic-corpus text (Jeremiah, Job) should produce the central entry with bidirectional back-reference.

5. **Hebrew *shachah / yishtachu apayim artzah* central entry.** The cross-corpus link to the Sumerian-Akkadian prostration-gesture is documented at `giri-ki-su-ub-appa-labanu-prostration-gesture-cross-corpus`; future Hebrew Editor pass on a patriarchal-prostration-scene (Gen 19:1, 33:6-7, 42:6, 1 Sam 25:23, 1 Sam 28:14) should produce the Hebrew central entry with bidirectional back-reference.

6. **Hebrew *yatzar* central entry.** As flagged at Enki and Ninmaḫ — the cross-corpus link to Sumerian *dim2* is documented at `im-sumerian-clay-of-human-creation-cross-corpus`; future Editor pass on Gen 2:7 / Jer 18 / Isa 64:7 should produce the Hebrew central entry.

7. **Hebrew *Har ha-Bayit / Tzion* central entry.** As flagged at Enki and Ninmaḫ.

8. **The Enki-and-Ninmaḫ overlay-entry `ninmah-ninhursaga-nintud-birth-goddess-epithet-cluster`** is **superseded** by this pass's promotion to central (`nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-cross-corpus`). The overlay entry will be flagged as superseded in the Enki-and-Ninmaḫ overlay glossary in a future routine-maintenance pass (no functional impact on the Enki-and-Ninmaḫ chapter pending — the overlay entry continues to govern the per-chapter occurrences via `appliesTo`).

## Cross-corpus bidirectional sibling-cluster summary

This Editor pass wires the project's **most extensive three-way Sumerian-Akkadian-Hebrew cross-language sibling-clusters** to date. The bidirectional links are verified in both directions on every cross-corpus central entry that references an existing Hebrew central entry.

### Three-way flood-vocabulary cluster
- **Sumerian *a-ma-ru* ↔ Akkadian *abūbu* ↔ Hebrew *mabbul*** — `a-ma-ru-abubu-mabbul-great-flood-vocabulary-cross-corpus` ↔ `mabbul`. The Hebrew *mabbul* and Akkadian *abūbu* are arguably Semitic-cognate (proto-Semitic √ybl); the Sumerian *a-ma-ru* is comparative-thematic.

### Three-way flood-vessel cluster
- **Sumerian *ma2 gur4-gur4* ↔ Akkadian *eleppu* ↔ Hebrew *tevah*** — `ma-gur-eleppu-tevah-flood-vessel-cross-corpus` ↔ `tevah`. The three lexemes are not philologically cognate; three distinct hull-form-specifications.

### Three-way boat-window cluster
- **Sumerian *ab-BUR2* ↔ Akkadian *aptu* ↔ Hebrew *chalon ha-tevah*** — `ab-bur-aptu-chalon-ha-tevah-flood-boat-window-cross-corpus` ↔ `tevah`. Thematic-narrative parallel; not lexical-cognate.

### Three-way oath-by-life-of-heaven-and-earth cluster
- **Sumerian *zi an-na zi ki-a* ↔ Akkadian *nīš ilī* / *nīš šamê u erṣetim* ↔ Hebrew *chay YHWH*** — `zi-an-na-zi-ki-a-nish-ilim-oath-by-life-of-heaven-and-earth-cross-corpus` ↔ `chei-x-oath-by-the-life-formula`. Reception-history extends through Matt 5:34-35.

### Three-way apotheosis cluster
- **Sumerian *til3 diĝir-gin7* ↔ Akkadian *kīma ilāni* ↔ Hebrew Hanokh-Eliyahu traditions** — `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus` ↔ `noach-vayithallech` ↔ `peru-urevu-postflood`. The Mesopotamian apotheosis is conspicuously absent at the Hebrew flood-narrative; the Hebrew tradition preserves the apotheosis-trope in the Hanokh and Eliyahu pericopes.

### Three-way eternal-life cluster
- **Sumerian *zi da-ri2* ↔ Akkadian *balāṭu dārû* ↔ Hebrew *chayei olam* / *brit olam*** — `zi-da-ri-balatu-daru-eternal-life-cross-corpus` ↔ `brit-olam`. The Akkadian *dārû* is a direct Sumerian-loanword from *da-ri2*.

### Three-way prostration-gesture cluster
- **Sumerian *giri17 ki su-ub* ↔ Akkadian *appa labānu* ↔ Hebrew *shachah apayim artzah*** — `giri-ki-su-ub-appa-labanu-prostration-gesture-cross-corpus`. All three deploy the *nose / face at the ground* body-part metaphor.

### Three-way destructive-storm cluster
- **Sumerian *im-ḫul* ↔ Akkadian *imḫullu* ↔ Hebrew *ruach ra'ah*** — `im-hul-imhullu-destructive-storm-wind-mesopotamian-storm-vocabulary-cross-corpus`. Akkadian *imḫullu* is a direct Sumerian-loanword; the Hebrew is comparative-thematic, not lexically-cognate.

### Three-way eastern-paradise cluster
- **Sumerian Dilmun (and Enki-and-Ninhursag ETCSL 1.1.1) ↔ Akkadian Utnapishtim-at-the-mouth-of-the-rivers (Gilgamesh XI.205-206) ↔ Hebrew Gan-Eden (Gen 2:8 *mi-qedem*)** — `dilmun-eastern-paradise-cross-corpus` ↔ `gan-be-eden` ↔ `eretz-nod-qidmat-eden`.

### Three-way divine-assembly-decree-irrevocability cluster
- **Sumerian *di-til-la inim puḫrum* ↔ Akkadian *puḫru ilāni* (Enuma Elish III-IV) ↔ Hebrew *sod YHWH* (Jer 23:18)** — `di-til-la-puhrum-irrevocability-of-divine-assembly-decree-cross-corpus`. Future Hebrew central entry `sod-yhwh-divine-council` will complete the bidirectional wiring.

### Mesopotamian-internal flood-narrative diagnostics (Sumerian-Akkadian)
- **`iz-zi-da-kikkish-talking-through-the-wall-to-keep-an-oath-flood-trope-cross-corpus`** — the most-cited Mesopotamian flood-tradition cross-corpus diagnostic (Atrahasis III.i.20, Gilgamesh XI.21-22).
- **`an-enlil-enki-ninhursaga-flood-council-quartet-cross-corpus`** — the flood-decision divine council across Sumerian Flood Story, Atrahasis I.i, Gilgamesh XI.14-19.
- **`enki-deliberates-in-his-own-heart-wisdom-god-private-deliberation-cross-corpus`** — the wisdom-god's private-deliberation; Mesopotamian flood-tradition cross-corpus + Hebrew Yahweh-deliberation Gen 6:6, 18:17.
- **`ma-mu-nu-me-a-not-a-dream-waking-revelation-cross-corpus`** — the waking-revelation form; Mesopotamian flood-tradition cross-corpus + Hebrew Num 12:6-8.
- **`divine-decree-to-destroy-humankind-flood-trope-cross-corpus`** — the destruction-decree; Mesopotamian flood-tradition cross-corpus + Hebrew Gen 6:5-13 (with the demographic → moral cause transformation).
- **`post-flood-thanksgiving-sacrifice-trope-cross-corpus`** — the post-flood sacrifice; one of the most-cited Mesopotamian-Hebrew comparative-mythology parallels with direct Hebrew-Akkadian lexical-cognation (*reiach ha-nichoach* ↔ *erīša ṭāba*).
- **`preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus`** — the preservation-aitia; Mesopotamian flood-tradition cross-corpus + Hebrew Gen 7:3, 9:1-7.
- **`seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus`** — the Mesopotamian-7-vs-Hebrew-40 transformation; one of the most-cited cross-corpus diagnostics.

### Project-wide Mesopotamian vocabulary clusters
- **`sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus`** — the Sumerian-Akkadian self-designation; sibling-cluster with `nam-lu2-ulu3-sumerian-humankind-cross-corpus`; functional-parallel to Hebrew *bnei Adam*.
- **`utu-shamash-sun-god-justice-divinity-cross-corpus`** — the Sumerian-Akkadian sun-god; functional-parallel to Hebrew *shemesh* cult-name fossils.
- **`nu-gig-high-status-woman-sacred-class-cross-corpus`** — the high-status / sacred-class woman; bidirectional sibling-cluster with the Hebrew `qedeshah` and `zonah` class-terms; modern-scholarly deprecation of *sacred prostitution* construct documented and followed.
- **`inana-laments-her-people-flood-divine-feminine-lament-cross-corpus`** — divine-feminine-lament-for-her-people; cross-corpus the Sumerian city-lament tradition; sibling to Hebrew Rachel-weeping `havah-li-banim-rachel-cry`.
- **`nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-cross-corpus`** — promoted from overlay; the Sumerian birth-goddess function across multiple epithets and cult-names.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible scholarly modern-English rendering in the Foster / Civil / Black et al. register. The lens lives in the apparatus (commentary + glossary entries), not in the translated English. Every glossary entry has all required fields, correct claim_type, and rationale that a scholar of Sumerian (or Akkadian, or Hebrew, where the cross-corpus links apply) would recognize as serious work. The bidirectional sibling-cluster wiring establishes the project's most-extensive cross-corpus Mesopotamian-Hebrew flood-narrative apparatus to date.

The 26 new central entries + 12 new overlay entries collectively constitute the project's foundational flood-narrative-vocabulary base. The conventions ratified at Enki and Ninmaḫ (lacuna-bracket; DINGIR-prefix; sh-digraph anglicization; manuscript-variant-inline-rendering) are extended without modification to this composition; no new project-wide conventions are introduced. The conventions established at this pass — single-divinity central entries (Utu / Šamaš); divine-quartet central entry (the flood-council); through-the-wall-trope cross-corpus; cross-corpus three-way oath-formula cluster; cross-corpus three-way apotheosis cluster — will scale to subsequent Mesopotamian texts.

The composition has zero `claim_type=speculative` entries; this Editor pass does not require human sign-off on speculative claims. Standard human Reviewer sign-off applies. The Editor's working principle on the eight major lens-risk concentrations identified at intake (Ziusudra name-cluster; antediluvian cities; seven-vs-forty flood duration; oath-by-life-of-heaven-and-earth; Dilmun-eastern-paradise; til3 diĝir-gin7 apotheosis; kingship-descended-from-heaven; flood-decision divine council quartet) was the **accuracy-above-lens** discipline with explicit operational disavowals at each high-risk concentration. The disavowals are surfaced in the rationale of the respective central entries (most prominently in `dilmun-eastern-paradise-cross-corpus`, `til-digir-gin-kima-ilani-apotheosis-of-flood-survivor-cross-corpus`, `ziusudra-atrahasis-utnapishtim-noach-flood-survivor-name-cluster-cross-corpus`, and `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus`).

---

## Corrective pass — 2026-06-01

A narrow corrective pass addressed a **referential-integrity defect** in this chapter's glossary references: four Mesopotamian-pipeline convention entries that the Translator and Editor had been treating as project-wide conventions were physically located in the **Enki-and-Ninmah overlay** rather than in the central glossary, so their `glossaryRef` entries did not resolve when consumed from Flood Story.

### Entries promoted from overlay → central

The following four entries were copied from `data-library/enki-and-ninmah-woh/_translation-glossary.json` into `data-content/i18n/translation-glossary.json` with their full content and rationale preserved verbatim. The `appliesTo[]` arrays were extended with the Flood Story `refId`s that already reference them:

- **`lacuna-bracket-convention-sumerian-mesopotamian-project-standard`** — appliesTo extended from 64 ENM refIds to 113 refIds (added 49 FLS refIds).
- **`dingir-prefix-prose-drop-convention`** — appliesTo extended from 40 ENM refIds to 59 refIds (added 19 FLS refIds).
- **`sumerian-proper-name-transliteration-convention`** — appliesTo extended from 10 ENM refIds to 36 refIds (added 26 FLS refIds).
- **`manuscript-variant-inline-rendering-convention`** — appliesTo extended from 10 ENM refIds to 11 refIds (added 1 FLS refId).

### Architectural rationale

These four entries encode **project-wide conventions** for all Sumerian and Akkadian compositions (the ETCSL editorial-apparatus bracket-marks; the DINGIR-determinative prose-drop policy; the š/ḫ digraph anglicization policy; the manuscript-variant inline-rendering policy). They are documented in their own rationale as ratified project-wide at the first Mesopotamian composition. Their appropriate home is therefore the central glossary, where they govern the Mesopotamian pipeline as a whole. This is the same architectural move as the Genesis-42 *hishtachavah* promotion from the Genesis-WoH overlay to central.

### Ids preserved verbatim

All four ids were kept unchanged to minimize back-edit scope across both chapters. The slightly redundant `-sumerian-mesopotamian-project-standard` suffix on the first id was retained on the same principle (the id is descriptive and the back-edit cost of renaming outweighs the cosmetic benefit).

### Version bumps

- **Central glossary** `data-content/i18n/translation-glossary.json`: `2.53.0` → `2.54.0` (semver-minor; 4 additions).
- **Enki-and-Ninmah overlay** `data-library/enki-and-ninmah-woh/_translation-glossary.json`: `1.1.0` → `1.2.0` (semver-minor; 4 deletions of project-wide entries, with `scopeNote` updated to record the promotion).
- **Flood Story chapter pin** `data-library/flood-story-woh/chapter-1.json` `translation.glossaryVersion`: `2.53.0` → `2.54.0`.
- **Enki-and-Ninmah chapter pin** `data-library/enki-and-ninmah-woh/chapter-1.json`: **left at `2.52.0` / `1.1.0`** as a frozen shipping-record. The chapter is stable; the pin records the glossary state at sign-off, not current state. All live `glossaryRefs` in that chapter that previously resolved via the overlay (1.1.0) now resolve via central (2.54.0); resolution remains clean.

### Chapter status

`translation.status` for Flood Story remains at `editor-review`. The Reviewer agent will re-verify referential integrity at the new central-glossary pin (`2.54.0`) and advance the chapter accordingly.
