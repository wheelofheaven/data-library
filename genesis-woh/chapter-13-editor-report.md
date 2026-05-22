# Chapter 13 Editor Report

## Summary

- **Chapter:** Genesis 13 — The return from Mitsrayim and the separation
  from Lot
- **Translator draft:** 18 verses, version 0.1.0-draft, 8
  `editorial_questions[]` flagged
- **Editor output:** all 8 questions resolved, 6 new glossary entries
  added, commentary written for 10 of 18 verses (vv 3, 4, 7, 10, 13,
  14, 15, 16, 17, 18 — every divergent or keystone verse; the
  remaining eight verses — 1, 2, 5, 6, 8, 9, 11, 12 — are routine
  narrative-bridge and receive no commentary)
- **Status advanced:** draft -> editor-review
- **Version advanced:** 0.1.0-draft -> 1.0.0-rc1
- **Glossary pinned version:** 2.9.0 -> 2.10.0
- **Speculative entries requiring human sign-off:** **none**

The chapter is not high-lens-leverage. Its single load-bearing
WoH-relevant moment is the *gan YHWH* back-reference at v 10, which
the Eden / Sodom typology framing handles in scholarly register
(Westermann, Sarna, Hamilton, Alter consensus) without arguing the
full cosmology. The rest is patriarchal-narrative scaffolding —
ketiv/qere normalization, a Documentary Hypothesis parenthetical,
the patriarchal seeing-formula, the seed-comparison triad, the
covenant-walking rite, and the Mamre site introduction. No reading
goes beyond what major modern critical scholars argue.

## Speculative entries requiring sign-off

**None.** No entry in this chapter rises to `claim_type=speculative`.
Of the 6 new entries: 3 are `direct` (the lexical / formulaic facts
of the text — *gan YHWH* back-reference, *sa eynekha* formula,
seed-comparison triad, *elonei Mamre*) and 3 are `inferred`
(Documentary Hypothesis parenthetical, covenant-walking rite, and
the Mamre site has a `direct` rationale but its name-and-position
sit within a forward-loaded scholarly cluster). Every `inferred`
entry is grounded in named modern critical scholarship in its
`rationale`.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

Bumped v2.9.0 -> v2.10.0 (semver-minor, additions only — no
modifications to existing entries). Updated `scopeNote` to document
the chapter 13 entries and explicitly flag the *gan YHWH*
back-reference as the chapter's only high-lens-leverage moment.

**6 entries added** (all cross-corpus or chapter-keystone; per the
"overlay vs. central" rule, all 6 govern lemmata that recur across
Genesis or beyond, so all go to central):

| ID | claim_type | Governs | Source |
|---|---|---|---|
| `kenaani-prizi-az-ba-aretz` | inferred | Gen 12:6, 13:7 | Canaanite-Perizzite redactional parenthetical; J-stratum reading (Wellhausen, Gunkel, von Rad, Speiser) vs. pre-conquest reading (Cassuto, Kitchen) |
| `gan-yhwh-eden-back-reference` | direct | Gen 13:10 | Eden / Sodom typology; mainstream critical consensus (Westermann, Sarna, Hamilton, Alter, von Rad) |
| `sa-eynekha-lift-your-eyes` | direct | Gen 13:14 + 11 other patriarchal-cycle verses | the *nasa eynayim* seeing-formula across the Abraham-Isaac-Jacob-Joseph arc |
| `patriarchal-seed-comparison-triad` | direct | Gen 13:16, 15:5, 22:17, 26:4, 32:13 | dust + stars + sand cosmographic distribution (Sarna, Alter, Hamilton, Wenham) |
| `hithallech-ba-aretz-covenant-walking` | inferred | Gen 13:17 | covenantal land-walking rite; Daube 1947 *Studies in Biblical Law* §3 and the German *Begehungsritus* tradition; parallels at Josh 1:3, 18:8, Deut 11:24 |
| `elonei-mamre` | direct | Gen 13:18 + 9 other Mamre-site verses across the Abraham cycle | distinct from `elon-moreh` (Shechem); forward-loaded for Gen 14:13, 18:1, and the Machpelah burial-narratives |

### Per-translation overlay

