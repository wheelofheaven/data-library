# Matthew Wave M2 Editor Report: Mt 2, 3, 4, 8, 9, 10, 14, 15, 19, 23, 26, 27

**Book / chapters:** `matthew-woh` 2 (23 verses), 3 (17), 4 (25), 8 (34), 9 (38), 10 (42), 14 (36), 15 (39), 19 (30), 23 (38; 23:14 absent from the critical text), 26 (75), 27 (66). That is 463 paragraphs.
**Editor pass:** 2026-11-01 (claude-opus-5-5, woh-editor role)
**Status at end of pass:**
- All twelve chapters moved from `draft` to `editor-review`.
- Version `0.1.0` → `1.0.0-rc1`.
- `glossaryVersion` set to 2.81.0, pending application of `wave-m2-central-diff.json` (base 2.80.0). The orchestrator may renumber it when sequencing the parallel Revelation and Ezekiel diffs.
- `overlayGlossaryVersion` set to 1.2.0 (applied).
- `claude-opus-5-5 (editor)` added to `modelDrafts`; `reviewer` left `pending`.

**Editorial questions:** 77 received, 77 resolved. Every array is cleared, and each resolution is logged in `editorial_questions_resolved[]` with its glossary entry. No question is escalated as unresolvable. Ten resolutions are listed below as founder-preference points.

**Files written (only these)**

- `matthew-woh/chapter-{2,3,4,8,9,10,14,15,19,23,26,27}.json`
- `matthew-woh/_translation-glossary.json` (1.1.0 → 1.2.0, edited directly)
- `matthew-woh/wave-m2-central-diff.json` (proposed, not applied; 2.80.0 → 2.81.0)
- this report

No central glossary file, published Matthew chapter, `_meta.json`, Revelation or Ezekiel file was read for editing or written.

**Counts**

- **Commentary** (`notes.official`): 267 of 463 paragraphs, about 12,900 words. The uncommented verses are plain narrative with no divergence from the ASV.
- **Reception notes:** 26 separately headed paragraphs ("Wheel of Heaven reading (reception note, not a translation claim)"). Eleven further canon-cited verses carry a pointer to the range note that covers them.
- **Overlay:** 35 new entries, all `direct`, and 1 appliesTo extension (`aionios-eternal-vs-age-pertaining-translation-convention` + 19:16, 19:29).
- **Central diff:** 0 new entries; 6 appliesTo-only extensions, including the requested `son-of-man-coming-in-cloud-...` + MAT-WOH-26:64.
- **English text changed at 32 verses** (33 edits). Every change is backed by an overlay entry (rule 7):
  - **'magi'** for 'wise men' (`magoi-magi-mt-2`): 2:1, 2:7, 2:16 (×2).
  - **'at its rising'** for 'in the east' (`en-te-anatole-at-its-rising-mt-2-2-9`): 2:2, 2:9.
  - **Generic ἄνθρωπος** (`anthropos-generic-people-convention-matthew`):
    - 'the men marveled' → 'the people marveled' (8:27).
    - 'to men' → 'to people' (9:8).
    - 'the precepts of men' → 'teaching human precepts as doctrines' (15:9).
    - 'defiles the man' → 'defiles a person' (15:11 ×2, 15:18, 15:20 ×2).
    - 'let no man separate' → 'let no one separate' (19:6).
  - **ναός → 'sanctuary'** for 'temple' (`naos-sanctuary-hieron-temple-matthew`): 23:16 (×2), 23:17, 23:21, 26:61, 27:5, 27:40, 27:51. ἱερόν stays 'temple' (4:5; 26:55), and 23:35 already read 'sanctuary'.
  - **'faith' → 'faithfulness'** at 23:23 (`krisis-eleos-pistis-justice-mercy-faithfulness-mt-23-23`; BDAG s.v. πίστις 1a lists this verse).
  - **'send me' → 'put at my disposal'** at 26:53 (`paristemi-put-at-disposal-mt-26-53`; BDAG s.v. παρίστημι 1a cites this verse).
  - **Colon before quotations** (`speech-introduction-colon-convention-matthew`; punctuation only): 10:7, 15:4, 15:5 (two levels), 19:5, 23:16, 23:30, 23:39, 26:18 (two levels), 26:31, 26:61, 27:43, 27:63, 27:64.
- All other lines are the Translator's draft, unchanged. Double quotes are balanced in every chapter and their count is unchanged from the drafts.

---

## Speculative entries requiring sign-off

