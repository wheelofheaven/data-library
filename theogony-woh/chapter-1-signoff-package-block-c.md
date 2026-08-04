# Sign-off package — Theogony (theogony-woh), chapter 1, Block C

**Scope:** Block C — lines 453–735 (Rhea/Kronos and the swallowed children; Zeus's birth and
the stone at Pytho; the Cyclopes' gift; the Iapetids — Mekone, the fire-theft, the kalon kakon
and the race of women, Prometheus bound and freed; the Titanomachy into the Tartarus opening).
Extends signed-off Blocks A–B (1–452). Block D (736–1022 + 929a–t) pending.

**Status at hand-off:** `awaiting-human` → **signed off** by zarazinsfuss 2026-08-04, with the
Briareos fork decided per the recommendation; promoted to `stable` / **1.2.0** at 2026-08-04T11:44:32Z.
**Central glossary:** v2.73.0 — **unchanged** (third consecutive block; zero THEO refIds in central)
**Overlay glossary:** v1.2.0 (38 entries; +12 new in Block C, 7 appliesTo extensions)

## Summary

| Metric | Value |
|---|---|
| Lines appended | 283 (453–735); chapter now 735 of 1042 |
| Block C lines with official commentary | 40 |
| Block C glossary refs | 95 (all resolving; none dangling) |
| Surface changes vs Evelyn-White-default draft | 3 (Krete 477/480; Briareos 734) |
| Editorial questions resolved | 14 of 14 |
| Overlay total after Block C | 38 (direct: 34, inferred: 4) |
| Reviewer verse verdicts | 42 (approve: 41, flag-for-human: 1) |
| Reviewer glossary verdicts | 19 (approve: 18, flag-for-human: 1) |
| Lens-leakage flags | 0 |
| Speculative entries | 0 |

## The two human decisions, and how they were resolved

1. **Krete (THEO-477/480).** Editor override of the draft's "Crete", confirmed by the Reviewer
   as *mandated* by the human's no-exceptions Greek-forms ruling (Block B rivers; Kypros
   precedent). Shipped as "Krete" under that standing ruling.
2. **Briareos (THEO-734).** The source's one-off prothetic-omicron variant *Ὀβριάρεως* was
   normalized to "Briareos" in the surface (variant preserved verbatim in the Greek text field
   and documented in commentary). The Reviewer withheld approval pending explicit human
   ratification since this set a NEW convention (variant-normalization, distinct from
   Latinization-avoidance). **Human ratified "Briareos"** (2026-08-04), consistent with the
   block's Hestia/Hades/Rhea/Parnassos surface-normalization pattern. The variant-normalization
   convention is now human-ratified precedent for Block D and future books.

## Orchestrator actions after review

1. Note 734 + overlay `dialectal-theonym-normalization-theogony` rationale corrected per the
   Reviewer's errata: the *Iliad* 1.403 citation now correctly identifies the Briareos/Aigaion
   name-doublet as a distinct phenomenon (the prothetic-omicron variant is Hesiodic — West ad
   734); the unverifiable "as Evelyn-White does" claim removed; occurrence count corrected to
   four (149, 617, 714, 734).
2. Note 630 precision fix: line 648 reads first-person *ἐκγενόμεσθα* (Reviewer erratum 3).
3. Promotion to stable/1.2.0; `_meta.json` → 735 lines, revision 3.

## Items noted for the future

1. **Block D (736–1022 + 929a–t)** — Tartarus description, Styx oath procedure, Typhoeus,
   Metis, Athena's birth, the 929a–t variant block, the closing marriage catalogues.
   Translator launched on sign-off. The 929a–t variant passage will pose the block model's
   biggest source-presentation question; the ratified variant-normalization and
   athetized-lines conventions are the governing precedents.
2. The Editor's optional central `succession-conflict-theomachy` spec (Block C report) remains
   a founder-level decision; both agents recommend against creating it now.
3. On composition completion (post-D): consolidation pass — composition-level sign-off record,
   `_meta` finalization, public roadmap doc refresh.

---

# Editor escalation report (inlined)

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


---

# Reviewer report (inlined)

**Reviewer:** claude-opus-4-8[1m] acting as woh-reviewer
**Reviewed at:** 2026-08-04T11:15:27Z
**Lens-leakage flags:** 0

## Verse verdicts (42)

