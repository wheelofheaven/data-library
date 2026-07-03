# Chapter 2 Editor Report

**Book:** The Hidden Words (Kalimát-i-Maknúnih), WoH-Translation (HW-WOH) — Part II, the Persian Hidden Words
**Chapter:** 2 (invocation prologue + the 82 Persian Hidden Words, HWP-1…HWP-82 + epilogue)
**Editor pass:** 2026-07 (claude-opus-4-8)
**Status at end of pass:** `editor-review` (advanced from `draft`; version `1.0.0-draft` → `1.0.0-rc1`)

---

## Summary

Part II is **the pipeline's first Persian source text** and completes the
Bahá'í pilot (Part I, the Arabic Hidden Words, is `reviewer-approved`). The
lens-risk profile matches Part I: the single genuine lens-level decision is
the recurring `b-h-y` / *Bahāʾ* self-referential onomastics — which reaches
its sharpest form in **HWP-77's letter-by-letter naming of the Name
(*bāʾ*+*hāʾ* = *Bahāʾ*)** — plus a dense stratum of Persian Sufi-lyric
technical vocabulary requiring fixed English mappings.

The pass (i) **resolved all 8 editorial questions** into glossary entries,
commentary, or literal-consensus readings, escalating **0 new speculative
entries** but flagging **1 standing lens item for explicit re-confirmation**
(the *b-h-y* onomastics / HWP-77 acrostic, per the ratified Part I ruling);
(ii) **extended the overlay glossary** (`_translation-glossary.json`, v1.0.0
→ **v2.0.0**) with **4 new Persian-scoped entries** and **4 modifications**
to reused Part I entries; (iii) applied per-verse `notes.official` commentary
to **24 paragraphs**, leaving the non-divergent aphorisms empty per the
commentary-discipline rule; (iv) made **1 authorized English edit** (HWP-71
*zamān* "Zamán" → "Time", backed by a new glossary entry); (v) recorded the
Part II collation result (no substantive variants) in the collation-witness
entry.

The surface English is a defensible scholarly rendering throughout and is
**independent of the authorised Bahá'í World Centre (Shoghi Effendi)
translation** — most visibly in the HWP-71 *zamān* = "Time" reading (Shoghi
Effendi reifies it into a place-name "Zamán") and in the disciplined
handling of the five deliberate Persian wordplays.

**Counts after pass:**
- Overlay glossary: **v1.0.0 → v2.0.0** (semver-major: modifications of
  existing entries) — **9 → 13 entries** (4 added; 4 modified)
- **0 `speculative` entries committed** to the glossary
- **1 standing `speculative` lens item re-flagged** for explicit
  re-confirmation (the *b-h-y* / HWP-77 acrostic — NOT committed; see below)
- **24 paragraphs with commentary**; all 84 paragraphs carry the Persian
  transliteration-convention ref; all 82 aphorisms carry the Persian
  vocative ref
- **1 authorized English edit** (HWP-71), backed by a glossary entry
- **8 of 8 editorial questions resolved**; `editorial_questions[]` cleared
  to `[]`

---

## Speculative entries requiring sign-off

### `baha-root-self-referential-onomastic-pun` — STANDING ITEM, re-flagged (NOT committed)

**Source:** root *b-h-y* — *ufuq-i abhā* "the Most Glorious Horizon"
(HWP-2), *sarādiq-i abhā* "the Most Glorious Pavilion" (HWP-23), and — most
pointedly — **HWP-77's letter-by-letter naming of the unspeakable Name**:
the first letter (*bāʾ*, ب) draws the celestial dwellers forth, the second
(*hāʾ*, ه) fells them to the dust, i.e. **B-H**, the opening of *Bahāʾ*, the
author's own title.

**WoH choice taken:** kept **strictly neutral** in the surface text
(*abhā* = "Most Glorious"; HWP-77 rendered "the first letter … the second
letter", the acrostic **un-annotated in the line**). The lexical facts (the
root recurs; it is the root of *Bahāʾ-Allāh*; the HWP-77 letters are *bāʾ*
and *hāʾ*) are carried **in commentary only** (HWP-2, HWP-23, HWP-77).

