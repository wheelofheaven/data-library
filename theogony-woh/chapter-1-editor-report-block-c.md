# Chapter 1 Editor Report — Block C (lines 453–735)

**Text:** Hesiod, *Theogony* (`theogony-woh/chapter-1.json`)
**Block C scope:** lines 453–735 — the Kronos–Rhea succession (swallowed
children, the swaddled stone), Zeus's birth in Krete and the disgorged stone
at Pytho, the freeing of the Kyklopes and their storm-triad gift, the Iapetids
(Atlas, Menoitios, Prometheus, Epimetheus), the Mekone sacrifice-division, the
fire-theft, the *kalon kakon* / fashioned woman and the race-of-women aetiology,
Prometheus bound and freed, and the Titanomachy into the opening of the Tartaros
description.
**Editor:** claude-opus-4-8[1m] acting as woh-editor
**Status advanced:** `draft` → `editor-review`; **version** `1.2.0-draft` →
`1.2.0-rc1`; scope C → `editor-review`. `editorial_questions[]` emptied (all 14
resolved below).
**Overlay:** `_translation-glossary.json` `1.1.0` → `1.2.0` (12 new entries + 7
appliesTo extensions; semver-minor, additions only).
**Central glossary:** no change requested (see the CENTRAL section).

Blocks A–B (1–452), their notes/glossaryRefs, and
`translation.reviewer / reviewedAt / reviewerReport / reviewerReportBlockB`
were treated as immutable and verified byte-identical after the edit.

---

## Decisions per editorial question

### THEO-454 — dialectal name-forms (Histiē→Hestia, Aïdēs→Hades)
**Decision:** Option 1 — standard Greek forms **Hestia** (454) and **Hades**
(455); source spellings *Ἱστίην* / *Ἀίδην* kept verbatim in the `text` field.
These are Greek forms, not Latinizations (which would be Vesta, Pluto/Dis), so
the name convention is honoured, not breached. Recorded in the new overlay entry
`dialectal-theonym-normalization-theogony` (claim_type `direct`), parallel to the
signed-off *Γῆ*→Gaia (106) and *Γρήνικον*→Granikos (342) normalizations. Note at
454/455.

