# Genesis 27 — sign-off package

**Status:** awaiting-human (one internal-consistency bug at v 39 requires human resolution; everything else clean)
**Chapter:** 27 — Isaac's blessing-deception. One of the most dramatic patriarchal narratives.
**Version:** 1.0.0-rc1
**Glossary version:** 2.25.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 46 / 46 |
| Reviewer verdicts | 45 approve / 0 revise / **1 flag-for-human (v 39)** |
| New glossary entries | 12 (11 `direct`, 1 `inferred`, 0 speculative) |
| Glossary verdicts | 11 approve / **1 flag-for-human (same v 39 entry)** |
| Verses with commentary | 12 / 46 |
| Verses with glossaryRefs | 19 / 46 |
| Lens-leakage flags | **0** |
| Items requiring human-only judgement | **1 (the v 39 *mi-shemanei* internal inconsistency)** |

## The v 39 internal-consistency bug

**The Reviewer caught a real bug**: the chapter file and the new glossary entry disagree with each other on which reading of *mi-shemanei ha-aretz* the WoH translation adopts.

- **Chapter `i18n.en` at v 39:** *"Behold, **of** the fatness of the land shall be your dwelling, and **of** the dew of the skies from above."* (**PARTITIVE**)
- **Chapter commentary at v 39:** declares partitive-as-WoH-choice.
- **Escalation report line 23:** declares partitive-as-WoH-choice.
- **Glossary entry `mi-shemanei-ha-aretz-partitive-vs-separative.wohChoice`:** declares **SEPARATIVE** ("away from the fatness")

The lexical work in both files is sound and presents both readings; only the `wohChoice` declaration disagrees. I'd asked the Editor to choose separative (modern critical: Sarna, Westermann, Speiser, NRSV — context-favoring because Esau is supposed to get the LESSER blessing, and partitive makes it nearly identical to Jacob's at v 28). The Editor wrote separative in the glossary entry but partitive in the chapter text and commentary. Two invocations + a stream timeout in the middle probably introduced the drift.

### Two clean resolution paths

**Option A: keep partitive (the chapter's de-facto choice).** Update the glossary entry's `wohChoice` to flip to partitive. Rationale:
- ASV / KJV / NJPS all read partitive
- Rabbinic-harmonizing tradition reads partitive (the apparent doubling is harmonized as "Esau too gets some fatness, just less of it" — Rashi etc.)
- Methodologically symmetric with the *nivrakhu* PD-default precedent (when modern critical splits the question, prefer the older PD translation)
- Reviewer's recommended resolution

**Option B: switch to separative (my original prompt direction).** Update the chapter text + commentary + escalation report to separative. Rationale:
- Modern critical consensus (Westermann, Speiser, Sarna apparatus, NRSV) reads separative
- Context: Esau is being given the LESSER blessing; the partitive reading makes Esau's blessing functionally identical to Jacob's (same dew, same fatness)
- Geographically defensible: Edom's territory is arid/desert relative to Canaan's
- The chapter's irony then lands cleanly: Jacob gets "from-the-fatness-as-portion"; Esau gets "from-the-fatness-as-distance"

**My recommendation: Option B (separative).** The context-favoring argument is strong (Esau is *supposed* to get the lesser blessing) and the modern critical consensus is wider than NJPS/ASV on this specific verse. But Option A is fully defensible and is the safer PD-fidelity choice. Either is a real philological position; this is a project-policy decision, not a technical fix.

If you choose Option A, the fix is one string edit (the glossary entry's `wohChoice` field). If you choose Option B, the fix is three edits (chapter v 39 i18n.en + chapter v 39 commentary + escalation report). I can apply either.

## The 12 new entries (v2.25.0)

| Slug | Notes |
|---|---|
| `matamim-savory-food-blessing-meal` | vv 4, 7, 9, 14, 17, 31; Prov 23:3, 2 Sam 13 cross-corpus |
| `nefesh-blessing-transfer` | vv 4, 19, 25, 31; Wolff 1974 *Anthropology of the OT* |
| `ha-qol-qol-yaakov-deception-formula` | v 22; chapter's irony-formula; rabbinic reception flagged-not-preempted |
| `tal-shamayim-shemanei-aretz-blessing-formula` | v 28; Deut 33:13, 28 Joseph-parallel |
| `yaavdukha-amim-peoples-shall-serve-formula` | v 29; Gen 9:25-27, Num 24:9, Ps 72:11, Isa 49:23 |
| `cursed-cursers-blessed-blessers-echo` | v 29; explicit echo of Gen 12:3 |
| `va-yecherad-charadah-trembling-formula` | v 33; blessing-irrevocability; 1 Sam 14:15, Dan 10:7 |
| `tzaaqah-gedolah-u-marah-bitter-cry` | v 34; Esther 4:1 verbatim |
| `mi-shemanei-ha-aretz-partitive-vs-separative` | vv 39-40; **THE V 39 BUG** |
| `cherev-tichye-by-the-sword-edom-tradition` | v 40; Bartlett 1989, Knauf *ABD*; 2 Kgs 8, Mal 1, Obadiah |
| `isaac-blindness-deception-frame` | v 1; Gen 48:10 Jacob-Joseph parallel |
| `rebekah-pretext-hittite-wives-cover` (only `inferred`) | v 46; Alter 1981 narrator-irony |

## Reviewer's verification of everything else

> *"Quality of the Editor's work is high. All 11 `direct` classifications hold against independent re-parse of MT... A credentialed scholar reading the English cold would not detect WoH-distinctive interpretive content."*

The Reviewer specifically affirmed:
- The chiastic doublet at v 22 (*ha-qol qol Yaakov*)
- The cognate accusatives at vv 33 (*charadah gedolah*) and 34 (*tza'aqah gedolah u-marah*)
- The qere/ketiv discipline at v 29 (*yishtachavu*)
- The *satam*-vs-*saneʾ* nuance at v 41
- The Esther 4:1 verbal-borrowing at v 34
- The Avrahamic-curse-blessing echo at v 29
- The `inferred` classification on `rebekah-pretext-hittite-wives-cover` — *"Alter (1981 ch. 6) and Sternberg (1985, 354-364) both read the scene this way; it is narrative-grammar inference, not lens-application."*
- No lens-leakage — Pauline Rom 9:13, rabbinic Esau-as-Rome, Genesis Rabbah 65:20's *qol*-as-Torah / *yadayim*-as-violence allegory, Hebrews 12:17 blessing-irrevocability — all flagged-not-preempted in apparatus only.

## Production note: pipeline recovery

The Editor pass was completed in two invocations due to a stream-idle timeout. First invocation added all 12 glossary entries (385 → 397 terms); second invocation completed the chapter file work and wrote the escalation report. The v 39 inconsistency may have been introduced at the seam between the two invocations. Audit trail intact across both.

## Sign-off requested

**Choose Option A (partitive) or Option B (separative) for v 39**, then I'll apply the one-or-three-edit fix and ship.

## Editor escalation report

See `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-27-editor-report.md`.

## Reviewer report

Embedded in chapter JSON at `translation.reviewerReport`. Citations from Westermann, Sarna, Wenham, Hamilton, Speiser, Alter (standard Genesis); Wolff 1974 (*nefesh*); Sternberg 1985 *Poetics of Biblical Narrative*, Alter 1981 (deception-ethics + Rebekah-pretext); Bartlett 1989, Knauf 1992 *ABD* (Edom); Esther 4:1, b. Bava Batra 16b, Genesis Rabbah 65-67, Rashi (reception traditions); BDB, HALOT (lexica).
