# Canon-cited program — latter-prophets — human sign-off package

| Chapter | Verses | Approve | Revise | Flag |
|---|---|---|---|---|
| Jeremiah 10 — The idols of the nations and the living God | 25 | 25 | 0 | 0 |
| Amos 4 — The cows of Bashan, the refrain of the plagues, and he who forms the mountains | 13 | 13 | 0 | 0 |
| Jonah 2 — The great fish and Jonah's prayer from its belly | 11 | 11 | 0 | 0 |
| Zephaniah 1 — The great day of YHWH is near | 18 | 18 | 0 | 0 |
| Zechariah 4 — The golden lampstand and the two olive trees | 14 | 12 | 2 | 0 |
| Zechariah 5 — The flying scroll and the woman in the ephah | 11 | 11 | 0 | 0 |
| Zechariah 9 — The oracle against the nations and the king riding on a donkey | 17 | 17 | 0 | 0 |

See the combined summary `canon-cited-final-signoff-summary.md` for decisions and fixes.

---

## Editor report (inlined)

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


---

## Reviewer report

### Jeremiah 10 — The idols of the nations and the living God



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with no interpretive content. Verified in the lines: English names, 'the Lord YHWH' / 'the Lord', unquoted messenger formula (Jer 10:2, 18), quoted speech inside oracles and visions, and nəʾum 'declares' kept distinct from ʾāmar 'says' (Zech 4:6 against 5:4). Two open points are recorded under founder recommendations: F3, where the reviewer supports 'declares', and F4, where the reviewer supports ratification. Text identical in all five overlays (hash-checked)."}, {"glossary_id": "hevel-vanity-latter-prophets", "status": "approve", "citations": ["BDB s.v. הֶבֶל I", "Holladay, Jeremiah 1 (Hermeneia), on 10:3"], "reasoning": "Approve: the literal sense 'breath' and the idol polemic (Deut 32:21) are stated accurately, 'vanity' keeps the Jer 10:3/8/15 repetition, and the homograph central hevel (Abel) is correctly not extended."}, {"glossary_id": "lexical-cruxes-jeremiah-10", "status": "approve", "citations": ["BDB s.v. מִקְשָׁה II; כִּנְעָה", "Holladay, Jeremiah 1 (Hermeneia)", "Lundbom, AB 21A"], "reasoning": "Approve. 'scarecrow in a cucumber field' (miqšâ = Isa 1:8; Ep Jer 70) and 'bundle' (BDB) are better grounded than the ASV readings, and 10:18 and 10:24 keep the MT/ASV. direct is acceptable since both changed readings are lexi
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 25 lines in the English alone. No English line reads as interpretation. The canon-cited verses (10:14) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "25 verdicts: 25 approve. Glossary/op reviews: 19 (18 approve, flag-for-human elohim-god-latter-prophets). Status -> awaiting-human."

### Amos 4 — The cows of Bashan, the refrain of the plagues, and he who forms the mountains



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with no interpretive content. Verified in the lines: English names, 'the Lord YHWH' / 'the Lord', unquoted messenger formula (Jer 10:2, 18), quoted speech inside oracles and visions, and nəʾum 'declares' kept distinct from ʾāmar 'says' (Zech 4:6 against 5:4). Two open points are recorded under founder recommendations: F3, where the reviewer supports 'declares', and F4, where the reviewer supports ratification. Text identical in all five overlays (hash-checked)."}, {"glossary_id": "lexical-cruxes-amos-4", "status": "approve", "citations": ["Andersen and Freedman, Amos (AB 24A, 1989)", "Paul, Amos (Hermeneia, 1991)"], "reasoning": "Approve: at each site the MT/ASV is kept and the alternatives are reported. Non-blocking: the related chapter note at 4:3 attributes 'the dung-heap' to Aquila; verify that attribution. The overlay text itself does not make the attribution."}, {"glossary_id": "mt-qere-textual-policy-latter-prophets", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012)", "BHS/WLC Ketiv-Qere at the three sites"], "reasoning": "Verified against the source: the three bracketed Ketiv/Qere pairs are Jer 10:13 (article), Jer 10:17 (archaic -tî) and Zech 4:2 (wyʾmr/wāʾōmar, sense-changing
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 13 lines in the English alone. No English line reads as interpretation. The canon-cited verses (4:13) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "13 verdicts: 13 approve. Glossary/op reviews: 15 (14 approve, flag-for-human elohim-god-latter-prophets). Non-blocking commentary fixes at AMO-WOH-4:3. Status -> awaiting-human."

