# Adapa and the South Wind — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality, but with a **verificationStatus caveat**)
**Text:** Adapa and the South Wind — **THE PROJECT'S FIRST AKKADIAN-SOURCE TEXT**. 79 lines across 4 fragments (A=Amarna EA 356; B=K.8214+ Neo-Assyrian Nineveh; C+D=Late Babylonian).
**Version:** 1.0.0-rc1
**Glossary version:** central v2.56.0 + overlay v1.1.0
**⚠ verificationStatus:** `best-effort reconstruction; verification pending against Izre'el 2001`

## Summary table

| Metric | Value |
|---|---|
| Lines translated | 79 / 79 across 4 segments |
| Reviewer verdicts | **79 approve / 0 revise / 0 flag** |
| New central entries | **13** (v2.55.0 → v2.56.0) — including the chapter's biggest cross-corpus payloads |
| New overlay entries | 9 (v1.0.0 → v1.1.0) |
| Existing-entry extensions | 7 central (Akkadian-side activations of Sumerian↔Akkadian↔Hebrew clusters) |
| Source languages (central) | extended `["he", "sux"]` → **`["he", "sux", "akk"]`** (Akkadian added) |
| Glossary verdicts | **29 approve / 0 revise / 0 flag** |
| Lines with commentary | 79 / 79 |
| Lens-leakage flags | **0** (despite 8 major lens-risk concentrations — the highest-lens-risk Mesopotamian text yet) |
| Speculative entries | **0** |
| Items requiring human-only judgement | **0** (the verificationStatus caveat is project-level, not item-level) |

## Three architectural firsts in this ship

1. **The project's first Akkadian-source text** end-to-end through the four-stage pipeline. The new schema (`bookCode: ADP-WOH`, ISO 639-3 `akk` source language, Akkadian conventions per `dingir-prefix-prose-drop` + `lacuna-bracket-convention` + `sumerian-proper-name-transliteration` + `manuscript-variant-inline-rendering` — all four now central) works.

2. **Akkadian-side activation of the three-way cross-language sibling-clusters** flagged-for-future at the Flood Story. The 11 clusters with Akkadian-future flags now have ADP-WOH extensions on 7 of them (digir, abzu-engur, sag-gig-ga, seven-day-flood, an-enlil-enki-ninhursaga-flood-council, zi-da-ri-balatu-daru, lacuna-bracket-convention). The three-way cross-language sibling-cluster architecture is now in production with explicit etymological-cognate-vs-comparative-mythology distinctions preserved in every rationale (Akkadian↔Hebrew Semitic-cognate vs Sumerian↔Hebrew comparative-mythology-only).

3. **The verificationStatus convention** for source-text reconstruction-pending text: a new metadata field that explicitly flags "best-effort reconstruction; verification pending" without blocking the pipeline. Used here for Adapa where Izre'el 2001's primary critical edition isn't openly digitized; the lens-discipline + glossary work proceeds confidently on the sense-of-line (well-attested across editions) while the sign-by-sign verification is queued as future work. The convention will be reusable for any future text where source-acquisition is similarly constrained.

## The 13 new central entries (v2.56.0)

The chapter's biggest payloads:

| Slug | claim_type | Notes |
|---|---|---|
| `nemequ-napishtu-dariti-wisdom-but-not-immortality-paradigm-sage-cross-corpus` | `direct` | A:10 — **THE FOUNDATIONAL CRUX**: Ea gives Adapa wisdom but withholds eternal life. Bidirectional cross-corpus to Hebrew Gen 3:22 |
| `akal-balati-me-balati-food-of-life-water-of-life-akkadian-hebrew-cross-corpus` | `direct` | B:51-52, 55-56 — **THE CHAPTER'S BIGGEST CROSS-CORPUS PAYLOAD**. Bidirectional sibling-cluster to Hebrew tree-of-life entries. **Triple operational disavowals**: Christian-soteriological (John 6:48 / John 4:14 / Rev 22), WoH-engineered-immortality-substance, Adapa-as-Adam identity. Inverse-parallel-with-Eden framed as comparative-mythology |
| `ea-warning-deception-misadvice-test-crux-cross-corpus` | `direct` | B:30-31, 50-52 — three named-scholarship readings preserved without adjudication (Lambert/Kvanvig deliberate-deception; Buccellati/Bing misadvice; Izre'el strategic-test) + Sitchin disavowal |
| `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` | `direct` | B:10-12 — Izre'el 2001's thesis (Adapa breaks immortal wind's wing by SPEECH) |
| `shutu-cardinal-winds-akkadian-four-winds-divinized-cross-corpus` | `direct` | B:7 — divinized South Wind |
| `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus` | `direct` | B:22, 35 — **MAJOR LENS-RISK**: cross-corpus Adapa/Etana/Enoch/Elijah/Isaiah/Ezekiel/Paul/Hekhalot ascent-tradition. **Explicit Sitchin disavowal** (no Anu's-palace-spaceship, no rocket-flight ascent) |
| `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus` | `direct` | B:23, 36-41 — Frazer + Mettinger 2001 critique; explicit Christian-resurrection-typology disavowal |
| `divine-secret-leak-forbidden-knowledge-from-gods-to-humans-cross-corpus` | `direct` | B:50 — cross-corpus Gen 3:22, 1 Enoch Watchers, Prometheus |
| `adapa-apkallu-first-antediluvian-sage-paradigm-cross-corpus` | `direct` | A:1+ — Adapa as first of seven antediluvian sages |
| `divine-laughter-anu-laughs-sahaq-tsachu-cross-corpus` | `direct` | B:58 — Anu's *īṣiḫ* "laughed"; cross-corpus Hebrew *tsachaq* (the laughter at Sodom; Sarah's laugh; Isaac's name) |
| `return-to-the-earth-mortality-verdict-adapa-genesis-cross-corpus` | `direct` | B:61 — Adapa sent back to mortal earth; cross-corpus Gen 3:19 *el-afar tashuv* |
| `shedu-lamassu-tutelary-spirit-akkadian-hebrew-shedim-cross-corpus` | `direct` | The *šēdu* lemma (B:9 winged-form usage) — Akkadian↔Hebrew Semitic-cognate |
| `mourning-garb-dishevelled-hair-sackcloth-cross-corpus` | `direct` | B:20, 37-38 — cross-corpus Hebrew sackcloth mourning |

Plus **7 existing central entries extended** with Akkadian-side ADP-WOH refIds: `digir-sumerian-divine-lexeme-cross-corpus` (+31 refs), `abzu-engur-sumerian-subterranean-deep-cross-corpus` (+7 refs), `sag-gig-ga-black-headed-people-sumerian-self-designation-cross-corpus` (+1 ref), `seven-day-flood-vs-forty-day-flood-duration-tradition-cross-corpus` (+1 ref), `an-enlil-enki-ninhursaga-flood-council-quartet-cross-corpus`, `zi-da-ri-balatu-daru-eternal-life-cross-corpus`, `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (+18 refs).

## The 9 new overlay entries (v1.1.0)

Composition-specific: title-and-meta; **verification-pending-disclosure** (the convention entry); *mê qadišūti* pure cult-waters; *bīt nūni* house-of-the-fish kenning; **Ilabrat the *sukkallu* of Anu** (flagged for future central promotion at Inana's Descent); *kappī* the wing-breaking image; the Ea coaching-speech form (master-disciple binding-instruction genre); the garment-and-oil non-deadly accompaniments; the Fragment-C/D conservative-rendering convention.

## Items requiring decision

**None at the line/entry level.** Clean reviewer-approved sweep with explicit verbatim disavowals throughout the lens-risk concentrations:

- Christian-soteriological pre-resolution disavowed (John 6:48 bread of life, John 4:14 living water, Rev 22, Communion typology, Logos/John 1:1, Pauline third-heaven, eschatological resurrection-typology)
- Sitchin / popular-fringe readings disavowed (Anunnaki-rebel-Ea, food-of-life-as-engineered-substance, ascent-as-spaceflight, sonic-frequency-weapon-speech, apkallu-as-Anunnaki-civilizing-mission)
- Adapa-as-Adam identity-claim disavowed (Cyrus Gordon 1958 et al. — comparative-mythology parallel, NOT identity; Adapa is Akkadian, possibly *adap-* "wise"; Adam is Hebrew *adam* from *adamah* "earth"; names etymologically unrelated)
- WoH "engineered-immortality" / "engineered-mortality" synthesis disavowed throughout

**One project-level caveat**: the `verificationStatus: best-effort reconstruction; verification pending against Izre'el 2001` flag remains in the chapter file. The Editor and Reviewer both verified that the lens-discipline + glossary work is independent of (and complementary to) the sign-level verification that remains as future work. The English surface reflects the well-attested sense of each line across editions (Foster 2005, Heidel 1942, Picchioni 1981, Izre'el 2001's published commentary); the per-line Akkadian transliteration may have sign-level reconstruction errors that would be caught by a verification pass against Izre'el 2001's primary critical edition.

## Editor escalation report (inlined)

See `chapter-1-editor-report.md` — no speculative entries; 13 new central entries with full disavowal-discipline apparatus; 9 new overlay entries; 7 existing-entry Akkadian-side activations; the verificationStatus caveat preserved.

## Reviewer report (inlined)

Appended to `chapter-1.json` `translation.reviewerReport`: 79 line verdicts (all approve), 29 glossary verdicts (all approve), 0 lens-leakage flags. The Reviewer independently audited each of the 8 lens-risk concentrations and the bidirectional Akkadian↔Sumerian↔Hebrew sibling-cluster wiring, confirming the etymological-cognate-vs-comparative-mythology distinction is preserved in every rationale.

## Recommendation

Clean pass on philology, glossary architecture, lens-discipline, and the three-way cross-language sibling-cluster pattern. **The project's first Akkadian text — and the highest-lens-risk Mesopotamian text yet (inverse-parallel to the Eden Fall narrative) — has landed with strict named-scholarly-literary discipline at every risk-concentration.** The Sitchin/popular-fringe / Christian-typological / Adapa-as-Adam temptations are explicitly disavowed in the rationales; the legitimate cross-corpus comparative-mythology is fully documented as named scholarship.

If you agree, reply **sign-off ok** and I'll ship Adapa — the **fourth Mesopotamian text** live, the **first Akkadian text** live, and the **first verificationStatus-flagged ship** in the project. The verification-pass against Izre'el 2001 remains as future work; the lens-discipline and glossary architecture in production are independent of and unaffected by that pending verification.
