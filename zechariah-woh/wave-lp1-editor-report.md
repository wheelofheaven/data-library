# Latter Prophets wave LP1 Editor Report

Chapters: Jer 10, Amos 4, Jonah 2 (MT numbering), Zeph 1, Zech 4, 5, 9. That is 109 verses across five new books.
Program: canon-cited chapters, each translated as a whole chapter.
Editor: claude-opus-5-5 (editor), 2026-11-01.
Base: central glossary v2.83.0 (read-only). The five overlays are new at v1.0.0 and have been applied.

## Summary

- **Editorial questions:** all 70 are resolved, and none is escalated. `editorial_questions[]` is empty in all seven files.
- **English-line changes:** 32 verses and 4 chapter titles (Jer 10; Zech 4, 5, 9). Each change is backed by an overlay entry. The full table is below.
- **Commentary:** 104 of 109 verses now have `notes.official`.
  - 10 of them carry a separately headed reception note ("**Wheel of Heaven reading (reception note, not a translation claim).**") at the canon-cited verses: Jer 10:14; Amos 4:13; Jonah 2:1, 2:11; Zeph 1:10; Zech 4:2, 4:10, 5:1, 5:9, 9:9.
  - 5:2 and 9:10 point to the notes at 5:1 and 9:9.
  - The canon readings the Translator had put into the question texts now appear only in these labelled notes.
- **Overlays:** five new files at v1.0.0.
  - Each carries the same 12-entry Latter-Prophets convention set. The text is identical across the five files, and each entry's appliesTo is the union over the five books, as the Kings overlays do it.
  - Book-specific entries: Jeremiah 4, Amos 2, Jonah 3, Zephaniah 2, Zechariah 8.
  - Total: 31 distinct entries. 30 are `direct` and 1 is `inferred`.
- **Central:** `wave-lp1-central-diff.json` holds 27 modify ops. All are appliesTo-only, with complete arrays plus `appliesToAdded`. There are no new entries.
  - Recommended version: **2.84.0**. Renumber to the next free minor if Isaiah I2 (also 2.83.0 → 2.84.0), Torah or Former-Prophets is merged first.
  - The chapters pin `glossaryVersion` 2.84.0 (pending) and carry a `verificationStatus` line that says so.
- **Status:** all seven chapters are at `editor-review`, `1.0.0-rc1`, `overlayGlossaryVersion` 1.0.0, with "claude-opus-5-5 (editor)" added to `modelDrafts`.
- **`bara` (coordinator check):** Amos 4:13 now reads "creates the wind" under the overlay `bara-create-latter-prophets`, following isaiah-woh. The central `bara` ("shape", Genesis-scoped) is not cited, is not extended, and is recorded in the diff as a deliberate non-extension. The Genesis "shape" decision stays with the founder.
- **Lens audit:** no English line carries a project reading.
  - Three lines now match the canon's English because that wording is the standard rendering: Amos 4:13 "the high places of the earth", Zech 4:10 "the whole earth" and Zech 5:9 "wind ... in their wings".
  - Where the line differs from the canon's quoted English, the reception note reports both: Jer 10:14 has the KJV "in his knowledge" against the privative reading, which the canon's French shares; Zech 5:1-2 has "roll/turned" against "scroll/again".
  - Zeph 1:10 "the Fish Gate" is capitalized as a gate name, as in NRSV and NJPS. The capital records a place-name and nothing more.

---

## Speculative entries requiring sign-off

None. One entry is `inferred`:

### `bene-hayyitshar-sons-of-fresh-oil-zechariah-4-14` (inferred)

**Source:** שְׁנֵי בְנֵי־הַיִּצְהָר, šənê ḇənê-hayyiṣhār.
**WoH choice:** "the two sons of fresh oil". This replaces the "the two anointed ones" of ASV and NRSV.
**Why inferred, not speculative:**
- The verse has neither *māšaḥ* nor *šemen*.
- *yiṣhār* is harvest oil and is never used for anointing (Rose, *Zemah and Zerubbabel*, 2000).
- Literal renderings are current in the commentaries (Petersen OTL; Boda NICOT).
- It is not consensus English, hence `inferred`.
- It carries no project lens. If anything it removes a later messianic reading from the line.

**Recommendation:** ship. The founder may prefer to keep "anointed ones" for reception continuity (F5).

