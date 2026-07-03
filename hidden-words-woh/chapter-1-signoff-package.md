# The Hidden Words, Part I (Arabic) — sign-off package

**Status:** `awaiting-human` — reviewer approved all 71 aphorisms + prologue as defensible renderings; three human gates remain before final sign-off.
**Text:** *Kalimát-i-Maknúnih*, Part I — the 71 Arabic Hidden Words of Bahá'u'lláh (c. 1857–58, Baghdad) + the opening invocation/preamble. **72 paragraphs in one chapter file.**
**Version:** 1.0.0-rc1
**Glossary:** new per-book overlay v1.0.0 (9 entries); central glossary untouched (one deferred `appliesTo` extension — see gates).
**⚠ verificationStatus:** original collated against the Bahá'í World Centre reference edition; **four readings pending pre-1930 lithograph verification** per `strategy-library-acquisition.md`.

## Summary table

| Metric | Value |
|---|---|
| Aphorisms translated | 71 / 71 + prologue |
| `ar` fidelity | byte-identical to `source-ar-1.json` (0 mismatches) |
| Reviewer verdicts | **72 approve / 0 revise / 0 veto** on the translations |
| Editorial questions | 13 raised → **12 resolved, 1 escalated** |
| Overlay glossary entries | 9 (4 `direct`, 5 `inferred`, **0 `speculative` committed**) |
| Lens-leakage flags | **0** (verse-by-verse sweep) |
| Independence from Shoghi Effendi | maintained; divergences disciplined, all disclosed in apparatus |
| Items requiring human ruling | **3** |

## Pipeline
- **Translator** (a8c89929): 72-paragraph draft in the Qur'an production format; 13 editorial questions; `ar` verbatim.
- **Editor** (af215cec): resolved 12/13; built the 9-entry Hidden Words overlay glossary; commentary on 26 paragraphs; escalated the Bahā-root pun.
- **Reviewer** (aea8df77): independent re-parse of all 72 paragraphs; approved every rendering; upheld the pun escalation (veto on surfacing); confirmed glossary claim-type discipline; zero lens-leakage.

## Milestones
- **The project's first Bahá'í-tradition text** end-to-end through the four-stage pipeline (tradition `bahai`, code BAH, previously empty of translated work).
- **The declared Bahá'í pilot** of the Translation Program; Part II (Persian, 82 aphorisms) is the next chapter and the pipeline's first Persian work.

## Three human gates (why status is `awaiting-human`)

1. **Bahā-root (b-h-y) self-referential pun — ruling needed by name.**
   Editor and reviewer *agree*: keep the English neutral ("glory / splendour / Most Glorious"), record the homonymy with the author's title *Bahá'u'lláh* as lexical fact in commentary only, and **do not** commit the `speculative` glossary entry. Rationale: the Hidden Words predate the assumption of the title *Bahāʾ* (Riḍván 1863) by ~5 years, so surfacing the pun in the line would be anachronistic retrojection. **Recommended action: ratify the neutral reading.**

2. **Pre-1930 lithograph verification of four source variants** (project policy). All four are retained-and-flagged on the Ocean of Lights witness; the reviewer notes two where the OL reading is most likely idiosyncratic/secondary and the lithograph is load-bearing:
   - **v61** `kuʾūb` (cups, pl.) — morphologically unusual (expected pl. *akwāb*); BWC has `kūb` (sg.).
   - **v70** omits `bi-dhātihi` ("by His own essence") — both BWC and Shoghi carry it; OL omission is plausibly haplography.
   - v63 `nafaḵtu` (1st person) — emendation of a witness pointing-error; strongly supported, but `ar` vocalization should be emended to match if the lithograph confirms.
   - v71 `alqaynāka` — sense-neutral, lowest stakes.
   **Decision needed: hold final sign-off for the lithograph, or accept retain-and-flag with the BWC collation as sufficient for a release candidate.**

3. **Central-glossary `appliesTo` extension** (deferred Python step) — add `HWA-prologue` to the central `allah-…` divine-name entry's `appliesTo`. Kept out of the agent pass per the known 4 MB central-glossary limitation; apply via direct Python.

## Files
- `chapter-1.json` — `awaiting-human`, 1.0.0-rc1, 72 paragraphs, commentary on 26, `ar` untouched.
- `_translation-glossary.json` — overlay v1.0.0, 9 entries.
- `chapter-1-editor-report.md` — editor adjudication + escalation.
