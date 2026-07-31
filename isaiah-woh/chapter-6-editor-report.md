# Chapter 6 Editor Report — Isaiah 6 (throne-room vision and commission)

**Book opened:** `isaiah-woh`. This chapter creates the book-local overlay
`data-library/isaiah-woh/_translation-glossary.json` at **v1.0.0**
(16 entries, all `claim_type=direct`).

**Chapter advanced:** `translation.status` → `editor-review`;
`translation.version` → `1.0.0-rc1`;
`translation.overlayGlossaryVersion` → `1.0.0`; `reviewer` left `pending`.

**Text discipline:** no English line in `paragraphs[].i18n.en` was altered.
Every editorial question resolved to a ratification of the Translator's
defensible-scholarly surface; the Wheel of Heaven lens is carried entirely in
`notes.official` commentary and in glossary `rationale` fields. Zero
`claim_type=speculative` entries were produced (see "Speculative entries"
below), so nothing on the speculative-block gate prevents the advance to
`editor-review`. Three **central-glossary** changes are required (two
`appliesTo` extensions + one new entry) and are specified as exact diffs below
for the orchestrator to apply via Python.

---

## Resolved editorial questions (15/15)

Each is ratified (R) or overruled (O) against the Translator's `default_taken`.

1. **`isa6-1-adonai-rendering`** — R. Bare אֲדֹנָי → **"the Lord"** (ASV/JPS);
   kept distinct from the "YHWH" house-style and from the compound
   `adonai-yhwh` entries. Escalation-option "read as masked YHWH" **declined**
   (accuracy-before-lens: consonantal MT reads אֲדֹנָי). New overlay entry
   `adonai-standalone-title-isaiah` governs ISA-6:1, 6:8, 6:11.

2. **`isa6-1-throne-ram-venissa`** — R. רָם וְנִשָּׂא attaches to the **throne**
   ("a throne, high and lifted up"); the Isa 57:15 God-attachment is an
   independent construction. Overlay `throne-ram-venissa-isaiah` (ISA-6:1).

3. **`isa6-1-shulayw-heikhal`** — R. שׁוּלָיו → **"the hem of his robe"**;
   הֵיכָל → **"the temple"** (altar of v6 + Uzziah setting fix the sanctuary),
   palace/audience-hall register moved to commentary. Overlay entries
   `shulayw-hem-train-isaiah` and `heikhal-temple-palace-isaiah` (ISA-6:1).

4. **`isa6-2-6-seraphim`** — R. **Transliterate "seraphim"**; "burning ones"
   (√śrp) in commentary. Escalation-option **"fiery/flying serpents" declined**
   for the throne-vision (the beings have faces/hands/feet/voices and act as
   courtiers). Overlay `seraphim-burning-ones-isaiah` (ISA-6:2, 6:6).

5. **`isa6-3-trisagion-qadosh`** — R. Preserve the threefold **"Holy, holy,
   holy"** (no intensive-superlative collapse). Handled by the existing
   **CENTRAL** trishagion entry, wired to ISA-6:3 — see **CENTRAL DIFF 1**.
   No duplicate overlay entry created (one-entry-per-lexical-decision).

6. **`isa6-3-5-yhwh-tzevaot`** — R. **"YHWH of hosts"**; the heavenly-host /
   divine-assembly reading (Mullen, Cross) stated in commentary, not in the
   title. Overlay `yhwh-tzevaot-hosts-isaiah` (ISA-6:3, 6:5).

7. **`isa6-3-kavod-eretz`** — R. **"the fullness of the whole earth is his
   glory"** (literal word order, *kevodo* as predicate); *kol ha-aretz* cosmic
   "whole earth"; physical-presence *kavod* sense in commentary. New overlay
   entry (the suffixed form ≠ the Ezekiel-scoped `kavod-yhwh` construct):
   `kevodo-kavod-suffixed-isaiah` (ISA-6:3).

8. **`isa6-4-ammot-sippim`** — R. **"the foundations of the thresholds"**
   (JPS); "posts of the door" / "door-pivots" recorded as equivalents. Overlay
   `ammot-sippim-thresholds-isaiah` (ISA-6:4). Verse 4 left without commentary
   (scene-setting; salient-verses policy).

9. **`isa6-5-nidmeti`** — R. **"I am undone"** (√dmh "cut off/ruined"), the
   majority reading, grounded by "for my eyes have seen the King"
   (seeing-deity death-danger); √dmm "silenced/struck dumb" recorded as the
   live minority alternative in commentary. Overlay `nidmeti-undone-isaiah`
   (ISA-6:5).