### THEO-462 — kingly-honour τιμή outside the honour-lexicon scope
**Decision:** Option 1 — render 'kingly honour' (462) / 'honour' (491)
consistently with the Block-B honour-vocabulary mapping, but that entry is **not
applied**. Rationale: *βασιληΐς τιμή* is the singular *royal* honour (kingship
itself), which belongs conceptually with the *kratos/phertatos* sovereignty
vocabulary, not with the shared-out *gerea/timai* of the Hekate hymn (the
honour-vocabulary entry's stated domain). No new entry; scope boundary recorded
in the note at 462.

### THEO-477 — Crete/Krete toponym exonym
**Decision:** **Krete** (Greek form), a surface **divergence from Evelyn-White's
'Crete'** — overriding the Translator's draft default. The Block-B river-exonym
question was signed off by the human as KEEP GREEK FORMS, no exceptions
(Neilos-not-Nile, Istros-not-Danube), and the closer Block-A island precedent
*Kypros*-not-Cyprus governs directly: Κρήτη is an island toponym exactly parallel
to Κύπρος, so 'Krete' follows a fortiori and is **not a materially different
case**. The other Block-C toponyms are already Greek-form (Lyktos, Mount Aigaion,
Pytho, Parnassos — the eta-spelling *Παρνησ-* normalized). New overlay entry
`place-name-greek-forms-block-c-theogony` (claim_type `direct`); surface changes
at 477, 480. **Flagged for the Reviewer** as a familiar-exonym judgement call.

### THEO-500 — the stone at Pytho, σῆμα
**Decision:** Option 1 — **'sign'** (Evelyn-White) for *σῆμα*; *θαῦμα* 'marvel'.
The text has only *σῆμα* + *θαῦμα*; the word *ὀμφαλός* does not occur. The later
*omphalos* ('navel-stone') identification of the Delphic stone is kept **out of
the surface** and named only as clearly-labeled reception apparatus in the note.
New overlay entry `sema-stone-at-pytho-theogony` (claim_type `direct`); the
swallowed-/disgorged-stone succession device and its ANE (Kumarbi) analogue
recorded as comparative apparatus, non-fusion. Substantial note at 500 (+485).

### THEO-504 — the Cyclopes' thunder-triad
**Decision:** Option 1 — **'thunder / blazing thunderbolt / lightning'**
(Evelyn-White) for *βροντή / κεραυνός / στεροπή*, with no rigid technical
distinction imposed. New overlay entry
`thunder-triad-bronte-keraunos-sterope-theogony` (claim_type `direct`) fixes the
consistent block-wide rendering across 458, 504–505, 515, 690–691, 699, 707.

### THEO-536 — Mekone dasmos/moira vs honour-lexicon scope
**Decision:** Option 1 — 'portion / divide / allot' (Evelyn-White), honour-
vocabulary entry **not applied**; *ἐκρίνοντο* (535) 'were settling their
reckoning' (Evelyn-White), the 'were being separated' reading (West) noted not
adopted. The *δα-* verbs and *μοῖρα* here are the meat-division / fate-allotment
domain (also Atlas's lot, 520), distinct from the divine-prerogative
apportionment. New overlay entry `dasmos-moira-meat-division-mekone-theogony`
(claim_type `direct`); the sacrifice-portion aetiology's ANE resonance recorded
as apparatus, non-fusion.

### THEO-546 — ankylomētēs transferred Kronos→Prometheus
**Decision:** Option 1 — render 'of the crooked counsel' (lexically identical to
the Kronos rendering); the Kronos-scoped
`ankylometes-crooked-counsel-kronos-epithet-theogony` entry is **not applied** to
546. **Audit trail:** the entry's appliesTo *was* extended to the two Block-C
*Kronos* uses (473, 495); 546 (Prometheus) is deliberately excluded and the
Hesiodic epithet-transfer documented as a distinct decision in the note at 546.
This keeps the entry's "recurring epithet of Kronos" framing intact and respects
the one-minor-bump / no-modification constraint.

### THEO-563 — Μελίῃσι crux
**Decision:** Option 1 — 'to the Meliai' (563), taken with Evelyn-White as the
Melian race of men in apposition to 'mortal men' (564) and linked to the
ash-nymphs of 187; the bare-'ash-trees' reading and the emendation *μελέῃσι*
'wretched' noted, not adopted. New overlay entry `meliai-crux-theogony` —
**claim_type `inferred`** (commits to one horn of a genuine crux, parallel to the
Block-B `ein-arimoisin-crux` entry). **This is the block's only non-`direct`
entry.** Note at 563.

### THEO-567 — νάρθηξ
**Decision:** Option 1 — **'hollow fennel-stalk'** (Evelyn-White; the giant
fennel *Ferula communis*, whose pith carries embers), over a transliterated
'narthex' or 'reed'. Folded into the new `fire-theft-prometheus-theogony` entry
(claim_type `direct`). Note at 566/567.

### THEO-571 — Amphigyeeis / Ennosigaios periphrases
**Decision:** Option 1 — render the epithet-titles **literally**, do not
substitute proper names: 'the loud-crashing Earth-Shaker' (456 = Poseidon, per
441) and 'the renowned Lame One' (571, 579 = Hephaestus). New overlay entry
`periphrastic-title-unnamed-god-theogony` (claim_type `direct`). Notes at 456,
571. The smith-god identification (WoH-salient) carried in the note, not the
surface.

### THEO-585 — kalon kakon
**Decision:** Option 1 — **'the beautiful evil'** (Evelyn-White; oxymoron
preserved). Verified and enforced: the *Theogony* names **no Pandora** and has
**no jar/pithos** — the woman is only the *πλαστὴ γυνή* / *παρθένος*; that
material (Works & Days) is **not imported**. Covered by the new
`kalon-kakon-fashioned-woman-theogony` entry (claim_type `direct`). Note at 585;
source line-final period preserved verbatim.

### THEO-590 — race-of-women register
**Decision:** Option 1 — literal Evelyn-White rendering, unsoftened; the
misogynistic register handled in commentary (register note at 590), not
sanitized in the surface. Governed by `kalon-kakon-fashioned-woman-theogony`.

### THEO-626 — Gaia's counsel/prophecy vocabulary
**Decision:** Option 2 — **coin a dedicated motif entry**,
`gaia-counsel-prophecy-vocabulary-theogony` (claim_type `direct`), tracking
Gaia's prophetic counsel across 463–465 / 475 / 494 / 626 (culminating at 884,
Block D); surface rendered literally per Evelyn-White. Lens-discipline note at
463/626.

### THEO-630 — Titan/theoi opposition formula
**Decision:** Option 1 — **apposition** 'the Titan gods and all who were born of
Kronos' (630/648/668), not a three-item list; both sides are *θεοί* (633/664 =
the 46/111 hemistich) → a theomachy, gods vs gods. New overlay entry
`titanomachy-both-sides-gods-theomachy-theogony` (claim_type `direct`). The
Titanomachy↔central-chaoskampf/theomachy convergence recorded as apparatus only,
non-fusion (see CENTRAL). Substantial note at 630.

