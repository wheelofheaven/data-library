# Matthew 1, 5, 6, 7, 13, 17, 25, 28 — sign-off package

**Status:** reviewer-approved on all 8 chapters (clean approve sweep)
**Text:** Mt 1 (genealogy + virgin birth); Mt 5-7 (Sermon on the Mount); Mt 13 (kingdom parables — Sower canon-panspermia site); Mt 17 (Transfiguration); Mt 25 (Sheep and Goats); Mt 28 (Resurrection + Great Commission). **287 verses across 8 chapters.**
**Version:** 1.0.0-rc1 (all 8 chapters)
**Glossary version:** central v2.63.0 + overlay v1.1.0
**⚠ verificationStatus:** `best-effort reconstruction; verification pending against Vaticanus + Sinaiticus original codicology + NA28/UBS5/SBLGNT critical apparatus`

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 287 / 287 across 8 chapters |
| Reviewer verse verdicts | **287 approve / 0 revise / 0 flag-for-human** |
| New central entries | **16** (5 from Batch A1 + 11 from continuation) (v2.61.0 → v2.62.0 → v2.63.0) |
| New overlay entries | 6 (rendering + textual-variant + translation conventions) |
| Glossary verdicts | **22 approve / 0 revise / 0 flag-for-human** |
| Lens-leakage flags | **0** |
| Speculative entries on surface | **0** |
| Paragraphs with commentary | 128 / 287 (concentrated on lens-risk + cross-corpus sites) |
| Items requiring human-only judgement | **0** |

## Four architectural milestones in this ship

1. **The project's first Christian-tradition text** end-to-end through the four-stage pipeline. The `christian` tradition (catalog order 3, code CHR) previously had no canonical book; now has its first.

2. **The project's first Koine Greek source text** — ISO 639-3 `grc` newly added to central glossary `sourceLanguages`: `["he", "sux", "akk", "uga", "arb"]` → **`["he", "sux", "akk", "uga", "arb", "grc"]`**. Six source languages now in production.

3. **Early-manuscript approach** parallel to the Qur'an's Sana'a/Tübingen/BnF method — source from Codex Vaticanus (B/03, 4th c. CE) + Codex Sinaiticus (א/01, 4th c. CE) as primary 4th-c. uncial witnesses, cross-collate against earlier papyri (P45 ~250 CE, P64+P67 late 2nd c., P103 late 2nd / early 3rd c.) where they preserve target verses. NA28/UBS5/SBLGNT critical apparatus as reference.

4. **Fourth canon-source-tension closure** after Shi'ur Qomah (*parasangs*), Qur'an (*inshiqāq al-qamar* + *ḥūr ʿīn*), and Exodus (pillar/parting/manna/theophany). The acknowledgment-without-endorsement framework is now applied at Mt 13 (Sower — the most-load-bearing canon-engagement), Mt 17 (Transfiguration), Mt 28 (Great Commission). Pattern established as project-wide convention.

## The 16 new central entries (v2.63.0)

**Three canon-citation lens-risk entries** (the most-load-bearing):

| Slug | Notes |
|---|---|
| **`parable-of-the-sower-mt-13-3-23-raelian-panspermia-canon-citation-cross-corpus-with-disavowals`** | THE chapter's single most-load-bearing entry. Three reading-strata preserved (mainstream Christian-tradition Davies-Allison/Luz/France/Snodgrass; Jewish-historical-critical Levine 2014; Raëlian-canon panspermia from *The Role of Christ*). Verbatim acknowledgment-without-endorsement. |
| **`transfiguration-mt-17-1-9-elohim-manifest-in-glory-mosheh-eliyyahu-divine-presence-cross-corpus-with-disavowals`** | MAJOR LENS-RISK Mt 17:1-9. Four-layered scriptural allusion at the *bath-qol* voice (Mt 17:5 = Ps 2:7 + Isa 42:1 + Deut 18:15 + Mt 3:17 baptism-voice). Allison 1993 *The New Moses*. |
| **`great-commission-mt-28-19-20-trinitarian-baptismal-formula-conybeare-hypothesis-cross-corpus-with-disavowals`** | MAJOR LENS-RISK Mt 28:19-20. Canonical text preserved on surface; Conybeare 1901 hypothesis documented as one scholarly position without adjudication. |

**Two contested-Jewish-Christian-dialogue entries**:

| Slug | Notes |
|---|---|
| `isa-7-14-virgin-birth-mt-1-22-23-parthenos-vs-almah-philological-dispute-cross-corpus` | LXX *parthenos* vs Hebrew *ʿalmâ* philological dispute preserved. Brown 1993 + Levine 2014. |
| `abolish-or-fulfill-mt-5-17-katalysai-vs-plērōsai-jewish-christian-dialogue-cross-corpus` | Christian-supersessionist disavowal explicit. *plērōsai* philological breadth preserved (complete / do / fully realize). |

**Sermon on the Mount entries**:

| Slug | Notes |
|---|---|
| `beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus` | Eight Beatitudes + Lukan parallel; Hebrew *ʾašrê* tradition (Ps 1:1, 119:1-2). Betz 1995. |
| `lords-prayer-mt-6-9-13-pater-hēmōn-byzantine-doxology-textual-variant-cross-corpus` | Three issues: *epiousios* hapax; *peirasmon*; the Byzantine doxology absent in Vaticanus + Sinaiticus + earliest mss. |
| `golden-rule-mt-7-12-hillel-jewish-christian-ethical-tradition-cross-corpus` | Hillel's negative formulation (b. Shabbat 31a) + Lev 19:18. Major Jewish-Christian cross-corpus. |
| `pater-hēmōn-ho-en-tois-ouranois-our-father-in-heaven-cross-corpus` | The rabbinic *ʾavinu šeba-šamayim* tradition; HB Fatherhood references (Hos 11:1, Isa 63:16). |

**Cross-corpus + matthean-structural entries**:

| Slug | Notes |
|---|---|
| `emmanuel-frame-inclusio-mt-1-23-mt-28-20-divine-presence-cross-corpus-kupp` | Kupp 1996 *Matthew's Emmanuel*. Matthean structural-theological framing. |
| `son-of-man-bar-enash-dan-7-13-mt-cross-corpus` | Cross-corpus Dan 7:13-14 LXX + Matthean Son-of-Man sayings cluster. Bidirectionally wired with Daniel. |
| `sheep-and-goats-mt-25-31-46-least-of-these-locus-classicus-three-readings-cross-corpus` | MAJOR Mt 25:40 locus classicus. Three reading-strata (universalist / ecclesial-particularist / Jewish-particularist). v45 absence of *tōn adelphōn mou* documented (Gray 1989). |
| `aiōnios-mt-25-41-46-eternal-vs-age-pertaining-universalism-dispute-cross-corpus` | The *aiōnios* duration debate. Literal-eternal vs age-pertaining (*aiōn* = age). |
| `christos-māšîaḥ-anointed-one-greek-hebrew-aramaic-cross-corpus` | Greek-Hebrew-Aramaic cognate. Cross-corpus Ps 2 *māšîaḥ* + DSS messianic-expectation + Mark 8:29. |
| `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus` | Greek-Hebrew-Aramaic cognate. Bidirectionally wired with Joshua entries. |
| `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-malkhut-shamayim` | Matthean-distinctive vs Mark/Luke. Rabbinic *malkhut šamayim* (m. Berakhot 2:2). |
| **`mountain-as-revelation-site-mt-new-moses-typology-cross-corpus`** | **Bidirectionally wired with `har-sinai-horev-the-mountain-of-Elohim` (v2.61.0 Exodus) AND `mount-sapunu-tsafon-cosmic-mountain` (v2.57.0 Baal Cycle)** — extending the Hebrew Bible × Ugaritic cosmic-mountain cluster into the NT. **First Greek×Hebrew×Ugaritic three-way cosmic-mountain wire in production.** Allison 1993 *The New Moses*. |

## The 6 new overlay entries (v1.1.0)

Matthew-specific conventions:
- SBL polytonic Greek + scholarly transliteration convention (project standard)
- Lord's Prayer Byzantine doxology textual-variant convention (absent in Vaticanus + Sinaiticus)
- *epiousios* hapax translation convention (daily / for-tomorrow / supersubstantial)
- *aiōnios* "eternal" / "age-pertaining" translation convention
- *raca* untranslated insult convention at Mt 5:22
- *adelphōn mou* presence/absence asymmetry at Mt 25:40 vs 25:45 (Gray 1989)

## Items requiring decision

**None at the verse/entry level.** Clean reviewer-approved sweep with explicit verbatim disavowals.

