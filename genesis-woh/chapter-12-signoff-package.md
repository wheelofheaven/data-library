# Genesis 12 — sign-off package

**Status:** awaiting-human (reviewer flagged 2 forward-binding policy decisions for explicit human ratification)
**Chapter:** 12 — Call of Abram, theophanies, descent to Mitsrayim (first wife-sister episode)
**Version:** 1.0.0-rc1
**Glossary version:** 2.9.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 20 / 20 |
| Reviewer verdicts | 20 approve / 0 revise / 0 flag |
| Glossary entries added | 13 (8 direct, 5 inferred, 0 speculative) |
| Glossary verdicts | 13 approve / 0 revise / 0 flag |
| Verses with commentary | 16 / 20 (vv 4, 12, 14, 19 left bare — narrative-bridge, Translator default uncontested) |
| Verses with glossaryRefs | 14 / 20 |
| Lens-leakage flags | 0 |
| Forward-binding policy items requiring human ratification | 2 |

## The two human-ratification items

### Item 1: v 3 niphal-passive blessing policy

**The dispute.** Genesis 12:3 says *u-v-rakhu vekha kol mishpechot ha-adamah*. The MT points the verb as niphal (passive — "shall be blessed by you"). The same formula recurs at 18:18 / 28:14 (also niphal pointed) and at 22:18 / 26:4 (hithpael pointed — "shall bless themselves by you"). The MT itself preserves both pointings.

**Modern critical positions:**
- **Middle/reflexive throughout** (NJPS, Sarna 1989, Speiser 1964, Westermann): the original was middle; the MT niphal pointings are late harmonizations.
- **MT-fidelity verse-by-verse** (Wenham 1987, Hamilton 1990): render niphal as passive and hithpael as middle exactly as pointed.
- **Passive throughout** (ASV, RSV, the Pauline reception at Gal 3:8): treat all five occurrences as theologically passive.

**The Editor chose MT-fidelity verse-by-verse.** That means v 3 / 18:18 / 28:14 will be rendered passive ("shall be blessed"); 22:18 / 26:4 will be rendered middle ("shall bless themselves").

**The Reviewer approves on the merits** but flags this as forward-binding — the policy locks the translation of chs 18, 22, 26, 28. If you'd prefer all-passive (Pauline / Christian-tradition consistency) or all-middle (modern-critical-consensus consistency), the `nivrakhu-bekha-niphal-hithpael` glossary entry needs amending before those chapters are drafted.

**Recommendation:** approve the MT-fidelity policy. It is the philologically most defensible — it preserves what the MT itself preserves. Both NJPS and NRSV took this stance and the project's "accuracy above lens" rule cuts the same way.

### Item 2: wife-sister type-scene `appliesTo` scope

**The decision.** The new `wife-sister-type-scene` glossary entry has an `appliesTo` array that covers ~40 verses across Gen 12:10-20, Gen 20:1-18, and Gen 26:1-11. The vocabulary-consistency lock means: when Gen 20 and Gen 26 are drafted, the same beauty-formula, sister-claim, taking-formula, and expulsion-formula renderings must carry over.

**The Reviewer approves** the lock — vocabulary consistency across the three type-scene instances is editorially correct and is exactly what Alter 1981 argued for when he gave the type-scene its canonical scholarly framing.

**Recommendation:** approve. The lock prevents drift; the alternative (each instance translated independently) would lose the type-scene's structural visibility.

## Glossary entries added (v2.9.0, 13 entries)

| Slug | Claim type | Cross-corpus? | Scope |
|---|---|---|---|
| `lekh-lekha` | direct | Gen 12, Gen 22 only | the doubled imperative |
| `nivrakhu-bekha-niphal-hithpael` | direct | Gen 12, 18, 22, 26, 28 | the blessing-form dispute |
| `nefesh-asher-asu` | direct | Gen 12:5 (plus rabbinic-vs-modern reception) | the "souls made" phrase |
| `elon-moreh` | inferred | Gen 12, 35, Deut 11, Judg 7 | sacred-tree-oracle site |
| `va-yera-yhwh-theophany` | direct | recurring (Gen 17, 18, 26, 35; Exod 3, 6) | theophany-formula |
| `zera-eretz-promise` | direct | recurring across patriarchal cycle | seed-land covenant nucleus |
| `qara-b-shem-yhwh` | direct | Gen 4:26, 12:8, 13:4, 21:33, 26:25 | calling-on-the-name at altars |
| `wife-sister-type-scene` | inferred | Gen 12, 20, 26 | the three-instance type-scene |
| `eshet-yefat-mareh` | direct | Gen 12, 29; 1 Sam 25; 2 Sam 14; 1 Kgs 1; Esth 2 | beautiful-woman formula |
| `imri-na-achoti-at` | direct | Gen 12, 20 | say-sister strategy |
| `camel-anachronism` | inferred | Gen 12:16, 24, 30, 37 (4 wife-sister mentions) | redaction-criticism marker |
| `nega-pharaoh-proto-exodus` | inferred | Gen 12:17 (forward to Exod 7-12) | plague-on-Pharaoh proto-typology |
| `va-y-shalchu-expulsion` | inferred | Gen 12:20, Exod 6:1 / 11:1 / 12:33 | expulsion-verb cross-reference |

## Lens posture

Quiet throughout. The lens surfaces only at v 7 (first patriarchal theophany — noting continuity with the divine-descent register of chs 1-11) and v 17 (divine affliction of Pharaoh — noting the typological link forward to the Exodus plagues, which scholars including Sarna treat as part of the proto-Exodus reading of Gen 12). Both surfacings are contained to commentary, restrained in voice, and reflect mainstream scholarly observation, not project-specific synthesis. The Reviewer registered no lens-leakage flags.

## Sign-off requested

To complete:
- Confirm the v 3 niphal-passive MT-fidelity policy (or amend to all-passive / all-middle)
- Confirm the wife-sister type-scene 40-verse `appliesTo` scope

Then deploy: glossary v2.9.0 + chapter-12 → data-content / data-library, mirror to www, FF submodule pointers. Genesis becomes **12 chapters / 319 paragraphs** (Phase 2 opens).

## Editor escalation report

See `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-12-editor-report.md`.

## Reviewer report

Embedded in chapter JSON at `translation.reviewerReport`. 20 verse verdicts + 13 glossary verdicts, all `approve`, with citations from Westermann, Speiser, Sarna, Wenham, Hamilton, Alter, Sternberg, Sapir-Hen & Ben-Yosef 2013, Finkelstein & Silberman 2001, plus standard reference works (BDB, HALOT, GKC).
