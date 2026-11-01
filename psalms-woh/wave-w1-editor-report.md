# Writings Wave W1 Editor Report: Job 37; Psalms 8, 19, 33, 139, 147; Proverbs 8, 10; Ecclesiastes 3

**Program:** canon-cited biblical chapters (every biblical chapter cited in Raël's first three books, whole chapters), Writings wave.
**Books / chapters:** `job-woh` 37 (24 verses); `psalms-woh` 8 (10), 19 (15), 33 (22), 139 (24), 147 (20); `proverbs-woh` 8 (36), 10 (32); `ecclesiastes-woh` 3 (22). Total: 205 verses. psalms-woh, proverbs-woh and ecclesiastes-woh are new books.
**Editor pass:** 2026-11-01 (claude-opus-5-5, woh-editor role).
**Status at end of pass:** all nine chapters `draft` → `editor-review`; version `0.1.0` → `1.0.0-rc1`; `glossaryVersion` 2.84.0 (the recommended target of this wave's central diff; re-pin if it lands under another number, see below); `overlayGlossaryVersion` 1.0.0; `claude-opus-5-5 (editor)` added to `modelDrafts`; `reviewer` left `pending`.
**Editorial questions:** 74 received, 74 resolved, every array cleared. None is escalated as unresolvable. Six resolutions are flagged as founder points (section 3).

## Files written (only these)

- Chapters: `job-woh/chapter-37.json`, `psalms-woh/chapter-{8,19,33,139,147}.json`, `proverbs-woh/chapter-{8,10}.json`, `ecclesiastes-woh/chapter-3.json`
- New overlays v1.0.0: `job-woh/_translation-glossary.json`, `psalms-woh/_translation-glossary.json`, `proverbs-woh/_translation-glossary.json`, `ecclesiastes-woh/_translation-glossary.json`
- `psalms-woh/wave-w1-central-diff.json` (proposed, not applied; base 2.83.0)
- this report

No central glossary file, `_meta.json` or file outside the four book directories was written.

## Counts

- Commentary (`notes.official`): 169 of 205 paragraphs (Job 37: 24/24; Ps 8: 10/10; Ps 19: 13/15; Ps 33: 16/22; Ps 139: 21/24; Ps 147: 17/20; Prov 8: 31/36; Prov 10: 20/32; Eccl 3: 17/22). The uncommented verses are plain lines with no divergence from the ASV and no lexical decision (for example Prov 10:2, 5, 9; Eccl 3:3-4, 6-8).
- Reception notes, separately headed "**Wheel of Heaven reading (reception note, not a translation claim).**", each checked against `writings-canon-citations.md`:
  - Ps 8:6 (TBWTT-3:239-240)
  - Ps 19:5 (3:243-245) and 19:7 (3:241-242)
  - Ps 33:13, covering vv 13-14 (3:246-247)
  - Ps 139:4, covering vv 4-6 (3:295-297)
  - Ps 147:4, covering vv 4-5 (3:298-299), and 147:15 (3:300-301)
  - Job 37:18 (3:257-260)
  - Prov 8:22, covering vv 22-23, 27, 29-31 (3:277-279), with short notes at 8:30 ('comme architecte') and pointers at 8:23, 27, 29, 31
  - Prov 10:13 (TBWTT-5:35)
  - Eccl 3:15 (3:280-281) and 3:19 (3:282-283)
  - Job 1-2 (LWTE ch. 2) are outside this wave.
- Ketiv/Qere: 6 bracketed pairs in the Leningrad text (Job 37:12; Ps 139:6, 16; 147:19; Prov 8:17, 35), all Qere translated, all Ketiv recorded. The brief counted seven; the seventh item is probably Prov 8:16, which is a manuscript variant, not a Ketiv/Qere pair.
- Overlay entries: 10 shared Writings conventions (identical text and appliesTo in all four overlays) plus 7 book-specific entries (Psalms 3, Proverbs 2, Ecclesiastes 2). Inferred: 2 (`ruach-wind-breath-spirit-writings`, `amon-master-workman-proverbs-8-30`); all others are direct.
- Central diff: 1 new entry (direct), 3 modifications (scope appended or a quotation corrected; no decision reversed), 12 appliesTo-only extensions.

## 1. English lines changed (18 verses, plus one chapter title)

Every change follows a glossary entry (rule 7). All other lines are the Translator's draft, unchanged.

| Verse(s) | Draft | Now | Governing entry |
|---|---|---|---|
| Ps 33:5, 18, 22; 147:11; Job 37:13 | lovingkindness | kindness | central `chesed-solitary-covenant-kindness` (extended) |
| Job 37:18, 21; Prov 8:28 | skies | clouds | new central `shechaqim-clouds-cross-corpus` |
| Ps 33:13; Eccl 3:10, 18, 19, 21 | the sons of men | the sons of the human | central `ha-adam` (extended; genesis-woh 11:5 precedent) + overlay `adam-enosh-ish-human-terms-writings` |
| Prov 8:4, 31 | the sons of men | the sons of human | central `ben-adam` (extended) + same overlay entry |
| Ps 33:19 | their soul | their life | overlay `nefesh-scope-writings` |
| Prov 8:36 | his own soul | his own life | overlay `nefesh-scope-writings` |
| Ps 139:13 | you covered me | you knit me together | overlay `sakhak-knit-together-psalm-139-13` |
| Eccl 3:21 | the spirit ... the spirit | the breath ... the breath | overlay `ruach-wind-breath-spirit-writings` (inferred) |
| Ps 33 title | ... on all the sons of men | ... on all the sons of the human | as Ps 33:13 |

No line carries the lens. The three places where a line now coincides with the canon's wording are noted in the apparatus as coincidences of the lexical ruling, not as its ground:
- Job 37:18 'clouds' (canon « nuages solides »)
- Prov 8:22 'created' (canon « m'a créée »)
- Prov 8:30 'master workman' (canon « comme architecte »)

## 2. Rulings requested in the brief

1. **Ps 8:6 *mĕʿaṭ mēʾĕlōhîm*: kept as 'a little less than Elohim'.** The Hebrew is anarthrous. The corpus rule follows the Hebrew article: central `elohim-as-translation`; overlay `divine-names-convention-writings`, parallel to the Kings clause 2 and job-woh 1:9. The commentary sets out the ASV/NRSV 'God', the LXX/Heb 2:7 'angels' and NJPS 'divine'. The reception note gives the canon's 'the Elohim' and its claim about copyists, and says that no witness reads 'equal'. Founder point A.
2. **Prov 8:22 *qānānî*: 'created' kept; central reconciled.** `koneh-shamayim-va-aretz` gains a verbal clause, the translation refIds, and a rationale paragraph that names Prov 8:22 as its most contested site (Vawter 1980 for 'acquire'; LXX, Targum, Peshitta, NRSV and NJPS 'created'; the birth verbs of vv 24-25). The `reshit-darkhei-el` rationale no longer quotes 'YHWH possessed me'. *rēʾšît darkô* is adverbial, 'at the beginning of his way'; the appositional Job 40:19 construal is recorded.
3. **šĕḥāqîm against šāmayim: 'clouds'.** This follows the stable job-woh 38:37 ('Who can count the clouds ... the bottles of the skies'), BDB/HALOT and the KJV at Prov 8:28. A new central entry is proposed because the lemma recurs across books. ʿāb 'thick cloud' and ʿānān 'cloud' stay distinct in Job 37:11, 15, 16. Founder point F asks for transparency, not a decision.
4. **raqia at Ps 19:2: extended ('dome'). ben-adam at Ps 8:5: extended ('a son of human').** The ben-adam rationale already cites Ps 8:5. The plural bĕnê (hā)ʾādām follows (founder point B).
5. **MT readings.**
   - Prov 8:16 (ṣedeq) and Eccl 3:21 (articular participles) are kept, and the versional readings are recorded. Eccl 3:21 goes against the LXX, Vulgate, ASV, NRSV and NJPS; flagged for the Reviewer.
   - Ps 8:2 keeps the ASV/NRSV construal 'you who have set'. This departs from the MT vowels only: the imperative *tĕnâ* does not construe after *ʾăšer*. The consonants are unchanged, and the departure is recorded as the single exception in `mt-baseline-versification-and-psalm-numbering-writings`.
   - Ps 19:5 « tente sur la mer » (emended *bayyām*) and Job 37:18 « nuages solides » are in reception notes only. The lines render MT *bāhem* 'in them' and lexical 'clouds' with 'strong' (ASV), not 'solid'.
6. **ASV stray headings: see follow-up 1.**

Other notable resolutions (all recorded in commentary and, where lexical, in the glossary):
- *šāmayim* by register: 'heavens' only at Ps 33:13 (YHWH's dwelling) and 139:8 (against She'ol); 'skies' elsewhere.
- ʾereṣ: 'earth' in cosmic and hymnic scope (the isaiah-woh ruling adopted); 'land' at Job 37:3 ('the wings of the land', the job-woh 38:13 precedent), 37:13 and Prov 10:30.
- Divine names: El, Eloah and Shaddai transliterated in Psalms as in Job (central `shaddai-eloah` extended); 'Praise Yah!'; 'our Lord' for ʾădōnênû.
- English proper names (David, Solomon, Jerusalem, Israel, Jacob, Zion, Job), as job-woh and ezekiel-woh.
- Lower-case 'wisdom' and lower-case 'spirit' (Ps 139:7).
- ʾašrê stays 'Blessed' (ASV), with 'Happy' (NJPS) recorded.
- Psalm 19 Torah terms as in the ASV, one word per term.
- Speech marking: no outer quotation marks for Elihu (Job 37) or Wisdom (Prov 8); a colon and no quotation marks for Qohelet's internal speech.
- MT Psalm numbering, with the superscription as v 1 (Ps 8, 19), or run into v 1 (Ps 139).

## 3. Founder decisions (flagged, not blocking)

The pass applies a recommendation in each case. None is a speculative entry.

- **A. Ps 8:6, the article on Elohim.** Recommendation: keep 'Elohim' without the article, as the Hebrew has none. The canon quotes 'the Elohim'.
- **B. bĕnê (hā)ʾādām.** Now 'the sons of the human' / 'the sons of human', for corpus coherence with central `ha-adam` / `ben-adam` and genesis-woh 11:5. The alternatives are the ASV and canon-EN 'the sons of men' and the 1 Kgs 8:39 woh 'the children of men'. The corpus is currently split three ways. Whichever form is chosen, 1 Kgs 8:39 should be aligned. The Writings lines can be reverted with a string swap if the founder prefers 'sons of men'.
- **C. ʾereṣ cosmic 'earth'.** isaiah-woh and now the four Writings overlays carry the same clause. Recommendation: promote it to a context clause of central `eretz` in a later diff. It is held back from this diff to avoid colliding with the parallel `eretz` appliesTo merges.
- **D. Proper names.** The Writings follow job-woh and ezekiel-woh (English forms) against the Kings transliteration (founder decision A). This is the open corpus-alignment point that the Ezekiel overlay already raised.
- **E. ḥesed 'kindness' in the Psalms.** Central `chesed-solitary` is applied (as in Kings wave C-D). The Psalter has about 120 further occurrences, often in the fixed pair with ʾĕmet (central `chesed-v-emet` keeps 'chesed' transliterated). Confirm 'kindness' for solitary ḥesed before the Psalms grow, or choose 'steadfast love'.
- **F. Job 37:18 'clouds'.** For transparency only: the rendering rests on job-woh 38:37 and the lexica, and it coincides with the canon's « nuages ». The adjective is kept as 'strong', not 'solid'.

Reviewer-attention items (not founder-level):
- Eccl 3:21, where the MT pointing is kept against all the major versions.
- Ps 8:2, the vowel departure.
- Eccl 3:19-21, 'breath' throughout (inferred).
- Prov 8:30 *ʾāmôn* (inferred).

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` entry is created or extended, in the overlays or in the central diff. Nothing blocks the speculative gate.

---

## Unresolved editorial questions

**None.** All 74 were resolved:

| Chapter | Questions | Resolved by |
|---|---|---|
| Job 37 | 11 | `shechaqim` (18); `chesed-solitary` (13); `shaddai-eloah`; overlay ʾereṣ, Ketiv/Qere (12), MT baseline (7, 13), lineation (1); job-woh 38:13 precedent (3); commentary (2, 9, 10, 20, 22) |
| Ps 8 | 5 | MT numbering and superscription; Ps 8:2 vowel exception; MT (3); `ben-adam` (5); divine-names article (6) |
| Ps 19 | 6 | numbering; `shamayim`/`raqia`/`shaddai-eloah` (2); ASV construal (4); MT + reception (5); register (7); Torah terms (8) |
| Ps 33 | 6 | `chesed-solitary`, ʾereṣ (5); `shamayim`, `tzeva`, rûaḥ (6); MT (7); ʾašrê, names (12); register + `ha-adam` (13); ASV (15) |
| Ps 139 | 14 | heading in v 1; ASV (4); Ketiv/Qere (6, 16); rûaḥ (7); register + She'ol (8); MT (11, 14, 18, 20); `koneh` + `sakhak` (13); ʾereṣ (15); El/Eloah (17); commentary (24) |
| Ps 147 | 6 | Yah, Elohim, MT unit (1); names (2); ASV (4); register, ʾereṣ (8); two words (15); Ketiv/Qere + MT (19) |
| Prov 8 | 13 | wisdom lower case (1); ʾādām terms (4); MT (16); Ketiv/Qere (17, 35); `koneh` + `reshit` fix (22); commentary (23, 25, 29); register (27); `shechaqim` (28); `amon` (30); ʾašrê + nepeš (32 / 36) |
| Prov 10 | 6 | names (1); ASV construal (6, 22); MT (10); ASV + reception (13); `sûpâ` 'storm' consistency (25) |
| Eccl 3 | 7 | register (1); article rule + ʾādām terms (10); `ha-olam` (11); ASV construal + reception (15); MT + speech (17); `hevel` + rûaḥ (19); MT + rûaḥ (21) |

---

## Glossary changes for review

### Central glossary: `psalms-woh/wave-w1-central-diff.json` (base 2.83.0; recommended 2.84.0, minor)

Several parallel diffs also target 2.83.0, so the version op asks the orchestrator for three things:
- Give this diff the next free minor.
- Apply `appliesToAdded` as a union wherever a parallel diff has already extended the same entry. `appliesTo` values are complete relative to 2.83.0.
- Re-apply the appended rationale or wohChoice text if a parallel diff changed the same field first.

**Added:**
- `shechaqim-clouds-cross-corpus` (claim_type: `direct`)

**Modified (no decision reversed):**
- `koneh-shamayim-va-aretz`. Was 'creator of heaven and earth' (epithet only). Now the epithet plus a verbal clause, 'created' (Ps 139:13; Prov 8:22). The rationale paragraph flags Prov 8:22 as contested. appliesTo +2 translation refIds; the legacy ids are kept.
- `reshit-darkhei-el`. The rationale quotation of Prov 8:22 changes from 'YHWH possessed me, the first of his ways' to 'YHWH created me at the beginning of his way', with the ASV and appositional readings noted. Reason: the two central entries disagreed.
- `shaddai-eloah`. Was 'Shaddai / Eloah'. Now also bare ʾēl 'El' in the poetic books. Rationale appended; appliesTo +10.

**appliesTo only:** `shamayim` (+12), `eretz` (+3, 'land' sites only), `raqia` (+1), `ben-adam` (+3), `ha-adam` (+10), `elohim-as-translation` (+12), `tehom` (+4), `sheol-underworld-realm-of-the-dead` (+1), `chesed-solitary-covenant-kindness` (+5, lines changed), `tzedakah-u-mishpat-justice-pair` (+1), `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus` (+1, astral), `toevah-abomination-cross-corpus-keyword` (+1).

### Per-translation overlays (all new, v1.0.0)

**Shared Writings set:** identical in job-woh, psalms-woh, proverbs-woh and ecclesiastes-woh; extend all four together.
- Added: `proper-names-english-forms-convention-writings` (claim_type: `direct`)
- Added: `divine-names-convention-writings` (`direct`)
- Added: `shamayim-register-application-writings` (`direct`)
- Added: `eretz-earth-and-land-scope-writings` (`direct`)
- Added: `adam-enosh-ish-human-terms-writings` (`direct`)
- Added: `nefesh-scope-writings` (`direct`)
- Added: `ruach-wind-breath-spirit-writings` (`inferred`)
- Added: `ketiv-qere-qere-translated-writings` (`direct`)
- Added: `mt-baseline-versification-and-psalm-numbering-writings` (`direct`)
- Added: `poetic-lineation-and-speech-convention-writings` (`direct`)

**Book-specific:**
- psalms-woh, added: `psalm-superscription-terms-psalms` (`direct`), `torah-vocabulary-psalm-19` (`direct`), `sakhak-knit-together-psalm-139-13` (`direct`)
- proverbs-woh, added: `chokhmah-personified-wisdom-proverbs` (`direct`), `amon-master-workman-proverbs-8-30` (`inferred`)
- ecclesiastes-woh, added: `hevel-vanity-ecclesiastes` (`direct`), `ha-olam-eternity-ecclesiastes-3-11` (`direct`)

The job-woh overlay holds only the shared set. The signed-off Job chapters (1, 2, 38, 40-42) predate it and are not retro-edited.

---

## Follow-ups for the orchestrator (read-only files; not touched)

1. **Hosted ASV Psalms reference files** append the next psalm's heading to the last verse: Ps 8:9 (Ps 9 heading), 19:14 (Ps 20), 33:22 (Ps 34), 139:24 (Ps 140), 147:20 ('Psalm 148'). Strip these before the ASV files are used as a comparison column. The ASV numbering also runs one behind the MT in Pss 8 and 19.
2. **job-woh 38:37** (stable) should receive `shechaqim-clouds-cross-corpus` in glossaryRefs at its next revision; the application note is in the entry.
3. **1 Kgs 8:39 woh** 'the children of men' is the corpus outlier for bĕnê hāʾādām (founder point B).
4. **isaiah-woh 13:5** has the same horizon idiom (*miqṣēh haššāmayim*) as Ps 19:7, which is ruled 'skies' here. Align at the next Isaiah pass.
5. **Torah 'law' / 'teaching'.** Kings and Ps 19 have 'law', Isaiah 'teaching', and exodus-woh transliterates 'torah'. A corpus-wide entry is still pending.
6. **Isaiah ʾēl / ʾĕlôah 'God'.** Isaiah's book-level exception stands. The extended `shaddai-eloah` now names it explicitly.