**THEO-453** — `approve`
: Re-parsed Ῥείη δὲ δμηθεῖσα Κρόνῳ τέκε φαίδιμα τέκνα: δμηθεῖσα (aor. pass. of δαμάζω) 'subdued/mastered' is the stock formula for a goddess bearing to a consort, and 'splendid children' for φαίδιμα τέκνα matches EW. The 'Rhea' surface form for the source's Ionic Ῥείη is correctly held to the signed-off Block-A form (135); ratified.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 453; LSJ s.v. δαμάζω

**THEO-454** — `approve`
: Ἱστίην is the Ionic accusative of Ἑστία; 'Hestia' is the standard panhellenic Greek form (not the Latin Vesta), so the name convention is honoured, not breached. Dialectal normalization with source spelling kept in the text field.
: *Citations:* Evelyn-White 1914 (Loeb); LSJ s.v. Ἑστία

**THEO-455** — `approve`
: Ἀίδην is the epic unaspirated form of Ἅιδης; 'Hades' (not the Latin Pluto/Dis) is the standard Greek form. ἴφθιμον 'mighty' and the chthonic 'who dwells in halls beneath the earth' are faithful.
: *Citations:* Evelyn-White 1914 (Loeb); LSJ s.v. Ἅιδης

**THEO-456** — `approve`
: ἐρίκτυπον Ἐννοσίγαιον 'the loud-crashing Earth-Shaker' designates the unnamed Poseidon; rendering the periphrastic title literally (not substituting the name) follows EW and the treatment fixed at 441. νηλεὲς ἦτορ 'pitiless heart' correctly attaches to Hades.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 456; LSJ s.vv. ἐρίκτυπος, Ἐννοσίγαιος

**THEO-462** — `approve`
: βασιληΐδα τιμήν is the singular royal honour (kingship itself), correctly distinguished from the shared-out gerea/timai of the Hekate hymn; holding the honour-vocabulary entry off this line and grouping it with the kratos/phertatos sovereignty domain is a defensible scope boundary, and the rendering 'kingly honour' stays consistent.
: *Citations:* West 1966 comm. ad 462; LSJ s.vv. τιμή, βασιληΐς

**THEO-463** — `approve`
: πεύθετο … Γαίης τε καὶ Οὐρανοῦ 'he had learned from Gaia and starry Ouranos' the prophecy (πέπρωτο 'it was fated', 464) is rendered literally with EW. Gaia's foreknowledge steering the succession is WoH-salient, but the line and note stay lexical — no cosmological reading pressed; lens-clean.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 463-465; LSJ s.vv. πεύθομαι, πέπρωται

**THEO-475** — `approve`
: καί οἱ πεφραδέτην, ὅσα περ πέπρωτο γενέσθαι 'they told her all that was fated to come to pass' — the second link in the Gaia/Ouranos counsel-prophecy motif; literal, faithful to EW.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 475

**THEO-477** — `approve`
: KRETE RULING — CONFIRMED. Κρήτης → 'Krete' diverges from EW's 'Crete' but is mandated by the human-signed-off no-exceptions Greek-forms ruling (Neilos/Istros) and the a-fortiori island precedent Kypros-not-Cyprus; 'Crete' is the Latin-derived exonym, 'Krete' the plain transliteration of Κρήτη. Pure Latinization-avoidance, zero lens. The human retains the documented one-line revert if they want a reader-familiar exonym exception, but under the standing ruling Krete is correct.
: *Citations:* West 1966 comm. ad 477-484; signed-off Block-B river-catalogue ruling (KEEP GREEK FORMS, no exceptions); Block-A Kypros-not-Cyprus precedent; 'Crete' < Latin Creta

**THEO-480** — `approve`
: Κρήτῃ ἐν εὐρείῃ 'in wide Krete' — the same Greek-form retention as 477; confirmed under the signed-off convention.
: *Citations:* West 1966 comm. ad 480; see THEO-477

**THEO-484** — `approve`
: Αἰγαῖον ὄρος → 'Mount Aigaion' (Greek form). The Cretan localization varies in the tradition (Ida/Dikte/Aigaion, West 1966), but the transmitted text names Aigaion and the surface faithfully follows it; note correctly records the variance without altering the line.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 484

**THEO-485** — `approve`
: μέγαν λίθον … σπαργανίσασα 'a great stone wrapped in swaddling-clothes' is rendered plainly. The Hurro-Hittite Kumarbi-cycle stone parallel is real and is recorded as clearly-labeled comparative apparatus only, not fused with any central entry — correct per the A/B non-fusion precedent.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 485; W, The East Face of Helicon (Kumarbi cycle)

