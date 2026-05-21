# Ezekiel 1 Sign-off Package

**Book:** Ezekiel (Wheel of Heaven Translation)
**Chapter:** 1 — The throne-vision by the Kebar canal
**Status:** stable v1.0.0
**Pinned glossary version:** v2.2.0
**Drafted by:** claude-opus-4-7
**Reviewed by:** zarazinsfuss, 2026-05-21T16:00:00+00:00

---

## Why this chapter, why now

Ezekiel 1 is the **Phase 1 cross-book pipeline pilot** per the WoH Translation Program roadmap. It tests whether the production pipeline (translator → editor → reviewer → human sign-off, with the production glossary as the artifact-of-record) generalizes off Genesis into the prophetic literature. The chapter was selected as the highest-leverage single chapter on the project's Hebrew Bible roadmap:

- **Standing public interest.** The Ezekiel-1-as-ancient-astronaut reading is the most-cited associated topic for the WoH lens outside the canon itself.
- **Strong philological backing.** The chapter has substantial modern scholarly treatment (Greenberg's Anchor Bible, Block's NICOT, Zimmerli's Hermeneia; the *kavod*-tradition literature; modern divine-council scholarship).
- **High lens leverage.** Throne-vision, four *chayyot*, *chashmal*, *ofan-b'tokh-ofan*, *raqia* above the heads, *kavod-YHWH* — six lens-loaded vocabulary clusters in one 28-verse chapter.
- **Glossary stress test.** The chapter forces the production glossary into a new vocabulary set (hapax words: *chashmal*, *bazaq*; technical phrases: *mar'eh demut*, *ruach ha-chayyah ba-ofanim*; new proper nouns: *Kevar*, *Yoyakhin*, *Buzi*). If the glossary system survives, it generalizes.

## What was produced

| Artifact | Detail |
|---|---|
| `source-he-1.json` | 28 verses from Westminster Leningrad (Tanach with Ta'amei Hamikra) via Sefaria API, Public Domain |
| `chapter-1.json` | 28 paragraphs, 24 with substantial commentary (4 brief or none); status=stable |
| `_meta.json` | Bumped from chapterCount=0 to chapterCount=1, revision=1, paragraphCount=28 |
| `translation-glossary.json` | Bumped v2.1.0 → **v2.2.0**, +18 new entries, no modifications of existing entries |

**Glossary deltas (v2.2.0):**
- 16 `direct` + 2 `inferred` + **0 `speculative`**
- No modifications of any prior entry — the pipeline confirms the existing production glossary generalizes off Genesis cleanly
- New entries cover: vision-opening vocabulary (`mar'ot-elohim`, `nehar-kevar`, `gola-yoyakhin`, `eretz-kasdim`, `yad-yhwh`, `ezekiel-ben-buzi`, `ruach-se'arah`), the lens-critical vocabulary cluster (`chashmal`, `chayyot`, `mar'eh-demut`, `arba-panim-arba-knafayim`, `ofan-b-tokh-ofan`, `tarshish-stone`, `gabotam-meleot-einayim`, `ruach-chayyot`), and the throne-presentation cluster (`qol-mayim-rabbim`, `eben-sapir-kisse`, `kavod-yhwh`)

## Lens-relevant translation choices

### 1. *chashmal* preserved untranslated (`claim_type: inferred`)

The chapter's most contested word — a hapax of unknown etymology. The LXX renders ἤλεκτρον (*elektron*, electrum); KJV/ASV 'amber'; modern translations split between 'electrum' and 'gleaming metal'. The WoH translation **preserves the Hebrew form *chashmal*** untranslated, parallel to how *Elohim* and *YHWH* are preserved. The reader encounters the chapter's own technical vocabulary directly. Commentary at v4 supplies the lexical context; the translation does not pretend to know what *chashmal* IS.

Modern Hebrew uses *chashmal* for *electricity* — a 19th-century reuse by Eliezer Ben-Yehuda that picked the biblical word for the new luminous-electrical concept. The reuse is itself a datum the commentary notes.

### 2. The *mar'eh demut* hedging formula preserved (`claim_type: direct`)

The chapter uses *mar'eh* (appearance) + *demut* (likeness) compulsively — 11 paragraphs reference the formula. Ezekiel is reporting what things *looked like* and what they had the *likeness of*, not what they were. The translation preserves the doubled hedging in English ("appearance of the likeness of..."), surfacing the chapter's epistemic discipline. A reader learns the chapter's reading-protocol from the text itself: *here is what it looked like*, not *here is what it was*.

The formula peaks at v28: *hu mar'eh demut kvod YHWH* — *this was the appearance of the likeness of the glory of YHWH*. Three layers of qualifying language. Ezekiel does not identify what he saw as YHWH directly.

### 3. *ruach* preserved as Hebrew at v12, v20, v21 (`claim_type: inferred`)

Where the chayyot move "wherever the *ruach* was to go" and "the *ruach* of the chayyah was in the wheels," the WoH translation **preserves *ruach* untranslated**. The Hebrew word covers three lexical fields (breath, wind, spirit) and the chapter is using *ruach* as the technical noun for the animating-directive principle of the chayyot-and-wheels system. Picking 'wind' or 'spirit' prematurely would resolve an ambiguity the chapter deliberately leaves open.

### 4. *raqia* rendered as 'dome' (consistent with Gen 1)

The same Hebrew word as the Gen 1:6-8 cosmic vault. The Ezekiel raqia is a smaller portable platform *above the heads of the chayyot* — but the same noun. The translation uses the same English ('dome') to surface the cosmological parallel. Commentary at v22 names the structural parallel: the throne-platform raqia (Ezek 1:22) and the cosmic raqia (Gen 1:6-8) share a noun; the chapter is positioning the chayyot apparatus as carrying *a portable raqia of the same kind* as the cosmic vault.

### 5. Hebrew-form proper names

Following the WoH convention established across Genesis (Hevel, Chavvah, Shet, Yapheth, Yoqtan, Kasdim, Bavel): *Yoyakhin* (not Jehoiachin), *Kevar* (not Chebar), *Kasdim* (not Chaldeans), *Shaddai* (not the Almighty), *Yehezkel ben Buzi* (Ezekiel's lineage in Hebrew form). The one exception: *Ezekiel* the prophet's name is kept in standard English (matching the book's catalog title across all WoH metadata).

## What the chapter does NOT do

The lens reads Ezekiel 1 as describing what looks technically like a vehicle / craft / apparatus — with chayyot (composite figures), wheels with rim-eyes, a portable raqia platform, a throne, a humanoid figure of *chashmal* and fire, and an integrated *ruach*-control system. **None of this reading is inserted into the translation itself.** The chapter's own vocabulary — *chashmal*, *chayyot*, *ofan b'tokh ofan*, *mar'eh demut*, *ruach* — already does the work. The English renders the Hebrew faithfully and the lens-reading lives in the commentary and glossary.

A credentialed Ezekiel scholar reading the translation cold (Greenberg, Block, Zimmerli register) should recognize it as careful philological work. The lens-relevant readings are surfaced in commentary where the verse warrants it; never imported into the English text.

## Items requiring human attention

**None.** All editorial questions raised during drafting were resolvable from the existing glossary or from new entries with `direct` / `inferred` claim_types. No reading is bold enough to require explicit speculative-entry approval.

The one structural decision worth flagging for future translators: *chashmal* preserved as Hebrew vs. translated. The current call (preserve as Hebrew, parallel to *Elohim*) is editorially coherent with the WoH project's pattern. A future editor might revisit; the glossary entry's rationale documents the reasoning so the decision is auditable.

## Pipeline validation

This chapter is the proof of three things the documented pipeline claimed:

1. **The production glossary generalizes off Genesis.** The 25 Genesis-specific entries from v1.0–v2.1 were not modified; 18 new Ezekiel-specific entries were added cleanly. The central glossary handled the cross-book transition without internal contradiction.
2. **The agent role-definitions work cross-book.** The Translator→Editor→Reviewer→Human sign-off pipeline that produced Genesis 10–11 produced Ezekiel 1 the same way, with the same kind of artifacts (chapter JSON, sign-off package).
3. **The mar'eh-demut discipline holds.** Ezekiel 1's strongest lens-leverage verses (v4 chashmal, v15-21 wheels, v26-28 throne and figure) are the most carefully hedged in the translation — the apparatus carries the lens, the text carries the translation.

Phase 1 of the WoH Translation Program roadmap is now complete. Phase 2 (Hebrew Bible spine: Exodus, Ezekiel 10 and 37, Job 1-2 + 38-42, Isaiah 6 + 24-27 + 53) is the natural next chunk.