**Why still escalated:** this applies the human ruling of **2026-07-03**
(keep the surface English neutral, pun in commentary only, commit no
`speculative` entry) to Part II. The reason it is re-flagged rather than
silently carried forward is that **HWP-77 is a materially sharper instance
than anything in Part I**: Part I had root-*recurrence* (a homonymy a reader
must notice); HWP-77 is an actual *narrative acrostic* — the text spells the
Name letter by letter and stages the cosmos's reaction to each letter. The
interpretive claim that this is a deliberate authorial self-signature
remains `speculative` (the Hidden Words predate Bahá'u'lláh's 1863 adoption
of the title *Bahāʾ*), and surfacing it would import the lens into the text.

**Recommendation:** **Ship the neutral rendering as-is.** Ask the reviewer
to **confirm by name** that the standing 2026-07-03 ruling extends to
HWP-77's acrostic — i.e., that the letter-narrative stays neutral and
un-annotated in the line, with the B-H fact living in commentary. This is
the one item in the pass that is a WoH-lens call rather than a philological
one, and the only thing blocking advancement past `editor-review`.

---

## Resolution of the 8 editorial questions

| # | Question (refIds) | Resolution |
|---|---|---|
| 1 | Persian transliteration convention (all) | **Resolved** → new overlay entry `dmg-iranica-transliteration-convention-hidden-words-woh-persian` (`direct`). Ratified the drafted DMG / Encyclopaedia-Iranica Persian scheme: macron long vowels (ā ī ū); kh/gh/sh/ch/zh digraphs; underdots retained on Arabic-origin consonants and the embedded Arabic clauses; and the **classical -i/-yi ezāfe** (not modern -e/-ye), because the vocalized OL witness points the classical vowel. Scoped to Persian, parallel to but distinct from the Arabic Part I convention entry. Applied to all 84 paragraphs. |
| 2 | Persian vocative-epithet extension; *khāk*/*turāb* level-or-distinguish (all) | **Resolved** → new overlay entry `persian-vocative-epithet-series-hidden-words-woh` (`inferred`), a **separate** entry from the Arabic Part I one (the Persian ezāfe construction and ~20 new epithets warrant it; keeps the approved Part I entry untouched). All 82 aphorism `glossaryRefs` swapped from the Arabic vocative entry to the Persian one. **Sub-question ruled the OPPOSITE way from Part I's insān/bashar:** *khāk* (Persian) and *turāb* (Arabic loan) are **levelled to "Dust"**, because — unlike insān/bashar, which carry distinct lexical weights — they are interchangeable stylistic synonyms (decisively HWP-48: created *min turāb*, returning *to khāk*, in parallel). Distinguishing them would manufacture a contrast the Persian does not mark (accuracy-before-lens). *gil* "mire/clay" and *ramād* "ashes" kept distinct; *insān* = "Man" (HWP-61) holds. |
| 3 | Sufi bestiary / toponyms — gloss vs retain (HWP-1, 13, 38) | **Resolved** → new overlay entry `persian-sufi-bestiary-cosmological-toponyms-hidden-words-woh` (`inferred`). **Hybrid policy** confirmed: gloss the common images (*bulbul* "nightingale", *gul/gulbun* "rose/rose-bower", *varqāʾ* "dove", *hudhud* "hoopoe"), retain the named entities with no clean English match (*Qáf* the cosmic mountain; *Humá* as "the Humá-bird"); *ʿanqā* = "phoenix" but kept distinct from Humá; *sabā* = "Sheba". Cited at HWP-1, 13, 38. |
| 4 | Bahāʾ-root (*b-h-y*) recurrence + HWP-77 acrostic (HWP-2, 23, 77) | **Resolved as neutral; standing lens item re-flagged** (see above). Surface English kept neutral throughout; HWP-77 letters un-annotated in the line; B-H fact carried in commentary only; **no `speculative` entry committed**, per the ratified Part I ruling. Reviewer asked to confirm the ruling extends to HWP-77 by name. |
| 5 | HWP-71 Sinai toponyms + *zamān* place-vs-"Time" (HWP-71) | **Resolved** → new overlay entry `hwp71-sinai-covenant-toponyms-faran-madyan-zaman-hidden-words-woh` (`inferred`). *Fārān* = "Mount Párán" (Paran, Deut 33:2 / Hab 3:3); *Madyan* = "Midian". **`zamān` overridden from the draft's named-locus "Zamán" to the common noun "Time"** — no Sinai toponym "Zamān" is attested, plain-sense "time" is preferred (accuracy-first), reading the covenant-site as the metaphysical locus of the pre-eternal Covenant (*alastu bi-rabbikum*, Q 7:172); also keeps the text independent of Shoghi Effendi. **1 authorized English edit** at HWP-71. Named-locus reading recorded as the alternative. |
| 6 | HWP-37 *inzāl* crux (+ HWP-57, 50, 68 minor cruxes) | **Resolved in commentary; no entry.** Kept the drafted "for a fleeting shower [of gain]" (*inzāl* √n-z-l "a sending-down/downpour", parallel to *bi-shahvatī* "for a lust"), interpolation bracketed and flagged; literal "a mere sending-down" / idiomatic "a paltry thing" recorded as alternatives. Minor cruxes rendered by default and noted: HWP-57 *nār-i ḥusbān* "fire of perdition" (cf. Q 18:40); HWP-50 *sāẕij* "simpleton"; HWP-68 *dast-i ālūda bi-shakar* "sticky with sugar". |
| 7 | *amr* register in Persian Part II (HWP-29, 43, 77, 80) | **Resolved** → **modified** the existing `amr-cause-vs-command-hidden-words-woh` entry: added an explicit **third "affair/matter" register** and confirmed **none** of the Part II occurrences is the technical "the Cause". *turāb-i amr* "clay of My command" (HWP-29, creative fiat) and *ḥasb al-amr* "according to the [divine] command" (HWP-77) = command/decree; *hīch amrī* "any matter" (HWP-43) and *al-umūr* "affairs" (HWP-80, the maxim *al-umūru muʿallaqatun bi-asbābihā*) = affair/matter. appliesTo extended to HWP-29, 43, 77, 80. |
| 8 | *shajara-yi anīsā* (HWP-19) | **Resolved in commentary; no entry.** Kept "the tree of companionship" — *anīsā* read as an intensive-adjectival form of *uns* "intimacy/companionship" (cf. *anīs*). Proper-name reading ("Tree of Anísá") noted as unattested; Sadra / Tree-of-Life register available but not forced into the text. Single occurrence; no overlay entry (would not yet meet the recurrence bar). |

All 8 `editorial_questions[]` cleared to `[]`.

---

## The five preserved Persian wordplays (glossed in commentary)

Each is a near-minimal pair the Translator preserved and the Editor glossed
without surfacing the philology in the line:

- **HWP-2** — *gul* (گُل "rose") / *gil* (گِل "mire"): "roses of nearness" vs
  "mires of remoteness" (vowel-only contrast).
- **HWP-7** — *qadam* (قدم "step") / *qidam* (قِدَم "pre-eternity"): "take the
  first step … tread upon the realm of pre-eternity".
- **HWP-36** — *dil* (دِل "heart") / *gil* (گِل "mire"): "spring forth from
  the heart and not from the mire" (*d*/*g* contrast).
