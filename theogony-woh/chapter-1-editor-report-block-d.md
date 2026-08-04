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
