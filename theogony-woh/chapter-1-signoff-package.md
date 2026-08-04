# Sign-off package — Theogony (theogony-woh), chapter 1

**Scope:** Block A — lines 1–210 of 1042 (proem, cosmogony, Ouranos). Blocks B (211–452), C (453–735), D (736–1022 + 929a–t) pending.

**Status:** `awaiting-human` | **Version:** `1.0.0-rc1`
**Reviewer (agent):** claude-opus-4-8[1m] acting as woh-reviewer at 2026-08-04T06:03:05Z
**Central glossary:** v2.73.0 — **unchanged** (no central diffs this chapter)
**Overlay glossary:** new file, v1.0.0

## Summary

| Metric | Value |
|---|---|
| Lines translated | 210 (1–210) |
| Lines with official commentary | 22 |
| Glossary refs in chapter | 34 (all resolving; none dangling) |
| Surface divergences from Evelyn-White | 1 (line 27) |
| Editorial questions resolved | 12 of 12 |
| Overlay entries added | 11 (direct: 9, inferred: 2) |
| Reviewer verse verdicts | 35 (approve: 34, revise: 1) |
| Reviewer glossary verdicts | 11 (approve: 10, revise: 1) |
| Lens-leakage flags | 0 |
| Speculative entries | 0 |

## Orchestrator actions after review

Both `revise` verdicts were mechanical Greek-typography errata; the orchestrator applied
them post-review, so they are **already fixed** in the shipped files:

1. Overlay `ankylometes-crooked-counsel-kronos-epithet-theogony` rationale: `κάρχαρόδοντα` → `καρχαρόδοντα` (stray acute removed).
2. Chapter THEO-49 `notes.official`: Latin capital K in `Κράτος` → Greek capital kappa (U+039A).

No other file changes were made outside the agents' own writes.

## Items requiring decision

1. **Ratify the package** — on sign-off the chapter is promoted to `stable` / `1.0.0`,
   `_meta.json` updated (chapterCount, chapterFiles, revision), and both repos committed.
2. **Optional central entry** `gigantes-septuagint-lexeme-cross-corpus` — Editor and
   Reviewer both recommend **leaving the central glossary untouched** (Hesiodic Giants ≠
   Nephilim; the shared LXX γίγαντες lexeme is documented in the overlay + commentary).
   Full JSON for the optional entry is in the escalation report below, only if you want
   the lexeme cross-referenced centrally. Default on plain sign-off: **no central change**.
3. **Block B (lines 211–452)** — next Translator run when you want to continue the book.

---

# Editor escalation report (inlined)

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


---

# Reviewer report (inlined)

**Reviewer:** claude-opus-4-8[1m] acting as woh-reviewer
**Reviewed at:** 2026-08-04T06:03:05Z
**Lens-leakage flags:** 0

## Verse verdicts (35)

**THEO-1** — `approve`
: Re-parsed Μουσάων Ἑλικωνιάδων ἀρχώμεθʼ ἀείδειν: 'From the Muses of Helikon let us begin to sing' is a faithful hortatory-subjunctive rendering. The transliterate-personified / gloss-common-noun name policy (Ouranos not Uranus, etc.) is standard scholarly practice and lens-free.
: *Citations:* West 1966, comm. ad 1; Most 2006 (Loeb) orthography

**THEO-11** — `approve`
: αἰγίοχον re-parsed as aig- + -οχος (< ἔχω): 'who holds the aegis' is the consensus rendering; aigis left untranslated as a cultic object. Evelyn-White retained, no divergence, no lens. (Also 13, 25, 52.)
: *Citations:* LSJ s.v. αἰγίοχος; Chantraine, DELG s.v. αἰγίς; West 1966 ad 11

**THEO-13** — `approve`
: Recurrence of αἰγίοχος (aegis-holding) with bright-eyed Athena; consistent with THEO-11. Faithful to Evelyn-White.
: *Citations:* —

**THEO-25** — `approve`
: Recurrence of αἰγίοχος; 'daughters of aegis-holding Zeus' faithful to source and Evelyn-White.
: *Citations:* —