---

## Founder decisions

### F1. Latter-Prophets convention split: Isaiah practice adopted, Ezekiel diverges

As directed, the five books follow **isaiah-woh** wherever Isaiah and Ezekiel differ:

| Item | These five books | isaiah-woh | ezekiel-woh |
|---|---|---|---|
| ʾĕlōhîm | God / your God / the God of hosts | God | Elohim |
| ʾereṣ | "earth" in cosmic and universal scope, "land" for territory | same | land |
| divine rûaḥ | lower-case "spirit" | spirit | ruach |
| bārāʾ | create | create | (no site) |
| maśśāʾ | oracle | oracle | (no site) |

Where the two precedents agree, the shared conventions are kept: English names, "YHWH", "the Lord YHWH", "the Lord", nested quotation marks, the Qere translated, and the MT baseline.

The draft had applied the Ezekiel/Genesis forms. It printed "Elohim" ×9 and "ruach" ×1, and it used "land" at 11 cosmic sites. All of these are corrected.

**Founder question:** ratify the Isaiah-aligned practice for the Latter Prophets, and decide whether published Ezekiel should be harmonized in a later pass.
**Recommendation:** ratify. Harmonize Ezekiel at its next wave rather than retro-editing signed-off chapters.

### F2. Corpus vocabulary alignments that diverge from isaiah-woh

As briefed, the wave aligns with these corpus rulings:
- "scroll" (Ezek 2:9; Isa 29)
- "lampstand" (2 Kgs 4:10; recommended for Ex 25)
- "officials" (Ezek 11:1)
- "shofar" (Kings, Exodus)

Two of these diverge from isaiah-woh, which kept the ASV:
- Isa 32:1, 40:23 and 43:28 have **"princes"** for *śārîm*.
- Isa 27:13 has **"a great trumpet"** for *šôp̄ār*.

**Founder question:** align Isaiah to "officials" and "shofar" at its next pass, or accept the book-level difference.
**Recommendation:** align Isaiah.

**Dependency:** `menorah-lampstand-latter-prophets` assumes that the pending exodus-woh Ex 25 ruling will be "lampstand". The Ex 25 draft still reads "candlestick" with "lampstand" recommended. If Exodus rules otherwise, the two must be reconciled.

### F3. nəʾum YHWH "declares YHWH" vs Isaiah's "says YHWH"

The draft's "declares YHWH" (the Ezekiel/ESV practice) is kept. Zechariah uses *nəʾum* and *ʾāmar* side by side (4:6; 5:4), and the two formulas should stay distinguishable in English. isaiah-woh renders both as "says".

**Recommendation:** adopt "declares" corpus-wide and align Isaiah later. Recorded in `house-conventions-latter-prophets`.

### F4. Messenger formula without quotation marks (Jer 10:2-5, 10:18)

Following isaiah-woh, "Thus says YHWH" opens an oracle without quotation marks. The draft, following Ezekiel's wave-E2 convention, had quoted Jer 10:2-5 and 10:18 and closed the speech at v5, a boundary the Hebrew does not mark.

Two kinds of speech keep their marks:
- speech inside narrative and vision dialogue (all of Zechariah 4-5);
- words quoted inside an oracle (Amos 4:1; Zeph 1:12; Jer 10:11).

**Recommendation:** ratify. This is the one point where "shared quotation conventions" had to pick a side.

### F5. Zech 4:14 "sons of fresh oil"

This is the only line change that departs from all three reference English versions (see the inferred entry above).
**Recommendation:** ship.

---

## Rulings on the brief's points

- **Jer 10:11 (Aramaic):** translated by the Hebrew rules: "the gods", "the skies and the earth", "under the skies". The draft's ASV "heavens" would have given one sky two English words across vv. 11-13. The language switch and the *ʿăḇaḏû* / *yēʾḇaḏû* wordplay are recorded in commentary, not marked typographically (`aramaic-verse-jeremiah-10-11`). The overlay's `sourceLanguages` is ["he", "arc"].
- **Jer 10:6-8, 10:** the MT is translated in full and in MT order. The LXX/4QJerᵇ minuses and the placement of v. 9 are noted at 10:5-10 (`mt-longer-edition-jeremiah-10`).
- **Zech 4:2 Qere:** "And I said" is translated, and the Ketiv "and he said" is noted. This is the one sense-changing Ketiv/Qere pair of the wave. The other two are Jer 10:13 (article only) and Jer 10:17 (archaic ending).
- **Zech 5:11:** the rafe over *lāh* is noted and the form translated "for her".
- **Vocabulary:**
  - roll → scroll: Zech 5:1, 2; title.
  - candlestick → lampstand: Zech 4:2, 11; title.
  - princes → officials: Zeph 1:8.
  - trumpet → shofar: Zeph 1:16; Zech 9:14.
  - burden → oracle: Zech 9:1; title.