**None.** No `claim_type=speculative` or `inferred` entry is created or extended, in either the overlay or the central diff. Nothing blocks advance on the speculative count.

### Canon-cited sites in wave M2

At each of these sites, the English line renders the Greek lexically. The Raëlian reading appears only in a paragraph headed **"Wheel of Heaven reading (reception note, not a translation claim)"**. Each site was checked against `matthew-canon-citations.md`.

| Site | Canon | Line |
|---|---|---|
| 2:2 | TBWTT 4: « son étoile se lever … nous prosterner »; the star as a guiding craft | 'his star at its rising … worship him' |
| 2:9 | TBWTT 4: « vint se placer au-dessus de l'enfant » | 'star … stood over where the child was' |
| 2:13 | TBWTT 4: the creators watch over the child | 'an angel of the Lord' |
| 2:19-20 | TBWTT 4 | 'an angel of the Lord … in a dream' |
| 3:16-17 | TBWTT 4: initiation by the creators; « mon fils, l'aimé » | 'the Spirit of God'; 'my beloved Son' |
| 4:1-11 | TBWTT 4 (4:1); LWTE 2: test of fidelity, *diabolos* = « calomniateur » | 'tempted by the devil' |
| 4:11 | LWTE 2: 'the Elohim's messengers' | 'angels' |
| 4:24 | TBWTT 4: healings by applied science | 'moon-struck … he healed them' |
| 8:2-3 | TBWTT 4: « sois purifié »; concentrated rays | 'be made clean' |
| 9:5, 7 | TBWTT 4: operation at a distance | 'Rise and walk … he rose' |
| 9:13 | TBWTT 4: 'the just' | 'the righteous' (critical text, no 'to repentance') |
| 10:9-10 | TBWTT 5: « Ne possédez ni or … ni monnaies » | 'Do not acquire … copper' |
| 10:32 | TBWTT 4: « mon père qui est dans les cieux » | 'my Father who is in the heavens' |
| 14:19 (and 15:36) | TBWTT 4: 'multiplication of the loaves' (no verse reference) | as written |
| 14:25 | TBWTT 4: anti-gravitational ray | 'walking on the sea' |
| 14:30, 32 | TBWTT 4: turbulence from the ray | 'the strong wind' (SBLGNT) |
| 15:11 | TBWTT 5: « profane l'homme » | 'defiles a person' |
| 19:23 | TBWTT 5: « le règne des cieux » | 'the kingdom of the heavens' |
| 19:30 | TBWTT 4: « Les premiers seront les derniers … » | 'many who are first will be last' |
| 23:4-11 | TBWTT 5: « un maître … un directeur, le Christ » | 'teacher'; 'instructor' |
| 26:52-54 | TBWTT 4: « faire appel … mettrait à ma disposition » | 'appeal to … put at my disposal' |
| 27:20 | LWTE 3: KJV wording | 'Barabbas' |
| 27:42-43 | ETTMTTP 2: « Je suis le fils de Dieu » | 'the Son of God' |

Two lines now coincide with the canon's French: 2:2 and 2:9 'at its rising', and 26:53 'put at my disposal'. In both cases the change rests on BDAG, which cites these very verses for these senses, and on the major modern versions (2:2, 9: NRSV and NAB 1970 'at its rising', ESV 'when it rose'; the RSV keeps 'in the East'). Both commentaries state the grounds and record the agreement separately, so a reviewer can audit that the lens was not the reason for the change.

---

## Unresolved editorial questions

None. The program-wide rulings the Translator asked for are summarized here with their entries:

| Point | Ruling | Entry |
|---|---|---|
| ἄγγελος (2:13 etc.) | 'angel', consistent with published Mt 1, 13, 25, 28 and Acts 12. The Hebrew-side 'messenger of YHWH' is not applied to the Greek; the reason is given at 2:13 | `angelos-angel-matthew-convention` |
| Spirit (3:16) | Capital 'Spirit' with the article for God's πνεῦμα; lower case for the human spirit (26:41; 27:50) and for unclean spirits | `pneuma-spirit-capitalization-matthew` |
| πειράζω (4:1) | 'tempted' / 'the tempter' where the devil is the agent; 'testing' for the opponents' questions (19:3). The 'test' reading is in the commentary | `peirazo-peirasmos-tempt-test-matthew` |
| διάβολος | 'the devil'; 'slanderer' etymology in the commentary | `diabolos-the-devil-matthew` |
| Σατανᾶς | 'Satan' as a name; central `ha-satan` (Hebrew, article) not applied | `satanas-satan-name-matthew` |
| generic people / men | 'people' / 'a person' / 'no one' for generic ἄνθρωπος; 'man' for individuals and every ἀνήρ | `anthropos-generic-people-convention-matthew` |
| εὐαγγέλιον | 'gospel', as in the published Mk 16:15 and Acts 15:7 | `euangelion-gospel-matthew` |
| ψυχή (10:28) | 'soul' at 10:28 and 26:38; 'life' at 2:20 and 10:39 | `psyche-soul-life-matthew` |
| ἐγώ εἰμι (14:27) | 'it is I'; the LXX 'I am' resonance in the commentary | `ego-eimi-it-is-i-mt-14-27` |
| Anarthrous Son of God (14:33; 27:43, 54) | 'the Son of God'; Colwell's rule and the 'a son of God' option in the commentary | `huios-theou-son-of-god-rendering-matthew` |
| παλιγγενεσία (19:28) | 'the regeneration' | `palingenesia-the-regeneration-mt-19-28` |
| ναός / ἱερόν (26:61) | 'sanctuary' / 'temple', consistently | `naos-sanctuary-hieron-temple-matthew` |
| σεισμός (8:24 vs 27:54) | 'tempest' on the sea; 'earthquake' on land | `seismos-tempest-earthquake-matthew` |
| γῆ (27:45) | 'over all the land'. The Translator's note attributing 'earth' to the KJV is mistaken: the KJV also reads 'land' | `ge-land-earth-mt-27-45` |
| καθηγητής (23:10) | 'instructor' | `kathegetes-instructor-mt-23-10` |
| Speech introduction | Colon in new chapters, at every level; comma only for embedded words | `speech-introduction-colon-convention-matthew` |
| Son of Man on the clouds (26:64) | Central entry extended to MAT-WOH-26:64 | central diff |
| Critical text vs Byzantine / KJV | SBLGNT translated; every Byzantine/KJV reading recorded in the commentary; 23:14 has no paragraph and is quoted at 23:13; 27:35 and 27:49 additions and Jesus Barabbas documented | `critical-text-baseline-and-byzantine-variant-recording-matthew` |

---

## Founder-preference points (resolved, non-blocking; confirm or overrule)

1. **ἄγγελος 'angel' in the Greek NT vs 'messenger' in the Hebrew Bible.** This is the deliberate split already implied by the published chapters. The Revelation editor is ruling in parallel, so the two Greek books should be harmonized at sign-off. The entry is held in the overlay and recommended for promotion to central once both books agree.
2. **ναός 'sanctuary'** throughout: 7 lines changed. 27:5 now reads 'into the sanctuary', which preserves Matthew's own crux and is explained in the commentary.
3. **23:14 has no paragraph.** This follows the 6:13 doxology precedent and the orchestrator's instruction. It is inconsistent with the stable 17:21, which is printed as a bracketed paragraph; see the follow-ups.
4. **Colon convention** for new chapters.
5. **'magi'** for μάγοι, replacing 'wise men'.
6. **'faithfulness'** at 23:23.
7. **'put at my disposal'** at 26:53. This is lexically grounded and coincides with the canon (see above).
8. **'at its rising'** at 2:2 and 2:9. This is lexically grounded and coincides with the canon (see above).
9. **'defiles a person'** at 15:11-20. The canon's English quotes 'the man'.
10. **'tempted'** at 4:1. The canon reads 'put to the test'; the line keeps the agent-driven sense, and the test reading is in the commentary.

---

## Glossary changes for review

### Central glossary (`wave-m2-central-diff.json`, 2.80.0 → 2.81.0 recommended, minor)

All six changes are appliesTo extensions (`modify`). No wohChoice, rationale or claim_type is changed.

- `son-of-man-coming-in-cloud-dan-7-13-synoptic-revelation-1-7-cross-corpus` + MAT-WOH-26:64
- `son-of-man-bar-enash-dan-7-13-mt-cross-corpus` + 8:20, 9:6, 10:23, 19:28, 26:2, 26:24, 26:45, 26:64
- `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim` + 3:2, 4:17, 8:11, 10:7, 19:12, 19:14, 19:23, 23:13
- `christos-māšîaḥ-anointed-one-cross-corpus-greek-hebrew-aramaic` + 2:4, 23:10, 26:63, 26:68, 27:17, 27:22
- `mountain-as-revelation-site-mt-cross-corpus-har-sinai-mount-sapunu` + 4:8, 8:1, 14:23, 15:29 (26:30 dropped after review: a place name, weak fit)
- `aiōnios-mt-25-41-46-eternal-vs-age-pertaining-cross-corpus` + 19:16, 19:29