### Jonah 2 — The great fish and Jonah's prayer from its belly



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "dag-gadol-great-fish-jonah-2", "status": "approve", "citations": ["Sasson, Jonah (AB 24B, 1990)", "Limburg, Jonah (OTL, 1993)", "Rashi on Jonah 2:2 (MT)"], "reasoning": "Approve the rendering: 'a great fish', 'prepared' and 'vomited out' are literal, and the canon's submarine reading is kept to labelled notes. Non-blocking factual fix, the same one as in the 2:2 note: the two-fish midrash is attributed to Pirqe de-Rabbi Eliezer 10, but the reviewer finds it in Rashi ad loc. (Midrash Yonah) and not in PRE 10. Verify and correct in both places."}, {"glossary_id": "mt-versification-jonah-2", "status": "approve", "citations": ["WLC Jonah 2 (source-he-2.json)", "TBWTT ch. 3"], "reasoning": "Approve: MT numbering is checked against the source (11 verses, 2:1 = English 1:17), it is consistent with the corpus refId practice, and it matches the canon's 'Jonas, II-1 / II-11' citations."}, {"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with no interpretive content. Verified in the lines: English names, 'the Lord YHWH' / 'the Lord', unquoted messenger formula (Jer 10:2, 18), quoted speech inside oracles and visions, and nəʾum 'declares' kept distinct from ʾāmar 'says' (Zech 4:6 against 5:4). Two open points are recorded under founder recommendations: F3, where the reviewe
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 11 lines in the English alone. No English line reads as interpretation. The canon-cited verses (2:1, 2:11) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "11 verdicts: 11 approve. Glossary/op reviews: 15 (14 approve, flag-for-human elohim-god-latter-prophets). Non-blocking commentary fixes at JNA-WOH-2:2. Status -> awaiting-human."

### Zephaniah 1 — The great day of YHWH is near



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with no interpretive content. Verified in the lines: English names, 'the Lord YHWH' / 'the Lord', unquoted messenger formula (Jer 10:2, 18), quoted speech inside oracles and visions, and nəʾum 'declares' kept distinct from ʾāmar 'says' (Zech 4:6 against 5:4). Two open points are recorded under founder recommendations: F3, where the reviewer supports 'declares', and F4, where the reviewer supports ratification. Text identical in all five overlays (hash-checked)."}, {"glossary_id": "lexical-cruxes-zephaniah-1", "status": "approve", "citations": ["Berlin, Zephaniah (AB 25A)", "Roberts, Nahum, Habakkuk, and Zephaniah (OTL, 1991)"], "reasoning": "Approve: the MT/ASV is kept at all six sites, the accent division at 1:14 was verified in the source, and the alternatives are reported."}, {"glossary_id": "mt-qere-textual-policy-latter-prophets", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012)", "BHS/WLC Ketiv-Qere at the three sites"], "reasoning": "Verified against the source: the three bracketed Ketiv/Qere pairs are Jer 10:13 (article), Jer 10:17 (archaic -tî) and Zech 4:2 (wyʾmr/wāʾōmar, sense-changing), and the Qere is translated at each. The versional readings listed are reported and not a
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 18 lines in the English alone. No English line reads as interpretation. The canon-cited verses (1:10) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "18 verdicts: 18 approve. Glossary/op reviews: 19 (19 approve). Status -> reviewer-approved."

### Zechariah 4 — The golden lampstand and the two olive trees

