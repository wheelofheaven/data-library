# Chapter 41 Editor Report

Isaiah 41 (29 verses), wave I-6 (Isa 36–39, 41).
Editor: claude-opus-5-5 (editor), 2026-11-27.
Base: central glossary v5.0.0 and isaiah-woh overlay v4.0.0, both read-only, with `wave-i6-rulings.md` in force (rule 3 for ch. 41, including the orchestrator's correction to 41:8).
All glossary changes are in `wave-i6-ch41-overlay-diff.json` and `wave-i6-ch41-central-diff.json`.

## Summary

- **Editorial questions:** all 29 are resolved and `editorial_questions[]` is empty. None needs a founder decision. Three are listed below for review because they depart from ASV or extend a scope.
- **English-line changes:** four verses change, and each change is backed by an op in `lexical-cruxes-isaiah-41`.
  - 41:8: "offspring of Abraham my friend" → "the seed of Abraham my friend" (orchestrator correction; *zeraʿ* = "seed" in the stable 43:5; 44:3; 45:19, 25; 48:19; ASV, JPS 1917 and NJPS all have "seed").
  - 41:14: "you men of Israel" → "you people of Israel" (gender-neutral rule; BDB puts the verse among the uses of *mat* where sex is "usually not emph.").
  - 41:15: "threshing sledge" → "threshing board" for *môraḡ* (NJPS), so that "threshing sledge" stays with *ḥārûṣ* as a noun (stable 28:27).
  - 41:23: "the things that are to come hereafter" → "the things that are coming hereafter" (*hāʾōṯiyyôṯ* as in the stable 44:7).
- **Commentary:** all 29 verses have `notes.official`. No verse has a speculative paragraph: the canon in data-library (TBWTT, ETTMTTP, *Let's Welcome the Extraterrestrials*) does not cite Isa 41. I searched for "XLI" and "Isaiah 41" and found no hits, so there is no sourced premise for a reception note (rule 4).
- **Status:** `editor-review`, `1.0.0-rc1`, and "claude-opus-5-5 (editor)" is added to `modelDrafts`. `glossaryVersion` and `overlayGlossaryVersion` stay at 5.0.0 and 4.0.0; the orchestrator sets them on merge. No paragraph `translit` was added.
- **Lens audit:** no English line carries a project reading. The figure of 41:2 and 41:25 stays unnamed and in lower case, and Cyrus is mentioned only in commentary, as the commentators' identification.
- **Verification (2026-11-27):**
  - ASV of Isa 41 via bible-api.com.
  - JPS 1917 and NJPS of Isa 41 via the Sefaria API v3. NJPS is "Tanakh: The Holy Scriptures, published by JPS", not the Gender-Sensitive Edition. The NJPS notes at 41:1, 2, 3, 14, 22, 23 and 27 were checked as well.
  - NJPS 2 Sam 24:22 ("threshing boards") and MT 2 Chr 20:7 (*ʾōhaḇḵā*) via Sefaria.
  - BDB (Sefaria lexicon) for *ʾî* I/II, *ḥārûṣ*, *mat* and *ʾāwen*.
  - Stable isaiah-woh lines quoted in the commentary were read from the chapter files: 10:6, 11:11, 14:8, 17:13, 19:2, 20:6, 23:2, 23:6, 24:15, 28:27–28, 29:5, 29:16, 29:20, 31:2, 32:6, 35:1, 35:4, 35:7, 40:3–48:19 as cited, 53:2 and 54:5. Gen 34:30, Gen 11:3 and Deut 4:27 were read in the corpus.
  - Not verified, and labelled so in the commentary: 1QIsaᵃ and LXX readings, the emendations proposed by commentators, Jas 2:23, and the *šʿh* derivation at 41:23. Strong's numbers are from recall.

## Speculative entries requiring sign-off

None. Both new entries and every extension are `claim_type: direct`. No commentary paragraph is labelled speculative.

---

## Decisions for review (not blocking)

### ISA-41:14 — *mᵉṯê yiśrāʾēl* "you people of Israel"

**Issue:** *mᵉṯîm* means "men". ASV, JPS 1917 and NJPS all have "men of Israel". The orchestrator asked for a decision under the gender-neutral rule, with "mortal" reserved for *ʾĕnôš*.
**Options considered:** (A) "you people of Israel"; (B) "you men of Israel" (ASV); (C) "you few of Israel" (the prose idiom *mᵉṯê mispār*); (D) the emendation "maggot" (NJPS note).
**Decision:** (A). BDB lists Isa 41:14 among the poetic uses of *mat* where "sex [is] usually not emph.". The phrase addresses the whole people, in parallel with "worm Jacob", and the addressee is grammatically feminine. (C) adds a nuance ("few") that only *mispār* supplies in prose. (D) changes the consonants. This applies wave I-4 rule 13 directly. It is not escalated, but the founder may want to confirm it, because all three standard versions print "men". The stable 3:25 (*mᵉṯayiḵ* "Your men", soldiers in parallel with "your mighty") and 5:13 ("their honored men") are not affected.

### ISA-41:15 — *môraḡ* "threshing board"

**Issue:** the draft's "threshing sledge" for *môraḡ* would give the stable 28:27 rendering of *ḥārûṣ* to a second noun.
**Decision:** use "threshing board", NJPS's word here and at 2 Sam 24:22. *ḥārûṣ* stays the adjective "sharp" with BDB, ASV and JPS 1917. NJPS's alternative construal ("A new thresher") is reported in the commentary. The line departs from ASV ("threshing instrument") and JPS 1917 ("threshing-sledge") only in the noun.

### Central `al-tira-fear-not-divine-encouragement-formula` — scope in Isaiah

**Issue:** the chapter 35 Editor kept 35:4 out, reading the entry narrowly as "do not fear, for I am with you". 41:10 has the full formula. 41:13 and 41:14 have the bare opener with "I will help you".
**Decision:** extend the entry to 41:10, 13 and 14. The entry's own distribution list names those verses, and also 43:1, 43:5 and 44:2. The rationaleAppend sets the Isaian scope as divine first-person oracles of assurance: "for I am with you" is printed only where the Hebrew has it (41:10; 43:5), and the herald's plural exhortation at 35:4 stays outside. This leaves the chapter 35 decision intact. If the founder prefers the narrow reading, drop ISA-41:13, 41:14, 43:1 and 44:2 from the op. No line changes either way.

---

## Unresolved editorial questions

### `ISA-41:23` (and the stable 44:7, 45:11) — *ʾōṯiyyôṯ*

**Issue:** the stable chapters render the participle *ʾōṯiyyôṯ* two ways: "the things that are coming" at 44:7 and "the things to come" at 45:11. 41:22 also has *habbāʾôṯ* "the things to come", from a different verb.
**Options considered:** (A) follow 44:7 at 41:23, so that *habbāʾôṯ* and *ʾōṯiyyôṯ* differ in adjacent verses (adopted); (B) follow 45:11, so that two lemmas share "the things to come" in 41:22–23; (C) keep the draft's ASV "the things that are to come", which matches neither stable site.
**Why escalating:** the remaining inconsistency is between two signed-off stable lines (44:7 and 45:11). The Editor may not reopen them. A founder or orchestrator ruling is needed only if 45:11 should later be harmonised to "the things that are coming". This is not urgent, because Isaiah has no further *ʾōṯiyyôṯ* sites.

---

## Resolution of the Translator's 29 questions

| refId | Question | Resolution |
|---|---|---|
| 41:1 | ʾiyyîm "coastlands" and the refs | New overlay `iy-coastlands-isaiah` (book-wide); line unchanged |
| 41:1 | the 40:31 repetition | MT kept; `mt-qere-textual-policy-isaiah`; NJPS note in commentary |
| 41:2 | ṣeḏeq construal | ASV adverbial kept; JPS 1917 and NJPS reported |
| 41:2 | hēʿîr "roused" | kept (45:13, NJPS); `lexical-cruxes-isaiah-41` |
| 41:2 | yard | ASV "makes him rule" kept; NJPS "trodden … down" reported |
| 41:3 | ʾōraḥ … lōʾ yāḇôʾ | ASV kept; JPS 1917 and NJPS ("No shackle") reported |
| 41:4 | verbless first/last clause | "am" supplied (44:6; 48:12); ASV, JPS 1917 and NJPS reported |
| 41:6 | everyone … his | kept (19:2; I-5 rule); `adam-humankind-ish-man-isaiah` extended |
| 41:6 | ḥzq chain | contextual renderings kept; noted in commentary |
| 41:7 | craft vocabulary | kept (40:19–20); NJPS reported |
| 41:8 | zeraʿ | **"the seed of Abraham"** (orchestrator correction) |
| 41:8 | ʾōhăḇî | "my friend" (all versions; 2 Chr 20:7 checked) |
| 41:9 | corners / rejected / quotation extent | kept; quotation extent = JPS 1917 |
| 41:10 | tense; al-tira scope | ASV futures kept; central al-tira extended (see above) |
| 41:11 | ʾanšê constructs | relative clauses kept (rule 13: adversaries in general, not fighters) |
| 41:12 | nothing-words | ASV pattern kept and documented |
| 41:14 | mᵉṯê | **"you people of Israel"** (see above) |
| 41:14 | Redeemer syntax | ASV predicate kept (54:5); central goel extended |
| 41:15 | threshing sledge vs 28:27 | **"threshing board"** (see above) |
| 41:18 | ʾereṣ ṣiyyāh | "the dry land" (35:1 pair) kept; 53:2 context noted |
| 41:19 | trees | ASV kept, with 14:8 "cypress" |
| 41:21 | case / reasons | kept |
| 41:22 | ʾōṯiyyôṯ, hišmîaʿ | 41:22 kept; 41:23 changed (see above) |
| 41:23 | qere wᵉnirʾeh | qere followed; 41:23 added to the qere list of `mt-qere-textual-policy-isaiah` |
| 41:24 | mēʾāp̄aʿ | MT kept, "of nought" |
| 41:25 | calls / come upon / ḥōmer / potter | ASV kept; ḥōmer context clause; `yotser-potter-clay-image-isaiah` extended |
| 41:26 | ṣaddîq | "He is right" (ASV, JPS 1917, NJPS) |
| 41:27 | elliptical crux | ASV supplement kept; JPS 1917 and NJPS reported |
| 41:29 | ʾāwen; nᵉsāḵîm | "vanity" kept (BDB "= idols Is 41:29"); central nesekh not applied |

---

## Glossary changes for review

### Central glossary (`wave-i6-ch41-central-diff.json`, proposed 5.0.0 → 5.1.0)

- Modified: `al-tira-fear-not-divine-encouragement-formula`, appliesTo + ISA-41:10, 41:13, 41:14 and the stable ISA-43:1, 43:5, 44:2, with a rationaleAppend setting the Isaian scope (claim_type `direct`, unchanged).
- Modified: `goel-geullah-redeemer-redemption-cross-corpus`, + ISA-41:14, with a rationaleAppend.
- Modified: `toevah-abomination-cross-corpus-keyword`, + ISA-41:24.
- Modified: `eretz`, + ISA-41:18, with a rationaleAppend.
- Deliberately not applied: `asah` (41:4, 20), `kalah-venecheratzah-decreed-full-end-cross-corpus` (41:15), `nesekh-libation-drink-offering` (41:29).

### Per-translation overlay (`wave-i6-ch41-overlay-diff.json`, proposed 4.0.0 → 4.1.0)

- Added: `iy-coastlands-isaiah` (claim_type: `direct`). It is book-wide; the context clause keeps "islands" at 42:15; *ʾî* II "jackal" is excluded.
- Added: `lexical-cruxes-isaiah-41` (claim_type: `direct`). It covers 26 refs.
- Modified (appliesTo only, or appliesTo plus rationaleAppend; no wohChoice or claim_type change):
  - `lexical-cruxes-isaiah-11`: append only; its *ʾî* item now points to the new entry.
  - `title-and-meta-conventions-isaiah`: + 41:1.
  - `mt-qere-textual-policy-isaiah`: + 41:1, 2, 14, 23, 24, 25, 29; 41:23 is a qere site.
  - `adam-humankind-ish-man-isaiah`: + 41:6, 11, 12, 14, 28.
  - `eved-servant-identity-isaiah`: + 41:8, 9.
  - `eretz-cosmic-scope-isaiah-24`: + 41:5, 9.
  - `elohai-elohenu-doxology-isaiah-25`: + 41:10, 13.
  - `elohei-yisrael-god-of-israel-isaiah-24`: + 41:17.
  - `bara-create-isaiah`: + 41:20.
  - `elohim-el-eloah-monotheistic-formula-isaiah`: + 41:23.
  - `tohu-bare-emptiness-wasteland-isaiah`: + 41:29.
  - `yotser-potter-clay-image-isaiah`: + 41:25.

### Stable sites for the orchestrator (glossaryRefs to add on merge; English unchanged)

- `iy-coastlands-isaiah`: ISA-11:11, 20:6, 23:2, 23:6, 24:15, 40:15, 42:4, 42:10, 42:12, 42:15 (42:15 under the "islands" context clause).
- Optional: drop ISA-20:6, 23:2, 23:6 from `lexical-cruxes-isaiah-11` appliesTo. They were added there only for *ʾî*. The op format has no remove operation.
- Central `al-tira-fear-not-divine-encouragement-formula`: ISA-43:1, 43:5, 44:2.
- Later Isaiah sites expected under `iy-coastlands-isaiah` (not yet drafted): 49:1; 51:5; 59:18; 60:9; 66:19.

---

## Post-review corrections (2026-11-27)

These follow the Reviewer's two `revise` verdicts on glossary ops. No English line, no `translation.status`, no reviewerReport block and no shared glossary was changed. Only the two diff files and this report were edited.

1. **Overlay `iy-coastlands-isaiah` (add), `standardEnglish`.** The ASV quotations are corrected:
   - "coast-land" at 20:6, and "coast" at 23:2 and 23:6;
   - "islands" at 11:11, 42:12 and 42:15;
   - "isles" at 24:15, 40:15, 41:5, 42:4 and 42:10;
   - "O islands" at 41:1.
   ASV has no "country" at any of these sites; my earlier wording was wrong. The rationale now says that ASV itself uses "coast-land" and "coast" at the singular sites, which supports the shore sense. appliesTo, wohChoice and claim_type are unchanged.
2. **Central `al-tira-fear-not-divine-encouragement-formula` (modify).**
   - **Added ISA-54:4** to appliesToAdded. It is a stable line ("Do not fear, for you will not be ashamed"), and the orchestrator must add the glossaryRef there. The version note is updated to match.
   - **The rationaleAppend is reworded.** It now says the entry's Isaiah paragraph names these verses "among others", rather than implying the list is complete.
   - **10:24 is decided as outside the entry.** The scope is absolute ʾal-tîrāʾ in a divine first-person oracle of assurance. 10:24 (ʾal-tîrāʾ ʿammî … mēʾaššûr) is the prohibitive with min plus a named object of fear, printed "do not be afraid of Assyria". The same rule places 37:6 outside; that is the chapter 37 Editor's site.
   - **Other sites outside the entry:** 35:4 and 40:9 (herald speech) stay outside. 7:4, 8:12, 51:7 and 54:14 are left to their own chapters.
   - **Advisory, recorded:** 44:8 uses ʾal-tip̄ḥăḏû wᵉʾal-tirhû, not yrʾ, so it is not a site of the formula. The entry's pairing of 44:8 with "al-tira avdi Ya'aqov" belongs to 44:2.

**Stable refs for the orchestrator (updated):** central al-tira applies at ISA-43:1, 43:5, 44:2 and **54:4**. The `iy-coastlands-isaiah` stable list is unchanged.

## Founder rulings applied (sign-off 2026-11-27)

The founder signed off wave I-6 on 2026-11-27, choosing every recommended option.

- **Ratified, no line change:** 41:14 *mᵉṯê yiśrāʾēl* "you people of Israel" and 41:15 *môraḡ* "threshing board". Both are marked "ratified, founder sign-off 2026-11-27" in the `lexical-cruxes-isaiah-41` wohChoice.
- **Open item, not decided now:** harmonising the stable 45:11 *ʾōṯiyyôṯ* ("the things to come") with 44:7 and 41:23 ("the things that are coming"). This is deferred to the next revision of chapter 45. No change in this wave.
- No pending wording remained in `chapter-41.json` outside the reviewerReport. `translation.status` and the reviewerReport were not touched.
