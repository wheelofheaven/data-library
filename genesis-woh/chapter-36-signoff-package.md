# Genesis 36 — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality)
**Chapter:** 36 — **The Esau toledot.** Edomite genealogies + Horite clans of Se'ir + eight Edomite kings before any king reigned in Israel. Closes the Esau line; the narrative pivots to the Yosef cycle at Gen 37.
**Version:** 1.0.0-rc1
**Glossary version:** central v2.34.0 + overlay v1.4.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 43 / 43 |
| Reviewer verdicts | **43 approve / 0 revise / 0 flag** |
| New glossary entries | 8 total (5 central + 3 overlay) |
| AppliesTo expansions | 1 central (`pilegesh-concubine-status-class` + v 12) |
| Glossary verdicts | **9 approve / 0 revise / 0 flag** |
| Verses with commentary | ~16 / 43 |
| Lens-leakage flags | **0** |
| Speculative entries | **0** |
| Items requiring human-only judgement | 0 |

## The 5 new central entries (v2.34.0)

| Slug | claim_type | Notes |
|---|---|---|
| `aluf-edomite-clan-chief-tribal-confederation` | `direct` | ~40 chapter occurrences vv 15-43; cross-corpus Exod 15:15, Jer 13:21, Zech 9:7, 12:5-6 |
| `amaleq-timna-genealogy-archetypal-enemy-origin` | `direct` | LOAD-BEARING; v 12; cross-corpus Exod 17, Deut 25, Num 24, 1 Sam 15+30, 2 Sam 1, Est 3, 1 Chr 1 |
| `chorim-horites-hurrian-or-cave-dweller-identification` | `inferred` | v 20 (+ Gen 14:6); Speiser AB Hurrian vs Westermann/Bartlett cave-dweller; unresolved |
| `yemim-hapax-hot-springs-mules-demons-lens-discipline` | `inferred` | v 24; five-reading apparatus (hot springs/mules/demons/Onqelos/*eimim*); ASV-baseline preserved |
| `edom-kings-before-israel-monarchy-documentary-anchor` | `direct` | LOAD-BEARING MAJOR; v 31; full Wellhausen → Eissfeldt → Friedman → Speiser → Westermann → Skinner apparatus; Cassuto/Rashi apologetic + Ibn Ezra *sod ha-shneim asar* preserved |

## The 3 new overlay entries (v1.4.0)

| Slug | claim_type | Notes |
|---|---|---|
| `hu-edom-fourfold-refrain-toledot-structure` | `direct` | vv 1, 8, 9, 19, 43; distinct from Gen 25 birth-etymology |
| `esav-wives-list-three-chapter-doublet-gen-36-side` | `direct` | Gen-36-side anchor for the Esau-wives cross-chapter doublet |
| `bela-vs-bilam-ben-beor-name-doublet` | `inferred` | v 32; Deir 'Alla inscription (Hoftijzer-van der Kooij 1976) cross-reference; chapter-36 anchor pending future Num 22 translation |

## Reviewer's verbatim verifications

**On v 12 Amaleq-Timna:**
> *"Cross-corpus reach into Exod 17, Deut 25, Num 24, 1 Sam 15+30, 2 Sam 1, Est 3, 1 Chr 1 verifiably justifies central placement. Lens-discipline exemplary: no WoH-distinctive synthesis on the archetypal-enemy reading; project-specific synthesis correctly wiki-reserved."*

**On v 24 *yemim* hapax:**
> *"All five readings (hot springs / mules / demons / Onqelos / *eimim*-emendation) documented; ASV-baseline 'hot springs' preserved on translation surface per modern majority (LXX, Vulgate, Sarna, Westermann, Speiser, Hamilton, Alter)."*

**On v 31 the documentary anchor:**
> *"Full Wellhausen → Eissfeldt → Friedman → Speiser → Westermann → Hamilton → Skinner → Sarna apparatus cited; Cassuto/Rashi apologetic preserved; Ibn Ezra's *sod ha-shneim asar* via Spinoza correctly documented. The framing as 'mainstream modern scholarship, not WoH-distinctive' is exactly right."*

**On the Chori-vs-Horite corpus-normalization:**
> *"Editor's deferral is correct. Chapter-14 is stable v1.0.0; retroactive modification in this pass would violate audit-trail discipline. The cross-reference in the central glossary's appliesTo array correctly establishes corpus-wide governance pending a discrete future normalization pass."*

## Architectural decisions ratified by Reviewer

1. **Chori-vs-Horite normalization deferral** — chapter-14 stays at "the Horites" (ASV-baseline) until a discrete corpus-normalization pass. Audit-trail-safe.
2. **Single Gen-36-side Esau-wives overlay** — rather than three sibling entries (one per attestation chapter Gen 26/28/36). Only Gen 36 introduces the Oholivamah-Anah-Tziv'on-Horite integration requiring an independent anchor.
3. **Fourfold *hu Edom* refrain as overlay** — preserves the distinction between Gen 25 birth-etymology (central) and Gen 36 structural-toledot refrain (overlay).
4. **Bela/Bil'am as overlay with documented promotion-path** — promote to central when Num 22 (Bil'am narrative) is translated.

## Carry-forward

- **Promotion candidates standing**:
  - `yisrael-name-aetiology-sarah-im-elohim` (overlay; Gen 32) — promote when Hos 12 / Isa 49 / Exod 4 are translated
  - `binyamin-ben-oni-twelfth-tribe-aetiology` (overlay; Gen 35) — promote when 1 Sam / 1 Chr 8/12 are translated
  - `bela-vs-bilam-ben-beor-name-doublet` (overlay; Gen 36, new) — promote when Num 22 is translated
- **Corpus-normalization pass deferred**: Chori-vs-Horite (Gen 14:6 retroactive update)
- **Chapter milestone**: Genesis crosses 36/50 (72%). Yosef cycle begins next chapter (Gen 37); Gen 38 Judah-Tamar interlude follows.

## Production note

Editor pass single invocation, no timeout. Reviewer pass single invocation, no timeout. Editor and Reviewer aligned on every glossary decision.

## Editor escalation report

See `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-36-editor-report.md`.

## Reviewer report

Embedded in chapter JSON at `translation.reviewerReport`. Citations from Westermann *Genesis 12-36* 1985; Sarna JPS Genesis 1989; Speiser AB *Genesis*; Skinner ICC; Hamilton NICOT *Genesis 18-50*; Alter (standard Genesis); Wellhausen *Prolegomena* 1883; Eissfeldt *The Old Testament: An Introduction*; Friedman *Who Wrote the Bible*; Cassuto *La Questione della Genesi* (apologetic); Ibn Ezra (medieval — *sod ha-shneim asar*); Bartlett 1989 *Edom and the Edomites*; Mendenhall 1973 *The Tenth Generation*; Sagi *Memory of Amalek*; Wilhelm 1989 *The Hurrians*; Hoftijzer-van der Kooij 1976 *Aramaic Texts from Deir 'Alla*; Levine 1981 *JAOS*; Caquot-Lemaire 1977 *Syria*; BDB, HALOT, TDOT (lexica); b. Pesahim 54a (mules-reading of yemim); Targum Pseudo-Jonathan (demons-reading); Onqelos (warm-waters-reading).
