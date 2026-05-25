# Chapter 33 Editor Report

**Chapter:** Genesis 33 — The reunion with Esav, the gift accepted, and the altar at Shechem
**Editor stage completed:** 2026-05-25
**Translator draft status:** `draft` (v0.1.0-draft) → **Editor output status:** `editor-review` (v1.0.0-rc1)
**Central glossary:** v2.30.0 → **v2.31.0** (semver-minor; 3 additions + 2 appliesTo expansions + 1 refId form correction)
**Per-translation overlay:** v1.0.0 → **v1.1.0** (semver-minor; 3 additions)

---

## Speculative entries requiring sign-off

**None.** Per the Translator's anticipation and the Editor's review, the chapter's eight mandatory editorial questions resolve cleanly into `direct` or `inferred` claim-types. The chapter is a structural-resolution chapter, densely-philological, but not lens-leveraged. All eight new and modified glossary entries land within mainstream modern critical scholarship; project-distinctive synthesis is reserved for the wiki in every case.

---

## Unresolved editorial questions

**None.** All eight Translator editorial questions were resolved during this pass:

| Verse | Question | Resolution |
|---|---|---|
| 33:4 | *va-yishaqehu* puncta extraordinaria | Extended central `puncta-extraordinaria-v9-elav` appliesTo to include `GEN-WOH-33:4`; commentary cites b. Sotah 13a, Bereshit Rabbah 78:9 kiss-or-bite tradition. |
| 33:10 | *p'nei Elohim* Esav-reunion echo of Penuel | Extended central `peniel-panim-el-panim-divine-face-encounter` appliesTo to include `GEN-WOH-33:10`; commentary documents the structural-keystone reading and the Speiser polite-hyperbole alternative. |
| 33:11 | *birkhati* — Jacob's gift named "blessing" | Created overlay entry `birkhati-jacob-gift-as-blessing-restitution`; commentary documents the Gen 27:35-36 → Gen 33:11 lexical-echo and the *laqach* verbal-parallel. |
| 33:14 | Promised Seir / actual Sukkot — implicit deception | Created overlay entry `ya-aqov-promised-seir-actual-sukkot-implicit-deception`; commentary documents the v 14 / v 17 discrepancy and the *aqav*-character continuity reading. |
| 33:17 | Sukkot etymology + cross-corpus reach | Created central entry `sukkot-toponym-and-festival-etymology`; commentary documents the patriarchal aetiology, the cross-corpus distribution (Exod 12; Num 33; Josh 13; Judg 8; 1 Kgs 7; Ps 60, 108), and the Tell Deir 'Allah site-identification. |
| 33:18 | *shalem* — adverbial / toponym / wordplay | Created overlay entry `shalem-shechem-arrival-three-readings`; commentary documents all three readings (Targum/Rashi/ASV adverbial; LXX/Vulgate toponym; Fokkelman/Alter wordplay). |
| 33:19 | Hivites-not-Hittites + parallel-acquisition pattern + kesitah | Created central entry `patriarchal-land-acquisition-pattern-makhpelah-shechem`; commentary documents Gen 23 / Gen 33:19 / Josh 24:32 parallel; the Hivite-Hittite distinction (Gen 34:2) is explicitly flagged; existing `kesitah` entry's appliesTo updated to use the WoH refId form `GEN-WOH-33:19`. |
| 33:20 | *El Elohei Yisra'el* — fifth patriarchal El-compound | Created central entry `el-elohei-yisrael-altar-shechem`; commentary documents the five-fold pattern (El Elyon, El Ro'i, El Shaddai, YHWH El Olam, El Elohei Yisra'el), the Alt 1929 / Cross 1973 / Smith 2001 patriarchal El-religion reconstruction, and the personal-to-collective-name transition of *Yisra'el* (33:20 personal → Exod 5:1 collective). |

---

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bumped:** v2.30.0 → v2.31.0 (semver-minor: additions + expansions, no breaking modifications).

**Added (3 new entries):**