**No overlay file created.** All 6 entries are either cross-corpus
(recur across Genesis or into the Deuteronomistic History) or encode
project-wide conventions about the patriarchal cycle, so all go to
central per the Editor brief's overlay-vs.-central rule.

### Modifications to existing entries

**None.** No existing entry was modified. The two glossary entries
the Translator had already mechanically applied (`eretz`,
`mitsrayim`, `qara-b-shem-yhwh`, `zera-eretz-promise`) remain
unchanged. The chapter's `elonei-mamre` entry is new and parallel to
`elon-moreh` (rather than an extension of it) — the two sacred-tree
sites are different proper names with different etymologies and
different recurrence-sets, and conflating them would erase the
distinction between the Moreh-as-oracle-giver reading and the
Mamre-as-Amorite-ally reading. Both Translator-flagged corrections
(no `va-yera YHWH` formula at v 14; `elonei Mamre` not the same as
`elon Moreh`) were sustained.

## Editorial decisions resolved

All 8 of the Translator's `editorial_questions[]` were resolved as
follows:

### `GEN-WOH-13:3` — ketiv/qere divergence

**Resolution:** translated the qere (אָהֳלוֹ / *oholo*, 'his tent').
**Method:** Editor's commentary at v 3 records the ketiv/qere
divergence, the three readings circulating (qere; defective
*oholah*; archaic spelling), and the consensus-with-ASV/NJPS/NRSV
position. No new glossary entry; the decision is verse-local and
follows standard Masoretic practice.

### `GEN-WOH-13:7` — Canaanite-Perizzite parenthetical

**Resolution:** translated 'were then dwelling in the land'
(participial-progressive). **New glossary entry:**
`kenaani-prizi-az-ba-aretz`, claim_type `inferred`. **Scope:**
applies to GEN-12:6 (where the simpler singular-Canaanite form
appears) and GEN-13:7. The retroactive addition to 12:6 is a
deliberate choice — the earlier verse's elon-moreh commentary
already noted the parenthetical, but the new entry gives the lemma
its own tracked glossary record. The Documentary Hypothesis reading
is recorded as well-attested but not universally accepted; both J-
stratum and pre-conquest readings are cited.

### `GEN-WOH-13:10` — *k-gan YHWH k-eretz Mitsrayim*

