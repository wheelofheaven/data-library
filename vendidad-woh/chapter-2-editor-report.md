# Chapter 2 Editor Report — Videvdad (Vendidad), Fargard 2

## Overview

Fargard 2 has two parts.
In the first (vv. 1-19), Ahura Mazda offers the Religion to Yima, son of Vivanghat.
Yima declines, accepts instead the office of protector of the living world, and three times enlarges the overcrowded earth.
In the second (vv. 20-43), Ahura Mazda warns Yima of the coming evil winters and commands him to build the Vara, an enclosure holding the best seeds of men, livestock, dogs, birds, fires and plants.
The Vara is sealed, self-lit and self-sustaining.
This is the first chapter of a new book and the program's first Avestan-source text.
It has 41 paragraph objects covering Geldner vv. 1-43, with refIds `VID-2:{n}` and the combined unit `VID-2:12-14`.

The Translator submitted **36 editorial_questions[]**.
This pass resolves all 36 and clears the array.
One of them (the exclusion list of v. 29) is resolved only in part and escalated below.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.overlayGlossaryVersion`: new, `1.0.0`
- `translation.glossaryVersion`: `2.73.0`, unchanged (the central file was not touched)
- `translation.modelDrafts`: editor appended
- `_meta.json`: not touched

**Commentary field.** The exemplar chapters (genesis-woh, hidden-words-woh, atrahasis-woh) and the dataset builder (`scripts/build_translation_datasets.py`, which reads `notes.official`) both carry per-verse commentary as `notes: {"official": …, "community": []}`.
The Translator's template had an empty `commentary` key instead.
The Editor wrote commentary to `notes.official` in the exemplar format and removed the empty `commentary` stubs.
**29 of 41 paragraphs carry commentary.**
The formulaic repeats (vv. 9, 15-18, 21, 33-37, 39) are left without notes, as in the program's salient-verses-only policy.

**English changes.** Every paragraph's `i18n.en` was revised, each one governed by an overlay entry.
Most of the changes are register changes (thou/thy/didst → you/your/did) under `register-and-proper-name-romanization-convention-vendidad-woh`.
The substantive lexical changes are listed in the ruling table.

---

## Rulings on the 36 editorial questions

| # | refId | Question | Ruling | Overlay entry (claim_type) |
|---|---|---|---|---|
| 1 | 12-14 | Abbreviation of vv. 12-14 | **Square brackets [ ] restore abbreviated formula text verbatim from its first full occurrence in this chapter.** The '(v. 13:)' and '(v. 14:)' markers are kept and the paragraph segmentation is kept. Brackets are **not** used for editorial supply (see #29). | `ellipsis-and-bracket-convention` (direct) |
| 2 | 6 | Numbering vs SBE (vv. 6-7, 40-41) | Geldner numbering is authoritative, and SBE mismatches are noted in commentary at vv. 6, 7, 32, 40, 41. v. 7 now reads "Yima is to bear the kingly rule" (*bərəθe* = dative infinitive). | `verse-numbering-geldner-vs-sbe-convention` (direct) |
| 3 | 1 | Proper-name romanization | Plain forms without diacritics, using stem forms: **Airyana Vaejah** (was "Vaejo"). *Vanguhi Daitya* is not a proper name: the genitive is rendered "of the Good Daitya". "Son of Vivanghat" is kept. | `register-and-proper-name-romanization-convention` (direct) |
| 4 | 1 | *mainyô spênishta* | "most beneficent Spirit" kept (reference default, within the debated range holy/bounteous/beneficent) | `ahura-mazda-vocative-formula-spenishta-mainyu-datar` (direct) |
| 5 | 1 | *dâtare gaêthanãm astvaitinãm* / *dadhvå* | "Maker of the material world" and "the Maker" kept; the literal "establisher of the bony living beings" is given in commentary | same (direct) |
| 6 | 1 | *ashâum* | **"righteous one" / "righteous"** (was "thou Holy One" / "holy") | `ashavan-righteous-vocative` (direct) |
| 7 | 1 | *aperese*; *anyô mana* | "converse" and "other than me" kept | `peres-converse-anyo-mana-other-than` (direct) |
| 8 | 1 | *daēnā* and its adjectives | "the Religion" kept. At v. 42 the text now reads **"the Mazda-worshipping Religion"** (was "the Religion of Mazda"). | `daena-the-religion-ahuiri-zarathushtri-mazdayasni` (direct) |
| 9 | 2 | Yima's epithets | *srīra* "fair" kept. *huuąθβa* is now **"of the good herds"** (was "the good shepherd"). *xšaēta* is now **"the radiant"** (was "fair"). *sraēšta* is now **"fairest"** at every occurrence. | `yima-epithets-srira-hvathwa-xshaeta-sraeshta` (direct) |
| 10 | 3 | *meretô beretaca*; *nôit dâtô* | **"rememberer and bearer"** (was "preacher and bearer"); **"I was not made"** (was "born") | `mereta-bereta-daenayai-rememberer-bearer` (**inferred**) |
| 11 | 4 | *gaêthå*; *thrâtâ haretâ aiwyâxshta* | "my world" kept, with the plural noted in commentary. The triad is now **"protector, keeper, overseer"** (was "nourisher, ruler, watcher"). | `gaetha-thratar-haretar-aiwyaxshtar` (direct) |
| 12 | 5 | *xšaθra* | **"rule"** throughout (was "sway"). vv. 8/12/16 now read "winters of Yima's rule". | `xshathra-rule-and-v7-berethe` (direct) |
| 13 | 6 | The implements and their verbs | ***suβrā* is transliterated as "suwra"** because it is lexically uncertain (seal/ring, horn and arrow/awl are all proposed). ***aštrā* is now "goad"** (was "poniard"). The verbs "pressed … pierced" keep the reference construal and are flagged. At vv. 30/38 see #29. | `suwra-ashtra-implements-and-their-verbs` (**inferred**) |
| 14 | 8 | *pasu/staora*; *gavãm gâvayanem*; *gêush saredhanãm* | "flocks and herds" everywhere (the draft's unification is kept); "a fold for cattle"; "kinds of cattle" | `pasu-staora-flocks-and-herds-gav` (direct) |
| 15 | 8 | *zima*; *hañjaseñti* | "winters" kept; **"were completed"** (was "passed") | `zima-winters-reckoning-hanjasenti` (direct) |
| 16 | 10 | *raocå â upa rapithwãm …*; *fritha*; *nemangha* | **"toward the lights, southward, on the path of the sun"** (was "in light"). "O dear Spenta Armaiti, move forward and spread apart, in reverence, …" | `raocah-rapithwa-path-of-sun-spenta-armaiti-invocation` (direct) |
| 17 | 11 | *ýatha kathaca hê zaoshô* | "in whatever way it pleased him" (singular kept, referent left open) | `thrishva-thirds-and-zaosha-pleasure` (direct) |
| 18 | 11 | *thrishva*; v. 19 | v. 19 reads "by three thirds" (Avestan), against Darmesteter's "two-thirds", which is an error in the reference | same (direct) |
| 19 | 20 | The assembly | **"convened an assembly with the spiritual Yazatas — he, renowned in Airyana Vaejah of the Good Daitya"**. *srūtō* goes with the subject (nominative), *mainiiauua* is "spiritual", and the genitive is "of the Good Daitya". | `hanjamana-assembly-mainyava-yazata-sruto-airyana-vaejah` (**inferred**) |
| 20 | 22 | The winters | "the evil winters" kept, with "the evil of winter" recorded as the alternative. **Malkosan / Mahrkusha is NOT introduced** because it is not in the Avestan. "an aredvi deep" is kept as a measure. | `aghem-zimo-evil-winters-aredvi-measure` (**inferred**) |
| 21 | 23 | v. 23 | "a third of the cattle … shall go away from here" (renders *θrižat*, which SBE omits). "sheltered dwellings" (not SBE's "underground"), "river valleys" | `thrizhat-third-of-cattle-v23` (**inferred**) |
| 22 | 24 | v. 24 | Reference construal kept, but *pauruua* = "before": **"before the waters are to flood it after the melting of the snow"** (was "overflow it abundantly") | `v24-pasture-before-meltwater-footprint-wonder` (**inferred**) |
| 23 | 25 | *vara* / *varəfšuua* | "the Vara", transliterated and capitalized; the plural "the Varas" is kept | `vara-varefshva-enclosure` (direct) |
| 24 | 25 | *caretu-drâjô …* | **"the length of a race-course on each of its four sides"** (was "riding-ground") | `caretu-drajah-race-course-measure-hathra` (direct) |
| 25 | 25 | *taoxma*; *mithwaire*; *ajyamna* | "seeds", "in pairs", "inexhaustible" kept; Darmesteter's KJV-echoing "two of every kind" avoided | `taoxma-seeds-mithwaire-ajyamna` (direct) |
| 26 | 26 | The v. 26/34 terms | **"by the golden-green, by the food that is eaten and never fails"** (SBE's "green that never fades" misattaches *ajiiamna*). Dwellings read **"a chamber and a pillared porch and a front enclosure and a surrounding enclosure"**, glossed by root. | `vara-dwelling-hapaxes-and-zairigaona` (**inferred**) |
| 27 | 28 | *urvara*; *hvaretha* | **"plants" / "foods"** (was "trees / fruits", which follows the Pahlavi commentary's examples) | `urvara-hvaretha-plants-foods` (direct) |
| 28 | 29 | Exclusion list | **Partly resolved and ESCALATED.** Transparent items are corrected: "humped in front / humped behind", "misshapen teeth", "leper whose body is set apart", "marks … of Angra Mainyu". The six uncertain middle items keep Darmesteter's renderings pending a human ruling. | `exclusion-list-daxshta-of-angra-mainyu` (**inferred**) |
| 29 | 30 | v. 30/38 terms and the ellipsis | **"foremost / middle / lowest"; "passages"** (was "largest/smallest", "streets"). The gapped verb is now **⟨stroke⟩ / ⟨stroked⟩** in angle brackets (was "[press]"), read as *aiβi-* + the following *marəz-*. "a door, a window self-shining from within" is kept as a verbless apposition. | `fratema-madhema-nitema-perethu-door-window` (**inferred**); suwra entry; bracket convention |
| 30 | 31 | v. 31-32 | "in the way that men now spread out soft earth" (no potter or clay). v. 32 is translated without brackets. | `vispar-vixadh-tread-knead-soft-earth` (direct) |
| 31 | 40 | *hvadhâta / stidhâta* | **"self-created lights and lights created in the world"** (was "uncreated … created") | `hvadhata-stidhata-self-created-lights` (direct) |
| 32 | 40 | *hakeret* | **"For only once is the setting and rising of the stars and the moon and the sun seen"** (renders *hakərət*, which SBE omits). No "[a year]" is supplied. | `hakeret-once-setting-and-rising-v40` (**inferred**) |
| 33 | 41 | v. 41 | "Every forty years, from two human beings two human beings are born, a pair, female and male". **"the fairest life"** (was "happiest") | `aiwigama-forty-years-pair-births` (direct) |
| 34 | 42 | Karshipta; *vî-barat* | "the bird Karshipta"; **"spread"** (was "brought"); "Spitama" kept | `karshipta-bird-vi-barat` (direct) |
| 35 | 43 | *anghuca ratushca*; Urvatat-nara | "their lord and master" kept; the ahu/ratu pair and the later role-assignment are given in commentary | `ahu-ratu-urvatat-nara` (direct) |
| 36 | 43 | "ashem vohû...!!" | Kept as the incipit "Ashem vohu …", because the prayer does not occur in full in the chapter and so cannot be restored | `ellipsis-and-bracket-convention` (direct) |

### Points where Darmesteter (SBE 4) is wrong or silent, now documented in commentary

- **v. 19:** SBE prints "two-thirds"; the Avestan *θribiiō θrišuuaēibiiō* is "three thirds".
- **v. 23:** SBE omits *θrižat* "a third", and its "underground abodes" is an interpretation of *paxruma-*.
- **v. 40:** SBE omits *hakərət* "once"; "uncreated" mis-renders *x'aδāta-* "self-created".
- **vv. 6-7 and 40-41:** SBE re-divides the verses and leaves v. 7 untranslated as "[Obscure.]".
- **v. 32:** SBE brackets a verse that Geldner prints in the text.
- **Smaller points:**
  - v. 20: SBE construes *srūtō* with the wrong noun.
  - v. 20: SBE renders *xšaēta* as "fair".
  - v. 26: SBE's "never fades" misattaches *ajiiamna*.
  - v. 31: SBE adds "potter's clay", which the text does not name.
  - v. 42: SBE drops "Spitama".
  - vv. 25/33: SBE switches to "sheep and oxen" for *pasu/staora*.

---

## Convention decisions (recorded as overlay entries)

1. **Register.** The English is modern (you/your/did), and the formality of the dialogue (vocative strings, "I, who am Ahura Mazda") is kept.
2. **Proper names.** Names are given in plain romanization without diacritics, using stem forms (Airyana Vaejah). Hoffmann forms appear only in the glossary and the commentary.
3. **Ellipsis and brackets.** Each mark has one function:
   - **[ ]** marks the source's own "…" abbreviation, restored verbatim from its first full occurrence *in this chapter*. It is used at VID-2:12-14 (from vv. 8-10) and VID-2:43 (from v. 1). Inline "(v. 13:)" and "(v. 14:)" markers show where Geldner's verse divisions fall.
   - **⟨ ⟩** marks an English word the Editor supplied where the Avestan is elliptical and contains no wording. It is used only at VID-2:30 and VID-2:38 (⟨stroke⟩ / ⟨stroked⟩). The typographic angle brackets are used instead of `< >` to avoid HTML/Markdown collision. This matches the central `lacuna-bracket-convention-…` distinction between [restoration] and <supply>.
   - **…** marks the source's own ellipsis where no full occurrence exists in the chapter and the text cannot be restored. It is used at VID-2:43, the "Ashem vohu …" incipit.
4. **Verse numbering.** Geldner's numbering is authoritative, and SBE divergences are noted in commentary.
5. **Indexing.** Avestan has no Strong's numbers. The `strongs` field carries Bartholomae, *Altiranisches Wörterbuch* (1904) headwords for auditability (role rule 9).

---

## Speculative entries requiring sign-off

The overlay contains **no** speculative entries: 23 are `direct` and 10 are `inferred`.
The single speculative item is a **proposed central** entry, specified in full in the CENTRAL section below.
It is referenced by id in the glossaryRefs of VID-2:25, 30, 40 and 41, and named once in the v. 25 commentary under an explicit "Wheel of Heaven reading (interpretive; not part of the translation)" label.

### `vara-as-designed-preservation-habitat-woh-reading` (proposed CENTRAL)

**Source:** Vd 2.25-41 (*varəm kərənauua … taoxma upa.bara … x'aδātāca raocā̊ stiδātāca*)

**WoH choice:** No effect on any English line. The entry records the project's interpretive reading as a reading: the Vara, together with Noah's *tevah* and Atra-ḫasīs's / Utnapishtim's boat, is read as a deliberately designed preservation of living stock carried out on instruction from a non-human authority.

**Why speculative:**
- The comparison of the Vara with the flood vessels is old and well documented (Darmesteter 1898), but its genetic relation to them is contested.
- The reading of all three as instances of one designed preservation program goes beyond what any single source states.
- Features the reading would lean on (self-created lights, "artificial lights" in Darmesteter n. 29, a sealed self-sufficient habitat, controlled reproduction every forty years) are rendered literally in the text and are not argued in the commentary.

**Recommendation:** ship as `speculative`, apparatus-only. The commentary mention at v. 25 is one labelled sentence. If the founder prefers no lens mention in this chapter's commentary at all, delete that one paragraph from VID-2:25 `notes.official` and drop the id from four glossaryRefs. Nothing else depends on it.

---

## Unresolved editorial questions

### `VID-2:29` / `VID-2:37` — the exclusion list

**Issue:** Six of the ten terms (*apāuuaiia-, hərəδi-, driβi-, daiβi-, kasuuī-, vīzbāri-*) are of uncertain meaning.

**Options considered:**
- **A.** Keep Darmesteter's moral or quasi-moral readings: impotent, lunatic, malicious, liar, spiteful, jealous. This is the current state.
- **B.** Adopt a physical-defect reading for all items, as in some later lexicography (e.g. *driβi-* "with skin blemishes", *kasuuī-* "stunted", *vīzbāri-* "deformed").
- **C.** Transliterate the six in the line and gloss them in commentary.

**Why escalating:** The choice changes whether the Vara selects by bodily soundness alone or by bodily and moral soundness. The Editor cannot settle it from the lexicon without importing a guess. Option C is the most accuracy-conservative, but it would leave six opaque words in a single sentence.

### `VID-2:6` (and vv. 10, 14, 18, 30, 38) — "suwra" transliterated

**Issue:** Not unresolved, but a visible decision the human may want to overturn. The line now reads "a golden suwra".

**Options considered:**
- **A.** Transliterate. This is the current state.
- **B.** Darmesteter's "seal".
- **C.** The Pahlavi "ring".

**Why escalating:** Readers will meet an untranslated word six times. The Editor judged that "seal" would assert an identification the evidence does not support, and that it would also tilt v. 30 toward a "sealing with a seal" reading.

### `VID-2:30` / `VID-2:38` — ⟨stroke⟩

**Issue:** The supplied verb depends on reading the preverb *aiβi-* with the following *marəz-* (gapping).

**Options considered:**
- **A.** ⟨stroke⟩. This is the current state.
- **B.** The draft's "[press]", imported from v. 10.
- **C.** Leave the gap visible ("And ⟨…⟩ over the Varas with the golden suwra").

**Why escalating:** It is low-stakes, but it is the only editorial supply in the chapter. The Reviewer should confirm it.

---

## Glossary changes for review

### Central glossary

**None written.** The central file is read-only for this run. All changes are proposed in the next section.

### Per-translation overlay

New file `vendidad-woh/_translation-glossary.json`, version 1.0.0, released 2026-10-31, `sourceLanguages: ["ave"]`, with 33 entries:

- **Conventions (direct, 3):**
  - `register-and-proper-name-romanization-convention-vendidad-woh`
  - `ellipsis-and-bracket-convention-vendidad-woh`
  - `verse-numbering-geldner-vs-sbe-convention-vendidad-woh`
- **Lexical, direct (20):**
  - `ahura-mazda-vocative-formula-spenishta-mainyu-datar-…`
  - `ashavan-righteous-vocative-…`
  - `peres-converse-anyo-mana-other-than-…`
  - `daena-the-religion-…`
  - `yima-epithets-srira-hvathwa-xshaeta-sraeshta-…`
  - `gaetha-thratar-haretar-aiwyaxshtar-…`
  - `xshathra-rule-and-v7-berethe-…`
  - `pasu-staora-flocks-and-herds-gav-…`
  - `zima-winters-reckoning-hanjasenti-…`
  - `raocah-rapithwa-path-of-sun-spenta-armaiti-invocation-…`
  - `thrishva-thirds-and-zaosha-pleasure-…`
  - `vara-varefshva-enclosure-…`
  - `caretu-drajah-race-course-measure-hathra-…`
  - `taoxma-seeds-mithwaire-ajyamna-…`
  - `urvara-hvaretha-plants-foods-…`
  - `vispar-vixadh-tread-knead-soft-earth-…`
  - `hvadhata-stidhata-self-created-lights-…`
  - `aiwigama-forty-years-pair-births-…`
  - `karshipta-bird-vi-barat-…`
  - `ahu-ratu-urvatat-nara-…`
- **Lexical, inferred (10):**
  - `mereta-bereta-daenayai-rememberer-bearer-…`
  - `suwra-ashtra-implements-and-their-verbs-…`
  - `hanjamana-assembly-mainyava-yazata-sruto-airyana-vaejah-…`
  - `aghem-zimo-evil-winters-aredvi-measure-…`
  - `thrizhat-third-of-cattle-v23-…`
  - `v24-pasture-before-meltwater-footprint-wonder-…`
  - `vara-dwelling-hapaxes-and-zairigaona-…`
  - `exclusion-list-daxshta-of-angra-mainyu-…`
  - `fratema-madhema-nitema-perethu-door-window-…`
  - `hakeret-once-setting-and-rising-v40-…`
- **Speculative (0).**

(All overlay ids end in `-vendidad-woh`.)

---

## CENTRAL — apply by orchestrator

Central v2.73.0 has no Avestan entries.
The proposed changes below add 3 new entries and extend `appliesTo` on 4 existing ones (a semver-minor bump, e.g. to 2.74.0).
The chapter's glossaryRefs already cite these ids.

### 0. Top-level

- Add `"ave"` to `sourceLanguages`, giving `["he","sux","akk","uga","arb","grc","ave"]`.
- Add a scopeNote line: "v2.74.0: first Avestan-source entries (Vendidad Fargard 2, Yima and the Vara)."

### 1. NEW — `vara-tevah-eleppu-divinely-instructed-refuge-against-world-catastrophe-cross-corpus` (inferred)

```json
{
  "id": "vara-tevah-eleppu-divinely-instructed-refuge-against-world-catastrophe-cross-corpus",
  "source": "Avestan vara- (Vd 2.25-38); Hebrew תֵּבָה tevah (Gen 6:14-16); Akkadian eleppu (Atra-ḫasīs III i; Gilgamesh XI 24-31)",
  "translit": "varəm kərənauua (Vd 2.25); ʿăśēh lᵉkā tēḇat ʿăṣê-gōp̄er (Gen 6:14); uqur bīta bini eleppa (Gilg. XI 24)",
  "strongs": "Bartholomae AirWb s.v. vara-; H8392 (tevah); CAD E 90-96 s.v. eleppu",
  "lemma": "vara-; tevah; eleppu",
  "partOfSpeech": "cross-corpus narrative-structure entry: a refuge built to divine specification by one forewarned individual to preserve living stock through a world-destroying catastrophe",
  "literal": "Avestan: an enclosure, a race-course long on each of four sides, stocked with the seeds of men, livestock, dogs, birds, fires and plants, sealed, with a self-shining window; Hebrew: a gopher-wood box-vessel with a roof-opening, stocked with Noah's household and pairs of every kind; Akkadian: a boat, sealed with pitch, stocked with family, craftsmen, animals and 'the seed of all living creatures'",
  "standardEnglish": "the Vara / var of Yima (Darmesteter 1898 and later Iranists); the ark (Gen); the boat (Atra-ḫasīs, Gilgamesh XI)",
  "wohChoice": "Render each structure in its own terms in its own translation ('the Vara' — never 'ark'; 'ark' for tevah per central `tevah`; 'boat' for eleppu per central `ma-gur-eleppu-tevah-flood-vessel-cross-corpus`); document the structural parallel, and its contested genetic status, here and in per-verse commentary only.",
  "claim_type": "inferred",
  "rationale": "Vendidad 2 narrates a sequence closely parallel to the Mesopotamian and Hebrew flood narratives: a chosen individual (Yima) is forewarned by the supreme deity (Ahura Mazda) of a catastrophe that will destroy the living (Vd 2.22-24), is instructed to build a refuge to given dimensions (2.25: 'the length of a race-course on each of its four sides'), stocks it with the seed of every kind in pairs (2.25-28), excludes the defective (2.29), seals it with a light-opening (2.30), and asks how to build it and is instructed (2.31). Darmesteter (SBE 4, 1898, introduction to Fargard 2) already judged that 'it is difficult not to acknowledge in the latter legend a Zoroastrian adaptation of the deluge', while noting the essential difference that the Iranian catastrophe is a winter, frost and snow, with a meltwater flood only as aftermath (2.24), and the story has also been read as an indigenous Iranian winter myth with no genetic link to the Mesopotamian flood (discussed in Boyce, A History of Zoroastrianism I, 1975, pp. 92 ff.). The structural parallels are textual facts and are uncontroversial as observations; whether they reflect borrowing, common inheritance or independent development is disputed, which is why the entry is marked inferred rather than direct. Divergences to preserve: the Vara is a land enclosure, not a vessel; its occupants are selected by excellence (2.27 'greatest, best, fairest'), not by righteousness (Gen 6:9) or kinship; the catastrophe is not presented as punishment; and the Vara is a permanent habitation with its own lights and regulated births (2.40-41), not a temporary vessel. The Hebrew and Akkadian sides are governed by the existing central entries `tevah`, `ma-gur-eleppu-tevah-flood-vessel-cross-corpus`, `flood-vessel-construction-cubic-vs-rectangular-gilgamesh-genesis-cross-corpus` and `preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus`, to which this entry is a sibling.",
  "appliesTo": ["VID-2:22", "VID-2:24", "VID-2:25", "VID-2:28", "VID-2:30", "VID-2:33", "VID-2:36", "VID-2:38"]
}
```

Suggested sibling back-links (optional, in rationale text only): mention this id in the rationales of `tevah` and `ma-gur-eleppu-tevah-flood-vessel-cross-corpus`.

### 2. NEW — `yima-yama-son-of-vivanghat-vivasvant-first-mortal-king-indo-iranian-cross-corpus` (direct)

```json
{
  "id": "yima-yama-son-of-vivanghat-vivasvant-first-mortal-king-indo-iranian-cross-corpus",
  "source": "Avestan yima- vīuuaŋhana- (Vd 2.3 etc.); Vedic yamá- vaivasvatá- (RV 10.14.1, 10.10)",
  "translit": "Yima, son of Vīuuaŋhuuaṇt / Yama, son of Vivasvant",
  "strongs": "Bartholomae AirWb s.v. yima-, vīuuaŋhuuaṇt-; MW s.v. yama, vivasvat",
  "lemma": "yima-; yama-",
  "partOfSpeech": "cross-corpus proper-name identity: the Indo-Iranian primeval figure Yima/Yama and his father Vīuuaŋhuuaṇt/Vivasvant",
  "literal": "Yima (Avestan) = Yama (Vedic); Vīuuaŋhuuaṇt = Vivasvant",
  "standardEnglish": "Yima son of Vivanghat (Darmesteter); Yama son of Vivasvant (Rigveda translations); later Persian Jam / Jamšēd",
  "wohChoice": "Retain each tradition's name-form ('Yima, son of Vivanghat' in the Vendidad); document the identity and the divergent roles here",
  "claim_type": "direct",
  "rationale": "The Avestan Yima son of Vīuuaŋhuuaṇt and the Vedic Yama son of Vivasvant are the same inherited Indo-Iranian figure; the name and the patronymic correspond exactly, and the identification is a standard datum of Indo-Iranian philology. The two traditions develop him differently: in the Rigveda (10.14) Yama is the first mortal to die, who found the path for the dead and rules over them; in the Avesta Yima is the first mortal to whom Ahura Mazda spoke (Vd 2.2), a king under whose rule there is no death (Vd 2.5), and the builder of the Vara (Vd 2.25-38). Bruce Lincoln (Death, War, and Sacrifice, 1991, p. 28; cited in the avesta.org edition of Darmesteter's Fargard 2) compares Yima's enclosure with Yama's realm of the dead; that comparison is recorded as a scholarly position, not adopted in translation. The later Persian name Jamšēd continues Avestan Yima xšaēta 'Yima the radiant' (Vd 2.20-21), which is why the WoH Vendidad renders xšaēta distinctly as 'radiant'.",
  "appliesTo": ["VID-2:2", "VID-2:3"]
}
```

### 3. NEW — `vara-as-designed-preservation-habitat-woh-reading` (**SPECULATIVE — requires human sign-off before ship**)

```json
{
  "id": "vara-as-designed-preservation-habitat-woh-reading",
  "source": "Vd 2.25-41 (varəm kərənauua; taoxma upa.bara; miθβairē; x'aδātāca raocā̊ stiδātāca; caθβarəsatəm aiβi.gāmanąm)",
  "translit": "the Vara of Yima as read in the Wheel of Heaven framework",
  "strongs": "Bartholomae AirWb s.v. vara-, taoxman-, x'aδāta-",
  "lemma": "vara-",
  "partOfSpeech": "project interpretive-synthesis entry (apparatus only; governs no English rendering)",
  "literal": "(not applicable — interpretive reading)",
  "standardEnglish": "(no standard equivalent — the standard readings are a mythic paradise-refuge, or an Iranian adaptation of the flood story)",
  "wohChoice": "No change to any translated line. The Vendidad English renders vara-, taoxman-, x'aδāta-/stiδāta- and the forty-year births literally (overlay entries in vendidad-woh). This entry records, as an explicitly labelled reading, that the Wheel of Heaven framework reads the Vara, with Noah's tevah and Atra-ḫasīs's / Utnapishtim's boat, as an account of a deliberately designed preservation of living stock, carried out on instruction from a non-human authority, through a catastrophe.",
  "claim_type": "speculative",
  "rationale": "The structural parallel between the Vara and the flood vessels is documented and marked inferred at `vara-tevah-eleppu-divinely-instructed-refuge-against-world-catastrophe-cross-corpus`; this entry goes further, reading the three accounts as instances of one designed preservation programme, which no single source states and which mainstream scholarship does not hold. Textual features the reading draws on are all rendered literally and neutrally in the translation: the instruction to build to dimensions (Vd 2.25), the gathering of seeds in pairs selected for excellence (2.27-28), the exclusion of the defective (2.29), the sealed structure with a self-shining window (2.30), lights that are 'self-created' and 'created in the world' (2.40; Darmesteter n. 29 himself glosses the second class as 'artificial lights'), and births regulated at two-for-two every forty years (2.41). The reading is marked speculative because it is an interpretive synthesis across traditions, and it is confined to the apparatus: it may be named in commentary under an explicit 'Wheel of Heaven reading (interpretive)' label and argued in wiki or article prose, but it must never shape the English of any translated line. Requires explicit human sign-off by name before the chapter ships.",
  "appliesTo": ["VID-2:25", "VID-2:30", "VID-2:40", "VID-2:41"]
}
```

### 4. EXTEND `appliesTo` of existing central entries (found by grep)

| Existing central id | Add to `appliesTo` | Reason |
|---|---|---|
| `preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus` (direct) | `VID-2:25`, `VID-2:27`, `VID-2:28`, `VID-2:33`, `VID-2:35`, `VID-2:36` | Avestan *taoxma upa.bara* "bring the seeds" of men, livestock, plants (Vd 2.25-28, 33-36) is the Iranian member of the seed-preservation cluster (Sumerian *numun nam-lu2-ulu3*, Gilg. XI 27/82-85 *zēr napšāti kalāma*, Gen 6:19-20). Suggested one-sentence addition to the rationale: "Avestan Vd 2.25-36 uses *taoxman-* 'seed' for the stock of men, animals, fires and plants brought into Yima's Vara, selected as 'the greatest, best and fairest' and kept 'in pairs'." |
| `paradise-by-negation-no-predation-no-illness-no-aging-cross-corpus` (direct) | `VID-2:5`, `VID-2:29`, `VID-2:37` | Vd 2.5 defines Yima's reign by enumerated absence ("neither cold wind nor hot, neither disease nor death"), and 2.29/37 define the Vara by enumerated exclusions. |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (direct) | `VID-2:12-14`, `VID-2:30`, `VID-2:38`, `VID-2:43` | The Vendidad overlay's bracket convention adopts the central [restoration] vs <supply> distinction (supply printed as ⟨ ⟩). Optional: add a note that Avestan formula-abbreviation restorations use [ ]. |
| `ab-bur-aptu-chalon-ha-tevah-flood-boat-window-cross-corpus` (direct) | `VID-2:30`, `VID-2:38` | *duuarəm raocanəm x'āraoxšnəm* "a door, a window self-shining from within" is a comparandum to the flood-boat window (Gen 6:16 / 8:6; Gilg. XI). Comparandum only, with no claim of dependence. The orchestrator may skip this if the entry is to stay strictly Sumerian-Akkadian-Hebrew. |

Not extended, deliberately:
- `ma-gur-eleppu-tevah-flood-vessel-cross-corpus` is not extended because the Vara is not a vessel. It is linked as a sibling from new entry 1 instead.
- `divine-decree-to-destroy-humankind-flood-trope-cross-corpus` is not extended because in Vd 2 Ahura Mazda warns of the winters but does not decree them, and the text does not say who sends them. The demonic Malkosan attribution belongs to the Pahlavi commentary only.

---

## Lens-routing summary

- **No English line carries the lens.** No line uses "ark" or "two of every kind" (Darmesteter's KJV echo). No line uses "Malkosan", "underground", "potter's clay" or "uncreated lights", all of which are reference or later-tradition intrusions. *suβrā* is not identified.
- The Flood/ark resonance appears in commentary as hedged comparative philology at vv. 22, 25, 27 and 30, with the contested status stated at v. 22.
- The WoH reading appears **once**, at v. 25, as a single paragraph labelled "Wheel of Heaven reading (interpretive; not part of the translation)". It points to the speculative central proposal.

## Escalation list (for human sign-off)

1. **SPECULATIVE:** `vara-as-designed-preservation-habitat-woh-reading` (proposed central). It needs explicit sign-off by name before ship, or deletion of the v. 25 commentary paragraph and 4 glossaryRefs.
2. **Unresolved:** the VID-2:29/37 exclusion list. Six uncertain items still carry Darmesteter's renderings (options A/B/C above).
3. **Decision for review:** "suwra" is transliterated at six occurrences, instead of "seal".
4. **Decision for review:** the editorial supply ⟨stroke⟩ / ⟨stroked⟩ at VID-2:30/38.