**Sequencing:** the appliesTo arrays are complete relative to 2.80.0, and each op also carries an informational `appliesToAdded`. If the Revelation diff (likely to extend the two Son-of-Man entries) is applied first, merge the arrays as a union rather than overwriting.

The following central entries are cited in the commentary as background and **not** applied: `malakh-yhwh-messenger`, `ha-satan`, `ruach-elohim`, `cosmic-signs-cluster-...` (27:45), `ulam-hekhal-devir-...`, `brit-covenant`, `karat-brit-cut-covenant`.

### Per-translation overlay (`_translation-glossary.json` 1.1.0 → 1.2.0, applied)

All 35 additions are `direct`:

- **Conventions:**
  - `critical-text-baseline-and-byzantine-variant-recording-matthew`
  - `raelian-canon-citation-reception-note-convention-matthew`
  - `speech-introduction-colon-convention-matthew`
  - `anthropos-generic-people-convention-matthew`
  - `proper-names-and-realia-forms-matthew`
- **Greek-NT lexical:**
  - `angelos-angel-matthew-convention`
  - `pneuma-spirit-capitalization-matthew`
  - `peirazo-peirasmos-tempt-test-matthew`
  - `diabolos-the-devil-matthew`
  - `satanas-satan-name-matthew`
  - `euangelion-gospel-matthew`
  - `psyche-soul-life-matthew`
  - `huios-theou-son-of-god-rendering-matthew`
  - `naos-sanctuary-hieron-temple-matthew`
  - `seismos-tempest-earthquake-matthew`
  - `proskyneo-worship-kneel-matthew`
  - `katharizo-make-clean-leprosy-matthew`
  - `skandalizo-fall-away-take-offense-matthew`
- **Site-specific:**
  - `magoi-magi-mt-2`
  - `en-te-anatole-at-its-rising-mt-2-2-9`
  - `pais-servant-mt-8`
  - `hoi-huioi-tou-nymphonos-mt-9-15`
  - `ktaomai-acquire-mt-10-9`
  - `ego-eimi-it-is-i-mt-14-27`
  - `doron-qorban-gift-mt-15-5`
  - `kynaria-the-dogs-mt-15-26`
  - `palingenesia-the-regeneration-mt-19-28`
  - `kathegetes-instructor-mt-23-10`
  - `krisis-eleos-pistis-justice-mercy-faithfulness-mt-23-23`
  - `diatheke-covenant-mt-26-28`
  - `hetaire-eph-ho-parei-mt-26-50`
  - `paristemi-put-at-disposal-mt-26-53`
  - `tes-dynameos-the-power-mt-26-64`
  - `ge-land-earth-mt-27-45`
  - `koustodia-you-have-a-guard-mt-27-65`

Extended: `aionios-eternal-vs-age-pertaining-translation-convention` + 19:16, 19:29.

Several overlay appliesTo arrays list published refIds (e.g. 1:20, 6:13, 13:21, 28:2), recording that these entries govern lines already published. No published line was changed.

---

## Follow-ups for the orchestrator (read-only or out-of-scope files)

1. **`matthew-woh/_meta.json`** still lists the 8 published chapters. Add the 12 wave-M2 chapter files at publication.
2. **Published inconsistencies to fix in a later pass** (not edited here):
   - (a) 17:21 is printed as a bracketed paragraph, against the 23:14 / 6:13 omission rule.
   - (b) 17:22 reads 'into the hands of men' against the generic-people convention.
   - (c) 25:12, 25:40, 25:45, 28:5 and 28:18 use a comma before speech; 1:20, 13:24 and 17:22 use a colon.
   - (d) The central `lords-prayer-mt-6-9-13-...` wohChoice says 'testing' for πειρασμός, but the stable 6:13 line reads 'temptation'. The wave follows the published line.
3. **Promotion candidates to central** after the Revelation ruling: `angelos-angel-matthew-convention`, `pneuma-spirit-capitalization-matthew`, `critical-text-baseline-and-byzantine-variant-recording-matthew`.
4. **Bibliographic precision:** the commentary and the overlay cite Davies-Allison, France, Hagner, Metzger and Brown 'ad loc.' rather than by page. The Reviewer may add page references.
