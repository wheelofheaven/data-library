# The Sumerian King List — sign-off package

**Status:** `awaiting-human` (clean review; one minor reviewer-caught line fix already applied — sign-off is a formality)
**Text:** The Sumerian King List (SKL-WOH), ETCSL c.2.1.1 composite. Single composition, **435 line-entries** (numbering to 431 + manuscript-insertion lines 73A/89A/106A/249A/283A/… and unnumbered variant lines A–D). The project's longest single-composition Sumerian ship.
**Chapter file:** `data-library/sumerian-king-list-woh/chapter-1.json`
**Version:** `1.0.0-rc1`
**Glossary version:** central **v2.70.0** + overlay **v1.0.0**
**Source language:** Sumerian (`sux`) — a proven pipeline language (Enki and Ninmah, Song of the Hoe, Flood Story); no new-language risk.

## Summary table

| Metric | Value |
|---|---|
| Lines translated | **435 / 435** (refId + n + translit byte-verbatim vs immutable source; order preserved) |
| Lines with `notes.official` commentary | 14 (salient-lines-only policy; mechanical regnal-total lines left empty by design) |
| Reviewer verdicts | **434 approve / 1 revise (applied) / 0 flag-for-human** |
| Reviewer lens-leakage flags | **0** |
| Reviewer glossary verdicts | **14 approve / 0 revise / 0 flag** |
| New overlay entries | **12** (v1.0.0) — 11 `direct`, 1 `inferred`, **0 `speculative`** |
| New central entries | **1** — `sumerian-toponym-onomasticon-preserve-s-and-g-anglicize-h-convention-cross-corpus` (`direct`) |
| Central `appliesTo` activations | **10** existing cross-corpus entries now list SKL lines (incl. `human-ascent-…` +SKL-64/65) |
| Central glossary bump | **v2.69.0 → v2.70.0** (semver-minor: additions + activation) |
| Speculative entries | **0** |
| Items requiring human-only judgement | **0 blocking** (see "Items requiring decision") |

## Why this text matters (canon leverage)

The Sumerian King List is a **WoH-direct** anchor and a **moat text** (no good CC0 English exists):

- **The antediluvian king-list is the structural pair to Genesis 5 and to Berossus** — eight kings across five cities (Eridug, Bad-tibira, Larag, Zimbir, Šuruppag) with impossibly long reigns (Alulim of Eridug: 28,800 years = 8 sar), then *"the flood swept over"* (`a-ma-ru ba-ur₃`) and *"kingship descended from heaven"* a second time. The Genesis 5 / Berossus longevity comparison is carried in commentary, not smuggled into the figures.
- **Two cross-corpus canon formulae:** the opening *nam-lugal an-ta ed₃-de₃-a* "kingship descended from heaven" (SKL-1, 41), and the flood formula (SKL-39/40).
- **Etana "who ascended to heaven"** (SKL-64) plugs into the existing Adapa/Etana/Enoch/Elijah ascent cluster (`human-ascent-to-heaven-…`, now extended to SKL).

**Lens discipline held throughout.** Every WoH-salient site was kept at the defensible-scholarly surface, with the lens confined to `notes.official`: `an-ta` reads "from heaven" (not "from the sky-people"); Etana "ascended to heaven" (no bodily-flight reading in the text); Gilgameš's father stays "a phantom" (no non-human paternity in the text). The Reviewer independently confirmed **zero lens leakage**.

## Central glossary changes (v2.69.0 → v2.70.0) — applied by orchestrator

The Editor correctly did **not** touch the 4.6 MB central file (write-crash constraint); all central edits were specified as diffs in the editor report and applied via direct Python.

1. **NEW entry** `sumerian-toponym-onomasticon-preserve-s-and-g-anglicize-h-convention-cross-corpus` (`direct`). Resolves a genuine self-contradiction the Translator caught: the older `sumerian-proper-name-transliteration-convention` entry documents š→sh anglicization (Enki-and-Ninmah era), but the Flood Story output and the central five-cities entry **preserve** š (Šuruppag, Bad-tibira). The new entry fixes the Sumerian-arc standard centrally: **preserve š and ĝ, anglicize only ḫ→h** (Kiš, Unug, Urim, Akšak, Agade, Hamazi). `appliesTo` spans 15 SKL toponym first-occurrences + 5 Flood-Story lines. *(The alternative — a semver-major clause on the old entry — was declined to leave the ENM-era description intact.)*
2. **`appliesTo` activation** on 10 existing cross-corpus entries (same pattern as the Atra-ḫasīs ship): `nam-lugal-an-ta-…` (+2), `a-ma-ru-…` (+2), `dumuzi-…` (+2), `utu-šamaš-…` (+4), `human-ascent-to-heaven-…` (+SKL-64/65), `five-antediluvian-cities-…` (+14), `dingir-prefix-prose-drop` (+45), `lacuna-bracket-convention` (+127), `manuscript-variant-inline-rendering` (+130), `sumerian-proper-name-transliteration-convention` (+233).

## Overlay entries (`_translation-glossary.json` v1.0.0) — 12 total, 11 `direct` / 1 `inferred`