**THEO-496** — `approve`
: Line 496 is athetized in the edition; retained and translated unmarked in the surface with the athetesis recorded, per the signed-off athetized-lines convention. Source carries no literal brackets (verified) — the note carries the text-critical status.
: *Citations:* West 1966 comm. (apparatus criticus) ad 496

**THEO-499** — `approve`
: Πυθοῖ 'at Pytho' (Delphic site) and the eta-spelling Παρνησοῖο normalized to standard 'Parnassos' in the surface, source form preserved in the translit — consistent with the Block-C place-name convention.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 499; LSJ s.v. Πυθώ

**THEO-500** — `approve`
: σῆμα → 'sign' (EW), θαῦμα → 'marvel'; the word ὀμφαλός does not occur, and the later omphalos ('navel-stone') identification of the Delphic stone (Pausanias 10.24.6) is correctly disciplined out of the surface and named only as labeled reception apparatus, with jerusalem-as-omphalos not extended. Exemplary lens discipline at a high-scrutiny site.
: *Citations:* West 1966 comm. ad 500; Pausanias 10.24.6; LSJ s.vv. σῆμα, θαῦμα

**THEO-504** — `approve`
: The Kyklopes' storm-triad βροντή/κεραυνός/στεροπή → 'thunder / blazing thunderbolt / lightning' with EW; the three-way sense is not lexically rigid in early epic, and fixing a consistent (non-rigid) block-wide rendering is a defensible consistency convention.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 504-505; LSJ s.vv. βροντή, κεραυνός, στεροπή

**THEO-511** — `approve`
: The Prometheus 'fore-thinker' / Epimetheus 'after-thinker' speaking-name contrast is left visible only in the Greek; the epithets (ποικίλον αἰολόμητιν; ἁμαρτίνοον) are rendered literally without a manufactured English pun — correct per the folk-etymology convention.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 510-511; LSJ s.vv. Προμηθεύς, Ἐπιμηθεύς

**THEO-518** — `approve`
: Source prints Εσπερίδων unaccented and without rough breathing (verified verbatim in the text field); the surface gives standard 'Hesperides'. Source quirk correctly preserved, not silently fixed.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 518

**THEO-520** — `approve`
: ταύτην … μοῖραν … ἐδάσσατο 'this portion Zeus allotted' — μοῖρα/δατέομαι here belong to the fate-allotment/meat-division domain, correctly held distinct from the divine-prerogative timē/geras apportionment; 'portion … allotted' with EW.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 520; LSJ s.v. μοῖρα

