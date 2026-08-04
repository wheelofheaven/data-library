# Sign-off package — Theogony (theogony-woh), chapter 1, Block B

**Scope:** Block B — lines 211–452 (Nyx's brood; Pontos line and monster catalogue; Nereid,
Okeanid and river catalogues; Helios/Selene/Eos; the Styx oath; the Hekate hymn). Extends the
signed-off Block A (1–210 @1.0.0). Blocks C (453–735) and D (736–1022 + 929a–t) pending.

**Status at hand-off:** `awaiting-human` → **signed off** by zarazinsfuss (standing sign-off,
2026-08-04); promoted to `stable` / **1.1.0** at 2026-08-04T08:55:55Z.
**Central glossary:** v2.73.0 — **unchanged** (second consecutive block with zero central diffs)
**Overlay glossary:** v1.1.0 (26 entries; +15 new in Block B, 5 appliesTo extensions)

## Summary

| Metric | Value |
|---|---|
| Lines appended | 242 (211–452); chapter now 452 of 1042 |
| Block B lines with official commentary | 34 |
| Block B glossary refs | 101 (all resolving; none dangling) |
| Surface divergences from Evelyn-White | 1 deliberate refinement (THEO-304 'among the Arimoi') + systematic Greek name-forms per Block A convention |
| Editorial questions resolved | 14 of 14 |
| Overlay total after Block B | 26 (direct: 23, inferred: 3) |
| Reviewer verse verdicts | 38 (approve: 37, flag-for-human: 1) |
| Reviewer glossary verdicts | 20 (approve: 19, flag-for-human: 1) |
| Lens-leakage flags | 0 |
| Speculative entries | 0 |

## The one flag-for-human, and how it was resolved

**THEO-338 / `river-catalogue-greek-forms-theogony` — river exonyms.** The catalogue renders
river names in Greek transliteration (Neilos, Istros, Maiandros, Skamandros) per the signed-off
Block A name convention, against Evelyn-White's entrenched English exonyms (Nile, Danube,
Maeander, Scamander). Both Editor and Reviewer judged the Greek forms philologically sound and
internally consistent; the Reviewer recommended keeping them, at most allowing a two-name
exception (Neilos→"Nile", Istros→"Danube") for reader familiarity. **Shipped as recommended
(full Greek forms, no exceptions)** under the user's standing sign-off. This is a presentation
convention, not an accuracy question — it can be flipped later by editing the catalogue lines
(337–345) and the overlay entry, with a patch version bump.

## Orchestrator actions after review

1. THEO-358 `notes.official`: opening form corrected to unaccented *Κροκοπεπλος* (matching the
   source and the overlay entry), resolving the Reviewer's one cosmetic imprecision.
2. Promotion to stable/1.1.0; `_meta.json` → 452 lines, revision 2.

## Items noted for the future

1. **Block C (lines 453–735)** — Rhea/Kronos succession, Zeus's birth and the stone, the
   Iapetids and Prometheus (incl. Mekone and Pandora), the Titanomachy. Translator launched
   on sign-off.
2. The optional central `monogenes` cross-corpus template sits in the Block B editor report
   (not created; Editor and Reviewer both recommend against unless the project wants the
   Johannine reception cross-referenced centrally).

---

# Editor escalation report (inlined)

# Chapter 1 (Block B, lines 211–452) Editor Report — Theogony (theogony-woh)

**Scope:** Nyx's and Eris's brood (211–232); the Pontos line and Nereus (233–239);
the Nereid catalogue (240–264); the Phorkys/Keto monster-catalogue — Graiai, Gorgons,
Medusa, Pegasos/Chrysaor, Geryones, Echidna, Typhaon's brood, Chimaira, Sphinx (265–336);
the River catalogue (337–345); the Okeanid catalogue (346–370); Helios/Selene/Eos and the
winds (371–382); the Styx episode and oath (383–403); Phoibe/Leto/Asteria (404–410); and the
Hekate hymn (411–452).
**Source:** Hesiod, *Theogony*, Perseus `tlg0020.tlg001.perseus-grc2` (Evelyn-White 1914 underlying text).
**Status advanced:** `draft` → `editor-review`. **Version:** `1.1.0-draft` → `1.1.0-rc1`.
**Scope field:** B entry `draft` → `editor-review`.
**Overlay glossary:** `_translation-glossary.json` v1.0.0 → **v1.1.0** — 15 entries added
(14 `direct`, 1 `inferred`, 0 `speculative`); 5 existing entries had `appliesTo` extended into Block B.
**Central glossary:** not modified. Findings and a standing recommendation-against-change are filed below.

The governing rule was again **accuracy-before-lens**. All fourteen Block-B editorial
questions were resolved; every one adopted the accuracy-first default (Evelyn-White, or the
Block A conventions applied forward), with the Wheel-of-Heaven reading — where one exists —
confined to clearly-marked lens-discipline notes in the glossary rationales. **No English
surface line was changed against the Translator's draft**: the draft had already applied the
resolved defaults, so the Editor's work is carried entirely in `glossaryRefs`, per-line
`notes.official` (34 lines), and the overlay.

---

## Decisions per editorial question (14 of 14 resolved)

- **THEO-211 — Nyx/Eris personified abstractions.** Accepted Evelyn-White (option 1):
  translate the transparent meanings (Doom, Death, Sleep, Toil, Famine, Oath…), transliterate
  only the name-like/cult members (Klotho, Lachesis, Atropos; Nemesis; Zelos, Nike, Kratos, Bia,
  384–385). New overlay `personified-abstractions-nyx-eris-brood-theogony` (**direct**); note on 211.
