# Genesis 17 Editor Report

**Chapter:** Genesis 17 — El Shaddai, the covenant of circumcision, and the renaming of Avram and Sarai
**Translator pass:** clean (27 verses, all English filled, 13 editorial questions, 7 glossaryRefs mechanically applied)
**Editor pass:** complete; advanced to `editor-review`, `1.0.0-rc1`, glossary pinned to `2.14.0`
**Date:** 2026-05-23

---

## Summary of editorial decisions

- All 13 editorial questions resolved (none escalated as unresolved).
- 10 new glossary entries added (9 from the brief's target set + 1 Editor-call addition for `b-etzem-ha-yom-ha-ze-P-formula`, which the brief explicitly flagged as Editor's call between glossary entry and commentary-only treatment).
- 3 existing entries expanded in `appliesTo[]` (additive only, no semver-major modifications). The Editor's recommendation in the brief (expand existing rather than create new) was adopted.
- 0 speculative-claim entries. Every new entry is `claim_type=direct` — the chapter's lens-leverage moves are all defensible on mainstream HB scholarship and the apparatus stays in scholarly register.
- 8 paragraphs received substantial commentary (vv 1, 5, 10, 14, 15, 17, 19, 20, 23); other verses left as narrative-bridge per the brief's guidance.
- Glossary bumped 2.13.0 → 2.14.0 (semver-minor, additions-only).

---

## Reviewer attention items

### High lens-leverage entries to verify

#### `el-shaddai`