**THEO-521** — `approve`
: The Prometheus-punishment digression (ἀλυκτοπέδῃσι 'inescapable fetters', the liver-eating eagle, Herakles' rescue) is placed by ring-composition before the Mekone aetiology; rendered with EW, no divergence.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 521-534

**THEO-535** — `approve`
: ἐκρίνοντο is a genuine crux: 'were settling their reckoning' (EW, followed) vs 'were being separated' — the parting of gods and men (West 1966). Following the reference and flagging West's alternative in commentary rather than diverging is the correct conservative call for the Mekone aetiology.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 535; LSJ s.v. κρίνω; Vernant 1979 (Detienne-Vernant, La cuisine du sacrifice)

**THEO-546** — `approve`
: Hesiod transfers Kronos's signature ἀγκυλομήτης 'of crooked counsel' to Prometheus here; the lexical value is identical so the rendering is unchanged, and correctly the Kronos-scoped entry is NOT applied to 546 — the epithet-transfer is documented as a distinct decision. Philologically sharp.
: *Citations:* West 1966 comm. ad 546; LSJ s.v. ἀγκυλομήτης

**THEO-556** — `approve`
: ἐκ τοῦ 'from that time' men burn the white bones on fragrant altars — the aetiological close of the Mekone division; faithful to EW.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 556-557

**THEO-563** — `approve`
: Μελίῃσι is one of the poem's hardest cruxes. The surface renders the bare transmitted dative 'to the Meliai' (in fact more conservative than EW's 'the Melian race of mortal men'), leaving 564 in apposition; the entry's commitment to the Melian-race construal is correctly graded inferred, not resolved in the line. No lens.
: *Citations:* West 1966 comm. ad 563; EW; Works & Days 145; Theogony 187 (the Meliai from Ouranos's blood)

**THEO-566** — `approve`
: τηλέσκοπον αὐγήν 'far-seen gleam' of fire in a hollow fennel-stalk; source prints a mid-phrase period after τηλέσκοπον (verified verbatim), sense enjambing to 567, correctly preserved. The fire-as-knowledge WoH resonance is confined to the note; the line says only 'fire' — lens-clean.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 566-567; LSJ s.v. νάρθηξ

**THEO-567** — `approve`
: νάρθηξ → 'hollow fennel-stalk' (the giant fennel, whose dry pith carries an ember), correctly retained over a transliterated 'narthex' or a generic 'reed'. Botanically exact and faithful to EW.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 567; LSJ s.v. νάρθηξ (Ferula communis)

**THEO-571** — `approve`
: περικλυτὸς Ἀμφιγυήεις 'the renowned Lame One' designates the unnamed Hephaestus, who moulds the first woman γαίης 'from earth'; the periphrastic title is rendered literally, the smith-god named only in the note. The WoH-salient 'craftsman-god fashions humankind's counterpart' motif is kept out of the surface — lens-clean.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 571; LSJ s.v. Ἀμφιγυήεις

**THEO-576** — `approve`
: The garland couplet 576-577 is athetized in the edition; retained/translated unmarked with the athetesis recorded, per the convention.
: *Citations:* West 1966 comm. (apparatus criticus) ad 576-577

**THEO-585** — `approve`
: καλὸν κακόν 'the beautiful evil' — the oxymoron is preserved with EW. Crucially enforced: the Theogony names no Pandora and has no jar (pithos) — that material belongs to Works & Days and is correctly NOT imported. The Genesis 2-3 Eve comparison is labeled apparatus only, ish-ishah/ezer-kenegdo/nin-ti not fused. Exemplary discipline.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 585; Works & Days 60-105 (Pandora, the pithos); Vernant 1974

**THEO-590** — `approve`
: ἐκ τῆς γὰρ γένος … γυναικῶν 'for from her is the race of women', a πῆμα 'plague' for men (592), rendered literally and unsoftened; the ancient misogynistic register is preserved accuracy-first, flagged in commentary as a datum of the text, neither sanitized nor editorialized in the surface — correct register handling, and no lens.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 590-612; Loraux, Les enfants d'Athéna; Vernant 1974

**THEO-591** — `approve`
: Line 591 is athetized as a doublet of 590; retained/translated unmarked with the athetesis recorded, per the convention.
: *Citations:* West 1966 comm. (apparatus criticus) ad 591

**THEO-614** — `approve`
: ἀκάκητα Προμηθεύς 'kindly/guileless Prometheus' stands in pointed contrast to the ἀγκυλομήτης of 546 (even the guileless one could not overreach Zeus's mind); the epithet is rendered with EW and the contrast correctly noted.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 614; LSJ s.v. ἀκάκητα

**THEO-617** — `approve`
: Βριάρεῳ → 'Briareos' (standard form, no normalization needed here); 'their father' correctly = Ouranos, who bound the Hundred-Handers. Faithful.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 617; Iliad 1.403 (Βριάρεως)

**THEO-626** — `approve`
: Γαίης φραδμοσύνῃσιν 'by the counsels of Gaia' — the fourth link in the Gaia counsel/prophecy motif (463/475/494/626); rendered literally with EW, lens confined to the note.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 626

**THEO-630** — `approve`
: THEOMACHY FRAMING VERIFIED. Τιτῆνές τε θεοὶ καὶ ὅσοι Κρόνου ἐξεγένοντο rendered as apposition ('the Titan gods, and all who were born of Kronos'), not a three-item list; the Olympians too are θεοί δωτῆρες ἐάων (633/664 = the 46/111 hemistich) — a war of gods against gods. The central chaoskampf-sea-conflict entry is verified NOT extended (0 THEO refIds) and any Theomachy-as-history reading is confined to labeled apparatus. Exemplary.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 630-664; LSJ s.vv. Τιτάν, θεός

**THEO-647** — `approve`
: NIKE/BIE RATIFICATION CONFIRMED. νίκη 'victory' (647) and βίη 'might' (649/662) are common nouns in the Titanomachy, correctly kept distinct from the personified Styx-children Nike and Bia (384-385); the same personified-vs-common-noun discipline as gaia/Gaia and Chimaira/chimaira. κράτος 'power' tracked by the sovereignty entry.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 647; LSJ s.vv. νίκη, κράτος

**THEO-659** — `approve`
: Source prints an obelus (†) after δʼ at 659 (verified verbatim), marking a transmitted-text crux; the daggered text is kept as-is and rendered per the received sense, not silently emended — correct source fidelity.
: *Citations:* West 1966 comm. (apparatus criticus) ad 659

**THEO-682** — `approve`
: First Block-C Τάρταρον ἠερόεντα 'misty Tartaros'; transliterated (standard), descriptive vocabulary with EW. No 2-Peter tartaroo import into the surface.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 682; LSJ s.v. Τάρταρος

**THEO-700** — `approve`
: καῦμα … κάτεχεν Χάος 'a marvellous heat seized Chaos' — Χάος here correctly read as the primordial gap/void of 116 (√χα-, West), now filled with the heat of Zeus's bolts at the cosmic climax, NOT the post-classical 'disorder'. High-quality philology; lens-clean.
: *Citations:* West 1966 comm. ad 700 and ad 116; Kirk-Raven-Schofield 1983

**THEO-721** — `approve`
: Τάρταρος transliterated, prison-description with EW. The derived verb ταρταρόω at 2 Peter 2:4 (of the imprisoned rebel angels) is correctly recorded as labeled Greco-Jewish/Christian RECEPTION apparatus only — no 2-Peter import into the surface, no central Tartaros entry created (verified none exists).
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 720-735; LSJ s.v. ταρταρόω; 2 Peter 2:4 (ταρταρώσας)

**THEO-732** — `approve`
: Ποσειδέων 'Poseidon' is named directly here (the source names him), so the surface names him — correctly contrasting with the periphrastic Ennosigaios at 456 where the poet withholds the name. Consistent name/periphrasis discipline.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 732; LSJ s.v. Ποσειδέων

**THEO-714** — `approve`
: Κόττος τε Βριάρεώς τε Γύης — Βριάρεώς is the standard form, rendered 'Briareos' with no normalization required; ἄατος πολέμοιο 'insatiate of war' faithful. Establishes the baseline against which the 734 variant is measured.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 714; Iliad 1.403

**THEO-734** — `flag-for-human`
: OBRIAREOS RULING. The source's prothetic-omicron Ὀβριάρεως (a marked metrical variant the poet uses ONLY here, against Βριάρεως at 149/617/714) is normalized to 'Briareos' in the surface, source form preserved in the text field with a note. The normalization is philologically defensible and mainstream translator practice, so this is NOT a revise; but because it is a surface change to a proper name where the poet's own text preserves the marked variant, under a normalization convention new to this block and not yet human-ratified, and because the equally-defensible fidelity-first alternative (let 'Obriareos' stand at 734 with the note, as a Most-style faithful edition would) sits squarely on the source-fidelity-vs-surface-consistency stance line, the direction warrants explicit human ratification. Note: the entry's Iliad 1.403 citation documents the Briareos/Aigaion NAME-doublet, not the Ὀβρ-/Βρι- orthographic variant — a minor citation imprecision; and the 'as Evelyn-White does' justification is a claim about EW's English I could not verify against the source.
: *Citations:* West 1966 comm. ad 734; Iliad 1.403 (the Βριάρεως/Αἰγαίων name-doublet); Most 2006 (Loeb) fidelity practice


## Glossary-entry verdicts (19)

**dialectal-theonym-normalization-theogony** — `flag-for-human`
: Two of the three members are unimpeachable and I approve them as claim_type direct: Ἱστίην→Hestia and Ἀίδην→Hades normalize dialectal/epic spellings to the standard PANHELLENIC GREEK forms (not the Latin Vesta/Pluto), honouring the name convention. The third member — Ὀβριάρεως→Briareos — drives a surface change to a proper name at the one line where the poet preserves the marked prothetic-omicron variant; that is the source-fidelity-vs-consistency stance call flagged at THEO-734 and it needs explicit human ratification, so the entry as a whole is flagged. The Iliad 1.403 citation attests the Briareos/Aigaion name-doublet, not the Ὀβρ-/Βρι- variant being normalized.
: *Citations:* West 1966 comm. ad 454, 617, 734; Iliad 1.403; LSJ s.vv. Ἑστία, Ἅιδης, Βριάρεως

**place-name-greek-forms-block-c-theogony** — `approve`
: claim_type direct verified: Krete/Lyktos/Aigaion/Pytho/Parnassos in Greek forms is a presentation convention, not an interpretive claim. Κρήτη is an island toponym exactly parallel to Κύπρος→Kypros, so 'Krete' follows the human-signed-off no-exceptions Greek-forms ruling a fortiori; 'Crete' is the Latin exonym. Internally consistent, lens-free.
: *Citations:* West 1966 comm. ad 477-484, 499; signed-off Block-B river ruling (KEEP GREEK FORMS); Block-A Kypros-not-Cyprus

**sema-stone-at-pytho-theogony** — `approve`
: claim_type direct verified: σῆμα→'sign' is the settled lexical value; ὀμφαλός is absent from the text, and the omphalos identification (later reception, Pausanias) plus the ANE Kumarbi-cycle parallel are both correctly held as labeled apparatus only, non-fused, with jerusalem-as-omphalos verified NOT extended. No lens in the line.
: *Citations:* West 1966 comm. ad 485-500; Pausanias 10.24.6; LSJ s.v. σῆμα

**thunder-triad-bronte-keraunos-sterope-theogony** — `approve`
: claim_type direct verified: a non-rigid consistency convention regularizing 'thunder / blazing thunderbolt / lightning' across the block's recurrences (458/504-505/515/690-691/699/707), matching EW; LSJ reports no fixed technical opposition, so imposing none is correct. No lens.
: *Citations:* West 1966 comm. ad 504-505, 690-708; LSJ s.vv. βροντή, κεραυνός, στεροπή

**dasmos-moira-meat-division-mekone-theogony** — `approve`
: claim_type direct verified: keeping the meat-division/fate-allotment moira/δα- domain distinct from the divine-prerogative timē/geras lexicon is a lexical-domain distinction, not interpretation. ἐκρίνοντο ambiguity correctly follows EW with West's 'separation' reading noted; the Near-Eastern sacrificial-portion resonance is labeled apparatus, non-fused. No lens pressed on the aetiology.
: *Citations:* West 1966 comm. ad 535-557; Detienne-Vernant 1979; LSJ s.vv. μοῖρα, δατέομαι, κρίνω

**fire-theft-prometheus-theogony** — `approve`
: claim_type direct verified: πυρὸς μένος/αὐγήν 'might/far-seen gleam of fire' and νάρθηξ 'hollow fennel-stalk' (the giant fennel, ember-carrier) are rendered with EW; the fire-as-knowledge/culture-gift WoH resonance is confined to the note and there is verified NO central fire entry to fuse. Lens-clean.
: *Citations:* West 1966 comm. ad 562-570; LSJ s.v. νάρθηξ; Ferula communis

**periphrastic-title-unnamed-god-theogony** — `approve`
: claim_type direct verified: rendering the epithet-titles literally ('loud-crashing Earth-Shaker'=Poseidon 456; 'renowned Lame One'=Hephaestus 571/579) without substituting the withheld names follows EW and the 441 treatment. The smith-god-fashions-woman WoH point is carried in the note, not the surface. Confirmed against the direct naming of Poseidon at 732.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 441, 456, 571; LSJ s.vv. Ἐννοσίγαιος, Ἀμφιγυήεις

**meliai-crux-theogony** — `approve`
: claim_type inferred verified and CORRECT (addressing the Editor's downgrade question): the surface renders the bare transmitted dative, but the entry's wohChoice explicitly commits to the Melian-race/apposition construal against the 'ash-trees' reading and the μελέῃσι emendation — committing to one horn of a genuine crux where major editors divide, exactly parallel to the Block-B ein-Arimoisin inferred entry. Keeping it inferred (not downgrading to direct) is the more transparent labeling; the construal is defended by EW and several editors, satisfying the inferred bar.
: *Citations:* West 1966 comm. ad 563; EW; Works & Days 145; Theogony 187

**kalon-kakon-fashioned-woman-theogony** — `approve`
: claim_type direct verified: the oxymoron 'beautiful evil' is preserved with EW; the firm no-Pandora / no-pithos discipline is correct (that material is Works & Days) and the misogynistic race-of-women register is preserved unsoftened as a datum, not editorialized. The Genesis 2-3 Eve comparison is labeled apparatus only, ish-ishah/ezer-kenegdo/nin-ti verified NOT fused. No lens.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 570-612; Works & Days 60-105; Vernant 1974

**gaia-counsel-prophecy-vocabulary-theogony** — `approve`
: claim_type direct verified: φραδμοσύνη/ἐννεσίη/πέπρωται are well-understood LSJ material rendered literally with EW; coining a motif-tracking entry for consistency (463/475/494/626, culminating 884) parallels the kratos-phertatos and honour-vocabulary entries — a lexical-consistency convention, not an interpretive claim. The Gaia-as-foreknowledge WoH theme stays lexical in both surface and note.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 463-465, 494, 626, 884

**titanomachy-both-sides-gods-theomachy-theogony** — `approve`
: claim_type direct verified: the apposition reading of the repeated formula (630/648/668) and the both-sides-are-θεοί framing are on the surface of the Greek itself (633/664 = the 46/111 hemistich). The central chaoskampf-sea-conflict entry is verified NOT extended to any THEO refId (0 hits), and the Near-Eastern theomachy convergence plus any Theomachy-as-history reading are confined to labeled apparatus — sound per the A/B non-fusion discipline.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 630-664; LSJ s.vv. Τιτάν, θεός

**tartaros-underworld-vocabulary-theogony** — `approve`
: claim_type direct verified: 'Tartaros' transliterated (standard) and the prison-description vocabulary rendered with EW. Verified NO central Tartaros entry exists; the ταρταρόω / 2 Peter 2:4 reception is correctly recorded as labeled apparatus only, none created or extended. The cosmic-prison WoH image is held to the lexical level. No lens.
: *Citations:* Evelyn-White 1914 (Loeb); West 1966 comm. ad 720-735; 2 Peter 2:4 (ταρταρώσας); LSJ s.vv. Τάρταρος, ταρταρόω

**ankylometes-crooked-counsel-kronos-epithet-theogony** — `approve`
: Block-C appliesTo extension reviewed: adding the two Kronos uses (473, 495) is correct, and DELIBERATELY EXCLUDING 546 — where Hesiod transfers the epithet to Prometheus — keeps the entry's 'recurring epithet of Kronos' scope intact, with the transfer documented as a distinct decision. Philologically sound; I decline the alternative of a context-subdivided appliesTo.
: *Citations:* West 1966 comm. ad 18, 473, 495, 546; LSJ s.v. ἀγκυλομήτης

**kratos-phertatos-sovereignty-vocabulary-theogony** — `approve`
: Extension to 647, 662 verified: κράτος 'power' in the Titanomachy speeches is the same sovereignty-word tracked from 49/385/403; consistent, correct.
: *Citations:* West 1966 comm. ad 647, 662; LSJ s.v. κράτος

**titanes-folk-etymology-theogony** — `approve`
: Extension to the eleven Block-C Titan occurrences (630/632/648/650/663/668/674/676/697/717/729) verified: 'Titans' transliterated consistently; the folk-etymology stays a Block-A/B matter, only the name-transliteration is carried forward. Correct.
: *Citations:* West 1966 comm. ad 207-210, 630; LSJ s.v. Τιτάν

**ouranos-gaia-cosmogony-personification-boundary-theogony** — `approve`
: Extension to fifteen Block-C sites verified: personified Gaia/Ouranos throughout (incl. the τῆς μὲν … τοῦ δʼ earth-she/heaven-he crash at 702-704 and life-giving γαῖα φερέσβιος at 693); the boundary is drawn where EW draws it. Correct.
: *Citations:* West 1966 comm. ad 700, 702; LSJ s.vv. γαῖα, οὐρανός

**theogony-name-and-title-conventions** — `approve`
: Extension to 453, 507, 617 verified: Rhea (453), Iapetos/Okeanine (507), Briareos (617) in Greek-form transliteration per the standing convention. Correct.
: *Citations:* West 1966 comm.; Most 2006 (Loeb) orthography

**aigiochos-aegis-bearer-zeus-epithet-theogony** — `approve`
: Extension to 735 verified: Διὸς αἰγιόχοιο → 'aegis-holding Zeus', the same recurring epithet as 11/13/25/52, aigis left untranslated. Correct.
: *Citations:* LSJ s.v. αἰγίοχος; W+ ad 735

**athetized-lines-convention-theogony** — `approve`
: Extension to 496, 576, 577, 591 verified: each is athetized in the edition and retained/translated unmarked with the athetesis recorded in the note, per the signed-off convention. The source text field carries no literal brackets (verified) — the note is the sole carrier of text-critical status. Correct.
: *Citations:* West 1966 comm. (apparatus criticus) ad 496, 576-577, 591