- **ZEC-WOH-4:10** — revise: Revise (speech marks; the eyes clause is approved). The quotation opened at v9 for YHWH's word (vv8-10a) closes only at the end of v10, so 10b, which the commentary itself calls the messenger's deferred answer to v4, is printed as part of YHWH's word to the prophet. Proposed: '... and shall see the plummet in the hand of Zerubbabel. "These seven are the eyes of YHWH; they run to and fro through the whole earth."' This closes YHWH's word after 'Zerubbabel', reopens for the messenger, and drops the ASV's supplied 'For' before 'they shall rejoice' (wəśāmḥû has no kî); cf. NRSV's paragraphing. 'the whole earth' (2 Chr 16:9) is approved. The reception note matches TBWTT ch. 3 and is labelled.
- **ZEC-WOH-4:13** — revise: Revise. The Hebrew is wayyōʾmer ʾēlay lēʾmōr 'And he said to me'; there is no wayyaʿan, so the ASV's 'And he answered me and said' adds a verb that is not in the text. Contrast vv4, 5, 11 and 12, where 'answered' renders ʿnh. Proposed: 'And he said to me, "Do you not know what these are?" And I said, "No, my lord."'

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "hammalakh-haddover-bi-interpreting-messenger-zechariah", "status": "approve", "citations": ["Meyers and Meyers, AB 25B (1987)", "Petersen, OTL (1984)"], "reasoning": "Approve: a fixed title translated identically, kept distinct from the malʾaḵ YHWH, with the dōḇēr bî 'speak through' option correctly noted."}, {"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with no interpretive content. Verified in the lines: English names, 'the Lord YHWH' / 'the Lord', unquoted messenger formula (Jer 10:2, 18), quoted speech inside oracles and visions, and nəʾum 'declares' kept distinct from ʾāmar 'says' (Zech 4:6 against 5:4). Two open points are recorded under founder recommendations: F3, where the reviewer supports 'declares', and F4, where the reviewer supports ratification. Text identical in all five overlays (hash-checked)."}, {"glossary_id": "menorah-lampstand-latter-prophets", "status": "approve", "citations": ["HALOT s.v. mənôrâ", "2KI-WOH-4:10"], "reasoning": "Approve: 'candlestick' is an anachronism, and 2-kings-woh 4:10 already prints 'lampstand' (checked). The Exodus 25 dependency is correctly disclosed. The canon's 'seven-branched candlestick' is reception only and kept out of the line."}, {"glossary_id": "menorah-vision-gullah-nerot-zechariah-4", "status": "appro
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 14 lines in the English alone. No English line reads as interpretation. The canon-cited verses (4:2, 4:10) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "14 verdicts: 12 approve, revise ZEC-WOH-4:10, revise ZEC-WOH-4:13. Glossary/op reviews: 13 (13 approve). Status -> awaiting-human."

### Zechariah 5 — The flying scroll and the woman in the ephah



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "megillah-scroll-latter-prophets", "status": "approve", "citations": ["BDB s.v. מְגִלָּה", "EZK-WOH-2:9"], "reasoning": "Approve: a register update that aligns with ezekiel-woh 2:9 ('a scroll of a book', checked in the data)."}, {"glossary_id": "megillah-afah-flying-scroll-zechariah-5", "status": "approve", "citations": ["GKC §120d", "Meyers and Meyers, AB 25B"], "reasoning": "Approve. 'flying scroll', the cubits, 'again' (GKC §120d) and the 1 Kgs 6:3 porch parallel are accurate, and the canon's 'flying craft' is confined to a labelled note."}, {"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with no interpretive content. Verified in the lines: English names, 'the Lord YHWH' / 'the Lord', unquoted messenger formula (Jer 10:2, 18), quoted speech inside oracles and visions, and nəʾum 'declares' kept distinct from ʾāmar 'says' (Zech 4:6 against 5:4). Two open points are recorded under founder recommendations: F3, where the reviewer supports 'declares', and F4, where the reviewer supports ratification. Text identical in all five overlays (hash-checked)."}, {"glossary_id": "hammalakh-haddover-bi-interpreting-messenger-zechariah", "status": "approve", "citations": ["Meyers and Meyers, AB 25B (1987)", "Petersen, OTL (1984)"], "reasoning": "Approve: a fixed title transla
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 11 lines in the English alone. No English line reads as interpretation. The canon-cited verses (5:1 (with 5:2), 5:9) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "11 verdicts: 11 approve. Glossary/op reviews: 13 (13 approve). Non-blocking commentary fixes at ZEC-WOH-5:3. Status -> reviewer-approved."

### Zechariah 9 — The oracle against the nations and the king riding on a donkey



- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:45:24Z"
- glossaryReview: [{"glossary_id": "massa-oracle-latter-prophets", "status": "approve", "citations": ["HALOT s.v. maśśāʾ II", "Weis, A Definition of the Genre Maśśāʾ (diss., 1986)", "Petersen, OTL (1995), on 9:1"], "reasoning": "Approve. The heading maśśāʾ 'oracle/utterance' is the standard lexical analysis, and the colon after the heading follows NRSV/NJPS; it matches isaiah-woh."}, {"glossary_id": "lexical-cruxes-zechariah-4-5-9", "status": "approve", "citations": ["Meyers and Meyers, AB 25B/25C", "Petersen, OTL (1984; 1995)"], "reasoning": "Approve: the MT is kept wherever construable, the ASV renderings are retained, and the alternatives are reported at every site."}, {"glossary_id": "mt-qere-textual-policy-latter-prophets", "status": "approve", "citations": ["Tov, Textual Criticism of the Hebrew Bible (3rd ed., 2012)", "BHS/WLC Ketiv-Qere at the three sites"], "reasoning": "Verified against the source: the three bracketed Ketiv/Qere pairs are Jer 10:13 (article), Jer 10:17 (archaic -tî) and Zech 4:2 (wyʾmr/wāʾōmar, sense-changing), and the Qere is translated at each. The versional readings listed are reported and not adopted, and the rafe at Zech 5:11 is handled correctly. direct is right for a textual policy consistent with the corpus."}, {"glossary_id": "house-conventions-latter-prophets", "status": "approve", "citations": ["ASV/NRSV/NJPS (quotation marks editorial in all)", "isaiah-woh _translation-glossary.json v1.6.0"], "reasoning": "direct is right for a presentation convention with
- lens-leakage-flags: []
- lensLeakageCheck: "Checked all 17 lines in the English alone. No English line reads as interpretation. The canon-cited verses (9:9 (with 9:10)) render the Hebrew at standard values, and each reception note is under its own 'Wheel of Heaven reading (reception note, not a translation claim)' heading. Each note's quotation was verified against the canon text (TBWTT ch. 3 and ch. 5, FR/EN). Capitalisation (e.g. 'the Fish Gate') and vocabulary updates ('scroll', 'lampstand') are register or name conventions with lexical basis, not lens."
- escalationReportAdjustments: "Initial verdicts on all 109 LP1 lines, 31 overlay entries and 27 central ops were formed from the chapters, the sources, the drafts, the overlays and the diff, and recorded before wave-lp1-editor-report.md was opened. After reading it, no verdict changed. The report's watch points were each re-tested: Zeph 1:18 'earth', Zeph 1:10-11 names, Zech 4:14, Zech 9:9, Jer 10:5 and the unquoted Jer 10:2-5. The report does not mention the two Zech 4 speech-line issues (4:10 quote boundary; 4:13 'answered'), which stand as revise. The founder points F1-F5 are answered below."
- founderDecisionRecommendations: {"F1-isaiah-aligned-conventions": "Ratify for the Latter Prophets: 'God', 'earth'/'land' by scope, lowercase 'spirit', 'create' and 'oracle' are each the ASV/NRSV/NJPS-backed rendering and keep the five books one volume with Isaiah. Harmonize Ezekiel at its next wave, not by retro-editing signed-off chapters. The 'God'/'Elohim' split is the one item the reviewer flags for explicit founder ratification, because it is a project-stance choice.", "F2-officials-shofar-vs-isaiah": "Align Isaiah to 'officials' (Isa 32:1; 40:23; 43:28) and 'shofar' (Isa 27:13) at its next pass; both are lexically better grounded and already corpus rulings. Then promote megillah/menorah/sarim/shofar to central entries as the report proposes. Keep the Exodus 25 'lampstand' dependency on the Exodus checklist.", "F3-neum-declares": "Adopt 'declares YHWH' corpus-wide. Zechariah has ʾāmar YHWH (4:6) and nəʾum YHWH (5:4) within a few verses, and Isaiah's 'says' for both (e.g. ISA-14:22, checked) erases a distinction the Hebrew makes. Align Isaiah later.", "F4-unquoted-messenger-formula": "Ratify. At Jer 10:2-6 the Hebrew does not mark where the oracle ends, and leaving it unquoted avoids inventing a boundary. Related: at Zech 4:9-10 the wave's own marks run YHWH's word into the messenger's answer, which is the reviewer's revise at ZEC-WOH-4:10.", "F5-sons-of-fresh-oil": "Ship 'the two sons of fresh oil'. It is the most literal rendering, lexically grounded (yiṣhār, no māšaḥ), and inferred is the honest labe
- summary: "17 verdicts: 17 approve. Glossary/op reviews: 15 (14 approve, flag-for-human elohim-god-latter-prophets). Non-blocking commentary fixes at ZEC-WOH-9:10. Status -> awaiting-human."