---

## Overlay changes — `_translation-glossary.json` v1.1.0 → v1.2.0

Semver-minor (additions only; no existing entry's `rationale`/`wohChoice`
modified). Description extended with a Block-C paragraph. **26 → 38 entries.**

### New entries (12) — claim_type: 11 `direct`, 1 `inferred`, 0 `speculative`

| id | claim_type | appliesTo |
|---|---|---|
| `dialectal-theonym-normalization-theogony` | direct | 454, 455, 734 |
| `place-name-greek-forms-block-c-theogony` | direct | 477, 480, 482, 484, 499 |
| `sema-stone-at-pytho-theogony` | direct | 485, 486, 497, 498, 500 |
| `thunder-triad-bronte-keraunos-sterope-theogony` | direct | 458, 504, 505, 515, 690, 691, 699, 707 |
| `dasmos-moira-meat-division-mekone-theogony` | direct | 520, 535, 536, 537, 544 |
| `fire-theft-prometheus-theogony` | direct | 563, 565, 566, 567, 569, 570 |
| `periphrastic-title-unnamed-god-theogony` | direct | 456, 571, 579 |
| `meliai-crux-theogony` | **inferred** | 563 |
| `kalon-kakon-fashioned-woman-theogony` | direct | 513, 570, 585, 590, 591, 592 |
| `gaia-counsel-prophecy-vocabulary-theogony` | direct | 463, 464, 465, 475, 494, 626 |
| `titanomachy-both-sides-gods-theomachy-theogony` | direct | 630, 633, 648, 664, 668 |
| `tartaros-underworld-vocabulary-theogony` | direct | 682, 721, 725, 729, 731 |

All twelve carry every required field
(`id/source/translit/strongs/lemma/partOfSpeech/literal/standardEnglish/wohChoice/claim_type/rationale/appliesTo`)
with ≥3-sentence rationales; Greek terms indexed by LSJ (+ West 1966 / Chantraine
DELG) per the overlay's auditability-not-Strong's convention.

### appliesTo extensions on 7 existing entries (additive)

- `ankylometes-crooked-counsel-kronos-epithet-theogony` → **+473, +495**
  (Kronos Block-C uses; **546 deliberately excluded** — see THEO-546).
- `kratos-phertatos-sovereignty-vocabulary-theogony` → +647, +662.
- `titanes-folk-etymology-theogony` → +630, 632, 648, 650, 663, 668, 674, 676,
  697, 717, 729.
- `ouranos-gaia-cosmogony-personification-boundary-theogony` → +461, 463, 470,
  479, 486, 494, 502, 505, 517, 626, 644, 679, 685, 693, 702.
