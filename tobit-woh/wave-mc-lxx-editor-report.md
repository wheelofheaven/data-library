# Wave MC (Septuagint part) — Editor Report

Chapters: `wisdom-of-solomon-woh` chapter 6 (25 verses, extends the published volume) and `tobit-woh` chapter 12 (22 verses, new book, code TOB-WOH).
Editor: claude-opus-5-5 (editor), 2026-11-02.
Both chapters are now `editor-review`, version `1.0.0-rc1`, `glossaryVersion` `2.90.0`.
`overlayGlossaryVersion` is `1.1.0` for Wis 6 and `1.0.0` for Tob 12.
Editorial questions resolved: Wis 6, 25 → 0; Tob 12, 17 → 0.

## Summary

- Wis 6: 13 English-line changes in 12 verses, 22 verses with commentary, one labelled reception note (6:22).
- Tob 12: 7 English-line changes in 6 verses, 19 verses with commentary, labelled reception notes at 12:19 and 12:20.
- New overlay `tobit-woh/_translation-glossary.json` v1.0.0 (8 entries, all `direct`).
- `wisdom-of-solomon-woh/_translation-glossary.json` 1.0.0 → 1.1.0 (5 new entries, 6 existing entries extended to Wis 6 sites; no earlier decision changed).
- Central proposals in `tobit-woh/wave-mc-lxx-central-diff.json`, 2.90.0 → 2.92.0: two appliesTo extensions plus one citation fix. No new central entry.

## Speculative entries requiring sign-off

None.
All 13 new overlay entries and both central ops are `claim_type: direct`.
A script checked all 47 English lines for Elohim, YHWH, Yahweh, creator, robot, eternal, planet, science, extraterrestrial, alien and Sagesse, and found no hits.
The canon's readings ('robots of the creators', 'Sagesse' as 'science', « éprouver ») appear only in the three labelled reception notes.

---

## Founder decisions needing sign-off

### 1. Tobit base recension: GI (Swete's B text)

