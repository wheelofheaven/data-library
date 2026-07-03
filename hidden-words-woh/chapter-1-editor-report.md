# Chapter 1 Editor Report

**Book:** The Hidden Words (Kalimát-i-Maknúnih), WoH-Translation (HW-WOH) — Part I, the Arabic Hidden Words
**Chapter:** 1 (prologue + the 71 Arabic Hidden Words, HWA-1…HWA-71)
**Editor pass:** 2026-07 (claude-opus-4-8)
**Status at end of pass:** `editor-review` (advanced from `draft`; version `1.0.0-draft` → `1.0.0-rc1`)

---

## Summary

The Hidden Words are **the project's first Bahá'í-tradition text and its
second Arabic-source text** (after the Qur'an-WoH selection). The lens-risk
profile is milder than the Qur'an's — there is no explicit Raëlian-canon
chapter-and-verse engagement to disavow — but there is one genuinely
lens-level decision (the Bahāʾ-root self-referential pun) and a dense set of
Sufi-theosophical technical vocabulary requiring fixed English mappings.

The pass (i) created a new per-book overlay glossary
(`hidden-words-woh/_translation-glossary.json`, v1.0.0) with **9 entries**;
(ii) resolved **12 of 13** editorial questions into glossary entries,
commentary, or literal-consensus readings, and **escalated 1** (the
Bahāʾ-root pun) as a proposed `speculative` entry requiring human sign-off;
(iii) applied per-verse `notes.official` commentary to **26 paragraphs**
(prologue + 25 aphorisms), leaving the non-divergent aphorisms empty per
the commentary-discipline rule; (iv) made **7 authorized English edits**
(each backed by a glossary entry); (v) recorded the **4 source variants**
in a collation-witness entry and in per-verse commentary.

The surface English is a defensible scholarly rendering throughout and is
**independent of the authorised Bahá'í World Centre (Shoghi Effendi)
translation** — most visibly in the deliberate `insān`/`bashar` distinction
(Shoghi Effendi levels both to "O Son of Man"; the WoH renders `ibn
al-bashar` "O Son of Mortal Man").

**Counts after pass:**
- Overlay glossary: new file at **v1.0.0** — **9 entries** (5 `inferred`, 4 `direct`)
- **0 `speculative` entries committed** to the glossary
- **1 `speculative` entry escalated** (Bahāʾ-root pun — NOT committed; see below)
- **26 paragraphs with commentary + `glossaryRefs[]`**; all 72 paragraphs carry the two convention refs, all 71 aphorisms carry the vocative ref
- **12 of 13 editorial questions resolved; 1 escalated**
- `editorial_questions[]` cleared to `[]`

---

## Speculative entries requiring sign-off

### `baha-root-self-referential-onomastic-pun-hidden-words-woh` (PROPOSED — NOT committed)

**Source:** root b-h-y — *al-bahiyy al-abhā* (prologue heading), *bahāʾī*
"My glory" (HWA-14), *al-shajar al-abhā* "the most-glorious tree" (HWA-21),
*jamāl* / aesthetic-glory field (HWA-67).
**WoH choice under consideration:** foreground, in the surface English
and/or as a capitalised "Glory / All-Glorious", the fact that the recurring
b-h-y "glory/splendour" vocabulary is homonymous with the author's own
title *Bahāʾ-Allāh* ("the Glory of God"), reading the recurrence as a
deliberate authorial self-signature.
**Why speculative:** The *lexical* facts are direct and are already carried
in commentary (the root recurs; it is the root of the author's title; this
is uncontested). What crosses into `speculative` is the *interpretive*
claim that the recurrences are an intentional self-referential pun, and the
editorial move of surfacing that reading in the translated text via
capitalisation or glossing. Bahá'u'lláh adopted the title *Bahāʾ* in 1863
(Riḍván), several years *after* the Hidden Words (Baghdad, c. 1857–58), so
a deliberate-self-signature reading is a project-specific synthesis, not
something any single source attests; it also risks importing the WoH lens
into the surface text in violation of the "lens lives in the apparatus"
rule.
**Recommendation:** **Ship the neutral rendering as-is** ("glory /
splendour / Most Glorious", pun noted in commentary at prologue, HWA-14,
HWA-21 only). **Do not** capitalise "Glory" in the surface text or commit
the pun entry without sign-off. If the reviewer wants the resonance
surfaced, the correct home is an expanded commentary note or a wiki
cross-reference, **not** the translated line. This is the single decision
in the pass that is a WoH-lens call rather than a philological one.

---

## Resolution of the 13 editorial questions

| # | Question (refIds) | Resolution |
|---|---|---|
| 1 | `yā bna …` vocative series (all) | **Resolved** → overlay entry `ya-bna-vocative-epithet-series-hidden-words-woh` (`inferred`). Rendered literally, epithet-by-epithet; **`insān` and `bashar` distinguished**: `ibn al-insān` = "O Son of Man", `ibn al-bashar` = "O Son of Mortal Man" (7 English edits at HWA-7/21/52/58; the distinction both increases lexical precision and keeps the rendering independent of Shoghi Effendi). Other epithets: Spirit / Being / Utterance / Light / Supreme Vision / Cloud / Throne / Beauty / Sons of the Divine Essence in the unseen / Son of Him who arose in the kingdom of His own self. |
| 2 | `amr` Cause-vs-command (HWA-16,29,30,34,40,41,42,46,51,65) | **Resolved** → overlay entry `amr-cause-vs-command-hidden-words-woh` (`inferred`). Contextual split confirmed and standardised: **"Cause"** for the institutional/religion sense (16, 34, 40, 41, 42, 46, 65), **"command/bidding"** for the imperative/decree sense (29, 30, 51). |
| 3 | Bahāʾ-root (b-h-y) pun (prologue, HWA-14, 21, 67) | **ESCALATED** (see above). Surface English kept neutral; pun noted in commentary only; proposed `speculative` entry NOT committed. |
| 4 | Realm hierarchy `mulk/malakūt/jabarūt/ʿamāʾ` (prologue, HWA-1,6,14,15,23,32,40,42,70) | **Resolved** → overlay entry `cosmological-realm-hierarchy-mulk-malakut-jabarut-amaa-hidden-words-woh` (`inferred`). Fixed mapping disambiguating `mulk`="dominion" from `jabarūt`="realm of omnipotence" (draft had both as "dominion"): `mulk`=dominion, `malakūt`=kingdom, `jabarūt`=realm of omnipotence, `ʿamāʾ`=the Cloud. Two English edits (prologue "omnipotent realm of glory"; HWA-6 "realm of omnipotence"; HWA-42 "in the dominion"). |
| 5 | HWA-63 `nafaḵta` vs `nafaḵtu` (pointing → subject) | **Resolved** → read **1st person `nafaḵtu`** ("I breathed"), restoring the divine-speaker parallelism with `ašraqtu`. `ar` field retains the witness's `nafaḵta`; English + translit adopt the emendation, flagged (not silent). Recorded in `hidden-words-collation-witnesses-…` and HWA-63 commentary. |
| 6 | HWA-61 `kuʾūb` (pl.) vs BWC `kūb` (sg.) | **Resolved** → follow retained OL witness: **plural "cups"**. `ar` unchanged; recorded in collation-witness entry + HWA-61 commentary. |
| 7 | HWA-70 omission of `bi-dhātihi` | **Resolved** → follow retained OL witness (**no "by His own essence"**). BWC fuller reading noted. Recorded in collation-witness entry + HWA-70 commentary. |
| 8 | HWA-71 `alqaynāka` vs BWC `alqaynā ilayka` | **Resolved** → follow OL; **English identical either way**. Recorded for completeness in collation-witness entry + HWA-71 commentary. |
| 9 | `inṣāf` (HWA-2) vs `ʿadl` (HWA-28) | **Resolved** → overlay entry `insaf-vs-adl-equity-vs-justice-hidden-words-woh` (`inferred`). Distinguished: `inṣāf`="equity", `ʿadl`="justice". |
| 10 | `aḥbār` (prologue) | **Resolved** → overlay entry `ahbar-the-learned-doctors-of-religion-hidden-words-woh` (`inferred`). "as a favour unto the learned" (literal reading over generalising "men"). |
| 11 | `Allāh` → "God"; `appliesTo` scope gap | **Resolved with a flagged deferral.** "God" retained (literal + matches the existing central entry). The central entry `allah-arabic-divine-name-…` is cited in the prologue `glossaryRefs`, but its `appliesTo` array currently lists **only** QUR-WOH refIds. **Extending that central `appliesTo` to include HWA-prologue is deferred to the separate Python step** (per the hard rule against loading/editing the ~4 MB central glossary in-agent). **Reviewer action item** — see below. No duplicate overlay `allah` entry was created (would bloat). |
| 12 | `istishhād` / martyrdom (HWA-45,46,47; +71) | **Resolved** → overlay entry `istishhad-fi-sabili-martyrdom-in-the-path-hidden-words-woh` (`direct`). **Literal** "seek martyrdom / be martyred in My path", preserving the `fī sabīlī` idiom; spiritual-self-sacrifice extension noted, not substituted. |
| 13 | Transliteration + rasm conventions (all) | **Resolved** → two overlay entries: `dmg-ala-lc-transliteration-convention-hidden-words-woh-arabic` (`direct`) and `rasm-skeleton-convention-hidden-words-woh-tashkil-strip-bracket-removal` (`direct`). The rasm entry documents that — **unlike the Qur'an-WoH paleographic convention** — hamza-seating and tāʾ-marbūṭa are **NOT** normalized here (this is a modern-orthography skeleton, not an early-Hijazi reconstruction; the Hidden Words have no early-manuscript paleographic layer). |

All 13 `editorial_questions[]` cleared to `[]`.

---

## Authorized English edits (each backed by a glossary entry)

Per the hard rule that `i18n.en` may not change without a corresponding
glossary change, the 7 edits are:

- **HWA-7, HWA-21, HWA-52, HWA-58** — "O Son of Man" → **"O Son of Mortal Man"** (`bashar`; vocative-series entry)
- **prologue** — "from the dominion of glory" → **"from the omnipotent realm of glory"** (`jabarūt`; realm-hierarchy entry)
- **HWA-6** — "Our exalted kingdom and Our most sublime dominion" → **"Our most exalted kingdom and Our most sublime realm of omnipotence"** (`malakūt`/`jabarūt`; realm-hierarchy entry)
- **HWA-42** — "victorious in the kingdom" → **"victorious in the dominion"** (`mulk`; realm-hierarchy entry)

The `ar` fields were **not** altered anywhere (including the four source
variants); the HWA-63 `nafaḵtu` first-person reading is carried in the
English and transliteration only, with the `ar` witness pointing retained.

---

## Glossary changes for review

### Central glossary

**No in-agent edits** (hard-rule compliance: the ~4 MB central glossary was
not loaded or modified). **One deferred action** for the separate Python
step: extend the `appliesTo` of `allah-arabic-divine-name-quranic-cross-corpus-hebrew-elohim-aramaic-elah`
to include `HWA-prologue` (currently QUR-WOH-only). Until then the prologue
cites the entry in `glossaryRefs` and this report flags the scope gap.

### Per-translation overlay (new file, v1.0.0)

**Added (9 entries):**

1. `dmg-ala-lc-transliteration-convention-hidden-words-woh-arabic` (`direct`) — promotion candidate (merge with Qur'an convention if corpus grows)
2. `rasm-skeleton-convention-hidden-words-woh-tashkil-strip-bracket-removal` (`direct`) — documents the deliberate **non**-normalization of hamza/tāʾ-marbūṭa vs the Qur'an paleographic convention
3. `ya-bna-vocative-epithet-series-hidden-words-woh` (`inferred`) — the `insān`/`bashar` distinction is the load-bearing decision
4. `amr-cause-vs-command-hidden-words-woh` (`inferred`)
5. `cosmological-realm-hierarchy-mulk-malakut-jabarut-amaa-hidden-words-woh` (`inferred`)
6. `insaf-vs-adl-equity-vs-justice-hidden-words-woh` (`inferred`)
7. `istishhad-fi-sabili-martyrdom-in-the-path-hidden-words-woh` (`direct`)
8. `ahbar-the-learned-doctors-of-religion-hidden-words-woh` (`inferred`)
9. `hidden-words-collation-witnesses-oceanoflights-primary-bwc-control-retained-edition-variants` (`direct`) — the 4 retained OL-vs-BWC variants

**Modified / promoted:** none (new file).

---

## Recommended next steps for the Reviewer

1. **Rule on the escalated Bahāʾ-root pun** (`speculative`). Editor
   recommendation: keep neutral surface English, pun in commentary only, do
   **not** commit the entry. This is the one item blocking advancement past
   `editor-review`.
2. **Confirm the `insān`/`bashar` split** — "O Son of Man" vs "O Son of
   Mortal Man". It is the most visible divergence from Shoghi Effendi and
   the project's independence-of-authorised-translation showcase for this
   text. Confirm the "Mortal Man" wording or propose an alternative
   ("Son of Mankind" / "Son of Humankind" were considered and rejected as
   losing the mortality nuance carried by the corpus `bashar`="mortal" entry).
3. **Confirm the `amr` Cause/command split** (or standardise to one register).
4. **Confirm the realm-hierarchy fixed mapping**, especially `jabarūt`=
   "realm of omnipotence" (the disambiguation from `mulk`="dominion").
5. **Verify the 4 source variants** (HWA-61 `kuʾūb`; HWA-63 `nafaḵtu`
   emendation; HWA-70 `bi-dhātihi` omission; HWA-71 `alqaynāka`) against a
   pre-1930 lithograph — project policy (strategy-library-acquisition.md)
   requires lithograph verification before final sign-off; this is still
   **pending** and should not be signed off as verified.
6. **Action the deferred central-glossary `appliesTo` extension** for the
   `allah` entry (add `HWA-prologue`) via the Python step.
7. **Confirm** chapter-1.json structural validation: 72 paragraphs; all
   `glossaryRefs` resolve to real overlay/central entries; commentary
   populated on the 26 divergent paragraphs and empty elsewhere; all
   `editorial_questions` cleared.

After Reviewer sign-off (including an explicit ruling on the Bahāʾ-root
`speculative` item by name), the chapter advances from `editor-review` to
`reviewer-approved`, then to `published` after human sign-off.