**THEO-52** — `approve`
: Recurrence of αἰγίοχος; refrain line, faithful to source.
: *Citations:* —

**THEO-18** — `approve`
: ἀγκυλομήτην re-parsed as ἀγκυλο- 'crooked' + μῆτις 'counsel': 'of the crooked counsel' is the consensus reading; the harpē/sickle folk-association is correctly noted-not-adopted. (Also 137, 168.)
: *Citations:* LSJ s.v. ἀγκυλομήτης; West 1966 ad 18

**THEO-137** — `approve`
: Recurrence of ἀγκυλομήτης for Kronos 'youngest'; consistent with THEO-18.
: *Citations:* —

**THEO-168** — `approve`
: Recurrence of ἀγκυλομήτης; consistent with THEO-18.
: *Citations:* —

**THEO-20** — `approve`
: Catalogue line (Gaia, Okeanos, black Nyx) re-parsed; the block name policy (personified theonyms transliterated in Greek forms) is a presentation convention matching the reference edition. No lens.
: *Citations:* Most 2006 (Loeb); Perseus tlg0020.tlg001.perseus-grc2

**THEO-27** — `approve`
: The block's one deliberate surface divergence. Re-parsed ἴδμεν ψεύδεα πολλὰ λέγειν ἐτύμοισιν ὁμοῖα (modelled on Od. 19.203). Rendering ἐτύμοισιν 'genuine' (distinct from ἀληθέα 'true' at 28), following Most 2006 against Evelyn-White's collapse of both to 'true', is philologically defensible: ἔτυμος = 'real/genuine/actual' vs ἀληθής = 'un-concealed/true'. The demythologizing (lens-congenial) reading is correctly confined to commentary; the line says only what the Greek says.
: *Citations:* Most 2006 (Loeb), trans. ad 27; LSJ s.v. ἔτυμος, ἀληθής; West 1966 comm. ad 27-28; Pucci 1977; Puelma 1989

**THEO-28** — `approve`
: ἀληθέα γηρύσασθαι 'how to utter what is true' re-parsed; ἀληθέα kept distinct from ἔτυμα (27). Faithful and internally consistent with the Most-based distinction.
: *Citations:* LSJ s.v. ἀληθής; Most 2006 (Loeb) ad 28

**THEO-45** — `approve`
: οὓς Γαῖα καὶ Οὐρανὸς εὐρὺς ἔτικτεν: the parental pair named by anticipation (personified), transliterated Gaia/Ouranos. Consistent with the boundary entry; matches Evelyn-White sense.
: *Citations:* —

**THEO-71** — `approve`
: οὐρανῷ ἐμβασιλεύει 'reigns in heaven' correctly taken as common-noun sky (Zeus not yet in the personified cosmogony here). Matches Evelyn-White.
: *Citations:* West 1966 ad 71; LSJ s.v. οὐρανός

**THEO-49** — `revise`
: TRANSLATION APPROVED: φέρτατός … κράτεϊ … μέγιστος 'the mightiest of the gods and greatest in power' is faithful (Evelyn-White retained). REVISE is note-only and mechanical: the official note writes 'Κράτος' with a LATIN capital K (U+004B) where Greek kappa Κ (U+039A) is required; correct to 'Κράτος'. The overlay kratos entry already uses the correct Greek Κ. No lens.
: *Citations:* LSJ s.v. κράτος, φέρτατος; West 1966 comm. — correct Greek form Κράτος (U+039A) as in the overlay glossary

**THEO-50** — `approve`
: κρατερῶν τε Γιγάντων re-parsed 'the mighty Giants'. The Giants=Nephilim adjudication is correct and lens-disciplined: the Hesiodic Gigantes are earth-born (γηγενεῖς, per 183-187), a distinct class from the biblical/Enochic Nephilim; the shared LXX lexeme γίγαντες (Gen 6:4, for both נפילים and גברים) is documented as comparative apparatus, NOT identity. The ancient-astronaut 'pan-giant fusion' is correctly declined in the surface. The optional central cross-lexeme entry remains a documented human-override decision (not required).
: *Citations:* Septuagint Gen 6:4 (γίγαντες = נְפִילִים / הַגִּבֹּרִים; Rahlfs-Hanhart); West 1966 comm. ad 185; LSJ s.v. Γίγας

