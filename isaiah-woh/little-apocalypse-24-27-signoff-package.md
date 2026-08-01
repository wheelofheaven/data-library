# Isaiah 24–27 ("The Little Apocalypse") — block sign-off package

**Scope:** the four-chapter Little Apocalypse, run as a sequential block. Closes the roadmap's initial `isaiah-woh` scope `{6, 24–27, 53}`.
**Chapters:** `chapter-24.json` (23v), `chapter-25.json` (12v), `chapter-26.json` (21v), `chapter-27.json` (13v) — **69 verses**.
**Version:** all four at `1.0.0-rc1`.
**Glossary:** central **v2.72.0 → v2.73.0**; overlay **v1.1.0 → v1.5.0** (+43 Isaiah entries).
**Source:** WLC "Tanach with Ta'amei Hamikra" (Public Domain, tanach.us), via Sefaria; cantillation + parasha markers preserved on all four.

## Block summary

| Ch | Verses | Reviewer verdict | Lens flags | Overlay added | Commentary |
|---|---|---|---|---|---|
| **24** | 23 | `reviewer-approved` — 23/23 approve | 0 | +11 (→v1.2.0) | 11 |
| **25** | 12 | `reviewer-approved` — 12/12 approve | 0 | +10 (→v1.3.0) | 9 |
| **26** | 21 | `reviewer-approved` — 21/21 approve | 0 | +11 (→v1.4.0) | 11 |
| **27** | 13 | `awaiting-human` — 12/13 approve, **1 flag** | 0 | +11 (→v1.5.0) | 6 |

**Every English line across all 69 verses is lens-clean** — the Reviewers independently found **zero lens leakage** in the translated text. The Wheel of Heaven reading is confined to `notes.official` and glossary `rationale` throughout. All citations verified real (Wildberger *Isaiah 13–27* — the correct volume for these chapters — Blenkinsopp AB 19, Kaiser OTL, Day 1985, Levenson, Mullen/Cross, Tsumura 2005; none fabricated).

## The four marquee lens sites — how each was held

- **24:21 — "the host of the height on high" (`ṣᵉḇāʾ ha-mārôm`) judged:** rendered plainly, **no rebellious-host / fallen-watchers / astral-deity identification** in the line (the 1 Enoch fallen-stars entry was deliberately *not* applied); the divine-council readings are `inferred`, apparatus-only. Kept distinct from `YHWH ṣᵉḇāʾôṯ` (24:23).
- **25:8 — "he has swallowed up death for ever" (`billaʿ ha-māweṯ`):** line reads **abstract lowercase "death"**, not the deified Ugaritic Môt. The Môtu-reversal (Baal Cycle, Day 1985) and NT reception (1 Cor 15:54; Rev 21:4) are commentary-only; the central `mot-mavet-death-personified` entry now lists 25:8 but stays `direct` and records the link only.
- **26:19 — "your dead shall live" (`yiḥyû mēṯeḵā`):** the clearest bodily-resurrection text in Isaiah, rendered at the **MT surface** (`direct`); the Dan 12:2 / Ezek 37 resurrection program is commentary-only (the central resurrection entry now lists 26:19). The **26:14 `rᵉp̄āʾîm`** is correctly the *shades/dead* sense ("shades"), **not** the giant-Rephaim/Nephilim homonym (those entries carry zero ISA-26 refs).
- **27:1 — "Leviathan the fleeing serpent… the twisting serpent… the dragon in the sea":** the flagship **chaoskampf**. The line is plain MT. The **Ugaritic Litan epithet-parallel** (`nāḥāš bāriaḥ`/`nāḥāš ʿăqallāṯôn` = KTU 1.5 I `bṯn brḥ`/`bṯn ʿqltn`) ships as the well-attested scholarly cognate it is (Day 1985), with Tsumura 2005 as the named counter-voice. The central chaoskampf cluster (`leviathan`/`taninim`/`lotanu-leviathan`/`chaoskampf`) now lists 27:1 with the direct/inferred split intact — **no synthesis smuggled into any `direct` `wohChoice`**.

## Central glossary changes (v2.72.0 → v2.73.0) — applied by orchestrator

`appliesTo` extensions only (no new central entries):
- `brit-olam` +24:5 · `harbah-arbeh-doubled-infinitive-intensive` +24:3/19/20
- `mot-mavet-death-personified-…` +25:8
- `resurrection-dan-12-2-3-foundational-…` +26:19 · `avon-iniquity-…` +26:21, +27:9
- chaoskampf cluster: `leviathan` +27:1, `taninim` +27:1, `lotanu-leviathan-…` +27:1, `chaoskampf-sea-conflict-…` +27:1

Deliberate non-extensions (recorded): 1 Enoch fallen-stars (24:21), `arubot-ha-shamayim`/"floodgates" (24:18), giant-Rephaim + Nephilim (26:14/19), `yamm`/`athirat-asherah` (27:1/9), `elohim-as-translation` (the doxological "our God" verses). All four chapters' glossaryRefs resolve — no dangling.

## Items requiring decision

**One item — a genuine framework-level call (the only reason ch. 27 is `awaiting-human`):**

1. **Ratify the fenced Theomachy-convergence synthesis paragraph** in the **27:1 commentary**. The Reviewer approved it *as fenced commentary* — it is blockquote-labelled "interpretive layer, beyond the text," encoded in **no** glossary `wohChoice`, honestly disclaimed as going beyond both the verse and the philology, and kept out of the translated line. But it is a **`framework`-level synthesis** (Isaiah's serpent / Ugaritic Lôtanu / Tiamat / Indo-European dragon-cycles as convergent memories of conflict among the Elohim) being written into the permanent record, so the Reviewer — correctly — will not sign it off unilaterally. **Confirm this paragraph.** Options: (a) ship as-is (fenced/hedged commentary); (b) soften/trim it further; (c) cut the synthesis and keep only the scholarly Ugaritic-cognate datum. The Reviewer's recommendation is (a).

Chapters 24, 25, 26 have **no open items** — pure `reviewer-approved`, sign-off is a formality.

## On sign-off

On your approval I will (woh-translation skill, step 7), for all four chapters:
- Promote each `chapter-{N}.json` → `reviewer="zarazinsfuss"`, `reviewedAt=<ts>`, `version="1.0.0"`, `status="stable"`.
- Update `_meta.json`: add 24/25/26/27 to `chapterFiles[]` → **Isaiah becomes 6 chapters** (6, 24, 25, 26, 27, 53), `paragraphCount = 94`, bump `revision`.
- Commit + push both repos (`data-library` block + `data-content` glossary v2.73.0), rebasing data-content if it diverged.

If you want to adjust the 27:1 synthesis paragraph first (option b/c above), tell me and I'll have the Editor revise ch. 27 before promotion. **Do not advance past the review gate without your explicit sign-off.**