10. **`isa6-5-ha-melekh-seeing-deity`** — R. **"the King, YHWH of hosts"**;
    the theophany-danger of physically seeing the deity (Exod 33:20; Judg
    13:22) in commentary. Overlay `ha-melekh-divine-title-isaiah` (ISA-6:5).

11. **`isa6-6-7-ritzpah-mouth-purification`** — R. **"a glowing coal"** (live
    coal / hot stone, cf. 1 Kgs 19:6), taken with tongs from the altar; the
    lip-purification developed in commentary. Overlay `ritzpah-live-coal-isaiah`
    (ISA-6:6).

12. **`isa6-7-kaphar-atonement`** — R. **"your iniquity is removed, and your
    sin is atoned for"** (√kpr; "purged/expiated" as equivalents). Overlay
    `kupar-atonement-isaiah` (ISA-6:7).

13. **`isa6-8-lanu-divine-council-plural`** (TOP PRIORITY) — R. Text preserves
    both numbers literally: **"Whom shall I send, and who will go for us?"** The
    1cp לָנוּ is a **direct** grammatical datum; the divine-council /
    Council-of-Eternals reading is **inferred** and confined to commentary. The
    `naaseh-adam` entry is Genesis-scoped and does **not** govern here (distinct
    lexeme: לָנוּ 1cp suffix vs. the נַעֲשֶׂה cohortative). A cross-corpus
    divine-council-plural entry is warranted and is proposed as a **NEW CENTRAL
    entry** (not overlay-only) cross-linked to the Genesis cluster — see
    **CENTRAL DIFF 2**.

14. **`isa6-9-10-hardening-commission`** — R. **Purposive imperatives at face
    value** ("make the heart of this people fat... lest it... be healed"); the
    ironic and resultative construals, the LXX resultative recast + NT reception
    (Matt 13:14–15; Acts 28:26–27), and the Targum paraphrase surfaced in
    commentary. v9 doubled-infinitive intensives already governed by the central
    `harbah-arbeh-doubled-infinitive-intensive` entry (already lists ISA-6:9).
    New overlay `hashmen-hardening-commission-isaiah` (ISA-6:10) for the v10
    hardening imperatives.

15. **`isa6-13-holy-seed-stump`** — R. **Retain the MT clause** "the holy seed
    is its stump"; לְבָעֵר → "for burning" (√bʿr); מַצֶּבֶת → "stump"
    (felled-tree). The **LXX-minus** of זֶרַע קֹדֶשׁ מַצַּבְתָּהּ flagged as a
    text-critical datum in commentary (MT translated, minus disclosed). Two
    overlay entries: `levaer-massevet-stump-isaiah` and
    `zera-qodesh-holy-seed-isaiah` (both ISA-6:13).

---

## Overlay entries added — `_translation-glossary.json` v1.0.0

**16 entries, claim_type breakdown: `direct` × 16, `inferred` × 0,
`speculative` × 0.**

| id | appliesTo | claim_type |
|---|---|---|
| `title-and-meta-conventions-isaiah` | ISA-6:1 | direct |
| `adonai-standalone-title-isaiah` | ISA-6:1, 6:8, 6:11 | direct |
| `throne-ram-venissa-isaiah` | ISA-6:1 | direct |
| `shulayw-hem-train-isaiah` | ISA-6:1 | direct |
| `heikhal-temple-palace-isaiah` | ISA-6:1 | direct |
| `seraphim-burning-ones-isaiah` | ISA-6:2, 6:6 | direct |
| `yhwh-tzevaot-hosts-isaiah` | ISA-6:3, 6:5 | direct |
| `kevodo-kavod-suffixed-isaiah` | ISA-6:3 | direct |
| `ammot-sippim-thresholds-isaiah` | ISA-6:4 | direct |
| `nidmeti-undone-isaiah` | ISA-6:5 | direct |
| `ha-melekh-divine-title-isaiah` | ISA-6:5 | direct |
| `ritzpah-live-coal-isaiah` | ISA-6:6 | direct |
| `kupar-atonement-isaiah` | ISA-6:7 | direct |
| `hashmen-hardening-commission-isaiah` | ISA-6:10 | direct |
| `levaer-massevet-stump-isaiah` | ISA-6:13 | direct |
| `zera-qodesh-holy-seed-isaiah` | ISA-6:13 | direct |

Rationale for the all-`direct` profile: every WoH-salient site
(seraphim, YHWH-of-hosts, *kavod*, the 6:8 plural, the holy-seed remnant)
was resolved by keeping the **standard scholarly surface** in the line and
routing the lens into commentary. No overlay rendering diverges from the
consensus versions, so none rises to `inferred`; the one genuinely
lens-forward reading (the divine-council interpretation of 6:8) is carried as
an `inferred` reading **inside the rationale/commentary**, while its glossary
`wohChoice` (the literal plural) remains `direct`.