- **THEO-240 — Nereid speaking-names.** Accepted Evelyn-White (option 1): transliterate as
  proper names, senses not glossed; the thematically-pointed Nemertes (262 ~ Nereus 235) flagged
  in commentary. New overlay `catalogue-speaking-names-transliteration-theogony` (**direct**);
  notes on 240, 262. Governs the Okeanid catalogue too (349, 361).
- **THEO-270 — Graiai.** Accepted transliteration 'Graiai' (Greek form, not Latin 'Graeae');
  *poliai* 'grey from birth' rendered literally, the *Graiai*~'grey' folk-etymology left in the
  Greek (as with the Titans). New overlay `graiai-grey-ones-folk-etymology-theogony` (**direct**);
  note on 270.
- **THEO-282 — Pegasos/Chrysaor folk-etymologies.** Accepted option 1 (render literally, pun in
  the Greek). Pegasos ~ *pēgai* 'springs' (282); Chrysaor ~ *aōr* 'blade' (283). New overlay
  `pegasos-chrysaor-folk-etymology-theogony` (**direct**); notes on 281, 282, 283. Also records the
  source misspelling *Χρυσαωρ* (missing accent, 281) kept verbatim.
- **THEO-299 — ophis/drakon vocabulary.** Accepted Evelyn-White (option 1): *ophis* 'serpent',
  *drakōn* 'dragon' by context, no fixed distinction; *nymphē* 'nymph'; antecedent at 295 = Keto in
  sense, crux noted. New overlay `ophis-drakon-serpent-vocabulary-theogony` (**direct**); note on 299,
  295.
