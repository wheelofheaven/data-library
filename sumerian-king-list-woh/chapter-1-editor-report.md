# Chapter 1 Editor Report — Sumerian King List (SKL-WOH)

**Stage:** Editor → Reviewer
**Chapter:** `data-library/sumerian-king-list-woh/chapter-1.json`
**Advanced to:** `translation.status = editor-review`, `translation.version = 1.0.0-rc1`,
`translation.overlayGlossaryVersion = 1.0.0` (`reviewer = pending`).
**Overlay created:** `data-library/sumerian-king-list-woh/_translation-glossary.json`
(v1.0.0, 12 entries).
**Central glossary:** NOT modified by the Editor (4.6 MB; write-crash constraint).
All central-side changes are specified below as diffs marked **CENTRAL — apply by
orchestrator**.

---

## Speculative entries requiring sign-off

**None.** No `claim_type = speculative` entry was created. The overlay is 11 `direct`
+ 1 `inferred` (see below). Every WoH-lens dimension that a speculative reading would
have carried (the sky-descent of *an-ta*; Etana's literal bodily ascent; a non-human
paternity for Gilgameš) was deliberately confined to per-line commentary and to the
wiki, and was **not** encoded into the translated text or into any glossary `wohChoice`
— accuracy before lens (Hard rule 1). See "Lens-discipline records" below.