**THEO-106** — `approve`
: οἳ Γῆς τʼ ἐξεγένοντο καὶ Οὐρανοῦ ἀστερόεντος: divine parental pair (personified by anticipation); Γῆς normalized to standard transliteration Gaia per the name convention. Matches Evelyn-White sense.
: *Citations:* West 1966 ad 106; LSJ s.v. γαῖα

**THEO-108** — `approve`
: γαῖα in the physical catalogue (gods, earth, rivers, sea, stars, heaven) correctly rendered common-noun 'the earth', though the register is genuinely ambiguous (personified nine lines later, 117). Matches Evelyn-White; the ambiguity is honestly flagged in commentary.
: *Citations:* West 1966 comm. ad 108; LSJ s.v. γαῖα

**THEO-110** — `approve`
: οὐρανὸς εὐρὺς ὕπερθεν 'the wide heaven above' correctly common-noun; personification onset fixed at 126-127. Matches Evelyn-White.
: *Citations:* West 1966 comm. ad 116-128

**THEO-117** — `approve`
: Γαῖʼ εὐρύστερνος 'wide-bosomed Gaia' — first personified/born deity; correctly transliterated. Faithful.
: *Citations:* —

**THEO-126** — `approve`
: Γαῖα … ἐγείνατο ἶσον ἑαυτῇ: Gaia as personified deity bearing Ouranos; correct. Faithful to source.
: *Citations:* —

**THEO-127** — `approve`
: Οὐρανὸν ἀστερόενθʼ 'starry Ouranos' — onset of Ouranos-personification correctly fixed here (126-128). Faithful.
: *Citations:* West 1966 comm. ad 126-128

**THEO-133** — `approve`
: Οὐρανῷ εὐνηθεῖσα 'having lain with Ouranos' — personified consort; consistent with the boundary. Faithful.
: *Citations:* —

**THEO-111** — `approve`
: Athetized line (verbatim repeat of 46) retained-and-translated unmarked in the surface, athetesis recorded in commentary — a transparent presentation convention with no interpretive content. Verified 111 == 46 in the source.
: *Citations:* West 1966 (apparatus criticus); Perseus <del> markup

**THEO-118** — `approve`
: Athetized line (suspected expansion of the 'seat of the immortals' formula, cf. 128) retained-and-translated, athetesis noted. Convention correctly applied.
: *Citations:* West 1966 (apparatus)

**THEO-196** — `approve`
: Athetized line (anticipatory cult-title gloss for 197-198) retained-and-translated, athetesis noted. Convention correctly applied.
: *Citations:* West 1966 (apparatus)

**THEO-116** — `approve`
: πρώτιστα Χάος γένετʼ 'first of all Chaos came to be'. Kept transliterated with the reference; the sense correctly fixed in commentary as the primordial gap/chasm/void (√χα-, χαίνω/χάσκω), NOT the post-classical 'disorder' — the settled scholarly reading. The spontaneous γένετο / no-creator observation is confined to comparative apparatus. No lens in the line.
: *Citations:* West 1966 comm. ad 116; Kirk-Raven-Schofield 1983; LSJ s.v. χάος, χάσκω

**THEO-123** — `approve`
: ἐκ Χάεος 'From Chaos came Erebos and black Nyx' — consistent with the gap/void sense fixed at 116. Faithful.
: *Citations:* —