1. **`sukkot-toponym-and-festival-etymology`** (claim_type: `direct`) — patriarchal toponym, in-text aetiology, cross-corpus distribution across the Exodus-itinerary / Gad-allocation / Judges / Kings / Psalms, Iron-Age site-identification at Tell Deir 'Allah, and the Sukkot pilgrimage-festival (Lev 23; Deut 16; Num 29; Neh 8; Zech 14). Justification for central placement: the cross-corpus reach across the Pentateuch, the Former Prophets, and the festal-legislation makes the toponym/lexeme decisively cross-book; an overlay placement would fail the architectural-split test. **applies to:** `GEN-WOH-33:17`.

2. **`patriarchal-land-acquisition-pattern-makhpelah-shechem`** (claim_type: `direct`) — the foundational HB legal-title-establishment motif across Gen 23 / Gen 33:19 / Josh 24:32, with the David / Aravnah-threshing-floor extension (2 Sam 24:24); the Hivite-Hittite ethnographic distinction (Gen 34:2 *ha-Chivvi*); ANE-comparative legal-formulae review (Lehmann 1953 / Tucker 1966 / Westbrook 1971, 1991). Justification for central placement: pattern-entry covering three distinct HB books (Genesis, Joshua, 2 Samuel); cross-corpus reach. **applies to:** `GEN-WOH-33:19`.

3. **`el-elohei-yisrael-altar-shechem`** (claim_type: `direct`) — the fifth and final patriarchal El-compound; cross-link to the four prior El-compound entries (`el-elyon`, `el-roi-and-halom-elohim-variant`, `el-shaddai`, `yhwh-el-olam`); the Alt 1929 / Cross 1973 / Smith 2001 patriarchal-El-religion reconstruction; the personal-to-collective-name transition of *Yisra'el*. Justification for central placement: the El-compound pattern is a project-wide convention; the entry sits naturally alongside the four prior El-compounds in the central glossary. **applies to:** `GEN-WOH-33:20`. **Note:** the pre-existing central entry `elohei-yisrael` (covering the collective-name register and Ezekiel-10) is **complementary, not redundant** — the new entry covers the Gen 33:20 personal-name register and the patriarchal El-compound pattern; the pre-existing entry covers the collective-name register and the wider HB cross-corpus distribution. The two entries cross-reference each other in their rationales.

**Modified (2 appliesTo expansions; 1 refId form correction):**

- **`puncta-extraordinaria-v9-elav`** — appliesTo expanded from `[GEN-18:9]` to `[GEN-18:9, GEN-WOH-33:4]`; rationale extended with a substantial Gen 33:4-specific section documenting the kiss-or-bite rabbinic-tradition (b. Sotah 13a; Bereshit Rabbah 78:9; Pirkei d-Rabbi Eliezer 37; Targum Pseudo-Jonathan; Rashi) and the *n-sh-q* / *n-sh-kh* consonantal-axis ambiguity. Editorial rationale: the existing entry's rationale already enumerated Gen 33:4 as one of the canonical fifteen *nequdot*; the appliesTo expansion brings the entry's scope into alignment with its content, with a Gen 33:4-specific philological section added. No breaking change — the Gen 18:9 treatment is preserved intact.

- **`peniel-panim-el-panim-divine-face-encounter`** — appliesTo expanded from `[GEN-WOH-32:31, GEN-WOH-32:32]` to `[GEN-WOH-32:31, GEN-WOH-32:32, GEN-WOH-33:10]`; rationale extended with a substantial Gen 33:10-specific section documenting the Esav-reunion-as-human-counterpart-of-Penuel structural-keystone reading (Sarna, Westermann, Fokkelman, Alter) and the Speiser polite-courtly-hyperbole vs. structural-echo philological alternative.

- **`kesitah`** — appliesTo refId form corrected: `GEN-33:19` → `GEN-WOH-33:19` (the WoH refId convention; the existing form was a legacy non-WoH form). No rationale changes.

### Per-translation overlay (`data-library/genesis-woh/_translation-glossary.json`)

