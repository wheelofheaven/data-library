# Sign-off package — Theogony (theogony-woh), chapter 1, Block D — COMPOSITION COMPLETE

**Scope:** Block D — lines 736–1022 + variant lines 929a–929t (Tartarus concluded; house of
Nyx; the Styx oath procedure; Typhoeus; Zeus's accession and the division of timai; Metis and
Athena's birth; the marriage catalogues; the goddesses with mortal men; the closing seam).
**With this block the full 1042-line composition is complete** (A @1.0.0, B @1.1.0, C @1.2.0,
D @1.3.0).

**Status at hand-off:** `awaiting-human` → **signed off** by zarazinsfuss 2026-08-04 (standing
sign-off; the Reviewer's rulings carried agent consensus); promoted to `stable` / **1.3.0**
at 2026-08-04T13:44:41Z.
**Central glossary:** v2.73.0 — **unchanged across all four blocks; zero THEO refIds in central**
**Overlay glossary:** v1.3.0 (42 entries; +4 new in Block D, 15 appliesTo extensions + 2 at sign-off)

## Summary

| Metric | Value |
|---|---|
| Lines appended | 307 (287 numbered 736–1022 + 20 variant 929a–t); chapter complete at 1042 |
| Block D lines with official commentary | 36 |
| Block D glossary refs | 205 (whole chapter: 435, all resolving) |
| Editorial questions resolved | 13 of 13 |
| Overlay total (final) | 42 (direct: 38, inferred: 4) |
| Reviewer verse verdicts | 38 (approve: 35, flag-for-human: 1, revise: 2) |
| Reviewer glossary verdicts | 19 (all approve) |
| Lens-leakage flags | 0 (0 across all four blocks) |
| Speculative entries | 0 (whole composition) |

## The three reviewer rulings, and how they were resolved

1. **929a–t variant passage (flag-for-human, precedent only).** Both agents endorse
   retain-and-translate-unmarked in source order, doublet status carried by commentary and the
   dedicated overlay entry (provenance verified to Chrysippus apud Galen, *De placitis* 3.8;
   West's bracketing documented; the internal 929s athetesis noted). **Human sign-off ratifies
   this as the corpus's supplement-presentation precedent** (extending the athetized-lines
   convention to `<add>`-supplement blocks). Reader-UI follow-up noted below.
2. **Phobos/Deimos (THEO-934, revise — APPLIED).** Surface changed "Panic and Fear" →
   "Phobos and Deimos" per the Reviewer's convention-consistency ruling (cult-established
   sons of Ares; Zelos/Nike/Kratos/Bia precedent at 384–385; sister Harmonia transliterated in
   the same clause at 937). The Editor had flagged the transliterate case as strong — agent
   consensus through escalation. Evelyn-White's translated rendering remains documented in the
   line note; revert is a one-line edit if the human prefers the reference.
3. **Aidoneus (THEO-913, approve).** Non-normalization affirmed: Ἀιδωνεύς is a distinct
   expanded name-form (*Il.* 5.190, 20.61), not an orthographic variant of Hades.

## Orchestrator actions after review

1. THEO-934 surface + note updated per revise; `personified-abstractions` entry appliesTo += 934.
2. THEO-887 hypometric line (Perseus omits *θεῶν*) documented per the Reviewer's independent
   catch: new line note; `source-orthographic-quirks-verbatim-theogony` appliesTo += 887.
3. Promotion to stable/1.3.0; `_meta.json` → 1042 lines, revision 4.

## Composition completion record (Reviewer's assessment)

With Block D signed off, the full 1042-line Theogony — the Translation Program's first
Archaic-Greek hexameter source — is complete. The Reviewer's composition-level assessment
(from the Block D review): a disciplined, accuracy-first scholarly translation defensible to
a credentialed Hellenist cold; Evelyn-White base tightened from Most 2006 and West 1966;
Greek rather than Latinized forms throughout with the entrenched Panhellenic exceptions
(Apollo, Athena, Achilles, Hephaestus) retained anglicized; difficult registers preserved
unsoftened; every genealogical doublet and text-critical fact in transparent, auditable
apparatus. Its most significant achievement is discipline under temptation: across four
blocks and every major convergence the WoH lens would most want — the Titanomachy/Typhoeus
theomachy, the Styx-oath sanction, the swallowed mētis, the Tartaros prison, the
divine-human hero-lines — the surface says only what the Greek says, the comparative
readings are labeled and quarantined, and not one THEO refId was fused into the central
glossary. The 42-entry overlay (38 direct, 4 inferred, 0 speculative) is a clean, veto-free
record.

## Items noted for the future

1. **Reader-UI**: the /library/ reader should render the 929a–t line numbering and
   doublet status visibly so the supplement block is distinguishable (Reviewer condition on
   the presentation precedent).
2. **Name-convention entry**: make the entrenched-Panhellenic-exception list (Apollo, Athena,
   Achilles, Hephaestus) explicit in `theogony-name-and-title-conventions` (Reviewer
   consistency note; signed off as-is since Block A).
3. **Downstream**: library data sync (data-library → www/api submodules + data-content pages),
   i18n fan-out eligibility, HuggingFace parallel-corpus eligibility (CC0) — separate
   decisions, not part of this sign-off.
4. The optional central specs documented across the four editor reports (gigantes-septuagint
   lexeme, monogenes, succession-conflict-theomachy, Block D fusion spec) all remain
   not-recommended founder-level options.

---

# Editor escalation report (inlined)

# Chapter 1 — Block D Editor Report

**Scope:** Block D — lines 736–1022 + the twenty variant lines 929a–929t (307 line objects), the final block of the composition.
**Editor:** claude-opus-4-8[1m] acting as woh-editor.
**Chapter state after this pass:** `translation.status` = `editor-review`, `translation.version` = `1.3.0-rc1`, scope-D marker = `editor-review`; `editorial_questions[]` cleared (13 → 0).
**Overlay after this pass:** `_translation-glossary.json` v1.2.0 → **v1.3.0** (semver-minor: 4 additions + 15 appliesTo extensions; no existing entry's semantic fields modified).
**Blocks A–C (1–735) and all `reviewer*` fields are untouched and immutable.**
**Surface (`i18n.en`) wording unchanged from the Translator's draft** — every Block-D decision is carried by commentary + glossary; the normalizations (Hades, Olympos, Iolkos) and verbatim source-quirks were already applied by the Translator and are here confirmed and governed by entries.

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry was created in Block D. All four new overlay entries are `claim_type=direct` (apparatus / lexical-consistency / source-fidelity conventions); the full overlay is now 38 `direct` + 4 `inferred` (the four inferred are the pre-existing A–C cruxes: `pseudea-etyma-alethea`, `gigantes`, `ein-arimoisin`, `meliai`). Status may advance to `editor-review` without a speculative-sign-off gate. Three presentation calls are nonetheless **flagged for the Reviewer** (below) — they are not speculative, but they are the block's genuine adjudications.

---

## Decisions per editorial question (13/13 resolved)

1. **THEO-929a — variant-passage presentation.** ADJUDICATED (option 1). Retain and translate the 20-line Chrysippus-apud-Galen supplement verbatim in source order after 929, **unmarked** in the reading surface; supplementary/doublet status recorded in commentary at 929a; the internal athetesis of 929s recorded at that line. Governed by the new `variant-passage-929a-929t-metis-doublet-theogony` entry (the athetized-lines philosophy extended from single `<del>` lines to an `<add>` block). **Flagged for the Reviewer** as the block's principal apparatus adjudication.

2. **THEO-784 — Styx oath procedure vs `horkos-styx` scope.** EXTEND (option 2). `horkos-styx-great-oath-theogony` appliesTo extended from THEO-400 to its Block-D payoff sites **784, 805** (the phrase *θεῶν μέγαν ὅρκον* of 784 is verbatim = 400; *horkos* = oath-object/sanction, not the deity *Horkos* of 231). Surface stays literal Evelyn-White; arc-closing note at 784. (This is the scope/appliesTo mechanism used as intended.)

3. **THEO-820 — Typhoeus chaoskampf.** RESOLVED (option 1). Plain surface; serpent-anatomy governed by `ophis-drakon` (scope +825), storm-weapons by `thunder-triad` (scope +839/845/846/854), Tartaros by `tartaros` entry. Near-Eastern combat-myth convergence recorded as clearly-labeled comparative apparatus in the 820 note; central `chaoskampf-sea-conflict-cross-corpus` **NOT extended** to any THEO refId (non-fusion). See CENTRAL section.

4. **THEO-886 — Metis / *mētis* / *ankylomētēs* network.** ADJUDICATED (option 3). Created dedicated `metis-metieta-cunning-counsel-network-theogony` entry (appliesTo 886, 887, 904, 914, 929g, 929n). Name transliterated 'Metis'; *mētieta* rendered 'the counsellor' (per 520); the *mētis*↔*ankylomētēs* etymological network kept in commentary; the signed-off `ankylometes` entry is **documented but not modified**.

5. **THEO-885 — *timai* division vs honour-lexicon scope.** EXTEND (option 2). `time-geras-moira-honor-vocabulary-theogony` appliesTo extended from ≤449 to the accession payoff **882, 885, 892, 904**. Surface literal; arc-closing note at 882.

6. **THEO-884 — Gaia-counsel motif extension.** EXTEND (option 2). `gaia-counsel-prophecy-vocabulary-theogony` appliesTo extended from ≤626 to its culmination **884, 891**. Arc-closing note at 884 back-referencing 463→475→494→626→884.

7. **THEO-902 — Horai / Eunomia / Dike / Eirene.** RESOLVED (option 1). Transliterate 'the Horai' and the names Eunomia/Dike/Eirene as cult-established Seasons-goddesses (parallel to the Charites at 909); transparent senses given in commentary, not glossed inline. Governed on the surface by the name convention (the `personified-abstractions` entry is cited as the governing *principle* but **not** extended into the Themis catalogue).

8. **THEO-904 — Moirai doublet vs Block-B 217.** RESOLVED (option 1). Klotho/Lachesis/Atropos transliterated exactly as at 218; collective *Μοίρας* = 'the Fates' (standing alone) vs 'the Destinies' at 217 (where paired with *Κῆρας*); the Nyx-vs-Zeus/Themis genealogical doublet flagged in commentary. `personified-abstractions` entry **not** silently extended.

9. **THEO-934 — Phobos / Deimos.** RESOLVED (option 1, = Evelyn-White) — 'Panic and Fear' translated. The strong option-2 case (transliterate, for consistency with the same-clause sister Harmonia 937 and the transliterated cult-retinue Zelos/Nike/Kratos/Bia 384–385) is documented at 934 and **flagged for the Reviewer**.

10. **THEO-913 — Aidoneus.** RESOLVED (option 1). Keep 'Aidoneus' (a fuller alternative name of Hades, not a mere orthographic variant); **NOT** folded into `dialectal-theonym-normalization` (which does normalize the plain epic *Ἀίδης/Ἀίδεω* at 768/774/850). Non-normalization flagged here.

11. **THEO-967 — mortal-union register.** ADJUDICATED (option 1 + dedicated entry). Created `union-formulae-mortal-goddess-catalogue-theogony` (appliesTo 17 union-verb lines). Formulae rendered literally/consistently with Evelyn-White and A–C; *δμηθεῖσα/ὑποδμηθεῖσα* 'subdued/tamed' force preserved (not euphemized).

12. **THEO-1021 — closing seam.** RESOLVED (option 1). 1019–1022 rendered literally as a transitional invocation; the redactional seam toward the (lost) *Catalogue of Women* (*Ehoiai*) and the authenticity discussion recorded in commentary (notes at 1021 and the parallel 965). No surface marking; commentary-only (no lexical entry needed).

13. **THEO-997 — variant-spelling documentation.** CONFIRMED (option 1). (a) epic Hades *Ἀίδεω/Ἀίδης* → 'Hades' (768/774/850) folded into `dialectal-theonym-normalization` appliesTo; (b) *Ἰαωλκόν* → 'Iolkos' (997) and (c) *Οὐλυμπ-* → 'Olympos' (855/953), with Krete (971), folded into `place-name-greek-forms-block-c-theogony` appliesTo; (d) edition orthographic quirks (761 grave *εἲς*, 902 *Εὐνουμίην*, 907 unaccented *Εὐρυνομη*, 975 *Ἀφροδιτης*, 1003 *κοῦραι,·*) governed by the new `source-orthographic-quirks-verbatim-theogony` entry — kept verbatim in the text field, standard forms in translit/English (Chrysaor precedent).

---

## Overlay changes (`_translation-glossary.json` → v1.3.0)

### New entries (4, all `claim_type=direct`)

- `variant-passage-929a-929t-metis-doublet-theogony` — governs all 20 of 929a–929t.
- `metis-metieta-cunning-counsel-network-theogony` — governs 886, 887, 904, 914, 929g, 929n.
- `union-formulae-mortal-goddess-catalogue-theogony` — governs 920, 923, 927, 929f, 941, 944, 962, 967, 970, 980, 1000, 1005, 1006, 1009, 1012, 1018, 1019.
- `source-orthographic-quirks-verbatim-theogony` — governs 761, 902, 907, 975, 1003.

### appliesTo extensions (15 existing entries; no semantic field modified — semver-minor)

| Entry | Block-D refIds added |
|---|---|
| `horkos-styx-great-oath-theogony` | 784, 805 |
| `time-geras-moira-honor-vocabulary-theogony` | 882, 885, 892, 904 |
| `gaia-counsel-prophecy-vocabulary-theogony` | 884, 891 |
| `ophis-drakon-serpent-vocabulary-theogony` | 825 |
| `thunder-triad-bronte-keraunos-sterope-theogony` | 839, 845, 846, 854 |
| `tartaros-underworld-vocabulary-theogony` | 736, 807, 841, 851, 868 |
| `chaos-primordial-chasm-void-theogony` | 740, 814 |
| `titanes-folk-etymology-theogony` | 814, 820, 851, 882 |
| `dialectal-theonym-normalization-theogony` | 768, 774, 850 |
| `athetized-lines-convention-theogony` | 774, 929s, 1014 |
| `aigiochos-aegis-bearer-zeus-epithet-theogony` | 920, 929c, 929s, 966, 1022 |
| `periphrastic-title-unnamed-god-theogony` | 818, 930, 945 |
| `place-name-greek-forms-block-c-theogony` | 855, 953, 971, 997 |
| `ouranos-gaia-cosmogony-personification-boundary-theogony` | 736, 746, 753, 761, 779, 807, 820, 821, 840, 847, 858, 884, 891 |
| `theogony-name-and-title-conventions` | 776, 886, 902, 934, 966, 1017 *(representative — this meta-entry's appliesTo is a sample, per the A–C precedent; it is referenced on 94 further Block-D lines)* |

Audit: every Block-D `glossaryRefs` entry except the representative name-convention resolves to a governing entry whose `appliesTo` lists that refId (0 orphans for all other entries).

---

## CENTRAL — apply by orchestrator

**No central-glossary change is required or recommended for Block D.** Confirmed by targeted query: **zero THEO refIds occur anywhere in `data-content/i18n/translation-glossary.json`** — the signed-off Block-A/B/C non-fusion precedent is intact and is maintained here. The four cross-corpus pulls the block raises are all recorded as clearly-labeled comparative/reception apparatus **overlay-side only**:

- **Typhoeus vs the chaoskampf cluster.** The Typhoeus-combat (820–880) is the poem's strongest instance of the Near-Eastern divine-combat pattern (central `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible`; the `leviathan` / `lotanu-leviathan-seven-headed-serpent` / `taninim` / `yamm-yammu` cluster), plus the Hurro-Hittite Illuyanka/Ullikummi. **Recommendation: do NOT extend** the central entry to any THEO refId (exactly as the Titanomachy was handled in Block C). *Optional* future spec if the founder ever chooses corpus-wide fusion: append the Typhoeus refId THEO-820 to the central `chaoskampf` appliesTo with a Greek-branch sub-note — **not recommended**; convergence stays in the 820 commentary.
- **Styx oath procedure vs oath/covenant entries.** The Greek *horkos*-by-Styx sanction (775–806) converges thematically with the Hebrew/Mesopotamian oath-and-covenant field (`brit-covenant`, `karat-brit-cut-covenant`, `bi-nishbati-divine-self-oath`, `zi-an-na-…-oath-by-life-of-heaven-and-earth`). **Recommendation: no central change**; governed overlay-side by `horkos-styx-great-oath-theogony`; convergence not asserted.
- **Metis-swallowing vs wisdom/counsel entries.** Zeus absorbing the counsel-goddess Metis converges with the Mesopotamian wisdom-god material (`enki-deliberates-in-his-own-heart-wisdom-god…`, `nemequ-napishtu-dariti-wisdom…`). **Recommendation: no central change**; governed overlay-side by `metis-metieta-cunning-counsel-network-theogony`.
- **Tartaros cosmography.** No central Tartaros entry exists; the 2 Peter 2:4 *ταρταρόω* reception is already recorded in the overlay `tartaros-underworld-vocabulary-theogony`. **No central change.**

---

## Unresolved editorial questions

**None.** All 13 Translator questions were resolved into glossary state (entries + appliesTo extensions) or into commentary + Reviewer flags.

---

## Notes for the Reviewer

1. **929a–929t passage-level presentation (headline call).** The 20-line Chrysippus-apud-Galen doublet is retained and translated **unmarked** in the reading surface, in source order after 929, with status in commentary (929a) and the internal athetesis of 929s noted. This extends the athetized-lines philosophy from single `<del>` lines to a whole `<add>` block. The alternative (mark the block as bracketed/secondary in the surface, or omit it) is a live option; please confirm the retain-unmarked decision or direct a stronger apparatus marking.

2. **Phobos / Deimos (934) — translate vs transliterate.** Standing choice: 'Panic and Fear' (Evelyn-White, = draft). The option-2 case is strong (same-clause sister Harmonia is transliterated at 937; the exactly-parallel cult-retinue Zelos/Nike/Kratos/Bia was transliterated at 384–385 under the personified-abstractions convention). If the Reviewer prefers project-internal consistency over the reference, this becomes a surface change ('Phobos and Deimos') carried by a glossary tweak. Flagged, not decided.

3. **Aidoneus (913) not normalized.** Kept as the fuller alternative name, deliberately NOT folded into `dialectal-theonym-normalization` (which normalizes only the plain epic *Ἀίδης/Ἀίδεω* at 768/774/850). Confirm the keep-Aidoneus / normalize-the-plain-forms split.

4. **793–794 clause distribution (informational, no change requested).** The couplet's English redistributes the enjambed relative clause across the two lines (line 793's English carries 794's 'of the immortals who hold Olympos', line 794's English carries 793's 'pours a libation … and swears falsely'); the total couplet sense matches Evelyn-White exactly. Left as the Translator rendered it; noted here only so a line-by-line reader is not surprised.

5. **Arc-closures to verify.** Four motifs tracked since A–C reach their payoff and are back-referenced in the commentary: the Styx oath (784 ← 400), the honour-lexicon (882/885 ← 392–449), Gaia's counsel (884/891 ← 463→475→494→626), and the *mētis*↔*ankylomētēs* network (886 ← 18/137/168/473/495). The Moirai genealogical doublet (904 ← 211/217) is flagged, not harmonized.

6. **Source-quirk fidelity.** The five edition quirks (761, 902, 907, 975, 1003) are preserved verbatim in the `text` field with standard forms in translit/English; the reading surface is clean. The three normalizations (Hades 768/774/850, Olympos 855/953, Iolkos 997) match the ratified conventions. Please spot-check the `text` fields against the source if desired — they were confirmed identical to `source-grc-1.json`.


---

# Reviewer report (inlined)

**Reviewer:** claude-opus-4-8[1m] acting as woh-reviewer
**Reviewed at:** 2026-08-04T13:34:32Z
**Lens-leakage flags:** 0

## Verse verdicts (38)

**THEO-736** — `approve`
: Re-parsed ἔνθα δὲ γῆς δνοφερῆς καὶ Ταρτάρου ἠερόεντος: 'misty Tartaros' and the πηγαί/πείρατα 'sources and limits' cosmography are the plain sense; γῆς/οὐρανοῦ correctly held as common nouns. Transliterated Tartaros with the tartaros-vocabulary entry; ratified.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 736–745; LSJ s.v. Τάρταρος, ἠερόεις

**THEO-740** — `approve`
: χάσμα μέγʼ 'a great chasm' is rendered plainly; the note's χάσμα~Χάος (√χα-) cognation is philological and correctly stated as cognation, not identity of referents. No lens; approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 740; LSJ s.v. χάσμα, χαίνω

**THEO-761** — `approve`
: Independently confirmed the source prints the grave proclitic εἲς (οὐρανὸν εἲς ἀνιὼν); the quirk is preserved verbatim in the text field and standard εἰς construed in English. The note's citation form ἀνιών (acute) is normal lemma citation, not an error.
: *Citations:* Perseus tlg0020.tlg001.perseus-grc2 (edition orthography); cf. Χρυσαωρ 281 precedent

**THEO-768** — `approve`
: Ἀίδεω is the epic (unaspirated) genitive of Ἅιδης, correctly normalized to the standard PANHELLENIC GREEK 'Hades' (not Latin Pluto/Dis) exactly as at 455; source spelling kept verbatim. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 768; LSJ s.v. Ἅιδης

**THEO-774** — `approve`
: Independently confirmed 774 repeats 768 verbatim and is athetized (<del>) in the source; retained-and-translated-unmarked per the ratified athetized-lines convention, athetesis recorded in commentary. Approve.
: *Citations:* West 1966 (app. crit.); Perseus <del> markup; LSJ s.v. Ἅιδης

**THEO-784** — `approve`
: θεῶν μέγαν ὅρκον 'the great oath of the gods' is verbatim = 400; ὅρκος is the oath-OBJECT (the Styx-water sanction) sworn by, correctly kept distinct from the personified Horkos (231) and lower-cased. Scope-extension of horkos-styx to 784 is warranted; no covenant vocabulary leaks into the surface. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 775–806, 784; LSJ s.v. ὅρκος II

**THEO-793** — `approve`
: The 793–794 couplet is a single enjambed relative clause; the English redistributes it (793-EN carries 794-Gk 'immortals who hold snowy Olympos', 794-EN carries 793-Gk 'pours a libation and swears falsely'). The composite sense matches Evelyn-White exactly and produces grammatical English; legitimate hexameter-enjambment handling. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 793–804

**THEO-805** — `approve`
: τοῖον ἄρʼ ὅρκον ἔθεντο... Στυγὸς ἄφθιτον ὕδωρ / ὠγύγιον 'such an oath the gods made, the imperishable primeval water of Styx' closes the oath-frame with ὅρκος again the oath-object; second payoff site of horkos-styx. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 805–806; LSJ s.v. ὅρκος, ἄφθιτος, ὠγύγιος

**THEO-814** — `approve`
: Τιτῆνες ναίουσι, πέρην Χάεος ζοφεροῖο 'the Titans dwell, beyond gloomy Chaos': Χάεος is the primordial gap of 116 functioning as underworld topography, correctly rendered 'Chaos' (not 'disorder'); chaos + titanes entries appropriately extended. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 814; LSJ s.v. χάος

**THEO-818** — `approve`
: βαρύκτυπος Ἐννοσίγαιος 'the deep-crashing Earth-Shaker' is Poseidon, correctly rendered by the periphrastic title without supplying the withheld name, as at 441/456. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 817–819; LSJ s.v. Ἐννοσίγαιος

**THEO-820** — `approve`
: HIGH-SCRUTINY (Typhoeus): re-parsed the whole set-piece against the Greek. The surface is a plain rendering (youngest child of Gaia in union with Tartaros; blasted by the thunderbolt; hurled into Tartaros) with NO chaoskampf coloring in the text; the Near-Eastern combat-myth convergence is confined to a clearly-labeled comparative note. No lens leakage; approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 820–880; Clay 2003, Hesiod's Cosmos

**THEO-825** — `approve`
: ἣν ἑκατὸν κεφαλαὶ ὄφιος, δεινοῖο δράκοντος 'a hundred heads of a serpent, a dread dragon': ὄφις/δράκων used of the one creature with no fixed technical opposition, per LSJ and the reference; ophis-drakon entry correctly extended to the climactic serpent. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 825; LSJ s.v. ὄφις, δράκων

**THEO-839** — `approve`
: ἐβρόντησε and the βροντή/στεροπή/κεραυνός recurrences (845–846, 854) render Zeus's storm-triad consistently as thunder/lightning/(blazing) thunderbolt, without a rigid technical distinction the poem does not mark; thunder-triad scope-extension warranted. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 839–846, 854; LSJ s.vv. βροντή, στεροπή, κεραυνός

**THEO-850** — `approve`
: τρέε δʼ Ἀίδης 'Hades trembled': the epic Ἀίδης normalized to the standard Greek form as at 768/774, source spelling kept verbatim. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 850; LSJ s.v. Ἅιδης

**THEO-855** — `approve`
: ἀπʼ Οὐλύμποιο: the epic diectatic Οὔλυμπ- normalized to the standard 'Olympos' (Greek form, not Latin Olympus) as at 397/953, source spelling kept verbatim. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 855; place-name Greek-forms convention

**THEO-866** — `approve`
: OBSERVATION (name-form): the surface uses the entrenched anglicized 'Hephaestus' (first occurrence here) rather than the Greek 'Hephaistos', as it does for Apollo (14) and Achilles (1007). This is inconsistent with the convention's Hellenizing thrust (Ouranos-not-Uranus) but falls in the same 'established English theonym' class as the signed-off Apollo/Athena (Block A), and follows the reference edition; defensible, no lens. Approve; recommend the name-convention entry make the entrenched-individual-theonym retention explicit.
: *Citations:* Evelyn-White 1914; name-and-title convention (THEO-1); cf. signed-off Apollo/Athena at 13–14

**THEO-868** — `approve`
: ῥῖψε δέ μιν... ἐς Τάρταρον εὐρύν 'he hurled him into wide Tartaros': plain rendering; the ταρταρόω/2 Peter reception is held to the apparatus and does NOT leak into the surface (no 'cast down to Tartaros' cosmology imported). Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 868; LSJ s.v. Τάρταρος; cf. 2 Pet 2:4 ταρταρόω

**THEO-882** — `approve`
: Τιτήνεσσι... τιμάων κρίναντο βίηφι and 885 ἑὰς διεδάσσατο τιμάς: the honour-lexicon reaches its accession payoff (Zeus distributes the timai); rendered 'honours' consistently, scope-extension of time-geras-moira to 882/885/892/904 warranted. A sovereign distributing offices is WoH-salient but the surface stays lexical; no lens. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 881–885; LSJ s.vv. τιμή, γέρας

**THEO-884** — `approve`
: Γαίης φραδμοσύνῃσιν 'by the counsels of Gaia' installs Zeus as king; the gaia-counsel motif culmination (463→475→494→626→884) is correctly tracked, surface literal, no cosmological reading pressed. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 884; LSJ s.v. φραδμοσύνη

**THEO-886** — `approve`
: HIGH-SCRUTINY (Metis): πρώτην ἄλοχον θέτο Μῆτιν 'made Metis his first wife' — name transliterated (not glossed 'Cunning'), the mētis wordplay-network held in commentary. The swallowing (891–900) is rendered plainly with NO wisdom-tradition import (no 'Wisdom/Sophia' capitalization); non-fusion with the central wisdom entries intact. No lens; approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 886–900; LSJ s.v. μῆτις, μητίετα; Detienne–Vernant, Les ruses de l'intelligence (1974)

**THEO-887** — `revise`
: The printed Perseus source line reads πλεῖστα τε ἰδυῖαν ἰδὲ θνητῶν ἀνθρώπων — hypometric, with θεῶν omitted — yet the surface supplies 'of gods and of mortal men', silently following the standard text and the doublet 929p (πλεῖστα θεῶν τε ἰδυῖα...). The rendering is CORRECT and should stand, but this word-level edition defect is undocumented while the overlay documents far smaller quirks (a stray comma at 1003). REVISE: add a per-line note (or extend source-orthographic-quirks-verbatim) recording that the Perseus line omits θεῶν and the surface follows the standard reading confirmed by 929p.
: *Citations:* West 1966 (text: πλεῖστα θεῶν εἰδυῖαν ἰδὲ θνητῶν ἀνθρώπων); Perseus tlg0020.tlg001.perseus-grc2 (defective line); cf. the parallel 929p

**THEO-891** — `approve`
: Γαίης φραδμοσύνῃσι καὶ Οὐρανοῦ ἀστερόεντος 'by the counsels of Gaia and of starry Ouranos': second gaia-counsel payoff, correctly rendered; Ouranos here the personified consort-deity, within the boundary entry's scope. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 891; LSJ s.v. φραδμοσύνη

**THEO-900** — `approve`
: The swallowing (ἐσκάτθετο νηδύν) 'so that the goddess might advise him of good and evil' and Athena's birth from Zeus's head (924, αὐτὸς δʼ ἐκ κεφαλῆς) are rendered plainly; δόλῳ/αἱμυλίοισι λόγοισιν 'by craft/with wheedling words' preserved. No lens. Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 897–900, 924–926; Loraux, Les enfants d'Athéna

**THEO-902** — `approve`
: Confirmed source prints Εὐνουμίην; kept verbatim in text, standard 'Eunomia' in translit/English. The Horai/Eunomia/Dike/Eirene transliterated as cult-established Seasons-goddesses (parallel to the Charites 909), transparent senses in commentary. Approve.
: *Citations:* Perseus edition orthography (Εὐνουμίην); Evelyn-White 1914; name-and-title convention

**THEO-904** — `approve`
: Μοίρας 'the Fates' (vs 'the Destinies' at 217, correctly distinguished since 217 paired with Κῆρας), Κλωθώ/Λάχεσιν/Ἄτροπον transliterated as at 218, μητίετα 'the counsellor', πλείστην τιμὴν 'the greatest honour'. The Nyx-vs-Zeus/Themis genealogical doublet is honestly flagged, not harmonized (West 1966). Approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 904 (Moirai doublet); LSJ s.v. μητίετα, τιμή

**THEO-913** — `approve`
: EXPLICIT RULING (flagged call 3 — Aidoneus): I AFFIRM the non-normalization. Ἀιδωνεύς is a distinct expanded -εύς name-form of Hades attested as a fuller proper name in epic (Il. 5.190), NOT a mere orthographic variant of Ἅιδης; keeping 'Aidoneus' while normalizing only the plain epic Ἀίδης/Ἀίδεω (768/774/850) is the philologically correct split and matches the reference. Approve.
: *Citations:* Evelyn-White 1914 (Aïdoneus); West 1966 comm. ad 913; LSJ s.v. Ἀϊδωνεύς; Homer Iliad 5.190, 20.61

**THEO-929a** — `flag-for-human`
: EXPLICIT RULING (flagged call 1 — headline). The retain-and-translate-unmarked-in-source-order treatment of the 20-line Chrysippus-apud-Galen doublet is philologically DEFENSIBLE and RECOMMENDED: it consistently extends the ratified athetized-lines convention, the 929a–t non-integer numbering is itself a strong in-surface signal, and the 929a note fully documents provenance/bracketing and the internal 929s athetesis. I flag-for-human ONLY the precedent, because this is the corpus's FIRST <add>-supplement block (sets policy for all future <add> supplements) and involves a 20-line audience-scale question versus single-line athetesis. Recommendation: keep retain-unmarked; the human should (a) ratify the precedent and (b) ensure the reader UI renders the 929a–t numbering + doublet-status so the block is visibly distinguishable. The renderings of 929a–t themselves are accurate (see 929g/929n/929s).
: *Citations:* West 1966 (app. crit. ad 929a–t); Galen, De placitis Hippocratis et Platonis 3.8 (Chrysippus fr.); Perseus <add>/<del> markup; Most 2006 (Loeb) app.

**THEO-929g** — `approve`
: ἐξαπαφὼν Μῆτιν καίπερ πολυδήνεʼ ἐοῦσαν 'deceiving Metis, though she was full of cunning': accurate doublet rendering; πολυδήνεα 'of many wiles' preserved, mētis network kept in commentary. Approve.
: *Citations:* Evelyn-White 1914; LSJ s.v. πολυδήνης, ἐξαπαφίσκω

**THEO-929n** — `approve`
: Μῆτις δʼ αὖτε Ζηνὸς ὑπὸ σπλάγχνοις λελαθυῖα 'Metis, hidden away beneath the vitals of Zeus': accurate; the swallowed-mētis motif rendered plainly, no lens. Approve.
: *Citations:* Evelyn-White 1914; LSJ s.v. σπλάγχνον, λανθάνω

**THEO-929s** — `approve`
: Independently confirmed 929s is athetized (<del>) even within the <add> supplement; retained-and-translated-unmarked, the double status (supplement + athetesis) recorded. αἰγίδα... φοβέστρατον 'the aegis, Athena's army-routing armour' — aigis left untranslated as a cultic object. Approve.
: *Citations:* West 1966 (app. crit. — 929s <del>); LSJ s.v. αἰγίς, φοβέστρατος

**THEO-934** — `revise`
: EXPLICIT RULING (flagged call 2 — Phobos/Deimos). I find the transliterate option MORE consistent with the project's own signed-off convention and recommend it. Φόβον καὶ Δεῖμον are cult-established named sons of Ares (Homeric daimones, Spartan cult) — exactly the 'cult-established name-like members' the personified-abstractions convention TRANSLITERATES (as it did Zelos/Nike/Kratos/Bia at 384–385) — and their sister Ἁρμονίη is transliterated three words later in the SAME clause (937). Translating 'Panic and Fear' while transliterating Harmonia is internally inconsistent. REVISE surface to 'Phobos and Deimos' (via a glossary tweak); the reference's 'Panic and Fear' remains defensible, so the human may override, but the reviewer's recommendation is transliterate.
: *Citations:* West 1966 comm. ad 934; LSJ s.vv. Φόβος, Δεῖμος; Homer Iliad 4.440, 15.119 (Deimos & Phobos, sons/attendants of Ares); project personified-abstractions-nyx-eris-brood convention

**THEO-967** — `approve`
: HIGH-SCRUTINY (union formulae): εὐνηθεῖσαι 'having lain with', (ἐν) φιλότητι μιγεῖσα 'mingling in love', δμηθεῖσα/ὑποδμηθεῖσα 'subdued/tamed by' (< δάμνημι), παρελέξατο 'lay beside' are rendered literally and consistently; the δμη- 'subdued' force is preserved (neither euphemized nor coarsened) AND carries no WoH divine-union lens into the surface. Register-precise; approve.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 963–1018; LSJ s.vv. εὐνάω, δάμνημι, φιλότης, παραλέγομαι

**THEO-1000** — `approve`
: δμηθεῖσʼ ὑπʼ Ἰήσονι, ποιμένι λαῶν 'subdued by Jason, shepherd of the people': the δμη- 'subdued' force preserved, not softened. Approve.
: *Citations:* Evelyn-White 1914; LSJ s.v. δάμνημι

**THEO-1006** — `approve`
: Πηλέι δὲ δμηθεῖσα θεὰ Θέτις 'the goddess Thetis, subdued by Peleus': same disciplined preservation of the 'subdued' force; approve.
: *Citations:* Evelyn-White 1914; LSJ s.v. δάμνημι

**THEO-1003** — `approve`
: Confirmed source prints a stray comma-plus-raised-dot after κοῦραι; kept verbatim in the text field and construed normally in English. Approve.
: *Citations:* Perseus edition orthography (κοῦραι,·); source-orthographic-quirks-verbatim entry

**THEO-1014** — `approve`
: Confirmed 1014 (Τηλέγονον...) is athetized (<del>) as a post-Hesiodic addition toward the Telegony; retained-and-translated-unmarked per convention, athetesis recorded. Approve.
: *Citations:* West 1966 (app. crit.); Perseus <del> markup; LSJ; the Telegony reception

**THEO-1021** — `approve`
: νῦν δὲ γυναικῶν φῦλον ἀείσατε 'but now sing the tribe of women' is rendered literally as the transitional invocation mirroring 965–966; the redactional-seam/authenticity discussion is recorded in commentary, not marked in the surface. Approve.
: *Citations:* Evelyn-White 1914; West 1966; Most 2006 (redactional seam toward the Catalogue of Women/Ehoiai)

**THEO-736–1022 + 929a–929t (block coverage)** — `approve`
: COVERAGE: every Block-D line object was re-parsed against the pointed Greek and its text field confirmed byte-identical (NFC) to the source. All lines not individually enumerated above (the house-of-Nyx/Sleep-Death description 744–766, the Styx cosmography 776–806, the Titan-prison seam 807–819, the Typhoeus-winds aetiology 869–880, the marriage- and mortal-goddess catalogues, and the 929b–t doublet interior) are plain, accurate Evelyn-White-consistent renderings with no lens leakage; approved.
: *Citations:* Evelyn-White 1914 (reference edition, whole block); West 1966 commentary; LSJ; independent NFC text-field verification against source-grc-1.json (0 mismatches across all 307 line objects)


## Glossary-entry verdicts (19)

**variant-passage-929a-929t-metis-doublet-theogony** — `approve`
: claim_type=direct is correct: this is an apparatus convention and its text-critical content is accurate and well-cited — the Chrysippus-apud-Galen provenance, West's bracketing, the doublet mapping (929a–d ↔ 927–929; 929e–t ↔ 886–900 + 924, birth by the Triton at 929m), and the internal 929s athetesis were all independently verified against the source. The PRESENTATION-precedent the entry encodes is flag-for-human (see THEO-929a), but the entry's factual apparatus is sound. Approve.
: *Citations:* West 1966 (app. crit. ad 929a–t); Galen, De placitis Hippocratis et Platonis 3.8 (Chrysippus fr.); Perseus <add>/<del> markup

**metis-metieta-cunning-counsel-network-theogony** — `approve`
: claim_type=direct is correct and the lexical evidence is real: Μῆτις = μῆτις 'cunning counsel', μητίετα 'the counsellor' (rendered as at 520), and the etymological tie to Kronos's ἀγκυλομήτης (ankylo- + mētis) are all settled LSJ/Chantraine/Detienne–Vernant material. The wordplay is correctly kept in commentary and OUT of the surface (no inline 'Metis — Cunning' gloss); non-fusion with the central wisdom entries preserved. Approve.
: *Citations:* LSJ s.vv. μῆτις, μητίετα, ἀγκυλομήτης; Chantraine DELG s.v. μῆτις; Detienne–Vernant, Les ruses de l'intelligence: la mètis des Grecs (1974); West 1966 comm. ad 886–900

**union-formulae-mortal-goddess-catalogue-theogony** — `approve`
: claim_type=direct is correct: preserving the δμη-/δαμ- 'subdued/tamed' force (< δάμνημι 'overpower, break, tame') against euphemism is a lexical fact of the Greek, not an editorial colouring. The 17-site consistency mapping matches the reference; the lens-discipline note keeps the WoH divine-human-union register out of surface and note. Approve.
: *Citations:* LSJ s.vv. δάμνημι, εὐνάω, φιλότης, παραλέγομαι; West 1966 comm. ad 963–1018; Evelyn-White 1914

**source-orthographic-quirks-verbatim-theogony** — `approve`
: claim_type=direct is correct: all five quirks (761 grave εἲς, 902 Εὐνουμίην, 907 unaccented Εὐρυνομη, 975 unaccented Ἀφροδιτης, 1003 κοῦραι,·) were independently confirmed present in the source and preserved verbatim in the text fields, standard forms in translit/English. NOTE: this entry does NOT cover the word-level defect at 887 (θεῶν omitted); see the THEO-887 revise — extending this entry to 887 is one acceptable fix.
: *Citations:* Perseus tlg0020.tlg001.perseus-grc2 (edition orthography); cf. Χρυσαωρ 281 precedent (pegasos-chrysaor entry)

**horkos-styx-great-oath-theogony** — `approve`
: Scope-extension to 784/805 is warranted and lexically exact: the 784 phrase θεῶν μέγαν ὅρκον is verbatim = 400 and ὅρκος is the oath-object/sanction (LSJ II 'that by which one swears'), correctly distinguished from the deity Horkos (231). No covenant-cosmology pressed; approve.
: *Citations:* West 1966 comm. ad 400, 775–806; LSJ s.v. ὅρκος II; Evelyn-White 1914

**time-geras-moira-honor-vocabulary-theogony** — `approve`
: Scope-extension to the accession payoff 882/885/892/904 is warranted: the τιμή/τιμαί apportionment lexicon of the Hekate hymn reaches its structural payoff as Zeus divides the timai. Consistent 'honours' rendering; surface stays lexical. Approve.
: *Citations:* West 1966 comm. ad 881–885, 892, 904; LSJ s.vv. τιμή, γέρας, μοῖρα; Evelyn-White 1914

**gaia-counsel-prophecy-vocabulary-theogony** — `approve`
: Scope-extension to the culmination 884/891 is warranted: Γαίης φραδμοσύνῃσιν installs Zeus and prompts the Metis-swallowing, closing the motif tracked from 463→475→494→626. Surface literal, no cosmological reading. Approve.
: *Citations:* West 1966 comm. ad 463–465, 494, 626, 884; LSJ s.v. φραδμοσύνη; Evelyn-White 1914

**ophis-drakon-serpent-vocabulary-theogony** — `approve`
: Extension to 825 (Typhoeus's hundred serpent-heads) is warranted: ὄφις/δράκων are used of the one creature with no fixed technical opposition, exactly the Block-B finding. Approve.
: *Citations:* LSJ s.vv. ὄφις, δράκων; West 1966 comm. ad 825

**thunder-triad-bronte-keraunos-sterope-theogony** — `approve`
: Extension to 839/845/846/854 is warranted: Zeus's storm-triad against Typhoeus rendered consistently with the Kyklopes'-gift and Titanomachy sites, no rigid technical distinction imposed. Approve.
: *Citations:* LSJ s.vv. βροντή, στεροπή, κεραυνός; West 1966 comm. ad 504–505, 690–708, 839–854

**tartaros-underworld-vocabulary-theogony** — `approve`
: Extension to 736/807/841/851/868 is warranted (the Block-D prison/cosmography sites); 'Tartaros' transliterated, description literal, the ταρταρόω reception kept as apparatus. No central Tartaros entry created; non-fusion intact. Approve.
: *Citations:* LSJ s.v. Τάρταρος; West 1966 comm. ad 720–735; cf. 2 Pet 2:4 ταρταρόω (reception, apparatus only)

**chaos-primordial-chasm-void-theogony** — `approve`
: Extension to 740 (χάσμα, √χα- cognate) and 814 (Χάεος as underworld region) is warranted; the primordial-gap sense is correctly maintained against the post-classical 'disorder'. Approve.
: *Citations:* LSJ s.v. χάος, χαίνω; West 1966 comm. ad 116, 740, 814; Kirk–Raven–Schofield 1983

**titanes-folk-etymology-theogony** — `approve`
: Extension to 814/820/851/882 is warranted: all are Τιτῆνες/Τιτήνεσσι occurrences, transliterated 'Titans' consistently. Approve.
: *Citations:* LSJ s.v. Τιτάν; West 1966 comm. ad 207–210; Evelyn-White 1914

**dialectal-theonym-normalization-theogony** — `approve`
: Extension to the epic Hades forms 768/774/850 is warranted and correctly SCOPED: the entry normalizes only the plain epic Ἀίδης/Ἀίδεω to the standard Greek 'Hades', and the distinct fuller name Ἀιδωνεύς (913) is rightly left OUT (kept as 'Aidoneus'; affirmed at THEO-913). Approve.
: *Citations:* LSJ s.v. Ἅιδης; West 1966 comm. ad 768, 850; Evelyn-White 1914

**athetized-lines-convention-theogony** — `approve`
: Extension to 774/1014/929s is warranted: all three independently confirmed as edition <del> lines, retained-and-translated-unmarked with athetesis in commentary per the ratified convention. Approve.
: *Citations:* West 1966 (app. crit.); Perseus <del> markup; independent verification: 774/1014/929s all carry <del> in the source

**aigiochos-aegis-bearer-zeus-epithet-theogony** — `approve`
: Extension to 920/966/1022 (Διὸς αἰγιόχοιο) and 929c (aigiochos epithet) and 929s (the aigis object) is warranted; 'aegis-holding' retained, aigis left untranslated as a cultic object. Approve.
: *Citations:* LSJ s.v. αἰγίοχος, αἰγίς; West 1966 comm. ad 11; Evelyn-White 1914

**periphrastic-title-unnamed-god-theogony** — `approve`
: Extension to 818/930 (Ennosigaios = Poseidon) and 945 (Amphigyeeis = Hephaestus, the Lame One) is warranted; the withheld names are rendered by literal periphrasis, not supplied in surface. Approve.
: *Citations:* LSJ s.vv. Ἐννοσίγαιος, Ἀμφιγυήεις; West 1966 comm. ad 441, 456; Evelyn-White 1914

**place-name-greek-forms-block-c-theogony** — `approve`
: Extension to Olympos 855/953, Krete 971, Iolkos 997 is warranted and consistent with the signed-off Greek-forms convention; source spellings (Οὐλυμπ-, Ἰαωλκ-) kept verbatim, standard Greek forms in surface. Approve.
: *Citations:* LSJ s.vv. Κρήτη, Ὄλυμπος, Ἰωλκός; West 1966; signed-off river-/island-exonym precedent (Kypros-not-Cyprus)

**ouranos-gaia-cosmogony-personification-boundary-theogony** — `approve`
: Extension to the 13 Block-D sites is warranted: the common-noun γῆ/οὐρανός sites (736/746/753/761/779/807/840/847/858) and the personified-deity sites (820/821 Gaia, 884/891 Gaia+Ouranos) are correctly assigned by the boundary the entry governs. Approve.
: *Citations:* LSJ s.vv. γαῖα, οὐρανός; West 1966 comm. ad 108, 116–128; Evelyn-White 1914

**theogony-name-and-title-conventions** — `approve`
: The six Block-D representative anchors (776/886/902/934/966/1017) follow the established A–C practice of sampling this meta-entry's appliesTo rather than listing all ~90 name-convention sites; verified that every OTHER (non-meta) entry has complete bidirectional Block-D coverage (0 orphans). Approve. Minor: the entry could state explicitly that entrenched individual theonyms (Apollo/Athena/Achilles/Hephaestus) are retained anglicized alongside the Hellenized majority (see THEO-866).
: *Citations:* Evelyn-White 1914; Most 2006 (Loeb); name convention (THEO-1); A–C sign-off precedent for representative appliesTo sampling

