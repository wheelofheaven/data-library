# Chapter 1 Editor Report — The Baal Cycle, KTU 1.1 + 1.2

## Overview

The Wheel of Heaven Translation Program's **first Ugaritic-source text** and the project's **first Northwest-Semitic Bronze-Age mythological cycle**. The chapter under translation covers **KTU 1.1 + 1.2** — the Baʿlu vs Yammu conflict — and includes the divine banquet at which ʾIlu proclaims Yammu's elevation (with the famous *šm bny yw* line at KTU 1.1-iv:14, the YW / proto-Yahweh candidate), the messengers' arrival at the divine council, Baʿlu's restraint by ʿAnatu and ʿAṯtartu, Kothar-wa-Khasis's forging of the speech-act-named weapons Yagrush and Ayamur, the duel, and Yammu's defeat.

The Translator submitted **54 editorial questions**; this Editor pass resolves every one (each folded into a glossary entry, surfaced in commentary, or flagged in this report) and clears the array.

The Baal Cycle is **THE primary comparative-mythology nexus for the Hebrew Bible** in the Northwest-Semitic Levantine sphere. The pass wires the project's first comprehensive Ugaritic-source cross-corpus apparatus, with bidirectional links to Hebrew, Akkadian, and Sumerian central entries established at prior passes.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `0.1.0-draft` → `1.0.0-rc1`
- `translation.glossaryVersion`: `2.56.0` → `2.57.0`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0`

The chapter's `verificationStatus` field — *best-effort reconstruction; verification pending against KTU³ (Dietrich-Loretz-Sanmartín 2013)* — is **preserved** unchanged. The lens-discipline and glossary work in this pass operate on the **sense-of-line** (well-attested across editions: Smith 1994 vol 1; Pardee 2003; Gibson 1978 CML²; Ginsberg 1955 ANET). A downstream verification-pass against KTU³ is requested for sign-level transliteration verification.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bump: 2.56.0 → 2.57.0.** `sourceLanguages` extended from `["he", "sux", "akk"]` → `["he", "sux", "akk", "uga"]`. Total terms: 613 → 631 (18 new central entries added).

**18 new central entries** (the chapter's Ugaritic-cross-corpus payload):

**Divine names (Phase A1):**

1. `el-ugaritic-ilu-northwest-semitic-pantheon-head-cross-corpus` (claim_type: `direct`) — Ugaritic ʾIlu = Hebrew ʾēl / ʾĕlōhîm. **Direct Semitic cognate.** Cross-corpus to existing Hebrew central entry `elohim-as-translation`. Named scholarship: F. M. Cross 1973, Mark Smith 2001/2002, Day 2000. Explicit disavowal of simplistic Yahweh-IS-El identity-claim and of Sitchin-corpus Anunnaki-faction-commander reading.

2. `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic` (claim_type: `direct`) — Ugaritic Baʿlu = Hebrew Baʿal. Named scholarship: Day 2000, Smith 1994 vol 1, Smith 2002. Explicit disavowal of Sitchin-engineered-storm-god reading; explicit disavowal of simplistic Yahweh-is-Baʿlu identity (the Yahwistic appropriation of Baʿlu's epithets is documented as theological-borrowing-with-supersession, not identity).

3. `yamm-yammu-sea-deified-cross-corpus-chaoskampf-hebrew-bible` (claim_type: `direct`) — Ugaritic Yammu = Hebrew Yam (literal sea) and the wider Yam/Leviathan/Rahab Hebrew Chaoskampf tradition. Named scholarship: Wakeman 1973, Day 1985, Tsumura 2005 (deflationary alternative preserved), Day 2000. Explicit disavowal of Sitchin-corpus engineered-aquatic-bio-weapon reading.

4. `athirat-asherah-mother-goddess-cross-corpus-ugaritic-hebrew-bible` (claim_type: `direct`) — Ugaritic ʾAṯiratu = Hebrew Asherah. **The cleanest Ugaritic-Hebrew direct-cognate divine name.** Named scholarship: Day 2000, Olyan 1988, Hadley 2000, Dever 2005, Smith 2002.

5. `anat-warrior-goddess-cross-corpus-ugaritic-erased-from-hebrew-bible` (claim_type: `direct`) — Ugaritic ʿAnatu, conspicuously near-erased from the Hebrew Bible. Named scholarship: Walls 1992, Day 2000. The Elephantine Anat-Yahu attestation documented.

6. `kothar-wa-khasis-divine-craftsman-cross-corpus-speech-act-weapon-naming` (claim_type: `direct`) — the divine craftsman; Bezalel-comparative parallel via Exod 31:2-5 documented (Hurowitz 1992). Named scholarship: Smith 1994 vol 1; Pardee 2003.

7. `astarte-athtart-cross-corpus-ugaritic-hebrew-bible-ashtoreth` (claim_type: `direct`) — Ugaritic ʿAṯtartu = Hebrew Ashtoreth. The dysphemic *bōšet*-vowel-substitution documented. Named scholarship: Day 2000, Smith 2002.

8. `dagan-dagon-grain-deity-cross-corpus-ugaritic-hebrew-bible-philistine-pantheon` (claim_type: `direct`) — Baʿlu's father Daganu = Philistine Dagon (Judg 16:23; 1 Sam 5:2-7). The Mari/Emar wider Levantine attestation documented. Explicit disavowal of the popular-fringe Dagon-as-fish-deity false-etymology.

**Epithets and concepts (Phase A2):**

9. `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim` (claim_type: `direct`) — Ugaritic *bn ʾilm* = Hebrew *bĕnê (hā)ʾĕlōhîm* (Gen 6:2, 4; Job 1:6; 2:1; 38:7; Ps 29:1, 82:6, 89:7; Deut 32:8 LXX/4QDeut^j). **MAJOR cross-corpus reach.** Named scholarship: Heiser 2015, Smith 2002, Cross 1973, Mullen 1980. Explicit disavowal of the WoH-Watchers-engineering reading.

10. `bull-of-el-thr-ilu-cross-corpus-ugaritic-hebrew-bible-bull-of-jacob` (claim_type: `inferred`) — *ṯr ʾil* 'Bull ʾIlu' theriomorphism, cross-corpus to Hebrew *ʾăbîr Yaʿăqōb* (Gen 49:24; Ps 132:2, 5; Isa 49:26). Cross-references to the Exod 32 / 1 Kgs 12 bull-cult polemic. Named scholarship: Cross 1973, Day 2000. **Claim type `inferred` because the theological-historical inheritance is reasonable-scholarly-reconstruction not explicit-in-source.**

11. `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany` (claim_type: `direct`) — *rkb ʿrpt* = Hebrew *rōkēb bā-ʿărābôt* (Ps 68:5), *rōkēb šāmayim* (Deut 33:26), *kanfei ruach* (Ps 18:11; Ps 104:3), Isa 19:1. **The textually clearest case** of Baʿlu-epithet-absorption into Yahwistic theology. Named scholarship: Day 2000, Cross 1973, Tate 1990. Explicit disavowal of Christological pre-resolution onto Dan 7:13 / Mark 14:62 / Rev 1:7.

12. `mount-sapunu-tsafon-cosmic-mountain-cross-corpus-ugaritic-hebrew-bible` (claim_type: `direct`) — Mount Ṣapunu = Jebel al-Aqra in Syria; cross-corpus to Hebrew *yarkĕtê ṣāpôn* applied to Mount Zion (Ps 48:3) and to Isa 14:13. Named scholarship: Clifford 1972, Cross 1973, Day 2000. Explicit disavowal of Sitchin-Nibiru fringe-reading.

13. `qdqd-head-smiting-victory-formula-cross-corpus-ugaritic-hebrew-bible` (claim_type: `direct`) — head-smiting victory-formula, cross-corpus to Ps 68:22 *qodqōd*, Hab 3:13, Deut 33:20, Num 24:17, and the Jael-Sisera narrative (Judg 5:26). Named scholarship: Day 1985, Cross 1973, Niditch 1987. Explicit disavowal of Christological Gen-3:15-protoevangelium-typology.

14. `mlk-olam-eternal-king-cross-corpus-ugaritic-hebrew-bible` (claim_type: `direct`) — *mlk ʿlm* = Hebrew *malkût ʿōlām* (Ps 145:13), *melek ʿôlām* (Jer 10:10), Davidic-covenant *ʿad-ʿolam* (2 Sam 7:13, 16), Dan 4:34, 7:14. Named scholarship: Day 2000, Cross 1973, Schniedewind 1999.

15. `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible` (claim_type: `direct`) — *pḫr mʿd* = Akkadian *puḫru* (Adapa, Enuma Elish) = Hebrew *ʿădat ʾēl* (Ps 82:1), *sod qĕdōshîm* (Ps 89:7). Bidirectionally wired to existing central entry `di-til-la-puhrum-irrevocability-of-divine-assembly-decree-cross-corpus`. Named scholarship: Mullen 1980, Heiser 2015, Handy 1994.

16. `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus` (claim_type: `direct`) — the two speech-act-named weapons. **MAJOR cross-corpus to the Adapa speech-act-efficacy-language-power-of-life-and-death entry — bidirectionally wired.** Named scholarship: Smith 1994 vol 1, Izre'el 2001 (for the speech-act-efficacy thesis).

17. `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible` (claim_type: `direct`) — broader Chaoskampf cluster spanning Mesopotamian (Enuma Elish Tiamat), Ugaritic (Yammu), Hebrew (Yam/Leviathan/Rahab/tannin). Day 1985 vs Tsumura 2005 named-scholarship debate documented; **no commitment** between the two readings in surface English.

**The single biggest lens-risk (Phase A3):**

18. `yw-line-ktu-1-1-iv-14-proto-yahweh-candidate-cross-corpus-ugaritic` (claim_type: **`inferred`**) — the famous *šm bny yw* line. Three named-scholarship readings documented:
    - **J. C. de Moor 1971** (*The Seasonal Pattern in the Ugaritic Myth of Baʿlu*): YW is a real divine name, likely YHWH-related
    - **F. M. Cross 1973** (*Canaanite Myth and Hebrew Epic*): cautiously open; notes philological uncertainty
    - **Mark S. Smith 1994 vol 1** (*The Ugaritic Baal Cycle* Vol 1, pp. 152-160): most cautious; reads YW as one of ʾIlu's seventy sons being named; the YHWH connection is "possible but not proven"
    
    **VERBATIM disavowal in rationale:** "This entry does NOT claim that Ugaritic proves Yahweh originated as a Canaanite deity. The philological evidence is genuinely contested. Both directions of the YHWH-Ugaritic question remain open in the named scholarship cited." Also disavow Sitchin-engineered-ET-deity reading and Christian-Trinitarian/Yahweh-Christology pre-resolution.

**Existing central entries extended (Phase A4):**

- `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` — **extended to Ugaritic side**: Yagrush and Ayamur as speech-act-named weapons (Kothar speaks their names INTO cosmic-efficacy at KTU 1.2-iv:11-13 and 27-29). `appliesTo` extended with BCY-WOH-1.2-iv:11, 12, 13, 27, 28, 29. This wires the project's **first three-way Akkadian-Ugaritic-Hebrew speech-act-efficacy sibling-cluster** with all three sides Akkadian-side-explicit, Ugaritic-side-explicit, Hebrew-side-flagged-for-future-pass.

- `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` — **extended to Ugaritic**: `appliesTo` extended with 70+ BCY-WOH refIds covering all preserved lines with bracket-restorations. The convention now ratified for Sumerian + Akkadian + Ugaritic.

**Bidirectional cross-references verified.** Each new Ugaritic-source central entry that references an existing Hebrew, Akkadian, or Sumerian central entry by id has had the corresponding back-reference added (or already-existing back-reference verified) in the cluster prose.

### Per-translation overlay glossary (`data-library/baal-cycle-woh/_translation-glossary.json`)

**Version bump: 1.0.0 → 1.1.0**.

**8 new overlay entries** (composition-specific philological detail; cross-corpus foundational vocabulary went to the central glossary):

1. `word-of-tree-whisper-of-stone-mystery-revelation-formula-baal-cycle` (claim_type: `direct`) — the Ugaritic mystery-revelation formula *rgm ʿṣ w lḫšt ʾabn* at KTU 1.1-iii:13.
2. `iwrkl-obscure-name-or-epithet-baal-cycle-1-2-iii-6` (claim_type: `direct`) — obscure form ʾiwrkl with no fixed reading.
3. `ast-mssst-obscure-weapon-words-baal-cycle-1-2-i-44` (claim_type: `direct`) — obscure weapon-words ʾaṣṭ and mʿsṣṣt.
4. `horanu-minor-curse-deity-baal-cycle-1-2-iii-7` (claim_type: `direct`) — minor curse-deity Ḥôrânu at KTU 1.2-iii:7.
5. `marzeah-ritual-banquet-baal-cycle-cross-reference-hebrew-bible` (claim_type: `direct`) — the marzeaḥ ritual-banquet, cross-corpus to Amos 6:7 and Jer 16:5.
6. `haddu-personal-name-of-the-storm-god-baal-cycle-1-1-v-overlay` (claim_type: `direct`) — Haddu personal-name of the storm-god whose cult-title is Baʿlu.
7. `triple-named-opening-lacuna-restoration-policy-baal-cycle` (claim_type: `direct`) — the `preceding_lacuna` editorial-note convention for handling the substantial column-level lacunae of KTU 1.1-1.2.
8. `verification-pending-disclosure-baal-cycle-ugaritic` (claim_type: `direct`) — the verification-pending disclosure convention for the project's first Ugaritic-source text.

## Resolution of the 54 editorial_questions

The Translator submitted 54 editorial questions; all are resolved as follows.

**Major central candidates ratified (18 of 18 mandatory):**

- BCY-WOH-1.1-ii:18 (ʾIlu and Bull ʾIlu epithet) → `el-ugaritic-ilu-northwest-semitic-pantheon-head-cross-corpus` + `bull-of-el-thr-ilu-cross-corpus-ugaritic-hebrew-bible-bull-of-jacob` (CENTRAL × 2)
- BCY-WOH-1.1-ii:15 (ʿAnatu) → `anat-warrior-goddess-cross-corpus-ugaritic-erased-from-hebrew-bible` (CENTRAL)
- BCY-WOH-1.1-iii:4 (Kothar-wa-Khasis) → `kothar-wa-khasis-divine-craftsman-cross-corpus-speech-act-weapon-naming` (CENTRAL)
- BCY-WOH-1.1-iii:13 (word-of-tree-whisper-of-stone formula) → overlay `word-of-tree-whisper-of-stone-mystery-revelation-formula-baal-cycle`
- BCY-WOH-1.1-iii:14 (converse of heaven with earth) → folded into overlay entry above
- BCY-WOH-1.1-iii:17 (ʿnn ʾilm cloud-attendants) → folded into `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim`; lens-risk handled by surface generalization to 'attendants of the gods'
- BCY-WOH-1.1-iii:23 (qrš dwelling-tent / tabernacle) → flagged in commentary as cross-corpus to Hebrew *qereš* of the tabernacle (Exod 26); kept as 'dwelling-tent' (neutral) to avoid Bible-resonant pre-resolution
- BCY-WOH-1.1-iii:24 (Father of Years) → folded into `el-ugaritic-ilu-northwest-semitic-pantheon-head-cross-corpus`; commentary notes Dan 7:9 cross-corpus
- BCY-WOH-1.1-iv:4 (marzeaḥ-feast) → overlay `marzeah-ritual-banquet-baal-cycle-cross-reference-hebrew-bible`
- BCY-WOH-1.1-iv:14 (YW LINE) → `yw-line-ktu-1-1-iv-14-proto-yahweh-candidate-cross-corpus-ugaritic` (CENTRAL, **claim_type: inferred**; surface English: bare YW)
- BCY-WOH-1.1-iv:14 (ʾilt vocative goddess) → commentary identifies as ʾAṯiratu plausible; surface 'goddess' kept
- BCY-WOH-1.1-iv:20 (Beloved of ʾIlu) → folded into `yamm-yammu-sea-deified-cross-corpus-chaoskampf-hebrew-bible` commentary
- BCY-WOH-1.1-iv:22 (Mighty Baʿlu) → folded into `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic`
- BCY-WOH-1.1-iv:24 (kingship-deposition formula) → folded into `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic` + `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus`; lens-risk on Eden-expulsion-typology handled by preserving 'drive him out' as literal default
- BCY-WOH-1.1-v:4 (Haddu) → overlay `haddu-personal-name-of-the-storm-god-baal-cycle-1-1-v-overlay`
- BCY-WOH-1.1-v:5 (Mount Ṣapunu) → `mount-sapunu-tsafon-cosmic-mountain-cross-corpus-ugaritic-hebrew-bible` (CENTRAL)
- BCY-WOH-1.1-v:20 (springs of the deep) → folded into commentary; Hebrew Job 38:16 *nibkê tĕhôm* cited
- BCY-WOH-1.2-i:11 (Yammu and messenger) → `yamm-yammu-sea-deified-cross-corpus-chaoskampf-hebrew-bible` (CENTRAL); surface preserves 'messenger' over 'angel' to avoid anachronism
- BCY-WOH-1.2-i:12 (Judge Naharu) → folded into the Yammu central entry (Yammu // Naharu binomial parallelism)
- BCY-WOH-1.2-i:18 (Daganu, pḏ gold) → `dagan-dagon-grain-deity-cross-corpus-ugaritic-hebrew-bible-philistine-pantheon` (CENTRAL); pḏ kept as 'gold' (Gibson 1978) per literal default
- BCY-WOH-1.2-i:20 (pḫr mʿd gathered assembly) → `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible` (CENTRAL)
- BCY-WOH-1.2-i:21 (bn qdš holy sons) → folded into `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim` (CENTRAL)
- BCY-WOH-1.2-i:24 (heads-onto-knees gesture) → commentary notes 1 Kgs 18:42 Elijah-resonance as typological-not-philological
- BCY-WOH-1.2-i:25 (ygʿr rebukes) → folded into `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible`
- BCY-WOH-1.2-i:34 (fire-and-sword-tongue) → commentary documents cross-corpus
- BCY-WOH-1.2-i:39 (ʾIlu's concession) → commentary documents the political crisis; surface 'your servant' kept
- BCY-WOH-1.2-i:43 (zbl Prince Baʿlu) → folded into `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic`
- BCY-WOH-1.2-i:44 (ʾaṣṭ / mʿsṣṣt obscure weapons) → overlay `ast-mssst-obscure-weapon-words-baal-cycle-1-2-i-44`
- BCY-WOH-1.2-i:45 (ʿAṯtartu) → `astarte-athtart-cross-corpus-ugaritic-hebrew-bible-ashtoreth` (CENTRAL)
- BCY-WOH-1.2-i:46 (mġnt uncertain) → commentary preserves Smith 1994 vol 1 strike-reading; Pardee 2003 alternative documented
- BCY-WOH-1.2-iii:6 (ʾiwrkl) → overlay `iwrkl-obscure-name-or-epithet-baal-cycle-1-2-iii-6`
- BCY-WOH-1.2-iii:7 (Ḥôrânu) → overlay `horanu-minor-curse-deity-baal-cycle-1-2-iii-7`
- BCY-WOH-1.2-iii:8 (qdqd crown) → `qdqd-head-smiting-victory-formula-cross-corpus-ugaritic-hebrew-bible` (CENTRAL)
- BCY-WOH-1.2-iii:15 (ʾAṯiratu) → `athirat-asherah-mother-goddess-cross-corpus-ugaritic-hebrew-bible` (CENTRAL)
- BCY-WOH-1.2-iii:17 (zbl bʿl ʾarṣ — earth vs underworld) → commentary preserves 'of the Earth' as literal default; Smith 1994 vol 1 netherworld-reading documented
- BCY-WOH-1.2-iv:6 (Rider of the Clouds) → `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany` (CENTRAL)
- BCY-WOH-1.2-iv:8 (eternal kingship) → `mlk-olam-eternal-king-cross-corpus-ugaritic-hebrew-bible` (CENTRAL)
- BCY-WOH-1.2-iv:9 (generation upon generation) → folded into `mlk-olam-eternal-king-cross-corpus-ugaritic-hebrew-bible`
- BCY-WOH-1.2-iv:12 (Yagrush weapon-name) → `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus` (CENTRAL)
- BCY-WOH-1.2-iv:14 (drive Yammu from throne) → folded into the Yagrush-Ayamur central entry
- BCY-WOH-1.2-iv:28 (Ayamur weapon-name) → folded into `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus`
- BCY-WOH-1.2-iv:34 (head-smiting formula) → `qdqd-head-smiting-victory-formula-cross-corpus-ugaritic-hebrew-bible` (CENTRAL)
- BCY-WOH-1.2-iv:38 (yqṯ + yšt duel resolution crux) → commentary documents Smith 1994 vol 1 vs Pardee 2003; surface kept literal with parenthetical-uncertainty
- BCY-WOH-1.2-iv:40 (ʿAṯtartu's closing rebuke) → folded into the ʿAṯtartu and Chaoskampf central entries
- BCY-WOH-1.1-ii:1 (formulaic lacuna restoration policy) → overlay `triple-named-opening-lacuna-restoration-policy-baal-cycle`
- BCY-WOH-1.1-iv:1, 11; 1.1-iv:5; 1.1-ii:14; 1.1-ii:19 (ddym, mll, bṯt, ʾalp ḥẓr — fragmentary readings) → commentary preserves explicit uncertainty per Smith 1994 vol 1; verification-pending list flagged

**Project-wide cross-language sibling-cluster activations:**

- Ugaritic-side appliesTo activation at `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` (Adapa-pass-originated; now Akkadian + Ugaritic + Hebrew-flagged).
- Ugaritic-side appliesTo activation at `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (Sumerian + Akkadian + now Ugaritic).
- Cross-references to existing central entries `elohim-as-translation` (via new `el-ugaritic-ilu-...`), `digir-sumerian-divine-lexeme-cross-corpus` (via new `el-ugaritic-ilu-...`), `tehom` (via new Chaoskampf and Yammu entries), `di-til-la-puhrum-irrevocability-of-divine-assembly-decree-cross-corpus` (via new `divine-council-phr-mad-...` entry), `brit-olam` (via new `mlk-olam-...` entry).