**Version bumped:** v1.0.0 → v1.1.0 (semver-minor: additions).

**Added (3 new entries):**

1. **`birkhati-jacob-gift-as-blessing-restitution`** (claim_type: `direct`) — Ya'aqov's *birkhati* at Gen 33:11 as deliberate lexical-recall of Gen 27:35-36's *birkhatekha* / *birkhati*; the symbolic-restitution-of-the-stolen-blessing reading (Sarna, Westermann, Alter, Fokkelman). **applies to:** `GEN-WOH-33:11`. Justification for overlay placement: chapter-singular Gen 27 → Gen 33 thematic-recall; no cross-corpus reach beyond the Genesis-cycle Ya'aqov-narrative; the wider *berakhah* lexeme already has central treatment in other entries.

2. **`ya-aqov-promised-seir-actual-sukkot-implicit-deception`** (claim_type: `inferred`) — the v 14 / v 17 destinational-discrepancy as Ya'aqov's continuing *aqav*-character deception of Esav; the chapter's evidence that the Penuel-renaming is structural-anticipation rather than completed-transformation. **applies to:** `GEN-WOH-33:14`. Justification for overlay placement: chapter-singular interpretive crux (the cross-narrative *aqav*-character pattern is documentary-context, not the entry's claim); cross-corpus reach is internal to the Ya'aqov-cycle alone. claim_type is `inferred` because the deception-reading requires cross-reference to v 17 and to the non-fulfillment in subsequent chapters; the verse's surface-statement is direct, but the editorial-reading is interpretive.

3. **`shalem-shechem-arrival-three-readings`** (claim_type: `inferred`) — the *shalem* lexical-ambiguity at Gen 33:18 with three readings (adverbial: Targum/Rashi/ASV/NJPS/NRSV; toponym: LXX/Vulgate/Peshitta; wordplay: Fokkelman/Alter); the WoH translation preserves the ASV-baseline adverbial without preempting the alternatives. **applies to:** `GEN-WOH-33:18`. Justification for overlay placement: single-verse interpretive crux; no cross-corpus reach (the Yerushalayim-Shalem of Gen 14:18 / Ps 76:3 is geographically and lexically-distinct from this Shechem-area Shalem). claim_type is `inferred` because the three-reading choice is interpretive rather than grammatically-determined.

---

## Central-vs-overlay decisions: the architectural-split applied

Per the Genesis 32 ratification of the overlay-vs-central architectural split, each new entry was assessed for cross-corpus reach. The decisions for this chapter:

**Central (cross-corpus reach):**

- `sukkot-toponym-and-festival-etymology` — the toponym recurs across at least seven HB books (Genesis, Exodus, Numbers, Joshua, Judges, Kings, Chronicles, Psalms); the lexeme governs the canonical pilgrimage-festival; the entry's scope is decisively cross-corpus.
- `patriarchal-land-acquisition-pattern-makhpelah-shechem` — the pattern crosses three distinct HB books (Genesis, Joshua, 2 Samuel) at minimum; the legal-title-establishment motif is a project-wide convention.
- `el-elohei-yisrael-altar-shechem` — the entry completes the five-fold patriarchal El-compound pattern that the central glossary already documents; placing the fifth-compound in the central glossary alongside the four prior compounds preserves the structural-symmetry of the El-compound treatment.

**Overlay (chapter-singular or near-singular reach):**

- `birkhati-jacob-gift-as-blessing-restitution` — Gen 27 → Gen 33 thematic-recall confined to the Ya'aqov-cycle; no cross-corpus extension; the wider *berakhah* lexeme is covered by other entries.
- `ya-aqov-promised-seir-actual-sukkot-implicit-deception` — single-verse interpretive observation about Ya'aqov-character; no cross-corpus reach.
- `shalem-shechem-arrival-three-readings` — single-verse interpretive crux; the Yerushalayim-Shalem of Gen 14:18 is geographically-distinct and not governed by this entry.

The decisions are conservative on central-glossary growth: when in doubt, the overlay was chosen.

