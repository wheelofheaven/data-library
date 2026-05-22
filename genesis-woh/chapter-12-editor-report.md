# Chapter 12 Editor Report

## Summary

- **Chapter:** Genesis 12 — The call of Abram and the descent to Mitsrayim
- **Translator draft:** 20 verses, version 0.1.0-draft, 13 editorial_questions[] flagged
- **Editor output:** all 13 questions resolved, 13 new glossary entries added,
  commentary written for 14 of 20 verses (vv 1, 2, 3, 5, 6, 7, 8, 9, 10, 11,
  13, 15, 16, 17, 18, 20 — i.e., every divergent or keystone verse; the
  remaining six verses — 4, 12, 14, 19 — are routine narrative-bridge and
  receive no commentary).
- **Status advanced:** draft → editor-review
- **Version advanced:** 0.1.0-draft → 1.0.0-rc1
- **Glossary pinned version:** 2.8.0 → 2.9.0
- **Speculative entries requiring human sign-off:** **none**.

The chapter is not high-lens-leverage. The Wheel of Heaven posture has been
held measured throughout, surfacing only at vv 7 (first patriarchal
theophany) and 17 (the divine affliction of Pharaoh's house) to note
continuity with the divine-descent register of chs 1-11 without
editorializing on cosmology. The translation reads as a defensible
scholarly rendering aligned with ASV register, with two close-readings to
the modern critical consensus (NJPS, Sarna, Alter) surfaced in commentary
rather than imposed on the English.

## Speculative entries requiring sign-off

**None.** No entry in this chapter rises to `claim_type=speculative`.
Every new entry is either `direct` (8 entries) or `inferred` (5 entries);
the `inferred` entries are all grounded in well-attested modern critical
scholarship and identified in their rationale by named scholarly works.
No reading goes beyond what major scholars argue.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

Bumped v2.8.0 → v2.9.0 (semver-minor, additions only — no modifications
to existing entries). Updated `scopeNote` to document the patriarchal-
narratives opening.

**13 entries added** (all cross-corpus or chapter-keystone; per the
"overlay vs. central" rule, all 13 govern lemmata that recur across
Genesis or beyond, so all go to central):

| ID | claim_type | Governs | Source |
|---|---|---|---|
| `lekh-lekha` | direct | Gen 12:1, 22:2 | doubled imperative + ethical dative; the Abraham-cycle inclusio |
| `nivrakhu-bekha-niphal-hithpael` | direct | Gen 12:3, 18:18, 22:18, 26:4, 28:14 | the niphal/hithpael blessing-form dispute across five verses |
| `nefesh-asher-asu` | direct | Gen 12:5 | proselytes-made vs. slaves-acquired three-way dispute |
| `elon-moreh` | inferred | Gen 12:6 | sacred-tree-oracle site reading |
| `va-yera-yhwh-theophany` | direct | Gen 12:7, 17:1, 18:1, 26:2, 26:24, 35:9, 48:3 | patriarchal theophany-formula |
| `zera-eretz-promise` | direct | Gen 12:7 + 11 other patriarchal-promise verses | seed-land covenant-nucleus |
| `qara-b-shem-yhwh` | direct | Gen 4:26, 12:8, 13:4, 21:33, 26:25 | calling on the name of YHWH at altars |
| `wife-sister-type-scene` | inferred | Gen 12:10-20, 20:1-18, 26:1-11 (40 verses) | Alter 1981's type-scene framing |
| `eshet-yefat-mareh` | direct | 13 verses across Genesis, Samuel, Kings, Esther | beautiful-woman formula |
| `imri-na-achoti-at` | direct | Gen 12:13, 20:2, 20:12, 26:7 | say-sister strategy + ethics dispute |
| `camel-anachronism` | inferred | Gen 12:16, 24:10-11, 24:64, 30:43, 31:17, 32:8, 32:16, 37:25 | Sapir-Hen & Ben-Yosef 2013 archaeological consensus |
| `nega-pharaoh-proto-exodus` | inferred | Gen 12:17 | proto-Exodus plague-formula typology |
| `va-y-shalchu-expulsion` | inferred | Gen 12:20 | Abram-Pharaoh / Moses-Pharaoh expulsion verb |

### Per-translation overlay

**No overlay file created.** All 13 entries are either cross-corpus (recur
across Genesis or into the Prophets / Writings) or encode project-wide
conventions about the patriarchal cycle, so all go to central per the
Editor brief's "overlay vs. central" rule.

### Modifications to existing entries

**None.** No existing entry was modified. The two glossary entries already
applied by the Translator (`eretz`, `mitsrayim`) remain unchanged.

## Editorial decisions resolved

All 13 of the Translator's `editorial_questions[]` were resolved as
follows:

### `GEN-WOH-12:1` — *lekh-lekha*

**Translator default:** "Go forth" (option 2).
**Editor decision:** Confirmed. Created glossary entry `lekh-lekha`
recording the ethical-dative philological question and the 12:1 / 22:2
inclusio. Translation text unchanged from Translator default; commentary
expanded.

### `GEN-WOH-12:3` — niphal vs. hithpael of *barakh*

**Translator default:** "in you all the families of the ground shall be
blessed" (option 1 — passive, matching MT pointing at this verse).
**Editor decision:** Confirmed. The MT-preserving verse-by-verse approach
(Wenham, Hamilton) is the cleanest position: passive at 12:3 / 18:18 /
28:14 where MT is pointed niphal; middle/reflexive at 22:18 / 26:4 where
MT is pointed hithpael. Created glossary entry
`nivrakhu-bekha-niphal-hithpael` governing all five verses; commentary
expanded with the three-position dispute and the Pauline-reception
complication (Gal 3:8).

### `GEN-WOH-12:5` — *nefesh asher asu*

**Translator default:** "the souls that they had made in Haran" (option 1
— literal).
**Editor decision:** Confirmed. Created glossary entry `nefesh-asher-asu`
recording the three-way dispute (proselytes / slaves-acquired /
dependents). Translation preserves the literal *asu* (*made*) per the
oddness-preservation principle.

### `GEN-WOH-12:6` — *elon Moreh*

**Translator default:** "the oak of Moreh" (option 1 — ASV proper-name
reading).
**Editor decision:** Confirmed. Created glossary entry `elon-moreh`
recording the *moreh*-as-teacher / sacred-tree-oracle reading and the
broader patriarchal sacred-tree pattern (Shechem, Bethel, Ophrah).
Translation unchanged; the oracle resonance lives in commentary.

### `GEN-WOH-12:7` — *va-yera YHWH*

**Translator default:** "YHWH appeared to Abram" (option 1).
**Editor decision:** Confirmed. Created glossary entry
`va-yera-yhwh-theophany` governing the patriarchal-theophany formula
across 12:7, 17:1, 18:1, 26:2, 26:24, 35:9, 48:3. Translation unchanged;
the mode-of-seeing question is left for the explicit-embodiment moment at
18:1 (Mamre).

### `GEN-WOH-12:7` — *l-zarakha eten et-ha-aretz ha-zot*

**Translator default:** "To your seed I will give this land" (option 1).
**Editor decision:** Confirmed. Created glossary entry `zera-eretz-promise`
governing the bare nucleus of the patriarchal land-promise and its 11
expansions across the patriarchal cycle.

### `GEN-WOH-12:8` — *qara b'shem YHWH*

**Translator default:** "called on the name of YHWH" (option 1, matching
ASV and the rendering used at 4:26).
**Editor decision:** Confirmed. Created glossary entry `qara-b-shem-yhwh`
governing the cult-site-invocation formula at 4:26, 12:8, 13:4, 21:33,
26:25. Translation unchanged.

### `GEN-WOH-12:10` — *va-yered Avram Mitzrayma* and the type-scene

**Translator default:** "Abram went down to Mitsrayim".
**Editor decision:** Confirmed. The translation question is uncontested
(the verb is *yarad*; the geographical idiom is fixed). Created glossary
entry `wife-sister-type-scene` governing all 40 verses of the three
instances at Gen 12, 20, 26. The Alter 1981 framing is identified as
inferred (a 20th-century literary-critical synthesis), not direct.

### `GEN-WOH-12:11` — *ishah yefat-mar'eh*

**Translator default:** "a woman beautiful of appearance" (literal,
preserves the formula).
**Editor decision:** Confirmed. Created glossary entry `eshet-yefat-mareh`
governing 13 occurrences of the beautiful-woman / beautiful-man formula
across Genesis (Sarai, Rebekah, Rachel, Joseph), Samuel (David, Abigail,
Bathsheba, Tamar), Kings (Abishag), and Esther (Vashti, Esther).

### `GEN-WOH-12:13` — *imri-na achoti at*

**Translator default:** "Say, please, that you are my sister" (modern
register).
**Editor decision:** Confirmed. Created glossary entry `imri-na-achoti-at`
recording the say-sister strategy and the three-way ethics dispute
(morally-compromised / apologetic-rabbinic / defensive-tactical).
Translation unchanged; the chapter's textual silence on the strategy's
ethics is preserved.

### `GEN-WOH-12:16` — the camel anachronism

**Translator default:** "and camels" (the only viable translation
rendering).
**Editor decision:** Confirmed. Created glossary entry `camel-anachronism`
recording the Sapir-Hen & Ben-Yosef 2013 archaeological consensus and the
redaction-criticism implications. The entry's `appliesTo` lists all nine
patriarchal camel-mentions across Gen 12, 24, 30, 31, 32, 37 — this is a
recurring corpus-level issue and the central glossary entry will govern
each future occurrence.

### `GEN-WOH-12:17` — *va-y-naga YHWH*

**Translator default:** "great plagues" (matches ASV, preserves the
cognate link to Exodus).
**Editor decision:** Confirmed. Created glossary entry
`nega-pharaoh-proto-exodus` recording the proto-Exodus typology (Garbini,
Crüsemann, Sarna) and the verbal link to Exod 11:1.

### `GEN-WOH-12:20` — *va-y-shalchu*

**Translator default:** "and they sent him away" (matches ASV, preserves
the verbal link to Exod 12:33).
**Editor decision:** Confirmed. Created glossary entry
`va-y-shalchu-expulsion` recording the piel-*sh-l-ch* verbal link to Exod
6:1 / 11:1 / 12:33 and the proto-Exodus expulsion-structure parallel.

## Unresolved editorial questions

**None.** All 13 questions were resolved into glossary entries with
expanded commentary. No issue required escalation beyond the Editor's
authority.

## Translation choices flagged for Reviewer attention

The Reviewer should specifically check:

1. **The niphal/hithpael verse-by-verse approach at `nivrakhu-bekha`.**
   The decision to follow MT pointing rather than smoothing to a single
   reading (passive or middle) across all five verses commits the project
   to rendering 22:18 and 26:4 with the middle/reflexive 'shall bless
   themselves' when those chapters are translated. The decision is
   defensible (Wenham 1994, Hamilton 1990) but it does have downstream
   implications. If the Reviewer or human sign-off prefers a single
   consistent rendering (either all-passive following Paul/ASV, or
   all-middle following NJPS/Sarna), the glossary entry would need to be
   modified before chs 18, 22, 26, 28 are translated. Flagged for explicit
   confirmation.

2. **The wife-sister type-scene's broad `appliesTo`.** The entry's
   `appliesTo[]` array covers 40 verses across Gen 12:10-20, 20:1-18,
   26:1-11. The Editor's reading is that the entry should govern all
   three instances so vocabulary remains type-scene-recognizable across
   the cycle. Reviewer should confirm this scope is appropriate, or
   narrow it to just the chapter-12 verses with a cross-reference at
   chs 20 and 26.

3. **The `imri-na-achoti-at` claim_type = direct** despite the entry
   covering an ethics dispute. The reasoning is that *both* the strategy
   itself *and* the three readings of it are uncontested facts of the
   text and the scholarly literature — presenting the dispute fairly is
   direct reporting, not interpretation. If the Reviewer prefers
   classifying ethics-disputes as `inferred`, the claim_type would
   shift; the rationale text would not need to change.

4. **The treatment of the proto-Exodus typology** at `nega-pharaoh-proto-exodus`
   and `va-y-shalchu-expulsion`. The classification as `inferred` (rather
   than `direct`) reflects the Editor's reading that the typology is a
   literary-critical *synthesis* across two passages rather than a claim
   made by either passage alone. The Reviewer may prefer to classify
   these as `direct` if the verbal parallels alone are taken as the
   evidence; the call is a judgment about what counts as direct.

5. **The chapter intentionally has no commentary at vv 4, 12, 14, 19.**
   These are narrative-bridge verses (Abram traveling at 75 years old;
   the Mitsrim seeing Sarai; Pharaoh's officers; Pharaoh's complaint).
   The Translator default text matches ASV closely and no philological
   choice is being made. Per the Editor brief's "Preserve the existing
   translation where the Translator was correct" principle, commentary
   is omitted. Reviewer should confirm that the no-commentary policy is
   appropriate for narrative-bridge verses or if a one-sentence
   contextual note would be preferred.

## Files modified

- `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-12.json`
  (status: draft → editor-review; version: 0.1.0-draft → 1.0.0-rc1;
  glossaryVersion: 2.8.0 → 2.9.0; editorial_questions: 13 → 0;
  commentary added to 14 verses; glossaryRefs updated on 11 verses)
- `/Users/zara/Development/github.com/wheelofheaven/data-content/i18n/translation-glossary.json`
  (version: 2.8.0 → 2.9.0; scopeNote updated; 13 new entries appended;
  total entries: 247 → 260)

## Next pipeline step

Hand off to Reviewer for final philological audit and human sign-off
before `translation.status` advances to `stable`.
