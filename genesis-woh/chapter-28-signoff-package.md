# Genesis 28 — sign-off package

**Status:** awaiting-human (one minor project-convention call on glossary appliesTo coverage)
**Chapter:** 28 — Jacob's ladder. **The highest-lens-leverage theophany in the Jacob cycle.**
**Version:** 1.0.0-rc1
**Glossary version:** 2.26.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 22 / 22 |
| Reviewer verdicts | **22 approve / 0 revise / 0 flag** |
| New glossary entries | 11 (all `direct`, 0 inferred, 0 speculative) |
| AppliesTo expansions | 6 (5 approved · **1 flag-for-human**) |
| Verses with commentary | 14 / 22 |
| Verses with glossaryRefs | 14 / 22 |
| Lens-leakage flags | **0** |
| Items requiring human-only judgement | **1 (a project-convention call)** |

## The one item requiring sign-off

The Editor extended the **singular** `malakh-elohim-messenger` entry (from Gen 16/21 — the *malakh Elohim* of the Hagar scenes) to also cover GEN-WOH-28:12, **and** created a new **plural** entry `malakhei-elohim-ascending-descending` covering the same verse. The Reviewer flagged this dual-coverage as a project-convention call.

**The verse:** *hineh malakhei Elohim olim v-yordim bo* — "behold, messengers of Elohim ascending and descending on it." The Hebrew is grammatically plural; the existing `malakh-elohim-messenger` entry covers singular occurrences.

**Two options:**

**Option A — keep dual-coverage.** Both the singular `malakh-elohim-messenger` entry AND the new plural `malakhei-elohim-ascending-descending` entry point to Gen 28:12. Maximum cross-reference visibility; readers landing on either entry see the connection.

**Option B — clean separation.** The new plural entry is the canonical home for Gen 28:12; the singular entry covers only singular occurrences. Removes the dual-coverage. Less cross-referencing noise.

**My recommendation: Option B (clean separation).** The new plural entry already documents the singular/plural distinction and cross-references the singular entry in its rationale. Dual-coverage creates a maintenance burden — if either entry's framing later changes, both have to be kept in sync. Clean separation matches the project's existing convention where each refId has one canonical-home entry.

If you choose Option B, the fix is a one-line edit removing GEN-WOH-28:12 from `malakh-elohim-messenger.appliesTo`.

## The chapter's signature wins (Reviewer-verified)

**`sulam-stairway-or-ladder`** — WoH chose "stairway" departing from ASV "ladder." Houtman 1977 *VT* 27; Sarna, Speiser, Hamilton, Westermann all adopt stairway. Akkadian *simmiltu ša šamê* + Gen 11:4 verbal echo (*u-rosho ba-shamayim*) documentary.

**`beit-elohim-shaar-ha-shamayim-cultic-formula`** — Akkadian *bab-ili* (gate-of-god) Babel-echo + Gen 11 polemic-reversal HB-explicit. NT John 1:51 + Gen Rab 69:7 receptions flagged-not-preempted in apparatus, NOT in English text.

**`matzevah-sacred-pillar-patriarchal-religion`** — Cross-corpus patriarchal-affirmation / Deuteronomic-prohibition / prophetic-lament distribution. Alt 1929 / Cross 1973 / Smith 2001 / Mettinger 1995 patriarchal-El-religion reading as mainstream consensus. Archaeological context (Hazor, Gezer, Arad masseboth) documented.

**`yaakov-vow-tithe-promise`** — First HB *neder*; second pre-Sinai *ma'aser*. Cartledge 1992 *JSOTSup 147*.

## Lens posture verification (Reviewer's verbatim)

> *"Zero flags. Discipline held verse by verse. The translated English reads as a defensible scholarly translation of Genesis 28. A credentialed Hebrew Bible scholar would NOT detect 'this is a WoH translation' from the English alone:*
> - *No 'spacecraft-ramp' framing of the sulam*
> - *No 'marker-of-extraterrestrial-visit' framing of the matzevah*
> - *No 'physical-portal' framing of the sha'ar ha-shamayim*
> 
> *The WoH lens-distinctive synthesis on all three load-bearing lexemes is explicitly reserved for the wiki per each entry's final paragraph, and does not enter either the English text or the glossary rationales."*

## All 11 new entries (v2.26.0)

| Slug | Notes |
|---|---|
| `qhal-amim-assembly-of-peoples-blessing` | v 3; Gen 35:11, 48:4 cross-refs |
| `birkat-avraham-blessing-transmission` | v 4; Abrahamic-promise cluster |
| `paga-ba-maqom-cultic-encounter` | v 11; *paga* polysemy + *ha-maqom* definite-article cultic-signal |
| `sulam-stairway-or-ladder` | v 12; stairway-departure from ASV-ladder |
| `malakhei-elohim-ascending-descending` | v 12; plural messengers; distinct from singular *malakh* |
| `yhwh-nitzav-alav-ladder-position-dispute` | v 13; *alav* three readings |
| `akhen-yesh-yhwh-discovery-of-sacred-place` | v 16; Exod 3:5, Josh 5:15, Judg 13:22 cross-refs |
| `beit-elohim-shaar-ha-shamayim-cultic-formula` | v 17; Akkadian *bab-ili* Babel-echo |
| `matzevah-sacred-pillar-patriarchal-religion` | v 18; patriarchal-El-religion + later-Yahwism-suppression |
| `bethel-luz-name-etymology` | v 19; Gen 35:6-7, Josh 16:2, Judg 1:23-26 cross-refs |
| `yaakov-vow-tithe-promise` | vv 20-22; first HB *neder*; second pre-Sinai *ma'aser* |

## Sign-off requested

Choose Option A (dual-coverage) or Option B (clean separation) for the `malakh-elohim-messenger` appliesTo question; either way I'll ship.

## Editor escalation report

See `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-28-editor-report.md`.

## Reviewer report

Embedded in chapter JSON at `translation.reviewerReport`. Citations from Westermann, Sarna, Wenham, Hamilton, Speiser, Alter (standard Genesis); Houtman 1977 *VT* 27, Cohen 1978 *JANES* 9 (sulam); Heidel 1951 *The Babylonian Genesis*, ANET (bab-ili); Alt 1929 *Der Gott der Väter*, Cross 1973 *CMHE*, Smith 2001 *The Origins of Biblical Monotheism*, Mettinger 1995 *No Graven Image?* (matzevah); Cartledge 1992 *JSOTSup 147* (vows); Brown 1966 *Anchor John I-XII* (NT John 1:51 reception); Genesis Rabbah 68:12, 69:7, b. Chullin 91b (rabbinic reception).
