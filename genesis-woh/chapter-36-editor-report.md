# Chapter 36 Editor Report

**Chapter:** Genesis 36 (Esav-toledot, Horite clans of Se'ir, Edomite king-list)
**Editor pass:** 2026-05-27
**Status transition:** `draft` → `editor-review`
**Version transition:** `0.1.0-draft` → `1.0.0-rc1`
**Glossary pin:** central `translation-glossary.json` v2.33.0 → v2.34.0; overlay `_translation-glossary.json` v1.3.0 → v1.4.0

The Esav-toledot is lexically thin (mostly proper-noun lists) but contains three load-bearing documentary-critical / ANE-comparative items (v 12 Amaleq-Timna genealogy, v 24 *yemim* hapax crux, v 31 documentary anchor) and several structural-observation items requiring editorial-level decisions.

## Speculative entries requiring sign-off

**None.** All thirteen editorial questions from the Translator have been resolved into `direct` or `inferred` claim-type entries. No `speculative` entries were created. The lens-discipline pattern (ratified at chapter 35) was applied to the two crux-entries (v 12 Amaleq-Timna; v 24 *yemim*) and to the v 31 documentary anchor: in all three cases the mainstream-scholarly apparatus is documented without WoH-distinctive synthesis; any project-specific reading is wiki-reserved.

## Lens-discipline application

Three load-bearing items required explicit lens-discipline application:

### v 31 — the documentary anchor

The verse's *lifnei melokh melekh livnei Yisra'el* formula is one of the most-cited documentary-critical anchors in the Pentateuch (Wellhausen 1885 / Eissfeldt 1965 / Friedman 1987 + 2003 / Speiser 1964 / Westermann 1985 / Hamilton 1995 / Skinner 1910 / Sarna 1989). The documentary-critical observation is **mainstream modern scholarship — not a WoH-distinctive claim** and is presented as such in the entry's rationale. The harmonizing-traditional reading (Rashi reading *lifnei melokh* as referring to the patriarchal-promise of Gen 17:6 / 35:11; Cassuto 1941/1961 treating the formula as predictive-prophecy or retrospective-comment) is documented alongside the documentary-critical reading. The medieval anticipation (Ibn Ezra's cryptic *sod ha-shneim asar... v-yodaim tidom*, widely interpreted via Spinoza *TTP* 1670 as Ibn Ezra's coded acknowledgment) is noted as documentary. The entry is `claim_type: direct` because the documentary-critical observation is mainstream and verifiable across the standard commentaries; the harmonizing-traditional reading is the traditional Jewish-Christian conservative position; both are presented as named positions in modern scholarship.

### v 12 — Amaleq-Timna archetypal-enemy origin

The Gen 36:12 genealogical-placement of Amaleq within the Esavite-secondary-line (Timna concubine of Elifaz son of Esav) is the structural-seed of the HB's archetypal-enemy-of-Israel tradition (Exod 17:8-16, Deut 25:17-19, Num 24:20, 1 Sam 15, 1 Sam 30, 2 Sam 1, Est 3:1 — Haman *ha-Agagi*). The genealogical-structure is documentary; the cross-corpus Amaleq-tradition is HB-internal-explicit. **Any WoH-distinctive reading of the Amaleq-archetype (a "why" of the perpetual enmity, a cosmic-or-civilizational layer, a proto-something reading) is wiki-reserved**. The entry's rationale states this explicitly: project-specific synthesis is reserved for the wiki and is not preempted by this entry. The lens-discipline pattern is applied identically to its Gen 35 ratification.

### v 24 — *yemim* hapax crux

The *yemim* lexeme is a HB hapax with at least five attested readings (hot springs LXX/Vulgate/Sarna/Westermann/modern-majority; mules b. Pesachim 54a/Rashi/KJV; demons Targum Pseudo-Jonathan/Gen Rab; warm waters / *eimanaya* Onqelos; *eimim* emendation per Skinner). The crux is genuinely philologically-unresolved. The entry documents all five readings without WoH-distinctive synthesis. The translation surface preserves ASV-baseline *hot springs* per accuracy-above-lens. The *yemim* hapax is exactly the kind of lexeme that invites lens-leakage; the editorial-discipline of preserving the mainstream readings without WoH-distinctive synthesis is the explicit constraint.

## Central-vs-overlay architectural decisions

The ratified architectural-split (chapter-singular → overlay; cross-corpus reach → central) was applied as follows:

### Central (cross-corpus reach)

- **`aluf-edomite-clan-chief-tribal-confederation`** — ~40 occurrences in Gen 36 plus cross-corpus distribution at Exod 15:15, Jer 13:21, Zech 9:7 + 12:5-6; tribal-confederation pre-statehood register editorially-load-bearing. **CENTRAL** justified by cross-corpus reach.
- **`amaleq-timna-genealogy-archetypal-enemy-origin`** — cross-corpus reach into Exod 17, Deut 25, Num 24, 1 Sam 15, 1 Sam 30, 2 Sam 1, Est 3, 1 Chr 1. **CENTRAL** justified by the most extensive cross-corpus reach of any Gen 36 item.
- **`chorim-horites-hurrian-or-cave-dweller-identification`** — cross-corpus distribution at Gen 14:6, Gen 36:20-30, Deut 2:12 + 22, 2 Chr 25:14. **CENTRAL** justified by cross-corpus reach.
- **`yemim-hapax-hot-springs-mules-demons-lens-discipline`** — the lexeme itself is hapax (Gen 36:24-only), but the entry's *apparatus* (LXX, Vulgate, Talmud, Targumim, modern majority, emendation-proposals) is substantial and the crux is invoked across the entire history of HB philological scholarship. **CENTRAL** justified by the scholarly-apparatus's cross-corpus weight and by the lens-discipline-pattern application register.
- **`edom-kings-before-israel-monarchy-documentary-anchor`** — the verse is Gen 36:31-only, but the documentary-critical observation is one of the most-cited verses across the entire Pentateuchal-critical literature. **CENTRAL** justified by the verse's standing as a documentary-critical anchor with project-wide methodological implications.

### Overlay (chapter-singular structural observation)

- **`hu-edom-fourfold-refrain-toledot-structure`** — chapter-36-internal structural-refrain (vv 1, 8, 19, 43); editorially-distinct from the Gen 25:25/30 birth-and-stew etymology (already covered by the central `esau-edom-name-etymology-double-play` entry). Housed in the overlay to preserve the central entry's integrity. The decision **not** to extend the central entry's `appliesTo` to vv 1, 8, 19, 43 preserves the categorical-distinction between the *etymology* (Gen 25) and the *structural-identification-refrain* (Gen 36).
- **`esav-wives-list-three-chapter-doublet-gen-36-side`** — sibling to the central `morat-ruach-bitterness-of-spirit-esau-hittite-wives` entry per the ratified sibling-overlay-entries pattern. The central entry is anchored at Gen 26:34-35 + Gen 27:46 and frames the issue around the chapter-26 narrative-setup function; this overlay entry covers the Gen 36-side specifically, including the Oholivamah-into-Horite-lineage integration that does not appear in the chapter-26 entry. Three-attestation cross-chapter doublet (Gen 26:34 + Gen 28:9 + Gen 36:2-3); decision to use a single Gen-36-side overlay entry rather than three sibling entries (one per attestation chapter) reflects (a) the Gen 26:34 anchor is already-covered centrally; (b) the Gen 28:9 attestation is a single redactional-bridge verse without independent material; (c) the Gen 36:2-3 side introduces independent material (the Anah-Tziv'on-Chivvi clan-identification) that justifies its own entry.
- **`bela-vs-bilam-ben-beor-name-doublet`** — provisional overlay anchor at Gen 36:32, pending a future Num 22-Bil'am translation that would justify promotion to central. The cross-corpus Bil'am-tradition (Num 22-24, Num 31:8 + 16, Deut 23:5-6, Josh 13:22 + 24:9-10, Mic 6:5, Neh 13:2, 2 Pet 2:15) is referenced in the rationale, with promotion-path documented.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

- **Version bump:** 2.33.0 → 2.34.0 (semver-minor; five additions + one extension)
- **Added:**
  - `aluf-edomite-clan-chief-tribal-confederation` (claim_type: `direct`)
  - `amaleq-timna-genealogy-archetypal-enemy-origin` (claim_type: `direct`)
  - `chorim-horites-hurrian-or-cave-dweller-identification` (claim_type: `inferred`)
  - `yemim-hapax-hot-springs-mules-demons-lens-discipline` (claim_type: `inferred`)
  - `edom-kings-before-israel-monarchy-documentary-anchor` (claim_type: `direct`)
- **Modified:**
  - `pilegesh-concubine-status-class` — `appliesTo` extended from `[GEN-WOH-35:22]` to `[GEN-WOH-35:22, GEN-WOH-36:12]`. Reason: Timna at Gen 36:12 is named *pilegesh*, and the central entry's rationale already lists Gen 36:12 as a cross-corpus attestation; the `appliesTo` extension formalizes that link.

### Per-translation overlay (`data-library/genesis-woh/_translation-glossary.json`)

- **Version bump:** 1.3.0 → 1.4.0 (semver-minor; three additions)
- **Added:**
  - `hu-edom-fourfold-refrain-toledot-structure` (claim_type: `direct`)
  - `esav-wives-list-three-chapter-doublet-gen-36-side` (claim_type: `direct`)
  - `bela-vs-bilam-ben-beor-name-doublet` (claim_type: `inferred`)

## Translation-surface changes

The translation surface stays ASV-baseline. No translation-text changes from the Translator's draft were required (no glossary-driven wording changes; the ASV-baseline rendering matches the modern-majority readings for all chapter items). The Translator's renderings of proper nouns (WoH-transliterated *Esav*, *Edom*, *Se'ir*, *Chori*/*Chorim*, *Adah*, *Oholivamah*, *Basemat*, *Timna*, *Amaleq*, *Hadad*/*Hadar*, *Bela*, *Be'or*, etc.) are preserved per the standing convention. The ASV-baseline *chief* for *aluf* is preserved (~40 occurrences). The ASV-baseline *hot springs* for *yemim* is preserved per the lens-discipline pattern. The ASV-baseline rendering of v 31 (*before any king reigned over the children of Yisra'el*) is preserved; the documentary-critical apparatus is housed in commentary and in the central glossary entry.

## Flag: Chori-vs-Horite corpus-normalization decision

The chapter-14 stable text at GEN-WOH-14:6 reads *the Horites* (ASV-baseline transliteration with the full English-Christian-translation-tradition spelling). The chapter-36 draft consistently reads *Chori* / *Chorim* (WoH-transliterated proper-noun convention, matching the broader chapter-36 transliteration of Edomite / Horite / Esavite proper nouns).

**Recommendation:** harmonize on *Chori* / *Chorim* per the broader proper-noun convention (the WoH convention is more consistent with the corpus-wide treatment of other proper nouns).

**Action for this pass:** chapter-14 is **NOT modified** in this pass; the inconsistency is flagged here for a separate corpus-normalization pass. The chapter-36 commentary at v 20 explicitly notes the inconsistency and the normalization recommendation. The central glossary entry `chorim-horites-hurrian-or-cave-dweller-identification` lists both GEN-WOH-14:6 and GEN-WOH-36:20 etc. in its `appliesTo` array; the cross-corpus governance is in place, with the per-chapter rendering pending the normalization pass.

## Unresolved editorial questions

All thirteen editorial questions from the Translator's draft are resolved into glossary entries (added or extended) or into per-verse commentary. None are escalated as unresolved.

## Inventory of all thirteen editorial-question resolutions

| # | refId | Resolution |
|---|-------|------------|
| 1 | GEN-WOH-36:1 | New overlay entry `hu-edom-fourfold-refrain-toledot-structure` (vv 1, 8, 9, 19, 43); commentary at v 1, 8, 9, 19, 43. |
| 2 | GEN-WOH-36:2 | New overlay entry `esav-wives-list-three-chapter-doublet-gen-36-side` (sibling to central `morat-ruach-bitterness-of-spirit-esau-hittite-wives`); commentary at v 2. |
| 3 | GEN-WOH-36:2 (Chivvi-vs-Chori) | Documented in the central `chorim-horites-hurrian-or-cave-dweller-identification` entry; commentary at v 2 + v 20. Translation preserves MT *Chivvi*. |
| 4 | GEN-WOH-36:5 (ketiv/qere Ye'ush) | Translator-default applied (qere *Ye'ush* per standing Translator Brief principle); commentary at v 5. |
| 5 | GEN-WOH-36:11 (Elifaz-Teman / Job link) | Commentary at v 11; full cross-corpus Job-link deferred to future Job-translation pipeline (no glossary entry). |
| 6 | GEN-WOH-36:12 (Timna-Amaleq) | New central entry `amaleq-timna-genealogy-archetypal-enemy-origin`; existing central `pilegesh-concubine-status-class` extended to include GEN-WOH-36:12. Commentary at v 12 + v 22. |
| 7 | GEN-WOH-36:15 (aluf) | New central entry `aluf-edomite-clan-chief-tribal-confederation` (appliesTo covers all ~40 occurrences vv 15-43). Commentary at v 15 + v 40. |
| 8 | GEN-WOH-36:20 (Chori identity) | New central entry `chorim-horites-hurrian-or-cave-dweller-identification` (appliesTo covers GEN-WOH-14:6 + Gen 36 Horite-block); commentary at v 20. Chori-vs-Horite corpus-normalization flag raised (see above). |
| 9 | GEN-WOH-36:24 (yemim hapax) | New central entry `yemim-hapax-hot-springs-mules-demons-lens-discipline` (lens-discipline applied); commentary at v 24. Translation preserves ASV-baseline *hot springs*. |
| 10 | GEN-WOH-36:31 (documentary anchor) | New central entry `edom-kings-before-israel-monarchy-documentary-anchor`; commentary at v 31. Documentary-critical observation framed as mainstream modern scholarship, not WoH-distinctive. |
| 11 | GEN-WOH-36:32 (Bela / Bil'am ben-Be'or) | New overlay entry `bela-vs-bilam-ben-beor-name-doublet` (provisional chapter-36 anchor pending future Num 22-Bil'am translation); commentary at v 32. |
| 12 | GEN-WOH-36:35 (Hadad-Midyan-Mo'av) | Commentary at v 35; no glossary entry (the regional-dynamics cluster will be better-anchored at a future Num 22 / Num 31 translation). |
| 13 | GEN-WOH-36:39 (Hadar/Hadad variant) | Commentary at v 39; no glossary entry (the resh/dalet paleographic confusion is a separate corpus-normalization concern; cf. Gen 10:3 *Rifat* / 1 Chr 1:6 *Difat*). Translation preserves MT *Hadar*. |

## Reviewer-recommended attention

1. **The v 31 documentary anchor** — confirm the framing as "mainstream modern scholarship, not WoH-distinctive" is the project's preferred register. The entry presents Wellhausen / Eissfeldt / Friedman as named positions and Cassuto / Rashi / Ibn Ezra as named opposing-or-anticipating positions; the WoH-stance is reportorial rather than partisan.
2. **The v 12 Amaleq-Timna lens-discipline application** — confirm the "wiki-reserved" framing of any WoH-distinctive Amaleq-archetype reading. The Amaleq-tradition is one of the HB's most politically- and theologically-loaded threads (Sha'ul-Agag, Esther-Haman, the Deut 25 cherem-command), and the project may have a distinctive reading; the entry explicitly defers to the wiki.
3. **The v 24 *yemim* lens-discipline application** — confirm the ASV-baseline *hot springs* translation surface is correct. The reviewer may prefer transliterating *yemim* in italics with the apparatus surfaced; the entry documents this as a translation option but does not adopt it.
4. **The Chori-vs-Horite normalization decision** — confirm the recommendation to harmonize chapter-14 retroactively onto *Chori* / *Chorim* (rather than re-harmonize chapter-36 onto *Horite* / *Horites*). The corpus-wide proper-noun convention is the underlying constraint.
5. **The Esav-wives single-overlay-entry decision** — confirm the decision to use a single Gen-36-side overlay entry rather than three sibling entries (one per attestation chapter Gen 26 / Gen 28 / Gen 36). The single-entry decision was made because (a) Gen 26:34 is already covered centrally; (b) Gen 28:9 is a single bridge verse without independent material; (c) the architectural-split prefers overlay-housing for chapter-specific structural-observations.