- **Book-specific entries:**
  - flying scroll (`megillah-afah-flying-scroll-zechariah-5`)
  - bənê-hayyiṣhār (above)
  - seven eyes (`shivah-elleh-ene-yhwh-seven-eyes-zechariah-4-10`)
  - dāḡ gāḏôl (`dag-gadol-great-fish-jonah-2`)
  - interpreting messenger (`hammalakh-haddover-bi-interpreting-messenger-zechariah`, alongside central `malakh-yhwh-messenger` for the lexeme)
  - plus the lampstand vision, the woman in the ephah and the king of 9:9
- **Other corrections beyond the brief (accuracy, not lens):**
  - **Jer 10:5** "a scarecrow in a cucumber field". The source is miqšâ = Isa 1:8, and the reading goes back to Ep Jer 70; NRSV, NJPS, Holladay and Lundbom agree.
  - **Jer 10:17** "bundle" (BDB, NRSV, NJPS).
  - **Zeph 1:10-11** "the Fish Gate", "the Second Quarter", "the Mortar" and "merchant people". The three city place-names are made consistent under the English-name convention. *kənaʿan* here means "trader", which is also the ASV margin.
  - **Zech 9:9** "righteous and victorious". *nôšāʿ* is Niphal (passive), so the ASV's active "having salvation" is an LXX/Vulgate carry-over.
  - **Zeph 1:18** "earth" (×2), because the verse closes the universal frame of 1:2-3 (cf. 3:8). NRSV agrees; ASV and NJPS read "land". The Reviewer may want to test this one.

## Unresolved editorial questions

None.

## Disposition of the 70 Translator questions

| Chapter | Kept as drafted, with commentary | Changed |
|---|---|---|
| Jer 10 (14) | Q2 vanity, Q4 MT edition, Q8 Qere, Q9 ASV weather terms, Q10 privative min, Q12 "find it", Q13 commotion, Q14 in measure | Q1 conventions (speech marks, God, earth); Q3 scarecrow; Q5 God / earth; Q6 skies (Aramaic); Q7 earth; Q11 Qere kept, bundle |
| Amos 4 (10) | Q1 their lords, Q2 hooks, Q3 Harmon, Q4 every three days, Q5 MT harbôṯ, Q6 captured horses, Q9 his thought | Q7 God; Q8 create (not central `bara`); Q10 earth / God of hosts (high places kept) |
| Jonah 2 (8) | Q1 MT numbering, Q2 prepared, Q4 depth / flood, Q5 MT ʾaḵ, Q6 soul, Q8 kindness | Q3 God; Q7 earth |
| Zeph 1 (12) | Q1 Cushi, Q2 utterly consume, Q3 MT stumbling blocks, Q4 Chemarim, Q5 Malcam, Q7 threshold, Q10 MT accents | Q6 officials; Q8 Fish Gate; Q9 the Mortar / merchant people; Q11 shofar; Q12 earth |
| Zech 4 (8) | Q1 messenger (overlay + central), Q2 Qere, Q5 top stone, Q7 "the gold" | Q3 lampstand; Q4 spirit; Q6 earth (plummet kept); Q8 sons of fresh oil / earth |
| Zech 5 (7) | Q2 cubits, Q3 ASV niqqâ, Q4 MT ʿênām, Q5 Wickedness, Q7 rafe / base | Q1 scroll ("again" kept); Q6 earth (wind and stork kept) |
| Zech 9 (11) | Q2 MT, Q3 the Lord, Q4 bastard, Q5 MT, Q8 Greece, Q10 MT, Q11 lifted on high | Q1 oracle; Q6 righteous and victorious; Q7 earth (MT "I" kept); Q9 shofar (south kept) |

Totals: 44 kept, 26 changed.

## English-line changes (32 verses + 4 titles)

