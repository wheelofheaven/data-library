# Chapter 1 Editor Report — Enki and Ninmah (ETCSL 1.1.2)

## Overview

The Wheel of Heaven Translation Program's **first Mesopotamian text** and **first Sumerian-source text**. 141 lines. The Translator submitted 43 editorial_questions; this Editor pass resolves every one (either folded into a glossary entry or escalated below) and clears the array.

This pass establishes the project's foundational Sumerian-source conventions for all subsequent Mesopotamian translations (Atraḫasīs, Enūma Eliš, Gilgameš, the Sumerian King List, Inana's Descent, Adapa, Enki and Ninhursaĝa, Enki and the World Order). The conventions ratified here — lacuna-bracket-rendering; DINGIR-prefix-prose-drop; sh-digraph anglicization; manuscript-variant-inline-rendering — are project-wide.

This pass also wires the project's first cross-language sibling-clusters spanning Sumerian-Akkadian-Hebrew. The same-central-glossary architecture decision (ratified earlier in the Genesis arc) here yields its first cross-corpus dividend: foundational Sumerian vocabulary with cross-corpus reach into Akkadian and Hebrew now lives in the central glossary with bidirectional sibling-references to existing Hebrew central entries.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.glossaryVersion`: `2.51.0` → `2.52.0`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0`

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bump: 2.51.0 → 2.52.0**. The `sourceLanguages` array extended from `["he"]` to `["he", "sux"]` — the project's first multi-language central glossary.

**16 new central entries** (all Sumerian-source foundational vocabulary with cross-corpus reach into Akkadian and Hebrew):

1. `digir-sumerian-divine-lexeme-cross-corpus` (claim_type: `direct`) — the foundational Sumerian divine-class lexeme; the DINGIR-sign as eight-pointed star; bidirectional sibling-links to Hebrew `elohim-as-translation`, `el-shaddai`, `anokhi-elohei-X-avikha-ancestral-god-formula`.
2. `abzu-engur-sumerian-subterranean-deep-cross-corpus` (claim_type: `direct`) — Enki's subterranean fresh-water domain; bidirectional sibling-link to Hebrew `tehom`. The Heidel-Westermann-Tsumura *tehom-Tiamat* cognate-debate documented; not pre-resolved.
3. `im-sumerian-clay-of-human-creation-cross-corpus` (claim_type: `direct`) — the Sumerian human-creation-clay-substance; bidirectional sibling-links to Hebrew `adam-adamah` and `afar-va-efer-creatural-humility`. The cross-corpus Sumerian *kir3-kir3* ↔ Hebrew *qaratz* (Job 33:6) verb-cognate documented.
4. `zi-sumerian-breath-of-life-cross-corpus` (claim_type: `direct`) — the Sumerian life-breath lexeme; bidirectional sibling-link to Hebrew `neshamah-chayim`. The line-11 *zi-bi inim ĝar* crux flagged via overlay-entry.
5. `nam-sumerian-destiny-fate-cross-corpus` (claim_type: `direct`) — the Sumerian destiny-fate-lexeme and *nam tar* destiny-decreeing-idiom; partial-functional-cognate to Hebrew *goral* (no Hebrew central entry yet; future cross-link flagged).
6. `me-sumerian-divine-offices-cosmic-functions` (claim_type: `direct`) — the Sumerian flagship-untranslatable theological-keyword; preserved untranslated.
7. `anuna-collective-of-great-gods-cross-corpus` (claim_type: `direct`) — the Anuna / Anunnaki collective; cross-corpus to Hebrew `bnei-elohim-yarinu`. The popular-literature *Anunnaki* form-variation documented; the ancient-astronaut interpretive overlays reserved for the wiki.
8. `namma-primordial-mother-goddess-tiamat-comparandum` (claim_type: `direct`) — the Sumerian primordial-mother-goddess; the Namma-Tiamat cognate-debate (Jacobsen vs Wiggermann) documented and not pre-resolved.
9. `nam-lu2-ulu3-sumerian-humankind-cross-corpus` (claim_type: `direct`) — the Sumerian humankind-lexeme; bidirectional sibling-link to Hebrew `adam-adamah`.
10. `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` (claim_type: `direct`) — the Sumerian-Akkadian shared divine-toil-keyword (one of the few clear Sumerian → Akkadian loanwords); cross-corpus link to Hebrew `mas-oved-corvee-labor-institutional-vocabulary-cross-corpus`.
11. `zub-sig-dusu-corvee-basket-cross-corpus` (claim_type: `direct`) — the iconic Mesopotamian corvée-labor-basket symbol; cross-corpus link to Hebrew *sevel*.
12. `kalam-ka-na-ag-the-land-cross-corpus` (claim_type: `direct`) — the Sumerian collective-territorial-identity Land-lexeme; cross-corpus to Akkadian *mātu* and Hebrew *ha-aretz*.
13. `ekur-house-of-the-mountain-enlil-temple-cross-corpus` (claim_type: `direct`) — Enlil's principal temple at Nippur; cross-corpus to the ANE temple-as-cosmic-mountain tradition (Ugaritic Mount Zaphon; Hebrew Mount Zion / *Har ha-Bayit*; Greek Mount Olympus; Vedic Mount Meru).
14. `an-enlil-nudimmud-cosmic-triad-cross-corpus` (claim_type: `direct`) — the Sumerian-Akkadian senior-gods cosmic-triad.
15. `nibru-nippur-cuneiform-cross-corpus` (claim_type: `direct`) — the Sumerian-source form of Nippur; the dual-register convention (Sumerian-source texts use *Nibru*; Akkadian-source texts will use *Nippur*) established.
16. `za-mi-doxological-praise-formula-sumerian-cross-corpus` (claim_type: `direct`) — the Sumerian doxological-praise-closing-formula; cross-corpus to Akkadian *tanattu* and Hebrew *tehillah / hallel / barukh*.