---

## CENTRAL-glossary changes for review — apply by orchestrator

> The Editor did **not** touch `data-content/i18n/translation-glossary.json`
> (4.6MB). Apply the three diffs below via Python, then bump the central file's
> `version` (semver-minor: two appliesTo extensions + one new entry;
> `harbah-arbeh-doubled-infinitive-intensive` already lists ISA-6:9 and needs
> no change).

### CENTRAL DIFF 1 — wire the Trisagion entry to Isaiah (appliesTo extension)

**Entry id:** `trisagion-rev-4-8-isa-6-3-sanctus-liturgical-tradition-cross-corpus`
**Change:** add `"ISA-6:3"` to `appliesTo`. The entry already documents Isa 6:3
at length and its own text states a future ISA-6:3 entry "should produce
bidirectional cross-references with this entry" — this activates that wiring.

```json
// appliesTo:  was
["REV-WOH-4:8"]
// appliesTo:  now
["REV-WOH-4:8", "ISA-6:3"]
```

Optional (recommended) bidirectional-note touch-up: no field change is
strictly required, but the entry's "Bidirectional cross-corpus wiring"
paragraph may have its clause "Future entry on Isa 6:3 (when an
Isaiah-translation is added)…" updated to record that ISA-6:3 is now wired.
This is cosmetic; the appliesTo addition is the load-bearing change.

### CENTRAL DIFF 2 — new cross-corpus divine-council-plural entry for Isa 6:8

**Rationale for CENTRAL (not overlay):** the first-person-plural divine speech
is a cross-corpus motif spanning Genesis (1:26, 3:22, 11:7) and Isaiah (6:8);
per the escalation instruction it is proposed as a central entry cross-linked
to the Genesis cluster rather than an overlay-only claim. `appliesTo` is
**ISA-6:8 only** — the distinct lexeme (לָנוּ 1cp suffix) is not the נַעֲשֶׂה
cohortative already governed by `naaseh-adam`, so this does **not** double-govern
GEN-1:26; the Genesis sites are cross-referenced in the rationale. **Note the
central `terms` schema has no `lemma` field** — the object below omits it to
match the central schema (the overlay schema keeps `lemma`; the central one
does not).

**Add this object to `terms[]`:**

```json
{
  "id": "divine-council-first-person-plural-isa-6-8-heavenly-assembly-cross-corpus",
  "source": "וּמִי יֵלֶךְ־לָנוּ (Isa 6:8)",
  "translit": "ûmî yēleḵ-lānû",
  "strongs": "H1980 (hālaḵ 'to go'); H4310 (mî 'who'); lānû = the inseparable preposition לְ (no discrete Strong's number) + 1cp suffix",
  "partOfSpeech": "interrogative + verb (Qal imperfect 3ms) + preposition with 1cp suffix; the divine first-person-plural in throne-room speech",
  "literal": "and who will go for us?",
  "standardEnglish": "and who will go for us? (ASV/JPS/NRSV)",
  "wohChoice": "'and who will go for us?' — the singular 'Whom shall I send' and the first-person-plural 'for us' (לָנוּ) preserved literally side by side, without committing the line to a reading. The divine-council interpretation is carried in commentary and rationale, not the text.",
  "claim_type": "direct",
  "rationale": "At Isa 6:8 the enthroned speaker asks *ʾeṯ-mî ʾešlaḥ ûmî yēleḵ-lānû* — 'Whom shall I send, and who will go for us?' — juxtaposing a singular 1cs verb ('I send') with a 1cp pronominal suffix on the preposition ('for us', לָנוּ). The plural is a direct, unambiguous datum of the grammar and is preserved literally, exactly as the project preserves the divine cohortatives at Gen 1:26 (`naaseh-adam`), Gen 3:22, and Gen 11:7 (`havah-neredah`, `naase-lanu-shem`). This is a DISTINCT lexeme from those cohortatives (a 1cp suffix, not a נַעֲשֶׂה/נֵרְדָה verb form), which is why it takes its own entry rather than an extension of `naaseh-adam`; the entries are cross-referenced bidirectionally. On the READING of the plural, the modern scholarly consensus (E. T. Mullen, *The Divine Council in Canaanite and Early Hebrew Literature*, HSM 24, 1980; F. M. Cross, *Canaanite Myth and Hebrew Epic*, 1973; and the standard Isaiah commentaries — Wildberger, *Isaiah 1–12*, 1991; Blenkinsopp, *Isaiah 1–39*, AB 19, 2000; Williamson, ICC *Isaiah 6–12*, 2018) is that the deity speaks as the enthroned head of the heavenly assembly convened in the vision itself — the seraphim and the 'hosts' (*ṣᵉḇāʾôṯ*) of v3 — deliberating and dispatching a messenger from within the council; the Wheel of Heaven lens develops this as the Council of Eternals. That council reading is INFERRED, not direct, and is the reason the entry is flagged for the human reviewer in the editor report; but the glossary `wohChoice` and the translated line commit only to the literal plural, which is why the entry's `claim_type` is `direct`. Lens-discipline: the alternative construals (plural of majesty / plural of self-deliberation; the prophet enlisted into the council) are acknowledged; none is imposed on the text. Cluster with `naaseh-adam`, `havah-neredah`, `naase-lanu-shem`, `divine-council-phr-mad-cross-corpus-ugaritic-akkadian-hebrew-bible`.",
  "appliesTo": ["ISA-6:8"]
}
```