| refId | Draft | Now | Governing entry |
|---|---|---|---|
| Jer 10 title | the living Elohim | the living God | `elohim-god-latter-prophets` |
| JER 10:2, 18 | quoted oracle | oracle unquoted | `house-conventions-latter-prophets` |
| JER 10:5 | a palm-tree of turned work | a scarecrow in a cucumber field | `lexical-cruxes-jeremiah-10` |
| JER 10:10 | true/living Elohim; the land quakes | true/living God; the earth quakes | `elohim-god-…`, `eretz-earth-or-land-…` |
| JER 10:11 | the heavens and the earth … under the heavens | the skies and the earth … under the skies | `aramaic-verse-jeremiah-10-11` |
| JER 10:12, 13 | the land / the end of the land | the earth / the end of the earth | `eretz-earth-or-land-…` |
| JER 10:17 | wares | bundle | `lexical-cruxes-jeremiah-10` |
| AMO 4:11, 12 | Elohim / your Elohim | God / your God | `elohim-god-…` |
| AMO 4:13 | shapes the wind … the land … Elohim of hosts | creates the wind … the earth … God of hosts | `bara-create-…`, `eretz-…`, `elohim-god-…` |
| JNA 2:2, 7 | his/my Elohim; the land with its bars | his/my God; the earth with its bars | `elohim-god-…`, `eretz-…` |
| ZEP 1:8 | princes | officials | `sarim-officials-…` |
| ZEP 1:10 | fish gate; second quarter | the Fish Gate; the Second Quarter | `fish-gate-mishneh-maktesh-zephaniah-1-10-11` |
| ZEP 1:11 | Maktesh; the people of Canaan | the Mortar; the merchant people | same |
| ZEP 1:16 | trumpet | shofar | `shofar-…` |
| ZEP 1:18 | the whole land … inhabitants of the land | the whole earth … inhabitants of the earth | `eretz-…` |
| ZEC 4 title, 4:2, 4:11 | candlestick | lampstand | `menorah-lampstand-…` |
| ZEC 4:6 | my ruach | my spirit | `ruach-spirit-wind-breath-…` |
| ZEC 4:10, 4:14 | the whole land | the whole earth | `eretz-…` |
| ZEC 4:14 | the two anointed ones | the two sons of fresh oil | `bene-hayyitshar-…` (inferred) |
| ZEC 5 title, 5:1, 5:2 | roll | scroll | `megillah-scroll-…` |
| ZEC 5:9 | the land and the skies | the earth and the skies | `eretz-…` |
| ZEC 9 title, 9:1 | The burden (of the word) | An oracle: (the word) | `massa-oracle-…` |
| ZEC 9:7, 9:16 | our/their Elohim | our/their God | `elohim-god-…` |
| ZEC 9:9 | he is just, and having salvation | he is righteous and victorious | `tsaddiq-wenosha-ani-king-on-a-donkey-zechariah-9-9` |
| ZEC 9:10 | the ends of the land | the ends of the earth | `eretz-…` |
| ZEC 9:14 | trumpet | shofar | `shofar-…` |

---

## Glossary changes for review

### Central glossary (`zechariah-woh/wave-lp1-central-diff.json`, base 2.83.0 → 2.84.0, NOT applied)

