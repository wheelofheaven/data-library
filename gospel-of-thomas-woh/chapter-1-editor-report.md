# Chapter 1 Editor Report — Gospel of Thomas, Block A (incipit and logia 1-38)

## Overview

This is the program's first Coptic-source text.
Block A covers the incipit (THOM-0) and logia 1-38 of Nag Hammadi Codex II,2, 39 paragraph objects.
Blocks B (39-76) and C (77-114) follow, and every convention below binds them.

The Translator submitted **49 editorial_questions[]**.
This pass resolves all 49 and clears the array.
Four rulings are flagged below for human review, and one speculative overlay entry needs sign-off by name.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.overlayGlossaryVersion`: new, `1.0.0`
- `translation.glossaryVersion`: `2.74.0`, unchanged (the central file was not touched)
- `translation.modelDrafts`: editor appended
- `_meta.json`: not touched; `source-cop-1.json`: not touched

**Commentary.** Written to `notes: {"official": …, "community": []}` in the program's format.
37 of 39 paragraphs carry commentary.
THOM-34 and THOM-35 have none: they are short synoptic parallels with no divergence or source issue.

**English changes.** Six paragraphs changed, each governed by an overlay entry:

| refId | Draft | Now | Entry |
|---|---|---|---|
| THOM-3 | 'the kingdom is in heaven' … 'the birds of heaven' | 'the kingdom is in **the sky**' … 'the birds of **the sky**' | `tpe-sky-heaven-context-rule-thomas-woh` |
| THOM-9 | 'ears toward heaven', 'fruit up toward heaven' | 'toward **the sky**' (×2) | same |
| THOM-20 | 'the birds of heaven' | 'the birds of **the sky**' | same |
| THOM-12 | 'Wherever you have come, you will go to James' | 'Wherever you have come **to**, you **are to** go to James' | `iakobos-pdikaios-james-the-righteous-thomas-woh` |
| THOM-21 | 'his house of his kingdom'; 'they will find.' | 'his house of his **domain**'; 'they will find **it**.' (also 'watching **out** for') | `mntero-the-kingdom-thomas-woh`; `logion-21-robbers-clause-and-chreia-thomas-woh` |
| THOM-33 | 'under a basket' | 'under a **measure**' | `other-ear-and-maaje-measure-logion-33-thomas-woh` |

Every other line keeps the Translator's draft, which was accurate.
No line was harmonised toward the synoptic gospels.
The hard sayings keep the manuscript reading: 7 (the lion), 21 (the robbers clause), 30 (three gods) and 37.

---

## Rulings on the 49 editorial questions

| # | refId | Question | Ruling | Overlay entry (claim_type) |
|---|---|---|---|---|
| 0 | 0 | Central entries; 'cop' | Overlay opened. Central changes proposed below: add `cop`; extend `iēsous…` (35 units), `kingdom-of-heaven…` (THOM-20) and `lacuna-bracket…` (5 units). Do **not** extend `beatitudes…` or `parable-of-the-sower…`. | see CENTRAL |
| 1 | 0 | ϣⲁϫⲉ ⲉⲑⲏⲡ | 'the hidden sayings' kept. ϣⲁϫⲉ = 'sayings' for the collection and 'words' in narrative; ϩⲏⲡ = 'hidden' everywhere. | `shaje-ethep-hidden-sayings` (direct) |
| 2 | 0 | ⲉⲧⲟⲛϩ capitals | Lower case throughout, including 'the son of the living one' (37). | `etonh-the-living-lowercase` (direct) |
| 3 | 0 | Didymos Judas Thomas | Kept. The Greek form is 'Didymos', and neither by-name is translated. | `didymos-judas-thomas-name` (direct) |
| 4 | 0 | Nomina sacra | Expanded silently and recorded as an overlay convention. | `nomina-sacra-and-abbreviation-expansion-convention` (direct) |
| 5 | 0 | Greek loanwords | Translated, never transliterated; meaningful loan/native pairs are recorded in the apparatus. | `greek-loanword-rendering-convention` (direct) |
| 6 | 0 | Greek incipit | Coptic in the line; the Greek is in commentary. | `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention` (direct) |
| 7 | 1 | Speaker of 'And he said' | Ambiguity preserved. | `register-sayings-format-and-proper-names-convention` (direct) |
| 8 | 1 | ϩⲉⲣⲙⲏⲛⲉⲓⲁ | 'interpretation' kept. | `hermeneia-interpretation` (direct) |
| 9 | 1 | 'taste death' | Kept at every occurrence. | `jitpe-mpmou-taste-death` (direct) |
| 10 | 2 | ⲡⲧⲏⲣϥ | 'reign over the All', with 'the All' capitalised here and at 67 and 77. | `ptirf-the-all-reign-over-the-all` (direct) |
| 11 | 2 | Greek vs Coptic | Coptic followed; 'rest' and Clement's form are given in commentary. | base-text convention (direct) |
| 12 | 3 | ⲧⲙⲛ̄ⲧⲉⲣⲟ | 'the kingdom'; 'the kingdom of the heavens' for the plural (central); later 'the kingdom of the Father'. | `mntero-the-kingdom` (direct) |
| 13 | 3 | ⲧⲡⲉ | **Changed.** 'sky' in physical contexts (3, 9, 20), keeping concordance within a saying; 'heaven' in cosmological ones (6, 11, 12); 'the heavens' for the plural. | `tpe-sky-heaven-context-rule` (**inferred**) |
| 14 | 3 | ϣⲏⲣⲉ | 'sons' in the filial formulas (Greek υἱοί); 'little child(ren)' for ϣⲏⲣⲉ ϣⲏⲙ. **For review:** see escalation 3. | `shere-son-child` (direct) |
| 15 | 3 | 'Father' capitals | Capitalised for the divine referent, lower case at 16 (matthew-woh precedent). | `eiot-father-capitalisation` (direct) |
| 16 | 3 | ⲙⲛ̄ⲧϩⲏⲕⲉ | 'poverty', paired with 'poor' at 54. | `mnthke-poverty` (direct) |
| 17 | 3 | Greek vs Coptic | Coptic followed; the five differences are in commentary. | base-text convention (direct) |
| 18 | 4 | ⲟⲩⲁ ⲟⲩⲱⲧ | 'a single one' / 'the single one'; plain 'one' for ⲟⲩⲁ (11, 22). | `oua-ouot-a-single-one` (direct) |
| 19 | 4 | ⲧⲟⲡⲟⲥ / ⲙⲁ | 'place' for both; 'the place of life'. | `topos-ma-place` (direct) |
| 20 | 4 | ⲣⲱⲙⲉ | The draft's context-dependent mix is kept, with generic 'man' as the base (matthew-woh). | `rome-man-human-person` (direct) |
| 21 | 4 | Greek 'and the last first' | Coptic followed; the Greek is in commentary. | base-text convention (direct) |
| 22 | 5 | Greek 'buried … raised' | Coptic followed; the Greek is in commentary. | base-text convention (direct) |
| 23 | 6 | Greek vs Coptic | Coptic followed; 'in the sight of heaven' keeps 'heaven'. | base-text convention; `tpe-…` |
| 24 | 7 | Lion crux | **Manuscript reading kept** ('the lion will become human'); the emendation is in commentary; 'loathsome'. | `lion-and-man-logion-7-manuscript-reading` (direct) |
| 25 | 8 | Restoration convention | Proposal (a)+(b)+(c) adopted; details under Conventions. | `restored-text-bracket-and-sigla-convention` (direct) |
| 26 | 9 | Sower | 'Behold, the sower went out' kept from matthew-woh, with Thomas's soils kept. The central sower entry is **not** applied. | `sower-parable-coptic-form-and-eisheete-behold` (direct) |
| 27 | 10 | ⲕⲟⲥⲙⲟⲥ / ⲕⲁϩ | 'the world' / 'the earth', 'the soil'; 'keep watch against the world'. | `kosmos-world-kah-earth` (direct) |
| 28 | 11 | Light; subject in 24 | 'he gives light', with 'it' given in commentary. | `ouoein-light-man-of-light` (direct) |
| 29 | 12 | James | 'James the Righteous'. **Changed:** 'Wherever you have come to, you are to go' (focalising future). | `iakobos-pdikaios-james-the-righteous` (**inferred**) |
| 30 | 13 | Logion 13 vocabulary | 'Teacher', 'righteous angel', 'wise philosopher', 'measured out', 'wholly unable' all kept. | `logion-13-sah-angelos-pege-vocabulary` (direct) |
| 31 | 14 | ⲡⲛⲉⲩⲙⲁ | Lower case 'spirit'; 'flesh' ≠ 'body'; 'wonder' / 'marvel'. | `pneuma-sarx-soma-spirit-flesh-body` (direct) |
| 32 | 15 | 'not born of woman' | Kept. | `jpo-not-born-of-woman` (direct) |
| 33 | 16 | ⲙⲟⲛⲁⲭⲟⲥ | 'as solitary ones', kept distinct from ⲟⲩⲁ ⲟⲩⲱⲧ. | `monachos-solitary` (**inferred**) |
| 34 | 18 | ⲁⲣⲭⲏ / ϩⲁⲏ | 'the beginning' / 'the end'. | `arche-hae-beginning-end` (direct) |
| 35 | 19 | Paradise | 'five trees in Paradise' kept. | `five-trees-in-paradise` (direct) |
| 36 | 21 | ⲙⲁⲣⲓϩⲁⲙ | 'Mariham'; the identification is in commentary. | `mariham-name` (direct) |
| 37 | 21 | 'house of his kingdom' | **Changed** to 'his house of his domain' (Lambdin); the lexical identity is in commentary. | `mntero-the-kingdom` (direct) |
| 38 | 21 | Robbers clause | Negative sense kept, without brackets. **Changed:** 'they will find it'. | `logion-21-robbers-clause-and-chreia` (**inferred**) |
| 39 | 22 | ϩⲓⲕⲱⲛ | 'an image in place of an image'; 'being nursed'. | `eikon-image` (direct) |
| 40 | 24 | ⲧⲥⲉⲃⲟ | 'Show us the place' kept. | `topos-ma-place` (direct) |
| 41 | 25 | ⲯⲩⲭⲏ | 'soul' at both occurrences; the reflexive idiom is in commentary. | `psyche-soul` (direct) |
| 42 | 27 | No intro; Sabbath | No 'Jesus said' supplied; 'fast from the world'; 'keep the Sabbath as Sabbath'; 'the kingdom'. | `logion-27-fast-from-the-world-sabbath-as-sabbath` (direct) |
| 43 | 30 | Three-gods crux | **Manuscript reading kept**; the Greek and the emendations are in commentary. | `three-gods-logion-30-manuscript-reading` (direct) |
| 44 | 31 | 'village' | Kept (Coptic). | base-text convention (direct) |
| 45 | 33 | Other ear; ⲙⲁⲁϫⲉ | Manuscript sequence kept. **Changed:** 'under a measure' (keeps the ear/measure pun). | `other-ear-and-maaje-measure-logion-33` (**inferred**) |
| 46 | 36 | Short vs long form | Coptic followed; the long Greek is in commentary. | base-text convention (direct) |
| 47 | 37 | 'son of the living one' | Lower case. | `etonh-the-living-lowercase` (direct) |
| 48 | 38 | Greek scraps | Coptic followed. | base-text convention (direct) |

All overlay ids carry the suffix `-thomas-woh`; it is omitted in the table.

---

## Conventions for Blocks B and C (binding)

1. **Register.** Modern English as in matthew-woh.
   Each saying begins 'Jesus said:' with a colon and no quotation marks around the saying; quoted speech inside it takes single quotes.
   No introductory formula is supplied where the Coptic lacks one.
   The sayings keep their terseness, and the line is never harmonised to the synoptics.
2. **Base text.** The English translates the Coptic of NHC II,2.
   The Greek of P.Oxy. 1/654/655 goes in commentary only, with restored Greek labelled as restored.
   In Block C this covers logion 77b in P.Oxy. 1, joined to 30.
3. **Restored text.**
   - **[ ]** encloses any English word whose Coptic token is wholly or partly restored inside [ ] in the source.
   - **⟨ ⟩** and **( )** source sigla (scribal omissions, abbreviations) are rendered silently in the English and noted in commentary where relevant.
   - **{ }** scribal surplus is dropped silently and noted in commentary if it is significant.
   - **…** marks an unrestorable gap.
   - English **⟨ ⟩** is reserved for English words the Editor supplies where no Coptic wording exists. It is not used in Block A.
   - **(?)** after a word marks a reading kept from the reference for a term of uncertain meaning, as in vendidad-woh. It is not used in Block A.
4. **Nomina sacra and overlined contractions** are expanded silently. The `text` field keeps the overlines.
5. **Greek loanwords** are translated, never transliterated.
6. **Cruxes.** The manuscript reading stands in the line. Emendations, and the Greek where it exists, go in commentary.
7. **Fixed renderings carried forward:**
   - 'the kingdom'; 'the kingdom of the Father'; 'the kingdom of the heavens' (54, 114)
   - 'the All' (67, 77)
   - 'will not taste death' (85, 111)
   - 'solitary ones' (49, 75)
   - 'image(s)' (50, 83, 84)
   - 'the living one', lower case (52, 59, 111)
   - 'poor' / 'poverty' (54)
   - 'Mariham' (114)
   - 'the Son of Man' at 86, under the central `son-of-man-…` convention, to be checked when Block C is drafted
   - 'Blessed is/are' (54, 58, 68, 69, 103), with the synoptic-parallel beatitudes proposed for the central beatitudes entry
   - ⲧⲡⲉ by the sky/heaven context rule
   - 'Father' capitalised for the divine referent

---

## Greek vs Coptic (Block A)

| Logion | Greek witness | Material divergence | Treatment |
|---|---|---|---|
| incipit | P.Oxy. 654.1-3 | Greek 'secret' (restored); 'Judas who is also Thomas' without Didymos; 'spoke' | Coptic; commentary |
| 1 | 654.3-5 | Agreement (speaker equally open) | Coptic |
| 2 | 654.5-9 | Greek: amazed → reign → **rest**; no 'troubled', no 'over the All' | Coptic; commentary (+ Clement, Strom. 2.9.45; 5.14.96) |
| 3 | 654.9-21 | 'under the earth' vs 'in the sea'; fish 'enter'; extra 'whoever knows himself will find it'; no 'you will be known'; 'kingdom [of God]' | Coptic; commentary |
| 4 | 654.21-27 | Greek adds 'and the last first' | Coptic; commentary |
| 5 | 654.27-31 | Greek adds 'nothing buried that will not be raised' | Coptic; commentary |
| 6 | 654.32-40 | 'How shall we fast?' vs 'Do you want us to fast?'; 'before the truth' vs 'in the sight of heaven' | Coptic; commentary |
| 7 | 654.40-42 | Traces only | Coptic (crux) |
| 24 | 655 frag. d | Traces only | Coptic |
| 26 | P.Oxy. 1.1-4 | End of saying; agreement | Coptic |
| 27 | 1.4-11 | Greek has 'Jesus says'; 'kingdom of God' | Coptic; commentary |
| 28 | 1.11-21 | Agreement ('in flesh', 'sons of men') | Coptic |
| 29 | 1.22 | End only ('this poverty') | Coptic |
| 30 | 1.23-30 | 'three … [gods/without God]' (restored); 'one alone'; stone/wood sentence (= Coptic 77b) | Coptic (crux); commentary |
| 31 | 1.30-35 | 'homeland' vs 'village' | Coptic; commentary |
| 32 | 1.36-41 | Agreement | Coptic |
| 33 | 1.41-42 | 'in your one ear' (rest lost) | Coptic; commentary |
| 36 | 655 i.1-17 | Greek much longer (food, lilies, stature, garment) | Coptic; commentary |
| 37 | 655 i.17-ii.1 | Broad agreement, fragmentary | Coptic |
| 38 | 655 ii.2-11 | Scraps; usual restoration agrees | Coptic |

---

## Source findings (source-cop-1.json stays immutable)

These are recorded in the commentary of the affected units, for whoever maintains the source pipeline.
None of them changes the English beyond following the corpus normalisation.

| refId | Finding |
|---|---|
| THOM-3 | Lemma aid counts 1 supplied span; `text` has no sigla. Diplomatic ⲉⲩϣⲁϫⲟⲟⲥ, normalised ⲉⲩϣⲁⲛϫⲟⲟⲥ (conditional ⲛ supplied but unmarked). |
| THOM-8 | Lemma aid counts 2 supplied spans; `text` shows 1 ([ⲡⲉ]). The normalisation also changes ⲁⲩⲟⲩⲱϩⲉ / ⲁⲩⲛⲟϭ to ⲉⲩ-. |
| THOM-10 | Lemma aid counts 1; `text` has none. Diplomatic ϯⲁⲣⲉϩ, normalised ϯϩⲁⲣⲉϩ. |
| THOM-14 | Stray ASCII apostrophe (U+0027) before ⲛ̄ⲧⲉⲧⲙ̄ⲙⲟⲟϣⲉ, apparently an encoding artefact (the file otherwise uses ⳿ U+2CFF). |
| THOM-18 | Lemma aid counts 1; `text` has none. Rasura in ⲥⲟⲩⲱⲛⲑϩⲁⲏ (Dilley 'ϩ rasura'); the normalised layer reads ⲥⲟⲩⲱⲛⲧϩϩⲁⲏ. Diplomatic ⲧⲛ̄ϩⲁⲏ, normalised ⲧⲉⲛϩⲁⲏ 'our end'. |
| THOM-22 | Lemma aid counts 6 supplied spans; `text` shows 2 ([ⲉⲧ], [ⲧⲉⲣ]). There is also a middle dot inside ⲙ̄ⲫⲟ·ⲟⲩⲧ. |
| THOM-32 | Diplomatic ⲁⲛ, normalised ⲟⲛ; the sense is unchanged. |

Recommendation (data maintainers, not this pass): check whether the diplomatic `orig_group` export drops the sigla of normalisation-only supplements at 3, 10 and 18. The source file should be re-fetched if so; it should not be hand-edited.

---

## Speculative entries requiring sign-off

### `woh-reading-kingdom-within-beginning-end-five-trees-thomas-woh` (overlay)

**Source:** Thomas 3 (the kingdom inside and outside you), 18 (where the beginning is, there the end will be), 19 (five trees in Paradise)

**WoH choice:** No effect on any English line.
The entry records three interpretive resonances:
- (3) self-knowledge as recognising oneself as a child of the creating Father, read alongside the canon's teaching that humans were made in the image of the Elohim;
- (18) the identity of beginning and end, read alongside the precessional cycle from which the project takes its name;
- (19) the five unchanging trees, read alongside the canon's reading of Eden as the Elohim's place of work.

**Why speculative:**
- None of the three sayings refers to the Elohim, to precessional ages or to a physical garden of the creators, and the canon does not cite these sayings.
- The resonances are a synthesis beyond any single source.
- The commentary at 3 states explicitly that the saying gives **no** support to a reading of the kingdom as a place in the sky.

**Recommendation:** ship as `speculative`, apparatus only. Each mention is one labelled paragraph ('Wheel of Heaven reading (interpretive; not part of the translation)') in the notes of THOM-3, 18 and 19.
If the founder prefers no lens in Thomas Block A, delete those three paragraphs and drop the id from three glossaryRefs. Nothing else depends on it.

---

## Unresolved editorial questions / decisions for review

None of the 49 questions is left open. The following rulings are judgement calls that the reviewer should confirm.

### `THOM-7` and `THOM-30` — manuscript reading kept at both cruxes

**Issue:** 'and the lion will become human' (7) and 'Where there are three gods, they are gods' (30) are widely suspected corruptions.
**Options considered:** (A) manuscript reading in the line with emendation in commentary (adopted); (B) emend in the line; (C) emend with ⟨ ⟩ marking.
**Why escalating:** (A) follows the brief and the program's crux rule, but popular translations often print the emendation at 7, so readers will notice the difference.

### `THOM-3` / `THOM-28` / `THOM-37` — 'sons' vs 'children' for ϣⲏⲣⲉ

**Issue:** ϣⲏⲣⲉ is common-gender.
'Sons' was chosen because the earlier Greek has υἱοί / υἱοῖς and matthew-woh uses 'sons of your Father'.
**Options considered:** 'sons' (adopted); 'children' (Patterson–Meyer).
**Why escalating:** this is a register policy question that also affects Blocks B and C (e.g. 50 'children of the light', 'children of the living Father').

### `THOM-33` — 'measure' diverges from matthew-woh 'basket'

**Issue:** Thomas's ϩⲁⲙⲁⲁϫⲉ is now 'under a measure', to keep the ear/measure pun, while Mt 5:15 has 'basket' in matthew-woh.
**Options considered:** 'measure' (adopted; `inferred`); 'basket' (matthew-woh harmony); 'bushel' (Lambdin/KJV).
**Why escalating:** this is a deliberate cross-text difference.

### `THOM-21` — robbers clause

**Issue:** The negative sense rests on reading ⲛⲉ as the negative optative ⲛ̄ⲛⲉ.
It is printed without brackets because the context makes it certain (`inferred`).
**Why escalating:** this is the only place in Block A where the English depends on an unmarked editorial reinterpretation of a converter.

---

## Glossary changes for review

### Central glossary

None written. All proposals are in the CENTRAL section below.

### Per-translation overlay (new file, v1.0.0, released 2026-10-31)

`gospel-of-thomas-woh/_translation-glossary.json`: **39 entries**: 33 `direct`, 5 `inferred`, 1 `speculative`.

- **Conventions (5, direct):** `register-sayings-format-and-proper-names-convention`, `restored-text-bracket-and-sigla-convention`, `nomina-sacra-and-abbreviation-expansion-convention`, `greek-loanword-rendering-convention`, `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention`
- **Lexical, direct (28):** `shaje-ethep-hidden-sayings`, `etonh-the-living-lowercase`, `didymos-judas-thomas-name`, `hermeneia-interpretation`, `jitpe-mpmou-taste-death`, `ptirf-the-all-reign-over-the-all`, `mntero-the-kingdom`, `shere-son-child`, `eiot-father-capitalisation`, `mnthke-poverty`, `oua-ouot-a-single-one`, `topos-ma-place`, `rome-man-human-person`, `makarios-blessed-singular-formula`, `lion-and-man-logion-7-manuscript-reading`, `sower-parable-coptic-form-and-eisheete-behold`, `kosmos-world-kah-earth`, `ouoein-light-man-of-light`, `logion-13-sah-angelos-pege-vocabulary`, `pneuma-sarx-soma-spirit-flesh-body`, `jpo-not-born-of-woman`, `arche-hae-beginning-end`, `five-trees-in-paradise`, `mariham-name`, `eikon-image`, `psyche-soul`, `logion-27-fast-from-the-world-sabbath-as-sabbath`, `three-gods-logion-30-manuscript-reading`
- **Inferred (5):** `tpe-sky-heaven-context-rule`, `iakobos-pdikaios-james-the-righteous`, `monachos-solitary`, `logion-21-robbers-clause-and-chreia`, `other-ear-and-maaje-measure-logion-33`
- **Speculative (1):** `woh-reading-kingdom-within-beginning-end-five-trees`

(All ids end in `-thomas-woh`.)
Indexing: the `strongs` field carries Crum, *A Coptic Dictionary* (1939) headwords. For Greek loans it also carries the Strong's G-number of the Greek word.

---

## CENTRAL — apply by orchestrator

Central v2.74.0 has no Coptic entries.
The proposals below add no new entries.
They add one source language and extend `appliesTo` on three existing entries: a semver-minor bump to **2.75.0**.
The chapter's glossaryRefs already cite the three extended ids.

### 0. Top-level

- Add `"cop"` to `sourceLanguages`, giving `["he","sux","akk","uga","arb","grc","ave","cop"]`.
- Add a scopeNote line: "v2.75.0: first Coptic-source references (Gospel of Thomas, NHC II,2, Block A); three existing Greek-NT/project entries extended to THOM refIds; Thomas-specific decisions live in the gospel-of-thomas-woh overlay."

### 1. EXTEND `appliesTo`

| Existing central id | Add to `appliesTo` | Reason |
|---|---|---|
| `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus` (direct) | `THOM-0`, `THOM-2`, `THOM-3`, `THOM-4`, `THOM-5`, `THOM-6`, `THOM-7`, `THOM-9`, `THOM-10`, `THOM-11`, `THOM-12`, `THOM-13`, `THOM-14`, `THOM-15`, `THOM-16`, `THOM-17`, `THOM-18`, `THOM-19`, `THOM-20`, `THOM-21`, `THOM-22`, `THOM-23`, `THOM-25`, `THOM-26`, `THOM-28`, `THOM-29`, `THOM-30`, `THOM-31`, `THOM-32`, `THOM-33`, `THOM-34`, `THOM-35`, `THOM-36`, `THOM-37`, `THOM-38` | Coptic ⲓ︤ⲥ︥ / ⲓⲏ︤ⲥ︥ is the nomen sacrum of Greek Ἰησοῦς, rendered 'Jesus' as in the entry. Optional note for the `source` field: "Coptic ⲓⲏⲥⲟⲩⲥ (nomen sacrum ⲓ︤ⲥ︥)". |
| `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim` (direct) | `THOM-20` | Coptic ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ keeps the plural, rendered 'the kingdom of the heavens' per the entry. Suggested sentence (optional; adding it is a rationale modification, so apply it at the next major bump or skip it): "The plural form also occurs in Coptic Thomas (logia 20, 54, 114), so it is not exclusively Matthean." Blocks B/C will add THOM-54 and THOM-114. |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (direct) | `THOM-8`, `THOM-16`, `THOM-22`, `THOM-29`, `THOM-37` | The Thomas overlay adopts the central [restoration] / ⟨supply⟩ distinction for Dilley's papyrological sigla. |

### 2. NOT extended, deliberately

- `parable-of-the-sower-mt-13-3-23-raelian-panspermia-canon-citation-cross-corpus-with-disavowals` is not extended. Its wohChoice governs Matthew's wording ('went out *to sow*', 'rocky ground'), which Thomas does not share. Its apparatus records a Raëlian-canon reading of Matthew's text, and extending it would attach that reading to a text the canon does not cite. The Thomas form is recorded in the overlay, which only cross-references the central entry. The Translator's glossaryRef at THOM-9 has been removed.
- `beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus` is not extended to THOM-7/18/19. Those sayings have no synoptic counterpart, and the lexical choice 'Blessed is' sits in the overlay. Recommend extending it in Blocks B/C to Thomas's synoptic-parallel beatitudes (54, 68, 69). The Translator's glossaryRefs at 7/18/19 have been removed.

### 3. Candidates for later promotion (no action now)

- `jitpe-mpmou-taste-death-thomas-woh` could be promoted when Mt 16 / Mk 9 / Jn 8 are translated (cross-corpus idiom).
- `nomina-sacra-and-abbreviation-expansion-convention-thomas-woh` could be promoted when a second Coptic or Greek manuscript-based text arrives.

---

## Lens-routing summary

- **No English line carries the lens.** No line uses 'Elohim', 'creators', 'planet' or 'messenger' for ⲁⲅⲅⲉⲗⲟⲥ. 'Sky' at 3/9/20 is a context-of-the-saying decision, and the commentary at 3 states that the saying cuts against a sky-located kingdom.
- **Mainstream framing.** The disputed date, the dispute over dependence on the synoptics (Patterson, DeConick vs Gathercole, Goodacre) and the debated relation to 'gnosticism' are stated at THOM-0 without adjudication.
- **WoH reading.** It appears three times (3, 18, 19), each as one labelled paragraph pointing to the single speculative overlay entry.
- **Raëlian sower reception.** It is not imported into Thomas 9.

## Escalation list (for human sign-off)

1. **SPECULATIVE:** `woh-reading-kingdom-within-beginning-end-five-trees-thomas-woh`. It needs sign-off by name, or deletion of the three labelled paragraphs (THOM-3, 18, 19) and their glossaryRefs.
2. **Review:** the manuscript reading is kept at the logion 7 and logion 30 cruxes.
3. **Review:** 'sons' rather than 'children' for ϣⲏⲣⲉ in the filial formulas (binds Blocks B/C).
4. **Review:** 'under a measure' at 33, against matthew-woh's 'basket' (`inferred`).
5. **Review:** the unbracketed negative reading of the logion 21 robbers clause (`inferred`).
6. **Orchestrator:** apply the CENTRAL section (add `cop`; three appliesTo extensions; bump to 2.75.0).
7. **Data maintainers:** the source findings at 3, 8, 10, 14, 18, 22 and 32 (source not edited).