**Resolution:** translated literally ('like the garden of YHWH, like
the land of Mitsrayim'). **New glossary entry:**
`gan-yhwh-eden-back-reference`, claim_type `direct`. **Scope:** Gen
13:10. **Lens-relevance:** this is the chapter's single
high-lens-leverage moment. The Editor took the recommended approach:
surface the Eden / Sodom typology explicitly in the rationale and
commentary (which is consensus-scholarly territory) but hold the WoH
posture to a single sentence at the end of the rationale noting that
Gen 1's primeval-creation and Gen 2–3's Eden-garden are taken as
describing a single project-beginning context. The translation reads
literally; the typological reading is held in commentary; the lens
is held in the glossary rationale. The claim_type is `direct` rather
than `inferred` because the lexical back-reference (*gan* + YHWH) is
grammatically explicit and the scholarly consensus is unambiguous on
its existence; what it *means* theologically remains open.

### `GEN-WOH-13:13` — *l-YHWH chataim* dative

**Resolution:** translated 'sinners against YHWH exceedingly'
(matches ASV). **No new glossary entry.** Per the brief's editor's
call, the dative-l construction is grammatically standard for
'sinners against [someone]' (cf. Gen 39:9, Exod 10:16, Num 32:23 —
all named in the commentary) and Speiser / HALOT both treat it as
the normal Hebrew idiom. The verse-level commentary records the
doubled epithet *ra'im v-chata'im*, the dative-l / *neged*
distinction, and the *me'od* intensifier's link to the narrator-
editorial intrusions of Gen 6:5, 6:11–12. A cross-corpus
narrator-editorial-intrusion index entry was considered and
declined — the cluster would be a literary-critical observation
rather than a lexical decision, and the present cluster is small
enough that per-verse commentary handles it without a glossary
record. Reconsider on Gen 19 if the destruction-cycle commentary
warrants a unified narrator-intrusion entry.

### `GEN-WOH-13:14` — *sa eynekha* formula

**Resolution:** translated 'Lift up now your eyes and look' (matches
ASV). **New glossary entry:** `sa-eynekha-lift-your-eyes`,
claim_type `direct`. **Scope:** Gen 13:14, plus 11 further
occurrences across the patriarchal cycle (18:2, 22:4, 22:13, 24:63,
24:64, 31:10, 31:12, 33:1, 33:5, 37:25, 43:29). The commentary at
v 14 also notes the distinction between *va-YHWH amar* (here) and
*va-yera YHWH* (12:7, 17:1), which the Translator's framing-brief
correction flagged. The verse stages an auditory revelation rather
than a visual theophany; the *sa eynekha* imperative asks Abram to
lift his own eyes, not to behold a visible YHWH.

### `GEN-WOH-13:16` — seed-like-dust

**Resolution:** translated 'as the dust of the earth' (matches ASV).
**New glossary entry:** `patriarchal-seed-comparison-triad`,
claim_type `direct`. **Scope:** Gen 13:16, 15:5, 22:17, plus the
later cross-corpus expansions at Gen 26:4 (stars-to-Isaac) and Gen
32:13 (sand-in-Jacob's-prayer). Editor took the brief's recommended
single-consolidated-entry approach rather than three separate
per-comparison entries: the comparison structure is parallel across
all three, and the cosmographic distribution (earth / sky / shore)
reads as a deliberate set rather than three independent images.
Hamilton's reading of the dust-image as a Gen 2:7 / 3:19
creation-recall is preserved in both commentary and rationale.

### `GEN-WOH-13:17` — *hit'hallekh ba-aretz*

**Resolution:** translated 'Arise, walk through the land in the
length of it and in the breadth of it' (matches ASV). **New
glossary entry:** `hithallech-ba-aretz-covenant-walking`, claim_type
`inferred`. **Scope:** Gen 13:17. The claim_type is `inferred`
because the juridical-act framing is the modern scholarly synthesis
(Daube 1947 and the consensus that follows him: Speiser, Sarna,
Westermann, Wenham) rather than an explicit statement in the verse.
Forward-applies to Josh 1:3, Josh 18:8, Deut 11:24 are noted in the
rationale but not added to `appliesTo[]` — those will be set when
the respective Joshua / Deuteronomy chapters are translated. The
rationale also distinguishes this juridical-spatial sense of the
hithpael from the ethical-relational walking-before-Elohim sense
(Gen 3:8 Eden; Gen 5:22 Enoch; Gen 6:9 Noah; Gen 17:1 Abraham; etc.).

### `GEN-WOH-13:18` — *elonei Mamre*

**Resolution:** translated 'oaks of Mamre' (matches ASV). **New
glossary entry:** `elonei-mamre`, claim_type `direct`. **Scope:**
Gen 13:18, 14:13, 14:24, 18:1, 23:17, 23:19, 25:9, 35:27, 49:30,
50:13. The entry is **parallel to** `elon-moreh` (Gen 12:6), not
an extension of it: the two sacred-tree sites have different proper
names with different etymologies (*Moreh* = teacher / oracle-giver;
*Mamre* = name of the Amorite ally at Gen 14:13, 14:24), different
geographical locations (Shechem in the central hill country vs.
Hebron in the southern), and different recurrence-sets. The
Translator's framing-brief correction (that the `elon-moreh` entry
does *not* apply at 13:18) was sustained. Both sites fit the
broader patriarchal sacred-tree pattern (recorded in both entries'
rationales).

## Unresolved editorial questions

**None.** All 8 questions resolved either by glossary entry or by
verse-level commentary.

## Notes for the Reviewer

- **`gan-yhwh-eden-back-reference` is the chapter's only WoH-lens-
  relevant moment.** The Eden / Sodom typology framing is mainstream
  critical-scholarly territory (the rationale cites Westermann,
  Sarna, Hamilton, Alter, von Rad by name); the WoH posture is held
  to a single sentence noting that Gen 1 and Gen 2–3 are taken to
  describe a single project-beginning context. Reviewer should
  confirm that this is the right register — visible-in-rationale but
  not-arguing-the-cosmology — and flag if it has crept too far in
  either direction.

- **The `kenaani-prizi-az-ba-aretz` entry's retroactive scope to
  Gen 12:6** is a deliberate choice (the Translator's framing-brief
  noted that 12:6's *v-ha-Kna'ani az ba-aretz* parallel was already
  implicitly carried by the `elon-moreh` commentary). The new entry
  gives the lemma its own tracked record. Reviewer should confirm
  the retroactive `appliesTo[]` addition is appropriate.

- **The `sa-eynekha-lift-your-eyes` entry's `appliesTo[]` list (12
  patriarchal verses)** is comprehensive for the Abraham-Isaac-
  Jacob-Joseph arc but may not cover every Hebrew Bible occurrence
  of the *nasa eynayim* formula. Editor's call: keep the scope
  patriarchal-Genesis for v2.10.0; expand to other corpora (Psalms,
  Prophets) when those texts are translated.