- **THEO-304 — ein Arimoisin.** Accepted 'among the Arimoi' (people-reading of the dative plural) —
  a small refinement away from Evelyn-White's place-leaning 'in the land of the Arimi'. New overlay
  `ein-arimoisin-crux-theogony` (**inferred** — the block's only inferred entry); note on 304.
- **THEO-319 — Chimaira boundary.** Accepted Evelyn-White (option 1): 'Chimaira' the monster
  (Greek form), 'she-goat' the common noun of the middle head (322–323), like the gaia/ouranos
  boundary. New overlay `chimaira-shegoat-personification-boundary-theogony` (**direct**); note on 319.
- **THEO-326 — Phix/Sphinx + pronoun.** Kept the panhellenic Greek 'Sphinx' (Σφίγξ — a Greek form,
  not a Latinization) in the surface, the Boeotian *Φῖκʼ* preserved verbatim in the source and
  documented; pronoun 'she' left ambiguous (Chimaira per E-W / Echidna resumed per West). New overlay
  `phix-sphinx-boeotian-form-theogony` (**direct**); note on 326.
- **THEO-338 — river exonyms.** Accepted Greek transliteration throughout (Neilos, Istros,
  Maiandros, Skamandros), per the name convention; E-W Latinized forms declined. *Γρήνικόν*→'Granikos'
  normalization noted. New overlay `river-catalogue-greek-forms-theogony` (**direct**); notes on 338, 342.
  *(Reviewer option — see below.)*
- **THEO-400 — Styx megas horkos.** Accepted 'the great oath of the gods' (E-W): *horkos* = the
  oath-object sworn *by* (Styx as oath-witness), distinct from personified *Horkos* (231–232); not
  capitalized. New overlay `horkos-styx-great-oath-theogony` (**direct**); notes on 231, 400.
- **THEO-411 — mounogenēs of Hekate.** Accepted 'only child' (E-W); the Johannine 'only-begotten'
  **declined** for the surface and recorded as reception apparatus only. New overlay
  `mounogenes-only-child-hekate-theogony` (**direct**); notes on 411, 426, 448.
- **THEO-414 — honour-vocabulary.** Accepted option 1, tightened: a consistent English mapping —
  *timē* 'honour', *geras* 'prerogative', *moira* 'share', *aisa* 'allotted part', *dasmos* 'division',
  *olbos* 'wealth' — regularizing Evelyn-White. New overlay `time-geras-moira-honor-vocabulary-theogony`
  (**direct**); note on 393.
- **THEO-450 — kourotrophos.** Accepted 'nurse of the young' (E-W); cult-title translated not
  transliterated; linked to the river-daughters' *kourizousi* (347). New overlay
  `kourotrophos-nurse-of-the-young-theogony` (**direct**); notes on 347, 450, 452.
- **THEO-358 — Krokopeplos.** Accepted epithet reading (E-W): *krokopeplos* 'saffron-robed' of
  Telesto (as of Enyo at 273), not a 42nd Okeanid name; the source capitalization not decisive. New
  overlay `krokopeplos-saffron-robed-epithet-theogony` (**direct**); note on 358.

**Additional text-critical item (not one of the 14, flagged by the task):** West's transposed
line order (214↔213, 427↔426, 434↔430) is preserved deliberately, so the `n`/refId sequence is
non-ascending at those points. Recorded in a new overlay convention
`west-transposed-line-order-theogony` (**direct**) and in notes on 214, 427, 434.

---

## Overlay changes for review (`_translation-glossary.json`, v1.0.0 → v1.1.0)

### Added (15 entries; 14 `direct`, 1 `inferred`)

- `personified-abstractions-nyx-eris-brood-theogony` (direct) — 211/212/214/217/218/223/224/225/226/227/228/229/230/231/384/385
- `catalogue-speaking-names-transliteration-theogony` (direct) — 240/243/262/349/361
- `graiai-grey-ones-folk-etymology-theogony` (direct) — 270/271/272
- `pegasos-chrysaor-folk-etymology-theogony` (direct) — 281/282/283/287
- `ophis-drakon-serpent-vocabulary-theogony` (direct) — 295/298/299/305/322/323/334
- `ein-arimoisin-crux-theogony` (**inferred**) — 304
- `chimaira-shegoat-personification-boundary-theogony` (direct) — 319/322/323
- `phix-sphinx-boeotian-form-theogony` (direct) — 326
- `river-catalogue-greek-forms-theogony` (direct) — 337/338/339/342/345
- `horkos-styx-great-oath-theogony` (direct) — 400
- `mounogenes-only-child-hekate-theogony` (direct) — 426/448
- `time-geras-moira-honor-vocabulary-theogony` (direct) — 393/394/395/396/413/414/415/418/420/422/425/427/449
- `kourotrophos-nurse-of-the-young-theogony` (direct) — 347/450/452
- `krokopeplos-saffron-robed-epithet-theogony` (direct) — 273/358
- `west-transposed-line-order-theogony` (direct) — 213/214/426/427/430/434

### `appliesTo` extended into Block B (5 existing entries; semver-minor, no field changed but `appliesTo`)

- `ouranos-gaia-cosmogony-personification-boundary-theogony` — + 238/300/335/346/365/373/382/413/414/421/427
- `kratos-phertatos-sovereignty-vocabulary-theogony` — + 385/403
- `titanes-folk-etymology-theogony` — + 392/424
- `athetized-lines-convention-theogony` — + 323/324
- `theogony-name-and-title-conventions` — + 233/411 (Block B anchors)

No existing entry's `id`, `wohChoice`, `rationale`, or `claim_type` was altered; only `appliesTo`
grew. Version bumped semver-minor (additions + appliesTo extensions), per the task's instruction.

---

## CENTRAL — apply by orchestrator

**No central change is requested.** Two Block-B sites have cross-corpus pull; both were checked
against the production glossary and both are resolved in the overlay, following the Block A
*gigantes* discipline (record the reception/lexeme link as apparatus; do not fuse referents).

### 1. `mounogenēs` (THEO-411 / 426, 448) — Johannine 'only-begotten'

**Central query result.** The only central touchpoint for `monogenes`/`only-begotten` is the
Hebrew entry **`yechid-only-one-formula`** (Gen 22:2/12/16), which *already* flags the downstream
Vulgate *unigenitum* / Johannine *monogenēs* (John 3:16) reception **within its own Hebrew domain**.
There is **no** central Greek or Johannine `monogenes` entry (the corpus has no Gospel-of-John
source text). `oath`/`horkos`: 44 central hits, all Hebrew-Bible oath entries (covenant-cutting,
divine self-oath `bi-nishbati-divine-self-oath`, oath-gesture `yad-tachat-yarekh-oath-gesture`);
no Greek `horkos`/Styx entry. `underworld`/Styx: `sheol-underworld-realm-of-the-dead` and cognates,
all Hebrew/Ugaritic/Sumerian; no Styx entry.

**Editor adjudication: do NOT extend `yechid-only-one-formula` (or any central entry) to a THEO
refId.** Hesiod's *μουνογενής* of Hekate and the Hebrew *yachid* of Isaac are different lexemes in
different corpora; their only shared point is the *later* Johannine *monogenēs*, which is reception,
not identity. Appending a THEO refId to the Hebrew entry would assert cross-governance the texts do
not support. The reception link is preserved as comparative apparatus in the overlay entry
`mounogenes-only-child-hekate-theogony` (which names `yechid-only-one-formula` in its rationale) and
in the line-426 commentary.

**Optional (only if the reviewer wants the reception cross-referenced centrally):** the Editor's
preference, mirroring the Block A `gigantes-septuagint-lexeme-cross-corpus` template, is a **new,
separate** central reception-note rather than extending the Hebrew entry — e.g.:

```json
{
  "id": "monogenes-only-begotten-reception-lexeme-cross-corpus",
  "source": "μουνογενής / μονογενής (Hesiod, Theogony 426, 448; John 1:14, 3:16); cf. יְחִיד (Gen 22) rendered ἀγαπητός/unigenitus",
  "translit": "monogenes",
  "strongs": "LSJ s.v. μονογενής; John 1:14/3:16; Vulgate unigenitus; cf. central `yechid-only-one-formula`",
  "partOfSpeech": "Greek adjective — the shared 'only-born' lexeme across the Greek reception",
  "literal": "single-born, only-born (mono- + gen-)",
  "standardEnglish": "only child (Hesiod); only-begotten (Johannine reception)",
  "wohChoice": "document μονογενής as a lexeme with distinct senses across corpora — 'only child' (Hesiod, Theogony) vs the theological 'only-begotten' (Johannine) — NOT an identity of referents or a single doctrine",
  "claim_type": "inferred",
  "rationale": "The adjective μονογενής ('single-born, only-born') is used by Hesiod of Hekate, the only child of a single mother (Theog. 426, 448), and later of Christ in the Johannine writings (John 1:14, 3:16), where the Vulgate renders unigenitus 'only-begotten'; the Christian reception also reads the Hebrew yachid of Gen 22 through this lexeme (LXX ἀγαπητός, Vulgate unigenitus). The entry records the shared reception-lexeme only; the Hesiodic 'only child' and the Johannine 'only-begotten' are different senses in different corpora, and the Editor recommends it NOT be created unless the reviewer wants the cross-reference.",
  "appliesTo": ["THEO-426", "THEO-448"]
}
```

If created, bump central `version` semver-minor. **Standing recommendation: leave central
untouched.**

### 2. `horkos` / Styx-oath (THEO-400)

Text-specific Greek oath-by-underworld-river; no appropriate central oath entry (the central oath
cluster is Hebrew self-oath / covenant-cutting / oath-gesture — a different phenomenon). Kept in the
overlay per the "when in doubt, overlay" rule. **No central change.**

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry was created in Block B. Every WoH-salient site was
resolved accuracy-first:

- **The Styx oath (383–403).** *horkos* rendered 'oath' (the oath-witness), kept distinct from
  personified Horkos; commentary held to the philological level. Zeus's institution of a binding
  cosmic sanction is *described*, not allegorized. Lens-discipline note in the glossary rationale.
- **`mounogenēs` (426, 448).** 'only child' in the surface; the Johannine 'only-begotten' resonance
  is apparatus-only and explicitly *not* imported into the line.
- **The Hekate honour-lexicon (411–452).** *timē/geras/moira/aisa/dasmos* rendered as a plain
  apportioned-honour vocabulary; the "sovereign distributing offices/domains" reading is named as a
  temptation in the lens-discipline note and pressed nowhere in surface or commentary.
- **`kourotrophos` (450).** 'nurse of the young' as a cult-title; the "rearer/cultivator of
  humanity" motif is not pressed beyond what the title states.

Status is therefore free to advance to `editor-review` with no speculative blocker.

---

## Notes for the Reviewer

- **Surface diff:** **zero** English-surface changes against the Translator's draft. The draft had
  already applied every resolved default; the Editor's contribution is 67 lines newly tagged with
  `glossaryRefs`, 34 lines of new `notes.official`, and the overlay. (Block A, by contrast, had one
  surface change at 27.)
- **THEO-338 rivers — a live reviewer choice.** The block uses **Greek transliteration throughout**
  (Neilos, Istros, Maiandros, Skamandros), consistent with the name convention and with 'Ouranos not
  Uranus'. The alternative (option 2: entrenched English exonyms Nile/Danube/Maeander/Scamander for
  the familiar few, Greek forms for the rest) is a reader-familiarity trade-off, not an accuracy
  issue; if the reviewer prefers it, the change is confined to 338–345 and the overlay entry
  `river-catalogue-greek-forms-theogony`.