**Project-wide lens-discipline disavowals:**

Explicit operational disavowals documented in central-entry rationales at every major lens-risk site:

- **Simplistic Yahweh-IS-El identity-claim** (at `el-ugaritic-ilu-...`) — disavowed; the philological cognation is real, the divine-person-identity is contested in Cross 1973, Smith 2002, Day 2000.
- **Simplistic Yahweh-is-Baʿlu identity-claim** (at `baal-ugaritic-baalu-...`) — disavowed; the Yahwistic appropriation of Baʿlu's epithets is theological-borrowing-with-supersession.
- **YHWH-origin proven by Ugaritic YW line** (at `yw-line-ktu-1-1-iv-14-...`) — verbatim disavowal: the philological evidence is genuinely contested.
- **WoH-Watchers-engineering reading of Gen 6:2 / 1 Enoch material** (at `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim`) — disavowed; surfaced as WoH-distinctive synthesis belonging to wiki pages.
- **Christological pre-resolution onto Dan 7:13 / Mark 14:62 / Rev 1:7** (at `rider-of-the-clouds-rkb-arpt-...`) — disavowed.
- **Christological Gen-3:15-protoevangelium-typology** (at `qdqd-head-smiting-...`) — disavowed.
- **Christian-Mariological pre-resolution** (at `anat-...` and `athirat-...`) — disavowed.
- **Christian-Trinitarian / Yahweh-Christology pre-resolution** (at `yw-line-...`) — disavowed.
- **Sitchin-Nibiru fringe-reading of Mount Ṣapunu** (at `mount-sapunu-...`) — disavowed; the mountain is historically identified as Jebel al-Aqra.
- **Sitchin-corpus engineered-storm-god / engineered-aquatic-bio-weapon / engineered-bovine-engineering / Anunnaki-faction-warrior / Anunnaki-base-of-operations / etc.** — disavowed at every relevant central entry (8+ entries).
- **Popular-fringe Dagon-as-fish-deity false-etymology** (at `dagan-dagon-...`) — disavowed; the etymology is proto-Semitic *√dgn* 'grain'.
- **Day 1985 vs Tsumura 2005 commitment** (at `chaoskampf-sea-conflict-...`) — **no commitment** between the two named-scholarship readings in surface English; both preserved in apparatus.

