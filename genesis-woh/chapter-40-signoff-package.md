# Genesis 40 — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality)
**Chapter:** 40 — **The cupbearer and baker dreams in the *beit ha-sohar*.** The second movement of the Yosef dream-pattern: Pharaoh's two *sarisim* — the *sar ha-mashqim* and *sar ha-ofim* — offend, are imprisoned with Yosef; each dreams a dream in one night; Yosef ("do not interpretations belong to Elohim?") decodes them — the cupbearer's three branches and the baker's three baskets both reckoned three days; the *nasa rosh* idiom turned positively for the one and grimly punned for the other; the third day Pharaoh's birthday feast "lifts up the head" of both; the cupbearer is restored, the baker hanged — and the cupbearer forgets Yosef, setting up Gen 41.
**Version:** 1.0.0-rc1
**Glossary version:** central v2.39.0 + overlay v1.8.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 23 / 23 |
| Reviewer verdicts | **23 approve / 0 revise / 0 flag** |
| New glossary entries | 5 total (3 central + 2 overlay) |
| AppliesTo / scope edits | 5 central (saris, sar-ha-tabbachim, beit-ha-sohar, bor, chesed) + 1 overlay (divine-name) + ha-ivri refId normalization |
| Glossary verdicts | **12 approve / 0 revise / 0 flag** |
| Verses with commentary | 15 / 23 |
| Lens-leakage flags | **0** |
| Speculative entries | **0** (all 5 new entries `inferred`) |
| Items requiring human-only judgement | **0** |

## The 3 new central entries (v2.38.0 → v2.39.0)

| Slug | claim_type | Notes |
|---|---|---|
| `sar-ha-mashqim-sar-ha-ofim-chief-cupbearer-baker` | `inferred` | vv1-2; the cupbearer-chief + baker-chief court-titles housed as ONE combined entry (a single literary doublet, narratively inseparable); ASV "chief of the butlers" / "chief of the bakers"; central by *mashqeh* cross-corpus reach to Neh 1:11 + 1 Kgs 10:5 / 2 Chr 9:4 |
| `pitron-dream-interpretation-yosef-cycle` | `inferred` | vv5, 8, 12, 16, 18, 22; **THE Gen 40-41 keyword** — *pitron* noun and *p-t-r* verb are near-exclusive to the Yosef cycle in the HB; explicitly distinguished from `divine-dream-communication-formula` (Gen 20:3/31:24 theophanic dreams); the Aramaic *pesher* cognate noted; dream-as-symbolic-puzzle framing is the narrative's own literary theology (Husser, Oppenheim), NOT WoH synthesis |
| `nasa-rosh-lift-up-the-head-idiom` | `inferred` | vv13, 19, 20; the literary hinge — positive (restoration v13), weaponized (decapitation/hanging v19, *me-alekha*), neutral keystone (both lifted at the feast v20); ASV rendered uniformly so the English preserves the pun; cross-corpus census (Exod 30:12, Num 1/4/26) + 2 Kgs 25:27 = Jer 52:31 Jehoiachin release |

Central scope-edits (no decision/rationale change): `saris` +40:2, 40:7; `sar-ha-tabbachim` +40:3, 40:4; `beit-ha-sohar` +40:3, 40:5; `bor-pit-cistern-dry-water-shaft` +40:15; `chesed-solitary-covenant-kindness` +40:14. Plus `ha-ivri-hebrew-etymology` Gen 40:15 ref normalized from bare `GEN-40:` to corpus `GEN-WOH-40:` form.

## The 2 new overlay entries (v1.7.0 → v1.8.0)

| Slug | claim_type | Notes |
|---|---|---|
| `zoafim-troubled-faces-cupbearer-baker-gen40` | `inferred` | v6; "their countenances were sad" — the *za'af* sad/dejected range; chapter-singular use |
| `sallei-chori-baskets-of-white-bread-hapax-gen40` | `inferred` | v16; hapax — white-bread (*chur*) / white-baskets / openwork-wicker (*chor*) readings documented, no surface adjudication; ASV "white baskets" preserved |

Overlay scope-edit: `yosef-cycle-divine-name-alternation-yhwh-elohim` +40:8 — Gen 40:8 ("do not interpretations belong to *Elohim*?") is a confirming scope-extension of the same observation (the cycle's unmarked Elohim default reasserting itself outside the Gen 39 YHWH-frame, paralleling Gen 39:9 on Yosef's lips), NOT a sibling locus.

## Two Editor judgment calls — both ratified by the Reviewer

1. **Combined cupbearer/baker into one central entry** (not two separate entries) — the Reviewer affirmed: they are a single literary doublet within one *sar ha-X* office-title pattern, narratively inseparable; splitting would fragment the doublet.
2. **Treated Gen 40:8 Elohim as a scope-extension** of the Gen 39 divine-name entry (not a sibling) — the Reviewer affirmed: v8 is the cycle's *unmarked default* reasserting itself, not a *marked* echo of the Gen 39 YHWH-frame; sibling treatment is for marked-feature echoes, scope-extension is correct here.

## Items requiring decision

**None.** Clean reviewer-approved sweep — every verse and every glossary entry approved, zero lens-leakage, zero speculative entries. The two lens-risk sites (the *pitron* dream-interpretation framing and the v8 Elohim note in a dream-interpretation chapter) were both scrutinized and clean: rationales draw on named scholarship (Husser, Oppenheim, Wellhausen, von Rad, Westermann, Coats, Redford, Friedman), zero WoH cosmological synthesis.

## Editor escalation report (inlined)

See `chapter-40-editor-report.md` — no speculative entries; lens-discipline applied at *pitron* and the Elohim divine-name extension; full central-vs-overlay reasoning for the combined court-title decision; promotion-candidate ledger carried forward with new Gen 40 nodes (`pitron` already at central / governs Gen 41; the cupbearer/baker doublet sets up Gen 41).

## Reviewer report (inlined)

Appended to `chapter-40.json` `translation.reviewerReport`: 23 per-verse verdicts (all approve), 12 glossary verdicts (all approve), 0 lens-leakage flags. Source re-parsed independently before evaluating the English; the escalation report read only after forming verdicts.

## Recommendation

Clean pass on philology, glossary architecture, and lens-discipline. The chapter's hardest items — the *pitron* dream-interpretation keyword cluster and the *nasa rosh* idiom's deliberate dark reversal — are handled exactly to spec. If you agree, reply **sign-off ok** and I'll ship Gen 40 (stable / 1.0.0, _meta + catalog bump, www submodule pointer bump, three-repo push).