**Decision taken:** translate GI, Swete's main text (Vaticanus, with Alexandrinus in the apparatus).
Report GII (Sinaiticus) readings that change the sense in commentary, marked as read from scan OCR.
Recorded in `swete-vaticanus-gi-base-recension-and-variant-reporting-convention-tobit`, whose wohChoice is flagged "FOUNDER DECISION … pending explicit sign-off".
**For GI:** the canon quotes GI word for word at TBWTT-3:264.
'Tous les jours' = πάσας τὰς ἡμέρας, 'je me rendais visible' = ὠπτανόμην, and 'dans un livre' = εἰς βιβλίον; GII has none of the three.
The canon's English edition quotes the KJV, which also translates the GI type.
GI is the only recension in a clean CC BY-SA transcription.
It keeps one base-text rule (Swete's Vaticanus) for the Septuagint books.
The central entries that already quote Tobit quote it in the GI wording.
**Against:** most scholars judge GII older and closer to Qumran (Fitzmyer, CEJL 2003; Moore, AB 40A 1996), and NRSV, NAB and NJB translate it.
The canon's paraphrase at TBWTT-3:263 ('vient aussi éprouver') is closest to the GII clause at 12:13-14, 'then I was sent to you to test you'.
That clause is reported at 12:13 and in the 12:19 reception note.
**Recommendation:** ship GI. If a GII track is ever wanted, it needs a fresh transcription of Swete's ℵ text from the page images, and it should be a parallel track, not a replacement.

### 2. Wis 6:12: clause missing in Vaticanus

**Decision taken:** under the ratified Swete convention, the line translates B* and ends at 'by those who love her'.
The clause καὶ εὑρίσκεται ὑπὸ τῶν ζητούντων αὐτήν 'and she is found by those who seek her' is reported in commentary.
Its witnesses, read from the OCR apparatus, are a B corrector's margin, ℵ and A; Rahlfs prints it, and the KJV, Brenton and NRSV translate it.
The note also explains the omission as a likely skip between the two endings in αὐτήν.
The Swete convention's wohChoice now states this rule in general form: report the longer text in commentary, no brackets in the line.
**Why the founder should see it:** this is the first place where the convention makes the English visibly shorter than every standard English Bible.
The alternative is to supply the clause in the line, marked as an addition.
That would need an exception to the ratified convention.
**Recommendation:** keep the convention as it stands (omit and report).

### 3. Ratified-convention extension: kyrios 'the Lord' as an overlay entry

The founder's ratified rule is now written as `kyrios-the-lord-rendering-wisdom` (Wis) and `divine-designations-theos-kyrios-ho-hagios-tobit` (Tob).
The ratified rule is applied as it stands.
It is listed here only because these are the first overlay entries that record it.

---

## Unresolved editorial questions

None of these blocks rc1.

### `WIS-WOH-6:8`, `TOB-WOH-12:*`: OCR-read apparatus and GII

Every A, B-corrector and ℵ attribution, and every GII reading, was read from OCR (the First1KGreek footnotes and the archive.org djvu layer), and each note says so.
The Reviewer, or anyone with Swete's printed pages (vol. 2; Tobit 12 at pp. 840-842) or the Göttingen editions (Ziegler 1962/1980; Hanhart 1983), should spot-check these:
- Wis 6:12: the witnesses for the added clause.
- Tob 12:13-14: the GII 'to test you' clause (the OCR is partly garbled at καὶ ἅμα).
- Tob 12:18: A + ἦλθον.
- Wis 6:8: the apparatus entry on ἐφίσταται is illegible, so nothing is reported.

### `WIS-WOH-6:12` (section capital)

Swete's section capital at Λαμπρά is noted in commentary, as at Wis 13:1 and 13:10.
The schema still has no section field.

---

## English-line changes

### Wisdom 6

| refId | Draft | Now | Governing entry |
|---|---|---|---|
| 6:3 | the Highest | the Most High | `hypsistos-the-most-high-wisdom` (corpus rendering in 1 Enoch, Daniel) |
| 6:6 | mightily tormented | mightily examined | `royal-address-and-judgment-vocabulary-wis-6-1-21` |
| 6:8 | a severe trial | a strict inquiry | same |
| 6:9 | O kings (τύραννοι) | O monarchs | same |
| 6:21 | O kings of peoples | O monarchs of peoples | same |
| 6:12 | Glorious | Radiant | `wisdom-and-sorites-vocabulary-wis-6-11-25` |
| 6:15 | perfection of wisdom (φρόνησις) | the perfection of prudence | same |
| 6:17 | desire of discipline | desire for instruction | same |
| 6:18 | care for discipline | care for instruction | same |
| 6:24 | a wise king … the upholding | a prudent king … the stability | same + `what-wisdom-is-vocabulary-wis-6-22-24` |
| 6:22 | how she came up; her nativity | how she came to be; her origin | `what-wisdom-is-vocabulary-wis-6-22-24` |
| 6:23 | for such a man will have | for it will have (οὗτος = φθόνος) | same |

Kept as drafted, with commentary: 'the Lord' (6:3), 'ministers' (6:4), 'the law' (6:4), 'he' (6:5), 'judged holy' (6:10), 'sitting at his gates' (6:14), 'incorruption' (6:18-19), 'makes one be near to God' (6:19), 'a kingdom' (6:20), 'mysteries' and 'into the light' (6:22), 'welfare' (6:24), lower-case 'wisdom'.

### Tobit 12

| refId | Draft | Now | Governing entry |
|---|---|---|---|
| 12:1 | My son (τέκνον) | My child | `household-and-burial-vocabulary-tob-12-1-13` |
| 12:6 | praise him (×3) | give thanks to him | `thanksgiving-and-almsgiving-vocabulary-tob-12-6-11` |
| 12:22 | confessed | acknowledged | same |
| 12:12 | remembrance | memorial | `raphael-self-disclosure-vocabulary-tob-12-12-22` |
| 12:13 | cover the dead | lay out the dead | `household-and-burial-vocabulary-tob-12-1-13` |
| 12:20 | that have been done | that have been accomplished | `raphael-self-disclosure-vocabulary-tob-12-12-22` |

The 12:20 change follows LSJ and Muraoka (συντελέω 'bring to completion').
It also agrees with the canon's French « accompli ».
The commentary gives the lexical basis first and records the agreement only in the reception note.

Kept as drafted, with commentary:
- 'he' (12:5) and 'the words of the works of God' (12:6).
- 'the secret of a king' (12:7) and 'alms' (12:8-9).
- 'the saints' (12:15), kept to match Rev 5:8 and 8:3-4.
- 'go in before' (12:15) and 'it will go well with you' (12:17).
- The B text 'your God' with only the copula supplied (12:18).
- 'I appeared to you' and 'a vision' (12:19), 'I am going up' (12:20), and 'an angel of the Lord' (12:22).

---

## Editorial questions: resolution map

### Wisdom 6 (25 → 0)

- Versification: primary numbers only; the alternative numbering and Swete's 6:12 capital are noted at 6:1, 6:12 and 6:22.
- Apparatus digest: minor variants are not reported verse by verse. Variants that change the sense are reported at 6:12, 6:14 and 6:20. Others appear where a note already exists, marked as OCR-read.
- kyrios: 'the Lord', recorded in the new `kyrios-the-lord-rendering-wisdom`.
- Hypsistos: 'the Most High', in the new entry. `el-elyon` is background only.
- nomos: 'the law' / 'her laws'. hypēretai: 'ministers'. Subject of 6:5: 'he'.
- etazō: 'examined'. syngnōstos: kept. ereuna: 'a strict inquiry'. tyrannoi: 'monarchs'. hosiōthēsontai: kept.
- 6:12 clause: omitted per the convention (founder decision 2). sophia: lower case. lampra: 'radiant'.
- paredros: kept. phronēsis / phronimos: 'prudence' / 'prudent'. paideia: 'instruction' throughout. aphtharsia: kept.
- 6:19/20 segmentation: accepted. Supplied object: 'one' kept. basileia: kept.
- 6:22 (three questions): reception note; 'came to be'; 'her origin'; 'mysteries' kept.
- houtos: 'it'. sōtēria / eustathia: 'welfare' / 'stability'.
- Overlay housekeeping: five entries extended, and the despotēs id kept unchanged because ids are stable.

### Tobit 12 (17 → 0)

- Recension: GI (founder decision 1).
- Conventions: new overlay.
- teknon: 'My child'.
- Apparatus: reported where it matters.
- 12:5 subject: 'he'.
- exomologeomai: 'give thanks' / 'acknowledge'.
- logoi: kept.
- mystērion: 'secret'.
- eleēmosynē: 'alms'.
- mnēmosynon: 'memorial'.
- peristellō: 'lay out'.
- 12:15: 'the saints' kept; central seven-archangels entry extended.
- 12:17: kept.
- 12:18: B text.
- 12:19: kept; central divine-eating entry extended; reception note.
- 12:20: 'accomplished'; reception note.
- 12:22: 'an angel of the Lord' (`malakh-yhwh-messenger` not applied).

---

## Glossary changes for review

### Central glossary (`tobit-woh/wave-mc-lxx-central-diff.json`, 2.90.0 → 2.92.0)

- Modified: `seven-archangels-list-1-enoch-20-tob-12-rev-8-cross-corpus`.
  - appliesTo gains `TOB-WOH-12:15`.
  - In the rationale, "per Fitzmyer 2003 AB 40A" is corrected: AB 40A is Moore's *Tobit* (1996), and Fitzmyer's *Tobit* is CEJL (2003).
  - wohChoice is unchanged.
- Modified: `divine-eating-anthropomorphism`. appliesTo gains `TOB-WOH-12:19`, the verse its rationale already quotes. wohChoice is unchanged.
- Numbering: 2.92.0 as briefed. The concurrent NT diff (`revelation-woh/wave-mc-nt-central-diff.json`) is 2.90.0 → 2.91.0 and touches different ids, so there is no conflict.

### Per-translation overlays

`wisdom-of-solomon-woh` 1.0.0 → 1.1.0:
- Added (all `direct`):
  - `kyrios-the-lord-rendering-wisdom`
  - `hypsistos-the-most-high-wisdom`
  - `royal-address-and-judgment-vocabulary-wis-6-1-21`
  - `wisdom-and-sorites-vocabulary-wis-6-11-25`
  - `what-wisdom-is-vocabulary-wis-6-22-24`
- Extended (appliesTo, plus site lists in the wohChoice text; no decision changed):
  - `swete-vaticanus-base-text-and-variant-reporting-convention-wisdom`. It now states the omission-reporting rule for 6:12 and the source-grc-6 corrections.
  - `theos-god-rendering-wisdom`
  - `despotes-lord-wis-13-3-9`
  - `greek-transliteration-and-hebrew-scoped-central-entries-convention-wisdom`
  - `raelian-canon-citation-reception-note-convention-wisdom`
- The bump is minor, as briefed.
  - The Swete entry's wohChoice gains a sentence that spells out an existing rule for a new case.
  - The founder may treat this as a modification, which would make it a major bump. The editor recommends minor.

`tobit-woh` 1.0.0 (new; all `direct`):
- `swete-vaticanus-gi-base-recension-and-variant-reporting-convention-tobit` (founder decision)
- `divine-designations-theos-kyrios-ho-hagios-tobit`
- `angelos-angel-rendering-tobit`
- `greek-transliteration-english-names-and-hebrew-scoped-central-entries-convention-tobit`
- `raelian-canon-citation-reception-note-convention-tobit`
- `thanksgiving-and-almsgiving-vocabulary-tob-12-6-11`
- `raphael-self-disclosure-vocabulary-tob-12-12-22`
- `household-and-burial-vocabulary-tob-12-1-13`

## Not touched

- No `_meta.json` exists for tobit-woh, and none was created; the catalog entry is for the orchestrator.
- No catalog edits, no git operations.
- The central glossary file was not edited.
