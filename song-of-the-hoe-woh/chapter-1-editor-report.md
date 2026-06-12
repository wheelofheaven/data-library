# Chapter 1 Editor Report — The Song of the Hoe (ETCSL 5.5.4)

**Book:** `song-of-the-hoe-woh` · **Chapter:** 1 (110 lines, composition 1)
**Editor pass:** claude-opus-4-8 (editor), 2026-06-12
**Status advanced:** `draft` → `editor-review` · **Version:** `1.0.0-draft` → `1.0.0-rc1`
**Overlay glossary:** `0.1.0` → `1.0.0` (11 entries added; semver-minor base bumped to 1.0.0 as the first populated release per the seed's planned trajectory)

This report is for the human Reviewer. It enumerates the editorial
decisions, the new glossary entries (with claim_type counts), and —
most importantly — the open cruxes and the lines where the lens reach
was deliberately held to the apparatus. **There are no
`claim_type=speculative` entries in this pass** (see the dedicated
section below confirming that and explaining why).

---

## Headline numbers

- **Editorial questions resolved:** 20 of 20 (the `editorial_questions[]`
  array is now empty). Every question was either (a) folded into a new
  overlay glossary entry with `appliesTo` pointing at the governing
  refIds, (b) resolved into per-line commentary citing the relevant
  central entry, or (c) escalated as an open crux below.
- **Lines with new commentary:** 29 of 110 (the divergent /
  interpretively-loaded lines; the remaining 81 are either routine
  catalogue members carrying only a `glossaryRefs` attachment, or lines
  where the Translator's draft matches the standard ETCSL reading and
  needs no apparatus).
- **Overlay glossary entries added:** 11.
  - **`direct`: 4** — `al-paronomasia-hoe-syllable-whole-composition-convention`,
    `al-gishal-hoe-mattock-brick-mould-lexeme`,
    `shu-giri-nose-hand-to-nose-obeisance-idiom`,
    `nunamnir-enlil-epithet-leader-of-heaven-and-earth`.
  - **`inferred`: 7** — `al-tar-hoe-wielder-construction-work-pun-lexeme`,
    `uzu-ea-uzu-mua-where-flesh-came-forth-human-emergence-place`,
    `dur-an-ki-bond-of-heaven-and-earth-bulug-axis`,
    `sag-namluulu-ushub-brick-mould-human-prototype`,
    `numun-kalam-ma-seed-of-the-land-human-germination`,
    `ninmena-birth-goddess-epithet-crown-lady`,
    `al-initial-technical-noun-catalogue-vv83-93`.
  - **`speculative`: 0.**
- **Central glossary changes:** none. All new entries went to the
  per-book overlay per the infrastructure constraint; existing central
  entries are referenced by id only.
- **`i18n.en` text changes:** none of substance. No translated line was
  altered to fit the Wheel of Heaven lens. The draft's renderings were
  accurate; the Editor pass added apparatus (commentary + glossary)
  and `glossaryRefs`, leaving the English as a defensible scholarly
  rendering.

---

## Speculative entries requiring sign-off

**None.** This pass produced zero `claim_type=speculative` entries, by
design. The lens-relevant material in this composition — the
human-creation cluster (Uzu-ea/Uzu-mua, the brick-mould prototype, the
seed-and-germination motif) and the humans-relieve-divine-toil topos —
is real and is documented, but every reading rests on **named
Sumerological scholarship and is `inferred` at most**, not project-
specific synthesis that goes beyond what any source attests.

Concretely, the four places a careless pass might have over-reached,
and why each is `inferred` not `speculative`:

1. **Uzu-ea / Uzu-mua = the human-emergence place, with a Genesis 2:7
   comparandum.** The toponym is *self-glossing* in the manuscripts
   (`uzu` 'flesh' + e3/mu2 'came-forth/grew'); the identification as the
   emergence-site rests on the Nippur cosmographic tradition (Jacobsen,
   Kramer). The `ʾāḏām/ʾăḏāmâ` comparison is a *reasonable comparative
   reading* (Westermann; Lambert 1965), explicitly held to commentary
   and never asserted in `i18n.en`. → `inferred`.
2. **The brick-mould as the human-creation matrix.** The hymn *itself*
   equates hoe, brick-mould, and the making of mankind at line 96
   (`^ĝišal u3-šub-ba ^ĝišal saĝ ĝal2-la-am3`) — so reading line 19's
   `u3-šub` as the human-prototype mould is textually warranted, not
   speculative. The cross-corpus clay-creation comparanda (Enki and
   Ninmah; Atraḫasīs I; Gen 2:7) are comparative, held to commentary.
   → `inferred`.
3. **The seed/germination-of-humankind motif.** `numun` = 'seed' and
   `dar` = 'break through' are direct lexical facts; that the passage
   portrays *humankind* germinating is the consensus reading resting on
   construing the unstated collective as the human-stock. → `inferred`.
4. **Humans created to relieve the gods' toil.** Documented at line 31
   via the central `du-lum-dullu-divine-toil-relieved-by-humans-cross-corpus`;
   the topos is explicit in Enki and Ninmah and Atraḫasīs but is a
   *comparative* reading of *this* text's `šukur2` provisioning line.
   → `inferred`.

**No sign-off is technically blocked by a speculative entry.** The
Reviewer should nonetheless confirm the four `inferred` readings above
are pitched at the right epistemic level for the project, since they
are the lens-bearing readings of the composition.

---

## Unresolved editorial questions / open cruxes

These are decisions the Editor made a defensible call on but which a
human Reviewer should eyeball, either because the source is damaged or
because the sense is genuinely obscure.

### `SOTH-WOH-1:81-82` — the "sons of the hoe" couplet

**Issue:** `ḫul-ĝal2 ud nu2-a dumu ^ĝišal-me-eš / u4-sa2 dug4-ga-ta
an-ta u3-tud-de3-eš`. The "evil ones who lie about in the daylight are
sons of the hoe, born from heaven after sleep had been spoken of."
The syntax of "sleep having been spoken" is uncertain; the couplet is
semantically opaque even in the standard editions.
**Options considered:** literal rendering (taken); ETCSL's smoothing
"born in sleep from heaven"; mark `(?)` for unresolved sense.
**Why escalating:** No reading is secure. The WoH translation keeps a
literal-as-possible rendering and the line-81 commentary flags the
obscurity. No glossary entry was created for a passage this insecure.
**Recommendation:** ship as-is with the obscurity flagged; revisit if a
better join of the witnesses surfaces.

### `SOTH-WOH-1:95` — damaged second-hemistich variant

**Issue:** principal `sa-par4-am3` ('a hunting-net') vs the damaged
witness `/šabra\-[…]` ('an overseer …'), with both the `/…\` damage
marker and the `[…]` lacuna present in the source.
**Options considered:** principal + partial variant (taken); lead with
the `šabra` 'overseer' variant; mark `(?)`.
**Why escalating:** the variant is only partially legible; the
reconstruction is not certain. Both the manuscript-variant and
lacuna/damage conventions are applied; the gap is preserved, not
filled.
**Recommendation:** ship; the damage is honestly represented.

### `SOTH-WOH-1:18 / 18A` — manuscript divergence around the brick-mould

**Issue:** the witnesses diverge on whether line 18 reads "at Uzu-ea he
set this very hoe to work" or "at Uzu-mua, the unassailable," and
line 18A (`uzu-mu2-a saĝ nu-ĝa2-ĝa2-de3`) is present in only some
witnesses. The composite is genuinely uneven here.
**Why escalating:** this is the immediate run-up to the human-creation
line (19); the Reviewer should confirm the inline variant rendering
reads cleanly and that the 18A purpose-clause is correctly subordinated.
**Recommendation:** ship; variants preserved per convention.

### `al-tar` line-44 agent-reading (`SOTH-WOH-1:44`)

**Issue:** ETCSL marks "hoe-wielder" `(?)` at line 44; the
overlay entry `al-tar-hoe-wielder-construction-work-pun-lexeme` is
`inferred` precisely because of this. The same word is rendered
"construction-work" at 45/47/48/54/55/57/58/60 and adjectivally
"mighty" at 47.
**Why noting:** the context-split of a single lexeme into three English
values is an editorial reading of the syntax, not a lexicon-fixed fact.
**Recommendation:** ship; the uncertainty is recorded in the entry and
the line-44 commentary.

---

## Resolved questions → where each landed

| Original question (refId) | Resolution |
|---|---|
| whole-composition `/al/` paronomasia | → overlay `al-paronomasia-...` (`direct`); ETCSL parenthetical convention ruled in; commentary at line 8 |
| `:6 / 18 / 18A` Uzu-ea/Uzu-mua | → overlay `uzu-ea-uzu-mua-...` (`inferred`); commentary at line 6; Gen 2:7 comparison held to apparatus |
| `:3` numun "seed of the Land" | → overlay `numun-kalam-ma-...` (`inferred`); commentary at lines 3, 20 |
| `:7` Dur-an-ki / bulug | → overlay `dur-an-ki-...` (`inferred`); commentary at line 7 |
| `:19 (+18A)` brick-mould prototype | → overlay `sag-namluulu-ushub-...` (`inferred`); commentary at lines 18A, 19, 96 |
| `:20-21` germination from soil | → folded into `numun-kalam-ma-...`; commentary at line 20 |
| `:8` ud al-e3 / day-vs-storm | → resolved in commentary (line 8); ETCSL "daylight" taken; day/storm ambiguity flagged at 36/47/59/62/81 |
| `:23` hand-to-nose obeisance | → overlay `shu-giri-...` (`direct`); cross-refs central prostration entry; commentary line 23 |
| `:27` Ninmena | → overlay `ninmena-birth-goddess-epithet-crown-lady` (`inferred`); cross-refs central birth-goddess cluster; commentary line 27 |
| `:28` Nunamnir | → overlay `nunamnir-enlil-epithet-...` (`direct`); commentary line 28 |
| `:31 / 43` rations / me | → line 31 commentary cites central `du-lum-dullu-...` (toil-relief); line 43 cites central `me-...`; no new overlay lexeme (topos covered centrally) |
| `:44-45` al-tar pun-lexeme | → overlay `al-tar-...` (`inferred`); commentary line 44 |
| `:50` wild-cow / woman | → resolved in commentary (line 50); principal `immal2` taken, variant preserved; composition-local, no entry |
| `:81-82` obscure couplet | → commentary (line 81) + escalated above |
| `:74-75 / 79-80` burial & occupational titles | → commentary at lines 74, 79; composition-local metaphors, no entries; Enkidu-ghost allusion noted |
| `:51 / 83-93` technical al-noun catalogue | → overlay `al-initial-technical-noun-catalogue-vv83-93` (`inferred`); commentary at lines 51, 83 |
| `:71-72` al-gar-sur instrument | → folded into the technical-catalogue entry; commentary line 71 |
| `:95` damaged variant | → commentary (line 95) + escalated above |
| `:78` gašam plus + oar/hoe pun | → resolved in commentary (line 78); added word kept as variant; oar/hoe homophony glossed |
| `:17` ki-in-du / crown of earth | → resolved in commentary (line 17); "crown of earth" taken; minor construal crux, no entry |

---

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

- **No additions, no modifications.** All cross-corpus lemmas the
  chapter relies on already exist centrally and are referenced by id:
  `digir-...`, `nam-...`, `kalam-...`, `nam-lu2-ulu3-...`,
  `sag-gig-ga-...`, `me-...`, `abzu-engur-...`,
  `du-lum-dullu-...`, `an-enlil-nudimmud-...`,
  `nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-...`,
  `giri-ki-su-ub-appa-labanu-prostration-gesture-...`,
  `za-mi-...`, `ekur-...`, `utu-shamash-...`,
  `anuna-...`, `nibru-...`,
  `five-antediluvian-cities-...`, plus the four project conventions
  (DINGIR-drop, manuscript-variant, lacuna-bracket, proper-name).

**Two deliberate non-promotions the Reviewer may want to revisit later:**

1. **Ninmena → central birth-goddess cluster.** I recorded Ninmena in
   the overlay (`ninmena-birth-goddess-epithet-crown-lady`) and
   cross-referenced the central cluster
   `nintur-nintud-ninhursaga-birth-goddess-epithet-cluster-cross-corpus`
   rather than adding "Ninmena" to that central entry's name-list.
   Rationale: Ninmena is a single-text epithet here. If Ninmena recurs
   in a later composition, promote it into the central cluster's
   `source`/`appliesTo`. (Editor's call; flagged for awareness.)
2. **Nunamnir → central Enlil/triad entry.** Recorded in the overlay
   (`nunamnir-enlil-epithet-leader-of-heaven-and-earth`); not added to
   `an-enlil-nudimmud-cosmic-triad-cross-corpus` (which fixes on the
   Enki by-name Nudimmud). Same recurrence-criterion applies. The
   Nunamnir = Enlil equation is uncontested, hence the overlay entry is
   `direct`.

### Per-translation overlay (`data-library/song-of-the-hoe-woh/_translation-glossary.json`)

Version `0.1.0` → `1.0.0`; `scopeNote` updated to describe the
populated state. **11 entries added** (4 `direct`, 7 `inferred`, 0
`speculative`):

- Added: `al-paronomasia-hoe-syllable-whole-composition-convention` (`direct`)
- Added: `al-gishal-hoe-mattock-brick-mould-lexeme` (`direct`)
- Added: `al-tar-hoe-wielder-construction-work-pun-lexeme` (`inferred`)
- Added: `uzu-ea-uzu-mua-where-flesh-came-forth-human-emergence-place` (`inferred`)
- Added: `dur-an-ki-bond-of-heaven-and-earth-bulug-axis` (`inferred`)
- Added: `sag-namluulu-ushub-brick-mould-human-prototype` (`inferred`)
- Added: `numun-kalam-ma-seed-of-the-land-human-germination` (`inferred`)
- Added: `shu-giri-nose-hand-to-nose-obeisance-idiom` (`direct`)
- Added: `ninmena-birth-goddess-epithet-crown-lady` (`inferred`)
- Added: `nunamnir-enlil-epithet-leader-of-heaven-and-earth` (`direct`)
- Added: `al-initial-technical-noun-catalogue-vv83-93` (`inferred`)

---

## Lens-discipline statement

Per the hard rules: **accuracy before the lens.** No `i18n.en` line was
altered to fit the Wheel of Heaven reading. The lens lives entirely in
the commentary and in the glossary rationales:

- The human-emergence cluster (Uzu-mua, brick-mould, seed/germination)
  is rendered in the English exactly as the Sumerian and the ETCSL
  reference support it ("flesh might sprout forth," "the first of
  humankind in the brick-mould," "his Land began to break up through
  the soil"). The *significance* — that this is a creation-from-
  earth-substance account comparable to Enki and Ninmah, Atraḫasīs, and
  Genesis 2:7 — is carried in commentary as an `inferred` comparative
  reading, never as an assertion in the text.
- The toponyms are rendered with their own self-glosses (the
  manuscripts translate themselves), not with any lens-loaded
  paraphrase. There is no "where humans were manufactured" or similar.
- The humans-relieve-divine-toil topos is named in commentary via the
  central toil-relief entry; the English ("to provide rations for the
  gods") is the plain reading.

A serious Sumerologist reading only the `i18n.en` column would find a
defensible scholarly translation of c.5.5.4. The lens is visible only
to a reader who opens the apparatus — which is exactly where it belongs.

---

## Recommended next steps for the Reviewer

1. Confirm the four lens-bearing `inferred` readings (Uzu-mua,
   brick-mould, germination, toil-relief) are pitched correctly.
2. Eyeball the two open damaged/obscure cruxes (`:81-82`, `:95`) and
   the `:18/18A` manuscript divergence.
3. Note the two non-promotions (Ninmena, Nunamnir) for the central
   glossary's future recurrence-driven maintenance.
4. On sign-off, advance `translation.status` past `editor-review`.
