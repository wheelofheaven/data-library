# Isaiah 6 — sign-off package

**Status:** `awaiting-human` (clean review; **one item needs your explicit ratification** — see "Items requiring decision")
**Text:** Isaiah 6 (ISA-WOH) — the throne-room vision (Uzziah's death-year call-narrative). **13 verses**, `ISA-6:1`–`ISA-6:13`. **Opens the `isaiah-woh` book** — the corpus's next Hebrew-source text after Genesis, and the roadmap's #1 named pick.
**Chapter file:** `data-library/isaiah-woh/chapter-6.json`
**Version:** `1.0.0-rc1`
**Glossary version:** central **v2.71.0** + overlay **v1.0.0**
**Source:** Westminster Leningrad Codex, "Tanach with Ta'amei Hamikra" (Public Domain, tanach.us), fetched via Sefaria; cantillation + parasha marker preserved.

## Summary table

| Metric | Value |
|---|---|
| Verses translated | **13 / 13** (refId parity exact; MT pointed+cantillated echoed verbatim; `(פ)` parasha marker on 6:13 preserved) |
| Verses with `notes.official` commentary | 10 (6:1–3, 5, 6–10, 13; 6:4/6:11/6:12 left empty by the salient-verses policy) |
| Reviewer verdicts | **13 approve / 0 revise / 0 flag-for-human** (verses) |
| Reviewer glossary verdicts | **18 approve / 1 flag-for-human / 0 veto** |
| Reviewer lens-leakage flags | **0** |
| New overlay entries | **16** (v1.0.0) — **all 16 `direct`**, 0 inferred, 0 speculative |
| New central entries | **1** — `divine-council-first-person-plural-isa-6-8-heavenly-assembly-cross-corpus` (`direct`) |
| Central `appliesTo` activations | **2** — trishagion entry `+ISA-6:3`; hineni formula `+ISA-6:8` |
| Central glossary bump | **v2.70.0 → v2.71.0** (semver-minor) |
| Speculative entries | **0** |
| Items requiring human decision | **1** (ratify the new central divine-council entry — below) |

## Why this text matters (canon leverage)

Isaiah 6 is a **dense lens-leverage** chapter — the reason the roadmap ranks it #1:

- **The throne vision** (6:1): the enthroned deity "high and lifted up," the hem filling the *hêḵāl* — the *kavod*-tradition throne-scene that pairs with **Ezekiel 1**.
- **The seraphim** (6:2, 6): the winged "burning ones," six wings, the flying/covering — the divine-attendant tradition. Kept as "seraphim" in the line; the Ezekiel-1 / Revelation-4 / winged-attendant resonance is commentary-only.
- **YHWH of hosts** (*ṣᵉḇāʾôṯ*, 6:3, 5) and **the trishagion** (*qādôš×3*, 6:3): the heavenly-host / assembly reading and the *kavod* physical-presence register — commentary-only; the trishagion entry (shared with Revelation 4:8) is now wired to Isaiah.
- **The divine-council plural** (6:8): *ûmî yēleḵ-lānû* "who will go **for us**?" — the 1cp plural beside the singular "I." This is the **Council-of-Eternals seed** in Isaiah, the sibling to the Genesis cohortatives (1:26, 3:22, 11:7). Handled with full discipline: the literal plural is `direct` in the line and glossary; the council → Council-of-Eternals reading is `inferred` and lives only in the commentary/rationale.
- **The hardening commission** (6:9–10) and **the holy seed / stump** (6:13, MT retained with the LXX-minus disclosed).

**Lens discipline held throughout.** The Reviewer independently confirmed **zero lens leakage** — every salient site sits at the standard scholarly surface, with the Wheel of Heaven reading confined to `notes.official` and glossary `rationale`.

## Central glossary changes (v2.70.0 → v2.71.0) — applied by orchestrator

The Editor specified these as diffs (4.6 MB central-file write-crash constraint); I applied them via Python.

1. **NEW entry** `divine-council-first-person-plural-isa-6-8-heavenly-assembly-cross-corpus` (`direct`, appliesTo `ISA-6:8`). Governs the *lānû* plural. A distinct lexeme from the Genesis `naaseh-adam` cohortative (a 1cp suffix, not a נַעֲשֶׂה verb), so its own entry, cross-linked to the Genesis divine-council cluster. The `wohChoice`/line commit only to the literal plural; the council reading is flagged `inferred` inside the rationale.
2. **`appliesTo` activation** — `trisagion-rev-4-8-isa-6-3-sanctus-liturgical-tradition-cross-corpus` `+ISA-6:3` (activating the bidirectional wiring the entry itself anticipated); `hineni-prophetic-response-formula` `+ISA-6:8`. *(`harbah-arbeh-doubled-infinitive-intensive` already listed ISA-6:9 — no change.)*

All 20 of the chapter's glossaryRefs resolve (4 central, 16 overlay) — no dangling references.

## Overlay entries (`_translation-glossary.json` v1.0.0) — 16, all `direct`

`title-and-meta-conventions-isaiah` · `adonai-standalone-title-isaiah` · `throne-ram-venissa-isaiah` · `shulayw-hem-train-isaiah` · `heikhal-temple-palace-isaiah` · `seraphim-burning-ones-isaiah` · `yhwh-tzevaot-hosts-isaiah` · `kevodo-kavod-suffixed-isaiah` · `ammot-sippim-thresholds-isaiah` · `nidmeti-undone-isaiah` · `ha-melekh-divine-title-isaiah` · `ritzpah-live-coal-isaiah` · `kupar-atonement-isaiah` · `hashmen-hardening-commission-isaiah` · `levaer-massevet-stump-isaiah` · `zera-qodesh-holy-seed-isaiah`

All `direct`: every salient site was resolved to the standard scholarly surface in the line, with the lens routed to commentary — so nothing rises to `inferred` in the overlay.

## Reviewer report (inlined summary)

**Reviewer:** `claude-opus-4-8` acting as woh-reviewer · **overall verdict:** `awaiting-human`.

- **Verses:** all 13 re-parsed independently from the pointed+cantillated WLC; **13/13 approve, 0 revise, 0 flag.** Divine-name skeleton verified (Adonai 6:1/8/11; YHWH 6:3/5/12; *lānû* 1cp at 6:8) — the Editor's house-style mapping is textually correct.
- **Lens-leakage:** independently checked verse by verse — **none.** Seraphim transliterated (no fiery-serpent/craft reading); YHWH-of-hosts / kavod / trishagion unaltered; 6:8 plural preserved and unresolved; 6:13 MT retained with LXX-minus disclosed.
- **Glossary:** 18 approve / 1 flag-for-human / 0 veto. All 16 overlay entries confirmed `direct` and defensible; trishagion `+ISA-6:3` and hineni `+ISA-6:8` approved.
- **The divine-council entry (6:8):** the direct/inferred split is **CONFIRMED clean** — the entry commits only the literal plural to `direct`; the Council-of-Eternals reading is explicitly `inferred` in the rationale. The Reviewer did **not** downgrade or veto. The single flag is *procedural* (see below).
- **Citations:** all verified real and correctly attributed — Wildberger *Isaiah 1–12* (1991); Williamson ICC *Isaiah 6–12* (2018); Blenkinsopp *Isaiah 1–39* (AB 19, 2000); Mullen *The Divine Council* (HSM 24, 1980); Cross *Canaanite Myth and Hebrew Epic* (1973); Joines *JBL* 86 (1967); Aune *Revelation 1–5* (WBC 52A); GKC §113 / Joüon-Muraoka §123; and the NT hardening-reception (Matt 13:14–15; Acts 28:26–27). None unverifiable.

## Editor escalation report

Full report at [`chapter-6-editor-report.md`](chapter-6-editor-report.md). All **15 Translator editorial questions resolved** (all ratified). **Zero speculative entries.** Lens-discipline records included for every salient site.

## Items requiring decision

**One item — a genuine human call, by design:**

1. **Ratify the new central divine-council entry** `divine-council-first-person-plural-isa-6-8-heavenly-assembly-cross-corpus` (and its `direct`/`inferred` split). This is a **new permanent cross-corpus entry that seeds the Council-of-Eternals development into the shared production glossary** at the opening of a new book. Both the Editor and the Reviewer flagged it for your eye — not because the philology is shaky (the Reviewer confirmed the split is clean and the plural is a `direct` grammatical datum) but because it's a project-stance commit into central infrastructure. The line and the glossary `wohChoice` say only "who will go for us?"; the council → Council-of-Eternals reading is `inferred` and confined to the apparatus. **Confirm the split is drawn where you want it before this central entry is ratified.**

Everything else — all 13 verses, all 16 overlay entries, both `appliesTo` activations — is Reviewer-approved with no open questions.

## On sign-off

When you approve, the following advance (woh-translation skill, step 7):

- `chapter-6.json` → `reviewer = "zarazinsfuss"`, `reviewedAt = <sign-off ISO timestamp>`, `version = "1.0.0"`, `status = "stable"`.
- `_meta.json` → add `chapter-6.json` to `chapterFiles[]`, `chapterCount = 1`, `paragraphCount = 13`, bump `revision`, strip the stale "**Planned**" marker from the description.
- Optionally continue the isaiah-woh initial scope (roadmap `{6, 24–27, 53}`) — chapters 24–27 (the "Little Apocalypse") and 53 (the suffering servant) are the next units.

**Do not advance past `awaiting-human` without your explicit sign-off.**