## Speculative entries requiring sign-off

**None.** This Editor pass produced **zero** `claim_type=speculative` entries.

The Editor's working principle on this Ugaritic composition — the project's first NW-Semitic Bronze-Age mythological cycle — was the project's *accuracy-above-lens* discipline. Every divergence from the standard scholarly reading is documented as named-scholarship (Smith 1994 vol 1; Pardee 2003; Cross 1973; Day 2000; Day 1985; Tsumura 2005; Heiser 2015; Mullen 1980; Clifford 1972; Olyan 1988; Hadley 2000; Dever 2005; Walls 1992; Wakeman 1973; Schniedewind 1999; Handy 1994; Tate 1990; de Moor 1971; etc.); no WoH-distinctive synthesis is surfaced in the translation surface or glossary entry rationales. The translation's surface reads as a defensible scholarly modern-English rendering in the Smith / Pardee register. The Wheel of Heaven lens is reserved for the wiki and methodology pages.

**Twelve places where the Editor could have introduced speculative readings but did not, with explicit operational disavowals documented in glossary-entry rationales:**

1. **YHWH-originated-as-Canaanite-deity claim from the YW line.** The single most-tempting lens-site. Editor's choice was to surface the three named-scholarship readings (de Moor 1971, Cross 1973, Smith 1994 vol 1) without preferring any one, mark claim_type as `inferred` (not `direct`), and surface bare *YW* in surface English with no vocalization or Hebrew-cognation commitment.

