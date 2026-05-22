# Chapter 42 Editor Report

Job 42 — the closing chapter of the book of Job. 17 verses, 20 editorial
questions from the Translator, all resolved. 7 new glossary entries added
to the central glossary (v2.7.0 → v2.8.0). One translation-text change
driven by glossary decision (v 10: ASV's *turned the captivity* → modern
critical consensus *restored the fortunes*). Status advanced to
`editor-review`, version `1.0.0-rc1`.

The book of Job is wisdom-literature, not a divine-council-disclosure
text. The Wheel of Heaven lens stays quiet throughout this chapter,
surfacing only at vv 7–8 to note the structural connection between
YHWH's verdict on the friends and the *bnei-elohim* framing of chs 1–2.
No new lens-driven readings are introduced.

---

## Speculative entries requiring sign-off

**None.** All seven new entries are `direct` or `inferred`. The most
contested decision — Job 42:6's three-way philological dispute — is
recorded as `direct` because the entry presents the dispute and the
chosen reading is the most-attested PD-default (ASV's traditional
rendering); the alternative readings are surfaced in commentary, not
asserted in the running text.

---

## Glossary changes for review

### Central glossary (data-content/i18n/translation-glossary.json)

Version: 2.7.0 → 2.8.0 (semver-minor; additions only, no modifications
to existing entries). `scopeNote` updated to summarize Job 42 close.

Added (7):

1. **`shema-ozen-eyni-ra-atkha`** (`direct`) — the keystone verse 42:5,
   ear-hearing vs. eye-seeing epistemology. Resolves editorial_question
   on v 5. ASV chiastic structure preserved; Newsom NIB cited for the
   same preservation argument; NRSV's *by hearsay* smoothing rejected
   on the ground that the *ozen* / *eyin* pairing is the verse's
   meaning. Lens explicitly stays quiet.

2. **`em-as-v-nikhamti-al-afar-va-efer`** (`direct`) — the three-way
   philological dispute on 42:6. Resolves editorial_question on v 6.
   All three readings (traditional submission / Newsom retract-the-
   lament / Curtis comfort-without-repentance) are documented in the
   rationale. The English text retains ASV's traditional reading on
   three grounds: (a) the standing PD-default rule applies maximally
   where the source is genuinely underdetermined; (b) the *al afar
   va-efer* phrase echoes 2:8's ash-heap setting, supporting the
   locative reading; (c) the WoH lens has no stake in either reading.
   A small lens-note observes that reading (c) would continue the
   acceptance-of-the-given stance of 1:21 / 2:10, but does not
   override the philological default. Citations: Newsom NIB 1996/2003;
   Curtis JBL 1979; Patrick VT 1976; Clines WBC 2011; the ASV/KJV
   tradition; medieval Jewish commentators.

3. **`lo-dibartem-elay-nekhonah`** (`direct`) — YHWH's verdict on the
   friends, vv 7–8. Resolves editorial_questions on vv 7 and 8. The
   *elay* directional-vs-referential ambiguity documented; standard
   referential reading adopted; Habel OTL 1985's directional minority
   surfaced. The verdict's structural function (closes the *bnei-elohim*
   framing of chs 1–2) is the one place in the chapter where the WoH
   lens surfaces — minimally.

4. **`shav-et-shvut`** (`direct`) — the pan-HB restoration phrase,
   v 10. Resolves editorial_question on v 10. **Drives a translation
   change**: ASV's *turned the captivity* → NRSV/NJPS/Newsom's
   *restored the fortunes*. This is one of the rare cases where the
   WoH translation departs from the PD-default rule, on the ground
   that modern philological consensus (Bracke JSOT 1985; Dahood
   Biblica 1965; HALOT with qualification) has settled the question
   in favor of the cognate-accusative *sh-w-b* derivation. The entry
   will govern future translations of Deuteronomy, the Major and
   Minor Prophets, the Psalms, and Lamentations — recording the
   decision now avoids relitigating it across 26 future verses.

5. **`kesitah`** (`direct`) — the archaic currency-unit, v 11; also
   Gen 33:19 and Josh 24:32. Resolves editorial_question on v 11.
   Preserved untranslated per Newsom / NJPS convention.

6. **`yemimah-ketziah-keren-happukh`** (`inferred`) — Job's three
   daughters, v 14. Resolves editorial_question on v 14. The
   `inferred` classification reflects that the *cassia* reading for
   Ketziah is fully secure, the *dove* / *day-bright* reading for
   Yemimah is a scholarly inference among several proposals, and the
   *beautified-one* metaphorical extension for Keren-happukh goes
   beyond the literal *kohl-horn* sense. Names preserved
   transliterated in the running text per WoH convention; semantic
   readings glossed.

7. **`zaqen-u-s-va-yamim`** (`direct`) — the patriarchal-good-death
   formula, v 17; also Abraham (Gen 25:8), Isaac (Gen 35:29), David
   (1 Chr 29:28), Jehoiada (2 Chr 24:15). Resolves editorial_question
   on v 17. Cross-corpus entry; will govern future Genesis and
   Chronicles translations.

### Per-translation overlay (data-library/job-woh/_translation-glossary.json)

**None added.** All seven entries are cross-corpus or load-bearing
across the book of Job and warrant placement in the central glossary.
No per-translation overlay file is created at this time.

### Modified entries

**None.** The pass is additive only. The existing entries
`avdi-iyov`, `shlosha-re-ei-iyov`, `tov-v-ra-nqabel`,
`YHWH-natan-YHWH-laqach`, and `lo-yibatzer-mehem` are referenced from
Job 42 paragraphs without modification.

---