- `theogony-name-and-title-conventions` → +453, 507, 617.
- `aigiochos-aegis-bearer-zeus-epithet-theogony` → +735.
- `athetized-lines-convention-theogony` → +496, 576, 577, 591.

### Surface (i18n.en) changes vs the Translator's draft — 3 lines

- **THEO-477** 'the rich land of Crete' → 'the rich land of **Krete**' (THEO-477).
- **THEO-480** 'in wide Crete' → 'in wide **Krete**' (THEO-477).
- **THEO-734** 'great-hearted **Obriareos**' → 'great-hearted **Briareos**'
  (dialectal-normalization; source *Ὀβριάρεως* kept in `text`).

No other Block-C surface line was altered; every verse the Translator handled at
the Evelyn-White standard was left intact. 40 Block-C lines received
`notes.official` commentary; all others left empty.

---

## CENTRAL — apply by orchestrator

**None requested.** No central-glossary entry
(`data-content/i18n/translation-glossary.json`, v2.73.0) is modified or extended
by this block. Central was queried (targeted `python3`, never read whole) for
every cross-corpus pull Block C raises; in each case the signed-off Block-A/B
**non-fusion precedent** governs — reception/convergence links are recorded
overlay-side as clearly-labeled apparatus, and no central entry is made to govern
a THEO refId. Rationale and the optional specs (should the founder later want the
convergence made explicit centrally):

1. **Titanomachy ↔ chaoskampf / theomachy cluster.** Central
   `chaoskampf-sea-conflict-cross-corpus-ugaritic-akkadian-hebrew-bible`
   (claim_type `direct`) is scoped to the Baal Cycle (`BCY-WOH-*`) and
   `ISA-27:1`; it references **no** THEO refId. The Titanomachy is the Greek
   instance of the same succession-conflict/theomachy pattern, but extending a
   Semitic-corpus *sea-conflict* entry to Greek theomachy would be interpretive
   synthesis (a `speculative`-grade cross-cultural claim) — declined. Recorded in
   the note at 630 and in `titanomachy-both-sides-gods-theomachy-theogony` as
   apparatus. *Optional future spec:* a new central
   `succession-conflict-theomachy-cross-corpus` entry (claim_type `speculative`,
   human sign-off required) could bind BCY / Enūma Eliš / Kumarbi / Theogony 630
   — but that is a founder-level convergence decision, not an Editor call.

2. **Swallowed/disgorged stone at Pytho ↔ omphalos.** Central has
   `jerusalem-as-omphalos-*` entries (1 Enoch 26; Jubilees 8:19). Hesiod's text
   says only *σῆμα* + *θαῦμα*; *ὀμφαλός* is absent. No extension — the omphalos
   reading is later reception, disciplined out of the surface and named only in
   the 500 note.

3. **Fire-theft (Prometheus).** No central `prometheus`/fire-theft entry exists
   (central `fire`-id hits are Leviathan / Sinai / Pentecost / Abraham-
   iconoclasm — unrelated). Nothing to extend; the culture/knowledge-gift lens is
   apparatus-only in the 566 note.

4. **kalon kakon / fashioned woman ↔ Eve / creation-of-woman.** Central has
   `ish-ishah`, `ezer-kenegdo`, and `nin-ti-lady-of-rib-…-eve` (Sumerian). The
   Pandora-less Theogony woman-as-bane aetiology is compared to Genesis 2–3 as
   apparatus only in the 585 note; no central Eve entry is extended (non-fusion,
   as with the Block-A gigantes↔nephilim and Block-B mounogenēs↔Johannine
   handling).

5. **Tartaros ↔ 2 Peter 2:4 *tartaroō*.** No central Tartaros entry exists. The
   2 Peter reception is recorded overlay-side in `tartaros-underworld-vocabulary-
   theogony` and the 721 note; nothing central to create or extend.

---

## Speculative escalations requiring human sign-off

**None.** No Block-C entry is `claim_type: speculative`; the one non-`direct`
entry (`meliai-crux-theogony`) is `inferred`. `translation.status` is therefore
advanced to `editor-review` cleanly, with no speculative entry gating further
advancement.