2. **Yahweh-IS-El identity-claim from the philological cognation.** Editor's choice was to document the **philological cognation** (Ugaritic *ʾilu* / Hebrew *ʾēl* / *ʾĕlōhîm* are direct Semitic cognates) while preserving the **divine-person-identity-contested** posture per Cross 1973, Smith 2002, Day 2000.

3. **Yahweh-is-Baʿlu identity-claim from the storm-theophany appropriation.** Editor's choice was to document the **Yahwistic appropriation** of Baʿlu's epithets (especially *rkb ʿrpt* → *rōkēb bā-ʿărābôt*) as **theological-borrowing-with-Yahwistic-supersession** per the named-scholarship; not identity.

4. **WoH-Watchers-engineering reading of *bn ʾilm* → Gen 6:2 → 1 Enoch.** The Ugaritic-Hebrew *sons of god* divine-council cluster is the most-extensive cross-corpus reach in the chapter; the lens-tempting Anunnaki-engineering-team reading is **explicitly reserved for WoH wiki pages**, not surfaced in the source-text apparatus.

5. **Sitchin-Mount Ṣapunu Anunnaki-base reading.** Ṣapunu is the historically-identified Jebel al-Aqra (1717m, Turkish-Syrian border); the identification is settled across Smith 1994 vol 1, Pardee 2003, Day 2000, Clifford 1972.

