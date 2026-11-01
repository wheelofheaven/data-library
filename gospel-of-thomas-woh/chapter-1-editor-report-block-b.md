# Chapter 1 Editor Report — Gospel of Thomas, Block B (logia 39-76)

## Overview

Block B covers logia 39-76 of Nag Hammadi Codex II,2: 38 paragraph objects in the separate file `chapter-1.blockB.draft.json`.
That file stays separate through review; the orchestrator merges it into `chapter-1.json` at sign-off.
Block A (`chapter-1.json`, signed off) was read only and has not been touched; neither has `_meta.json` or `source-cop-1.json`.

The Translator submitted **47 editorial_questions[]**.
This pass resolves all 47 and clears the array.
One speculative overlay entry needs sign-off by name, and nine rulings are flagged for human review.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.1.0-rc1`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0`
- `translation.glossaryVersion`: `2.74.0` → `2.75.0` (the central version the Block A extensions were applied at; the central file was not touched by this pass)
- `translation.modelDrafts`: editor appended

**Commentary.** Written to `notes: {"official": …, "community": []}` as in Block A.
37 of 38 paragraphs carry commentary.
THOM-41 has none: it is a short synoptic parallel (Mk 4:25) with no divergence or source issue.

**English changes.** Seven edits in six paragraphs, each governed by an overlay entry:

| refId | Draft | Now | Entry |
|---|---|---|---|
| THOM-49 | 'the solitary ones and the chosen' | 'the solitary and chosen ones' | `sotp-chosen` |
| THOM-50 | 'movement and rest' | 'movement and **repose**' | `kim-anapausis-mton-movement-repose-rest` |
| THOM-51 | 'the rest of the dead' | 'the **repose** of the dead' | same |
| THOM-60 | 'They saw a Samaritan'; 'within rest' | '**⟨They saw⟩** a Samaritan'; 'within **repose**' | `whole-word-supply-angle-brackets-convention`; `kim-anapausis-…` |
| THOM-62 | 'I tell my mysteries to [those who are worthy] of [my] mysteries' | '**It is to** [those who are worthy] of [my] mysteries **that I tell my mysteries**' (focalising present → cleft) | `mysterion-mysteries` |
| THOM-74 | 'in the sickness(?)' | 'in the sickness' ('(?)' kept on 'drinking trough' only) | `logion-74-jote-shone-crux` |

Every other line keeps the Translator's draft, which was accurate.
No line was harmonised toward the synoptics.
The hard sayings keep the manuscript reading in the English: 42, 60, 61, 65, 67, 68, 71, 74, 75 (and 76 'his treasure').

---

## Rulings on the 47 editorial questions

All overlay ids carry the suffix `-thomas-woh`; it is omitted in the table.