The single `inferred` entry (`gilgamesh-phantom-father-lil-crux-skl`) is flagged for
Reviewer attention as the one WoH-adjacent crux where the retained reading ("a
phantom") is defensible but not consensus.

---

## Editorial-question resolutions (15/15 resolved)

All 15 Translator defaults were **ratified**, with two refinements: SKL-113 keeps the
default rendering but its `claim_type` is set to `inferred` (crux, not consensus), and
SKL-181's convention is ratified **and enforced uniformly** by normalizing the two
draft outliers (SKL-336, SKL-338).

### `SKL-1` — *an-ta* / "kingship descended from heaven"
**Decision:** Ratify default "from heaven." Surface rendering is glossary-fixed
(central `nam-lugal-an-ta-ed-de-a-ba-...`, consensus) and unchanged. The sky-descent
dimension is recorded in commentary **only**; no text change, no new glossary
`wohChoice`.
**Rationale:** *an-ta* = *an* "heaven/sky" + ablative *-ta*; *ed₃* is vertical-motion.
The spatial reading is grammatically available, but the consensus surface is "from
heaven," and the lens belongs in the apparatus, not the text (Hard rules 1, 2).

### `SKL-4` — antediluvian regnal figures (sar/ner)
**Decision:** Ratify "bare composite numeral, no gloss." Codified project-wide in the
overlay entry `sexagesimal-reign-figure-rendering-convention-skl`.
**Rationale:** Matches ETCSL and the cuneiform sign-values; the sar (3600) / ner (600)
structure and the Genesis 5 / Berossus longevity comparison are carried in the SKL-4
commentary, not the figures.

### `SKL-181` — sexagesimal *šu-ši* (60) units
**Decision:** Ratify "computed product + parenthetical factor" (`N years (N × 60)`)
**and enforce it uniformly**: the two draft outliers that read "7 sixties" (SKL-336,
SKL-338) were normalized to "420 years (7 × 60)". One convention now governs the whole
composition (overlay entry as above).
**Rationale:** The draft was internally inconsistent (181/183/187/188 computed the
product; 336/338 did not). The product form matches ETCSL and preserves the reader's
ability to reconstruct the arithmetic.

### `SKL-39` — flood formula *a-ma-ru ba-ur₃*
**Decision:** Ratify "the flood swept over."
**Rationale:** Matches ETCSL and the WoH Flood-Story rendering; *ur₃* "sweep/efface"
here stands intransitively (no stated object), noted in commentary.

### `SKL-42` — post-diluvian toponym/onomasticon transliteration (š/ĝ/ḫ)
**Decision:** Ratify "preserve š and ĝ; anglicize only ḫ→h." SKL-specific roster placed
in overlay `skl-postdiluvian-toponym-onomasticon-roster`. The conflict flagged by the
Translator (the central convention entry's `wohChoice` literally says "sh for š", which
the Flood-Story output and the five-cities entry already contradict) is escalated as a
**CENTRAL** diff (see below).
**Rationale:** Matches the Flood-Story precedent and the central five-antediluvian-cities
entry (Šuruppag, Bad-tibira); preserves phonemic information; ḫ→h aids the general
reader.

### `SKL-97` — *en* vs *lugal*
**Decision:** Ratify *en* = "lord" (standalone); *lugal* = "king"; *en* untranslated
inside frozen throne-names. Overlay `en-lugal-royal-title-distinction-skl`.
**Rationale:** "Lord" is the neutral value ETCSL also uses; over-specifying to "high
priest" asserts a cultic office the line does not spell out. Keeps *en* ≠ *lugal*.

### `SKL-8` — dynasty-fall verb *ba-šub* / *ba-šub-be₂-en*
**Decision:** Ratify impersonal "Then X was abandoned" for both forms. Overlay
`basub-dynasty-abandonment-verb-crux-skl`.
**Rationale:** The apparent 2nd-person *-en* has no addressee in the ledger-style text;
ETCSL renders both impersonally. Best taken as a morphological feature of the formula.

### `SKL-93` — defeat formula *(ĝiš)tukul ba-an-sag₃*
**Decision:** Ratify "was defeated by force of arms"; variants (*ba-gul*; *bal-bi
ba-kur₂*) carried inline. Overlay `tukul-ba-sag-defeat-formula-skl`.
**Rationale:** ETCSL idiom; the concrete "weapon struck it" image is preserved in the
`translit`/`literal` fields.

### `SKL-15` — DINGIR determinative on **deified** kings
**Decision:** Ratify silent drop per the central convention; deification flagged in
commentary. Overlay scope-note `deified-king-dingir-determinative-scope-note-skl`.
**Rationale:** The determinative is unpronounced; "the divine Šulgi" over-renders an
orthographic sign. Royal deification (Dumuzid, Gilgameš, Ur III / Isin kings) is real
and is stated in the apparatus, not the prose.

### `SKL-64` — Etana's ascent
**Decision:** Ratify "the one who ascended to heaven"; apply the central ascent entry
and extend its `appliesTo` (**CENTRAL** diff below).
**Rationale:** *an-še₃ … ed₃* is grammatically explicit; the Etana-Adapa-Enoch-Elijah
motif is cross-corpus. The literal-ascent lens reading stays in commentary.

### `SKL-113` — Gilgameš's paternity *lil₂-la₂*
**Decision:** Ratify rendering "a phantom" **but set `claim_type = inferred`** (the one
refinement of a default). Overlay `gilgamesh-phantom-father-lil-crux-skl`.
**Rationale:** *lil₂*/*lilû* spirit-reading matches ETCSL but is a genuine crux (vs
*lillu* "deficient one / nobody"); the WoH-adjacent non-human-paternity upgrade is
declined. Flagged for the Reviewer.

### `SKL-353A` — *ki-en-gi* "Sumer"
**Decision:** Ratify "Sumer." Overlay `ki-en-gi-sumer-homeland-name-skl`; kept distinct
from *kalam* "the Land."
**Rationale:** Endonym, standard; the homeland-name carries the emotional weight of the
Ur III collapse.

### `SKL-160` — occupation-epithets (low-born rulers)
**Decision:** Ratify standard ETCSL occupational renderings; *gudug* transliterated.
Overlay `occupation-epithets-low-born-rulers-skl`.
**Rationale:** Settled Sumerological values; the low-born-ruler ideology (culminating
in Sargon) is noted in commentary, not asserted in the text.

### `SKL-284` — kingless / nameless interregnum
**Decision:** Ratify direct ETCSL rendering ("Who was king? Who was not king?"; "whose
name is unknown"), *mu* = "name," with the "fame/renown" nuance in commentary. Overlay
`kingless-interregnum-formulae-skl`.
**Rationale:** Preserves the composition's rare rhetorical register.

### `SKL-73A` — *bal* subtotal-insertion lines
**Decision:** Ratify *bal* = "reign"; insertion lines (73A, 89A, 106A, 249A, 283A) kept
as translated content. Overlay `bal-dynastic-reign-term-skl`.
**Rationale:** *bala* = "turn / term of office / reign," the rotating-kingship concept
that structures the list; ETCSL numbers and prints these lines as transmitted text.

---

## Lens-discipline records (WoH-salient sites held to the apparatus)

Three lines are WoH-salient and were deliberately kept at the defensible-scholarly
surface, with the lens confined to commentary/wiki — recorded here for auditability:

- **`SKL-1` / `SKL-41` (*an-ta*):** text stays "from heaven"; the "descent from the
  sky" dimension is commentary-only. No lens in the text or glossary.
- **`SKL-64` (Etana):** text says only "ascended to heaven" (what the Sumerian states);
  the literal-ascent reading is apparatus-only.
- **`SKL-113` (Gilgameš's father):** text stays "a phantom" (`inferred`); no upgrade to
  a definite non-human/divine paternity.

---

## Overlay entries added (`_translation-glossary.json` v1.0.0)

**12 entries — `claim_type`: 11 `direct`, 1 `inferred`, 0 `speculative`.**

| id | claim_type | governs |
|---|---|---|
| `title-and-meta-conventions-skl` | direct | chapter title/meta |
| `sexagesimal-reign-figure-rendering-convention-skl` | direct | SKL-4, 181, 183, 187, 188, 336, 338 |
| `skl-postdiluvian-toponym-onomasticon-roster` | direct | 15 toponym first-occurrences |
| `en-lugal-royal-title-distinction-skl` | direct | SKL-97, 114 |
| `occupation-epithets-low-born-rulers-skl` | direct | 14 epithet lines |
| `gilgamesh-phantom-father-lil-crux-skl` | **inferred** | SKL-113 |
| `bal-dynastic-reign-term-skl` | direct | SKL-73A, 89A, 106A, 249A, 283A |
| `basub-dynasty-abandonment-verb-crux-skl` | direct | SKL-8, 18, 24, 30 |
| `tukul-ba-sag-defeat-formula-skl` | direct | 19 defeat-formula lines |
| `kingless-interregnum-formulae-skl` | direct | SKL-284, 309 |
| `ki-en-gi-sumer-homeland-name-skl` | direct | SKL-353A |
| `deified-king-dingir-determinative-scope-note-skl` | direct | SKL-15, 107, 112 |

Commentary (`notes.official`) written for 14 salient lines: SKL-1, 4, 15, 39, 41, 64,
73A, 97, 100, 113, 160, 284, 353A, 428. Mechanical regnal-summary lines left empty by
design (salient-verses-only policy).

---

## CENTRAL-glossary changes for review

> **CENTRAL — apply by orchestrator.** The Editor did not touch
> `data-content/i18n/translation-glossary.json`. Bump its `version` on application
> (semver-minor for additions / appliesTo activation; semver-major for the `wohChoice`
> modification in Diff 2b, if adopted).

### CENTRAL Diff 1 — extend `human-ascent-...` appliesTo (Etana) — REQUIRED (SKL-64)

Entry id: `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus`
Current `appliesTo`: `["ADP-WOH-B:18", "ADP-WOH-B:22", "ADP-WOH-B:35"]`
**Add:** `"SKL-64"`, `"SKL-65"`
Resulting `appliesTo`:
```json
["ADP-WOH-B:18", "ADP-WOH-B:22", "ADP-WOH-B:35", "SKL-64", "SKL-65"]
```

### CENTRAL Diff 2 — SKL-42 toponym convention

The Translator correctly flagged that the central entry
`sumerian-proper-name-transliteration-convention` is **self-contradictory**: its
`wohChoice` documents anglicized digraphs ("sh for š", e.g. "Shu-zi-ana") for the
Enki-and-Ninmah chapter, yet the Flood-Story output and the central
`five-antediluvian-cities-...` entry **preserve** š (Šuruppag, Bad-tibira). The SKL
Editor ruling (preserve š/ĝ, anglicize only ḫ→h) follows the latter, de-facto standard.
Two application options; **Diff 2a (new entry) is recommended** so the ENM-era
description is left intact.

**Diff 2a (RECOMMENDED) — add a new central entry** codifying the Sumerian-arc
preserve-š/ĝ standard:
```json
{
  "id": "sumerian-toponym-onomasticon-preserve-s-and-g-anglicize-h-convention-cross-corpus",
  "source": "(convention)",
  "translit": "š (postalveolar /ʃ/) and ĝ (velar nasal /ŋ/) PRESERVED; ḫ (velar/uvular fricative) → h",
  "strongs": null,
  "lemma": "(convention)",
  "partOfSpeech": "transliteration-convention — Sumerian-arc toponyms and royal onomasticon",
  "literal": "preserve š and ĝ in the English prose; anglicize only ḫ→h",
  "standardEnglish": "Akkadian-conventional English forms (Kish, Uruk, Ur, Akkad) are common; ETCSL and this project preserve the Sumerian forms (Kiš, Unug, Urim, Agade).",
  "wohChoice": "For the Sumerian-arc texts (Flood Story, Sumerian King List, and successors), i18n.en prose PRESERVES š and ĝ and anglicizes ONLY ḫ→h — Kiš, Unug, Urim, Akšak, Agade, Hamazi (ḫa-ma-zi), Šuruppag, Meškiaĝgašer, Šarru-kin, Šulgi. This supersedes, for these texts, the earlier Enki-and-Ninmah practice of anglicizing š→sh (documented in `sumerian-proper-name-transliteration-convention`). The translit field keeps the strict ETCSL forms.",
  "claim_type": "direct",
  "rationale": "The project's Sumerian-arc output (Flood Story onward) and the central five-antediluvian-cities entry preserve š and ĝ, whereas the older Enki-and-Ninmah convention entry describes š→sh anglicization; the two practices diverge, and the King List needs the preserve-š/ĝ standard fixed centrally. Preserving š and ĝ retains the phonemic information a scholarly reader needs and keeps the toponyms visually consistent across the Sumerian corpus, while the ḫ→h relaxation aids the general reader. No lens is carried; this is an orthographic-consistency convention only.",
  "appliesTo": ["SKL-42", "SKL-84", "SKL-94", "SKL-103", "SKL-110", "SKL-114", "SKL-133", "SKL-147", "SKL-178", "SKL-204", "SKL-210", "SKL-231", "SKL-265", "SKL-332", "SKL-425", "FLS-WOH-B:11", "FLS-WOH-B:12", "FLS-WOH-B:13", "FLS-WOH-B:14", "FLS-WOH-B:15"]
}
```

**Diff 2b (ALTERNATIVE, semver-major) — modify the existing entry.** If you prefer not
to add a new entry, append a superseding clause to the `wohChoice` of
`sumerian-proper-name-transliteration-convention`:
> "Scope update: for the Sumerian-arc texts from the Flood Story onward (including the
> Sumerian King List), the prose PRESERVES š and ĝ and anglicizes only ḫ→h (Kiš, Unug,
> Šuruppag), superseding the Enki-and-Ninmah š→sh practice described above."

In either case, **also activate SKL appliesTo** on this entry (see Diff 3).

### CENTRAL Diff 3 — batch `appliesTo` activation (all applied central entries)

Every central entry referenced in the draft's `glossaryRefs` is now applied to SKL
lines but its `appliesTo` does not yet list them (same pattern as the Atra-ḫasīs
report). **Rule for each id below: `appliesTo += [every SKL refId whose `glossaryRefs`
in `chapter-1.json` contains that id]`** (recoverable programmatically). WoH-salient and
small sets given in full; large convention sets given by count.

| central id | # SKL lines | full list? |
|---|---|---|
| `nam-lugal-an-ta-ed-de-a-ba-kingship-descended-from-heaven-cross-corpus` | 2 | `SKL-1`, `SKL-41` |
| `a-ma-ru-abubu-mabbul-great-flood-vocabulary-cross-corpus` | 2 | `SKL-39`, `SKL-40` |
| `dumuzi-tammuz-adonis-dying-and-rising-vegetation-god-cross-corpus` | 2 | `SKL-15`, `SKL-109` |
| `utu-shamash-sun-god-justice-divinity-cross-corpus` | 4 | `SKL-97`, `SKL-253`, `SKL-303`, `SKL-335` |
| `human-ascent-to-heaven-adapa-etana-enoch-elijah-cross-corpus` | 2 | `SKL-64`, `SKL-65` (= Diff 1) |
| `five-antediluvian-cities-eridug-bad-tibira-larag-zimbir-shuruppag-cross-corpus` | 14 | SKL-2, 3, 8, 9, 11, 18, 19, 20, 24, 25, 26, 30, 31, 32 |
| `dingir-prefix-prose-drop-convention` | 45 | by rule |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` | 127 | by rule |
| `manuscript-variant-inline-rendering-convention` | 130 | by rule |
| `sumerian-proper-name-transliteration-convention` | 233 | by rule |

---

## Unresolved editorial questions

**None.** All 15 Translator questions were folded into overlay entries or (SKL-42,
SKL-64) into the CENTRAL diffs above. The only items awaiting external action are the
CENTRAL diffs (orchestrator/Python) and the standing verification pass (below).

## Notes for the Reviewer

- **Sign-by-sign transliteration** was not re-collated; the ETCSL composite `translit`
  is trusted as the scholarly source. Sense-of-line follows ETCSL (Black, Cunningham,
  Robson, Zólyomi) with Jacobsen 1939 and Glassner 2004 as the editorial authorities.
- **Inferred entry to review:** `gilgamesh-phantom-father-lil-crux-skl` (SKL-113) — the
  retained "a phantom" is defensible (ETCSL) but the *lil₂* reading is a crux.
- **Scholarship cited in commentary** (all real): Jacobsen 1939; Glassner 2004;
  Michalowski 1983 (*JAOS* 103); Marchesi 2010; Steinkeller 2003; Hallo 1970;
  R. R. Wilson 1977; Burstein 1978 (Berossus); Kinnier Wilson 1985 and Foster
  (*Before the Muses*) on Etana; George 2003 on Gilgameš; Sarna and Cassuto on the
  Genesis 5 figures.