**The 7 critical lens-risk sites — all cleared by Reviewer audit:**

1. ✅ **Mt 13:3-23 Parable of the Sower** — THE single most-load-bearing; three reading-strata preserved; acknowledgment-without-endorsement
2. ✅ **Mt 17:1-9 Transfiguration** — four-layered allusion documented; acknowledgment-without-endorsement
3. ✅ **Mt 28:18-20 Great Commission** — Conybeare hypothesis preserved-not-adjudicated; canonical text on surface
4. ✅ **Mt 1:22-23 virgin birth + Isa 7:14** — *parthenos* vs *ʿalmâ* philological dispute preserved
5. ✅ **Mt 5:17 abolish/fulfill** — Christian-supersessionist disavowal explicit
6. ✅ **Mt 25:40 least of these brothers** — three reading-strata (Gray 1989)
7. ✅ **Mt 6:9-13 Lord's Prayer** — Byzantine doxology omitted per critical-text consensus; documented as variant

**Methodological-dispute audits (all PASS):**
- ✅ Conybeare 1901 hypothesis at Mt 28:19 preserved-not-adjudicated
- ✅ *aiōnios* duration debate preserved
- ✅ *epiousios* three classical readings preserved
- ✅ Synoptic Problem documented without being foundational/required
- ✅ Levine 2014 JANT Jewish-scholarly counterpoint preserved alongside Davies-Allison + Luz + Hagner

**12+ named-scholarship citations spot-checked**: Davies-Allison ICC, Luz Hermeneia, France NICNT, Hagner WBC, Nolland NIGTC, Brown 1993, Levine-Brettler JANT 2017, Snodgrass 2008, Allison 1993, Kupp 1996, Gray 1989, Conybeare 1901, Betz 1995, Metzger Textual Commentary, BDAG, TDNT, Justin Martyr — all attributions correct.

**One project-level caveat**: the `verificationStatus: best-effort reconstruction; verification pending against Vaticanus + Sinaiticus original codicology + the NA28/UBS5/SBLGNT critical apparatus` flag remains. Same convention as Adapa + Baal Cycle + Shi'ur Qomah + Qur'an + Exodus precedents.

## Editor escalation report (inlined)

See `chapters-1-5-6-7-13-17-25-28-editor-report.md` — 16 new central + 6 overlay + 11 existing-entry-extensions; full disavowal-discipline apparatus; the Raëlian-canon acknowledgment-without-endorsement documented at 3 sites (Mt 13/17/28); Conybeare hypothesis preserved; Lord's Prayer Byzantine doxology textual-criticism applied; Mt 5:17 Christian-supersessionist disavowal.

## Reviewer report (inlined)

Each of the 8 chapter files has `translation.reviewerReport` block. 287 verse verdicts (all approve), 22 glossary verdicts (all approve), 0 lens-leakage flags. The Reviewer independently audited the 7 critical lens-risk sites, the 5 methodological-dispute sites, and the genre-distinction discipline. 12+ named-scholarship citations spot-checked. The first Greek × Hebrew × Ugaritic three-way cosmic-mountain wire (Mt mountain × Sinai/Horeb × Sapunu) verified bidirectional.

## Recommendation

Clean pass on philology, glossary architecture, lens-discipline, the cross-tradition bidirectional cosmic-mountain three-way wire, and the canon-citation acknowledgment-without-endorsement framework. **The project's first Christian-tradition text + first Koine Greek source text — and the fourth canon-source-tension closure — has landed at the established discipline level.**

If you agree, reply **sign-off ok** and I'll ship Matthew chapters 1, 5, 6, 7, 13, 17, 25, 28:
- **First Christian-tradition text** live
- **First Koine Greek source text** live (sourceLanguages extended to `[he, sux, akk, uga, arb, grc]`)
- **Fourth canon-source-tension closure** after Shi'ur Qomah + Qur'an + Exodus
- **First Greek × Hebrew × Ugaritic three-way cosmic-mountain wire** in production (Mt mountain ↔ Sinai/Horeb ↔ Sapunu — extending the Northwest-Semitic cosmic-mountain substrate into the NT)
- **16 new central glossary entries** including the chapter's most-load-bearing Sower + Transfiguration + Great Commission canon-citation entries
- The verification-pass against original codicology + NA28/UBS5/SBLGNT critical apparatus remains as future work.