| # | refId | Question | Ruling | Overlay entry (claim_type) |
|---|---|---|---|---|
| 0 | 39 | Greek overlap (P.Oxy. 655) | Coptic in the line; commentary states the Greek is largely restored and shows no secure divergence. | `coptic-base-text-…-convention` (direct, extended) |
| 1 | 39 | ⲅⲛⲱⲥⲓⲥ; ϩⲱⲡ | 'the keys of knowledge'; 'have hidden them'. | `gnosis-knowledge` (direct); `shaje-ethep-hidden-sayings` (extended) |
| 2 | 42 | Crux | 'Become passers-by.' kept; alternatives in commentary. | `parage-passers-by-logion-42` (direct) |
| 3 | 43 / 61 | Missing speech formula | No formula supplied at either place (binding register convention). 43 is clear from 'I say'. **61 escalated** (see review 4). | register convention (extended); `salome-name` (direct) |
| 4 | 43 | Jews / Judeans | 'the Jews'. | `ioudaioi-the-jews` (direct) |
| 5 | 44 | Triad; passive | 'the Father … the Son … the Holy Spirit'; 'he will be forgiven'. | `son-and-holy-spirit-triad-logion-44` (direct) |
| 6 | 45 | bad / evil | 'bad' (ⲕⲁⲕⲟⲥ, ϩⲟⲟⲩ), 'evil things' (ⲡⲟⲛⲏⲣⲟⲛ). | `kakos-poneron-hoou-bad-evil` (direct) |
| 7 | 46 | Unwritten negative; 'lowered' | Normalised negative followed, no brackets (as THOM-21); 'lowered' kept, literal 'broken' in commentary. | `logion-46-eyes-lowered-and-little-one` (**inferred**) |
| 8 | 46 | ⲉϥⲟ ⲛ̄ⲕⲟⲩⲉⲓ | 'becomes a little one'. | same; `shere-son-child` (extended) |
| 9 | 47 | ϩⲙϩⲁⲗ | 'slave' throughout (47, 64, 65). | `hmhal-slave-joeis-master-lord` (direct) |
| 10 | 47 | ϫⲟⲉⲓⲥ | 'master' (47, 64, 65); 'the lord' lower case (73); vocative 'Lord' (74). | same |
| 11 | 48 | Adjectival ⲟⲩⲱⲧ | 'single' (48, 76). | `oua-ouot-a-single-one` (extended) |
| 12 | 49 | ⲥⲱⲧⲡ; syntax | 'chosen' (49, 50). **Changed** at 49 to one group: 'the solitary and chosen ones' (bare relative ⲉⲧⲥⲟⲧⲡ needs ⲙⲟⲛⲁⲭⲟⲥ as antecedent). | `sotp-chosen` (direct) |
| 13 | 49 / 58 | Beatitude coverage | Overlay makarios entry at 49 and 58, scope extended to plural 'Blessed are' for non-synoptic beatitudes. | `makarios-blessed-singular-formula` (extended) |
| 14 | 50 | Pronouns, filial | 'its sons' (ratified 'sons' rule); 'It [stood]'; 'their image' unresolved; 'Is it you?'. | `logion-50-light-and-interrogation-vocabulary` (direct) |
| 15 | 50 | Mechanical brackets | 'It [stood] and [appeared]' kept (rule is mechanical); 'stood' is literal for ⲱϩⲉ ⲉⲣⲁⲧ=. | same |
| 16 | 50 | rest / repose | **Changed.** ⲁⲛⲁⲡⲁⲩⲥⲓⲥ = 'repose' (50, 51, 60; 90 in Block C); native ⲙ̄ⲧⲟⲛ = 'rest' (61; 86 in Block C); ⲕⲓⲙ = 'movement'. | `kim-anapausis-mton-movement-repose-rest` (direct) |
| 17 | 51 | anapausis vs anastasis | Manuscript: 'the repose of the dead'. The 'resurrection' conjecture is not printed. | same |
| 18 | 52 | 'in you'; ⲕⲱ | 'spoke in you', 'left aside' kept. | `logion-52-twenty-four-prophets` (direct) |
| 19 | 53 | Circumcision | 'in spirit' lower case; 'useful' / 'profitable'; central brit-milah **not** cited; ⟨ⲙ̄⟩ silent. | `logion-53-circumcision-in-spirit` (direct) |
| 20 | 54 | Central refs; 'yours' | Central beatitudes (54, 68, 69) and kingdom-of-the-heavens (54) cited; 'yours' kept. | CENTRAL |
| 21 | 55 | Staurogram | Silent expansion 'cross'; nomina-sacra entry scope extended to the staurogram. | `nomina-sacra-…-convention` (extended) |
| 22 | 56 | ⲡⲧⲱⲙⲁ | 'corpse' (56, 60) vs 'body' (80). | `ptoma-corpse` (direct) |
| 23 | 57 | Darnel parable | 'darnel'; 'in order to pull up'; passive for the impersonal plural; sigla silent; restorations bracketed. | `logion-57-darnel-parable-vocabulary` (direct) |
| 24 | 58 | ϩⲓⲥⲉ | 'who has suffered'. | `hise-suffer-toil` (direct) |
| 25 | 59 | ϭⲱϣⲧ ⲛ̄ⲥⲁ; negative | 'Look to the living one'; normalised negative followed, no brackets. | `goosht-look-watch` (direct) |
| 26 | 60 | ⟨ⲁⲩⲛⲁⲩ⟩ | **Changed.** '⟨They saw⟩' in English angle brackets: rule 2 covers supplied letters, not a supplied whole word. | `whole-word-supply-angle-brackets-convention` (direct) |
| 27 | 60 | Crux | Manuscript kept: 'That one is around the lamb.' | `logion-60-samaritan-crux` (direct) |
| 28 | 61 | ϩⲱⲥ ⲉⲃⲟⲗ ϩⲛ̄ⲟⲩⲁ | 'As though from someone' (indefinite ⲟⲩⲁ). | `shesh-equal-and-logion-61-crux` (direct) |
| 29 | 61 | ⲡⲉⲧϣⲏϣ | 'the one who is equal' (literal); 'the undivided' in commentary. | same |
| 30 | 61 | ϣⲏϥ crux | Manuscript kept: 'When he is destroyed'; ϣⲏϣ emendation in commentary (Dilley, citing Layton 1989, p. 74). | same |
| 31 | 61 | Salome | 'Salome', unidentified in the line; feminine ⲧⲉⲕ- explained in commentary. | `salome-name` (direct) |
| 32 | 62 | ⲙⲩⲥⲧⲏⲣⲓⲟⲛ | 'mysteries'. **Changed** to a cleft for the focalising present ⲉⲓ̈ϫⲱ. | `mysterion-mysteries` (direct) |
| 33 | 64 | Banquet vocabulary | 'guests' / 'village' / 'money due from' / 'dinner' kept. | `logion-64-dinner-parable-vocabulary` (direct) |
| 34 | 64 | Closing line | 'Buyers and [merchants will] not [enter] the places of my Father'; both merchant words 'merchants'; speaker left open. | same |
| 35 | 65 | ⲭⲣⲏ[ⲥⲧⲟ]ⲥ | Edition's restoration '[good]' kept; 'creditor/usurer' restoration in commentary, **unattributed** (see review 7). | `logion-65-vineyard-restoration-and-crux` (direct) |
| 36 | 65 | ⲙ̄ⲡⲉϥⲥⲟⲩⲱⲛⲟⲩ | Manuscript kept: 'Perhaps he did not know them'; 'farmers'; 'feel shame before'. | same |
| 37 | 67 | Parse | 'Whoever knows the All but is lacking in himself is lacking entirely.'; topos entry not applied; ⟨ϥ⟩ silent. | `logion-67-lacking-entirely` (**inferred**) |
| 38 | 68 | Crux | Literal kept; Pella allusion noted as a commentators' suggestion; ϩⲟⲧⲁ(ⲛ) finding recorded. | `logia-68-69-persecution-beatitudes-wording` (direct) |
| 39 | 69 | Wording | 'within their heart'; 'the belly of the one who desires will be filled'. | same |
| 40 | 70 | ϫⲡⲟ | 'bring forth' (context rule recorded on the jpo entry); 'within you'. | `jpo-not-born-of-woman` (extended) |
| 41 | 71 | Gap | 'build it …'; no conjecture printed. | `logion-71-destroy-and-build` (direct) |
| 42 | 72 | Brackets | 'A [man said]' (adjacent restored words share brackets, as at THOM-37). | `refposhe-divider-logion-72` (direct); restored-text (extended) |
| 43 | 74 | ϫⲱⲧⲉ / ϣⲱⲛⲉ | Editor's Coptic check below. 'drinking trough(?)' kept; **'sickness' without '(?)'**. | `logion-74-jote-shone-crux` (direct) |
| 44 | 75 | ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ | 'the bridal chamber'; the Valentinian rite is disclaimed in commentary. | `ma-nsheleet-bridal-chamber` (direct) |
| 45 | 76 | Merchant vocabulary | 'a man, a merchant … merchandise … wise … this single pearl' kept. | `logion-76-merchant-pearl-and-treasure` (direct) |
| 46 | 76 | {ⲉϥ} conflict | 'his treasure' kept: the manuscript reading (with the scribe's correction) stands; Dilley's { } deletion is reported in commentary. | same |

---

## Specific rulings requested

### Logion 74 — Coptic check of ϫⲱⲧⲉ / ϣⲱⲛⲉ

- **ϣⲱⲛⲉ is certain as a word.** It is the common Coptic for 'sickness' (Crum s.v.). The corpus lemmatises it so, and the same lemma gives ⲛⲉⲧϣⲱⲛⲉ 'the sick' at THOM-14.
  The difficulty is that the sense fits the image poorly, which is a question of suspected corruption, not of meaning.
  Dilley records the conjecture ϣⲱⲧⲉ 'well, cistern' as uncertain (Layton 1989, p. 80). Lambdin prints 'cistern'.
  The Greek saying reported by Origen (Contra Celsum 8.15-16: many around the well, no one in the well) supports the sense of the emendation.
  Ruling: manuscript in the line, 'sickness', **no '(?)'**; the emendation goes in commentary under the crux rule.
- **ϫⲱⲧⲉ is genuinely uncertain.** The Editor could not identify an attested Coptic noun of this form with a sense that fits; 'drinking trough' (Lambdin) is a contextual guess.
  Ruling: '(?)' kept on 'drinking trough', the vendidad-woh use of '(?)' for a term of uncertain meaning.
- **Source finding.** Dilley's emendation note is attached to *both* tokens in the corpus. The emendation in the literature concerns ϣⲱⲛⲉ; the duplication looks like an annotation error.
- ϣⲱⲧⲉ does occur elsewhere in Thomas (logion 96) in its other sense, 'dough'. That gives no support either way.

### Logion 60 — the whole-word supply ⟨ⲁⲩⲛⲁⲩ⟩ (rule 2 vs ⟨ ⟩)

Block A's rule 2 justifies silent rendering because bracketing a whole English word for a one-letter scribal slip would make an intact text look damaged.
That reasoning does not cover a supplied whole word: here the manuscript has no main verb, and a silent 'They saw' would tell the reader that it does.
The ⟨ ⟩ that Block A reserved for 'English words the Editor supplies where no Coptic wording exists' fits the case exactly.
Ruling: '⟨They saw⟩'. This is recorded as a refinement in a new convention entry; the ratified entry is extended only by a scope note.
This is the first use of English ⟨ ⟩ in Thomas (review 3).

### Logion 72 — the bracket merge

'A [man said]' is kept.
Both ⲟⲩⲣ[ⲱⲙ]ⲉ and [ⲡⲉ]ϫⲉ are partly restored, and adjacent bracketed English words share one pair, as in Block A's '[then you will]' (THOM-37).
'A' stands on ⲟⲩ, which is extant (underdotted only), so it is outside the bracket.

### Logia 46 and 59 — unmarked negatives

Both follow the normalised layer, without brackets, as the restored-text convention requires and as Block A ruled at THOM-21.
They differ in one respect.
At 46 the lemma aid counts a supplied span (ⲛ̄ⲛⲉⲩ-), so the edition supplies letters that `text` does not mark.
At 59 the lemma aid counts no supplied span; the negative exists only in the normalisation of ϫⲉⲛⲉⲧⲙ̄ⲙⲟⲩ to ⲛ̄ⲛⲉⲧⲛ̄ⲙⲟⲩ, as at THOM-21.
In both cases every standard translation has the negative and the context requires it.
Claim types: 46 is `inferred`, because of 'lowered', not because of the negative; 59 falls under the direct convention.

### Source anomalies (source stays immutable)

| refId | Finding | Effect on English |
|---|---|---|
| THOM-45 | Word-internal middle dot ϣⲁϥ·ⲉⲓⲛⲉ (also in the normalised layer; cf. THOM-22) | None |
| THOM-46 | Negative optative supplied in the normalised layer, unmarked in `text` (lemma aid: 1 span) | Negative followed |
| THOM-51 | Word-internal middle dot ⲛⲁ·ϥ; diplomatic ⲉⲡⲕⲟⲥⲙⲟⲥ, normalised ⲉⲣⲉⲡⲕⲟⲥⲙⲟⲥ | None |
| THOM-55 | Staurogram encoded as U+2CC1 COPTIC SMALL LETTER SAMPI instead of U+2CE8 COPTIC SYMBOL TAU RO (look-alike substitution) | None ('cross') |
| THOM-57 | A run of **454 spaces** inside `text` (offset 253, between ⲛⲧⲉⲧⲛϩⲱⲗⲉ and ⲙ̄ⲡⲥⲟⲩⲟ); the normalised layer is continuous, so nothing is missing | None |
| THOM-59 | Negative only in normalisation (lemma aid: no supplied span) | Negative followed |
| THOM-60 | ⟨ⲁⲩⲛⲁⲩ⟩ is a whole-word supply | '⟨They saw⟩' |
| THOM-63 | Rasura ⲛ̄ⲧⲁⲱ[[ϩ]]ⲥϩ with metathesis; normalised ⲛ̄ⲧⲁⲱϩⲥ; [[ ]] is a scribal erasure, not a restoration | None ('reap', no bracket) |
| THOM-65 | Lemma aid counts 4 supplied spans, `text` shows 2; normalisation supplies ⲉⲣⲉ- | None |
| THOM-68 | `text` reads ϩⲟⲧⲁⲛ unmarked; lemma aid has ϩⲟⲧⲁ(ⲛ) (1 span) | None |
| THOM-71 | Lemma aid counts 1 span, `text` shows 2 bracket groups (restoration + unrestored gap) | None |
| THOM-74 | Dilley's ϣⲱⲧⲉ note attached to both ϫⲱⲧⲉ and ϣⲱⲛⲉ | None |
| THOM-76 | {ⲉϥ}: the `orig` attribute reads ⲡ{ⲉϥ}, the token content ⲡⲉ{ϥ} (internal inconsistency); the normalised layer reads ⲡⲉϥⲁϩⲟ; the superscript ⲉ is encoded as ASCII `\bⲉ/` (literal backslash, Latin b, slash) in `text`; first ⲙⲁⲣⲅⲁⲣⲓⲧⲏⲥ POS-tagged V | 'his treasure' kept |

Recommendation for the data maintainers (not this pass): re-fetch rather than hand-edit.
Check the exporter's handling of `hi_rend="superscript"` (76), whitespace runs (57) and the staurogram code point (55), and re-check the supplied-span counts against the diplomatic sigla (65, 68, 71), as already recommended for Block A.

### The {ⲉϥ} conflict at 76 — reasoning

The manuscript has ⲡⲉϥ with an ⲉ written above the line. That scribal correction produces ⲡⲉϥⲉϩⲟ 'his treasure'.
Dilley's { } is the modern editor's deletion, not a scribal cancellation; Dilley marks scribal erasure with [[ ]], as at 63.
The normalised layer and Lambdin both read 'his treasure'.
Rule 2 (drop { } silently) was written for evident scribal surplus; here the bracket deletes a meaningful morpheme against the scribe's own correction.
Convention 6 (the manuscript reading stands; emendations in commentary) therefore governs.
The ruling is recorded in a scope note on the ratified restored-text entry and in `logion-76-merchant-pearl-and-treasure-thomas-woh` (review 5).

---

## Greek vs Coptic (Block B)

| Logion | Greek witness | Material divergence | Treatment |
|---|---|---|---|
| 39 | P.Oxy. 655 col. ii | None secure; the Greek is largely restored | Coptic; commentary |
| 40-76 | none | — | Coptic |

---

## Speculative entries requiring sign-off

### `woh-reading-logion-50-origin-from-the-light-thomas-woh` (overlay)

**Source:** Thomas 50, ⲛ̄ⲧⲁⲛⲉⲓ ⲉⲃⲟⲗ ϩⲙ̄ⲡⲟⲩⲟⲉⲓⲛ ⲡⲙⲁ ⲉⲛⲧⲁⲡⲟⲩⲟⲉⲓⲛ ϣⲱⲡⲉ ⲙ̄ⲙⲁⲩ … ⲁϥⲟⲩⲱⲛϩ ⲉ[ⲃ]ⲟⲗ ϩⲛ̄ⲧⲟⲩϩⲓⲕⲱⲛ
**WoH choice:** No effect on any English line.
One labelled paragraph in the notes of THOM-50 ('Wheel of Heaven reading (interpretive; not part of the translation)') records one resonance.
The saying answers a question of origin with a place and says that the light 'appeared in their image', with an unresolved plural; this can be read alongside Gen 1:26 'in our image' and the canon's teaching that humans were made in the image of the Elohim.
**Why speculative:** The saying names no makers, no planet and no place in the sky, and the canon does not cite it.
Reading the plural 'their' as the Elohim is an interpretive synthesis beyond any single source.
The commentary states the mainstream reading first (a catechism of origin and return, with 'the light' as the realm of origin), and the English keeps 'their' unresolved.
**Recommendation:** ship as `speculative`, apparatus only.
If declined, delete the last paragraph of the THOM-50 notes and drop the id from THOM-50's glossaryRefs. Nothing else depends on it.

This is the only point at which the lens touches Block B.
Logion 49 ('you are from it, and … you will go again') was considered and deliberately left without a lens paragraph, to keep the use sparing.

---

## Unresolved editorial questions / decisions for review

None of the 47 questions is left open. The following are judgement calls the reviewer should confirm.

### 1. `THOM-50/51/60` — 'repose' for ⲁⲛⲁⲡⲁⲩⲥⲓⲥ (English changed)

**Issue:** The draft's 'the rest of the dead' (51) reads in English as 'the remainder of the dead'.
**Options considered:** (A) 'repose' for the Greek loan, 'rest' for native ⲙ̄ⲧⲟⲛ (adopted; Lambdin's rendering); (B) 'rest' throughout; (C) 'repose' at 51 only.
**Why escalating:** (A) binds Block C (logion 90, ⲁⲛⲁ{ⲩ}ⲡⲁ⟨ⲩ⟩ⲥⲓⲥ) and creates a deliberate difference from 'rest' in Mt 11:28-29, while (C) would break the 50 → 51 link.

### 2. `THOM-49` — 'the solitary and chosen ones' (English changed)

**Issue:** The bare relative ⲉⲧⲥⲟⲧⲡ makes the blessed one group; the draft had two groups.
**Why escalating:** It is a change of the draft's syntax and touches the ratified 'solitary ones' wording, adjusted only by word order.

### 3. `THOM-60` — first use of English ⟨ ⟩ in Thomas

**Issue:** The convention is refined: supplied letters stay silent, supplied whole words are marked.
**Options considered:** '⟨They saw⟩' (adopted); silent 'They saw' (rule 2 applied literally); no verb (unidiomatic).
**Why escalating:** It refines a ratified convention. Block C should apply it, and the Block C draft already exists in the workspace.

### 4. `THOM-61` — no speech formula before 'I am your disciple'

**Issue:** The feminine ⲧⲉⲕ- shows Salome is speaking; the English cannot show it and, under the binding register convention, supplies no formula, so a reader may take Jesus as the speaker.
**Options considered:** (A) no formula, speaker explained in commentary (adopted, per the binding convention); (B) '⟨Salome said:⟩' in English angle brackets.
**Why escalating:** (B) is arguably more accurate for an English reader, but it would breach convention 1 as ratified. The Editor recommends that the human reviewer decide; if (B) is chosen, extend `whole-word-supply-angle-brackets-convention-thomas-woh` to 'speaker identification carried by Coptic grammar alone'.

### 5. `THOM-76` — 'his treasure' against the diplomatic {ⲉϥ}

**Issue:** The two corpus layers disagree. The manuscript reading (with the scribal correction) is kept over the editor's deletion.
**Why escalating:** It is the first case where convention 6 is ruled to override the silent-drop rule for { }.

### 6. `THOM-74` — '(?)' on 'drinking trough' only

**Issue:** The draft had '(?)' on both nouns. 'Sickness' is a certain word in a suspect context.
**Why escalating:** The Editor could not verify the meaning of ϫⲱⲧⲉ against Crum directly and relies on its absence from the Editor's knowledge of the lexicon; a Coptic specialist should confirm.

### 7. `THOM-65` — restoration and attribution

**Issue:** The line prints the edition's '[good]'.
The Translator attributed the alternative restoration 'usurer' to Layton/Lambdin. The Editor could not confirm that attribution, so the commentary reports the alternative restoration ⲭⲣⲏ[ⲥⲧⲏ]ⲥ without naming anyone.
**Why escalating:** It is a restoration crux with two serious options, and the attribution needs checking before anyone cites it.

### 8. `THOM-46` and `THOM-67` — the two `inferred` entries

46 'lowered' interprets ⲟⲩⲱϭⲡ 'break'; 67's parse of ⲟⲩⲁⲁϥ and ⲙ̄ⲡⲙⲁ ⲧⲏⲣϥ is one of several.
Both follow the crux rule in spirit (literal sense or alternatives in commentary), but the line takes a position.

### 9. Hard sayings kept in the manuscript reading

42, 60, 61 (ϣⲏϥ), 65 (ⲙ̄ⲡⲉϥⲥⲟⲩⲱⲛⲟⲩ), 67, 68, 71, 74, 75 and 76 keep the manuscript reading; the emendations, with attribution only where it is certain (Dilley's notes citing Layton 1989; Lambdin where the Editor is confident of the wording), are in commentary.
As in Block A, readers who know popular translations (74 'well', 65 'they did not know him') will notice the difference.

---

## Glossary changes for review

### Central glossary

None written. All proposals are in the CENTRAL section below.

### Per-translation overlay (v1.0.0 → **v1.1.0**, released 2026-11-01; semver-minor: additions and scope extensions only)

`gospel-of-thomas-woh/_translation-glossary.json`: 39 → **70 entries** (61 direct, 7 inferred, 2 speculative).

**Added (31):** 28 `direct`, 2 `inferred`, 1 `speculative`.

- **Convention (1, direct):** `whole-word-supply-angle-brackets-convention`
- **Lexical, direct (27):** `gnosis-knowledge`, `parage-passers-by-logion-42`, `ioudaioi-the-jews`, `son-and-holy-spirit-triad-logion-44`, `kakos-poneron-hoou-bad-evil`, `hmhal-slave-joeis-master-lord`, `sotp-chosen`, `kim-anapausis-mton-movement-repose-rest`, `logion-50-light-and-interrogation-vocabulary`, `ptoma-corpse`, `logion-57-darnel-parable-vocabulary`, `hise-suffer-toil`, `goosht-look-watch`, `logion-60-samaritan-crux`, `salome-name`, `shesh-equal-and-logion-61-crux`, `mysterion-mysteries`, `logion-64-dinner-parable-vocabulary`, `logion-65-vineyard-restoration-and-crux`, `logia-68-69-persecution-beatitudes-wording`, `logion-71-destroy-and-build`, `refposhe-divider-logion-72`, `logion-74-jote-shone-crux`, `ma-nsheleet-bridal-chamber`, `logion-76-merchant-pearl-and-treasure`, `logion-52-twenty-four-prophets`, `logion-53-circumcision-in-spirit`
- **Inferred (2):** `logion-46-eyes-lowered-and-little-one`, `logion-67-lacking-entirely`
- **Speculative (1):** `woh-reading-logion-50-origin-from-the-light`

**Extended (23 ratified entries; appliesTo + new `scopeNote` field only; wohChoice, rationale and claim_type unchanged):**
`register-sayings-format-and-proper-names-convention`, `restored-text-bracket-and-sigla-convention`, `nomina-sacra-and-abbreviation-expansion-convention` (staurogram), `greek-loanword-rendering-convention`, `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention`, `shaje-ethep-hidden-sayings`, `etonh-the-living-lowercase`, `ptirf-the-all-reign-over-the-all`, `mntero-the-kingdom`, `tpe-sky-heaven-context-rule`, `shere-son-child`, `eiot-father-capitalisation`, `mnthke-poverty`, `oua-ouot-a-single-one` (adjectival ⲟⲩⲱⲧ), `topos-ma-place`, `rome-man-human-person`, `makarios-blessed-singular-formula` (plural non-synoptic 'Blessed are'), `kosmos-world-kah-earth`, `ouoein-light-man-of-light`, `pneuma-sarx-soma-spirit-flesh-body`, `jpo-not-born-of-woman` (ϫⲡⲟ context rule), `monachos-solitary`, `eikon-image`.
(All ids end in `-thomas-woh`.)

glossaryRefs on every Block B unit are generated from the overlay `appliesTo` arrays plus the four central ids below, so the two cannot drift; every id resolves in the overlay v1.1.0 or central v2.75.0.

---

## CENTRAL — apply by orchestrator

Central v2.75.0 is not modified by this pass.
The proposals add no new entries and extend `appliesTo` on four existing entries: a semver-minor bump to **2.76.0**.
The Block B glossaryRefs already cite all four ids.

### 1. EXTEND `appliesTo`

| Existing central id | Add to `appliesTo` | Reason |
|---|---|---|
| `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus` (direct) | `THOM-39`, `THOM-40`, `THOM-41`, `THOM-42`, `THOM-44`, `THOM-45`, `THOM-46`, `THOM-47`, `THOM-48`, `THOM-49`, `THOM-50`, `THOM-54`, `THOM-55`, `THOM-56`, `THOM-57`, `THOM-58`, `THOM-59`, `THOM-61`, `THOM-62`, `THOM-63`, `THOM-64`, `THOM-66`, `THOM-67`, `THOM-68`, `THOM-69`, `THOM-70`, `THOM-71`, `THOM-73`, `THOM-75`, `THOM-76` (30 units) | Every Block B unit whose `text` contains the nomen sacrum ⲓ︤ⲥ︥ (including 62, where the letters are underdotted). Not added: 43, 51, 52, 53, 60, 65, 72, 74, which have no ⲓ︤ⲥ︥. |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (direct) | `THOM-45`, `THOM-50`, `THOM-57`, `THOM-62`, `THOM-64`, `THOM-65`, `THOM-70`, `THOM-71`, `THOM-72` | Units with real [ ] restorations or an unrestored [ ] gap (71). Not THOM-63, whose [[ ]] is a scribal erasure. |
| `beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus` (direct) | `THOM-54`, `THOM-68`, `THOM-69` | Confirmed synoptic-parallel beatitudes: 54 = Mt 5:3 / Lk 6:20; 68 = Mt 5:11 / Lk 6:22; 69 = Mt 5:10 and Lk 6:21 / Mt 5:6. Thomas's wording differs ('the poor', 'yours'); the Thomas form is recorded in the overlay. Not extended to 49 or 58, which have no synoptic counterpart. |
| `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim` (direct) | `THOM-54` | ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ keeps the plural: 'the kingdom of the heavens'. Thomas 54 pairs it with Luke's 'yours', which shows the plural is not tied to Matthew's wording. (Block C will add THOM-114.) |

### 2. scopeNote line (suggested)

"v2.76.0: Gospel of Thomas Block B (logia 39-76): iēsous extended to 30 further THOM units; lacuna-bracket to 9; beatitudes extended to the synoptic-parallel beatitudes THOM-54/68/69; kingdom-of-the-heavens to THOM-54. Thomas-specific decisions live in the gospel-of-thomas-woh overlay v1.1.0."

### 3. NOT extended, deliberately

- `brit-milah-circumcision-covenant` is not extended to THOM-53. It governs the Hebrew covenant term of Gen 17, and Thomas's saying has no lexical link to it (the Translator did not cite it either).
- `parable-of-the-sower-…` is not applicable to Block B.

### 4. Candidates for later promotion (no action now)

- `kim-anapausis-mton-movement-repose-rest-thomas-woh`: ἀνάπαυσις recurs in Mt 11:28-29 and across Nag Hammadi texts. Promote if a second Coptic text or Mt 11 is translated.
- `ma-nsheleet-bridal-chamber-thomas-woh`: νυμφών (Mt 9:15; Thomas 104). Promote if Mt 9 or a further Coptic text arrives.
- `hmhal-slave-joeis-master-lord-thomas-woh`: the 'slave' convention for δοῦλος already holds de facto in matthew-woh and could become a central cross-corpus entry.

No new cross-corpus entry is proposed now.

---

## Lens-routing summary

- **No English line carries the lens.** No line uses 'Elohim', 'creators', 'planet' or similar. 'Their image' (50) stays unresolved; 'the light' stays 'the light'; 'the places of my Father' (64) and 'the bridal chamber' (75) are standard renderings.
- **WoH reading.** It appears once (50), as one labelled paragraph pointing to a single speculative overlay entry, placed after the mainstream reading.
- **Mainstream framing.** Polemical and debated items are stated, not softened or adjudicated: 'the Jews' (43), the Pella suggestion (68), the Valentinian 'bridal chamber' (75).

## Escalation list (for human sign-off)

1. **SPECULATIVE:** `woh-reading-logion-50-origin-from-the-light-thomas-woh`. Sign off by name, or delete the labelled last paragraph of the THOM-50 notes and drop the id from THOM-50's glossaryRefs.
2. **Review:** 'repose' for ⲁⲛⲁⲡⲁⲩⲥⲓⲥ (English changed at 50, 51, 60; binds logion 90).
3. **Review:** '⟨They saw⟩' at 60, the first English ⟨ ⟩ and a refinement of rule 2.
4. **Review:** no '⟨Salome said:⟩' at 61 (binding convention kept; option B offered).
5. **Review:** 'his treasure' at 76 against the diplomatic {ⲉϥ}.
6. **Review:** logion 74, '(?)' on 'drinking trough' only; ϫⲱⲧⲉ to be confirmed by a Coptic specialist.
7. **Review:** logion 65, '[good]' and the unconfirmed 'usurer' attribution.
8. **Review:** 'the solitary and chosen ones' at 49 (English changed).
9. **Review:** the two `inferred` entries (46 'lowered', 67 parse).
10. **Review:** hard sayings kept in the manuscript reading (42, 60, 61, 65, 67, 68, 71, 74, 75, 76).
11. **Orchestrator:** apply the CENTRAL section (four appliesTo extensions; bump to 2.76.0) and merge Block B into `chapter-1.json` at sign-off.
12. **Data maintainers:** the source findings at 45, 46, 51, 55, 57, 59, 63, 65, 68, 71, 74 and 76 (source not edited).
