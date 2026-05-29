# Genesis 38 — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality)
**Chapter:** 38 — **The Judah–Tamar interlude.** The self-contained unit that interrupts the Yosef cycle: Yehudah leaves his brothers and marries bat-Shua; the deaths of Er and Onan; the levirate duty (*yibbum*) withheld from Shelah; Tamar's veiled wait at Petach Einayim; the pledge-triad (signet, cord, staff); the *zonah*/*qedeshah* exchange; the burning verdict reversed by *haker-na* and *tzadqah mimmeni*; the twin birth of Peretz (the Davidic-messianic ancestor) and Zerach.
**Version:** 1.0.0-rc1
**Glossary version:** central v2.36.0 + overlay v1.6.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 30 / 30 |
| Reviewer verdicts | **30 approve / 0 revise / 0 flag** |
| New glossary entries | 10 total (3 central + 7 overlay) |
| AppliesTo extensions | 1 central (`zonah-...` + GEN-WOH-38:15, 38:24) |
| Glossary verdicts | **11 approve / 0 revise / 0 flag** |
| Verses with commentary | 17 / 30 |
| Lens-leakage flags | **0** |
| Speculative entries | **0** (all 10 new entries `inferred`) |
| Items requiring human-only judgement | **0** |

## The 3 new central entries (v2.36.0)

| Slug | claim_type | Notes |
|---|---|---|
| `yibbum-levirate-marriage-institution` | `inferred` | vv8-10; the levirate-marriage technical term; cross-corpus Deut 25:5-10 (institution) + Ruth 4 (redemption-marriage); ASV periphrasis kept; institution documented without synthesis |
| `qedeshah-consecrated-woman-sacred-prostitution-crux` | `inferred` | vv21-22; **the MAJOR crux** — transliterated on surface to preserve the *zonah*→*qedeshah* shift; documents BOTH the traditional cultic-prostitution reading (Albright/Speiser) AND the revisionist denial (Budin, Westenholz, Gruber, Bird, Frymer-Kensky) even-handedly; cross-corpus Deut 23:18, Hos 4:14 |
| `peretz-breach-davidic-ancestor-etymology` | `inferred` | v29; *mah-paratzta* / "breach"; central on the Davidic-messianic line reach (Ruth 4:18-22, 1 Chr 2, Matt 1:3) |

Plus appliesTo extension: `zonah-prostitute-status-vocabulary-cross-corpus` += GEN-WOH-38:15, 38:24 (closes the rationale-vs-scope gap the Translator flagged).

## The 7 new overlay entries (v1.6.0)

| Slug | claim_type | Notes |
|---|---|---|
| `zera-levirate-progeny-raise-up-seed` | `inferred` | vv8-9; "seed/offspring" in the levirate-reckoning sense |
| `ve-shichet-artzah-onan-euphemism` | `inferred` | v9; the Onan euphemism ("spilled it on the ground") |
| `petach-einayim-toponym-eyes-pun` | `inferred` | v14; "entrance to Enaim" / "opening of the eyes" toponym-pun (+ *tza'if* veil, *tit'allaf*) |
| `eravon-pledge-triad-signet-cord-staff` | `inferred` | vv17-18; the *eravon* pledge + *chotam/petil/matteh* triad |
| `haker-na-tamar-recognition-gen38` | `inferred` | v25; **the ratified Gen 37→38 sibling** — bidirectional cross-ref to the Gen 37 `haker-na-nakar-recognition-motif`; the measure-for-measure echo (brothers deceive Ya'aqov with the coat / Tamar turns the words on Yehudah with the pledge); NOT an appliesTo-extension |
| `tzadqah-mimmeni-she-is-in-the-right` | `inferred` | v26; *tzedaqah* "she is more righteous than I"; comparative-vs-forensic *min* documented |
| `zerach-shining-scarlet-etymology` | `inferred` | v30; the scarlet-thread twin; *zarach* "to shine/rise" / *shani* |

## Items requiring decision

**None.** Clean reviewer-approved sweep — every verse and every glossary entry approved, zero lens-leakage, zero speculative entries. The two questions the Editor surfaced were both resolved against established convention and confirmed by the Reviewer:

- **YHWH stands** (not "Yahweh") — verified against stable chapters 15, 18, 22, 28 + all 20 prior occurrences; the brief's "Yahweh" deferred to a future deliberate retransliteration pass.
- **`qedeshah` / `yibbum` held at `inferred`** (not `direct`) — the Reviewer independently confirmed the calibration: the recorded substance in each is a contested/interpretive layer, not a self-evident gloss.

## Editor escalation report (inlined)

See `chapter-38-editor-report.md` — no speculative entries; lens-discipline applied at the *qedeshah* crux (both sacred-prostitution camps documented as named positions, no surface adjudication); full central-vs-overlay reasoning; the Gen 27/37/38 *haker-na* recognition-doublet now complete; four new cross-corpus promotion nodes (yibbum→Deut/Ruth, Peretz→Davidic line, qedeshah→Deut/Hos/Kings).

## Reviewer report (inlined)

Appended to `chapter-38.json` `translation.reviewerReport`: 30 per-verse verdicts (all approve), 11 glossary verdicts (all approve), 0 lens-leakage flags. Source re-parsed independently before evaluating the English; the escalation report read only after forming verdicts (corroborated every point, no revisions). The "no speculative" classification independently confirmed; the `haker-na` sibling verified as a genuine separate entry with bidirectional cross-reference (Gen 37 entry's appliesTo correctly remains [37:32]).

## Recommendation

Clean pass on philology, glossary architecture, and lens-discipline. The chapter's hardest item — the sacred-prostitution standoff at *qedeshah* — is handled exactly to spec: transliterated surface, both scholarly camps named, no adjudication. If you agree, reply **sign-off ok** and I'll ship Gen 38 (stable / 1.0.0, _meta + catalog bump, www submodule pointer bump, three-repo push).
