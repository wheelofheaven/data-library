# Chapter 3 Editor Report — Atra-ḫasīs, Tablet III

## Overview

Tablet III is the **Flood tablet** — the Mesopotamian flood-narrative in its
oldest connected form, the direct antecedent of Gilgamesh XI and the
comparandum to Genesis 6–9. The arc: Enki, oath-bound, warns Atra-ḫasīs
**through the reed wall** (dismantle the house, build a boat, save life); the
boat is built, loaded, and sealed; Adad's storm and the **seven-day Flood**
destroy humankind; Enki's heart breaks; **Nintu/Bēlet-ilī laments** her
drowned offspring; the gods, **cut off from offerings, hunger and thirst**;
the Flood recedes, Atra-ḫasīs **offers**, and the starved gods gather **"like
flies"** over it; Enlil rages that a human survived; Enki confesses and
proposes **measured checks in place of another flood**; and Nintu institutes
the **permanent population-limits** (non-bearing women, the *pašittu* demoness,
celibate priestesses under a birth-taboo, and settled **mortality**). **113
lines / 8 segments**, schema `composition/column/line`, refIds
`ATRA-WOH-III:{col}.{line}`. The **best-preserved** tablet, reconstructed more
fully.

The Translator submitted **9 editorial_questions[]**; this pass resolves every
one and clears the array.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0` (semver-minor)
- `translation.glossaryVersion`: `2.69.0` → **unchanged** (central file
  untouched)

`verificationStatus` preserved unchanged in `chapter-3.json` and
`source-akk-3.json`. **No `i18n.en` line was modified.** All edits to
`notes.official`, `glossaryRefs[]`, metadata, and `editorial_questions[]`.
**26 lines received commentary**; plain and formulaic lines left empty.

---

## Resolution of the 9 editorial questions

| # | refId | Question | Resolution |
|---|---|---|---|
| 1 | III:iii.8 | *abūbu* 'the Flood' | **Resolved** → central `a-ma-ru-abubu-mabbul-great-flood-vocabulary-cross-corpus` applied by id ('the Flood'); Akkadian `appliesTo` activation on the 10 Atra-ḫasīs occurrences **flagged** for the Python step. No new overlay entry (central covers it). |
| 2 | III:i.13 | *eleppu* 'boat' (anti-"ark") | **Resolved** → central `ma-gur-eleppu-tevah-flood-vessel-cross-corpus` applied; **anti-"ark" decision honored** — plain 'boat'. Commentary notes the central wohChoice ('great boat') is tuned to Sumerian *ma-gur*; Akkadian `appliesTo` flagged. |
| 3 | III:i.11 | reed-wall oath-loophole (*igāru/kikkišu*) | **Resolved** → overlay `igaru-kikkishu-reed-wall-oath-loophole-atrahasis` (`direct`); central trope entries applied by id, Akkadian `appliesTo` flagged. Gilgamesh XI 21–22 parallel in commentary. |
| 4 | III:v.42 | *kīma zumbī* "like flies" | **Resolved** → central `gods-like-flies-vs-pleasing-aroma-flood-sacrifice-cross-corpus` applied; commentary marks this the **OLDEST witness** of the simile (→ Gilgamesh XI; contrast Gen 8:21 *rêaḥ nîḥōaḥ*). Akkadian `appliesTo` flagged. Literal 'flies' retained. |
| 5 | III:vii.8 | population-limit apparatus | **Resolved** → **new overlay cluster (4 entries):** `pasittu-...` (`direct`), `la-alittu-...` (`direct`), `ugbabtu-entu-igisitu-...-ikkibu-...` (`direct`), `mutu-settled-mortality-...` (`direct`). Demon/priestess-names retained transliterated (Tablet-I *lullû*/*eṭemmu* precedent); *lā ālittu*/*ikkibu*/*mūtu* rendered plainly. |
| 6 | III:i.14 | *napišta bulliṭ* 'save life' | **Resolved** → overlay `napishtu-bullit-save-life-flood-instruction-atrahasis` (`direct`). Collective 'keep life alive' (not reflexive 'save your own life'); Gen 6:19–20 / 7:3 *lĕhaḥăyôt* parallel in commentary. |
| 7 | III:ii.10 | *Atra-ḫasīs* = 'exceedingly wise' | **Resolved** → shared overlay `atrahasis-name-exceedingly-wise-atrahasis` (`direct`, also governs II:ii-1). Retained untranslated; etymology glossed in commentary. |
| 8 | III:vii.4 | *mūtu* settled mortality | **Resolved** → overlay `mutu-settled-mortality-etiological-verdict-atrahasis` (`direct`). *mūtu* = the CONDITION/verdict (not a death-demon); central `return-to-the-earth-mortality-verdict-...` applied by id, Akkadian `appliesTo` flagged; Gen 3:19 parallel in commentary. |
| 9 | III:iii.7 | reconstruction-uncertain similes | **Resolved as verification notes.** iii.7 ('like a pot'), iii.13 ('screaming eagle'), iv.7 ('like a raft') retained as tentative, marked reconstruction-uncertain in commentary; `verificationStatus` holds. No glossary entry. |

All 9 `editorial_questions[]` cleared to `[]`.

---

## ⚠ Lens-routing decisions

Three readings that are **in the Akkadian** and rendered plainly, with no
softening:

1. **The gods regret destroying their own creation** — Enki's heart in torment
   as he sees "his children cast down before him" (iii.16–17), and the gods
   weeping with Nintu (iv.11). Rendered plainly.
2. **The gods hunger when cut off from offerings** — "the gods' lips were
   parched with hunger," the Anunna "sat in thirst and hunger" (iv.16–19), and
   they swarm "like flies" over the first sacrifice (v.41–42). This is the
   offering-dependency that the anthropogony of Tablet I set up (humankind made
   to feed the gods). Rendered plainly.
3. **Deliberate, permanent population-limiting** — the fertility-checks and
   settled mortality of vii.4–11. Rendered plainly.

Held out of every `i18n.en` line and every `notes.official`:

- **Nothing lens-y touches any line.** No `i18n.en` modified.
- **Nothing lens-y touches any commentary.** Commentary is philology + hedged
  cross-corpus comparison, cited: the **Genesis 6–9 / Noah** flood parallel
  (with the causation contrast — *noise* vs Genesis's moral corruption, carried
  at II:vii-5 and the *rigmu* entry), the **Gilgamesh XI** dependence, and the
  **flies-simile → Gen 8:21** contrast. No commentary asserts the Elohim frame.
- The **interpretive Elohim-frame identification** (makers grieving an
  engineered creation; engineered lifespan-limits) is escalated below and
  routed to the Explainer — never the line. Flagged explicitly in the
  commentary at iii.16 and in the `mutu-...` entry rationale.

---

## Speculative entries requiring sign-off

The Tablet-III lens-temptation is the same proposed-not-committed entry
escalated for Tablet II — `atrahasis-population-control-elohim-frame`
(identifying the gods as the Elohim-as-advanced-civilization and the
grief/hunger/limits as engineered demographic management). **Do NOT commit;
route to the Explainer.** Zero committed speculative entries block the advance.
**Human reviewer:** confirm by name.

---

## Glossary changes for review

### Central glossary — **no in-agent edits.** Deferred to the Python step:

**Akkadian-side `appliesTo` activation** on existing central entries for the
Tablet-III refIds (the **flood cluster**):
`a-ma-ru-abubu-mabbul-great-flood-vocabulary-cross-corpus` (iii.8, 12, 15;
v.35, 36, 47; vi.21, 23; viii.10, 16);
`ma-gur-eleppu-tevah-flood-vessel-cross-corpus` (i.13, 15; ii.21, 33; vi.5);
`gods-like-flies-vs-pleasing-aroma-flood-sacrifice-cross-corpus` (v.41–42, the
**older witness**); `iz-zi-da-kikkish-...` and `ea-warning-...` (i.11–12, 22–23);
`an-enlil-enki-ninhursaga-flood-council-quartet-...`;
`divine-decree-to-destroy-humankind-...`;
`preservation-of-the-seed-of-humankind-and-animals-flood-aitia-...`;
`return-to-the-earth-mortality-verdict-adapa-genesis-cross-corpus` (vii.4);
`seven-day-flood-vs-forty-day-flood-duration-tradition-...` (v.34);
`ziusudra-atrahasis-utnapishtim-noach-...` (survivor-name);
`kupru-koper-bitumen-pitch-...`; `im-hul-imhullu-...` storm-wind; and the
DINGIR / Anunna-Igigi / lacuna-bracket conventions. All already referenced by
id in the draft's per-line `glossaryRefs[]`.

### Per-translation overlay (`_translation-glossary.json`) → v1.1.0

**Added (Tablet III, 6 entries):** `igaru-kikkishu-reed-wall-oath-loophole-...`
(`direct`), `napishtu-bullit-save-life-flood-instruction-...` (`direct`), and
the **population-limit cluster** — `pasittu-infant-snatching-demoness-...`
(`direct`), `la-alittu-non-bearing-women-...` (`direct`),
`ugbabtu-entu-igisitu-celibate-priestesses-ikkibu-birth-taboo-...` (`direct`),
`mutu-settled-mortality-etiological-verdict-...` (`direct`). Plus the shared
`atrahasis-name-exceedingly-wise-...` (created with Tablet II, governs III:ii.10).

Distribution: **6 `direct`, 0 `inferred`, 0 committed `speculative`.**

---

## refId-scheme note

Tablet III's `ATRA-WOH-III:{col}.{line}` (dot) is the **recommended target
form** for normalizing Tablet II's dash. See the chapter-2 report; the reviewer
should rule once for both tablets. Non-blocking.

---

## Unresolved editorial questions

**None.** All 9 resolved; `editorial_questions[]` is `[]`.

---

## Items for the human reviewer

1. **Confirm the speculative routing (required):** `atrahasis-population-control-elohim-frame`
   stays in the Explainer, out of the translation/glossary (shared with Tablet II).
2. **Ratify the anti-"ark" *eleppu* rendering** ('boat', not 'ark') and the
   literal 'like flies' (indignity retained, not softened).
3. **Rule on the refId scheme** (dot form recommended as the target; shared
   with Tablet II).
4. **Approve the central Akkadian-side `appliesTo` activations** for the flood
   cluster (Python step), including the flies-simile older-witness flag and the
   mortality-verdict activation.
5. **Verification-pass:** the reconstruction-uncertain similes (iii.7, iii.13,
   iv.7) and bracketed restorations await sign-level collation against
   Lambert–Millard 1969 and eBL L.1.1; `verificationStatus` holds.

## Sign-off recommendation

**Recommend advancing to Reviewer.** The translation reads as a defensible
scholarly rendering in the Lambert–Millard / Foster register; the gods'
regret, their hunger when cut off from offerings, and the deliberate
population-limiting are delivered plainly because they are in the Akkadian, and
the Elohim-frame lens is held entirely out of the translation and apparatus.
Every overlay entry has all required fields, correct claim_type, and CAD/AHw +
named-scholarship grounding. **Zero committed `claim_type=speculative`
entries**; standard Reviewer sign-off applies, plus the speculative-routing
confirmation.
