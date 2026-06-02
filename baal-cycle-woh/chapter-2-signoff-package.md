# Baal Cycle KTU 1.3 + 1.4 — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality, but with a **verificationStatus caveat**)
**Text:** The palace-building cycle — ʿAnat's bloody battle, ʾAṯirat's intercession, Kothar's construction, the window debate, Baʿlu's enthronement. **634 lines across 14 segments** (KTU 1.3 cols i–vi + KTU 1.4 cols i–viii).
**Version:** 1.0.0-rc1
**Glossary version:** central v2.58.0 + overlay v1.2.0
**⚠ verificationStatus:** `best-effort reconstruction; verification pending against KTU³ (Dietrich-Loretz-Sanmartín 2013)`

## Summary table

| Metric | Value |
|---|---|
| Lines translated | 634 / 634 across 14 segments |
| Reviewer line verdicts | **634 approve / 0 revise / 0 flag-for-human** |
| New central entries | **13** (v2.57.0 → v2.58.0) |
| Promoted overlay → central | **1** (`word-of-tree-whisper-of-stone-mystery-revelation-formula`) |
| New overlay entries | 3 (composition-specific) |
| Existing-entry extensions | 15 central (KTU 1.3-1.4 refIds added) |
| Glossary verdicts | **31 approve / 0 revise / 0 flag-for-human** |
| Lens-leakage flags | **0** (despite ~10 major lens-risk concentrations) |
| Speculative entries on surface | **0** |
| `claim_type=inferred` entries | 0 (all 13 new central are `direct` — well-attested cross-corpus) |
| Items requiring human-only judgement | **0** |

## Three architectural milestones in this ship

1. **Second Levantine chapter** — Baal Cycle Ch 2 brings the corpus to 5 texts total (4 Mesopotamian + 1 Levantine-with-2-chapters). The `levantine` tradition now has multi-chapter coverage of its flagship text.

2. **First overlay→central promotion in the Levantine tradition** — `word-of-tree-whisper-of-stone-mystery-revelation-formula` recurred at KTU 1.3 iii (after first appearance at KTU 1.1 iii). Editor promoted per the established "Gen 42 hishtachavah / Flood Story corrective" pattern: new central entry created with refIds spanning BOTH chapters, chapter-1.json live glossaryRefs back-edited from overlay ID → central ID, overlay entry deleted. Verified by Reviewer.

3. **The largest glossary growth across a single chapter pair** — Combined with Ch 1's 18 new entries, the Baal Cycle has now added **31 new central glossary entries** (+ 1 promoted + 11 overlay across both chapters) in two ships. Central glossary now at v2.58.0 with ~644 terms across `[he, sux, akk, uga]`.

## The 13 new central entries (v2.58.0)