For the human reviewer's awareness (not blocking): every high-scrutiny WoH-salient
site in the block — the Titanomachy, Gaia's prophetic counsel, the σῆμα at Pytho,
the fire-theft, the *kalon kakon* / fashioned woman, and Tartaros — was rendered
**accuracy-first**, with the canon lens (Theomachy-as-history, fire-as-knowledge,
omphalos, woman↔Eve, cosmic-prison) confined to clearly-labeled lens-discipline
notes and to reception/comparative apparatus. Those apparatus links are the
place the block goes furthest, and they are all overlay-side and non-fusion; if
the founder wants any of them promoted to an explicit central convergence claim,
that would be a new `speculative` central entry requiring sign-off (see the
CENTRAL section, item 1).

---

## Notes for the Reviewer

**Translator consistency decisions — both ratified:**

- **'Rhea' surface form (453, 467, 625, 634).** *Ratified.* The Translator kept
  'Rhea' for the source's Ionic *Ῥείη/Ῥέην*, matching Block A's surface at 135.
  'Rhea' is the standard transliteration of the goddess (not a Latinization), and
  surface consistency with the signed-off Block A is correct. No new governance
  was created (Block A 135 established the form and is immutable); ratification
  recorded in the note at 453.
- **Nike / Bie as common nouns in the Titanomachy.** *Ratified.* In the battle,
  *νίκη* 'victory' (628, 647) and *βίη* 'might/force' (e.g. 649, 662, 677) are
  common nouns, correctly kept distinct from the *personified* Styx-children
  **Nike** and **Bia** (384–385, Block B) governed by
  `personified-abstractions-nyx-eris-brood-theogony`. This is the same
  personified-vs-common-noun discipline applied to Chimaira/chimaira and
  gaia/Gaia. Ratification recorded in the note at 647.

**Flagged judgement call — Crete → Krete (477, 480).** The one place I overrode
the Translator's draft default. Draft had the familiar 'Crete'; I rendered
'Krete' under the signed-off KEEP-GREEK-FORMS river-exonym precedent and the even
closer Kypros-not-Cyprus island precedent. If the human prefers reader-familiar
'Crete' as an entrenched-exonym exception, that is a one-line revert of
`SURFACE[477]`/`[480]` and a claim_type-neutral note tweak; I judged consistency
with the signed-off convention the stronger call. Please confirm.

**Source-fidelity quirks — all preserved verbatim, none "fixed", each noted:**
- **Athetized lines 496, 576–577, 591** — retained/translated unmarked, athetesis
  recorded (athetized-lines convention).
- **Dagger crux at 659** (`ἄψορρον δʼ† ἐξαῦτις…`) — obelus kept, rendered per the
  received sense, not emended (note at 659).
- **Mid-phrase stop at 566** (`…τηλέσκοπον. αὐγὴν`) — kept; sense enjambs to 567
  (note at 566).
- **Line-final period at 585** though the sentence enjambs to 586 — kept (note at
  585).
- **Unaccented *Εσπερίδων* 518** — kept in `text`; surface 'Hesperides' (note at
  518).
- **Eta-spelling *Παρνησοῖο* 499** — kept in translit; surface 'Parnassos'
  (place-name entry; note at 499).
- **Variant *Ὀβριάρεως* 734** — kept in `text`; surface normalized to 'Briareos'
  for consistency with 617/714 (note at 734).

**No West transpositions in this range** (the west-transposed-line-order
convention entry governs Block B only; not extended).

**Reviewer focus suggestions:** (1) the Crete→Krete divergence; (2) the
`meliai-crux-theogony` `inferred` grade and whether the apposition-reading should
instead be flagged as a bare `direct` literal-dative with the crux in commentary
only; (3) the 546 ankylomētēs non-application decision (entry Kronos-scoped, the
Prometheus transfer as a note) vs. extending the entry with context-subdivided
appliesTo; (4) the register handling of the race-of-women passage (590–612) —
confirm the accuracy-first "preserve unsoftened, flag in commentary" ruling.
