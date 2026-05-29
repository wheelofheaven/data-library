# Chapter 37 Editor Report

**Chapter:** Genesis 37 (the opening of the Yosef cycle — the dreams, the *ketonet passim*, and the sale into Mitsrayim)
**Editor pass:** 2026-05-29
**Status transition:** `draft` → `editor-review`
**Version transition:** `1.0.0-draft` → `1.0.0-rc1`
**Glossary pin:** central `translation-glossary.json` v2.34.0 → v2.35.0; overlay `_translation-glossary.json` v1.4.0 → v1.5.0

All twenty-three editorial questions from the Translator have been resolved — into five central-glossary entries, twelve overlay entries, one central-entry `appliesTo` extension, and per-verse commentary (twenty verses carry commentary). The translation surface stays ASV-baseline 1901 with WoH proper-name transliteration; no WoH-distinctive synthesis was introduced on the surface or in any glossary rationale.

## Speculative entries requiring sign-off

**None.** No `speculative` claim_type entries were created. Every Genesis 37 entry is `direct` (none, this pass — all the chapter's items are interpretive cruxes rather than grammatically-explicit facts) or `inferred` (all seventeen new entries). The two highest-stakes items — the *ketonet passim* crux and the Ishmaelite/Midianite/Medanite documentary doublet — are both `inferred`, not `speculative`, because in each case the surface preserves the MT / ASV-baseline and the apparatus documents named mainstream-scholarly positions without project-specific synthesis. The documentary-critical reading of the sale-doublet is presented as **mainstream modern scholarship, not a WoH-distinctive claim** (the lens-discipline pattern ratified at Gen 35-36).

No entry is blocked from advancing past `editor-review` on speculative grounds. The chapter awaits Reviewer-agent pass and human sign-off in the normal course.

## Lens-discipline application

Two items invited lens-leakage and were held to the accuracy-above-lens line:

### v 35 — *She'olah* (the descent to She'ol)

The first weighty Yosef-cycle occurrence of *She'ol* is exactly the kind of cosmologically-loaded term where a project-specific reading of the realm-of-the-dead / descent motif could leak. The entry `sheol-underworld-realm-of-the-dead` documents only the **mainstream ANE realm-of-the-dead picture** (subterranean abode of all the dead; not the individual tomb, not the later Christian "hell"); the transliteration choice is justified on standard text-critical grounds (NJPS / NRSV / Alter precedent + the term's irreducibility), and the rationale states explicitly that any project-specific reading of the descent-to-She'ol motif is **wiki-reserved**.

### v 25 / 28 / 36 — the sale-doublet documentary seam

The Ishmaelite/Midianite/Medanite doublet is a classic source-critical teaching-case. The entry documents the documentary-critical reading (J/E strand-conflation) and the harmonizing reading (overlapping nomad confederations, Judg 8:24) as **named, opposing mainstream positions** — the WoH stance is reportorial, not partisan. The surface preserves all three ethnonyms verbatim (the principal-reading principle); no smoothing, no harmonization, no documentary-synthesis is imposed on the translation.

## Central-vs-overlay architectural decisions

The ratified split (chapter-singular / near-singular → overlay; cross-corpus reach → central) was applied as follows.

### Central (cross-corpus reach) — `translation-glossary.json` v2.35.0

