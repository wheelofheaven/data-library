# Atra-ḫasīs, Tablets II–III — sign-off package (completes the epic)

**Status:** `reviewer-approved` (RC), human-ratified 2026-07-04. With these two tablets, `atrahasis-woh` covers the **whole Old Babylonian Atra-ḫasīs** (Tablets I–III) — catalog `status: complete`.
**Text:** Tablet II (overpopulation "noise" → plague / drought / famine as divine population-control; Enlil's resolve on the Flood) + Tablet III (the Flood: reed-wall warning, the boat, the deluge, the gods' regret and hunger, the offering, and the new mortal order with permanent population-limits).
**Version:** 1.0.0-rc1 · **Glossary:** overlay **v1.1.0** (22 entries; +12 for II–III; 0 committed speculative).
**⚠ verificationStatus:** `best-effort-reconstruction-pending-verification` — sign-collation against Lambert–Millard 1969 / eBL L.1.1 pending; **Tablet II is the most damaged** (cols v–viii outline-only).

## Summary
| Metric | Tablet II | Tablet III |
|---|---|---|
| Lines | 72 / 8 seg | 113 / 8 seg |
| Reviewer | all approved | all approved |
| Editorial questions | 10 → resolved | 9 → resolved |
| Lens-leakage | **0** | **0** |

Book totals: **3 tablets, 296 lines**; overlay glossary 22 entries.

## Pipeline
- **Translators** (aec15fd4 / aa176599): scaffolded both tablets — best-effort Akkadian (verification-pending) + drafts + 19 editorial questions.
- **Editor** (aa88b1b9): resolved 19/19; overlay v1.0.0→v1.1.0 (+12 entries); 44 commentary notes; escalated the Elohim-frame identification (proposed-not-committed) → Explainer.
- **Reviewer** (ab3b5f7c): independent Akkadian re-parse of all 185 lines; approved every line and glossary entry; upheld the lens routing; **zero leakage**.

## Human rulings applied
- **Lens (the critical call):** the overpopulation-as-problem, the gods' regret over destroying their own labor-force, their hunger cut off from offerings, and the deliberate population-limiting are rendered **plainly** (all in the Akkadian). The **Elohim/ancient-astronaut identification** is kept OUT of translation and glossary — proposed-not-committed `atrahasis-population-control-elohim-frame`, routed to the Explainer.
- **Ratified:** `eleppu` = "boat" (not "ark" — refuses the Vulgate *arca* / Hebrew *tēbāh* import); `kīma zumbī` = "like flies"; Tablet II refIds normalized to the dot form (`ATRA-WOH-II:{col}.{line}`).
- **`ṭēmu` distinction upheld:** Tablet II's `ṭēmu` = "plan/counsel" correctly held distinct from the Tablet I anthropogonic `ṭēmu→eṭemmu` pun.

## Non-blocking follow-ups (Python/central + collation gates)
- Central `rigmu`/`ḫubūru` creation/flood-cause candidate (vs Hebrew *ḥāmās*/*ṣeʿāqâ*); Akkadian-side `appliesTo` activation for the flood cluster (`abūbu`, `eleppu`, gods-like-flies, council/decree/oath/name, mortality-verdict) on the II/III refIds — deferred to the central Python step (4 MB glossary not touched).
- Sign-level collation (Lambert–Millard 1969 / eBL L.1.1): carry II iii.12, II vi.3, III iii.7 / iii.13 / iv.7. `verificationStatus` holds.

## Comparative apparatus (commentary only, cited + hedged)
Genesis 6–9 flood parallel with the **causation contrast** (noise vs moral corruption); Gilgamesh XI dependence (Atra-ḫasīs the older witness); the flies-simile → Gen 8:21 *rêaḥ nîḥōaḥ* contrast.
