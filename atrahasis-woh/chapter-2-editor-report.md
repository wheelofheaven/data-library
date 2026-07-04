# Chapter 2 Editor Report — Atra-ḫasīs, Tablet II

## Overview

Tablet II carries the **population-control cycle**: the land grows wide and
humankind multiplies until its *rigmu/ḫubūru* (noise/clamor) robs Enlil of
sleep, whereupon he sends successive afflictions to thin humankind — plague
(via Namtar), drought (Adad ordered to withhold the rain), then famine — each
over a recurring ~1200-year interval, each circumvented by Enki's
offering-concentration stratagem, until Enlil escalates to the **Flood** and
binds the gods by oath. **72 lines / 8 segments**, schema
`composition/column/line`, refIds `ATRA-WOH-II:{col}-{line}` (Lambert–Millard
column numbering). Tablet II is the **most damaged** of the three: cols v
(famine-catalogue) and vi–viii (assembly, accusation of Ea, flood-decree,
oath) are **outline-only** with `preceding_lacuna` gaps. A MOAT TEXT — no
usable PD English exists; the program renders its own.

The Translator submitted **10 editorial_questions[]**; this pass resolves
every one and clears the array.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0` (semver-minor;
  additions only)
- `translation.glossaryVersion`: `2.69.0` → **unchanged** (the ~4 MB central
  file was neither loaded nor modified)

`verificationStatus` — *best-effort-reconstruction-pending-verification;
Tablet II is the MOST DAMAGED; cols v, vi–viii outline-only* — is
**preserved unchanged** in `chapter-2.json` and `source-akk-2.json`. Editorial
work operates on the **sense-of-line** (well-attested across Lambert–Millard
1969, George & Al-Rawi 1996, Foster 2005), independent of sign-level collation.
**No `i18n.en` line was modified.** All edits are to `notes.official`,
`glossaryRefs[]`, `translation` metadata, and `editorial_questions[]`.

**18 lines received commentary**; plain narrative and formulaic
speech-introduction lines were left empty per the "empty where it does not
diverge" norm.

---

## Resolution of the 10 editorial questions

| # | refId | Question | Resolution |
|---|---|---|---|
| 1 | II:i-3 | *rigmu / ḫubūru* clamor (flood-cause) | **Resolved** → overlay `rigmu-huburu-clamor-of-overpopulation-flood-cause-atrahasis` (`inferred`). Plain 'noise'/'clamor' retained; overpopulation reading in apparatus only. **CENTRAL candidate** (cross-corpus to Hebrew *ḥāmās*/*ṣeʿāqâ*; Gilgamesh XI) — flagged for the Python step, central file untouched. |
| 2 | II:i-9 | *Namtar* | **Resolved** → overlay `namtar-plague-fate-god-atrahasis` (`direct`). Retained untranslated as a divine name. |
| 3 | II:iii-7 | Adad's inverted drought-role | **Resolved** → overlay `adad-inverted-drought-role-scope-note-atrahasis` (`direct`). Rain-withheld-as-drought rendered plainly; central Adad entry applied by id for the name; Akkadian `appliesTo` + scope note flagged for the central step. |
| 4 | II:iii-1 | 1200 / 600-years interval | **Resolved as a textual note** (commentary at iii-1). Numeral bracketed `[12-me]`, verification-pending. **No glossary entry** (reading crux, not lexical) — parallels the I:37 precedent. |
| 5 | II:ii-11 | offering-concentration stratagem + *ṭēmu*='plan' | **Resolved** → overlay `offering-concentration-shaming-the-god-stratagem-atrahasis` (`direct`). *bâšu*+*kadrû*+*nasāḫu qāta* rendered plainly; **Tablet-II *ṭēmu* ('plan') held DISTINCT from the Tablet-I anthropogonic *ṭēmu*-pun — the two are NOT conflated** (pun-entry not applied here). |
| 6 | II:iv-4 | affliction vocabulary | **Resolved** → overlay `population-control-afflictions-vocabulary-atrahasis` (`direct`). *šuruppû*/*diʾu*/*bubūtu*/*idrānu* rendered plainly; possible central affliction-cluster flagged (not asserted). |
| 7 | II:i-7 | divine-repose / sleep disturbed | **Resolved in commentary** (i-6, vi-4), folded into the *rigmu* entry. **No separate entry** (plain rendering, no lexical decision). |
| 8 | II:ii-1 | *Atra-ḫasīs* name | **Resolved** → overlay `atrahasis-name-exceedingly-wise-atrahasis` (`direct`). Retained untranslated; etymology glossed in commentary; central survivor-name-cluster Akkadian `appliesTo` flagged. |
| 9 | II:vii-5 | flood causation (noise vs corruption) | **Resolved** → central flood-vocabulary/causation/decree/oath entries applied by id; commentary at vii-5 carries the **Genesis 6:5–7 noise-vs-corruption contrast**; Akkadian `appliesTo` activation flagged. Rationale housed in the *rigmu* entry. |
| 10 | II:i-1 | refId scheme (column-line) | **Resolved / escalated to reviewer.** Column-line refIds kept as-is; **recommendation to normalize the dash to Tablet III's dot form** — see §refId. Non-blocking. |

All 10 `editorial_questions[]` cleared to `[]`.

---

## ⚠ Lens-routing decisions

The **overpopulation-as-problem**, the gods sending **deliberate
population-control** afflictions, and the **noise (not moral corruption) as
the flood-cause** are all **in the Akkadian** and are rendered plainly — no
softening, no editorializing. What is held out of every `i18n.en` line and
every `notes.official`:

1. **Nothing lens-y touches any `i18n.en` line.** No line was modified; the
   surface English reads in the Lambert–Millard / Foster register.
2. **Nothing lens-y touches any `notes.official`.** Commentary is confined to
   philology (named forms, standard renderings, WoH choices, scholarly basis:
   Lambert–Millard 1969; Foster 2005; Kilmer 1972; Moran 1971; CAD/AHw) and
   cited/hedged cross-corpus comparison (Genesis *ḥāmās*/*ṣeʿāqâ*; Gilgamesh
   XI). No commentary asserts the Elohim frame.
3. **The overpopulation reading is mainstream Assyriology** (Kilmer 1972) and
   is allowed in the apparatus; the **interpretive Elohim-frame identification**
   (the gods as an advanced civilization managing a labor-population's numbers)
   is escalated below and routed to the Explainer, never the line.
4. **Two lens-temptations declined in-text:** *rigmu/ḫubūru* rendered plainly
   'noise/clamor' (not 'population pressure'); the Tablet-II *ṭēmu* rendered
   'plan/scheme' (not 'programmed directive').

---

## Speculative entries requiring sign-off

### `atrahasis-population-control-elohim-frame` (PROPOSED — NOT committed)

**Source:** the population-control cycle as a whole (Tablet II) plus the
etiological limits of Tablet III vii — overpopulation, engineered afflictions,
and deliberate standing fertility-caps.

**WoH reading under consideration:** identify the Atra-ḫasīs gods with the
Wheel of Heaven **Elohim** and read the noise-triggered afflictions and the
permanent fertility-limits as a compressed memory of a technologically-managed
population.

**Why speculative:** the *lexical/narrative* facts (overpopulation noise →
afflictions → flood → standing fertility-checks) are direct and are already
carried plainly. What crosses into `speculative` is the *identification* of
these gods as an advanced civilization and of the afflictions as engineered
demographic management — an interpretive synthesis beyond what the Akkadian
attests.

**Recommendation:** **Do NOT commit**; **route to the Explainer**
(`made-from-the-ground-to-bear-the-labor` and/or a flood/population Explainer).
Zero committed speculative entries block the advance.

**Human reviewer action:** confirm by name that this reading stays in the
Explainer and out of the translation/glossary.

---

## Glossary changes for review

### Central glossary — **no in-agent edits.** Deferred to the Python step:

- **CREATE (candidate):** `rigmu-huburu-...` → central *rigmu/ḫubūru*
  clamor-flood-cause entry, cross-corpus to Hebrew *ḥāmās*/*ṣeʿāqâ* and the
  Gilgamesh XI flood-cause. `inferred`.
- **Akkadian-side `appliesTo` activation** on existing central entries for the
  Tablet-II refIds: `adad-hadad-baal-storm-god-flood-instrument-cross-corpus`
  (+ drought scope note), `a-ma-ru-abubu-mabbul-...`,
  `flood-causation-divine-council-...` (+ the Genesis 6:5–7 noise-vs-corruption
  contrast), `divine-decree-to-destroy-humankind-...`,
  `zi-an-na-...-oath-...`, `ziusudra-atrahasis-utnapishtim-noach-...`, and the
  DINGIR / Anunna-Igigi / lacuna-bracket conventions (already referenced by id).
- **Flag (not asserted):** a possible central "divine population-control
  afflictions" cluster (*šuruppû/diʾu/bubūtu/idrānu*).

### Per-translation overlay (`_translation-glossary.json`) → v1.1.0

**Added (Tablet II, 6 entries):** `rigmu-huburu-...` (`inferred`),
`namtar-...` (`direct`), `adad-inverted-drought-role-...` (`direct`),
`offering-concentration-shaming-the-god-stratagem-...` (`direct`),
`population-control-afflictions-vocabulary-...` (`direct`),
`atrahasis-name-exceedingly-wise-...` (`direct`).

Distribution: **5 `direct`, 1 `inferred`, 0 committed `speculative`.**

---

## refId-scheme recommendation

Tablet II uses `ATRA-WOH-II:{col}-{line}` (dash); Tablet III uses
`ATRA-WOH-III:{col}.{line}` (dot); Tablet I uses continuous `:{line}`. The
divergence is faithful to Lambert–Millard's numbering but internally
inconsistent. **Recommendation: normalize Tablet II's dash to Tablet III's
dot** (`ATRA-WOH-II:{col}.{line}`) for consistency across the column-numbered
tablets, OR ratify both as-is. This is a **human/reviewer call**; it does not
block the advance. If normalized, the `refId` and `appliesTo` values in
`chapter-2.json` and the overlay must be updated in lockstep (a mechanical
find-replace, easily scripted).

---

## Unresolved editorial questions

**None.** All 10 resolved; `editorial_questions[]` is `[]`.

---

## Items for the human reviewer

1. **Confirm the speculative routing (required):** `atrahasis-population-control-elohim-frame`
   stays in the Explainer, out of the translation/glossary.
2. **Rule on the refId scheme:** normalize II's dash → dot, or ratify as-is.
3. **Approve the central action items** for the Python step (the *rigmu/ḫubūru*
   central candidate; the Akkadian-side `appliesTo` activations incl. the Adad
   drought scope note and the Genesis noise-vs-corruption contrast).
4. **Verification-pass:** schedule sign-level collation against Lambert–Millard
   1969 and eBL L.1.1 — Tablet II confidence is LOWER than Tablet I; cols v and
   vi–viii are outline-only. `verificationStatus` holds.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible
scholarly rendering; the overpopulation / population-control reading is
delivered plainly because it is in the Akkadian, and the Elohim-frame lens is
held entirely out of the translation and apparatus. Every overlay entry has
all required fields, correct claim_type, and CAD/AHw + named-scholarship
grounding. **Zero committed `claim_type=speculative` entries**; standard
Reviewer sign-off applies, plus the speculative-routing confirmation and the
refId ruling in the items above.