- **THEO-326 antecedent** and **THEO-299 antecedent (Echidna's mother, 295)** are genuine grammatical
  cruxes; both were left ambiguous in the English on purpose ('she'), following the Greek. If the
  reviewer wants a committed genealogy, that is a surface decision to make explicitly.
- **Source-orthography preserved verbatim** (per instruction, not corrected in the `text` field):
  *Χρυσαωρ* missing its final accent at 281 (correct *Χρυσάωρ* at 287); *Γρήνικόν* with eta at 342
  (standard 'Granikos' given only in the English). Both are documented in commentary.
- **West transpositions** (214↔213, 427↔426, 434↔430) mean `n` is deliberately non-ascending at three
  points; the transmitted athetized lines **323–324** are retained-and-translated with the athetesis
  in commentary, per the Block A convention.
- **Greek in the notes was hand-set.** As in Block A, a light proofreading pass over the Greek forms
  in the new commentary and overlay rationales is advisable at Reviewer stage. (Three transliteration/
  accent slips were caught and corrected pre-write; a fourth check is prudent.)
- **Forward-scoped entries.** The catalogue-speaking-name convention, the honour-vocabulary, the
  serpent vocabulary, and the West-transposition convention are all likely to recur in Blocks C–D and
  should carry forward.


---

# Reviewer report (inlined)

**Reviewer:** claude-opus-4-8[1m] acting as woh-reviewer
**Reviewed at:** 2026-08-04T08:50:18Z
**Lens-leakage flags:** 0

## Verse verdicts (38)

**THEO-211** — `approve`
: Re-parsed νὺξ δʼ ἔτεκεν στυγερόν τε Μόρον καὶ Κῆρα μέλαιναν: rendering the transparent abstractions (Doom, Fate) while transliterating only the name-like members is Evelyn-White's own distribution and standard for the catalogue; the boundary is the reference edition's, not a lens choice.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 211-232; LSJ s.vv. Μόρος, Κήρ

**THEO-214** — `approve`
: Verified the source list itself stores 214 before 213; the non-ascending refId is faithful reproduction of West's/Perseus's transposition, a text-critical datum correctly confined to the note, not a translation move.
: *Citations:* West 1966 (editorial line-order ad 213-214); Perseus tlg0020.tlg001.perseus-grc2

**THEO-217** — `approve`
: Μοίρας 'Destinies' / Κῆρας νηλεοποίνους 'ruthless-avenging Fates' follows Evelyn-White's distribution; the Moirai doublet with 904-906 is a known feature of the poem and is left as transmitted, correctly flagged in commentary.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 217; cf. 904-906

**THEO-231** — `approve`
: Ὅρκον as the last of Eris's children = the personified avenging Oath; keeping it distinct from the oath-by-Styx at 400 is the correct philological separation, and 'Oath' capitalized matches the personification convention.
: *Citations:* LSJ s.v. ὅρκος; West 1966 comm. ad 231-232

**THEO-233** — `approve`
: Πόντος kept personified (sea-god) per the name convention; the truth-epithets ἀψευδέα/ἀληθέα given plain senses, echoing the Muses' pseudea/alēthea field at 27-28 in commentary only. Lens-free and Evelyn-White-faithful.
: *Citations:* LSJ s.vv. ἀψευδής, ἀληθής, νημερτής; West 1966 comm. ad 233-236

**THEO-240** — `approve`
: Transliterating the fifty Nereid speaking-names as proper names rather than glossing each sense is standard practice and matches the reference; rendering the meanings would misrepresent a roll-call as a word-list.
: *Citations:* West 1966 comm. ad 240-264; Evelyn-White 1914

**THEO-262** — `approve`
: Νημερτής 'Unerring', last Nereid, reprises Nereus's own epithet νημερτής (235); the thematic point is correctly carried in the note while the surface keeps the plain transliterated name.
: *Citations:* West 1966 comm. ad 262; LSJ s.v. νημερτής

**THEO-270** — `approve`
: Γραίας transliterated as the Greek 'Graiai' (not Latin 'Graeae'), with πολιάς 'grey from birth' rendered literally so the Graiai~'grey/old-woman' folk-etymology stays audible only in the Greek — the same discipline used for the Titans at 207-210.
: *Citations:* Chantraine, DELG s.v. γραῦς; West 1966 comm. ad 270-271

**THEO-281** — `approve`
: Confirmed the source reads the unaccented Χρυσαωρ at 281 (vs. correct Χρυσάωρ at 287); the misspelling is preserved verbatim in the text field per source-immutability policy, with the standard 'Chrysaor' only in translit/translation. Correct handling.
: *Citations:* Perseus tlg0020.tlg001.perseus-grc2 (apparatus); West 1966 comm. ad 281

**THEO-282** — `approve`
: Pēgasos etymologized from the πηγαί 'springs' of Okeanos; the clause rendered literally, the name-play left in the Greek with no manufactured English pun. Consistent with the Titan/Graiai etymology treatment.
: *Citations:* LSJ s.v. πηγή; West 1966 comm. ad 282

**THEO-283** — `approve`
: Chrysaōr etymologized from the ἄορ χρύσειον 'golden blade'; clause rendered literally, name-play kept in the Greek. Lexical evidence (chrys- + aōr 'sword') is accurate.
: *Citations:* LSJ s.v. ἄορ; West 1966 comm. ad 283

**THEO-295** — `approve`
: The mother of Echidna is genuinely ambiguous (nearest antecedent Kalliroe 288; Keto supplied by the summarizing 336); the bare 'she' preserves the ambiguity while following the Keto sense — the crux is noted, not silently resolved.
: *Citations:* West 1966 comm. ad 295; Evelyn-White 1914

**THEO-299** — `approve`
: ὄφις 'serpent' and δράκων 'serpent/dragon' are largely synonymous in early epic; rendering by context without imposing a fixed technical distinction is correct, since the Greek marks none. νύμφη 'nymph' in its plain sense.
: *Citations:* LSJ s.vv. ὄφις, δράκων, νύμφη; West 1966 comm. ad 295-336

**THEO-304** — `approve`
: The block's single inferred surface reading: εἰν Ἀρίμοισιν as dative plural of a people ('among the Arimoi') is the more literal construal of an ancient crux and is adopted by modern translators (Athanassakis); the place-reading ('in Arima', Strabo 13.4.6) is correctly recorded and the referent left unglossed. Defensible; properly classed inferred.
: *Citations:* West 1966 comm. ad 304; Homer, Iliad 2.783; Strabo 13.4.6; Athanassakis 1983

**THEO-319** — `approve`
: Χίμαιρα the monster capitalized (Greek form, not 'Chimaera'), χίμαιρα 'she-goat' the common noun of the middle head (322-323) lower-case — the personified/common-noun boundary drawn exactly where Evelyn-White draws it, parallel to gaia/ouranos in Block A.
: *Citations:* LSJ s.v. χίμαιρα; West 1966 comm. ad 319-324; Chantraine, DELG s.v. χίμαρος

**THEO-323** — `approve`
: Verified 323-324 are the only athetized lines in range; retained-and-translated with the bracketing recorded in commentary per the signed-off Block A convention. No surface bracket, full received text preserved.
: *Citations:* West 1966 (athetesis ad 323-324); LSJ s.v. δράκων

**THEO-324** — `approve`
: Falls within the athetized 323-324; retained and translated per convention, athetesis noted. Consistent with 323.
: *Citations:* West 1966 (athetesis ad 323-324)

**THEO-326** — `approve`
: Source Φῖκʼ (Boeotian dialect form) preserved verbatim; surface gives the panhellenic Greek 'Sphinx' (Σφίγξ — a Greek form, not a Latinization), the reader-recognizable name. The mother-pronoun crux (Chimaira per E-W / Echidna per West) is left ambiguous as in the Greek.
: *Citations:* West 1966 comm. ad 326; Chantraine, DELG s.v. Σφίγξ

**THEO-338** — `flag-for-human`
: The river-catalogue renders Greek forms throughout (Neilos not 'Nile', Istros not 'Danube', Maiandros, Skamandros). Philologically this is sound, internally consistent with the signed-off name convention, and arguably less anachronistic (Greek Istros = the lower Danube, not the modern river). But applying the Greek-forms rule to globally-entrenched exonyms is a NEW convention extension and a reader-familiarity / project-stance call the Editor explicitly punted to review; per rule 7 this belongs to the human. Reviewer recommendation: KEEP the Greek forms for consistency; the only defensible alternative is a tiny exonym-exception list (Neilos->'Nile', Istros->'Danube') for the two most entrenched names.
: *Citations:* West 1966 comm. ad 337-345; Evelyn-White 1914 (Latinized Nilus/Ister/Maeander/Scamander); LSJ s.vv.

**THEO-342** — `approve`
: Confirmed the source reads Γρήνικόν (with eta) at 342; preserved verbatim in the text field, normalized to the standard river-name 'Granikos' only in the English, with the source form kept in translit. Correct source-immutability handling.
: *Citations:* Perseus tlg0020.tlg001.perseus-grc2 (apparatus); West 1966 comm. ad 342

**THEO-347** — `approve`
: ἄνδρας κουρίζουσι 'rear men to manhood' rendered with Evelyn-White; the kour- root correctly cross-linked in commentary to Hekate's kourotrophos (450). Lexical, lens-free.
: *Citations:* LSJ s.v. κουρίζω; West 1966 comm. ad 346-348

**THEO-349** — `approve`
: Okeanid speaking-names transliterated as proper names as in the Nereid catalogue; the presence of soon-major figures (Styx, Metis, Kalypso, Dione) is left to speak for itself without gloss. Correct and consistent.
: *Citations:* West 1966 comm. ad 346-366; Evelyn-White 1914

**THEO-358** — `approve`
: Κροκοπεπλος read as the epithet krokopeplos 'saffron-robed' of Telesto (as of Enyo at 273), not a 42nd Okeanid name, keeping the roll at 41 — the philologically economical reference reading; source capitalization/missing-accent correctly judged non-decisive. (Minor cosmetic: the line-358 note cites the form as accented 'Κροκόπεπλος' while noting the source drops the accent — see errata.)
: *Citations:* West 1966 comm. ad 358; LSJ s.v. κροκόπεπλος; Evelyn-White 1914

**THEO-361** — `approve`
: Στύξ 'most eminent of them all' (προφερεστάτη) kept as theonym, correctly read as the anticipatory flag of her singular role at 383-403. Faithful.
: *Citations:* West 1966 comm. ad 361; LSJ s.v. προφερής

**THEO-371** — `approve`
: Theia's luminary children kept as theonyms Helios/Selene/Eos (Greek forms, not Sol/Luna/Aurora, not the common nouns sun/moon/dawn), since here they are the shining powers born and acting. Consistent with the name convention.
: *Citations:* West 1966 comm. ad 371-374; LSJ s.vv. Ἥλιος, Σελήνη, Ἠώς

**THEO-393** — `approve`
: Zeus's accession-offer introduces the apportioned-honour lexicon; the consistent mapping (timē 'honour', geras 'prerogative', with privatives atimos/agerastos at 395) regularizes Evelyn-White and reads as one thematic thread. Lexical, not allegorical.
: *Citations:* LSJ s.vv. τιμή, γέρας, ἄτιμος, ἀγέραστος; West 1966 comm. ad 392-401

**THEO-400** — `approve`
: High-scrutiny site cleared: θεῶν μέγαν ... ὅρκον rendered 'the great oath of the gods' (lower case) = the oath-object/witness sworn BY, correctly distinct from personified Horkos (231-232). No covenant/cosmological lens pressed into the surface; commentary held to the philological level.
: *Citations:* LSJ s.v. ὅρκος II ('that by which one swears, witness of an oath'); West 1966 comm. ad 400, 775-806

**THEO-411** — `approve`
: The Hekate-hymn framing note (a share in earth/sea/starry heaven; Zeus confirms rather than strips the Titan-daughter's honours) is an accurate summary of the passage's much-discussed argument, kept descriptive. Cruxes correctly deferred to their lines.
: *Citations:* West 1966 comm. ad 411-452; Clay 2003 (Politics of Olympus); Boedeker 1983 on Hekate

**THEO-427** — `approve`
: Verified the source stores 427 before 426; the non-ascending refId reproduces West's transposition (427 completes the earth/heaven/sea tricolon before 426 resumes the mounogenēs thought). Text-critical, correctly noted.
: *Citations:* West 1966 (editorial line-order ad 426-427); Perseus tlg0020.tlg001.perseus-grc2

**THEO-426** — `approve`
: High-scrutiny site cleared: μουνογενής (Ionic for monogenēs) rendered 'only child' — the structural pivot of the hymn — with the Johannine 'only-begotten' correctly kept OUT of the surface and confined to reception apparatus. Lexical evidence (mono- + gen-) accurate.
: *Citations:* LSJ s.v. μονογενής; West 1966 comm. ad 426

**THEO-434** — `approve`
: Verified the source stores 434 after 429 (order 429,434,430-433); the transposition places the two civic-sphere clauses (434 kings in judgment; 430 assembly) consecutively. Faithfully reproduced, correctly noted.
: *Citations:* West 1966 (editorial line-order ad 430-434); Perseus tlg0020.tlg001.perseus-grc2

**THEO-448** — `approve`
: μουνογενὴς ἐκ μητρός 'only child from her mother' restates the hymn's thesis at its close; 'only child' kept, 'only-begotten' declined. Consistent with 426.
: *Citations:* LSJ s.v. μονογενής; West 1966 comm. ad 448

**THEO-450** — `approve`
: High-scrutiny site cleared: κουροτρόφον rendered 'nurse of the young' (cult-title translated, not transliterated), extended to all mortals born after Hekate; the kour- link to 347 noted. The 'rearer/cultivator of humanity' motif is not pressed beyond the cult-title. No lens.
: *Citations:* LSJ s.v. κουροτρόφος; West 1966 comm. ad 450-452; Chantraine, DELG s.v. κοῦρος

**THEO-452** — `approve`
: κουροτρόφος closes the hymn resuming 450; αἳ δέ τε τιμαί 'and these are her honours' rounds off the apportioned-honour theme. Faithful, lens-free.
: *Citations:* West 1966 comm. ad 452; LSJ s.v. κουροτρόφος

**THEO-264** — `approve`
: κοῦραι πεντήκοντα 'fifty maidens' confirms the Nereid count underlying the 240 note; rendering plain. Independently re-parsed though uncommented.
: *Citations:* West 1966 comm. ad 264; LSJ s.v. πεντήκοντα

**THEO-278** — `approve`
: Κυανοχαίτης rendered 'the Dark-haired One' — a transparent epithet (of Poseidon) translated rather than replaced by the theonym, matching Evelyn-White and the epithet-translation practice; no lens. Uncommented but re-parsed.
: *Citations:* LSJ s.v. κυανοχαίτης; Evelyn-White 1914

**THEO-381** — `approve`
: Ἑωσφόρον 'Eosphoros' (the star/dawn-bringer) and Ἠριγένεια 'Erigeneia' (early-born, of Eos) kept as Greek names; astra 'stars' plain. Consistent with the name convention. Uncommented but re-parsed.
: *Citations:* LSJ s.vv. Ἑωσφόρος, Ἠριγένεια; West 1966 comm. ad 381

**THEO-441** — `approve`
: Ἐννοσιγαίῳ rendered 'Earth-Shaker' — the transparent Poseidon title translated (as Κυανοχαίτης at 278), not transliterated 'Ennosigaios' nor replaced by 'Poseidon'; matches Evelyn-White. No lens. Uncommented but re-parsed.
: *Citations:* LSJ s.v. ἐννοσίγαιος; Evelyn-White 1914


## Glossary-entry verdicts (20)

**personified-abstractions-nyx-eris-brood-theogony** — `approve`
: claim_type=direct verified: translating the transparent abstractions and transliterating only the name-like/cult members (Moirai names, Nemesis, Zelos/Nike/Kratos/Bia) is Evelyn-White's own boundary, drawn line-by-line; the Block A cosmic-theonym transliteration is correctly NOT extended wholesale. No lens.
: *Citations:* Evelyn-White 1914; West 1966 comm. ad 211-232, 383-385; LSJ s.vv.

**catalogue-speaking-names-transliteration-theogony** — `approve`
: claim_type=direct verified: transliterating the transparent Nereid and Okeanid speaking-names as proper names, with thematically-pointed senses (Nemertes 262) carried in commentary only, is standard reference practice — a presentation convention with no interpretive content.
: *Citations:* West 1966 comm. ad 240-264, 346-366; Evelyn-White 1914

**graiai-grey-ones-folk-etymology-theogony** — `approve`
: claim_type=direct verified: 'Graiai' (Greek form, not Latin 'Graeae') with πολιάς 'grey from birth' literal; the folk-etymology (Graiai~graus/poliai) is Hesiod's own and left in the Greek. Lexical evidence accurate.
: *Citations:* Chantraine, DELG s.v. γραῦς/γέρων; West 1966 comm. ad 270-271; LSJ s.v. πολιός

**pegasos-chrysaor-folk-etymology-theogony** — `approve`
: claim_type=direct verified: Pēgasos~pēgai 'springs' (282) and Chrysaōr~aōr 'sword'+chrys- 'gold' (283) are accurate etymologies rendered as literal clauses; the source misspelling Χρυσαωρ (281) correctly preserved verbatim with standard form in translit/English.
: *Citations:* LSJ s.vv. πηγή, ἄορ; West 1966 comm. ad 281-283

**ophis-drakon-serpent-vocabulary-theogony** — `approve`
: claim_type=direct verified: ophis/drakōn are largely synonymous in early epic and LSJ reports no stable opposition; rendering by context without a manufactured technical distinction is correct. The Echidna-mother crux (295=Keto in sense) is honestly flagged.
: *Citations:* LSJ s.vv. ὄφις, δράκων, νύμφη; West 1966 comm. ad 295-336

**ein-arimoisin-crux-theogony** — `approve`
: claim_type=inferred verified and defended: the block's only inferred entry commits to the people-reading 'among the Arimoi' (the more literal dative-plural construal of a genuine ancient crux, adopted by modern translators), honestly records the place-reading (Strabo) and the divergence from Evelyn-White's place-leaning rendering, and leaves the unrecoverable referent unglossed. Correctly NOT direct; lexical grounding is real.
: *Citations:* West 1966 comm. ad 304; Homer, Iliad 2.783; Strabo 13.4.6; Athanassakis 1983

**chimaira-shegoat-personification-boundary-theogony** — `approve`
: claim_type=direct verified: 'Chimaira' the monster capitalized (Greek form), χίμαιρα 'she-goat' the common noun of the middle head lower-case — the boundary drawn where Evelyn-White draws it, parallel to the signed-off gaia/ouranos entry. No lens.
: *Citations:* LSJ s.v. χίμαιρα; West 1966 comm. ad 319-324; Chantraine, DELG s.v. χίμαρος

**phix-sphinx-boeotian-form-theogony** — `approve`
: claim_type=direct verified: 'Sphinx' (Σφίγξ) is the panhellenic GREEK form, not a Latinization, so surfacing it is consistent with the name convention while the Boeotian Φῖκʼ is preserved verbatim and documented. The mother-pronoun crux is correctly left ambiguous.
: *Citations:* West 1966 comm. ad 326; Chantraine, DELG s.v. Σφίγξ

**river-catalogue-greek-forms-theogony** — `flag-for-human`
: The claim_type=direct classification is philologically defensible and the rendering is internally consistent with the signed-off name convention (and less anachronistic than 'Danube' for Istros). BUT this is a NEW convention extension to globally-entrenched exonyms (Nile, Danube) with a real reader-familiarity cost, which the Editor explicitly nominated as a reviewer option; per rule 7 the audience/project-stance call belongs to the human. Reviewer recommendation: keep the Greek forms; at most permit a two-name exonym exception (Neilos->Nile, Istros->Danube). This is the block's status-driver to awaiting-human.
: *Citations:* West 1966 comm. ad 337-345; Evelyn-White 1914 (Latinized forms); LSJ s.vv.

**horkos-styx-great-oath-theogony** — `approve`
: claim_type=direct verified: horkos at 400 = the oath-object/witness sworn BY (LSJ s.v. II), rendered 'oath' lower-case and kept distinct from personified Horkos (231-232); the settled lexical value. The lens-discipline note correctly holds this high-salience site (a binding cosmic sanction) to philology only.
: *Citations:* LSJ s.v. ὅρκος II; West 1966 comm. ad 400, 775-806

**mounogenes-only-child-hekate-theogony** — `approve`
: claim_type=direct verified: 'only child' is the consensus rendering of μουνογενής in Hesiod; the Johannine 'only-begotten' is reception, correctly apparatus-only. I independently verified the central yechid-only-one-formula entry (claim_type=direct, appliesTo GEN-WOH-22:2/12/16) already carries the Vulgate/Johannine reception WITHIN its Hebrew domain — so the Editor's no-central-change call is sound: yachid and mounogenēs are unrelated lexemes converging only in later Christian reception, and cross-governance would assert an identity the texts do not support.
: *Citations:* LSJ s.v. μονογενής; West 1966 comm. ad 426, 448; John 1:14, 3:16; central yechid-only-one-formula (verified GEN-WOH-22 scope)

**time-geras-moira-honor-vocabulary-theogony** — `approve`
: claim_type=direct verified: the fixed English mapping of the apportioned-honour lexicon regularizes Evelyn-White as a lexical-consistency convention (parallel to the signed-off kratos-phertatos entry), not an interpretive move. The lens-discipline note correctly declines to allegorize the 'sovereign distributing offices' theme.
: *Citations:* LSJ s.vv. τιμή, γέρας, μοῖρα, αἶσα, δασμός, ὄλβος; West 1966 comm. ad 392-401, 411-452

**kourotrophos-nurse-of-the-young-theogony** — `approve`
: claim_type=direct verified: kourotrophos 'nurse/rearer of the young' is a widespread cult-title (Gaia, Hestia, Artemis, Hekate) translated not transliterated; the kour- link to 347 is real. High-salience site held to the lexical fact; no 'cultivator of humanity' overreach.
: *Citations:* LSJ s.v. κουροτρόφος; West 1966 comm. ad 450-452; Chantraine, DELG s.v. κοῦρος

**krokopeplos-saffron-robed-epithet-theogony** — `approve`
: claim_type=direct verified: reading Κροκοπεπλος as the epithet 'saffron-robed' of Telesto (as of Enyo 273), not a 42nd name, is the reference and philologically economical reading (keeps the roll at 41); source capitalization correctly judged non-decisive. Entry's source field quotes the source form unaccented correctly; only the separate line-358 note shows it accented (cosmetic, self-flagged).
: *Citations:* LSJ s.v. κροκόπεπλος; West 1966 comm. ad 358; Evelyn-White 1914

**west-transposed-line-order-theogony** — `approve`
: claim_type=direct verified: I confirmed the source list itself stores 214<213, 427<426, 434 after 429; preserving the edition's order (non-ascending refId) is a text-critical datum recorded in commentary, parallel to the athetized-lines convention. No interpretive content.
: *Citations:* West 1966 (editorial line-order); Perseus tlg0020.tlg001.perseus-grc2

**ouranos-gaia-cosmogony-personification-boundary-theogony** — `approve`
: appliesTo extension into Block B (238/300/335/346/365/373/382/413/414/421/427) verified: each new anchor uses gaia/ouranos as common noun ('earth'/'heaven') or personified consistently with the signed-off Block A boundary. No field other than appliesTo changed; claim_type=direct intact.
: *Citations:* West 1966 comm. ad 108, 116-128; LSJ s.vv. γαῖα, οὐρανός

**kratos-phertatos-sovereignty-vocabulary-theogony** — `approve`
: appliesTo extension to 385 (Kratos/Bia as Zeus's enforcer-retinue) and 403 (mega kratei ... anassei) verified: the sovereignty-word tracking is exactly what the Block A entry anticipated ('personified later as Κράτος at 385'). Consistent; direct intact.
: *Citations:* LSJ s.v. κράτος; West 1966 comm. ad 385, 403

**titanes-folk-etymology-theogony** — `approve`
: appliesTo extension to 392 (Τιτῆσι) and 424 (Τιτῆσι ... proteroisi theoisin) verified: both are plain occurrences of the Titan name rendered 'Titans', consistent with the signed-off folk-etymology entry; no new pun-site. Direct intact.
: *Citations:* LSJ s.vv. Τιτάν, τίσις; West 1966 comm. ad 207-210

**athetized-lines-convention-theogony** — `approve`
: appliesTo extension to 323/324 verified as the only athetized lines in Block B; retained-and-translated unmarked in the surface with athetesis in commentary, exactly as the signed-off Block A convention (111/118/196). Direct intact.
: *Citations:* West 1966 (athetesis apparatus); Perseus <del> markup

**theogony-name-and-title-conventions** — `approve`
: appliesTo extension to Block B anchors 233 (Pontos) and 411 (Hekate) verified: Greek personified theonyms transliterated in Greek (not Latinized) forms, consistent with the signed-off Block A policy. Presentation convention, no lens; direct intact.
: *Citations:* Most 2006 (Loeb) orthography; Perseus tlg0020.tlg001.perseus-grc2; West 1966