**Source:** אֵל שַׁדַּי (`El Shaddai`)
**WoH choice:** *El Shaddai* (transliterated; etymology unresolved)
**Why this entry needs careful review:** First HB occurrence of the divine name at Gen 17:1; recurs at Gen 28:3, 35:11, 43:14, 48:3, 49:25; P-document programmatic name at Exod 6:3. The entry presents three modern critical etymologies (Cross 1973 / Albright 1935 *šadû* mountain reading; Ouellette 1969 / Hess 2007 West-Semitic *Šaddai* class-epithet reading supported by the Deir ʿAlla *shdyn* inscription; the traditional *shadad* destroy-be-powerful reading behind LXX *pantokrator* and Vulgate *omnipotens*) in parallel without preempting any. The P-document harmonization at Exod 6:3 is documented as the source-critical frame.
**What to check:** (a) all three etymology positions presented in parallel and none preempted; (b) Deir ʿAlla *shdyn* inscription cited as direct documentary evidence for the West-Semitic *Šaddai* tradition (Hess 2007); (c) Cross 1973 *Canaanite Myth and Hebrew Epic* and Albright 1935 *JBL* 54 cited for the Akkadian *šadû* reading; (d) P-document harmonization at Exod 6:3 documented; (e) cross-reference to existing `shaddai-eloah` entry (Job-scoped) preserved; (f) translation choice (transliteration over ASV's *God Almighty*) consistent with WoH practice at `el-elyon` (Gen 14:22) and `el-roi-and-halom-elohim-variant` (Gen 16:13); (g) lens posture in apparatus only — no WoH cosmological claim made in the entry itself.
**Recommendation:** ship as written.

#### `brit-milah-circumcision-covenant`

**Source:** הִמּוֹל לָכֶם כָּל־זָכָר ... בְּשַׂר עָרְלַתְכֶם ... אוֹת בְּרִית
**WoH choice:** ASV-baseline preserved; institution treated comprehensively in apparatus
**Why this entry needs careful review:** The chapter's most editorially sensitive entry. Covers the institution comprehensively across four legal elements (eighth-day timing, household-slave inclusion, *karet* sanction, covenant-in-flesh formula), ANE comparative material (Egyptian Sixth Dynasty Karnak depictions; Herodotus II.36-37; Sasson 1966 *JBL* 85; Bergmann 1968), documentary-hypothesis stratification (Friedman 1987; Knohl 1995), cross-corpus reach (Gen 21:4, Gen 34, Exod 4:24-26 / Propp on *chatan damim*, Exod 12:43-49, Lev 12:3, Josh 5:2-9, 1 Sam 17:26+, Jer 9:24-25, Ezek 44:7-9), and downstream receptions (Maccabean revolt 1 Macc 1:48 / 60-61, Pauline Galatians 2-5 / Romans 2:25-29 + 4:9-12, rabbinic Cohen 1996).
**What to check:** (a) entry stays in mainstream HB-scholarship register; (b) no Jewish-vs-Christian supersessionist position implied; (c) Pauline reception explicitly *flagged-not-preempted* and located as downstream Christian interpretation; (d) rabbinic tradition treated in parallel with the Pauline reception, neither favored; (e) editorial-caution statement present ("This entry must not ship a Jewish-vs-Christian supersessionist position"); (f) ANE comparative material accurate (Jer 9:24-25 documenting circumcision as regional, not exclusively Israelite); (g) the four canonical legal elements correctly enumerated; (h) Propp 1999 *AB Exodus* cited for the *chatan damim* episode.
**Recommendation:** ship as written. The editorial caution is explicit and the downstream receptions are properly distanced.

#### `karet-penalty-cut-off-from-people`

**Source:** וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ
**WoH choice:** *that nefesh shall be cut off from his people* (preserves *nefesh* per chapter-2 convention)
**Why this entry needs careful review:** First *karet* formula in the Hebrew Bible; cross-corpus reach across ~30 Pentateuchal occurrences; load-bearing P/H legal-theological category.
**What to check:** (a) Milgrom *AB Leviticus 1-16* (1991) Excursus on *karet* correctly cited as the modern critical consensus position (divine-direct execution, premature death and extinction of line); (b) Wold 1979 dissertation cited as the standard monograph; (c) all four positions presented in parallel (Milgrom divine-direct, Phillips 1970 excommunication, Tigay JPS Deut 1996 premature death, Levine JPS Lev 1989 extinction of line); (d) cross-corpus reach accurate (~30 verses across Exod, Lev, Num — the Genesis list in the entry should be cross-checked against Milgrom's appendix); (e) the *nefesh* preservation rationale linked to the chapter-2 convention; (f) the *me-ameha* plural noted as a formula-marker.
**Recommendation:** ship as written.

### Documenting the `appliesTo` expansion choices

Per the Editor's-judgment paragraph in the brief, the additive-only expansion path was chosen for all three pre-existing entries (no new duplicate entries created). The expansions are technically additive (refIds added; no existing data modified) and are therefore not semver-major; the glossary bump 2.13.0 → 2.14.0 is semver-minor.

#### `brit-olam`

**Existing scope before this pass:** GEN-9:16 only (Noachic).
**Expansion:** added GEN-17:7, GEN-17:13, GEN-17:19 (the patriarchal Abrahamic occurrences).
**Rationale documented in-entry:** v2.14.0 expansion paragraph appended to the `rationale` field, listing the Gen 17 additions and documenting the wider HB distribution (Exod 31:16, Lev 24:8, Num 18:19, Num 25:13, 2 Sam 23:5, 1 Chr 16:17 / Ps 105:10, Isa 24:5 / 55:3 / 61:8, Jer 32:40 / 50:5, Ezek 16:60 / 37:26) for forward reference.
**Editor's call rationale:** the brief recommended expansion over new-entry creation, on the grounds that "this is how the project's cross-corpus glossary architecture is designed to work." The Editor concurs: `brit olam` is a single concept across all occurrences; creating a separate `brit-olam-patriarchal` entry would fragment the lexical decision unnecessarily.

#### `meqim-brit`

**Existing scope before this pass:** GEN-9:9, GEN-9:11 (Noachic).
**Expansion:** added GEN-17:7, GEN-17:19, GEN-17:21 (the patriarchal occurrences).
**Rationale documented in-entry:** v2.14.0 expansion paragraph appended; cross-references to the distinct `karat-brit-cut-covenant` (Gen 15:18 J/E) and the new `natan-brit-covenant-verb-cluster` (Gen 17:2) noted, framing the three covenant-verbs as a deliberate documentary-stratified cluster.
**Editor's call rationale:** the chapter-17 cluster uses three distinct covenant-verbs (*natan* v 2, *heqim* vv 7/19/21, implicit *zot briti* v 10), and the *heqim* selection at vv 7/19/21 is precisely the same idiom as the Noachic occurrences at Gen 9:9/9:11. One unified entry preserves the cross-corpus lexical insight.

#### `yishmael-name-etymology`

**Existing scope before this pass:** GEN-16:11, GEN-16:15, GEN-25:25, GEN-25:26, GEN-29:32, GEN-29:33, GEN-29:35, GEN-30:24, GEN-21:6 (9 refIds).
**Expansion:** added GEN-17:18, GEN-17:20, GEN-17:23, GEN-17:25, GEN-17:26 (the 5 Gen 17 Yishma'el occurrences). The order in `appliesTo[]` was rationalized into canonical reading order (GEN-16 → GEN-17 → GEN-21 → GEN-25 → GEN-29 → GEN-30).
**Rationale documented in-entry:** existing rationale unchanged (additive-only expansion of `appliesTo[]`).
**Editor's call rationale:** the entry already covers the cross-corpus patriarchal name-etymology pattern (Yitzchaq, Esav, Ya'aqov, Yosef, Re'uven, Shim'on, Yehuda); the Gen 17 Yishma'el occurrences fall straightforwardly within the existing scope. No new entry is warranted.

---

## Resolution of editorial questions

All 13 questions resolved. Mapping:

| refId | issue | resolution |
|---|---|---|
| GEN-WOH-17:1 (q1) | El Shaddai etymology / translation | New entry `el-shaddai`; transliteration preserved over ASV's *God Almighty*; three etymologies in parallel |
| GEN-WOH-17:1 (q2) | *hithallekh lefanai veheyeh tamim* | New entry `tamim-walk-before-god-covenant`; rendered *walk before me, and be you blameless* (NRSV/NIV-aligned, ASV's *perfect* rejected for moral-perfectionism mis-import) |
| GEN-WOH-17:2 | *v-etnah briti* / *natan brit* | New entry `natan-brit-covenant-verb-cluster`; rendered *I will make my covenant* (ASV-baseline) |
| GEN-WOH-17:5 | Avram → Avraham name-change | New entry `avraham-name-etymology`; transliteration preserved; folk-etymology + dialectal-variant readings both presented |
| GEN-WOH-17:7 (q1) | *brit olam* | Expansion of existing `brit-olam` `appliesTo[]` to include GEN-17:7, 17:13, 17:19 |
| GEN-WOH-17:7 (q2) | *va-haqimoti* / *heqim brit* | Expansion of existing `meqim-brit` `appliesTo[]` to include GEN-17:7, 17:19, 17:21 |
| GEN-WOH-17:10 | brit milah | New entry `brit-milah-circumcision-covenant`; comprehensive treatment |
| GEN-WOH-17:12 | *yelid bayit* / *miknat kesef* household-slave categories | Resolved into commentary on `brit-milah-circumcision-covenant` entry (ANE slave-classification material included there). No standalone glossary entry — the brief flagged this as "possibly skip in favor of commentary alone" and the Editor concurred |
| GEN-WOH-17:14 | *karet* penalty | New entry `karet-penalty-cut-off-from-people`; standalone (not sub-entry of brit-milah) per the brief's recommendation |
| GEN-WOH-17:15 | Sarai → Sarah name-change | New entry `sarah-name-change`; transliteration preserved |
| GEN-WOH-17:17 | *va-yitzchaq* / Yitzchaq word-play | New entry `yitzchaq-name-etymology-laughter-pattern`; ASV-baseline preserved, word-play carried in apparatus |
| GEN-WOH-17:20 | twelve princes of Yishma'el | New entry `twelve-princes-of-ishmael`; forward-applies to GEN-25:13-16 |
| GEN-WOH-17:23 | *b-etzem ha-yom ha-ze* P-formula | New entry `b-etzem-ha-yom-ha-ze-P-formula`; ASV's *in the selfsame day* preserved |

---

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bump:** 2.13.0 → 2.14.0 (semver-minor, additions-only).

**ScopeNote:** v2.14.0 paragraph appended documenting the chapter's 9 new entries (+ 1 Editor-call addition), the 3 appliesTo expansions, the two high-lens-leverage entries (`el-shaddai`, `brit-milah-circumcision-covenant`) and their accuracy-above-lens discipline.

**Added entries (10):**
- `el-shaddai` (`claim_type: direct`) — first patriarchal El Shaddai occurrence; three etymologies in parallel
- `tamim-walk-before-god-covenant` (`claim_type: direct`) — covenant-conduct stock formula
- `natan-brit-covenant-verb-cluster` (`claim_type: direct`) — the four covenant-verb idioms
- `avraham-name-etymology` (`claim_type: direct`) — Avram → Avraham name-change
- `brit-milah-circumcision-covenant` (`claim_type: direct`) — comprehensive circumcision institution entry
- `karet-penalty-cut-off-from-people` (`claim_type: direct`) — standalone *karet* entry
- `sarah-name-change` (`claim_type: direct`) — Sarai → Sarah name-change
- `yitzchaq-name-etymology-laughter-pattern` (`claim_type: direct`) — three laughter-Isaac plays
- `twelve-princes-of-ishmael` (`claim_type: direct`) — forward-applies to Gen 25
- `b-etzem-ha-yom-ha-ze-P-formula` (`claim_type: direct`) — P-document same-day-compliance formula

**Modified entries (3, appliesTo expansion only):**
- `brit-olam` — added GEN-17:7, GEN-17:13, GEN-17:19; rationale expanded with v2.14.0 expansion paragraph
- `meqim-brit` — added GEN-17:7, GEN-17:19, GEN-17:21; rationale expanded with v2.14.0 expansion paragraph
- `yishmael-name-etymology` — added GEN-17:18, GEN-17:20, GEN-17:23, GEN-17:25, GEN-17:26; appliesTo[] reordered into canonical reading order; rationale unchanged

### Per-translation overlay (`data-library/genesis-woh/_translation-glossary.json`)

None created. All chapter-17 entries went to the central glossary, consistent with the chapter's cross-corpus lexical reach (every new entry has substantial forward-application to other patriarchal and P-document chapters).

---

## What did not require escalation

The chapter has **no speculative-claim entries**. Every lens-leverage move is defensible on mainstream HB scholarship:

- `el-shaddai` — three modern critical etymologies, all mainstream
- `brit-milah-circumcision-covenant` — Sasson 1966, Bergmann 1968, Friedman 1987, Knohl 1995, Cohen 1996 — all mainstream
- `karet-penalty-cut-off-from-people` — Milgrom 1991 consensus position
- `twelve-princes-of-ishmael` — Knauf 1989 reconstruction is mainstream ANE-historical scholarship

The two high-lens-leverage entries (`el-shaddai`, `brit-milah-circumcision-covenant`) carry the lens entirely in the apparatus; the English text reads as defensible scholarly translation at every divergence point (ASV-baseline preserved on every verse). The lens-relevant material — the West-Semitic patriarchal-El cult inheritance behind *El Shaddai*, the P-document harmonization at Exod 6:3, the ANE comparative circumcision evidence, the Yishma'el / Yitzchaq covenant-distinction as an election-over-primogeniture pattern — is documented in apparatus only.

---

## Files modified

- `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-17.json` (status advanced to `editor-review`; version `1.0.0-rc1`; glossaryVersion `2.14.0`; 27 paragraphs with `glossaryRefs[]` populated; 8 paragraphs with commentary; editorial_questions cleared to empty array)
- `/Users/zara/Development/github.com/wheelofheaven/data-content/i18n/translation-glossary.json` (version 2.13.0 → 2.14.0; scopeNote extended; 10 new entries appended; 3 existing entries modified by `appliesTo[]` expansion)
- `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-17-editor-report.md` (this file)

---

## Ready for Reviewer

The chapter is ready for the Reviewer agent and subsequent human sign-off. No speculative entries gate the advance.
