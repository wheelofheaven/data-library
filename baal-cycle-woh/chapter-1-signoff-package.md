# Baal Cycle KTU 1.1 + 1.2 — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality, but with a **verificationStatus caveat**)
**Text:** Baʿlu vs Yammu — the sea-conflict episode of the Ugaritic Baal Cycle. **THE PROJECT'S FIRST UGARITIC-SOURCE TEXT and FIRST LEVANTINE-TRADITION TEXT.** 226 lines across 10 segments (KTU 1.1 cols i–vi + KTU 1.2 cols i–iv).
**Version:** 1.0.0-rc1
**Glossary version:** central v2.57.0 + overlay v1.1.0
**⚠ verificationStatus:** `best-effort reconstruction; verification pending against KTU³ (Dietrich-Loretz-Sanmartín 2013)`

## Summary table

| Metric | Value |
|---|---|
| Lines translated | 226 / 226 across 10 segments |
| Substantive lines (non-lacuna) | 211 |
| Reviewer line verdicts | **226 approve / 0 revise / 0 flag-for-human** |
| New central entries | **18** (v2.56.0 → v2.57.0) — the largest single glossary expansion in project history |
| New overlay entries | **8** (v1.0.0 → v1.1.0) |
| Existing-entry extensions | 2 central (Ugaritic-side activations: `speech-act-efficacy...`, `lacuna-bracket-convention...`) |
| Source languages (central) | extended `["he", "sux", "akk"]` → **`["he", "sux", "akk", "uga"]`** (Ugaritic added) |
| Glossary verdicts | **26 approve / 0 revise / 0 flag-for-human** |
| Lines with commentary | 47 / 226 (concentrated on lens-risk + cross-corpus sites; empty on mechanical / lacunar lines per editorial discipline) |
| Lens-leakage flags | **0** (despite 12 major lens-risk concentrations — the most lens-risk-heavy text in the corpus) |
| Speculative entries on surface | **0** |
| `claim_type=inferred` entries | 2 (the YW line + bull-of-El epithet — both honest markings of legitimate scholarly debate) |
| Items requiring human-only judgement | **0** (the verificationStatus caveat is project-level, not item-level) |

## Four architectural firsts in this ship

1. **The project's first Ugaritic-source text** end-to-end through the four-stage pipeline. ISO 639-3 `uga` source language; central glossary `sourceLanguages` extended `["he", "sux", "akk"]` → **`["he", "sux", "akk", "uga"]`**.

2. **The project's first Levantine-tradition text** — new tradition `levantine` added to the catalog (order 11, icon `waves`), distinct from `mesopotamian` (separate Hittite-Hurrian tradition will land later per user direction). The tradition is the home for Late Bronze Age Northwest-Semitic mythological literature from the eastern Mediterranean — Ugaritic primarily (Baal Cycle, Aqhat, Kirta), with potential future texts from Mari, Emar, etc.

3. **The project's first text where the original-script Unicode is included in the source file from day one.** Ugaritic alphabetic cuneiform is a 30-letter abjad with a 1:1 mapping to Unicode block U+10380–U+1039F. The helper script `scripts/translit_to_ugaritic.py` (33 lines) mechanically converts KTU/standard transliteration → Ugaritic Unicode. Every line has both `translit` (strict KTU with ʾa/ʾi/ʾu alef markings + ḫ/ḏ/ġ/ṯ/ḥ/ṣ/ṭ/ẓ/ʿ/ʾ/ś/š diacritics) AND `cuneiform` (Unicode-rendered). This is distinct from Sumerian/Akkadian where logographic-cuneiform requires a back-rendering pipeline run separately.