| Slug | claim_type | Notes |
|---|---|---|
| `mot-mavet-death-personified-cross-corpus-ugaritic-hebrew-bible` | `direct` | Môtu / Hebrew *mavet*. Proleptic to KTU 1.5-1.6. Day 2000, Smith 1985, Healey 1999 (DDD). Disavow Christian-Adam-Christology (1 Cor 15:54-55). |
| `lotanu-leviathan-seven-headed-serpent-cross-corpus-ugaritic-hebrew-bible` | `direct` | **The cleanest cognate-cluster in NW-Semitic Chaoskampf studies**: Ugaritic *lṭn bṯn brḥ wbṯn ʿqltn* ↔ Hebrew *liwyāṯān nāḥāš bāriaḥ wĕ-liwyāṯān nāḥāš ʿăqallāṯôn* (Isa 27:1). Day 1985, Day 2000, Wakeman 1973, Tsumura 2005. Disavow Rev 12:9 dragon-typology pre-resolution. |
| `qlh-qds-tr-arts-thunder-voice-theophany-cross-corpus-ugaritic-hebrew-bible-psalm-29` | `direct` | **F. M. Cross 1973's foundational thesis**: Ps 29 = "Yahwehized" Baʿlu hymn. *qlh qdš tr ʾarṣ* ↔ *qol YHWH yaḥsōb ʾărāzîm* (Ps 29:5). Cross 1973, Day 2000, Smith 2002. Disavow Acts 2 Pentecost-typology. |
| `palace-temple-building-typology-cross-corpus-ugaritic-mesopotamian-hebrew-bible` | `direct` | **The Hurowitz 1992 cluster**. Cross-corpus to Enuma Elish (Esagil), Ugaritic Baal Cycle (Kothar's construction), Hebrew Bible (1 Kgs 5-8 Solomon, 2 Sam 7 Nathan oracle, Ezra 3, Hag 1-2). Disavow Sitchin-Anunnaki-construction-tech and John 2:21 Christ-as-true-temple. |
| `window-of-heaven-arubbah-cross-corpus-ugaritic-hebrew-bible-storm-god-cosmology` | `direct` | Ugaritic *ḥln* (KTU 1.4 vi 1-15, vii 14-40) ↔ Hebrew *ʾărubbôt ha-šāmayim* (Gen 7:11, 8:2, Mal 3:10). **Reviewer audit emphasis**: chronological-discipline preserved — "shared NW-Semitic cosmological substrate, not Genesis-copied-Ugaritic." Day 2000, Smith & Pitard 2009. |
| `qnyt-ilm-creatress-of-the-gods-cross-corpus-ugaritic-hebrew-bible-qoneh-shamayim` | `direct` | ʾAṯirat's epithet ↔ Gen 14:19, 22 *qōnēh šāmayim wā-ʾāreṣ*. Shared *qny/qnh* "create" root. Day 2000, Smith 2001, Westermann 1985. |
| `seventy-sons-of-athirat-bnei-elohim-deut-32-8-cross-corpus-ugaritic-hebrew-bible` | `direct` | **Heiser thesis** activation. Numerical-cognate: seventy sons of ʾAṯirat (KTU 1.4 vi 46) ↔ Deut 32:8 LXX/4QDeut^j *lmspr bny ʾlhym*. Heiser 2008/2015, Smith 1990, Cross 1973. Bidirectional wire to existing `bn-ilm-sons-of-god`. |
| `kothar-dwelling-caphtor-memphis-cross-corpus-ugaritic-hebrew-bible-philistine-origins` | `direct` | Kothar at Memphis (*ḥkpt*) + Caphtor (*kptr*) ↔ Amos 9:7, Gen 10:14, Jer 47:4. Late-Bronze-Aegean toponym. Day 2000, Singer 1992, Niemeier 1998. |
| `house-like-the-gods-divine-residency-complaint-cross-corpus-ugaritic-hebrew-bible-temple-theology` | `direct` | The "Baʿlu has no house like the gods" lament (5 recurrences) ↔ 2 Sam 7:2 / 1 Chr 17:1 Nathan-oracle. Structural-trigger for the palace cycle. Hurowitz 1992. |
| `descent-to-sheol-bt-hpzt-arts-cross-corpus-ugaritic-hebrew-bible-underworld-vocabulary` | `direct` | *bt ḫpṯt ʾarṣ* "house of freedom-from-life" ↔ Hebrew *bēt ḥōpšît* (2 Kgs 15:5, Ezek 26:20). Day 2000, Healey 1999. |
| `cosmic-distance-pilgrimage-formula-thousand-acres-ten-thousand-hectares-cross-corpus-ugaritic` | `direct` | Formulaic "thousand fields, ten thousand acres" (recurs across 1.3-1.4). Compositional poetic-formula. |
| `seven-day-banquet-feast-structure-cross-corpus-ugaritic-mesopotamian-hebrew-bible` | `direct` | Seven-day-banquet (KTU 1.3 i, 1.4 vi firing, 1.4 vii enthronement) ↔ 1 Kgs 8:65-66, Lev 23:34-36. Hurowitz 1992, Milgrom 2001. |
| `cedars-of-lebanon-erez-cross-corpus-ugaritic-hebrew-bible-construction-material-economy` | `direct` | Lebanon cedars at Baʿlu's palace ↔ 1 Kgs 5:6-10 Hiram-Solomon, Ps 104:16, Ezra 3:7. Late-Bronze/Iron-Age prestige-construction-economy. Liphschitz 2007, Hurowitz 1992. |

Plus **1 promoted-from-overlay**: `word-of-tree-whisper-of-stone-mystery-revelation-formula-cross-corpus-ugaritic-hebrew-bible` — recurred at KTU 1.3 iii 31, sufficient cross-composition reach for promotion. Hab 2:11 + Ps 19 cross-corpus. Chapter-1.json back-edited, overlay deleted, all named-scholarship preserved.

Plus **15 existing v2.57.0 central entries extended** with KTU 1.3-1.4 refIds: el, baal, yamm, athirat, anat, kothar, dagan, bn-ilm, bull-of-el, rider-of-clouds, mount-sapunu, mlk-olam, divine-council-phr-mad, chaoskampf, lacuna-bracket-convention.

## The 3 new overlay entries (v1.2.0)

Composition-specific to the Baal Cycle:
- `pidrayu-tallayu-arsayu-baals-three-daughters-baal-cycle` — Baʿlu's three daughters (Pidrayu daughter-of-light, Tallayu daughter-of-rain, ʾArṣayu daughter-of-the-wide-world); weak cross-corpus reach
- `qadesh-amrar-athirats-attendant-baal-cycle` — Qadeš-wa-ʾAmrar, ʾAṯirat's *mšlmt* attendant; weak cross-corpus reach
- One additional Baal Cycle-specific compositional item

## Items requiring decision

**None at the line/entry level.** Clean reviewer-approved sweep with explicit verbatim disavowals throughout. The ~10 lens-risk concentrations in Ch 2 — all cleared:

1. **ʿAnat's bloody battle** (KTU 1.3 ii) — warrior-goddess scholarship preserved; no Christian-Mariological pre-resolution
2. **ʿAnat's threat to ʾIlu** (KTU 1.3 v) — feminist-scholarship implications preserved (Smith & Pitard 2009 audacity-within-patriarchy)
3. **ʾAṯirat-of-the-Sea** (KTU 1.4 ii) — Asherah polemic disavowal at `athirat-asherah-...` and `qnyt-ilm-...`
4. **Seventy sons of ʾAṯirat** (KTU 1.4 vi 46) — Heiser-thesis Deut 32:8 cross-corpus + Watchers-engineering disavowal preserved
5. **Kothar's palace construction** (KTU 1.4 vi) — Hurowitz 1992 cluster + Sitchin-construction-tech and Christ-as-true-temple disavowals
6. **The seven-day firing** (KTU 1.4 vi 24-32) — cosmic prototype for 1 Kgs 8:65-66; no source-derivation framing
7. **The WINDOW debate** (KTU 1.4 vi-vii) — **chronological-discipline preserved verbatim** by Reviewer: "shared NW-Semitic cosmological substrate, not Genesis-copied-Ugaritic"; Sitchin-window-as-airlock disavowed; Pentecost-typology disavowed
8. **Baʿlu's voice from the palace** (KTU 1.4 vii 32-34) — F. M. Cross 1973 Ps 29 = Yahwehized Baʿlu hymn correctly attributed; Acts 2 Pentecost disavowal explicit
9. **Baʿlu's challenge to Môt** (KTU 1.4 viii) — proleptic to KTU 1.5-1.6; Christian-Adam-Christology disavowal preserved
10. **The Lôtanu reference** (KTU 1.3 iii 41-42) — cleanest NW-Semitic Chaoskampf cognate; Rev 12:9 dragon-typology disavowed

**One project-level caveat**: the `verificationStatus: best-effort reconstruction; verification pending against KTU³` flag remains. Same convention as Ch 1 + Adapa.

## Editor escalation report (inlined)

See `chapter-2-editor-report.md` — 13 new central + 1 promoted + 3 overlay + 15 existing-entry extensions; full disavowal-discipline apparatus; the word-of-tree promotion documented with chapter-1.json back-edit confirmation.

## Reviewer report (inlined)

Appended to `chapter-2.json` `translation.reviewerReport`: 634 line verdicts (all approve), 31 glossary verdicts (all approve), 0 lens-leakage flags. The Reviewer specifically verified the chapter-1.json back-edit for the word-of-tree promotion (live glossaryRefs at BCY-WOH-1.1-iii:12-16 now point to central ID, overlay file no longer contains the entry). 5+ named-scholarship citations spot-checked: F. M. Cross 1973, Hurowitz 1992, Day 1985, Heiser 2015, Smith & Pitard 2009 — all attributions correct.

## Recommendation

Clean pass on philology, glossary architecture, lens-discipline, the overlay→central promotion pattern, and the chronological-discipline (Ugaritic precedes Hebrew Bible, but the project doesn't slide into "Genesis copied Ugaritic" — it preserves "shared NW-Semitic cosmological substrate"). **The most substantial central-glossary growth in any Levantine chapter to date — and the second multi-tablet Baal Cycle ship — has landed with strict named-scholarly-literary discipline at every risk-concentration.** F. M. Cross 1973's Ps 29 = Yahwehized Baʿlu hymn entry alone is worth the chapter; combined with Hurowitz 1992 palace-typology, Day 1985 Lôtanu-Leviathan cognate-cluster, Heiser-thesis seventy-sons-of-ʾAṯirat → Deut 32:8 cross-corpus, and the window-of-heaven cluster — this chapter is the dense center of the Levantine tradition's first-pass payload.

If you agree, reply **sign-off ok** and I'll ship Baal Cycle Ch 2 — second Levantine chapter live, second Ugaritic ship, first overlay→central promotion in the Levantine tradition, 13 new central + 1 promoted + 3 overlay + 15 extensions. The verification-pass against KTU³ Dietrich-Loretz-Sanmartín 2013 remains as future work.