| id | claim_type | governs |
|---|---|---|
| `title-and-meta-conventions-skl` | direct | chapter title/meta |
| `sexagesimal-reign-figure-rendering-convention-skl` | direct | reign figures (sar/ner/šu-ši) |
| `skl-postdiluvian-toponym-onomasticon-roster` | direct | 15 toponym first-occurrences |
| `en-lugal-royal-title-distinction-skl` | direct | *en*="lord" vs *lugal*="king" |
| `occupation-epithets-low-born-rulers-skl` | direct | 14 epithet lines |
| **`gilgamesh-phantom-father-lil-crux-skl`** | **inferred** | SKL-113 (*lil₂-la₂* crux) |
| `bal-dynastic-reign-term-skl` | direct | subtotal-insertion lines |
| `basub-dynasty-abandonment-verb-crux-skl` | direct | dynasty-fall verb |
| `tukul-ba-sag-defeat-formula-skl` | direct | 19 defeat-formula lines |
| `kingless-interregnum-formulae-skl` | direct | SKL-284, 309 |
| `ki-en-gi-sumer-homeland-name-skl` | direct | SKL-353A ("Sumer") |
| `deified-king-dingir-determinative-scope-note-skl` | direct | deification scope-note |

## Reviewer report (inlined summary)

**Reviewer:** `claude-opus-4-8` acting as woh-reviewer · **reviewedAt:** 2026-07-31T07:10:40Z · **overall verdict:** `awaiting-human`.

- **Translit integrity:** all 435 `translit` fields byte-identical to the immutable ETCSL source; English tracks ETCSL sense-of-line throughout.
- **Verdicts:** 434 lines approve (16 salient lines cited individually + 1 aggregate over all remaining roster/regnal lines), **1 revise (SKL-97 — applied, see below)**, 0 flag-for-human.
- **Lens-leakage:** independently checked every salient site (SKL-1/41, 64/65, 100, 113, occupation epithets) — **none found**. No Raëlian-canon terminology in any prose; every lens dimension confined to `notes.official`.
- **The `inferred` entry** `gilgamesh-phantom-father-lil-crux-skl` (SKL-113): **approved, no downgrade.** *lil₂*/*lilû* "phantom-spirit" is ETCSL's own reading and a genuine crux vs *lillu* "fool/deficient one" (CAD L 189–190, verified); the WoH-adjacent non-human-paternity upgrade was explicitly and correctly declined. `inferred` is the right label.
- **Glossary review:** 14 entries (12 overlay + 2 central) — all approve. Sexagesimal arithmetic re-verified (28800 = 8×3600; 6 šu-ši = 360; 7 šu-ši = 420); the two former draft outliers SKL-336/338 correctly normalized.
- **Citations:** all commentary citations verified as real, correctly-attributed works — Jacobsen 1939 (*AS 11*); Glassner 2004; Michalowski 1983 (*JAOS* 103); Marchesi 2010; Steinkeller 2003; Hallo 1970 (*JCS* 23); R. R. Wilson 1977; Burstein 1978 (Berossus); Kinnier Wilson 1985 / Foster on Etana; George 2003; Sarna / Cassuto on Genesis 5; CAD L for *lilû/lillu*. **None unverifiable.** One non-blocking nuance: the `bal` entry's "Sallaberger on the bala-institution" is slightly loose (his bala work centers the Ur III redistributive system rather than the SKL's dynastic-turn sense), but the core lexical claim rests on ePSD2/Jacobsen and is sound.

## The one applied revision (SKL-97)

The Reviewer's single `revise` — a segmentation infelicity, not a meaning or lens error:

- **Before:** `dumu ^dutu en-am₃` → "the son of Utu, was lord **and king**;"
- **After:** "the son of Utu, was lord;"

`en-am₃` alone = "was lord (*en*)"; "king" (*lugal-am₃*) belongs to the next line, SKL-98 ("he was king; he ruled for 324 years"). The original doubled "king." The fix is exactly the reading the Editor's own `en-lugal-royal-title-distinction-skl` overlay entry already states, and matches ETCSL's segmentation. Because the woh-reviewer has no edit tool, the fix was applied by the orchestrator; SKL-98 is unchanged and all 435 lines remain intact. It awaits the human reviewer's ratification but is not an open question.

## Editor escalation report

Full report at [`chapter-1-editor-report.md`](chapter-1-editor-report.md). All **15 Translator editorial questions were resolved** (14 defaults ratified; two refinements: SKL-113 `claim_type` set to `inferred`, and SKL-181's sexagesimal convention enforced uniformly by normalizing SKL-336/338). **Zero unresolved questions; zero speculative entries.**

## Items requiring decision

**None blocking.** The pipeline is complete and internally consistent:

1. **SKL-97 fix** — already applied per the Reviewer's exact specification and the Editor's own glossary entry. Needs only your ratification, not a decision.
2. **The one `inferred` entry** (`gilgamesh-phantom-father-lil-crux-skl`, SKL-113) — Reviewer-approved; noted here for transparency since `inferred` entries are the ones you may wish to eyeball.

## On sign-off

When you approve, the following advance (per the woh-translation skill, step 7):

- `chapter-1.json` → `translation.reviewer = "zarazinsfuss"`, `translation.reviewedAt = <sign-off ISO timestamp>`, `translation.version = "1.0.0"`, `translation.status = "stable"`.
- `_meta.json` → add the `chapter-1.json` entry to `chapterFiles[]`, set `chapterCount = 1`, `paragraphCount = 435`, bump `revision`.
- Optionally trigger multi-language fanout (step 8) once `stable`.

**Do not advance past `awaiting-human` without your explicit sign-off.**
