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
