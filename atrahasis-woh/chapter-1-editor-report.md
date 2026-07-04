# Chapter 1 Editor Report — Atra-ḫasīs, Tablet I

## Overview

The Wheel of Heaven program's **second Akkadian-source text** (after Adapa)
and its **single most on-thesis Mesopotamian composition**: humankind
fashioned from clay mixed with a slain god's flesh and blood, expressly to
bear the *dullu* (corvée-labor) of the gods. **111 lines / 9 segments**,
schema `composition/section/line`, refIds `ATRA-WOH-I:{line}`, Lambert–Millard
1969 numbering. A **MOAT TEXT** — no usable public-domain English
translation of Atra-ḫasīs exists, so the program renders its own from the
Akkadian.

The Translator submitted **9 editorial_questions[]**; this pass resolves
every one (folded into an overlay glossary entry, surfaced in commentary, or
recorded as a textual note) and clears the array. Because this is the
program's most lens-tempting text, **lens discipline was the governing
constraint** and is documented explicitly at §"Lens-routing decisions"
below.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.overlayGlossaryVersion`: `null` → `1.0.0`
- `translation.glossaryVersion`: `2.69.0` → **unchanged** (no central-glossary
  edits in this pass; the ~4 MB central file was neither loaded nor modified)

The source file's `verificationStatus` — *best-effort-reconstruction-pending-verification;
sign-by-sign transliteration pending collation against Lambert–Millard 1969
and eBL L.1.1* — is **preserved unchanged** in both `source-akk-1.json` and
`chapter-1.json`. The lens-discipline and glossary work operates on the
**sense-of-line** (well-attested across Lambert–Millard 1969, George &
Al-Rawi 1996, Foster 2005), which is independent of the sign-level
transliteration collation. A downstream collation-pass against Lambert–Millard
1969 and eBL L.1.1 is requested.

**No `i18n.en` line was modified in this pass.** All edits are to
`notes.official` (commentary), `glossaryRefs[]`, `translation` metadata, and
`editorial_questions[]`. The Translator's English was judged a defensible
scholarly rendering throughout; the Editor's job here was to make the
divergences and cruxes explicit in the apparatus, not to re-translate.

---

## Resolution of the 9 editorial questions

| # | refId(s) | Question | Resolution |
|---|---|---|---|
| 1 | I:192, 199 | *lullû* primeval human | **Resolved** → overlay `lullu-primeval-human-anthropogonic-keyword-atrahasis` (`direct`). Retained transliterated, glossed 'primeval human' on first occurrence. No text change (draft already retained it). |
| 2 | I:1 | *inūma ilū awīlum* frame syntax | **Resolved** → overlay `inuma-ilu-awilum-frame-crux-atrahasis` (`direct`). Lambert–Millard comparative 'like man' retained as baseline; the more lens-congenial Foster identity reading ('the gods **were** man') documented but **explicitly not adopted** — see lens-routing §. |
| 3 | I:217, 219, 227, 229 | *eṭemmu* ghost/spirit | **Resolved** → overlay `etemmu-ghost-spirit-divine-element-in-humankind-atrahasis` (`direct`). Retained, glossed 'spirit'; 'ghost' = Lambert–Millard baseline. **Flagged for future central promotion** (recurs across the Akkadian corpus + Hebrew *ruaḥ*/*nefeš* cross-corpus). |
| 4 | I:222, 238 | *Wê-ila* / *ṭēmu* + the double pun | **Resolved** → overlay `we-ila-temu-anthropogonic-pun-atrahasis` (`direct`). Name Wê-ila retained (variants noted); *ṭēmu* 'intelligence' retained; both puns (*Wê+ila→awīlu*, *ṭēmu→eṭemmu*) surfaced in commentary. |
| 5 | I:212–215, 224–225 | *ṭiddu/šīru/damu* triad | **Resolved** → overlay `siru-damu-tiddu-anthropogonic-triad-atrahasis` (`inferred`). Flesh/blood/clay rendered plainly; the triad flagged as a **CENTRAL-GLOSSARY candidate** (see §"Central-glossary action items"). |
| 6 | I:216, 226 | *uppu* 'drum'(?) | **Resolved** → overlay `uppu-drum-heartbeat-ghost-crux-atrahasis` (`direct`). 'Drum(?)' retained (L–M baseline, marked uncertain); Abusch heartbeat/ghost-token reading documented, not adjudicated. |
| 7 | I:37 | 40 / 3600 years number | **Resolved as a textual note** — left open '[ … ] years' (as the draft has it); both readings recorded in I:37 commentary. **No glossary entry** (textual/reading crux, not lexical). |
| 8 | I:242 | *urûtam* 'freedom'/'birth-stool' | **Resolved** → overlay `urutam-freedom-birth-stool-crux-atrahasis` (`direct`). 'Freedom(?)' retained on the parallelism argument; birth-stool alternative noted. |
| 9 | I:233 | *ruʾtu* 'spittle' | **Resolved** → overlay `rutu-spittle-igigi-clay-ratification-atrahasis` (`direct`). 'Spat upon the clay' kept plain; three interpretive readings of the act reserved for commentary. |

All 9 `editorial_questions[]` cleared to `[]`.

---

## Commentary added (`notes.official`)

12 lines received commentary, covering every meaningful divergence and crux;
plain narrative lines were left with empty commentary per the "empty where it
does not diverge" norm.

- **I:1** — the frame-crux (comparative vs identity), with the lens non-selection recorded.
- **I:2** — *dullu* / *šupšikku* thesis-vocabulary; ties to the central `du-lum-dullu-…` Akkadian-side activation.
- **I:37** — the 40 / 3600-years textual crux (with the *šār* great-cycle note).
- **I:192** — *lullû* first occurrence.
- **I:195** — *awīlum lišši dulli ilī*, the anthropogony thesis-line; Gen 1:26–27 *ṣelem/dĕmût* labor-vs-image contrast (cited, hedged).
- **I:212** — the *šīru/damu/ṭiṭṭu* triad; Gen 2:7 *ʿāfār*/breath parallel **and** the theomachic-blood divergence (cited, hedged).
- **I:216** — *uppu* crux.
- **I:217** — *eṭemmu* first occurrence.
- **I:222** — the Wê-ila / *ṭēmu* double pun — the anthropogonic heart.
- **I:233** — *ruʾtu* spittle interpretive note.
- **I:242** — *urûtam* crux.
- **I:260** — the fourteen pieces / seven-and-seven primal pairs.

Every commentary note names the Akkadian form, the standard rendering, the
WoH choice, and at least one scholarly basis (Lambert–Millard 1969; Foster
2005; Kilmer 1972; Moran 1970; Abusch 1998; Batto 1992; Clifford 1994;
Middleton 2005; CAD / AHw). None argues the WoH cosmology.

---

## ⚠ Lens-routing decisions (the critical call for this text)

The **"created from clay + a slain god's blood, to serve the gods"** reading
is **in the Akkadian** and is rendered plainly — the text is allowed to speak
for itself, with no softening. What is held out of the translation and
apparatus is the **Elohim / ancient-astronaut identification** (the gods as
an advanced civilization engineering a labor-force). Confirmations:

1. **Nothing lens-y touches any `i18n.en` line.** No `i18n.en` was modified;
   the surface English reads as a defensible scholarly rendering in the
   Lambert–Millard / Foster register.
2. **Nothing lens-y touches any `notes.official`.** Commentary is confined to
   philology (named forms, standard renderings, WoH choices, scholarly basis)
   and cited/hedged cross-corpus comparison (Gen 2:7 *ʿāfār*/breath; the
   Gen 1:26–27 *ṣelem/dĕmût* labor-vs-image contrast). No commentary asserts
   the Elohim frame or "what the text really means."
3. **The frame-crux non-selection is recorded.** At I:1, the identity reading
   ("the gods **were** man" — a mundane laboring population, the more
   lens-congenial rendering) was **declined** in favor of the Lambert–Millard
   comparative baseline, precisely because accuracy-above-lens forbids
   choosing a reading because it flatters the lens. Documented in
   `inuma-ilu-awilum-frame-crux-atrahasis`.
4. **Two further lens-temptations declined in-text**, recorded in glossary
   rationales: *ṭēmu* rendered "intelligence/reason" (not "engineered/downloaded
   cognition"); *ruʾtu* kept as "spat" (not "animating agent").
5. **The Elohim-frame reading is escalated as `speculative` and routed to
   the Explainer**, not the translation — see next §.

---

## Speculative entries requiring sign-off

### `atrahasis-labor-force-anthropogony-elohim-frame` (PROPOSED — NOT committed)

**Source:** the anthropogonic core as a whole (I:189–276) — humankind
fashioned from *ṭiṭṭu* (clay) mixed with the *šīru* (flesh) and *damu*
(blood) of the slain god Wê-ila, expressly to bear the *dullu* (labor) the
gods refuse.

**WoH reading under consideration:** identify the Atra-ḫasīs gods with the
Wheel of Heaven **Elohim** — an advanced civilization that engineered a
biological labor-force ("made from the ground to bear the labor"), reading
the clay-plus-god's-blood anthropogony as a compressed memory of
laboratory/genetic creation and the *dullu*-transfer as a workforce
substitution.

**Why speculative:** The *lexical and narrative* facts are direct and are
already carried plainly in the translation and commentary (humankind is made
from clay + a god's flesh and blood; it is made to bear the gods' labor; this
is uncontested Assyriology). What crosses into `speculative` is the
*interpretive identification* of these gods as the Elohim-as-advanced-civilization
and of the anthropogony as engineered biotechnology — an interpretive
synthesis that goes beyond what the Akkadian attests and that no single
source states. It is exactly the Sitchin-adjacent move the program's
accuracy-above-lens discipline holds out of the source apparatus.

**Recommendation:** **Do NOT commit** this as a glossary entry and **do NOT**
surface it in any `i18n.en` line or `notes.official`. **Route it to the
in-progress Explainer `made-from-the-ground-to-bear-the-labor`** (and/or the
relevant wiki entries), where framework/speculative claims belong and can be
argued with the full comparative apparatus. The translation's job is to
deliver the clay-and-blood-to-serve reading cleanly; the Explainer's job is
to read it through the lens. This is the single decision in the pass that is a
WoH-lens call rather than a philological one, and it is escalated here as the
project's accountability surface.

**Human reviewer action:** confirm by name that this reading stays in the
Explainer and out of the translation/glossary. No committed speculative entry
blocks the advance to `editor-review`; this proposed entry is recorded, not
shipped.

---

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**No in-agent edits.** Hard-rule compliance: the ~4 MB central glossary was
neither loaded nor modified. The following are **deferred to the separate
central-glossary (Python) step** and do not block this pass:

**A. New central entry to CREATE — the anthropogonic triad (from Q5):**

- **`siru-damu-tiddu-...` → promote to a central `*bāśār/dām/ʿāfār-ḥōmer* creation-vocabulary triad` entry.**
  Wire Akkadian *šīru* (flesh) / *damu* (blood) / *ṭiṭṭu* (clay) ↔ Hebrew
  *bāśār* / *dām* / *ʿāfār*–*ḥōmer* → Genesis 2:7 (dust + breath) and the
  Gen 1:26–27 *ṣelem/dĕmût* labor-vs-image contrast. claim_type `inferred`
  (named-scholarship comparative reading: Kilmer 1972; Moran 1970; Batto
  1992; Clifford 1994; Middleton 2005). The overlay entry
  `siru-damu-tiddu-anthropogonic-triad-atrahasis` holds the proposal; the
  central promotion is the Python step's job. The existing central
  `im-sumerian-clay-of-human-creation-cross-corpus` already covers the clay
  member and should be cross-referenced, not duplicated.

**B. Akkadian-side `appliesTo` activation on existing central entries**
(Atra-ḫasīs supplies the refIds; extend each central entry's `appliesTo`):

- `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus` — **Atra-ḫasīs is the principal Akkadian activation locus** (explicitly deferred here at Adapa). Add I:2, 3, 4, 6, 37, 195, 239 (+ the *dullu*/*tupšikku* attestations).
- `im-sumerian-clay-of-human-creation-cross-corpus` — add I:205, 213, 215, 225, 230, 233, 256, 260 (the *ṭiṭṭu* attestations).
- `anunnaki-igigi-mesopotamian-divine-classes-...` — add I:5, 6, 221, 231, 232.
- `zub-sig-dusu-corvee-basket-cross-corpus` — add I:2, 3, 67, 240.
- `nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-...` — add the Nintu / Bēlet-ilī / Mami / šassūru attestations (I:191–200, 213, 225, 234, 251–271).
- `digir-sumerian-divine-lexeme-cross-corpus` and `dingir-prefix-prose-drop-convention` — add the (d)PN and *ilu* attestations already referenced in the draft glossaryRefs.
- `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` — add the bracketed lines (I:2, 3, 14, 24, 37, 95, 226).

All of the above are **already referenced by id** in the draft's per-line
`glossaryRefs[]`; only the central `appliesTo` back-population remains, and it
is a Python-step task.

### Per-translation overlay (`data-library/atrahasis-woh/_translation-glossary.json`) — new file, v1.0.0

**Added (10 entries):**

1. `title-and-meta-conventions-atrahasis` (`direct`) — chapter-title convention.
2. `verification-pending-disclosure-atrahasis-akkadian` (`direct`) — moat-text verification-pending disclosure.
3. `lullu-primeval-human-anthropogonic-keyword-atrahasis` (`direct`) — Q1.
4. `inuma-ilu-awilum-frame-crux-atrahasis` (`direct`) — Q2; carries the lens non-selection record.
5. `etemmu-ghost-spirit-divine-element-in-humankind-atrahasis` (`direct`) — Q3; **future central-promotion candidate.**
6. `we-ila-temu-anthropogonic-pun-atrahasis` (`direct`) — Q4; the double pun.
7. `siru-damu-tiddu-anthropogonic-triad-atrahasis` (`inferred`) — Q5; **CENTRAL-GLOSSARY candidate.**
8. `uppu-drum-heartbeat-ghost-crux-atrahasis` (`direct`) — Q6.
9. `urutam-freedom-birth-stool-crux-atrahasis` (`direct`) — Q8.
10. `rutu-spittle-igigi-clay-ratification-atrahasis` (`direct`) — Q9.

Claim-type distribution: **9 `direct`, 1 `inferred`, 0 committed
`speculative`.** (The one speculative item — the Elohim-frame identification —
is escalated above as PROPOSED-NOT-committed and routed to the Explainer.)

---

## Unresolved editorial questions

**None.** All 9 are resolved; `editorial_questions[]` is `[]`.

---

## Verification-pending status

Preserved unchanged. Lines carrying the most transliteration-reconstruction
risk (bracketed restorations / damaged spans), flagged for the collation-pass
against Lambert–Millard 1969 and eBL L.1.1:

- **I:37** — `[X ME] ša-na-tim` — the years-number is damaged (40 vs 3600); traces do not settle it.
- **I:14** — `[(d)en-líl]` — restored subject after Lambert–Millard.
- **I:24** — `[i-na]` — bracketed restoration.
- **I:95, I:226** — bracketed restorations.
- **Editorial-selection gaps** — the draft curates I:1–71 and I:189–276; intervening spans (I:17–20, 26–36, 72–169, 170–188) are not reconstructed and are marked with editorial-selection gap notes, not lacunae.

The sense-of-line for every rendered line is well-attested across the cited
editions; the lens-discipline and glossary work is independent of the
sign-level collation. Both pipelines should converge at the Reviewer pass.

---

## Items for the human reviewer

1. **Confirm the speculative routing (required).** Confirm by name that
   `atrahasis-labor-force-anthropogony-elohim-frame` stays in the Explainer
   `made-from-the-ground-to-bear-the-labor` and is **not** committed to the
   glossary or surfaced in the translation. This is the pass's one WoH-lens
   call.
2. **Ratify the frame-crux baseline (I:1).** Confirm the Lambert–Millard
   comparative 'like man' as the shipped reading, with the Foster identity
   reading documented-not-adopted. (The Editor declined the lens-congenial
   option deliberately.)
3. **Approve the central-glossary action items** (§"Central glossary" A + B)
   for the separate Python step: create the *šīru/damu/ṭiṭṭu* ↔
   *bāśār/dām/ʿāfār-ḥōmer* triad entry, and back-populate Akkadian-side
   `appliesTo` on the eight existing central entries (esp. `du-lum-dullu-…`,
   for which Atra-ḫasīs is the principal Akkadian locus).
4. **Note the `eṭemmu` future-promotion flag** — not blocking; promote when a
   further Akkadian text (Gilgamesh XII, Descent of Ištar) supplies additional
   attestations.
5. **Verification-pass** — schedule sign-level collation against
   Lambert–Millard 1969 and eBL L.1.1; `verificationStatus` remains
   pending-verification until then.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible
scholarly rendering in the Lambert–Millard / Foster register; the "clay + a
god's blood, to bear the gods' labor" reading is delivered plainly because it
is in the Akkadian. The Elohim-frame lens is held entirely out of the
translation and apparatus and escalated to the Explainer as the accountability
surface. Every overlay entry has all required fields, correct claim_type, and
CAD/AHw + named-scholarship grounding a serious Assyriologist would recognize.
The one committed cross-corpus reading (the *šīru/damu/ṭiṭṭu* triad, `inferred`)
is named-scholarship comparative work; the one speculative reading is proposed,
not shipped. **Zero committed `claim_type=speculative` entries; standard human
Reviewer sign-off applies, plus the explicit speculative-routing confirmation
in item 1.**