---

## Lens-discipline application

Per the Gen 32 ratification of the lens-discipline pattern, every new entry was reviewed for lens-leakage. The chapter's reading-positions in all eight cases are mainstream modern critical scholarship (Sarna, Westermann, Wenham, Hamilton, Speiser, Alter, von Rad, Fokkelman, Cross, Smith, Alt). Project-distinctive synthesis is reserved-for-the-wiki in every entry's rationale where applicable (notably for `el-elohei-yisrael-altar-shechem` — the patriarchal-El-religion-reconstruction is mainstream; any Wheel of Heaven reading of the local-El-cult as preserving a patriarchal-period record of a specific divine-figure is wiki-reserved); none of the entries leverage the lens on the translation surface or in the rationale-text.

The translation surface for all 20 verses is ASV-baseline with WoH proper-name conventions (Ya'aqov / Yosef / Esav / Le'ah / Kena'an / Paddan-Aram / Chamor / Shechem / Sukkot / Seir / El Elohei Yisra'el / Elohim). No verse received a lens-distinctive rendering; the translation is a defensible scholarly translation that a serious Hebrew-Bible reader would recognize as conservative-ASV.

---

## Translation status advancement

- **Status:** `draft` → `editor-review`
- **Version:** `0.1.0-draft` → `1.0.0-rc1`
- **Central glossary pin:** `2.30.0` → `2.31.0`
- **Overlay glossary pin (new field):** `1.1.0`
- **Model attribution:** `claude-opus-4-7 (translator)` + `claude-opus-4-7 (editor)`

The chapter is now ready for the Reviewer agent's verification pass and subsequent human sign-off. No speculative entries trigger the human-escalation gate; the chapter can advance through the Reviewer to human review without additional sign-off requirements on speculative content.

---

## Notes for the Reviewer

1. **The v 14 / v 17 deception reading** is `inferred` rather than `direct` and is documented as a mainstream modern critical reading with a noted minority-alternative (Cassuto's polite-diplomatic-fiction reading). The Reviewer should verify that the translation surface (which preserves Ya'aqov's stated-intention as-stated, with the discrepancy observable-by-cross-reference) does not impose the deception-reading on the English. The deception-reading is documented in commentary and in the overlay-entry rationale only.

2. **The Hivite-Hittite distinction** at v 19 is explicitly flagged in commentary; the central `bnei-het-hittites-canaanite-anatolian-question` entry is **not** cross-applied to this verse, per the architectural-split criterion (the two peoples are distinct ethnographic categories). The Hivites' own ethnographic-identity (Hurrian, per Speiser; Canaanite, per the modern critical default) is documented in the new central entry's discussion without committing to either side.

3. **The pre-existing `elohei-yisrael` central entry** has been **preserved intact** rather than modified. The new `el-elohei-yisrael-altar-shechem` entry covers the Gen 33:20 personal-name register and the patriarchal El-compound pattern; the pre-existing entry covers the collective-name register and the wider HB cross-corpus distribution. Both entries cross-reference each other in their rationales. The Reviewer may wish to consider, in a future pass, expanding the pre-existing `elohei-yisrael` entry's appliesTo to include `GEN-WOH-33:20` as a cross-corpus anchor; this Editor judged the cleaner architecture is to leave the two entries thematically-distinct (the Gen 33:20 verse foregrounds the El-compound pattern, not the collective-name register, since *Yisra'el* at 33:20 is the personal-name).

4. **The Sukkot festival cross-corpus material** (Lev 23; Deut 16; Num 29; Neh 8; Zech 14) is documented in the central entry's rationale but is **not** added to the entry's appliesTo. The appliesTo is kept narrow (GEN-WOH-33:17) so the entry governs the patriarchal-toponym occurrence only; the festival-legislation verses will get their own appliesTo when those books are translated, with the central entry then expanded to cover them. The Reviewer may wish to consider whether the festival-legislation material warrants a separate central entry or remains-folded-into the toponym entry.