**THEO-120** — `approve`
: ἠδʼ Ἔρος 'and Eros, fairest among the immortal gods'. Kept transliterated (not 'Love'/'Desire') as a named primordial entity; the cosmogonic-principle role (λυσιμελής, 121-122) correctly marked in commentary and distinguished from the secondary Eros of 201. Mainstream reading, no lens. (Accent Ἔρος verified correct — the Editor's post-write fix.)
: *Citations:* West 1966 comm. ad 120; Kirk-Raven-Schofield 1983; LSJ s.v. ἔρος

**THEO-201** — `approve`
: τῇ δʼ Ἔρος ὡμάρτησε: the secondary Eros attending new-born Aphrodite, correctly distinguished from the primordial Eros of 120. Faithful.
: *Citations:* —

**THEO-185** — `approve`
: γείνατʼ Ἐρινῦς τε κρατερὰς μεγάλους τε Γίγαντας: the earth-born Giants' aetiology (from Ouranos's blood-drops, with Erinyes and Meliai). 'the great Giants' faithful; cross-reference to the 50 Giants=Nephilim distinction correct.
: *Citations:* West 1966 comm. ad 185; LSJ s.v. Γίγας

**THEO-207** — `approve`
: Hesiod's folk-etymology of Τιτῆνες re-parsed: τιταίνοντας 'straining/overreaching' (< τιταίνω) and τίσιν 'requital' (< τίσις) rendered literally, the τιταίνω~Τιτῆνες / τίσις double pun left visible only in the Greek. Correctly declines both a manufactured English pun and an inline gloss; the true origin of Τιτᾶνες is unknown to philology, honestly stated.
: *Citations:* West 1966 comm. ad 207-210; LSJ s.v. Τιτάν, τιταίνω, τίσις

**THEO-208** — `approve`
: παῖδας νεικείων μέγας Οὐρανός: Ouranos reproaching his sons; faithful, part of the Titan-etymology frame.
: *Citations:* —

**THEO-209** — `approve`
: φάσκε δὲ τιταίνοντας: 'straining in their presumption' — the pun-word rendered literally per the adopted policy. Faithful.
: *Citations:* —

**THEO-210** — `approve`
: τίσιν μετόπισθεν ἔσεσθαι: 'there would afterward be requital' — the assonant τίσις element rendered literally. Faithful.
: *Citations:* —

**THEO-2 … THEO-206 (all remaining unglossed lines of Block A)** — `approve`
: Independently re-parsed all 210 lines of the Perseus grc source. The unglossed remainder (the proem's bee-simile and just-king passage 22-104, the Kyklopes 139-146, Hundred-Handers 147-153, the castration narrative 154-200, Aphrodite's birth 188-206, etc.) faithfully tracks Evelyn-White with standard epic-hexameter renderings; no undocumented divergences, no mistranslations, and no lens leakage were found. μήδεα rendered plainly 'genitals' (176-200) with no euphemism or lens.
: *Citations:* Evelyn-White 1914 (Loeb) as baseline; West 1966 comm.


## Glossary-entry verdicts (11)

**theogony-name-and-title-conventions** — `approve`
: claim_type=direct verified: the transliterate-personified / gloss-common-noun policy and the descriptive chapter title are presentation conventions matching the reference edition, carrying no interpretive claim and no lens.
: *Citations:* Most 2006 (Loeb) orthography; Perseus tlg0020.tlg001.perseus-grc2; West 1966

**aigiochos-aegis-bearer-zeus-epithet-theogony** — `approve`
: claim_type=direct verified: αἰγίοχος = aig- + -οχος (< ἔχω), 'aegis-holding', is the consensus rendering; the ἀΐσσω minority etymology is correctly noted as not changing the received sense. Evelyn-White retained, no lens.
: *Citations:* LSJ s.v. αἰγίοχος; Chantraine, DELG s.v. αἰγίς; West 1966 ad 11

**pseudea-etyma-alethea-muses-truth-crux-theogony** — `approve`
: claim_type=inferred VERIFIED and correctly chosen. The ἔτυμα 'genuine' vs ἀληθέα 'true' distinction is defended by named scholarship (Most 2006) and debated by others (Pucci, Puelma) — a reasonable reading, not universal consensus, so 'inferred' (not 'direct') is the honest label. The lexical evidence cited (LSJ ἔτυμος 'real/actual' vs ἀληθής 'un-concealed') is accurate. The lens-discipline note correctly quarantines the demythologizing reading to commentary.
: *Citations:* Most 2006 (Loeb) ad 27-28; LSJ s.v. ἔτυμος, ἀληθής, ψεῦδος; West 1966 comm. ad 27-28; Pucci 1977; Puelma 1989; Od. 19.203

