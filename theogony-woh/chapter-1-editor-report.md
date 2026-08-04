# Chapter 1 (Block A, lines 1–210) Editor Report — Theogony (theogony-woh)

**Scope:** proem / *Dichterweihe* (1–115), cosmogony (116–133), Ouranos episode (134–210).
**Source:** Hesiod, *Theogony*, Perseus `tlg0020.tlg001.perseus-grc2` (Evelyn-White 1914 underlying text).
**Status advanced:** `draft` → `editor-review`. **Version:** `0.1.0-draft` → `1.0.0-rc1`.
**Overlay glossary:** created `_translation-glossary.json` v1.0.0 (11 entries; 9 `direct`, 2 `inferred`, 0 `speculative`).
**Central glossary:** not modified by the Editor. One recommendation (against a change) is filed below.

The governing rule for the whole block was **accuracy-before-lens**: every contested
site was rendered at its defensible scholarly value and the Wheel-of-Heaven reading, where
one exists, was confined to clearly-marked commentary. Only **one** line's English surface
was changed (27); everything else was ratified as translated and documented.

---

## Decisions per editorial question (12 of 12 resolved)

- **THEO-1 — name policy.** Accepted the Evelyn-White default: transliterate personified
  theonyms in Greek (not Latinized) forms — Ouranos, Kronos, Gaia, Kypros, Kythereia,
  Kyklopes — and gloss the common-noun senses only where the reference does. Folded into
  overlay meta-entry `theogony-name-and-title-conventions`; per-line note on 20. No surface change.
- **THEO-11 — *aigiochos*.** Accepted 'aegis-holding' (Evelyn-White); *aigis* left
  untranslated. Overlay `aigiochos-aegis-bearer-zeus-epithet-theogony` (direct); note on 11.
  No surface change.
- **THEO-27 — Muses' *pseudea/etyma/alēthea* crux.** **Surface change at 27** to distinguish
  *ἔτυμα* 'genuine' from *ἀληθέα* 'true', following Most (2006 Loeb) against Evelyn-White
  (who renders both 'true'). Overlay `pseudea-etyma-alethea-muses-truth-crux-theogony`
  (**inferred**); notes on 27, 28. The demythologizing implication is kept in commentary only.
- **THEO-18 — *ankylomētēs*.** Accepted 'of crooked counsel' (< *mētis*); the *harpē*/sickle
  folk-association noted, not adopted. Overlay `ankylometes-crooked-counsel-kronos-epithet-theogony`
  (direct); note on 18. No surface change.
- **THEO-49 — rule vocabulary.** Accepted 'mightiest … greatest in power'; *κράτος* tracked as
  the poem's sovereignty-word (personified Kratos at 385, outside the block). Overlay
  `kratos-phertatos-sovereignty-vocabulary-theogony` (direct); note on 49. No surface change.
- **THEO-50 — *Gigantes* / cross-corpus.** Translated 'Giants'. Held the Hesiodic earth-born
  Giants **distinct** from the Nephilim; the shared Septuagint lexeme γίγαντες recorded as
  comparative apparatus only. Overlay `gigantes-hesiodic-earthborn-vs-nephilim-theogony`
  (**inferred**); notes on 50, 185. **Central entry NOT extended** — see the CENTRAL section.
- **THEO-108 — *gaia* personification.** Accepted common noun 'the earth' (physical
  catalogue). Folded into the boundary entry; note on 108. No surface change.
- **THEO-110 — *ouranos* boundary.** Accepted common noun at 71/110; god elsewhere;
  personification onset fixed at 126–127. Overlay
  `ouranos-gaia-cosmogony-personification-boundary-theogony` (direct); notes on 106, 108, 110, 127.
  No surface change.
- **THEO-116 — *Chaos* sense.** Transliterated 'Chaos'; sense fixed in commentary as the
  primordial 'gap/chasm/void' (√χα-, West 1966), not the later 'disorder'. Overlay
  `chaos-primordial-chasm-void-theogony` (direct); notes on 116, 123. No surface change.
- **THEO-120 — *Eros* cosmic principle.** Transliterated 'Eros'; primordial cosmogonic-principle
  role marked in commentary; distinguished from the later Eros of 201. Overlay
  `eros-primordial-cosmogonic-principle-theogony` (direct); notes on 120, 201. No surface change.
- **THEO-111 — athetized lines.** Retained and translated 111, 118, 196 unmarked in the
  surface; athetesis recorded in commentary. Overlay `athetized-lines-convention-theogony`
  (direct); notes on 111, 118, 196. No surface change.
- **THEO-207 — Titans folk-etymology.** Transliterated 'Titans'; *τιταίνοντας* 'straining'
  and *τίσιν* 'requital' rendered literally, the τιταίνω~Τιτῆνες / τίσις pun left visible only
  in the Greek. Overlay `titanes-folk-etymology-theogony` (direct); notes on 207, 209, 210.
  No surface change.

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry was created in Block A. Every site of special
Wheel-of-Heaven interest (the Muses' truth-declaration 27–28, Chaos 116, Eros 120, the
Ouranos/Gaia cosmogony 116–133, the Titan etymology 207–210, the Gigantes 50/185) was
resolved accuracy-first, with any lens-reading confined to commentary as clearly-marked
interpretation. Status is therefore free to advance to `editor-review` with no speculative
blocker.

