# Job 42 — sign-off package

**Status:** awaiting-human (review-approved by `claude-opus-4-7 acting as woh-reviewer`, 2026-05-22)
**Chapter:** 42 — Job's final response and the restoration epilogue
**Version:** 1.0.0-rc1
**Glossary version:** 2.8.0
**Source:** Tanach with Ta'amei Hamikra (Westminster Leningrad Codex, Public Domain)

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 17 / 17 |
| Reviewer verdicts | 17 approve / 0 revise / 0 flag-for-human |
| Glossary entries added | 7 (6 direct, 1 inferred, 0 speculative) |
| Glossary entries: reviewer verdicts | 7 approve / 0 revise / 0 flag-for-human |
| Verses with commentary | 16 / 17 (v 1 omitted: pure narrative tag) |
| Verses with glossaryRefs | 10 / 17 (across 12 distinct entries — 7 new, 5 existing carried over from chs 1, 2, 38) |
| Lens-leakage flags | 0 |
| Translation-text changes from PD default | 1 (v 10: "fortunes" not "captivity") |
| PD-default reading retained where contested | 1 (v 6: ASV traditional retained) |
| Ketiv/qere variants surfaced | 4 (vv 2, 10, 11, 16 — all qere followed per standard) |

## Glossary entries added in v2.8.0 (Job 42)

| Slug | Claim type | Cross-corpus? | Verse(s) |
|---|---|---|---|
| `shema-ozen-eyni-ra-atkha` | direct | Job 42 only | v 5 (keystone) |
| `em-as-v-nikhamti-al-afar-va-efer` | direct | Job 42 only | v 6 |
| `lo-dibartem-elay-nekhonah` | direct | Job 42 only | vv 7-8 |
| `shav-et-shvut` | direct | yes — pan-HB (26+ occurrences across Deut/Jer/Ezek/Hos/Joel/Amos/Zeph/Ps/Lam) | v 10 |
| `kesitah` | direct | yes — Gen 33:19, Josh 24:32, Job 42:11 | v 11 |
| `yemimah-ketziah-keren-happukh` | inferred | Job 42 only | v 14 |
| `zaqen-u-s-va-yamim` | direct | yes — patriarchal-good-death formula across Gen 25:8 (Abraham), 35:29 (Isaac), 1 Chr 29:28 (David), 2 Chr 24:15 (Jehoiada), Job 42:17 | v 17 |

## Load-bearing decisions (both reviewer-approved)

### v 6 — `em'as v-nikhamti al afar va-efer`

Three modern philological readings:
- **(a) Traditional / ASV:** "Therefore I despise myself, and repent in dust and ashes"
- **(b) Newsom 2003:** "Therefore I retract / and find consolation in dust and ashes" (*nicham* = "be sorry, be comforted"; *em'as* without reflexive object = "retract, despise")
- **(c) Curtis 1979 / Patrick 1976:** "Therefore I retract / and am comforted concerning dust and ashes" (rejecting the repentance-in-dust trope, with continuity to 1:21 / 2:10's acceptance-of-the-given stance)

**Editor's choice:** retain ASV traditional (a).
**Editor's rationale:** specialist consensus has not converged; PD-default rule applies; all three readings preserved in commentary and glossary entry.
**Reviewer verdict:** approve. Reviewer notes own philological sympathy lies with (c) on contextual grounds, but "philological sympathy is not consensus and is not grounds to override the PD-default."

### v 10 — `shav et-shvut Iyov`

**Editor's choice:** "restored the fortunes of Job" (modern critical consensus) — departs from ASV's "turned the captivity of Job".
**Editor's rationale:** Bracke 1985 settled the *sh-w-b* cognate-accusative derivation against the *sh-b-h* captivity derivation. Job was never literally captive. Modern criticism (HALOT, Dahood, NRSV, NJPS, Newsom) is settled. The new `shav-et-shvut` entry will govern 26 future occurrences across the prophetic and poetic corpus, so the decision is recorded canonically now.
**Reviewer verdict:** approve. The v 6 / v 10 "inconsistency" is in fact the PD-default rule operating correctly in both directions — it holds when specialists have not converged (v 6) and yields when modern critical consensus is settled (v 10).

## Editor's escalation report (inlined)

See `/Users/zara/Development/github.com/wheelofheaven/data-library/job-woh/chapter-42-editor-report.md`.

Key items from the Editor's report (none blocking):
- v 6 reading choice flagged for Reviewer attention — Reviewer approved
- v 10 PD-default departure flagged for Reviewer attention — Reviewer approved
- Candidate `appliesTo[]` extensions to existing entries (`lo-yibatzer-mehem`, `tov-v-ra-nqabel`, `YHWH-natan-YHWH-laqach`) left unmodified per additive-only pass discipline — can be expanded in a future pass

## Reviewer report (inlined)

The full reviewer report block lives in the chapter file at `translation.reviewerReport`. Key fields:
- 17 verse verdicts, all `approve`, all with reasoning and (where contested) scholarly citations drawn from Newsom *NIB* IV (1996), Clines *WBC* 18B (2011), Habel *OTL* (1985), Pope *Anchor* (1973), Bracke *JSOT* 7/22 (1985)
- 7 glossary-entry verdicts, all `approve`, claim-types verified
- 0 lens-leakage flags. Lens correctly quiet throughout — Job 42 is wisdom-literature, not divine-council-disclosure
- `reviewerNote` confirms both load-bearing decisions reflect the correct epistemic posture

## Items requiring decision

**None.** Reviewer advanced status to `reviewer-approved` cleanly. No items flagged for human-only judgement.

## Sign-off requested

To complete: human reviewer (zarazinsfuss) sets:
- `translation.reviewer` to `"zarazinsfuss"`
- `translation.reviewedAt` to ISO 8601 sign-off timestamp
- `translation.version` to `"1.0.0"`
- `translation.status` to `"stable"`

Then deploy: glossary v2.8.0 + chapter-42 to data-content / data-library, mirror to www, FF submodule pointers in www. Job book becomes **6 chapters / 151 paragraphs / completes the book's keystone narrative arc** (chs 1-2 council frame + chs 38-42 voice-from-the-whirlwind closure).
