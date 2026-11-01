# Canon-cited program — wisdom — human sign-off package

| Chapter | Verses | Approve | Revise | Flag |
|---|---|---|---|---|
| Wisdom of Solomon 13 — The craftsman known from his works, and the carved idol | 19 | 17 | 2 | 0 |

See the combined summary `canon-cited-final-signoff-summary.md` for decisions and fixes.

---

## Editor report (inlined)

# Wisdom of Solomon 13 — Editor Report (wave WIS1)

Book: `wisdom-of-solomon-woh` (new; the corpus's first Septuagint-only text).
Chapter 13, 19 verses. Source: Swete 1896 (Codex Vaticanus), First1KGreek transcription.
Editor: claude-opus-5-5 (editor), 2026-11-01.
Chapter advanced to `editor-review`, version `1.0.0-rc1`; `glossaryVersion` 2.83.0 (central, unchanged pending the diff), `overlayGlossaryVersion` 1.0.0.

Note on the brief: it asked to set "glossaryVersion and overlayGlossaryVersion '1.0.0'".
`glossaryVersion` records the central glossary the chapter was edited against, so it stays `2.83.0`, as in every other book.
`overlayGlossaryVersion` is `1.0.0`.
If the brief really meant the central field, change it at sign-off.

## Speculative entries requiring sign-off

None.
All 15 overlay entries and both central ops are `claim_type: direct`.
No English line contains lens vocabulary.
A script checked the 19 lines for Elohim, Yahweh, YHWH, creators, eternal, planet, craft, council, president, science, extraterrestrial and alien, and found no hits.
The canon readings the Translator had put in the question texts now appear only in the two labelled reception notes, at 13:1 and 13:5.

---

## Unresolved editorial questions

None of these blocks rc1.
Each needs a check against a printed source that the editor could not see.

### `WIS-WOH-13:13` (variant ἀνέσεως / συνέσεως)

**Issue:** Swete prints ἐμπειρίᾳ ἀνέσεως ('the skill of his leisure'). The KJV's 'the skill of his understanding' presupposes συνέσεως.
**Options considered:** (A) follow Swete and note the variant without witnesses; (B) follow the KJV reading; (C) name the witnesses.
**Resolution taken:** A. The commentary says only that συνέσεως is "a reading found in part of the Greek tradition". It does not name any manuscript.
**Why escalating:** Swete's apparatus was stripped from the transcription. The Translator's guess was "Alexandrinus and/or Sinaiticus", and the editor could not verify it. The Reviewer, or anyone with Swete's printed page or Ziegler's Göttingen apparatus, should add the sigla if wanted.

### `WIS-WOH-13:10` (full stop → comma)

**Issue:** The source now reads a comma, as the brief reports. The English reads 'the work of an ancient hand' as standing in apposition to the stone.
**Why escalating:** Only to confirm against the Swete page image that the stop was transcription residue and not Swete's punctuation. Either way the English stays the same.

### `WIS-WOH-13:1`, `13:10` (section capitals)

**Issue:** Swete capitalizes Μάταιοι (13:1) and Ταλαίπωροι (13:10) to mark sections. The paragraph schema has no section or paragraph-break field.
**Resolution taken:** The capitals stay in the Greek, and the commentary at 13:1 and 13:10 names the break.
**Why escalating:** Adding a section field is a schema and tooling decision for the orchestrator, not a translation decision.

---

## Editorial questions: resolution map (37 → 0)

| # | refId | Question | Resolution | Governing entry |
|---|---|---|---|---|
| 0 | 13:1 | Book-level Greek convention | New overlay adopts theos 'God' / theoi 'gods' and generic anthrōpos; adds base-text and scope-rule conventions | `theos-god-rendering-wisdom`, `swete-vaticanus-…`, `greek-transliteration-and-hebrew-scoped-…` |
| 1 | 13:1 | ton onta | 'him who is' (kept; Rev 1:4 rendering); central Ex 3:14 entry extended | `ton-onta-him-who-is-wis-13-1`; central `ehyeh-asher-ehyeh-…` |
| 2 | 13:1 | technitēs | 'the craftsman' (kept); 'workmaster' only in the reception note | `technites-craftsman-wis-13-1` |
| 3 | 13:1/10/13 | anthrōpoi | 'all people' (**changed**), 'human hands' (kept), 'a human being' (**changed**) | `anthropos-generic-people-convention-wisdom` |
| 4 | 13:1 | mataioi | 'vain' (kept) | `knowing-god-vocabulary-wis-13-1-9` |
| 5 | 13:1 | hois parēn agnōsia | 'in whom there was ignorance of God' (kept) | `knowing-god-vocabulary-…` |
| 6 | 13:2 | pneuma | 'wind' (kept) | `elements-and-heavenly-bodies-list-wis-13-2` |
| 7 | 13:2 | prytaneis kosmou | 'rulers of the world' (kept); civic sense in commentary only | `prytaneis-kosmou-rulers-of-the-world-wis-13-2` |
| 8 | 13:2 | kyklon astrōn | 'the circle of the stars' (kept); not 'zodiac' | `elements-and-heavenly-bodies-…` |
| — | 13:2 | phōstēras (not asked) | 'luminaries' (**changed** from 'lights'), under central `meorot` | central `meorot` (extension) |
| 9 | 13:3 | despotēs | 'Lord' (kept) | `despotes-lord-wis-13-3-9` |
| 10 | 13:3 | genesiarchēs | 'the first author' (kept) | `creator-vocabulary-…` |
| 11 | 13:3 | ektisen | 'created' (kept); central `bara` is background only | `creator-vocabulary-…` |
| 12 | 13:4 | dynamei kai energeia | 'power and working' (kept) | commentary 13:4 |
| 13 | 13:4 | ho kataskeuasas | 'he who fashioned them' (**changed** from 'made'), to match 13:11 | `creator-vocabulary-…` |
| 14 | 13:5 | syntax of ek megethous… | 'the greatness and beauty of created things' (kept) | `analogos-theoreitai-by-analogy-wis-13-5` |
| 15 | 13:5 | analogōs | 'by analogy' (kept) | `analogos-theoreitai-…` |
| 16 | 13:5 | genesiourgos | 'their maker' (kept); singular | `creator-vocabulary-…` |
| 17 | 13:5 | theōreitai | 'is seen' (kept) | `analogos-theoreitai-…` |
| 18 | 13:6 | theon / tacha | 'seeking God'; 'perhaps' (kept) | `theos-god-rendering-wisdom`, `knowing-god-…` |
| 19 | 13:7 | diereunōsin etc. | 'search them out … trust their sight' (kept) | `knowing-god-…` |
| 20 | 13:8 | syngnōstoi | 'to be pardoned' (kept); spelling kept | `knowing-god-…`, `swete-vaticanus-…` |
| 21 | 13:9 | stochasasthai ton aiōna | 'form conjectures about the world' (**changed** from 'aim at the world') | `stochasasthai-ton-aiona-wis-13-9` |
| 22 | 13:9 | ton toutōn despotēn | 'the Lord of these things' (kept) | `despotes-lord-wis-13-3-9` |
| 23 | 13:10 | full stop | Source already corrected to a comma; apposition (kept). See escalation | `swete-vaticanus-…` |
| 24 | 13:10 | technēs emmeletēma | 'a thing worked out with art'; 'likenesses of living creatures' (kept) | `idol-polemic-vocabulary-wis-13-10-19` |
| 25 | 13:10 | en nekrois | 'their hopes are in dead things' (**changed** from 'among dead things are their hopes') | `idol-polemic-…` |
| 26 | 13:11 | idol-making vocabulary | kept, except 'handsomely fashioned' (**changed** from 'fashioned in seemly fashion'); central `pesel` is background only | `idol-polemic-…`, `creator-vocabulary-…` |
| 27 | 13:12 | apoblēmata | 'leftovers' (kept) | `idol-polemic-…` |
| 28 | 13:13 | ἀνέσεως / συνέσεως | Swete followed; variant noted without witnesses. See escalation | `swete-vaticanus-…` |
| 29 | 13:13 | epimeleia argias; eikoni anthrōpou | 'care of his idleness' (kept); 'he likened it to the image of a human being' (**changed**) | `idol-polemic-…`, `anthropos-…` |
| 30 | 13:14 | miltos / phykos / chroa | kept | `idol-polemic-…` |
| 31 | 13:15 | oikēma | 'a dwelling' (kept); 'niche' in commentary | `idol-polemic-…` |
| 32 | 13:17 | gamōn | 'his marriage' (kept): the plural of gamos means a single wedding or marriage | `idol-polemic-…` |
| 33 | 13:18 | apeirotaton | 'the most inexperienced thing' (**changed** from 'the most helpless thing') | `idol-polemic-…` |
| 34 | 13:19 | wordplay | 'vigor … without vigor' (kept) | `idol-polemic-…` |
| 35 | 13:1 | OCR corrections | accepted; Vaticanus orthography kept | `swete-vaticanus-…` |
| 36 | 13:10 | section break | noted in commentary. See escalation | `swete-vaticanus-…` |

### English-line changes (8 lines, each governed by a glossary entry)

- 13:1 'all men' → 'all people' (`anthropos-generic-people-convention-wisdom`)
- 13:2 'the lights of heaven' → 'the luminaries of heaven' (central `meorot`, extension proposed)
- 13:4 'he who made them' → 'he who fashioned them' (`creator-vocabulary-…`)
- 13:9 'aim at the world' → 'form conjectures about the world' (`stochasasthai-ton-aiona-wis-13-9`)
- 13:10 'among dead things are their hopes' → 'their hopes are in dead things' (`idol-polemic-…`)
- 13:11 'has fashioned in seemly fashion' → 'has handsomely fashioned' (`idol-polemic-…`, `creator-vocabulary-…`)
- 13:13 'he made it a likeness of the image of a man' → 'he likened it to the image of a human being' (`idol-polemic-…`, `anthropos-…`)
- 13:18 'the most helpless thing' → 'the most inexperienced thing' (`idol-polemic-…`)

All other lines are the Translator's draft, unchanged.
Commentary is in `notes.official` for 17 of the 19 verses.
13:12 and 13:16 have none because their lines do not diverge.

---

## Glossary changes for review

### Central glossary (proposed in `wave-wis1-central-diff.json`; base 2.83.0 → recommend 2.84.0, or the next free minor)

- Modified: `ehyeh-asher-ehyeh-divine-name-revelation-ex-3-14-cross-corpus` (appliesTo only, +WIS-WOH-13:1). This is a reception site of the LXX *ho ōn* stratum, on the same pattern as the Revelation sites. The Greek line reads 'him who is'.
- Modified: `meorot` (appliesTo +WIS-WOH-13:2; strongs extended with Greek φωστήρ G5458). This is the gophrit/theion precedent.
- Considered, not proposed: `apo-ho-on-rev-1-4-…`. Its subject is the Revelation solecism, while Wis 13:1 has the regularly declined accusative, so the entry is background only. Also not proposed: `bara`, `pesel-utemunah-…` and `tzeva-ha-shamayim-…`, which are Hebrew-text decisions and stay background under the scope rule.
- Concurrency: the diff carries complete appliesTo arrays plus `appliesToAdded`. If another 2.83.0-based diff lands first, union-merge and renumber.

### Per-translation overlay (new file, v1.0.0, 15 entries, all `direct`)

- Added: `swete-vaticanus-base-text-and-variant-reporting-convention-wisdom`
- Added: `theos-god-rendering-wisdom` (adopts the revelation-woh convention)
- Added: `greek-transliteration-and-hebrew-scoped-central-entries-convention-wisdom` (adopts the matthew-woh transliteration and the revelation-woh scope rule)
- Added: `anthropos-generic-people-convention-wisdom` (adopts the matthew-woh rule)
- Added: `raelian-canon-citation-reception-note-convention-wisdom`
- Added: `ton-onta-him-who-is-wis-13-1`
- Added: `technites-craftsman-wis-13-1`
- Added: `creator-vocabulary-ktizo-genesiarches-kataskeuazo-genesiourgos-wis-13`
- Added: `despotes-lord-wis-13-3-9`
- Added: `prytaneis-kosmou-rulers-of-the-world-wis-13-2`
- Added: `elements-and-heavenly-bodies-list-wis-13-2`
- Added: `analogos-theoreitai-by-analogy-wis-13-5`
- Added: `stochasasthai-ton-aiona-wis-13-9`
- Added: `knowing-god-vocabulary-wis-13-1-9`
- Added: `idol-polemic-vocabulary-wis-13-10-19`

The four Greek conventions now exist in three overlays: Matthew, Revelation and Wisdom.
That supports the pending recommendation to promote a central Greek convention.

---

## Founder decisions (recommendations)

- **A. theos 'God' in the Septuagint.** Endorse. Wisdom was written in Greek, so no *ʾĕlōhîm* stands behind the word. This is the same rule as the five Greek books already in the corpus.
- **B. technitēs 'craftsman', not the canon's 'workmaster'.** Endorse. 'Workmaster' is the KJV's word for the same noun, not a different reading. 'Craftsman' keeps the chapter's word-play on divine and human craft visible (7:21; 13:10, 11). The canon's word is quoted in the 13:1 reception note.
- **C. anthrōpoi 'people'.** Endorse. This is the Matthew rule; NRSV makes the same choice.
- **D. analogōs 'by analogy'.** Endorse. It is the lexical sense and current English. It agrees with the canon's French « par analogie », though that agreement was not the reason for the choice. The KJV 'proportionably' is recorded.
- **E. despotēs 'Lord'.** Endorse. This is the standard rendering (KJV, NRSV) and the LXX equivalent of *ʾādôn*. The difference from *kyrios* is named in commentary. Rev 6:10 'Sovereign Lord' is a vocative-address practice and does not apply here.
- **F. prytaneis kosmou 'rulers of the world'.** Endorse, and keep the decision closed. The civic sense 'presiding member of the Council' is lexically real but does not fit the context. An institutional rendering ('presidents', 'council') would look like a lens choice in a verse the canon does not cite. The commentary deliberately draws no link to canon terminology.
- **G. 13:13 ἀνέσεως.** Endorse following Swete. Adding manuscript sigla should wait until someone checks the apparatus.
- **H. Plural 'creators' (TBWTT ch. 3).** The canon reads 13:1 and 13:5 as showing that people could "recognize the creators" from what they made. All the Greek agent nouns are singular (*technitēs*, *genesiourgos*, *ho kataskeuasas*, *ho despotēs*). The line keeps them singular, and the reception notes say so explicitly. This needs no decision. It is listed so that the sign-off sees where the reading and the text part company.

Follow-up outside this chapter: TBWTT ch. 3 also quotes Wis 6:22 (TBWTT-3:266). That would be the natural next Wisdom chapter if the program wants complete canon coverage.

## Files

- `wisdom-of-solomon-woh/chapter-13.json` (revised)
- `wisdom-of-solomon-woh/_translation-glossary.json` (new, v1.0.0)
- `wisdom-of-solomon-woh/wave-wis1-central-diff.json` (new)
- `wisdom-of-solomon-woh/wave-wis1-editor-report.md` (this file)

No `_meta.json` created. Nothing committed or pushed. No central glossary file edited.


---

## Reviewer report

### Wisdom of Solomon 13 — The craftsman known from his works, and the carved idol

- **WIS-WOH-13:11** — revise: Rendering approved. Copyedit: 'skilfully' (British) sits in the same chapter as 'vigor' (13:19, American), and psalms-woh lines use 'skillfully'. Change to 'skillfully'. Also optional: the commentary could note that ei de kai tis ... (13:11-12) has no formal apodosis before 13:13, where KJV, Brenton and NRSV drop the 'if' altogether.
- **WIS-WOH-13:13** — revise: The line is approved: ἀνέσεως (Swete; NRSV 'skill gained in idleness'), 'he likened it to the image of a human being'. Revise the commentary. Its premise that 'Swete's apparatus is not reproduced in the transcription' is wrong. The raw XML keeps the apparatus as footnotes, OCR-degraded with ℵ written 'U+05D0'. That apparatus gives συνέσεως as the reading of a corrector of Sinaiticus (ℵc.a), and ἐργασίας for ἀργίας as ℵc.a A. Name that witness and drop 'witnesses not named'. The Translator's guess of Alexandrinus is not supported. Also optional: note that 'then' renders apodotic δέ after the protasis of 13:11.

- reviewer: "claude-opus-5-5 acting as woh-reviewer"
- reviewedAt: "2026-11-01T14:28:55Z"
- glossaryReview: [{"glossary_id": "swete-vaticanus-base-text-and-variant-reporting-convention-wisdom", "status": "revise", "citations": ["Swete 1896, vol. 2, apparatus to Wis 13 (preserved in First1KGreek tlg0527.tlg033 XML footnotes)", "Ziegler, Sapientia Salomonis, Göttingen Septuaginta XII/1 (1962; 2nd ed. 1980)"], "reasoning": "Direct is right for the convention itself: translate Swete's B text, list OCR fixes, and keep B orthography. All 9 listed corrections were verified by diffing the raw XML against source-grc-13.json, with no unlisted change. Revise the rationale, wohChoice and 13:13 note, which say the apparatus is 'lost' or 'stripped'. It survives as OCR footnotes and already confirms the entry's orthography claims (διεραυνῶσιν B*, συνγνωστοί B*). It also supplies the 13:13 siglum (συνέσεως ℵc.a), so the rule becomes: name witnesses where Swete's apparatus gives them, and mark them as read from an OCR transcription."}, {"glossary_id": "theos-god-rendering-wisdom", "status": "approve", "citations": ["BDAG s.v. θεός", "Muraoka (2009) s.v. θεός"], "reasoning": "Direct is correct: Wisdom was composed in Greek, LXX theos renders ʾĕlōhîm/ʾēl and kyrios the Tetragrammaton, and the rule matches all Greek books in the corpus."}, {"glossary_id": "greek-transliteration-and-hebrew-scoped-central-entries-convention-wisdom", "status": "approve", "citations": ["LSJ, BDAG s.v. φωστήρ", "LXX Gen 1:14, 16"], "reasoning": "Direct. The entry states the explicit lexical criterion the Revelation reviewe
- lens-leakage-flags: []
- lensLeakageCheck: "All 19 English lines were re-read against the Greek. No line contains Elohim, Yahweh, creators, council, president, craft, planet or any other lens vocabulary. At the two canon-cited sites the Greek agent nouns are singular (13:1 ton onta, ton technitēn; 13:5 ho genesiourgos autōn), and the lines keep them singular ('him who is', 'the craftsman', 'their maker'). The canon's plural 'creators' (TBWTT-3:269) appears only in the two paragraphs headed 'reception note, not a translation claim'. 13:2 prytaneis kosmou is 'rulers of the world', the poetic/general sense shared by KJV and NRSV, not the civic 'presidents'/'council'. No ambiguity is resolved in the canon's direction. Where line and canon agree (13:5 'par analogie'), the agreement is lexical (LSJ), and the KJV words the canon's English quotes ('workmaster', 'proportionably') are recorded as older renderings of the same Greek. 'luminaries' at 13:2 follows NRSV and LXX Gen 1, not the lens."
- sourceVerification: "source-grc-13.json was diffed against the raw First1KGreek XML (scratchpad wis/wis.xml). Every difference is one of the 9 listed corrections (8 OCR fixes plus the 13:10 comma), and nothing else was changed. The OCR fixes are certain (ὁραωμένων, μέν γὰρ, ἀλλ ἢ, δυνα-τώτερος, ἴνα, ἀνθρώπωον, μέν οὗν, and the apparatus block run into 13:10). The 13:10 comma is plausible but was not checked against Swete's page image (vol. 2 p. 628). The XML keeps Swete's apparatus as OCR footnotes. It confirms the B* orthographies the overlay keeps and gives ℵc.a for συνέσεως at 13:13. The source file's note that the apparatus is 'not reproduced' is accurate for the source JSON, but the overlay's statement that it was 'lost' in the transcription is not."
- escalationReportAdjustments: "Initial verdicts on 19 verses, 15 overlay entries and 2 central ops were formed from the chapter, the overlay, the diff, the 2.83.0 base, the source and the raw XML before wave-wis1-editor-report.md was opened. After reading it, no verdict changed. The report's escalation on 13:13 ('Swete's apparatus was stripped from the transcription ... the Reviewer ... should add the sigla') is answered by the 13:13 and Swete-convention revises: the apparatus gives συνέσεως ℵc.a, not A. The Translator's 'Alexandrinus' guess is not supported. The 13:10 page-image check remains open and is non-blocking. The section-field question (13:1, 13:10) is a schema matter for the orchestrator, and the commentary handles it adequately. The report's '8 changed lines' were confirmed and each is endorsed. No _meta.json exists for the new book, so the orchestrator should create it before publication."
- founderDecisionRecommendations: {"A-theos-God-in-the-Septuagint": "Endorse. No ʾĕlōhîm stands behind a Greek-composed text; same rule as Matthew/Revelation.", "B-technites-craftsman-not-workmaster": "Endorse. 'Workmaster' is the KJV's word for the same noun; 'craftsman' (or NRSV 'artisan') is current English and keeps the 7:21/13:10-11 word-family.", "C-anthropoi-people": "Endorse; Matthew rule, NRSV practice.", "D-analogos-by-analogy": "Endorse; LSJ sense, Winston's 'correspondingly' is the same reading.", "E-despotes-Lord": "Endorse; KJV/NRSV; kyrios distinction named in commentary.", "F-prytaneis-kosmou-rulers-of-the-world": "Endorse and keep closed. The predicate reading follows KJV/Brenton/NRSV, and 'presidents/council' would be a lens-shaped lexical choice the context does not support.", "G-13:13-aneseos": "Endorse following Swete (ἀνέσεως is also the reading behind NRSV). Modify the 'wait for sigla' part: Swete's apparatus, which survives in the transcription's footnotes, gives συνέσεως as ℵc.a (a corrector of Sinaiticus), so the siglum can be added now.", "H-plural-creators": "Agree that no decision is needed. Every Greek agent is singular, the lines keep the singular, and the reception notes state the divergence accurately against TBWTT-3:268-270."}
- summary: "19 verdicts: 17 approve, 2 revise (13:11 spelling copyedit 'skilfully' → 'skillfully'; 13:13 commentary should name the ℵc.a siglum for συνέσεως, now verifiable from the apparatus in the transcription). 17 glossary/op reviews: 16 approve, 1 revise (Swete convention: the apparatus is not lost). 0 speculative entries. 0 lens-leakage flags. The English lines need only the one-word copyedit; the other revisions are to apparatus text. Status: awaiting-human."