## Editorial decisions where I exercised judgment beyond the brief

### Entries the Editor chose NOT to create

The Translator flagged several candidate entries the Editor judged
better resolved in commentary alone:

- **`panav-essa-acceptance-idiom` (v 8)**. The Translator flagged the
  face-lifting idiom as a potential glossary entry. Editor decision:
  resolve in commentary on v 8 only. Grounds: the idiom appears widely
  in HB (Gen 19:21, Mal 1:8, et al.) and creating an entry here
  pre-commits the WoH translation to a face-idiom policy that should
  be set when the idiom recurs prominently in a future text (likely
  the Psalms or the prophetic blessings). Flagged for future
  consideration; the commentary in v 8 documents the idiom's range.

- **`shiv'anah-banim` (v 13)**. The Translator flagged the unusual
  *shiv'anah* numeral form as a potential glossary entry. Editor
  decision: resolve in commentary on v 13 only. Grounds: the minority
  *fourteen* reading (Pope, Newsom) is interesting but not adopted;
  the standard *seven* reading matches 1:2 exactly and preserves the
  intended same-number-not-doubled theological point. A glossary entry
  would over-elevate a hapax-form question.

- **`ra'ah-asher-hevi-YHWH` (v 11)**. The Translator flagged the
  narrator's attribution of Job's calamity directly to YHWH as a
  potential entry. Editor decision: resolve in commentary on v 11
  through cross-reference to the existing `YHWH-natan-YHWH-laqach`
  (1:21) and `tov-v-ra-nqabel` (2:10) entries. Grounds: the agentic
  attribution is consistent across the book's framing chapters, and
  the existing entries already capture the load-bearing claim; a new
  entry would duplicate without adding.

- **`nachalah-b-tokh-achehem` (v 15)**. The Translator flagged the
  daughter-inheritance arrangement. Editor decision: resolve in
  commentary on v 15 only. Grounds: the translation is uncontested
  (no lexical decision is at stake); the legal-philological
  significance is fully surfaced in the commentary; a glossary entry
  would record an interpretive point rather than a lexical decision,
  which is not what the glossary is for.

- **`lxx-iyov-appendix` (v 17)**. The Translator flagged the LXX
  appendix's Jobab identification as an optional glossary entry.
  Editor decision: resolve in commentary on v 17 only. Grounds:
  textual-tradition divergences are appropriately handled in
  commentary; the glossary records lexical decisions, not textual-
  criticism notes. The Jobab identification's content is fully
  surfaced in the v 17 commentary.

- **`re-i-iyov` for the singular-collective *re'ehu* (v 10)**. The
  Translator flagged whether to create a companion entry or extend
  the existing `shlosha-re-ei-iyov` entry. Editor decision: neither.
  The singular-collective is a routine Hebrew construction; the
  existing `shlosha-re-ei-iyov` entry is referenced and the
  commentary on v 10 notes the construction. No glossary work is
  needed.

### One translation-text change driven by glossary

Verse 10 is the only verse in the chapter where the English running
text was changed during the Editor pass. The Translator drafted *turned
the captivity of Job* (following ASV's PD-default). The Editor changed
this to *restored the fortunes of Job* on the strength of the new
`shav-et-shvut` glossary entry. This is documented explicitly in the
v 10 commentary and in the glossary entry's rationale. The change is
permitted under the rule that glossary state drives translation text;
the Editor created the entry first, then changed the text.

---

## Unresolved editorial questions

**None.** All 20 editorial_questions from the Translator pass are
resolved. The `editorial_questions[]` array is empty in the
editor-review output.

---

## Items flagged for Reviewer attention (not blocking)

- **The v 6 reading is the chapter's most-contested decision** and
  deserves Reviewer attention even though it does not require
  human sign-off as a speculative entry. The Editor retained the
  traditional submission reading on philological-default grounds;
  the Reviewer should confirm comfort with that choice or argue for
  the Newsom retract-the-lament reading. If the Reviewer prefers
  reading (b), the change is: English text becomes *Therefore I
  despise myself and repent of dust and ashes*; glossary entry
  `em-as-v-nikhamti-al-afar-va-efer` rationale needs revision.

- **The v 10 translation change** (*turned the captivity* → *restored
  the fortunes*) is a departure from the standing PD-default rule.
  The Reviewer should confirm comfort with adopting modern critical
  consensus over the PD default in this case. The argument for the
  departure is philological and pre-emptive (the entry will govern
  26 future verses across multiple books).

- **Cross-references to existing entries.** v 2 references
  `lo-yibatzer-mehem` (Gen 11:6) for the Babel echo; v 11 references
  `tov-v-ra-nqabel` (Job 2:10) and `YHWH-natan-YHWH-laqach` (Job 1:21)
  for the narrator's closing attribution. The Reviewer may want to
  consider extending those entries' `appliesTo[]` arrays to include
  Job 42:2 and Job 42:11 respectively, recording the structural
  echoes. The Editor did not modify the existing entries (the pass is
  additive only), but the cross-references are noted as candidate
  modifications for the next central-glossary minor version.

---

## Closing note

This pass closes the book of Job at chapter level. With chapters 1, 2,
38, 40, 41 already stable and 42 now in editor-review, the WoH
translation of Job has primary coverage of the framing chapters and
the divine-speech / epilogue arc. The remaining chapters (3–37, the
dialogue cycle, and 39, the first divine speech) are queued under the
project's prioritised text roadmap; the glossary entries created in
this pass (especially `shav-et-shvut`, `kesitah`, and
`zaqen-u-s-va-yamim`) will also be load-bearing for future translations
across Genesis, the prophets, and Chronicles.