### CENTRAL DIFF 3 — wire the hineni formula to Isaiah (appliesTo extension)

**Entry id:** `hineni-prophetic-response-formula`
**Change:** add `"ISA-6:8"` to `appliesTo`. הִנְנִי שְׁלָחֵנִי "Here am I; send
me" at Isa 6:8 is the prophetic-response formula this entry governs; the
Translator already placed the ref on ISA-6:8, and this activates it (parallel
to `harbah-arbeh-doubled-infinitive-intensive`, which **already** lists ISA-6:9
and needs no change).

```json
// appliesTo:  was
["GEN-WOH-22:1", "GEN-WOH-22:7", "GEN-WOH-22:11", "GEN-WOH-46:2"]
// appliesTo:  now
["GEN-WOH-22:1", "GEN-WOH-22:7", "GEN-WOH-22:11", "GEN-WOH-46:2", "ISA-6:8"]
```

> After DIFF 2 is applied, the glossaryRef
> `divine-council-first-person-plural-isa-6-8-heavenly-assembly-cross-corpus`
> already placed on ISA-6:8 in `chapter-6.json` becomes live. Likewise, after
> DIFF 1, the glossaryRef
> `trisagion-rev-4-8-isa-6-3-sanctus-liturgical-tradition-cross-corpus` on
> ISA-6:3 becomes live. Both refs are already written into the chapter file in
> anticipation, following the Sumerian-King-List precedent (central ids
> referenced in `glossaryRefs`, activation deferred to the central Python step).

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry was produced. Per hard rule 5,
nothing blocks the advance to `editor-review`.

**One item nonetheless warrants an explicit human eye** (not a speculative
entry, but the chapter's sharpest lens-decision): the `inferred` divine-council
reading in **CENTRAL DIFF 2** and in the ISA-6:8 commentary. The *entry* and the
*line* are `direct` (literal plural only); the *interpretation* (council →
Council of Eternals) is `inferred` and lives in the apparatus. Confirm the
`direct`/`inferred` split is drawn where you want it before the central entry is
committed.

---

## Lens-discipline records (salient sites)

- **Seraphim (6:2, 6:6):** "fiery serpents" **declined** in the throne-vision;
  transliteration kept, iconographic/serpent prehistory and Ezek-1/Rev-4
  resonance in commentary only.
- **YHWH of hosts (6:3, 6:5):** title unchanged; heavenly-host/assembly reading
  (Mullen/Cross) in commentary, not surfaced by re-rendering *ṣᵉḇāʾôṯ*.
- **Trisagion (6:3):** threefold form preserved; reception-tradition handled by
  the central entry; no lens asserted in the line.
- **kevodo (6:3):** "his glory" kept; physical-presence *kavod* register in
  commentary; suffixed form deliberately NOT folded into the Ezekiel construct
  entry.
- **"for us" (6:8):** literal plural preserved; council/Council-of-Eternals is
  an `inferred` reading in the apparatus, `direct` in the line.
- **Hardening commission (6:9–10):** imperatives kept at face value; LXX/NT
  mitigations disclosed in commentary, not imposed.
- **Holy seed / stump (6:13):** MT clause retained; LXX-minus disclosed as a
  text-critical datum; remnant theology in commentary.

## Notes for the Reviewer

- No English translation line was changed; the Translator's draft surface is
  intact (hard rule 8).
- Verses **6:4, 6:11, 6:12** are intentionally left without `notes.official`
  (scene-setting / desolation-oracle; salient-verses policy). 6:4's lexical
  decision is recorded in the overlay.
- `editorial_questions[]` cleared (all 15 resolved above).
- `_meta.json` untouched.