- **The `patriarchal-seed-comparison-triad` entry's `appliesTo[]`**
  was set at five verses (Gen 13:16, 15:5, 22:17, 26:4, 32:13). The
  rationale lists many further Hebrew Bible expansions (Exod 32:13,
  Deut 1:10, 10:22, 28:62, etc.) but those are *later citations* of
  the patriarchal triad rather than instances of the triad itself.
  Reviewer should confirm the scope is correct — the triad is the
  five verses; the citations-of-the-triad are tracked in the
  rationale but not in `appliesTo[]`.

- **The `hithallech-ba-aretz-covenant-walking` entry's forward
  scope** (Josh 1:3, 18:8, Deut 11:24) is **not** in `appliesTo[]`.
  Reviewer should confirm this is the right policy — the parallels
  are noted in the rationale but the `appliesTo[]` is held to verses
  in the currently-translated corpus.

- **The `elonei-mamre` entry is forward-loaded for the cycle.** The
  entry's `appliesTo[]` covers all 10 Mamre-site verses across
  Genesis, including verses (14:13, 14:24, 18:1, 23:17, 23:19, 25:9,
  35:27, 49:30, 50:13) that will be translated later. The
  forward-load is appropriate for a recurring proper-name site, but
  reviewer should confirm the policy.

- **No `claim_type=speculative` entries.** The chapter cleared
  without requiring human sign-off on speculative readings; this
  matches the chapter's pre-flagged non-high-lens-leverage character.

## Citations consulted

- BDB, *A Hebrew and English Lexicon of the Old Testament* (1907)
  — *elon* / *elah* / *alon* lexical entries; *naga* / *nega*
  entries
- HALOT, *The Hebrew and Aramaic Lexicon of the Old Testament*
  (Koehler-Baumgartner, ET 1994–2000) — *elon* / *elah* distinction;
  *chata* + *l-* dative construction
- Cassuto, *A Commentary on the Book of Genesis*, vol. II (1944
  Hebrew / 1961 ET) — pre-conquest reading of the
  Canaanite-Perizzite parenthetical
- Daube, *Studies in Biblical Law* (1947) — §3 on the
  walking-the-land covenant-possession rite (*Begehungsritus*)
- Speiser, *Anchor Bible Genesis* (1964) — Documentary-Hypothesis
  reading of the parentheticals; dative-l with *chata*; covenant-
  walking rite
- von Rad, *Genesis* (1972 ET) — Eden / Sodom typology at 13:10
- Westermann, *Genesis 12–36*, Hermeneia (1985 ET) — Eden allusion
  at 13:10; *sa eynekha* formulaic character; Mamre site aetiology
- Wenham, *WBC Genesis 1–15* (1987) — context-specific reading of
  the Canaanite-Perizzite parenthetical; covenant-walking rite
- Sarna, *JPS Torah Commentary: Genesis* (1989) — Eden allusion;
  seed-comparison triad; covenant-walking rite; Mamre as Amorite
  contemporary
- Hamilton, *NICOT Genesis 1–17* (1990) — Eden allusion; dust-image
  as Gen 2:7 / 3:19 creation-recall; *sa eynekha* as
  threshold-of-vision marker
- Alter, *The Five Books of Moses* (2004) — Eden allusion at 13:10;
  seed-comparison triad; *sa eynekha* across the patriarchal arc
- Kitchen, *On the Reliability of the Old Testament* (2003) —
  pre-conquest reading of the parentheticals
- Gunkel, *Genesis* (1901) — classical source-critical reading of
  the parentheticals
- Wellhausen, *Prolegomena zur Geschichte Israels* (1883) — J-stratum
  foundational treatment
