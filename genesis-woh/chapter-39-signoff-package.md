# Genesis 39 — sign-off package

**Status:** reviewer-approved (clean approve sweep after one corrective pass; sign-off is formality)
**Chapter:** 39 — **Yosef in Potifar's house.** The Yosef cycle resumes in Egypt: Yosef sold to Potifar (*seris Par'oh, sar ha-tabbachim*); "YHWH was with Yosef" and he prospers as overseer; Potifar's wife's advance and Yosef's refusal ("how can I sin against Elohim"); the seized garment and the false accusation; Yosef cast into the *beit ha-sohar* (prison); the refrain returns — "YHWH was with Yosef" — and he is given charge of all the prisoners.
**Version:** 1.0.0-rc1
**Glossary version:** central v2.38.0 + overlay v1.7.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 23 / 23 |
| Reviewer verdicts | **23 approve / 0 revise / 0 flag** |
| New glossary entries | 5 total (2 central + 3 overlay) |
| AppliesTo / scope edits | 3 central (`saris`, `sar-ha-tabbachim` +GEN-WOH-39:1; `ha-ivri` refId normalized) + 1 bidirectional cross-ref (corrective) |
| Glossary verdicts | **6 approve / 0 revise / 0 flag** (after corrective pass) |
| Verses with commentary | 9 / 23 |
| Lens-leakage flags | **0** |
| Speculative entries | **0** (all 5 new entries `inferred`) |
| Items requiring human-only judgement | **0** |

## The 2 new central entries (v2.37.0 → v2.38.0)

| Slug | claim_type | Notes |
|---|---|---|
| `beit-ha-sohar-prison-round-house` | `inferred` | vv20-23; ASV "prison"; *sohar* etymology debate (Egyptian loanword / "round-house" / Akkadian) documented, not adjudicated; distinguished from the Gen 37 *bor* and the *beit ha-bor* of Gen 40:15/41:14; recurs Gen 40-41 → central |
| `chesed-solitary-covenant-kindness` | `inferred` | v21; solitary *chesed* (~245 HB occurrences); genuine companion to (not duplicate of) the existing `chesed-v-emet` pair-entry; ASV "kindness"; covenant-loyalty range (Glueck/Sakenfeld) in apparatus |

Central scope-edits (no decision/rationale change): `saris-court-official-eunuch-ambiguity` and `sar-ha-tabbachim-captain-of-the-guard` appliesTo += GEN-WOH-39:1; `ha-ivri-hebrew-etymology` Gen 39 refs normalized from bare `GEN-39:` to corpus `GEN-WOH-39:` form.

## The 3 new overlay entries (v1.7.0)

| Slug | claim_type | Notes |
|---|---|---|
| `yosef-cycle-divine-name-alternation-yhwh-elohim` | `inferred` | vv2,3,5,9,21,23; Gen 39 as the cycle's SOLE YHWH-frame chapter (narrator's YHWH vs. Elohim in Yosef's mouth at v9); documents ONLY the named documentary-critical reading (Wellhausen, von Rad, Westermann, Redford, Friedman); WoH synthesis explicitly wiki-reserved; **the designated lens-risk item — Reviewer scrutinized, zero leakage** |
| `yefeh-toar-beauty-formula-rachel-yosef` | `inferred` | v6; the masc. "beautiful in form and fair to look upon" formula is verbatim the fem. Rachel formula (Gen 29:17); ASV rendered identically so the Hebrew echo survives in English |
| `le-tzachek-mockery-piel-gen39` | `inferred` | vv14,17; the *tzachaq* mockery/innuendo sense; **genuine sibling** (bidirectional cross-ref by id) to the central Gen 21:9/26:8 tz-ch-q entry — NOT an appliesTo-extension |

## Process note — one corrective pass

The Reviewer's first pass approved all 23 verses but returned a single `revise` on `le-tzachek-mockery-piel-gen39`: it claimed a "bidirectional" cross-reference to the central tz-ch-q entry, but the central entry didn't name the sibling back. **Not a translation defect — a glossary-housekeeping bug.** The Editor fixed it by adding the sibling's id to the central `metzacheq-conjugal-vs-contested-disambiguation` entry's rationale (the corpus's prose-by-id sibling convention, matching the Gen 37↔38 `haker-na` precedent), bumping central v2.37.0 → v2.38.0 (semver-minor, per the glossary's uniform `.0` history). The Reviewer re-verified the fix in isolation and flipped the verdict to `approve`. The chapter is now a clean sweep.

## Items requiring decision

**None.** Clean reviewer-approved sweep — every verse and every glossary entry approved, zero lens-leakage, zero speculative entries. The lens-risk item (the YHWH/Elohim divine-name alternation) was handled exactly to spec: both names rendered as the MT distributes them, documentary-critical reading documented as named scholarship, no WoH cosmological synthesis.

## Editor escalation report (inlined)

See `chapter-39-editor-report.md` — no speculative entries; lens-discipline applied at the divine-name alternation entry; the corrective-pass section documents the cross-ref fix; promotion-candidate ledger carried forward with new Gen 39 nodes (`beit ha-sohar` → Gen 40-41; solitary `chesed` → Gen 40:14/47:29 onward; the tz-ch-q sibling-cluster; the beauty-formula seed).

## Reviewer report (inlined)

Appended to `chapter-39.json` `translation.reviewerReport`: 23 per-verse verdicts (all approve), 6 glossary verdicts (all approve after the corrective pass), 0 lens-leakage flags. Source re-parsed independently; escalation report read only after forming verdicts.

## Recommendation

Clean pass on philology, glossary architecture, and lens-discipline. The chapter's lens-risk item — the YHWH/Elohim alternation that documentary criticism reads source-critically — is documented as named scholarship with no WoH synthesis. If you agree, reply **sign-off ok** and I'll ship Gen 39 (stable / 1.0.0, _meta + catalog bump, www submodule pointer bump, three-repo push).