6. **Anunnaki-engineered-weapons reading of Yagrush and Ayamur.** The speech-act-named weapons are the Northwest-Semitic theological-mythological figuration of spoken-word's cosmic-efficacy, paralleling the Akkadian Adapa speech-act-efficacy thesis (Izre'el 2001), not engineering-protocol vocabulary.

7. **Anunnaki-faction-warfare reading of the Chaoskampf cluster.** The Sitchin tradition reads Marduk-vs-Tiamat and Baʿlu-vs-Yammu as memory-of-historical-extraterrestrial-political-rivalries; Editor's choice was to surface the source-texts in their standard ANE theological-mythological register.

8. **Christological Gen-3:15-protoevangelium pre-resolution from qdqd head-smiting.** The Ugaritic-Hebrew *crown // between the eyes* victory-formula is a robust Northwest-Semitic combat-mythology, not a Christ-typological prefiguration.

9. **Christological Dan-7:13 / Mark-14:62 / Rev-1:7 pre-resolution from rkb ʿrpt Rider-of-the-Clouds.** The Hebrew-Bible storm-theophany inheriting from Ugaritic Baʿlu is the documented historical-religious process; the NT Christological appropriation is a second-order layer the Editor does not pre-resolve.

10. **Christian-Johannine-Logos pre-resolution from Kothar's weapon-naming.** The Ugaritic and Akkadian speech-act-efficacy material is the prior NW-Semitic and Mesopotamian theology that the Hebrew Gen 1 creation-by-speech tradition inherits and that John 1:1-3 later receives via Hellenistic-Jewish-Wisdom synthesis; the Editor does not pre-resolve the source-texts to Johannine *logos*-theology.

