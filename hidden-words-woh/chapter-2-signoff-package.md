# The Hidden Words, Part II (Persian) — sign-off package

**Status:** `reviewer-approved` (RC), human-ratified 2026-07-03 — completes the Bahá'í pilot (both Parts now translated).
**Text:** *Kalimát-i-Maknúnih*, Part II — the 82 Persian Hidden Words + invocation + epilogue (84 paragraphs). The pipeline's **first Persian-source work**.
**Version:** 1.0.0-rc1 · **Glossary:** overlay **v2.0.0** (13 entries; 0 speculative committed).
**⚠ verificationStatus:** collated against the Bahá'í World Centre original; **no substantive Persian variants** (differences are orthographic house-style only). Pre-1930 lithograph verification pending for both Parts — flagged follow-up, not a blocker.

## Summary table

| Metric | Value |
|---|---|
| Aphorisms translated | 82 / 82 + prologue + epilogue |
| `fa` fidelity | byte-identical to `source-fa-2.json` |
| Reviewer verdicts | **83 approve / 0 revise / 0 veto**; HWP-77 lens-ratification (philology endorsed) |
| Editorial questions | 8 raised → **8 resolved** |
| Glossary entries added | 4 (Persian translit convention `direct`; Persian vocatives `inferred`; Sufi bestiary/toponyms `inferred`; HWP-71 Sinai toponyms `inferred`) + 4 modifications |
| Lens-leakage flags | **0** |
| Independence from Shoghi Effendi | maintained (e.g. HWP-71 `zamān`="Time" not the place-name "Zamán") |

## Pipeline
- **Translator** (a69761c2): 84-paragraph draft; 8 editorial questions; `fa` verbatim; 5 Persian wordplays preserved.
- **Editor** (a36d100f): resolved 8/8; glossary → v2.0.0; commentary on 24 paragraphs; ruled `khāk`/`turāb` levelled ("Dust") — deliberately *opposite* to Part I's `insān`/`bashar` split (HWP-48 parallelism decisive); re-flagged HWP-77.
- **Reviewer** (a5b33bf4): independent re-parse; approved all renderings; **declined the veto** on HWP-77 (neutral surface is *also* the accurate reading — the Persian withholds the Name); zero lens-leakage.

## Human ruling applied
The standing 2026-07-03 **Bahā-root neutral** ruling was extended to **HWP-77's letter-by-letter acrostic** (bāʾ+hāʾ = Bahāʾ) per unanimous editor+reviewer recommendation: surface English literal ("the first letter … the second letter"), onomastics in commentary only, no speculative entry. *Flag if you want this sharper instance handled differently.*

## Pilot complete
Both Parts (71 Arabic + 82 Persian) are reviewer-approved release candidates. `hidden-words-woh` is now catalog `status: complete`, `completeLangs: [en]`. Remaining follow-ups: pre-1930 lithograph verification (both Parts); central-glossary `allah` `appliesTo` extension (Python step, HWA-prologue + 9 HWP refs).