**Modified, appliesTo only (27):**
- adam-adamah (+3)
- adonai-yhwh (+4)
- aluf-edomite-clan-chief-tribal-confederation (+1)
- arafel-thick-darkness-divine-presence-cross-corpus (+1)
- asah (+3)
- bor-pit-cistern-dry-water-shaft (+1)
- chesed-solitary-covenant-kindness (+1)
- darash-yhwh-seeking-oracle (+2)
- davar-yhwh-prophetic-formula (+2)
- eretz (+6, "land" sites only)
- eretz-shinar (+1)
- kerem-vineyard (+2)
- mahapekhah-overthrowing-formula (+1; legacy `AMOS-4:11` kept)
- malakh-yhwh-messenger (+5)
- mayim (+2)
- mifthan-ha-bayit (+1)
- mizbeach-olah (+1)
- ototh (+1)
- pesel-utemunah-… (+1)
- qorbanot-… (+3)
- shamayim (+5)
- sheol-… (+1)
- tehom (+1)
- tzarah-… (+2)
- tzeva-ha-shamayim-… (+1)
- ulam-hekhal-devir-… (+2; the entry's own "temple" context clause)
- yatsar (+2)

**Added:** none.

**Deliberate non-extensions,** recorded in the version op:
- **bara**
- **elohim-as-translation**
- eretz at the "earth" sites
- hevel (the personal name)
- nesekh (homograph)
- taninim
- otzrot-sheleg-barad
- mlk-olam
- shut-ba-aretz
- she-erit
- baal-ugaritic-baalu
- hishtachavah
- mitsrayim
- bethel-luz-name-etymology
- pelishtim-caphtor

**Concurrency:** re-base the arrays as the union if Isaiah I2, Torah or Former-Prophets lands first. Likely overlaps: eretz, shamayim, asah, yatsar, adam-adamah, pesel, qorbanot, chesed, bor-pit and adonai-yhwh. After renumbering, update `glossaryVersion` in the seven chapters.

**Promotion candidates (not proposed in this diff):** the shared entries `megillah-scroll-…`, `menorah-lampstand-…`, `sarim-officials-…`, `shofar-…` and `hevel-vanity-…` each govern a lemma that occurs in several books. They should become central entries once F2 is settled and the sibling overlays have been reconciled (Isaiah "princes"/"trumpet"; Kings/Exodus shofar entries; ecclesiastes-woh's pending heḇel ruling).

### Per-translation overlays (all new, v1.0.0, applied)

**Shared Latter-Prophets set, in all five overlays (12, all direct):**
- house-conventions-latter-prophets
- elohim-god-latter-prophets
- eretz-earth-or-land-latter-prophets
- ruach-spirit-wind-breath-latter-prophets
- mt-qere-textual-policy-latter-prophets
- bara-create-latter-prophets
- massa-oracle-latter-prophets
- megillah-scroll-latter-prophets
- menorah-lampstand-latter-prophets
- sarim-officials-latter-prophets
- shofar-latter-prophets
- hevel-vanity-latter-prophets

The text and the union appliesTo are identical in all five files, so extend all five together. The rule tôrâ → "teaching" for later chapters is carried in the house-conventions entry.

**jeremiah-woh:**
- mt-longer-edition-jeremiah-10
- aramaic-verse-jeremiah-10-11
- nivar-middaat-brutish-without-knowledge-jeremiah-10-14
- lexical-cruxes-jeremiah-10

All direct.

**amos-woh:**
- bamote-aretz-theophany-hymn-amos-4-13
- lexical-cruxes-amos-4

All direct.

**jonah-woh:**
- dag-gadol-great-fish-jonah-2
- mt-versification-jonah-2
- lexical-cruxes-jonah-2

All direct.

**zephaniah-woh:**
- fish-gate-mishneh-maktesh-zephaniah-1-10-11
- lexical-cruxes-zephaniah-1

All direct.

**zechariah-woh:**
- hammalakh-haddover-bi-interpreting-messenger-zechariah
- menorah-vision-gullah-nerot-zechariah-4
- shivah-elleh-ene-yhwh-seven-eyes-zechariah-4-10
- **bene-hayyitshar-sons-of-fresh-oil-zechariah-4-14 (inferred)**
- megillah-afah-flying-scroll-zechariah-5
- ephah-rishah-woman-in-the-ephah-zechariah-5
- tsaddiq-wenosha-ani-king-on-a-donkey-zechariah-9-9
- lexical-cruxes-zechariah-4-5-9

All direct except the one marked inferred.

---

## Notes for the Reviewer and the orchestrator

**Reviewer watch points:**
- Zeph 1:18 "earth"
- Zeph 1:10-11 place-names and "merchant people"
- Zech 4:14 "sons of fresh oil"
- Zech 9:9 "victorious"
- Jer 10:5 "scarecrow"
- Jer 10:2-5 unquoted oracle

**Library follow-ups:**
- The hosted "ASV" files `amos/chapter-4` and `jonah/chapter-2` are actually the World English Bible (2000). The Jonah file also uses English versification.
- No ASV edition of Zechariah is hosted.
- The printed ASV (1901) was the comparison text throughout. This is recorded in commentary at Jonah 2:1 and Zech 4:1.

**Not created, per the brief:** `_meta.json` for the five new books. It is needed at bundle time.

Nothing was committed or pushed.