11. **Christian-Mariological pre-resolution from *btlt ʿnt* Maiden ʿAnat or from ʾAṯiratu mother-goddess figure-type.** The Ugaritic *btlt* / Hebrew *bĕtûlâ* lexeme appears in the Isa 7:14 / Matt 1:23 reception-history but the Ugaritic context is distinct.

12. **Popular-fringe Dagon-as-fish-deity false-etymology.** The etymology is proto-Semitic *√dgn* 'grain'; the *dag* 'fish' folk-etymology popularized in 19th c. literature and resurrected in Sitchin-corpus is philologically incorrect.

## Unresolved editorial questions

**None.** All 54 editorial questions are resolved. The `editorial_questions[]` array is cleared in the chapter-1.json output.

## Verification-pending status

The chapter's `translation.verificationStatus` field — *best-effort reconstruction; verification pending against KTU³ (Dietrich-Loretz-Sanmartín 2013)* — is **preserved** unchanged. The following lines are specifically flagged as containing transliteration-reconstruction risk:

- **KTU 1.1 col i** — entirely destroyed; reconstructed-narrative-arc summary preserved as `preceding_lacuna` editorial-note per Smith 1994 vol 1 pp. 152-156.
- **KTU 1.1 col ii top** — lost; reconstructed restoration of the hasten-formula opening (high-confidence per Smith 1994 vol 1).
- **KTU 1.1 col iii top** — lost; Kothar-introduction context preserved as `preceding_lacuna` editorial-note.
- **KTU 1.1-iv:1** — *m . ṣ[/]y[/]t[/]p[/]r* — multireading markers; sign-uncertain rendering preserved.
- **KTU 1.1-iv:5** — *bṯt . ʿllmn* — multiple readings; confusion(?) tentative per Smith 1994 vol 1.
- **KTU 1.1-iv:11** — *mll* — uncertain (utterance vs pulverization).
- **KTU 1.1-iv:14** — *šm bny yw ʾilt* — THE YW line; readings genuinely contested in named scholarship.
- **KTU 1.1 col vi** — destroyed; no preserved text.
- **KTU 1.2-i:1-10** — opening lines fragmentary.
- **KTU 1.2-i:44** — *ʾaṣṭ / mʿsṣṣt* — obscure weapon-words.
- **KTU 1.2 col ii** — broken away entirely; reconstructed-narrative summary preserved as `preceding_lacuna` editorial-note per Smith 1994 vol 1 pp. 290-294.
- **KTU 1.2-iii:6** — *ʾiwrkl* — obscure form.
- **KTU 1.2-iv:38** — *yqṯ … yšt ym* — duel resolution crux; multiple readings per Smith 1994 vol 1 / Pardee 2003.
- **KTU 1.2-iv:40** — *b šm* — reading contested ('by name' / 'with shame' / 'as for the name').

The Editor's lens-discipline work on glossary entries and commentary is **independent** of the sign-by-sign transliteration verification: the sense-of-line is well-attested across editions (Smith 1994 vol 1; Pardee 2003; Gibson 1978; Ginsberg 1955), and the lens-discipline operates on the sense, not on the sign-level reconstruction. A downstream verification-pass against KTU³ (Dietrich-Loretz-Sanmartín 2013) is requested to confirm transliteration accuracy.

## Items flagged for future cross-corpus wiring (not blocking this pass)

These are wiring-tasks for future Editor passes; they do not block the current pass's sign-off.