- **HWP-38** — *nafs* (نفْس "self") / *nafas* (نفَس "breath"): "renounce self
  … with the breath of the All-Merciful" (one skeleton نفس; Ibn ʿArabī's
  *Nafas al-Raḥmān*).
- **HWP-39** — *gulshan* (گلشن "rose-garden") / *gulkhan* (گلخن "furnace,
  ash-pit"): "the everlasting rose-garden … the perishing ash-pit of dust".

---

## Authorized English edits (each backed by a glossary entry)

Per the hard rule that `i18n.en` may not change without a corresponding
glossary change, the **1 edit** is:

- **HWP-71** — "situate within the blessed precincts of **Zamán**" →
  "situate within the blessed precinct of **Time**" (`zamān` as common
  noun; backed by `hwp71-sinai-covenant-toponyms-faran-madyan-zaman-hidden-words-woh`).

No `fa` fields were altered. The vocative-ref swap (Arabic → Persian entry)
on all 82 aphorisms is a `glossaryRefs` change, not a text change.

---

## Glossary changes for review

### Central glossary

**No in-agent edits** (hard-rule compliance: the ~4 MB central glossary was
not loaded or modified). **One deferred action** carried over from Part I
and now also applicable to Part II: extend the `appliesTo` of
`allah-arabic-divine-name-quranic-cross-corpus-hebrew-elohim-aramaic-elah`
to include the **9 HWP refIds** that cite it (HWP-9, 36, 51, 52, 56, 80,
81, 82, epilogue), via the separate Python step.
Until then those paragraphs cite the entry in `glossaryRefs` and this report
flags the scope gap.

### Per-translation overlay (v1.0.0 → v2.0.0)

**Added (4 entries):**

1. `dmg-iranica-transliteration-convention-hidden-words-woh-persian` (`direct`) — Persian scheme; promotion candidate if the Persian corpus grows
2. `persian-vocative-epithet-series-hidden-words-woh` (`inferred`) — the *khāk*/*turāb* levelling is the load-bearing sub-decision
3. `persian-sufi-bestiary-cosmological-toponyms-hidden-words-woh` (`inferred`) — retain-vs-gloss policy
4. `hwp71-sinai-covenant-toponyms-faran-madyan-zaman-hidden-words-woh` (`inferred`) — Fārān/Párán, Madyan/Midian, *zamān*="Time"

**Modified (4 entries; the semver-major driver):**

- `amr-cause-vs-command-hidden-words-woh` — added explicit third "affair/matter" register; appliesTo += HWP-29, 43, 77, 80
- `cosmological-realm-hierarchy-mulk-malakut-jabarut-amaa-hidden-words-woh` — appliesTo += HWP-6, 29, 37, 40, 41, 44, 53, 70, 74
- `insaf-vs-adl-equity-vs-justice-hidden-words-woh` — appliesTo += HWP-4, 77 (Persian *pisar-i inṣāf* vocative)
- `hidden-words-collation-witnesses-…` — added Part II collation note (no substantive variants; the HWP-1 opening-clause structural realignment recorded)

**No `speculative` entry committed.**

---

## Recommended next steps for the Reviewer

1. **Confirm by name** that the standing 2026-07-03 *b-h-y* / *Bahāʾ* ruling
   extends to **HWP-77's letter-by-letter acrostic** (keep neutral,
   un-annotated in the line, B-H in commentary only, no entry). **This is
   the item blocking advancement past `editor-review`.**
2. **Confirm the *khāk*/*turāb* → "Dust" levelling** — note this is the
   *opposite* call from Part I's insān/bashar split, and deliberately so
   (HWP-48 parallelism). Confirm or request a distinction.
3. **Confirm the HWP-71 *zamān* = "Time" override** (the one authorized
   English edit; diverges from Shoghi Effendi's named-locus "Zamán").
4. **Confirm the bestiary retain-vs-gloss policy** — esp. *ʿanqā* =
   "phoenix" kept distinct from *Humá* (retained).
5. **Confirm the Persian transliteration convention** (macrons + classical
   -i/-yi ezāfe) as the project standard for Persian sources.
6. **Confirm the *amr* third-register extension** and that no Part II
   occurrence is the technical "Cause".
7. **Action the deferred central-glossary `appliesTo` extension** for the
   `allah` entry (add the HWP refIds) via the Python step.
8. **Verify the Persian source against a pre-1930 lithograph** — project
   policy (strategy-library-acquisition.md) requires lithograph
   verification before final sign-off; still **pending** for both Parts and
   should not be signed off as verified.
9. **Confirm** chapter-2.json structural validation: 84 paragraphs; all
   `glossaryRefs` resolve; commentary on the 24 divergent paragraphs and
   empty elsewhere; `editorial_questions` cleared.

After Reviewer sign-off (including an explicit ruling by name on the
HWP-77 / *b-h-y* `speculative` item), the chapter advances from
`editor-review` to `reviewer-approved`, then to `published` after human
sign-off.