4. **The largest single glossary expansion in project history**: 18 new central entries (vs Adapa's 13, Flood Story's 11, Enki and Ninhursag's 2). Driven by the Baal Cycle's centrality to Hebrew Bible comparative-mythology — the El/Baʿlu/Yammu/ʾAṯirat/ʿAnat/Kothar pantheon is the single biggest cross-corpus payload in Northwest-Semitic studies.

## The 18 new central entries (v2.57.0)

The chapter's payload — divine names, epithets, Chaoskampf vocabulary, and the YW line:

| Slug | claim_type | Notes |
|---|---|---|
| `el-ugaritic-ilu-northwest-semitic-pantheon-head-cross-corpus` | `direct` | ʾIlu = El. Genuine Northwest-Semitic cognate. Cross 1973, Smith 2001, Day 2000. Disavow simplistic-identity. |
| `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic` | `direct` | Baʿlu = Baʿal. Day 2000, Smith 1994. Polemical-dialogue, not identity. |
| `yamm-yammu-sea-deified-cross-corpus-chaoskampf-hebrew-bible` | `direct` | Yammu = Yam. Day 1985, Wakeman 1973, Tsumura 2005. |
| `athirat-asherah-mother-goddess-cross-corpus-ugaritic-hebrew-bible` | `direct` | ʾAṯirat = Asherah. Cleanest cognate in NW-Semitic studies. Day 2000, Olyan 1988, Hadley 2000, Dever 2005, Smith 1990. |
| `anat-warrior-goddess-cross-corpus-ugaritic-erased-from-hebrew-bible` | `direct` | ʿAnat the warrior consort. Walls 1992, Day 2000. |
| `kothar-wa-khasis-divine-craftsman-cross-corpus-speech-act-weapon-naming` | `direct` | The divine craftsman. Smith 1994, Pardee 2002. |
| `astarte-athtart-cross-corpus-ugaritic-hebrew-bible-ashtoreth` | `direct` | ʿAṯtart. Day 2000. |
| `dagan-dagon-grain-deity-cross-corpus-ugaritic-hebrew-bible-philistine-pantheon` | `direct` | Daganu. Singer 1992, Day 2000. Disavow popular fish-deity false-etymology. |
| `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim` | `direct` | bn ʾilm = bnei elohim. Heiser 2008/2015, Smith 1990, Cross 1973. Massive cross-corpus reach (Gen 6, Job 1:6, 38:7, Deut 32:8 LXX/4QDeut^j). Disavow Watchers-engineering reading. |
| `bull-of-el-thr-ilu-cross-corpus-ugaritic-hebrew-bible-bull-of-jacob` | `inferred` | Honest marking — the philological cognate-cluster is real (Cross 1973), but the theological-historical inheritance-from-Ugaritic-ʾIlu-cult-specifically is scholarly-reconstruction, not explicit-in-source. |
| `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany` | `direct` | rkb ʿrpt → Ps 68:5 rōkēb bā-ʿărābôt. Day 2000, Cross 1973. Disavow Christological pre-resolution (no Son-of-Man typology, no Rev 1:7). |
| `mount-sapunu-tsafon-cosmic-mountain-cross-corpus-ugaritic-hebrew-bible` | `direct` | Mt Ṣapunu (Jebel al-Aqra, 1759m) → Hebrew tsafon (Ps 48:3 yarketei tsafon). Clifford 1972, Day 2000. Disavow Sitchin-Nibiru fringe. |
| `qdqd-head-smiting-victory-formula-cross-corpus-ugaritic-hebrew-bible` | `direct` | qdqd zbl ym → Ps 68:22, Hab 3:13, Judg 5:26. Day 2000, Cross 1973. Disavow Gen-3:15-protoevangelium Christological-typology. |
| `mlk-olam-eternal-king-cross-corpus-ugaritic-hebrew-bible` | `direct` | mlk ʿlm → Ps 145:13, Jer 10:10. Day 2000. |
| `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible` | `direct` | pḫr mʿd → Akkadian puḫru + Hebrew sod / ʿadat-el (Ps 82). Mullen 1980, Heiser 2008. Three-way Akkadian↔Ugaritic↔Hebrew cluster. |
| `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus` | `direct` | **The two divine weapons** (KTU 1.2 IV 11-28). Major cross-corpus to Adapa's `speech-act-efficacy-language-power-of-life-and-death` — bidirectionally wired. Smith 1994. Disavow Sitchin-engineered-weapon and Christian-Logos pre-resolution. |
| `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible` | `direct` | The broader Chaoskampf cluster. Day 1985, Wakeman 1973, Tsumura 2005, Day 2000. Cross-corpus to Mesopotamian (Enuma Elish Tiamat — anticipates future activation), Ugaritic (Yammu), Hebrew (Yam/Leviathan/Rahab). |
| **`yw-line-ktu-1-1-iv-14-proto-yahweh-candidate-cross-corpus-ugaritic`** | **`inferred`** | **THE CHAPTER'S BIGGEST LENS-RISK SITE.** Famous `šm bny yw` line. Three named readings preserved without adjudication (de Moor 1971 / Cross 1973 / Smith 1994). Surface English bare `YW` — no vocalization commitment. **Verbatim disavowal**: "This entry does NOT claim that Ugaritic proves Yahweh originated as a Canaanite deity. The philological evidence is genuinely contested. Both directions of the YHWH-Ugaritic question remain open in the named scholarship cited." Also disavows Sitchin-engineered-ET-deity reading. |

Plus **2 existing central entries extended** with Ugaritic-side ADP-WOH/BCY-WOH refIds:
- `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` — Ugaritic-side wired: Yagrush and Ayamur are speech-act-named weapons (Kothar speaks their names INTO existence, and the names ARE the weapons' effective power). Three-way Akkadian↔Ugaritic↔Hebrew speech-act-efficacy sibling-cluster now in production. Bidirectional with `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus`.
- `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` — Ugaritic-side wired with 70+ refIds. The lacuna-bracket convention is now genuinely project-wide across all four source languages.

## The 8 new overlay entries (v1.1.0)

Composition-specific Baal Cycle items:
- `word-of-tree-whisper-of-stone-mystery-revelation-formula-baal-cycle` — the *rgm ʿṣ w lḫšt ʾabn* esoteric-cosmic-communication formula (KTU 1.1-iii:13)
- `iwrkl-obscure-name-or-epithet-baal-cycle-1-2-iii-6` — uncertain reading; Smith 1994 leaves untranslated
- `ast-mssst-obscure-weapon-words-baal-cycle-1-2-i-44` — ʾaṣṭ / mʿsṣṣt; Smith 1994 tentative readings preserved
- `horanu-minor-curse-deity-baal-cycle-1-2-iii-7` — Ḥôrânu; weak cross-corpus reach (only Hebrew Bible place-name Beth-Ḥôrôn carries the divine name)
- Plus 4 additional Baal Cycle-specific entries (kingship-deposition formula; triple-named opening lacuna policy; etc.)

## Items requiring decision

**None at the line/entry level.** Clean reviewer-approved sweep with explicit verbatim disavowals throughout the lens-risk concentrations:

**The 12 lens-risk concentrations — all with explicit, named, verbatim operational disavowals:**

1. **Yahweh-IS-El identity-claim** disavowed (at `el-ugaritic-ilu-...`)
2. **Yahweh-IS-Baʿlu identity-claim** disavowed (at `baal-ugaritic-baalu-...`)
3. **Watchers-engineering reading of bn ʾilm / Gen 6** disavowed (at `bn-ilm-sons-of-god-...`)
4. **Christological Dan 7:13 / Mark 14:62 / Rev 1:7 pre-resolution** from Rider-of-the-Clouds disavowed (at `rider-of-the-clouds-...`)
5. **Christological Gen-3:15-protoevangelium typology** from qdqd head-smiting disavowed (at `qdqd-head-smiting-...`)
6. **Sitchin-Nibiru Mount Ṣapunu fringe** disavowed (at `mount-sapunu-...`)
7. **Sitchin Anunnaki-faction Chaoskampf reading** disavowed (at `chaoskampf-sea-conflict-...`)
8. **Christian-Johannine-Logos pre-resolution** from Kothar's speech-act weapon-naming disavowed (at `yagrush-ayamur-...` and `speech-act-efficacy-...`)
9. **Christian-Mariological pre-resolution** from ʿAnat / ʾAṯirat disavowed (at `anat-...` and `athirat-...`)
10. **Popular-fringe Dagon-as-fish false-etymology** disavowed (at `dagan-dagon-...`)
11. **WoH-Council-of-Eternals reading of pḫr mʿd** disavowed (at `divine-council-phr-mad-...`)
12. **Sitchin-engineered-ET-deity reading of yw** disavowed (at the YW line entry)

**The YW line audit specifically** (the chapter's highest-lens-risk site, KTU 1.1-iv:14, `šm bny yw`):
- ✅ `claim_type` correctly `inferred` (not `direct`)
- ✅ All three named-scholarly readings (de Moor 1971, Cross 1973, Smith 1994) documented faithfully
- ✅ Surface English bare `YW` — no vocalization commitment, no Hebrew-cognation commitment
- ✅ Verbatim disavowal present
- ✅ Sitchin-engineered-ET-deity disavowal explicit
- ✅ Christian-Trinitarian / Yahweh-Christology pre-resolution disavowal explicit

**One project-level caveat**: the `verificationStatus: best-effort reconstruction; verification pending against KTU³ (Dietrich-Loretz-Sanmartín 2013)` flag remains in the chapter file. The Editor and Reviewer both verified that the lens-discipline + glossary work is independent of (and complementary to) the sign-level verification that remains as future work. The English surface reflects the well-attested sense of each line across editions (Smith 1994, Pardee 2003, Gibson 1978, Ginsberg 1955); the per-line Ugaritic transliteration may have sign-level reconstruction errors that would be caught by a verification pass against KTU³'s primary critical edition. This is the second text shipped with the verificationStatus convention (Adapa was first).

## Editor escalation report (inlined)

See `chapter-1-editor-report.md` — no speculative entries; 18 new central entries with full disavowal-discipline apparatus; 8 new overlay entries; 2 existing-entry Ugaritic-side activations; the verificationStatus caveat preserved.

## Reviewer report (inlined)

Appended to `chapter-1.json` `translation.reviewerReport`: 226 line verdicts (all approve), 26 glossary verdicts (all approve), 0 lens-leakage flags. The Reviewer independently audited each of the 12 lens-risk concentrations, the YW-line handling specifically, the bidirectional Akkadian↔Ugaritic↔Hebrew speech-act-efficacy sibling-cluster wiring, and the etymological-cognate-vs-comparative-mythology distinction (Akkadian↔Ugaritic↔Hebrew = real Semitic-cognate; Sumerian↔Ugaritic = comparative-mythology-typological-only). 5+ named-scholarship citations spot-checked against Smith 1994, Cross 1973, Day 2000, Pardee 2003, Izre'el 2001 — all positions accurately attributed.

## Recommendation

Clean pass on philology, glossary architecture, lens-discipline, and the three-way + four-way cross-language sibling-cluster pattern. **The project's first Ugaritic-source text and first Levantine-tradition text — and the most lens-risk-heavy text in the WoH corpus (the comparative-mythology center of gravity for Hebrew Bible scholarship) — has landed with strict named-scholarly-literary discipline at every risk-concentration.** The Sitchin/popular-fringe / Christian-typological / Yahweh-IS-Baʿlu-or-El identity-claim temptations are explicitly disavowed in the rationales; the legitimate cross-corpus comparative-mythology and (where genuinely philological) Northwest-Semitic Semitic-cognate work is fully documented as named scholarship. The YW line — the chapter's biggest single lens-risk — is handled with the precise philological humility that the genuinely-contested debate requires.

If you agree, reply **sign-off ok** and I'll ship the Baal Cycle KTU 1.1 + 1.2 — the **first Levantine text** live, the **first Ugaritic text** live, the **first text with original-script Unicode in the source file from day one**, and the **largest single-pass glossary expansion in project history** (+18 central + 8 overlay). The verification-pass against KTU³ Dietrich-Loretz-Sanmartín 2013 remains as future work; the lens-discipline and glossary architecture in production are independent of and unaffected by that pending verification.