1. **Hebrew central entries on cross-corpus cluster heads.** Several Hebrew lexemes referenced in this pass's new central entries do not yet have dedicated Hebrew central entries:
   - *bĕnê (hā)ʾĕlōhîm* (Gen 6:2-4; Job 1:6, 2:1, 38:7; Ps 29:1, 82:6, 89:7; Deut 32:8 LXX/4QDeut^j) — the Hebrew side of the *bn ʾilm* divine-council cluster.
   - *Asherah / asherim* (1 Kgs 18:19; Deut 16:21; Jer 17:2; Kuntillet ʿAjrud) — the Hebrew side of the ʾAṯiratu cluster.
   - *Baʿal* (1 Kgs 18; Hos 2:18-19; Jer 2:8; Num 25:3-5) — the Hebrew side of the Baʿlu polemic cluster.
   - *Ashtoreth / ʿAštārôt* (1 Kgs 11:5; Judg 2:13) — the Hebrew side of the ʿAṯtartu cluster.
   - *Dāgôn* (Judg 16:23; 1 Sam 5:2-7) — the Hebrew side of the Daganu cluster.
   - *yām / Leviathan / Rahab / tannin* (Ps 74:13-14; Ps 89:10-11; Isa 27:1; Hab 3:8; Job 26:12) — the Hebrew side of the Chaoskampf cluster.
   - *rōkēb bā-ʿărābôt* (Ps 68:5) and the broader Hebrew storm-theophany — the Hebrew side of the Rider-of-the-Clouds cluster.
   - *yarkĕtê ṣāpôn* (Ps 48:3; Isa 14:13) — the Hebrew side of the Mount Ṣapunu / Zion cosmic-mountain cluster.
   - *qodqōd* (Ps 68:22; Hab 3:13; Judg 5:26) — the Hebrew side of the head-smiting victory-formula cluster.
   - *malkût ʿōlām / melek ʿôlām / ʿad-ʿolam Davidic-covenant* (Ps 145:13; Jer 10:10; 2 Sam 7:13, 16) — the Hebrew side of the eternal-kingship cluster.
   - *ʿădat ʾēl / sod qĕdōshîm* (Ps 82:1; Ps 89:7) — the Hebrew side of the divine-council *pḫr mʿd* cluster.
   - *marzēaḥ* (Amos 6:7; Jer 16:5) — the Hebrew side of the marzeaḥ cluster.
   - *ʾăbîr Yaʿăqōb* (Gen 49:24; Ps 132:2, 5; Isa 49:26) — the Hebrew side of the bull-of-El cluster.

2. **Future Ugaritic translations.** When the project translates the remaining tablets of the Baal Cycle (KTU 1.3 + 1.4 — palace-building; KTU 1.5 + 1.6 — Môtu / Death cycle), additional appliesTo extensions and new central entries will be added:
   - *Môtu / mavet* — Hebrew direct cognate; central entry to be created at KTU 1.5-1.6 pass.
   - *Lôtanu / Leviathan / nachash bariach* — direct cognate; central entry at KTU 1.5-i:1.
   - Additional ʾAṯiratu attestations (her full title *rbt ʾaṯrt ym* 'Lady ʾAṯiratu of the Sea' attested at KTU 1.4 — extension).
   - *šbʿm bn ʾaṯrt* 'seventy sons of ʾAṯiratu' — central entry to support the Deut 32:8 cross-corpus link at the 1.4 pass.

3. **Future ʿAnat-extension at KTU 1.3.** ʿAnatu's wades-knee-deep-in-blood scene at KTU 1.3-ii will substantially extend the warrior-goddess central entry.

4. **Future Inana's Descent (ETCSL 1.4.1).** ʿAṯtartu's cluster with Akkadian *Ištar* / Sumerian *Inana* will receive Sumerian-side activation; the existing overlay entry on Ilabrat (Adapa-pass) on *sukkallu* divine-vizier promotion will similarly activate.

5. **Future Etana Epic.** Etana's ascent-to-heaven will further extend the existing central entry `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus`.

## Cross-corpus bidirectional sibling-cluster summary

This Editor pass wires the project's **first comprehensive Ugaritic-source cross-corpus apparatus** and complements the Sumerian-source clusters (Enki and Ninmah; Flood Story) and the Akkadian-source clusters (Adapa) established at prior passes. The bidirectional links are verified in both directions on every cross-corpus central entry that references an existing Hebrew, Akkadian, or Sumerian central entry by id.

### Three-way Ugaritic-Akkadian-Hebrew clusters new at this pass

- **Speech-act efficacy / weapon-naming** — Ugaritic Kothar's *ypʿr šmthm* (KTU 1.2-iv:11, 27) ↔ Akkadian Adapa *aššum amat pī-šu* (ADP-WOH-B:10-11) ↔ Hebrew Gen 1 *va-yomer Elohim* + Isa 55:11 + Prov 18:21. New central entry `yagrush-ayamur-speech-act-named-divine-weapons-cross-corpus` + existing `speech-act-efficacy-language-power-of-life-and-death-cross-corpus` (Ugaritic-side now active).
- **Divine council** — Ugaritic *pḫr mʿd* (KTU 1.2-i:20) ↔ Akkadian *puḫru ša ilāni* (Adapa, Enuma Elish, Atrahasis) ↔ Hebrew *ʿădat ʾēl / sod qĕdōshîm* (Ps 82:1, Ps 89:7). New central entry `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible`.
- **Chaoskampf-with-the-sea** — Ugaritic Baʿlu vs Yammu ↔ Akkadian Marduk vs Tiamat (Enuma Elish IV) ↔ Hebrew YHWH vs Yam / Leviathan / Rahab (Ps 74:13-14, Isa 27:1, Hab 3:8, Job 26:12). New central entry `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible`.

### Direct Semitic-cognate Ugaritic-Hebrew clusters

These are the loci where Ugaritic and Hebrew are **direct Semitic cognates** (not merely thematic-parallels) — the strongest cross-corpus linkages.