**ankylometes-crooked-counsel-kronos-epithet-theogony** — `revise`
: claim_type=direct ENDORSED (ἀγκυλο- + μῆτις 'of crooked counsel'; sickle folk-association correctly noted-not-adopted). REVISE is a single mechanical accent fix: the rationale spells the sickle epithet 'κάρχαρόδοντα' with an extraneous acute on the first alpha (U+03AC); correct to 'καρχαρόδοντα' (plain alpha U+03B1), as spelled correctly in source lines 175 and 180. No substantive change.
: *Citations:* LSJ s.v. ἀγκυλομήτης; West 1966 ad 18; source lines 175/180 (correct spelling καρχαρόδοντα)

**kratos-phertatos-sovereignty-vocabulary-theogony** — `approve`
: claim_type=direct verified: φέρτατος 'mightiest' and κράτος 'sovereign might' are standard; 'mightiest … greatest in power' retained from Evelyn-White. Tracking κράτος as the poem's sovereignty-word (personified Κράτος at 385) is sound. NB the Latin-K erratum flagged under THEO-49 is in the CHAPTER note, not in this entry (which uses the correct Greek Κ).
: *Citations:* LSJ s.v. κράτος, φέρτατος; West 1966 comm.

**gigantes-hesiodic-earthborn-vs-nephilim-theogony** — `approve`
: claim_type=inferred VERIFIED. The two factual components (Hesiodic Giants earth-born; LXX γίγαντες renders both Nephilim and gibborim at Gen 6:4) are accurate; the synthetic framing of γίγαντες as the 'shared lexical hinge' of the later giants tradition is a reasonable reading, so 'inferred' is defensible (even conservative). Non-extension of the central Nephilim entry is the correct call.
: *Citations:* Septuagint Gen 6:4 (Rahlfs-Hanhart); West 1966 ad 185; LSJ s.v. Γίγας; Hansen 2004

**chaos-primordial-chasm-void-theogony** — `approve`
: claim_type=direct verified: the √χα- (χαίνω/χάσκω) 'gap/chasm/void' sense of Χάος, against the post-classical 'disorder', is the settled scholarly reading; keeping the word transliterated in the line (sense in commentary) is correctly justified. The no-creator comparative note is quarantined to apparatus.
: *Citations:* West 1966 comm. ad 116; Kirk-Raven-Schofield 1983; LSJ s.v. χάος, χάσκω

**eros-primordial-cosmogonic-principle-theogony** — `approve`
: claim_type=direct verified: the primordial-cosmogonic-principle reading of Ἔρος (120), distinct from the secondary Eros (201), is mainstream; transliteration retained, role in commentary. No lens.
: *Citations:* West 1966 comm. ad 120; Kirk-Raven-Schofield 1983; LSJ s.v. ἔρος

**ouranos-gaia-cosmogony-personification-boundary-theogony** — `approve`
: claim_type=direct verified: the line-by-line common-noun/personified boundary (physical at 71/108/110; personified from 117, onset 126-127) matches Evelyn-White; the Γῆς→Gaia normalization at 106 follows the name convention. The genuine ambiguity at 108 is honestly acknowledged.
: *Citations:* West 1966 comm. ad 108, 116-128; LSJ s.v. γαῖα, οὐρανός

**athetized-lines-convention-theogony** — `approve`
: claim_type=direct verified: 111 (= 46 verbatim), 118, 196 are bracketed in the edition; retaining-and-translating them with the athetesis in commentary is a transparent apparatus convention, no interpretive content.
: *Citations:* West 1966 (apparatus criticus); Perseus <del> markup

**titanes-folk-etymology-theogony** — `approve`
: claim_type=direct verified: Hesiod's τιταίνω~Τιτῆνες / τίσις wordplay (207-210) is his own folk-etymology; rendering the pun-words literally and leaving the play in the Greek is defensible, and the entry honestly states the real origin of Τιτᾶνες is unknown.
: *Citations:* West 1966 comm. ad 207-210; LSJ s.v. Τιτάν, τιταίνω, τίσις