- **`sheol-underworld-realm-of-the-dead`** (claim_type `inferred`) — She'ol recurs across the whole corpus (Gen 42 + 44, Num 16, Deut 32, 1-2 Sam, Job, Psalms, Proverbs, Isaiah, the prophets). **CENTRAL** by decisive cross-corpus reach. Transliterates *She'ol*.
- **`ketonet-passim-ornamented-tunic-crux`** (claim_type `inferred`) — near-singular within Genesis (3 occurrences here), **but** the decisive philological evidence is the cross-corpus 2 Sam 13:18-19 parallel (the phrase's only other HB occurrence) and the lexeme *pas* reaches to Dan 5:5. The entry must govern both the Genesis and the 2 Samuel occurrences when Samuel is translated. **CENTRAL** by the 2 Samuel cross-corpus link, exactly the judgment the brief flagged. ASV-baseline "coat of many colours" preserved on the surface; the philologically-stronger long-sleeved / ornamented-status-tunic readings flagged in commentary.
- **`saris-court-official-eunuch-ambiguity`** (claim_type `inferred`) — recurs in both senses across Gen 40, Kings, Isaiah (56:3-4), Jeremiah, Esther, Daniel. **CENTRAL** by cross-corpus reach. ASV-baseline "officer" preserved.
- **`sar-ha-tabbachim-captain-of-the-guard`** (claim_type `inferred`) — fixed title across the Yosef cycle (Gen 39-41) and the Nevuzaradan *rav-tabbachim* parallel (2 Kgs 25; Jer 39-52) plus the Aramaic *tabbachayya* (Dan 2:14). **CENTRAL** by cross-corpus reach. ASV-baseline "captain of the guard" preserved.
- **`bor-pit-cistern-dry-water-shaft`** (claim_type `inferred`) — five occurrences here, plus the Yosef-cycle dungeon-*bor* (Gen 40-41) and a large literal-cistern + poetic-pit-of-the-dead corpus. **CENTRAL** by cross-corpus reach. ASV-baseline "pit" preserved; cistern-specificity (made explicit by v 24) documented.

### Central — `appliesTo` extension

- **`puncta-extraordinaria-v9-elav`** — `appliesTo` extended from `[GEN-18:9, GEN-WOH-33:4]` to add `GEN-WOH-37:12` (the dotted *nota accusativa* over את). The v 12 puncta are the same scribal-apparatus phenomenon already governed; extension formalizes the link rather than creating a duplicate entry.

### Overlay (chapter-singular / near-singular / sibling-doublet) — `_translation-glossary.json` v1.5.0

- **`toledot-yaaqov-narrative-cycle-header`** (`inferred`) — chapter-specific application of the *toledot*-formula at a narrative (not genealogical) header. **Deliberately does NOT extend the central `toledot` entry's `appliesTo`** (that entry is anchored at GEN-2:4 with the "tale of" wohChoice, which contradicts the surface "generations" rendering used at the chapter-25/36 headers). Housing this in the overlay preserves the central entry's integrity and records the header-rendering decision at its locus. **Note:** the draft's stale `toledot` glossaryRef at v 2 (which pointed at the central GEN-2:4 entry that does not govern this verse) was removed and replaced by this overlay entry.
- **`ishmaelite-midianite-medanite-documentary-doublet`** (`inferred`) — **sibling-overlay treatment per the ratified Gen-35 pattern.** Decision to use a **single** overlay entry governing all four verses (25, 27, 28, 36) rather than per-ethnonym sibling entries, because the three names are interwoven strands within a *single* chapter (not the same event across *different* chapters, the Esav-wives logic), and the editorial point is the seam between the strands. **Flagged as a promotion candidate** pending a Judges translation (the Judg 8:24 Ishmaelite=Midianite equation is the cross-corpus node).
- **`ben-zequnim-son-of-old-age`** (`inferred`) — idiom + Targumic "wise son" alternative; near-singular loaded use.
- **`dibbatam-raah-evil-report-slander`** (`inferred`) — the dual ambiguity (whose-evil; true-or-false) at the character-establishing verse.
- **`naar-lad-youth-or-attendant`** (`inferred`) — the Gen 37:2-specific syntactic ambiguity (youth vs attendant-to-the-handmaid-sons); does not attempt to govern the very common *na'ar* corpus-wide.
- **`hishtachavah-obeisance-yosef-dreams`** (`inferred`) — the dream-obeisance keyword (vv 7, 9, 10). **STRONG promotion candidate:** the verb is the structural keyword of the whole Yosef cycle (fulfilment at Gen 42:6; 43:26 + 28; 44:14; 50:18) and *the* worship/homage verb of the HB. Housed in overlay now (the editorial point is the chapter-and-cycle consistency-anchor); a central `hishtachavah-bow-down-obeisance-worship` entry should be created when the fulfilment-verses are translated, with this as the dream-anchor sibling.
- **`baal-ha-chalomot-dream-master-epithet`** (`inferred`) — chapter-singular hapax-phrase; the idiom-vs-literal-sarcasm choice.
- **`chayah-raah-evil-or-wild-beast`** (`inferred`) — the cover-story bracket (vv 20, 33); "evil" vs "wild/savage". Lev/Ezek covenant-curse "evil beasts" noted as a possible future promotion-node.
- **`nekhot-tzeri-lot-caravan-spices`** (`inferred`) — the caravan-cargo botanicals (v 25, doublet at Gen 43:11). *tzeri* / balm-of-Gil'ad (Jer, Ezek) noted as a possible future promotion-node.
- **`haker-na-nakar-recognition-motif`** (`inferred`) — the *nakar* recognition-loop (v 32, answered v 33), cross-referencing the Gen 27 (Ya'aqov deceiving Yitzchaq) and Gen 38:25-26 (Tamar to Yehudah) echoes. **Genesis-internal sibling-doublet:** a sibling overlay entry for the Gen 38 *haker-na* should be created when ch 38 is processed, cross-referencing this one.
- **`twenty-kesef-slave-price-yosef-sale`** (`inferred`) — confirms (per the Translator's flag) that the existing central money-unit entries (`kesitah`, the Gen 23 *kesef* formulae, `beqa-mishqal-shekel-weight-units`) do **NOT** govern this sale-price; documents the implied shekel-denomination and the ANE slave-price comparanda (Lev 27:5; Exod 21:32; CH; Nuzi/Mari).
- **`dotan-toponym-locative-form`** (`inferred`) — the toponym form-decision (locative *Dotaynah* collapsed to base *Dotan*; WoH 't'-transliteration not ASV "Dothan"), consistent with the v 14 Shechemah → Shechem treatment.

## Items resolved in commentary without a glossary entry

- **v 33 `tarof toraf` (doubled-infinitive intensive)** — the construction is a node in the existing central `harbah-arbeh-doubled-infinitive-intensive` pattern (cf. *mot tamut*, Gen 2:17). No new entry; the v 33 commentary cross-references the central pattern, and the central entry's glossaryRef is added at v 33. The central `harbah-arbeh` `appliesTo` was **not** extended to GEN-WOH-37:33, because that entry governs the *rbh* lemma specifically per its own rationale; the doubled-infinitive *pattern* is surfaced in commentary rather than by extending an *rbh*-anchored entry to a *trp* verb. (Flag for the Reviewer: if the project prefers a dedicated, lemma-agnostic "doubled-infinitive intensive" central entry that all such constructions point at, that is a corpus-normalization decision beyond this chapter.)
- **v 34 `saq` (sackcloth)** — standard, uncontested rendering (ASV/KJV/NJPS "sackcloth"). Commentary note on its cultic/mourning weight across the HB; no glossary entry warranted.
- **v 36 Pharaoh vs Par'oh** — **Confirmed: "Pharaoh" stands.** The established chapter-12–20 convention (every prior occurrence renders "Pharaoh") governs; the brief's proper-name-list "Par'oh" is noted in commentary as deferred to any future corpus-wide retransliteration pass. No glossary entry; the EQ is resolved by confirming the established convention.

## Standing promotion candidates and sibling-doublet recurrence nodes (for the report's running ledger)

1. **`hishtachavah-obeisance-yosef-dreams`** — strong promotion candidate; promote to central when the Yosef-cycle fulfilment-verses (Gen 42-50) and the wider worship-corpus are in view.
2. **`ishmaelite-midianite-medanite-documentary-doublet`** — promotion candidate pending Judges (Judg 8:24 node).
3. **`haker-na-nakar-recognition-motif`** — Genesis-internal sibling-doublet; create the Gen 38 sibling when ch 38 is processed; consider promotion to central if the *nakar*-recognition motif proves a corpus-wide literary node.
4. **`nekhot-tzeri-lot-caravan-spices`** — *tzeri* (balm of Gil'ad) is a Jeremiah/Ezekiel node; promotion candidate when those books are translated.
5. **`chayah-raah-evil-or-wild-beast`** — Lev 26 / Ezek 5 + 14 + 34 "evil beasts" covenant-curse node; promotion candidate.
6. **`ketonet-passim-ornamented-tunic-crux`** (already central) — its `appliesTo` should be extended to 2 Sam 13:18-19 when Samuel is translated.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

- **Version bump:** 2.34.0 → 2.35.0 (semver-minor; five additions + one `appliesTo` extension)
- **Added:** `sheol-underworld-realm-of-the-dead` (`inferred`); `ketonet-passim-ornamented-tunic-crux` (`inferred`); `saris-court-official-eunuch-ambiguity` (`inferred`); `sar-ha-tabbachim-captain-of-the-guard` (`inferred`); `bor-pit-cistern-dry-water-shaft` (`inferred`)
- **Modified:** `puncta-extraordinaria-v9-elav` — `appliesTo` extended to add `GEN-WOH-37:12`

### Per-translation overlay (`data-library/genesis-woh/_translation-glossary.json`)

- **Version bump:** 1.4.0 → 1.5.0 (semver-minor; twelve additions)
- **Added:** `toledot-yaaqov-narrative-cycle-header`; `ishmaelite-midianite-medanite-documentary-doublet`; `ben-zequnim-son-of-old-age`; `dibbatam-raah-evil-report-slander`; `naar-lad-youth-or-attendant`; `hishtachavah-obeisance-yosef-dreams`; `baal-ha-chalomot-dream-master-epithet`; `chayah-raah-evil-or-wild-beast`; `nekhot-tzeri-lot-caravan-spices`; `haker-na-nakar-recognition-motif`; `twenty-kesef-slave-price-yosef-sale`; `dotan-toponym-locative-form` (all `inferred`)

## Translation-surface changes

The translation surface stays ASV-baseline 1901 with WoH proper-name transliteration. **No wording changes from the Translator's draft were required** — every crux resolved to the ASV-baseline surface rendering (with the divergence documented in glossary + commentary), and the Translator's defaults were all confirmed. Specifically confirmed-as-stable: "a coat of many colours" (vv 3, 23, 32); "She'ol" transliterated (v 35); "an officer of Pharaoh's" and "the captain of the guard" (v 36); "Pharaoh" not "Par'oh" (v 36); all three ethnonyms preserved verbatim (Yishme'elim / Midyanim / Medanim, vv 25-36); "pit" for *bor*; "twenty pieces of silver"; "Dotan" (not "Dothan"); "made obeisance"; "this dreamer"; "an evil beast"; "spicery, balm, and myrrh"; "know now"; "without doubt torn in pieces"; "sackcloth". The only chapter-JSON change beyond commentary/glossaryRefs/status was the removal of the stale central `toledot` glossaryRef at v 2 (see the overlay-decisions section).

## Unresolved editorial questions

**None.** All twenty-three editorial questions are resolved into glossary entries (added or extended) or into per-verse commentary. None is escalated as unresolved.

## Inventory of all twenty-three editorial-question resolutions

| # | refId | Issue | Resolution |
|---|-------|-------|------------|
| 1 | 37:2 | *toledot* at a narrative header | Overlay `toledot-yaaqov-narrative-cycle-header`; ASV "generations" per ch-25/36 convention; stale central `toledot` ref removed. Commentary v 2. |
| 2 | 37:2 | *na'ar* (lad vs attendant) | Overlay `naar-lad-youth-or-attendant`; ASV "a lad". Commentary v 2. |
| 3 | 37:2 | *dibbatam ra'ah* | Overlay `dibbatam-raah-evil-report-slander`; ASV "their evil report". Commentary v 2. |
| 4 | 37:3 | *ben-zequnim* | Overlay `ben-zequnim-son-of-old-age`; ASV "son of his old age". Commentary v 3. |
| 5 | 37:3 | *ketonet passim* (the crux) | **Central** `ketonet-passim-ornamented-tunic-crux` (2 Sam 13 cross-corpus link); ASV "coat of many colours" surface, stronger readings flagged. Commentary vv 3, 23, 32. |
| 6 | 37:7 | *hishtachavah* obeisance | Overlay `hishtachavah-obeisance-yosef-dreams` (vv 7, 9, 10; strong promotion candidate); ASV "made obeisance". Commentary vv 7, 9, 10. |
| 7 | 37:12 | puncta extraordinaria over את | Central `puncta-extraordinaria-v9-elav` `appliesTo` extended to GEN-WOH-37:12. Commentary v 12. |
| 8 | 37:17 | Dotan / Dotaynah toponym | Overlay `dotan-toponym-locative-form`; "Dotan" (locative collapsed, 't'-translit). Commentary v 17. |
| 9 | 37:19 | *ba'al ha-chalomot* | Overlay `baal-ha-chalomot-dream-master-epithet`; ASV "this dreamer". Commentary v 19. |
| 10 | 37:20 | *chayah ra'ah* | Overlay `chayah-raah-evil-or-wild-beast` (vv 20, 33); ASV "an evil beast". Commentary vv 20, 33. |
| 11 | 37:20 | *bor* (pit vs cistern) | **Central** `bor-pit-cistern-dry-water-shaft` (vv 20, 22, 24, 28, 29); ASV "pit", cistern-sense documented. Commentary vv 20, 22, 24, 28, 29. |
| 12 | 37:25 | *nekhot / tzeri / lot* spices | Overlay `nekhot-tzeri-lot-caravan-spices`; ASV "spicery, balm, and myrrh". Commentary v 25. |
| 13 | 37:25 | Ishmaelite/Midianite/Medanite doublet | Overlay `ishmaelite-midianite-medanite-documentary-doublet` (vv 25, 27, 28, 36; sibling-overlay pattern; promotion candidate). Commentary vv 25, 28, 36. |
| 14 | 37:25 | ethnonym -im plural transliteration | Resolved within the doublet entry; transliterated -im plurals (Yishme'elim / Midyanim / Medanim). Commentary v 25. |
| 15 | 37:28 | *twenty kesef* slave-price | Overlay `twenty-kesef-slave-price-yosef-sale`; confirms existing money-unit entries do not apply; ASV "twenty pieces of silver". Commentary v 28. |
| 16 | 37:32 | *haker-na* (recognition) | Overlay `haker-na-nakar-recognition-motif` (Gen 27 + 38 cross-refs); ASV "know now". Commentary v 32. |
| 17 | 37:33 | *tarof toraf* (doubled-infinitive) | Commentary v 33 cross-referencing central `harbah-arbeh-doubled-infinitive-intensive`; ASV "without doubt torn in pieces". No new entry. |
| 18 | 37:34 | *saq* (sackcloth) | Commentary v 34; ASV "sackcloth". No glossary entry (uncontested). |
| 19 | 37:35 | *She'ol* (the crux) | **Central** `sheol-underworld-realm-of-the-dead`; transliterated "She'ol", lens-discipline applied. Commentary v 35. |
| 20 | 37:36 | *Medanim* (MT vs LXX/SamP) | Resolved within the doublet entry; MT *Medanim* preserved. Commentary v 36. |
| 21 | 37:36 | *saris* (officer vs eunuch) | **Central** `saris-court-official-eunuch-ambiguity`; ASV "officer". Commentary v 36. |
| 22 | 37:36 | *sar ha-tabbachim* | **Central** `sar-ha-tabbachim-captain-of-the-guard`; ASV "captain of the guard". Commentary v 36. |
| 23 | 37:36 | Pharaoh vs Par'oh | **Confirmed "Pharaoh" stands** (ch-12–20 convention). Commentary v 36. No glossary entry. |

## Reviewer-recommended attention

1. **The *ketonet passim* surface-vs-philology gap** — confirm the decision to retain the ASV-baseline "coat of many colours" on the surface while the commentary flags that the philologically-stronger readings are the long-sleeved / ornamented status-tunic (the 2 Sam 13:18 parallel, NJPS, Speiser). This is the chapter's most culturally-entrenched rendering; the editor judged surface-conservatism (accuracy-above-lens / ASV-baseline) appropriate, with the correction carried in the apparatus. The Reviewer may prefer surfacing the status-reading.
2. **The single-entry decision for the sale-doublet** — confirm the choice of one overlay entry governing all four verses rather than per-ethnonym sibling entries. Rationale: interwoven strands within a single chapter, vs the cross-chapter logic of the Esav-wives sibling pattern.
3. **The `hishtachavah` overlay-then-promote decision** — confirm housing the dream-obeisance keyword in the overlay now (chapter-and-cycle consistency-anchor) with promotion to central deferred until the Gen 42-50 fulfilment-verses. The verb is one of the most common in the HB; promoting prematurely would create a central entry with a single-chapter `appliesTo`.
4. **The `tarof toraf` no-entry decision** — confirm that the doubled-infinitive intensive at v 33 is adequately served by a commentary cross-reference to the central `harbah-arbeh-doubled-infinitive-intensive` pattern, rather than (a) extending that *rbh*-anchored entry to a *trp* verb, or (b) creating a lemma-agnostic central "doubled-infinitive intensive" entry. The latter is a corpus-normalization question beyond this chapter.
5. **The stale `toledot` glossaryRef removal at v 2** — confirm removing the central GEN-2:4-anchored `toledot` ref (whose "tale of" wohChoice and GEN-2:4-only `appliesTo` do not govern this verse) and replacing it with the overlay `toledot-yaaqov-narrative-cycle-header` entry that records the "generations" header-decision.
6. **Pharaoh vs Par'oh** — confirm "Pharaoh" stands corpus-wide pending a deliberate retransliteration pass (the brief's proper-name list says "Par'oh"; the chs-12–20 stable text says "Pharaoh").