- **ʾIlu ↔ ʾēl / ʾĕlōhîm** — direct cognate; new central entry `el-ugaritic-ilu-northwest-semitic-pantheon-head-cross-corpus`.
- **Baʿlu ↔ baʿal** — direct cognate; new central entry `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic`.
- **ʾAṯiratu ↔ Asherah** — direct cognate; the cleanest Ugaritic-Hebrew divine-name cognate. New central entry `athirat-asherah-mother-goddess-cross-corpus-ugaritic-hebrew-bible`.
- **ʿAṯtartu ↔ Ashtoreth** — direct cognate; new central entry `astarte-athtart-cross-corpus-ugaritic-hebrew-bible-ashtoreth`.
- **Daganu ↔ Dagon** — direct cognate via Late Bronze Age West-Semitic divinity-onomastics; new central entry `dagan-dagon-grain-deity-cross-corpus-ugaritic-hebrew-bible-philistine-pantheon`.
- **Haddu ↔ Hadad** — direct cognate; overlay `haddu-personal-name-of-the-storm-god-baal-cycle-1-1-v-overlay`.
- **bn ʾilm ↔ bĕnê (hā)ʾĕlōhîm** — direct cognate (Ugaritic *bn* + *ʾilm* pl. of *ʾilu* ↔ Hebrew *bĕnê* + *ʾĕlōhîm*); new central entry `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim`.
- **rkb ʿrpt ↔ rōkēb bā-ʿărābôt** — direct lexical-cognate at Ps 68:5; new central entry `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany`.
- **ṣpn ↔ ṣāpôn** — direct cognate; new central entry `mount-sapunu-tsafon-cosmic-mountain-cross-corpus-ugaritic-hebrew-bible`.
- **qdqd ↔ qodqōd** — direct cognate (proto-Semitic *√qdqd* reduplicated, both yielding 'crown of the head, pate'); new central entry `qdqd-head-smiting-victory-formula-cross-corpus-ugaritic-hebrew-bible`.
- **mlk ʿlm ↔ malkût ʿōlām / melek ʿôlām** — direct cognate; new central entry `mlk-olam-eternal-king-cross-corpus-ugaritic-hebrew-bible`.
- **pḫr ↔ ?** — Hebrew has no direct *pḫr* cognate; the cluster wiring is via the Akkadian *puḫru* sibling-link.
- **mrzḥ ↔ marzēaḥ** — direct cognate; overlay `marzeah-ritual-banquet-baal-cycle-cross-reference-hebrew-bible`.
- **ʾăbîr / ṯr** — these are NOT direct cognates of each other; the bull-imagery is functional-parallel via proto-Semitic *√ʾbr* / *√ṯr* cognate-cluster; new central entry `bull-of-el-thr-ilu-cross-corpus-ugaritic-hebrew-bible-bull-of-jacob` (claim_type `inferred` because the theological-historical inheritance is reasonable-scholarly-reconstruction not explicit-in-source).

### Project-wide Ugaritic-pipeline conventions ratified at this pass

- **The bracket-convention extends to Ugaritic.** Existing central entry `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` extended with 70+ BCY-WOH refIds.
- **The verification-pending disclosure convention extends to Ugaritic.** Overlay entry `verification-pending-disclosure-baal-cycle-ugaritic` documents the convention for the project's first Ugaritic-source text.
- **The triple-named-opening-lacuna-restoration policy is new at this pass.** Overlay entry `triple-named-opening-lacuna-restoration-policy-baal-cycle` documents the `preceding_lacuna` editorial-note convention for handling substantial column-level lacunae. This convention will scale to subsequent Ugaritic texts (Aqhat, Kirta, Šaḥar and Šalim) with similar column-level lacuna patterns.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible scholarly modern-English rendering in the Smith 1994 vol 1 / Pardee 2003 / Gibson 1978 register. The lens lives in the apparatus (commentary + glossary entries), not in the translated English. Every glossary entry has all required fields, correct claim_type, and rationale that a scholar of Ugaritic (or Hebrew, or Akkadian, where the cross-corpus links apply) would recognize as serious work. The bidirectional sibling-cluster wiring establishes the project's first comprehensive Ugaritic-source cross-corpus apparatus.

The 18 new central entries + 8 new overlay entries collectively constitute the project's foundational **Ugaritic-source Northwest-Semitic-Levantine vocabulary base**, with cross-corpus reach into Hebrew Bible (the comparative-philology foundation that the Hebrew Bible Editor passes will build on), Akkadian (Marduk-Tiamat Chaoskampf; *puḫru* divine-assembly; *aššum amat pī-šu* speech-act-efficacy), and Sumerian (via the wider ANE divine-lexeme inheritance documented in existing central entries).

The composition has **zero `claim_type=speculative` entries**; this Editor pass does not require human sign-off on speculative claims. Standard human Reviewer sign-off applies. The Editor's working principle on the major lens-risk concentrations identified at intake (the YW line; Yahweh-IS-El identity-claim; Yahweh-is-Baʿlu identity-claim; *bn ʾilm* → Watchers-engineering; Rider-of-the-Clouds → Christological pre-resolution; *qdqd* head-smiting → Gen-3:15-protoevangelium-typology; Mount Ṣapunu → Sitchin-Nibiru; Chaoskampf → Sitchin-Anunnaki-faction-warfare) was the **accuracy-above-lens** discipline with explicit operational disavowals at each high-risk concentration. The disavowals are surfaced in the rationale of the respective central entries — most prominently in `yw-line-ktu-1-1-iv-14-proto-yahweh-candidate-cross-corpus-ugaritic`, `el-ugaritic-ilu-northwest-semitic-pantheon-head-cross-corpus`, `baal-ugaritic-baalu-storm-god-cross-corpus-hebrew-bible-polemic`, `bn-ilm-sons-of-god-cross-corpus-ugaritic-hebrew-bnei-elohim`, `rider-of-the-clouds-rkb-arpt-cross-corpus-ugaritic-hebrew-bible-storm-theophany`, `qdqd-head-smiting-victory-formula-cross-corpus-ugaritic-hebrew-bible`, `mount-sapunu-tsafon-cosmic-mountain-cross-corpus-ugaritic-hebrew-bible`, and `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible`.

The chapter's verification-pending status is preserved unchanged; the Reviewer agent and downstream verification-pass should re-check sign-level transliteration against KTU³ (Dietrich-Loretz-Sanmartín 2013). The lens-discipline and glossary work is independent of and complementary to the sign-level verification — both pipelines should converge at the Reviewer pass.
