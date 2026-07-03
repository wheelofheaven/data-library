# Chapter 1 Editor Report

**Book:** Ōmoto Shin'yu (大本神諭, Divine Revelations), WoH-Translation (OSHIN-WOH)
**Chapter:** 1 — the Meiji 25 (1892) founding oracles of Deguchi Nao (first *fude*, old-cal. 1st month; and old-cal. 5th month 5th day), OSHIN-1:1…OSHIN-1:93
**Editor pass:** 2026-07 (claude-opus-4-8[1m])
**Status at end of pass:** `editor-review` (advanced from `draft`; version `1.0.0-draft` → `1.0.0-rc1`)

---

## Summary

The Ōmoto Shin'yu is **the pipeline's first Japanese-source text**. No prior
overlay glossary or Japanese-scoped convention existed; both were built in
this pass. The lens-risk profile is defined by one genuinely lens-level
decision — the rendering of **神 (kami)**, handled exactly as the Hidden
Words *b-h-y* rule — plus a dense stratum of Ōmoto-technical and
Buddhist/Shintō cosmological vocabulary requiring fixed English mappings,
and a **sensitive-register** obligation (the 1892 text's xenophobic and
ableist passages).

The pass (i) created a new per-book overlay glossary
(`oomoto-shinyu-woh/_translation-glossary.json`, **v1.0.0**) with **16
entries** (10 `inferred`, 6 `direct`, **0 `speculative` committed**); (ii)
**resolved all 18 editorial questions** into glossary entries, commentary,
or literal-consensus readings, and **escalated 1 proposed `speculative`
entry** (the kami/Elohim-frame identification) requiring human sign-off;
(iii) applied per-verse `notes.official` commentary to **31 paragraphs**,
leaving non-divergent verses empty per the commentary-discipline rule; (iv)
made **1 authorized English edit** (OSHIN-1:1 一同 "all at once" → "all
together"), backed by the collation entry; (v) recorded the partial
collation state (38/93 exact witness match) and the one sense-bearing
orthographic variant in a collation-witness entry; (vi) held the
verification status at **witness-confirmed-collation-partial** — a
single-edition philological pass remains pending.

The surface English is a defensible, independent scholarly rendering
throughout. **神 is kept strictly neutral ("the kami"); no Elohim / Raëlian
vocabulary is in any line.**

**Counts after pass:**
- Overlay glossary: new file at **v1.0.0** — **16 entries** (10 `inferred`, 6 `direct`)
- **0 `speculative` entries committed**
- **1 `speculative` entry escalated** (kami/Elohim frame — NOT committed; see below)
- **31 paragraphs with commentary**; all 93 carry the romanization-convention ref; all ぞよ-final verses carry the oracular-ender ref
- **18 of 18 editorial questions resolved; 1 speculative escalated**; `editorial_questions[]` cleared to `[]`
- **1 authorized English edit** (OSHIN-1:1), backed by a glossary entry

---

## Speculative entries requiring sign-off

### `kami-elohim-frame-identification-oomoto-shinyu-woh` (PROPOSED — NOT committed)

**Source:** 神 / 艮の金神 / 国常立尊 — the divine speaker of the oracle,
identified at OSHIN-1:52 as Ushitora no Konjin = Kunitokotachi-no-Mikoto, a
wronged, banished, and now-**returning creator-kami** who will "appear
openly" (表に現はれて, 1:7, 1:62, 1:73) to rebuild the world.

**WoH choice under consideration:** identify Ōmoto's banished-and-returning
creator-kami with the Wheel of Heaven Elohim frame, and/or surface that
identification in the translated line (e.g. rendering 神 as "the Elohim" or
capitalising/glossing toward the frame).

**WoH choice taken instead:** kept **strictly neutral** in the surface
text. 神 is rendered "the kami" throughout (committed entry
`kami-neutral-theism-oomoto-shinyu-woh`, `inferred`); 艮の金神 and 国常立尊
are retained as romanized theonyms. The Elohim-frame resonance is confined
to a single restrained **comparative** note at OSHIN-1:52 (naming the
banished-returning-creator motif as "the natural site of comparative
reading," with the identification explicitly reserved to the apparatus and
wiki), and to this report. **No `speculative` entry is committed and no
Raëlian vocabulary appears in any line.**

**Why speculative:** the *lexical* facts are direct and already carried
(神 = "the kami"; Ushitora no Konjin is a Konjin-class directional deity;
the text itself equates him with Kunitokotachi; the eschatology is a
banished-power's return-and-rebuild). What crosses into `speculative` is the
*interpretive* claim that this figure **is** the Elohim of the Wheel of
Heaven frame — a project-specific synthesis attested by no single source —
and the editorial move of surfacing it in the translated text. Doing so
would import the lens into the line in violation of the "lens lives in the
apparatus" rule.

**Recommendation:** **Ship the neutral rendering as-is** ("the kami"; frame
resonance in the 1:52 comparative note only). **Do not** inject "Elohim" or
commit the identification entry without sign-off. If the reviewer wants the
resonance developed, the correct home is expanded commentary or a wiki
cross-reference, **not** the translated line. This is the single decision in
the pass that is a WoH-lens call rather than a philological one, and — with
the pending philological pass (below) — the thing blocking advancement past
`editor-review`. **This applies the ratified Hidden Words *b-h-y* ruling of
2026-07-03 to the Japanese corpus; please confirm by name that it extends
here.**

---

## Resolution of the 18 editorial questions

| # | Question (refIds) | Resolution |
|---|---|---|
| 1 | 艮の金神 Ushitora no Konjin (1:1, 14, 25, 52, 54) | **Resolved** → entry `ushitora-no-konjin-theonym-…` (`direct`). **Retain romanized theonym + gloss** on first use; not descriptivized. Governs the 1:52 Kunitokotachi apposition too. |
| 2 | 三千世界 sanzen sekai (1:1, 7, 10, 17, 57) | **Resolved** → entry `sanzen-sekai-three-thousand-worlds-…` (`inferred`). **Literal "the three-thousand worlds"**, preserving the Buddhist trichiliocosm register over naturalizing "the whole universe". |
| 3 | 立替へ立直し tatekae-tatenaoshi (1:7, 14, 15, 50, 51, 56) | **Resolved** → entry `tatekae-tatenaoshi-reconstruction-renewal-…` (`inferred`). **Translated "reconstruction and renewal"** (reduced 世の立替 = "the reconstruction of the world"); carpentry metaphor glossed. |
| 4 | 改心 kaishin (1:43, 78, 81, 86) | **Resolved** → entry `kaishin-change-of-heart-…` (`inferred`). **"change of heart"** over the Christian-freighted "repentance" (source uses 改心, not 悔い改め). |
| 5 | ぞよ zo yo oracular ender (pervasive) | **Resolved** → entry `zoyo-oracular-ender-unmarked-declarative-…` (`direct`). **Unmarked assertive declarative**; "zo yo" kept in translit only; no repeated English tag (pastiche risk). Applied to every ぞよ-final verse. |
| 6 | 神 kami — the lens call (all) | **Resolved neutral; speculative escalated.** Committed entry `kami-neutral-theism-…` (`inferred`) = **"the kami"** (untranslated, not "God"). Elohim-frame identification **NOT committed**; escalated above. |
| 7 | 神国 shinkoku (1:2, 10, 19, 39, 40, 65) | **Resolved** → entry `shinkoku-divine-land-…` (`inferred`). **"divine land"**, NOT the militarist-era "divine nation" (1892 predates that appropriation — noted in commentary). 神道 Shintō (1:3) and 神世 kamiyo (1:70) kept distinct. |
| 8 | 神柱 / 守護神 / 守護人 (1:14, 15, 40, 51, 53, 56, 57, 66) | **Resolved** → entry `kamibashira-shugojin-shugonin-guardian-hierarchy-…` (`inferred`). **Distinguished:** 神柱 "divine pillar" (human mediums), 守護神 "guardian deity", 守護人 "guardian" (person). shugojin/shugonin NOT merged. |
| 9 | 1:14 acrostic; 玉芝 Tamashiba (1:14) | **Resolved in commentary; PHILOLOGICAL escalation.** Literal rendering, names preserved; wordplay glossed not reconstructed. **玉芝 has no secure referent — flagged for a specialist reading.** No entry (single-verse crux). |
| 10 | Lacuna markers ○○○［ (1:23, 29, 39, 71) | **Resolved** → entry `lacuna-redaction-marker-convention-…` (`direct`). **Preserve verbatim** in both ja and en (over bracketed ellipsis / footnote). |
| 11 | 金輪王 + Takamagahara / Ryūmonkan / 生神 (1:49, 53, 71) | **Resolved** → entry `konrinno-mythic-cosmological-toponyms-…` (`inferred`). **Hybrid:** translate the title "Golden-Wheel King" (cakravartin); retain-with-gloss the named loci (Takamagahara, Ryūmonkan, ikigami). |
| 12 | 1:52 国常立尊 identification (1:52) | **Resolved** → folded into `ushitora-…` entry (`direct`) + commentary. **Apposition, both romanized**, following the source's own equation; not collapsed. |
| 13 | から kara = China vs Korea (1:60) | **Resolved in commentary; interpretive-default flag.** **China (唐)** on the 1892 dating + war sequence (then Russia 1:63, then world war). Recorded as a default, not a certainty. No entry (single occurrence). |
| 14 | 直 / Nao name-vs-adverb pun (1:45, 91, 92) | **Resolved** → entry `deguchi-nao-name-adverb-pun-…` (`inferred`). **Read 直 as the name "Nao"** (kami's lament for the medium); adverbial "truly/directly" carried in the same clause + noted. |
| 15 | Sensitive vocabulary (1:4, 5, 6, 24, 25, 30) | **Resolved** → entry `sensitive-register-accuracy-first-contextualize-…` (`direct`). **Literal English kept** (獣類 "beasts", 悪魔 "devils", 盲目聾 "blind and deaf", 外国人 "foreigners") — neither softened nor amplified — **plus scholarly framing notes** at 1:4 and 1:24 (pre-militarist 1892 dating; oracular/figurative idiom). |
| 16 | 大本 Ōmoto site vs "great origin" (1:17, 39, 40, 50, 53, 56, 59) | **Resolved** → entry `omoto-site-vs-great-origin-…` (`inferred`). **Split:** "the Ōmoto" (site/movement) vs "the great origin" (common noun); site-sense flagged proleptic (not yet formally named in 1892). |
| 17 | Orthographic variants; 1:1 一同/一度 (1:1) | **Resolved** → entry `oomoto-shinyu-collation-witnesses-…` (`direct`) + **1 authorized English edit**. ja kept as-is; printed **一同 = "all together"** followed over the witness's 一度 "at one stroke"; variant recorded; **single-edition pass held pending** (38/93 match). |
| 18 | 水晶魂 crystal soul / 霊魂 (1:76, 85, 86) | **Resolved** → entry `crystal-soul-soul-purification-…` (`inferred`). **"crystal soul"** (metaphor retained) + 霊魂の改め = **"the sifting of souls"**. |

All 18 `editorial_questions[]` cleared to `[]`.

---

## Authorized English edits (each backed by a glossary entry)

Per the hard rule that `i18n.en` may not change without a corresponding
glossary change, the **1 edit** is:

- **OSHIN-1:1** — "…all at once, the plum blossom opens…" → "…**all
  together**, the plum blossom opens…" (printed 一同 *ichidō* "all as one",
  disambiguated from the ambiguous "all at once" which leant toward the
  witness variant 一度 *ichido* "at one stroke"; backed by
  `oomoto-shinyu-collation-witnesses-…`).

No `ja` fields were altered anywhere. The draft had already implemented the
default renderings for most technical terms (kami, shinkoku,
tatekae-tatenaoshi, kaishin, crystal soul, Golden-Wheel King), so this pass
is predominantly **ratification + glossary-backing + commentary**, not
re-translation.

---

## Glossary changes for review

### Central glossary

**No in-agent edits** (hard-rule compliance: the ~4 MB central glossary was
not loaded or modified). No Japanese lemma exists centrally, and none was
promoted this pass. The Hepburn-romanization and (eventually) the core
Ōmoto-cosmology entries are **promotion candidates** if a second Japanese
text enters the corpus.

### Per-translation overlay (new file, v1.0.0)

**Added (16 entries):**

1. `hepburn-romanization-convention-oomoto-shinyu-woh` (`direct`) — promotion candidate (project-wide Japanese convention)
2. `zoyo-oracular-ender-unmarked-declarative-oomoto-shinyu-woh` (`direct`)
3. `ushitora-no-konjin-theonym-oomoto-shinyu-woh` (`direct`) — incl. the 1:52 Kunitokotachi identification
4. `sanzen-sekai-three-thousand-worlds-oomoto-shinyu-woh` (`inferred`)
5. `tatekae-tatenaoshi-reconstruction-renewal-oomoto-shinyu-woh` (`inferred`)
6. `kaishin-change-of-heart-oomoto-shinyu-woh` (`inferred`)
7. `kami-neutral-theism-oomoto-shinyu-woh` (`inferred`) — **the load-bearing lens decision** (neutral "the kami")
8. `shinkoku-divine-land-oomoto-shinyu-woh` (`inferred`)
9. `kamibashira-shugojin-shugonin-guardian-hierarchy-oomoto-shinyu-woh` (`inferred`)
10. `lacuna-redaction-marker-convention-oomoto-shinyu-woh` (`direct`)
11. `konrinno-mythic-cosmological-toponyms-oomoto-shinyu-woh` (`inferred`)
12. `omoto-site-vs-great-origin-oomoto-shinyu-woh` (`inferred`)
13. `deguchi-nao-name-adverb-pun-oomoto-shinyu-woh` (`inferred`)
14. `sensitive-register-accuracy-first-contextualize-oomoto-shinyu-woh` (`direct`)
15. `crystal-soul-soul-purification-oomoto-shinyu-woh` (`inferred`)
16. `oomoto-shinyu-collation-witnesses-reikaimonogatari-partial-orthographic-variants` (`direct`)

**Modified / promoted:** none (new file).

**Proposed but NOT committed (escalated):**
`kami-elohim-frame-identification-oomoto-shinyu-woh` (`speculative`).

---

## Recommended next steps for the Reviewer

1. **Rule on the escalated kami/Elohim-frame `speculative` item by name.**
   Editor recommendation: **keep 神 neutral ("the kami"), no Elohim in any
   line, resonance in the 1:52 comparative note only, do not commit the
   entry** — extending the ratified 2026-07-03 *b-h-y* ruling to the
   Japanese corpus. This is a primary blocker for advancement past
   `editor-review`.
2. **Confirm the sensitive-register handling** — literal English kept for
   獣類/悪魔/外国人/盲目聾, with framing notes at 1:4 and 1:24. Confirm the
   text is neither sanitized nor amplified and that the framing register is
   right (contextualize, not endorse).
3. **Action the pending single-edition philological pass** (the second
   blocker). Only 38/93 verses matched the reikaimonogatari.net witness
   exactly after furigana-stripping; the verification status is held at
   **witness-confirmed-collation-partial** and must not be signed off as
   verified. In particular settle the OSHIN-1:1 一同/一度 variant against an
   authoritative Ōmoto Shin'yu edition and lock verse numbering.
4. **Resolve 玉芝 (Tamashiba) at OSHIN-1:14** — a specialist philological
   crux with no secure referent; the WoH renders it as a bare romanized
   place-name pending expert reading.
5. **Confirm the から = China (唐) interpretive default at OSHIN-1:60** (over
   Korea 韓), on the 1892 dating + prophetic war-sequence.
6. **Confirm the core technical mappings** — sanzen sekai "three-thousand
   worlds" (literal); tatekae-tatenaoshi "reconstruction and renewal";
   kaishin "change of heart"; shinkoku "divine land" (not "divine nation");
   the 神柱/守護神/守護人 three-way split; "crystal soul" + "sifting of souls".
7. **Confirm the Hepburn convention** and the ぞよ "unmarked declarative"
   policy as the standard for Japanese-source texts (both promotion
   candidates).
8. **Confirm** chapter-1.json structural validation: 93 paragraphs; all 255
   `glossaryRefs` resolve to overlay entries; commentary on the 31
   divergent paragraphs and empty elsewhere; `editorial_questions` cleared;
   status `editor-review`, version `1.0.0-rc1`, overlay v1.0.0.

After Reviewer sign-off (including an explicit ruling by name on the
kami/Elohim `speculative` item and clearance of the pending philological
pass), the chapter advances from `editor-review` to `reviewer-approved`,
then to `published` after human sign-off.