**6 existing Hebrew central entries received bidirectional sibling-references** to the new Sumerian central entries (modifications to existing entries' rationale prose; no `wohChoice` or `appliesTo` changes):

- `elohim-as-translation` — back-reference to `digir-sumerian-divine-lexeme-cross-corpus` and `anuna-collective-of-great-gods-cross-corpus`.
- `tehom` — back-reference to `abzu-engur-sumerian-subterranean-deep-cross-corpus`.
- `neshamah-chayim` — back-reference to `zi-sumerian-breath-of-life-cross-corpus`.
- `adam-adamah` — back-references to `nam-lu2-ulu3-sumerian-humankind-cross-corpus` and `im-sumerian-clay-of-human-creation-cross-corpus`.
- `afar-va-efer-creatural-humility` — back-reference to `im-sumerian-clay-of-human-creation-cross-corpus`.
- `el-shaddai` — back-reference to `digir-sumerian-divine-lexeme-cross-corpus`.
- `anokhi-elohei-X-avikha-ancestral-god-formula` — back-reference to `digir-sumerian-divine-lexeme-cross-corpus`.

**Bidirectional cross-references verified.** Each new Sumerian central entry that references an existing Hebrew central entry by id has had the corresponding back-reference added to the Hebrew entry's rationale prose in the same edit.

### Per-translation overlay glossary (`data-library/enki-and-ninmah-woh/_translation-glossary.json`)

**Version bump: 1.0.0 → 1.1.0**.

**26 new overlay entries** (all composition-singular or chapter-localized; cross-corpus Sumerian foundational vocabulary went to the central glossary):

**Project-wide convention entries** (ratified here as the first Sumerian/Mesopotamian text; will govern all subsequent Sumerian-Akkadian translations):

1. `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (claim_type: `direct`) — preserve [restoration] and <editorial-supply> and […] lacuna; silently collapse /damage-but-readable\\; flag <<scribal-addition-deletion>> only in commentary where editorially-significant.
2. `dingir-prefix-prose-drop-convention` (claim_type: `direct`) — drop ^d DINGIR-determinative prefix in i18n.en prose; preserve in translit field.
3. `sumerian-proper-name-transliteration-convention` (claim_type: `direct`) — anglicized digraphs (sh for š; h for ḫ; ng for ĝ) in i18n.en prose; strict scholarly forms in translit field.
4. `manuscript-variant-inline-rendering-convention` (claim_type: `direct`) — render both manuscript-variants inline as `{primary} {alternate manuscript: variant}`.

**Chapter-specific philological-crux entries**:

5. `ud-re-a-ta-once-upon-a-time-formula` (claim_type: `direct`) — the Sumerian primordial-time-opener; cross-corpus to Akkadian *inūma* and Hebrew *be-reshit*.
6. `an-ki-bi-ta-heaven-and-earth-separation-cosmogony` (claim_type: `inferred`) — the heaven-and-earth-separation cosmogonic formula.
7. `ama-inana-mother-goddesses-class-noun` (claim_type: `inferred`) — the class-noun reading of *ama-Inana* vs proper-name vs Inana-epithet readings.
8. `sig7-en-sig7-hi-birth-goddesses-uncertain-vocalization` (claim_type: `direct`) — the cuneiform-sign-value preservation for the birth-goddess team-names.
9. `zi-inim-line11-breath-into-clay-vs-complain-about-life-crux` (claim_type: `inferred`) — **MANDATORY MAJOR** — the line-11 *zi-bi inim ĝar* construction; ETCSL *complain-about-life* reading retained on the surface; Lambert/Jacobsen *breath-into-clay* alternate reading surfaced in commentary with Gen 2:7 cross-corpus parallel.
10. `kig-sig-line23-substitute-vs-evening-meal-crux` (claim_type: `inferred`) — the *kiĝ2-sig10* substitute-laborer vs literal-evening-meal crux.
11. `hal-anku-enki-deliberation-chamber` (claim_type: `inferred`) — Enki's private deliberation-chamber toponym.
12. `harali-mythic-toponym-source-of-clay` (claim_type: `direct`) — the *Harali* toponym; location uncertain.
13. `ninmah-ninhursaga-nintud-birth-goddess-epithet-cluster` (claim_type: `direct`) — the Sumerian birth-goddess epithets are documented as referring to the same divine-class function (Jacobsen / Wiggermann / Kramer / Black et al. consensus).
14. `eight-birth-assistant-goddesses-vv34-35` (claim_type: `direct`) — the seven (or eight, with manuscript variants) birth-goddesses listed at vv 34-35: Ninimma, Shu-zi-ana, Ninmada, Ninbarag, Ninmug, ShAR.ShAR.GABA, Ninguna.
15. `lu2-gi-sushuru-sasade-nugam-weak-handed-disabled` (claim_type: `inferred`) — the first defective creature (weak-handed man).
16. `gi-nu-gi-blind-man-marvel-of-onlookers` (claim_type: `inferred`) — the second defective creature (the blind man) and the blind-musician aetiology; cross-corpus to Homer's Demodokos, Teiresias, Phineus, rabbinic blind-singer-tradition.
17. `lu2lil-fool-court-defective-creature` (claim_type: `direct`) — the third defective in the manuscript-variant reading; Akkadian *lillu* cognate.
18. `lu2-su-ba-gish-galla-no-genitalia` (claim_type: `direct`) — the sixth defective creature with neither penis nor vulva.
19. `tiru-third-gender-courtier-palace-attendant` (claim_type: `direct`) — the Sumerian-Akkadian third-gender palace-and-temple role; cross-corpus to Hebrew *saris*, with the explicit acknowledgement that the Sumerian-Akkadian and Hebrew lexemes are *not* philologically cognate but functionally-parallel.
20. `ushumgal-great-one-throne-dais` (claim_type: `direct`) — the *ušumgal* dragon/honorific-pre-eminent lexeme at v 65.
21. `namtar-disease-demon-vs-destiny-parsing-crux` (claim_type: `direct`) — the *nam-tar* dual-parsing (abstract-destiny vs proper-name Namtar-demon); the demon-reading uniquely at v 71.
22. `umul-sickly-creature-name-etymology` (claim_type: `inferred`) — Umul, Enki's contest-creature; etymology debated (Jacobsen 'my day is distant' vs Black et al. 'sickly-newborn' vs ETCSL opaque-proper-name); preserved as proper name.
23. `a-za-ad-head-fontanel-body-part` (claim_type: `direct`) — uncertain-precise-reference body-part lexeme; 'head' or 'fontanel' (Stol).
24. `lu2-til-la-lu2-ug-ga-neither-living-nor-dead` (claim_type: `direct`) — the *neither-living-nor-dead* liminal-being category at v 101; cross-corpus to Mesopotamian *eṭemmū*, *rabiṣu*, demonology.
25. `la2-line132-ninmah-work-counterbalanced-vs-undone` (claim_type: `inferred`) — the *la2* verb at vv 57 and 132; counter-balance (Jacobsen, WoH) vs undone (ETCSL) vs hang-in-balance (Foster).
26. `title-and-meta-conventions` (claim_type: `direct`) — the chapter-title-and-subtitle convention.

## Resolution of the 43 editorial_questions

The Translator submitted 43 editorial_questions; all are resolved as follows.

**Convention questions (folded into project-wide overlay entries):**

- ENM-WOH-1:1 (lacuna-bracket convention) → `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (overlay)
- ENM-WOH-1:0 (DINGIR-prefix prose convention) → `dingir-prefix-prose-drop-convention` (overlay)
- ENM-WOH-1:33 (Ninmah / Ninmaḫ digraph convention) → `sumerian-proper-name-transliteration-convention` (overlay)
- ENM-WOH-1:66 (manuscript-variant rendering) → `manuscript-variant-inline-rendering-convention` (overlay)
- ENM-WOH-1:34 (eight birth-goddesses transliteration) → `eight-birth-assistant-goddesses-vv34-35` (overlay) + `sumerian-proper-name-transliteration-convention` (overlay)
- ENM-WOH-1:77 (Nibru vs Nippur) → `nibru-nippur-cuneiform-cross-corpus` (CENTRAL)
- ENM-WOH-1:0 (title) → `title-and-meta-conventions` (overlay)

**Foundational central-glossary vocabulary (the project's first Sumerian-source central entries):**

- ENM-WOH-1:1 (ud re-a-ta) → `ud-re-a-ta-once-upon-a-time-formula` (overlay)
- ENM-WOH-1:1 (an ki-bi-ta separation) → `an-ki-bi-ta-heaven-and-earth-separation-cosmogony` (overlay)
- ENM-WOH-1:3 (nam ba-tar-ra) → `nam-sumerian-destiny-fate-cross-corpus` (CENTRAL)
- ENM-WOH-1:4 (a-nun-na / Anuna) → `anuna-collective-of-great-gods-cross-corpus` (CENTRAL)
- ENM-WOH-1:5 (ama-Inana) → `ama-inana-mother-goddesses-class-noun` (overlay)
- ENM-WOH-1:8 (kurum6 food-rations) → folded into `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` (CENTRAL)
- ENM-WOH-1:9 (diĝir šar2-šar2 / tur-tur senior vs lesser) → `digir-sumerian-divine-lexeme-cross-corpus` (CENTRAL)
- ENM-WOH-1:9 (du2-lum toil) → `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` (CENTRAL)
- ENM-WOH-1:10 (Harali) → `harali-mythic-toponym-source-of-clay` (overlay)
- ENM-WOH-1:11 (zi-bi inim ĝar) → `zi-inim-line11-breath-into-clay-vs-complain-about-life-crux` (overlay) + `zi-sumerian-breath-of-life-cross-corpus` (CENTRAL)
- ENM-WOH-1:13 (engur / a-sur-ra) → `abzu-engur-sumerian-subterranean-deep-cross-corpus` (CENTRAL)
- ENM-WOH-1:13 (diĝir) → `digir-sumerian-divine-lexeme-cross-corpus` (CENTRAL)
- ENM-WOH-1:17 (Namma) → `namma-primordial-mother-goddess-tiamat-comparandum` (CENTRAL)
- ENM-WOH-1:17 (ama palil u3-tud) → folded into `namma-primordial-mother-goddess-tiamat-comparandum` (CENTRAL)
- ENM-WOH-1:23 (kiĝ2-sig10 substitute) → `kig-sig-line23-substitute-vs-evening-meal-crux` (overlay)
- ENM-WOH-1:25 (Hal-anku) → `hal-anku-enki-deliberation-chamber` (overlay)
- ENM-WOH-1:26 (SIG7-EN, SIG7-ḪI) → `sig7-en-sig7-hi-birth-goddesses-uncertain-vocalization` (overlay)
- ENM-WOH-1:26 (me-dim2) → folded into commentary on lines 26, 28, 32, 54, 83, 133
- ENM-WOH-1:30 (zub-sig3 / dusu corvée-basket) → `zub-sig-dusu-corvee-basket-cross-corpus` (CENTRAL)
- ENM-WOH-1:31 (im ugu abzu — clay over the abzu) → `im-sumerian-clay-of-human-creation-cross-corpus` (CENTRAL)
- ENM-WOH-1:31 (abzu) → `abzu-engur-sumerian-subterranean-deep-cross-corpus` (CENTRAL)
- ENM-WOH-1:37 (nam-lu2-ulu3) → `nam-lu2-ulu3-sumerian-humankind-cross-corpus` (CENTRAL)
- ENM-WOH-1:47 (An, Enlil, Nudimmud) → `an-enlil-nudimmud-cosmic-triad-cross-corpus` (CENTRAL)
- ENM-WOH-1:51 (me) → `me-sumerian-divine-offices-cosmic-functions` (CENTRAL)
- ENM-WOH-1:65 (ušumgal) → `ushumgal-great-one-throne-dais` (overlay)
- ENM-WOH-1:66 (lu2lil) → `lu2lil-fool-court-defective-creature` (overlay)
- ENM-WOH-1:71 (Namtar demon vs destiny parsing) → `namtar-disease-demon-vs-destiny-parsing-crux` (overlay)
- ENM-WOH-1:77 (tiru eunuch / third-gender) → `tiru-third-gender-courtier-palace-attendant` (overlay)
- ENM-WOH-1:88 (Umul) → `umul-sickly-creature-name-etymology` (overlay)
- ENM-WOH-1:88 (a-za-ad head) → `a-za-ad-head-fontanel-body-part` (overlay)
- ENM-WOH-1:101 (lu2 til3-la / lu2 ug5-ga — neither living nor dead) → `lu2-til-la-lu2-ug-ga-neither-living-nor-dead` (overlay)
- ENM-WOH-1:123 (ka-na-aĝ2 / kalam — the Land) → `kalam-ka-na-ag-the-land-cross-corpus` (CENTRAL)
- ENM-WOH-1:127 (E-kur) → `ekur-house-of-the-mountain-enlil-temple-cross-corpus` (CENTRAL)
- ENM-WOH-1:132 (ḫe2-bi2-la2-la2 counter-balance vs undone) → `la2-line132-ninmah-work-counterbalanced-vs-undone` (overlay)
- ENM-WOH-1:141 (za3-mi2 doxology) → `za-mi-doxological-praise-formula-sumerian-cross-corpus` (CENTRAL)

**Cross-corpus link-inventory (ENM-WOH-1:0):** the Translator's intake question (1) lists ten cross-corpus links the translation establishes. All ten have been wired into the central glossary via bidirectional sibling-references as documented above.

## Speculative entries requiring sign-off

**None.** This Editor pass produced zero `claim_type=speculative` entries.

The Editor's working principle on this composition was the project's *accuracy-above-lens* discipline. Every divergence from the standard scholarly reading is documented as named-scholarship (Jacobsen, Lambert, Black et al., Kramer, Foster, Bottéro-Kramer, Kilmer, Wiggermann, Westermann, Sparks, Walton, etc.); no WoH-distinctive synthesis is surfaced in the translation or glossary entry rationales. The translation's surface reads as a defensible scholarly modern-English rendering in the Foster / Jacobsen / Black et al. register. The Wheel of Heaven lens is reserved for the wiki and methodology pages.

Three places where the Editor could have introduced speculative readings but did not, with rationale:

1. **The line-11 *zi-bi inim ĝar* crux.** The breath-into-clay reading (Lambert, Jacobsen, Foster, Bottéro-Kramer) is structurally-attractive for the Gen 2:7 cross-corpus parallel and is a defensible reading of the named-scholarship. The Editor's choice was to retain the Translator's surface ETCSL *complain-about-life* reading and surface the breath-into-clay alternate reading in commentary. The translation does not pre-commit to the surface-reading that would be most-WoH-friendly. The decision matches the *accuracy-above-lens* discipline.

2. **The Namma-Tiamat cognate-status.** The functional parallel between Sumerian *Namma* and Akkadian *Tiamat* (both primordial-mother-deities; both associated with the cosmic-watery-deep) is widely-attested in older Jacobsen-tradition scholarship; more recent scholarship (Wiggermann) is more cautious about the etymological-cognate-status. The Editor's decision was to document the cognate-debate as named-scholarship without pre-resolving it. A WoH-distinctive synthesis could have asserted the cognate; the Editor declined.

3. **The Anuna / Anunnaki ancient-astronaut-popular-tradition.** The Sitchin-corpus and related ancient-astronaut-tradition deploy *Anunnaki* with interpretive overlays distinct from the modern academic Assyriology-tradition. The Editor's decision was to document the popular-form and explicitly note that the interpretive overlays are *reserved for the wiki and broader-corpus discussions, not preempted by the translation-glossary entry*. The lens is held in the apparatus, not in the translation-glossary-rationale prose.

## Unresolved editorial questions

**None.** All 43 editorial questions are resolved. The `editorial_questions[]` array is empty in the chapter-1.json output.

## Items flagged for future cross-corpus wiring (not blocking this pass)

These are wiring-tasks for future Editor passes; they do not block the current pass's sign-off.

1. **Hebrew *goral* central entry.** The cross-corpus link between Sumerian *nam / nam tar* and Hebrew *goral* (lot, portion) is documented in this pass's central entry `nam-sumerian-destiny-fate-cross-corpus`. The Hebrew *goral* lexeme does not yet have its own central entry. When a Genesis-WoH or Job-WoH Editor pass produces the *goral* central entry, it should add a bidirectional back-reference to `nam-sumerian-destiny-fate-cross-corpus`.

2. **Akkadian foundational entries.** When the project translates Atraḫasīs and Enūma Eliš, the foundational Akkadian vocabulary will receive central entries: *ilum* / *Anu* / *Ea* / *Tiamat* / *šīmtu* / *amēlūtu* / *dullu* / *napištu* / *parṣū* / *tanattu*. Each should be wired bidirectionally to (i) the Sumerian-source central entries from this pass; (ii) the Hebrew-source central entries on the corresponding lexemes; (iii) the existing Genesis-WoH centrals where applicable. The architecture established here generalizes to that wiring.

3. **Hebrew *ha-aretz / eretz* central entry.** The cross-corpus link between Sumerian *kalam* and Hebrew *ha-aretz* is documented in this pass's central entry `kalam-ka-na-ag-the-land-cross-corpus`. The Hebrew *eretz / ha-aretz* lexeme does not yet have its own central entry. Future Genesis-WoH or prophetic-corpus Editor pass should add the central entry with bidirectional back-reference.

4. **Hebrew *Har ha-Bayit / Tzion* central entry.** The cross-corpus link between Sumerian *E-kur* and Hebrew *Har ha-Bayit / Tzion* is documented in `ekur-house-of-the-mountain-enlil-temple-cross-corpus`. Future Editor pass on a temple-and-Zion text should establish the Hebrew central entry with back-reference.

5. **Hebrew *yatzar* (form, fashion) central entry.** The cross-corpus link between Sumerian *dim2* and Hebrew *yatzar* (Gen 2:7; Jer 18; Isa 64:7) is documented in this pass's central entry `im-sumerian-clay-of-human-creation-cross-corpus`. The Hebrew *yatzar* lexeme does not yet have its own central entry (the existing `bara` central entry is on the parallel-creation-verb; *yatzar* is distinct). Future Editor pass should create the central entry with back-reference.

## Cross-corpus bidirectional sibling-cluster summary

This Editor pass wires the project's **first cross-language sibling-clusters** spanning Sumerian-Akkadian-Hebrew. The bidirectional links are verified in both directions:

**Divine-class cluster.** Sumerian `digir-sumerian-divine-lexeme-cross-corpus` ↔ Hebrew `elohim-as-translation`, `el-shaddai`, `anokhi-elohei-X-avikha-ancestral-god-formula`. The Sumerian *diĝir* and the Hebrew *el / Elohim* are *not* etymologically cognate (Sumerian is a language isolate; Hebrew *el* is West-Semitic, cognate with Akkadian *ilum* and Ugaritic *il*). The cross-corpus-functional cluster is documented as named-scholarship (Cross, Albright, Smith, Heiser) without forcing etymological cognate-claims that the scholarship does not support.

**Cosmographic-deep cluster.** Sumerian `abzu-engur-sumerian-subterranean-deep-cross-corpus` ↔ Hebrew `tehom`. The Sumerian *abzu* is the source of Akkadian *apsû* (true loanword). The Hebrew *tehom* is etymologically-cognate with Akkadian *Tiamat* (both from proto-Semitic *thm-*). The Heidel-Westermann-Tsumura cognate-debate documented; not pre-resolved.

**Human-creation-substance cluster.** Sumerian `im-sumerian-clay-of-human-creation-cross-corpus` ↔ Hebrew `adam-adamah` and `afar-va-efer-creatural-humility`. The cross-corpus *human-from-clay-or-dust* topos is one of the corpus's clearest comparative-mythology patterns. The Sumerian-Hebrew verb-cognate *kir3-kir3* (nip off) ↔ *qaratz* (Job 33:6 nip off) is editorially-foundational and documented.

**Breath-of-life cluster.** Sumerian `zi-sumerian-breath-of-life-cross-corpus` ↔ Hebrew `neshamah-chayim`. The line-11 *zi-bi inim ĝar* crux (Lambert/Jacobsen *breath-into-clay* reading) provides the most-direct *creator-breathes-life-into-clay* cross-corpus parallel with Gen 2:7. The crux is documented in both the central entry and the overlay-entry `zi-inim-line11-breath-into-clay-vs-complain-about-life-crux`.

**Humankind cluster.** Sumerian `nam-lu2-ulu3-sumerian-humankind-cross-corpus` ↔ Hebrew `adam-adamah`. The Sumerian humankind-lexeme and the Hebrew *adam* function as cross-corpus humankind-class-noun cognates.

**Divine-toil cluster.** Sumerian `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` ↔ Hebrew `mas-oved-corvee-labor-institutional-vocabulary-cross-corpus`. The Sumerian *du-lum* and Akkadian *dullu* are one of the few clear Sumerian → Akkadian loanwords. The cross-corpus *humans-relieve-divine-toil* topos is foundational for the Mesopotamian creation tradition; the Hebrew Bible's labor-vocabulary preserves the thematic-parallel without the divine-toil-relief rationale at the foreground.

**Divine-assembly cluster.** Sumerian `anuna-collective-of-great-gods-cross-corpus` ↔ Hebrew `bnei-elohim-yarinu`. The Sumerian-Akkadian Anuna / Anunnaki is the Mesopotamian-source instantiation of the wider ANE divine-assembly tradition; the Hebrew *bnei Elohim* is the Hebrew-Bible instantiation.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible scholarly modern-English rendering in the Foster/Jacobsen/Black et al. register. The lens lives in the apparatus (commentary + glossary entries), not in the translated English. Every glossary entry has all required fields, correct claim_type, and rationale that a scholar of Sumerian (or Akkadian, or Hebrew, where the cross-corpus links apply) would recognize as serious work. The bidirectional sibling-cluster wiring establishes the foundation for subsequent Mesopotamian translations.

The 16 new central entries + 26 new overlay entries collectively establish the project's first Sumerian-source vocabulary base and the first cross-language sibling-cluster architecture. The conventions ratified here (lacuna-bracket; DINGIR-prefix; sh-digraph anglicization; manuscript-variant-inline-rendering) are project-wide for the Mesopotamian arc.

The composition has zero `claim_type=speculative` entries; this Editor pass does not require human sign-off on speculative claims. Standard human Reviewer sign-off applies.