**Lens-surface audit (for the Reviewer):** the only English surface change in the block is
27, and it is purely philological (ἔτυμα 'genuine' vs ἀληθέα 'true', per Most 2006) — not a
lens move. The passages a lens would most want to bend — Chaos-without-a-creator (116), Eros
as a generative principle (120), the Muses mixing plausible falsehood with truth (27–28), and
the pan-tradition "giants" fusion (50) — were all deliberately **not** bent in the text.

---

## Unresolved editorial questions

**None.** All 12 questions were resolved into overlay glossary entries and per-line
commentary; the `editorial_questions[]` array is now empty.

---

## Glossary changes for review

### Per-translation overlay (`data-library/theogony-woh/_translation-glossary.json`, new file, v1.0.0)

Added (11 entries):

- `theogony-name-and-title-conventions` (direct) — THEO-1, THEO-20
- `aigiochos-aegis-bearer-zeus-epithet-theogony` (direct) — THEO-11/13/25/52
- `pseudea-etyma-alethea-muses-truth-crux-theogony` (**inferred**) — THEO-27/28 *(surface change)*
- `ankylometes-crooked-counsel-kronos-epithet-theogony` (direct) — THEO-18/137/168
- `kratos-phertatos-sovereignty-vocabulary-theogony` (direct) — THEO-49
- `gigantes-hesiodic-earthborn-vs-nephilim-theogony` (**inferred**) — THEO-50/185
- `chaos-primordial-chasm-void-theogony` (direct) — THEO-116/123
- `eros-primordial-cosmogonic-principle-theogony` (direct) — THEO-120/201
- `ouranos-gaia-cosmogony-personification-boundary-theogony` (direct) — THEO-45/71/106/108/110/117/126/127/133
- `athetized-lines-convention-theogony` (direct) — THEO-111/118/196
- `titanes-folk-etymology-theogony` (direct) — THEO-207/208/209/210

### Central glossary — apply by orchestrator

**No central change is requested.** The relevant question, THEO-50, concerns the central
cross-corpus entry `nephilim-giants-1-enoch-7-gen-6-4-cross-corpus` (current `appliesTo`
scope: Enoch / Genesis / Jubilees refIds; **no** THEO-* refIds).

**Editor adjudication: do NOT extend that entry to the Theogony.** The Hesiodic Gigantes are
earth-born (*γηγενεῖς*) from the blood of the castrated Ouranos — a mythic class distinct from
the Watcher-progeny Nephilim/*gibbōrîm*. Appending THEO-50/185 to that entry's `appliesTo`
would assert that the central entry *governs* those lines, which over-reads a shared Greek
translation-word (γίγαντες, used by the LXX for both Nephilim and *gibbōrîm* at Gen 6:4) as an
identity of referents. The shared-lexeme datum is preserved as comparative apparatus in the
overlay entry `gigantes-hesiodic-earthborn-vs-nephilim-theogony` and in the line-50/185
commentary instead.

**Optional (only if the human reviewer overrides the adjudication):** should the project decide
it wants the γίγαντες lexeme cross-referenced at the central level, the Editor's preference is a
**new, separate** central lexeme-note rather than extending the Nephilim entry — e.g.:

```json
{
  "id": "gigantes-septuagint-lexeme-cross-corpus",
  "source": "γίγαντες (LXX Gen 6:4 = נְפִילִים / הַגִּבֹּרִים); Γίγαντες (Hesiod, Theogony 50, 185)",
  "translit": "gigantes",
  "strongs": "LSJ s.v. Γίγας; LXX Gen 6:4; Rahlfs–Hanhart",
  "partOfSpeech": "Greek noun — the shared 'giants' translation-lexeme across the Greek reception",
  "literal": "the giants",
  "standardEnglish": "the giants",
  "wohChoice": "document γίγαντες as the shared Greek reception-word for otherwise distinct 'giant' classes (Hesiodic earth-born vs biblical/Enochic Nephilim); NOT an identity of referents",
  "claim_type": "inferred",
  "rationale": "The Septuagint renders both נְפִילִים and הַגִּבֹּרִים at Gen 6:4 with γίγαντες, the same word Hesiod uses for the earth-born Giants (Theog. 50, 185); this makes γίγαντες the shared lexical hinge of the later Greco-Jewish and Christian giants tradition, while the underlying mythic classes remain distinct (Hesiodic γηγενεῖς from Ouranos's blood vs the Watcher-human hybrids of 1 Enoch 6–7). The entry records the reception-lexeme link only; it does not assert that the classes are the same, and the Editor recommends it NOT be created unless the reviewer explicitly wants the cross-reference.",
  "appliesTo": ["GEN-6:4", "THEO-50", "THEO-185"]
}
```

If created, bump central `version` semver-minor (addition). The Editor's standing
recommendation is to leave central untouched.

---

## Notes for the Reviewer

- **Surface diff from Evelyn-White:** exactly one line (27). All other lines were ratified as
  drafted or given commentary only.
- **Athetized lines 111/118/196** are retained and translated per project convention;
  111 is a verbatim repeat of 46 (checkable). Their bracketed status is in the commentary,
  not the surface.
- **Transliteration verification:** the Greek quoted in the overlay/commentary was hand-set;
  one accent was corrected post-write (Ἔρος at 120). A light proofreading pass over the Greek
  glosses in the notes is advisable at Reviewer stage.
- **Blocks B–D (211–1042) pending;** several overlay entries (aigiochos, ankylomētēs, the
  personification boundary, kratos) are scoped to recur and should carry forward.
