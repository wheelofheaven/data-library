# Sign-off package — Vendidad Fargard 2 (vendidad-woh, chapter 2)

**Status:** `awaiting-human` · **version** `1.0.0-rc1` · central glossary 2.73.0 (+ proposals pending) · overlay `1.0.0`

The program's first Avestan text: Ahura Mazda, Yima, the evil winters and the Vara (Geldner 1896 via avesta.org; reference Darmesteter, SBE 4, 1898). Pipeline: Translator → Editor → Reviewer, all complete; nothing is stable until the human sign-off below.

## Summary

| Item | Count |
|---|---|
| Verses translated | 41 (Geldner 1–43; 12–14 one abbreviated unit) |
| Verses with commentary (`notes.official`) | 29 |
| Translator questions raised / resolved | 36 / 36 |
| Overlay entries (new book glossary) | 33 — direct 23, inferred 10 |
| Central proposals | 3 new (1 direct, 1 inferred, 1 speculative) + 4 `appliesTo` extensions + `ave` in sourceLanguages |
| Reviewer verse verdicts | approve 35, revise 3, flag-for-human 3 |
| Lens-leakage flags | 0 |

## Items requiring decision

1. **Speculative central entry `vara-as-designed-preservation-habitat-woh-reading`** (reviewer: flag-for-human). The first extension of the Wheel of Heaven lens into Avestan; cited only in apparatus (glossaryRefs at 25/30/40/41 and one labelled paragraph in the v.25 commentary). Reviewer asks to replace the phrase "non-human authority" (entry + v.25 commentary) with "on instruction from a superior authority (in the text, Ahura Mazda)", to match the 2026-05 framing (Elohim as a small advanced human civilization). **Options:** (a) accept with that wording fix; (b) drop the entry, the four refs and the v.25 paragraph.
2. **Exclusion list, VID-2:29/37** (reviewer: flag-for-human). Six terms of uncertain meaning (*apāuuaiia-, hərəδi-, driβi-, daiβi-, kasuuī-, vīzbāri-*) carry Darmesteter's renderings. Reviewer recommends: keep them, mark each "(?)" in the English, and add "(?)" to the bracket convention; do NOT adopt the editor's unsourced physical-defect glosses.
3. **VID-2:25** (reviewer: flag-for-human) — carries the labelled interpretive paragraph; follows item 1.
4. **Reviewer revise items (apply at ratification):**
   - VID-2:22 English → "from which the cloud shall first snow down snowflakes" (*pauruuō* "first", *snaoδō* singular); same fix in overlay entry `aghem-zimo-evil-winters-aredvi-measure-vendidad-woh` (`literal`, `wohChoice`).
   - VID-2:24 commentary → "The WoH text follows Darmesteter's construal but takes…".
   - VID-2:30 commentary → the reviewer's reworded ⟨stroke⟩ sentence; retarget the boat-window pointer to the vara-tevah-eleppu entry.
   - Central `vara-tevah-eleppu-…`: "stocks it with the seeds of every kind (2.25-27), the plant and food seeds in pairs (2.28)"; cite "CAD E s.v. eleppu" without the unverified page range.
   - Do **not** extend `ab-bur-aptu-chalon-ha-tevah-…` (built-in self-shining window ≠ hull opening after the storm); drop it from the glossaryRefs of 30 and 38.
   - Seed-preservation extension: note the Avestan has no reward clause. Lacuna-bracket extension: note that [ ] restores from earlier in the same chapter.
   - Non-blocking: "x'airiieiti" → source form "x'airiieite"; v.25 "Therefore" → "Then" for *āat*; credit or reword the *suβrā* "horn / arrow or awl" proposals.
5. **Approved by the reviewer, listed for completeness:** *suβrā* left untranslated (×6); ⟨stroke⟩/⟨stroked⟩ supplied at 30/38; the bracket convention ([ ] restored / ⟨ ⟩ supplied / … source ellipsis); `yima-yama-…` central entry (direct, Christensen).

## Reviewer report

```json
{
  "reviewer": "claude-opus-5-5 acting as woh-reviewer",
  "reviewedAt": "2026-10-31T19:16:53Z",
  "verdicts": [
    {
      "refId": "VID-2:1",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 1",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. ašauuan-, aniia-"
      ],
      "reasoning": "Re-parsed: peresat + acc.; voc. string mainiiō spəništa dātarə gaēθanąm astuuaitinąm ašāum; kahmāi … aperəse.tūm with dat.; aniiō mana 'other than me'. 'Other than me' is more literal than SBE 'before myself' (paoiriiō already carries 'first'), and 'righteous one' for ašāum is a lexically grounded modernisation; no lens."
    },
    {
      "refId": "VID-2:2",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 2 with n. 2",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. huuąθβa-"
      ],
      "reasoning": "Dative yimāi srīrāi huuąθβāi answers kahmāi; huuąθβa- is a bahuvrīhi 'having good herds', so 'of the good herds' restores the word where SBE's 'good shepherd' follows the Pahlavi gloss. Yima-Yama note is standard Indo-Iranian philology and stays in commentary."
    },
    {
      "refId": "VID-2:3",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. mərəta-, dāta-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 3"
      ],
      "reasoning": "vīsaŋha imperative 'consent, be ready' (SBE 'Well … be thou'); mərətō bərətaca 'rememberer and bearer' follows the roots mar-/bar-; nōit dātō … nōit cistō 'not made … not taught' is the participle of dā-, SBE's 'born' a paraphrase. Defensible, marked inferred."
    },
    {
      "refId": "VID-2:4",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. θrātar-, harətar-, aiβiiāxštar-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 4"
      ],
      "reasoning": "θrātar- = Vedic trātṛ- 'protector', harətar- 'keeper', aiβiiāxštar- 'overseer': the corrected triad is lexically secure and SBE's 'nourish/rule' is the outlier; 'my world' for plural gaēθā̊ is the established idiom with the plural disclosed in commentary."
    },
    {
      "refId": "VID-2:5",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Exact: future/subjunctive 1sg. forms answered point by point; nōit mana xšaθre buuat aotō vātō nōit garəmō nōit axtiš nōit mahrkō = 'under my rule there shall be neither cold wind nor hot, neither disease nor death'."
    },
    {
      "refId": "VID-2:6",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 6 with nn. 3-4",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. suβrā-, aštrā-"
      ],
      "reasoning": "zaiia (dual) 'two implements' matches SBE; aštrā- 'goad' is the Vendidad's own penal-instrument word, SBE's 'poniard' imports later investiture imagery. Leaving suβrā- transliterated is the honest choice for an object with no secure identification (SBE itself wavers 'seal'/'ring' at vv. 30/38). Non-blocking: the commentary's 'later proposals include a horn and an arrow or awl' should be attributed to named scholars or generalised to 'other objects have been proposed'."
    },
    {
      "refId": "VID-2:7",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 vv. 6-7 ('[Obscure.]')",
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "yimō asti bərəθe xšaθraiiā̊: copula + dative infinitive; 'Yima is to bear the kingly rule' is a minimal, non-smoothing rendering of an obscure clause, and the commentary states the obscurity. Geldner numbering correctly preferred over SBE's relocation."
    },
    {
      "refId": "VID-2:8",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 8"
      ],
      "reasoning": "θrisatō.zima haṇjasəṇti 'three hundred winters … were completed'; catalogue (pasu/staora, men, dogs, birds, suxra saociṇta fires) rendered completely and identically to its later recurrences."
    },
    {
      "refId": "VID-2:9",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "paiti.vaēδaēm 'I warned/informed'; present-tense direct speech (pərəne … haṇgata … nōit … vīndəṇti) rendered as present. Formula consistent with v. 8."
    },
    {
      "refId": "VID-2:10",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. raocah-, rapiθβā-, friθa-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 10 with nn. 5-6"
      ],
      "reasoning": "raocā̊ ā is acc. pl. + directional ā, so 'toward the lights' corrects SBE's 'in light'; rapiθβā 'midday' = south is standard. fraca šuua vīca 'move forward and spread apart' is closer than SBE's paraphrase and nəmaŋha is restored. The uncertain handling verbs are disclosed."
    },
    {
      "refId": "VID-2:11",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. θrišuua-, zaoša-"
      ],
      "reasoning": "aēuua θrišuua 'by one third'; hē is singular, so 'it pleased him' is grammatical where SBE's 'as many as he wished' adds a quantity. 'went forth' for fracarəṇta fine."
    },
    {
      "refId": "VID-2:12-14",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed) (abbreviated unit)",
        "Central lacuna-bracket-convention-sumerian-mesopotamian-project-standard"
      ],
      "reasoning": "Source prints xšuuaš.satō.zima … pərəne … mašiiānąmca; text outside the brackets corresponds exactly to the printed words (incl. final 'men' = mašiiānąmca), and the bracketed span is a verbatim restoration of vv. 8-10 with verse markers. Convention correctly applied."
    },
    {
      "refId": "VID-2:15",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "duua θrišuua 'by two thirds'; formula identical to v. 11."
    },
    {
      "refId": "VID-2:16",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "nauua.satō.zima 'nine hundred winters'; formula identical to v. 8."
    },
    {
      "refId": "VID-2:17",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Identical to v. 9; re-read in source."
    },
    {
      "refId": "VID-2:18",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Identical to v. 10; re-read in source."
    },
    {
      "refId": "VID-2:19",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 19 ('two-thirds')",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. θrišuua-"
      ],
      "reasoning": "θribiiō θrišuuaēibiiō is instr./abl. pl. 'by three thirds', completing the 1/2/3 series; SBE's 'two-thirds' repeats v. 15 and is an error in the reference. Correction confirmed."
    },
    {
      "refId": "VID-2:20",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. srūta-, mainiiauua-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 20"
      ],
      "reasoning": "srūtō is nom. sg. masc. and cannot agree with loc. airiiene vaējahi, so 'he, renowned in Airyana Vaejah' is grammatically forced; vaŋhuiiā̊ dāitiiaiiā̊ is gen. sg. fem. ('of the Good Daitya'); mainiiauua- 'spiritual'; xšaēta- 'radiant' distinguished from srīra-. All corrections of SBE confirmed."
    },
    {
      "refId": "VID-2:21",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "ā.tat haṇjamanəm paiti.jasat … renders the arrival formula exactly, parallel to v. 20."
    },
    {
      "refId": "VID-2:22",
      "status": "revise",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pauruua- ('first, former') vs pouru- ('much')",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 22",
        "Overlay entry v24-pasture-before-meltwater-footprint-wonder-vendidad-woh (Editor's own lexical ruling)"
      ],
      "reasoning": "Re-parsed: yahmat haca pauruuō snaoδō vafra snaēžāt — pauruuō is from pauruua- 'first, former' and snaoδō is nom. SINGULAR. The English 'many clouds' treats pauruuō as pouru- 'much' and pluralises the subject, contradicting the Editor's own ruling at v. 24 (pauruua 'before, first', not pouru 'much'). Proposed English: '…upon the material world the evil winters shall come, from which the cloud shall first snow down snowflakes on the highest mountains, on the heights, an aredvi deep.' (or, if 'much/many' is retained, the commentary must justify reading pauruuō as 'much' against the v. 24 note). Otherwise approved: 'evil winters' hedged correctly, Malkosan rightly excluded, aredvi disclosed, Flood comparison properly hedged with the indigenous-winter-myth alternative (Boyce, HZ I)."
    },
    {
      "refId": "VID-2:23",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 23",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. θrižat-, θβiiąstəma-, raona-"
      ],
      "reasoning": "θrižatca … gə̄uš apa.jasāt opens with 'a third', which SBE omits; θβiiąstəmaēšu asaŋhąm 'in the most dreadful of places' is literal; 'shall go away' keeps the escape/perish ambiguity open; 'sheltered dwellings' avoids SBE's subterranean interpretation of paxruma-. Correction confirmed."
    },
    {
      "refId": "VID-2:24",
      "status": "revise",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 24",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pauruua-, abda-, vītaxti-"
      ],
      "reasoning": "English approved: the construal is obscure but disclosed; pauruua 'before' is right, and 'flood' for meltwater (āfš … vazaiδiiāi) is Darmesteter's own word, a natural English rendering of meltwater, not a Flood import (the commentary says the meltwater is aftermath only). Revise is for the COMMENTARY only: it contains pipeline meta-language unfit for a permanent reader-facing note. Replace 'The Editor keeps the Translator's Darmesteter-based construal but takes *pauruua* as…' with 'The WoH text follows Darmesteter's construal but takes *pauruua* as…'."
    },
    {
      "refId": "VID-2:25",
      "status": "flag-for-human",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 introduction to Fargard 2 and v. 25 with nn. 18-19",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. vara-, carətu-, taoxman-"
      ],
      "reasoning": "English approved as translation: varəm kərənauua 'make the Vara' (transliterated as in all Iranist practice), carətu.drājō kəmcit paiti caθrušanąm 'the length of a race-course on each of its four sides', taoxma 'seeds'; no 'two of every kind', no 'ark'. ('Therefore' for āat follows SBE; elsewhere āat is 'then' — optional harmonisation.) Flagged only because the commentary's labelled 'Wheel of Heaven reading' paragraph depends on the speculative central proposal needing named sign-off, and its phrase 'on instruction from a non-human authority' should be checked against the project's 2026-05 framing (Elohim as a small advanced human civilisation); suggested wording: 'on instruction from a superior authority (in the text, Ahura Mazda)'."
    },
    {
      "refId": "VID-2:26",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 26 with n. 20",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. zairi.gaona-, ajiiamna-, fraskəmba-"
      ],
      "reasoning": "āpəm frātat.caiia 'make the waters flow'; marəγa 'birds'; ajiiamna- qualifies the food that is eaten, not the colour, so SBE's 'green that never fades' is correctly undone. The four dwelling terms (three hapaxes per SBE n. 20) are glossed by root and marked inferred. Non-blocking typo: commentary and overlay write 'x'airiieiti'; the source form is x'airiieite (avesta.org hvairyeite)."
    },
    {
      "refId": "VID-2:27",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. sarəδa-, sraēšta-"
      ],
      "reasoning": "taoxma of narąm nāirinąmca, mazišta- vahišta- sraēšta- 'greatest and best and fairest'; gə̄uš sarəδanąm 'all kinds of cattle'. The Genesis contrast (selection by excellence) is properly in commentary."
    },
    {
      "refId": "VID-2:28",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 28 ('two of every kind')",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. miθβara-, ajiiamna-, uruuarā-"
      ],
      "reasoning": "uruuarā- 'plants' and x'arəθa- 'foods' are the general terms (SBE's trees/fruits follow the Pahlavi examples). Key lens check passed: miθβairē is rendered 'in pairs', deliberately avoiding SBE's KJV-echoing 'two of every kind' (Gen 6:19). varəfšuua loc. pl. 'in the Varas' kept honestly."
    },
    {
      "refId": "VID-2:29",
      "status": "flag-for-human",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 29 with nn. 24-25",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. frakauua-, apakauua-, daxšta-"
      ],
      "reasoning": "Re-parsed: mā + nominative list; transparent items corrected well (fra-/apa-kauua 'humped in front/behind'; vīmitō.dantan- 'misshapen teeth'; paēsa- yō vītərətō.tanuš 'leper whose body is set apart'; daxšta- 'marks'). The six middle items (apāuuaiia-, hərəδi-, driβi-, daiβi-, kasuuī-, vīzbāri-) are genuinely uncertain and the English presents Darmesteter's moral readings with no visible uncertainty. Reviewer recommendation: keep option A as interim but mark each of the six with '(?)' in the line (standard Iranist practice; record as a fourth mark in the bracket convention), and have the human weigh that the frame 'marks of Angra Mainyu laid upon mortals' and the bodily company of the list (humps, teeth, leprosy) give contextual weight to a physical-defect reading. Option B must not be adopted unless each gloss is checked against and attributed to a named lexicon (e.g. Bartholomae)."
    },
    {
      "refId": "VID-2:30",
      "status": "revise",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. marəz-, pərətu-, raocana-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 30"
      ],
      "reasoning": "English approved: fratəma/maδəma/nitəma 'foremost/middle/lowest' and pərəθβō 'passages' are lexical; 1000/600/300 exact; ⟨stroke⟩ is a well-motivated supply (preverb aiβi- gapped with following marəza, parallel to api … marəza), honestly marked, and better than SBE's silent merger or importing v. 10's verb; the verbless 'a door, a window self-shining from within' is left as apposition, more faithful than SBE's supplied 'make'. Revise is for the COMMENTARY only: remove pipeline meta-language. Replace 'The Editor therefore supplies ⟨stroke⟩ in angle brackets, the overlay sign for editorial supply. The draft's '[press]' imported a verb from v. 10, and Darmesteter merges…' with 'The WoH text therefore supplies ⟨stroke⟩ in angle brackets, the overlay sign for editorial supply; importing *aiwišuuat* 'pressed' from v. 10 would add a verb the clause does not imply, and Darmesteter merges…'. Also retarget the boat-window pointer (see glossary review of the ab-bur extension)."
    },
    {
      "refId": "VID-2:31",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 31 with n. 27",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. xšuuisti-"
      ],
      "reasoning": "mąsta 'thought'; pāšnābiia vīspara zastaēibiia vīxaδa 'tread apart with your heels, knead apart with your hands'; the comparison names no potter and no clay, so SBE's 'potter's clay' is rightly removed and the link to vīšāuuaiia- (vv. 11/15/19) preserved."
    },
    {
      "refId": "VID-2:32",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 32 with n. 28",
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Geldner prints the verse in the text (SBE brackets it 'From the Vendidad Sada'); translated unbracketed per numbering convention. Re-read: vīsparat / vīxaδat 3sg. past executing v. 31 exactly."
    },
    {
      "refId": "VID-2:33",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Execution formula of v. 25 (kərənaot / upa.barat), rendered identically in past tense."
    },
    {
      "refId": "VID-2:34",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Execution of v. 26 (frātat.caiiat, auuastaiiat); identical renderings."
    },
    {
      "refId": "VID-2:35",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Execution of v. 27; identical renderings."
    },
    {
      "refId": "VID-2:36",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "Execution of v. 28 (kərənaot miθβairē 'he made them in pairs'); no 'two of every kind'."
    },
    {
      "refId": "VID-2:37",
      "status": "flag-for-human",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 37",
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "nōit (indicative negation) correctly rendered 'There was there no…' against v. 29's prohibitive mā. Same six uncertain terms as v. 29; whatever ruling the human makes at v. 29 must be mirrored here."
    },
    {
      "refId": "VID-2:38",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. marəz-"
      ],
      "reasoning": "Execution of v. 30 with ⟨stroked⟩ marked consistently; aiβica hō varəfšuua … apica hō varəm marəzat parsed the same way."
    },
    {
      "refId": "VID-2:39",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)"
      ],
      "reasoning": "caiiō … aēte raocā̊ … yō … ā.raocaiieite aētaēšuua varəfšuua 'What, then, are those lights … that shine there in those Varas'; plural kept."
    },
    {
      "refId": "VID-2:40",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 40 with nn. 29-30",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. x'aδāta-, stiδāta-, hakərət"
      ],
      "reasoning": "x'aδāta- 'self-created' (x'a- + dāta-) corrects SBE's 'uncreated'; stiδāta- 'created in the world'. hakərət is rendered ('only once'), which SBE's 'the one thing missed' omits; SBE's 'underground' explanation and 'artificial lights' gloss are rightly kept out of the line. Note 'only' slightly strengthens hakərət but is idiomatic for the sense. No technological framing leaks into 'self-created lights'."
    },
    {
      "refId": "VID-2:41",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 41 with n. 32",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. aiβi.gāma-, miθβana-"
      ],
      "reasoning": "taēca aiiarə maniieṇte yat yārə opens v. 41 in Geldner; caθβarəsatəm aiβi.gāmanąm 'every forty years'; duuaēibiia haca nərəbiia duua nara us.zaiieiṇte miθβana strīca nairiiasca rendered with the duals and the female-male order intact; sraēšta- gaiia 'fairest life' keeps the srīra- link."
    },
    {
      "refId": "VID-2:42",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 42 with n. 34",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. vī-bar-, māzdaiiasni-"
      ],
      "reasoning": "vīš karšipta 'the bird Karshipta'; vī.barat 'spread'; māzdaiiasnī- 'Mazda-worshipping'; 'Spitama' kept where SBE substitutes 'holy'. All lexical."
    },
    {
      "refId": "VID-2:43",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 43 with n. 35"
      ],
      "reasoning": "kō aēšąm asti aŋhuca ratušca 'Who is their lord and master'; uruuatat.narō … tūmca yō zaraθuštrō. Bracket convention correctly applied twice: [of the material world] restores the source's 'dātarə … ašāum' from v. 1, and 'Ashem vohu …' keeps an unrestorable incipit."
    }
  ],
  "glossaryReview": [
    {
      "glossary_id": "register-and-proper-name-romanization-convention-vendidad-woh",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2",
        "Encyclopaedia Iranica, s.v. Airyana Vaējah"
      ],
      "reasoning": "Direct confirmed: a house-style convention; modern register and plain stem-form names carry no lens. The genitive 'of the Good Daitya' is grammatically correct."
    },
    {
      "glossary_id": "ellipsis-and-bracket-convention-vendidad-woh",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Central lacuna-bracket-convention-sumerian-mesopotamian-project-standard"
      ],
      "reasoning": "Direct confirmed: three marks with one function each, applied correctly at 12-14, 30, 38, 43. If the human adopts '(?)' for the v. 29/37 uncertain terms, add it here as a fourth mark."
    },
    {
      "glossary_id": "verse-numbering-geldner-vs-sbe-convention-vendidad-woh",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed)",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 vv. 6-7, 32, 40-41"
      ],
      "reasoning": "Direct confirmed against the reference: SBE's relocation of v. 7, its bracketing of v. 32 and its v. 40/41 re-division are accurately described."
    },
    {
      "glossary_id": "ahura-mazda-vocative-formula-spenishta-mainyu-datar-vendidad-woh",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 1",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. spəništa-, astuuant-"
      ],
      "reasoning": "Direct: reference renderings retained; the debated range of spəṇta- is honestly stated and the literal sense disclosed in commentary."
    },
    {
      "glossary_id": "ashavan-righteous-vocative-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. ašauuan-"
      ],
      "reasoning": "Direct: ašauuan- is the possessive of aša-; 'righteous' is a mainstream modern rendering and keeps the aša link."
    },
    {
      "glossary_id": "peres-converse-anyo-mana-other-than-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pərəs-, aniia-"
      ],
      "reasoning": "Direct: aniia- 'other' is grammatically explicit."
    },
    {
      "glossary_id": "daena-the-religion-ahuiri-zarathushtri-mazdayasni-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. daēnā-, māzdaiiasni-"
      ],
      "reasoning": "Direct: 'the Religion' is the established rendering in this context; 'Mazda-worshipping' renders the compound exactly."
    },
    {
      "glossary_id": "yima-epithets-srira-hvathwa-xshaeta-sraeshta-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. huuąθβa-, xšaēta-",
        "Christensen, Les types du premier homme et du premier roi, vol. 2 (1934), on Yima/Jamšēd"
      ],
      "reasoning": "Direct: the four epithets are lexically distinct and the xšaēta- > Jamšēd continuity is standard."
    },
    {
      "glossary_id": "mereta-bereta-daenayai-rememberer-bearer-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. mərəta-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 3"
      ],
      "reasoning": "Inferred is the right label: the root-based 'rememberer' is defensible and the residual nuance is honestly disclosed."
    },
    {
      "glossary_id": "gaetha-thratar-haretar-aiwyaxshtar-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. θrātar-, harətar-"
      ],
      "reasoning": "Direct: θrātar-/trātṛ- 'protector' is an exact cognate equation; SBE's 'nourisher/ruler' is the outlier."
    },
    {
      "glossary_id": "xshathra-rule-and-v7-berethe-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. xšaθra-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 7 '[Obscure.]'"
      ],
      "reasoning": "Direct for 'rule'; the v. 7 rendering is minimal and the clause's obscurity is disclosed in commentary."
    },
    {
      "glossary_id": "suwra-ashtra-implements-and-their-verbs-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. suβrā-, aštrā-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 vv. 6, 30, 38 with n. 4"
      ],
      "reasoning": "Inferred appropriate; transliterating suβrā- is the accuracy-first choice given SBE's own seal/ring wavering, and aštrā- 'goad' is secure. Non-blocking: attribute the 'horn / arrow or awl' proposals to named scholars or generalise the wording."
    },
    {
      "glossary_id": "pasu-staora-flocks-and-herds-gav-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pasu-, staora-"
      ],
      "reasoning": "Direct: standard pair; unification across vv. 8-35 is a fidelity gain over SBE's switch to 'sheep and oxen'."
    },
    {
      "glossary_id": "zima-winters-reckoning-hanjasenti-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. zim-"
      ],
      "reasoning": "Direct: literal unit and verb."
    },
    {
      "glossary_id": "raocah-rapithwa-path-of-sun-spenta-armaiti-invocation-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. raocah-, rapiθβā-, friθa-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 10 nn. 5-6"
      ],
      "reasoning": "Direct: acc. pl. + ā is grammatically explicit; south = midday quarter is standard."
    },
    {
      "glossary_id": "thrishva-thirds-and-zaosha-pleasure-vendidad-woh",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed) v. 19",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 19"
      ],
      "reasoning": "Direct: the v. 19 correction is a matter of the printed text."
    },
    {
      "glossary_id": "hanjamana-assembly-mainyava-yazata-sruto-airyana-vaejah-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. srūta-, mainiiauua-"
      ],
      "reasoning": "Inferred approved: the srūtō construal is grammatically required; the label honestly reflects phrasing variance among translators."
    },
    {
      "glossary_id": "aghem-zimo-evil-winters-aredvi-measure-vendidad-woh",
      "status": "revise",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pauruua-, pouru-, snaoδa-"
      ],
      "reasoning": "The winters/aredvi/Malkosan decisions are sound, but the 'literal' field ('much cloud') and wohChoice ('many clouds') treat pauruuō as pouru- 'much' and pluralise singular snaoδō, contradicting the overlay's own v. 24 ruling. Change literal to 'from which the cloud shall first snow snows' and wohChoice to 'from which the cloud shall first snow down snowflakes' (or justify 'much' explicitly)."
    },
    {
      "glossary_id": "thrizhat-third-of-cattle-v23-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. θrižat-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 23"
      ],
      "reasoning": "Inferred approved: θrižat- is in the text and SBE omits it; the escape/perish ambiguity is preserved, not resolved."
    },
    {
      "glossary_id": "v24-pasture-before-meltwater-footprint-wonder-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pauruua-, abda-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 24"
      ],
      "reasoning": "Inferred approved: pauruua- 'before' vs pouru- 'much' is lexically correct. Its pipeline wording ('the Translator…the Editor') is acceptable in a glossary audit trail but not in the reader commentary (see VID-2:24)."
    },
    {
      "glossary_id": "vara-varefshva-enclosure-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. vara-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 25"
      ],
      "reasoning": "Direct: transliteration is universal practice and the loc. pl. varəfšuua is grammatically explicit."
    },
    {
      "glossary_id": "caretu-drajah-race-course-measure-hathra-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. carətu-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 25 n. 18"
      ],
      "reasoning": "Direct: distributive phrase rendered exactly; the commentary's mile-estimate stays out of the line."
    },
    {
      "glossary_id": "taoxma-seeds-mithwaire-ajyamna-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. taoxman-, miθβara-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 28"
      ],
      "reasoning": "Direct: 'seeds' and 'in pairs' are literal; avoiding SBE's KJV-echoing 'two of every kind' is exactly the right lens discipline."
    },
    {
      "glossary_id": "vara-dwelling-hapaxes-and-zairigaona-vendidad-woh",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 26 n. 20",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. fraskəmba-"
      ],
      "reasoning": "Inferred approved: root-based glosses of hapaxes, honestly labelled conjectural. Fix the 'x'airiieiti' typo (source x'airiieite)."
    },
    {
      "glossary_id": "urvara-hvaretha-plants-foods-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. uruuarā-, x'arəθa-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 28 nn. 22-23"
      ],
      "reasoning": "Direct: general terms restored over Pahlavi-driven narrowing."
    },
    {
      "glossary_id": "exclusion-list-daxshta-of-angra-mainyu-vendidad-woh",
      "status": "flag-for-human",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. frakauua-, daxšta-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 29 n. 25"
      ],
      "reasoning": "Transparent corrections approved; the six uncertain items need a human ruling. Recommend interim option A with a visible '(?)' on each of the six in the line, and attribution to a named lexicon before any option-B physical glosses are adopted."
    },
    {
      "glossary_id": "fratema-madhema-nitema-perethu-door-window-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. pərətu-, x'āraoxšna-"
      ],
      "reasoning": "Inferred approved: superlatives and pərətu- rendered lexically; the verbless apposition is a fidelity gain over SBE's supplied 'make'."
    },
    {
      "glossary_id": "vispar-vixadh-tread-knead-soft-earth-vendidad-woh",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 31 n. 27"
      ],
      "reasoning": "Direct: no potter or clay in the Avestan; preverb vī- kept."
    },
    {
      "glossary_id": "hvadhata-stidhata-self-created-lights-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. x'aδāta-",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 40 n. 29"
      ],
      "reasoning": "Direct: transparent compound; 'uncreated' and 'artificial' are rightly confined to reception history."
    },
    {
      "glossary_id": "hakeret-once-setting-and-rising-v40-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. hakərət",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 40"
      ],
      "reasoning": "Inferred approved: hakərət = Vedic sakṛt 'once' is secure; the uncertainty of irixta- is disclosed."
    },
    {
      "glossary_id": "aiwigama-forty-years-pair-births-vendidad-woh",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. aiβi.gāma-, miθβana-"
      ],
      "reasoning": "Direct: duals and the female-male order are in the text."
    },
    {
      "glossary_id": "karshipta-bird-vi-barat-vendidad-woh",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 42 n. 34"
      ],
      "reasoning": "Direct: vī-bar- 'spread'; 'Spitama' is in the source."
    },
    {
      "glossary_id": "ahu-ratu-urvatat-nara-vendidad-woh",
      "status": "approve",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 43 n. 35"
      ],
      "reasoning": "Direct: standard pair; role-assignment rightly kept to commentary as later tradition."
    },
    {
      "glossary_id": "vara-tevah-eleppu-divinely-instructed-refuge-against-world-catastrophe-cross-corpus (PROPOSED CENTRAL, inferred)",
      "status": "revise",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 introduction ('It is difficult not to acknowledge … a Zoroastrian adaptation of the deluge')",
        "Boyce, A History of Zoroastrianism I (1975), pp. 92 ff."
      ],
      "reasoning": "Inferred is defensible: a named scholar (Darmesteter) asserts the comparison and the contested genetic status plus divergences are stated. Two fixes before apply: (1) 'stocks it with the seed of every kind in pairs (2.25-28)' should read 'stocks it with the seeds of every kind (2.25-27), the plant and food seeds in pairs (2.28)', so the rationale does not itself echo Gen 6:19 beyond what the Avestan says; (2) the CAD E page range for eleppu was not verified by the Reviewer; confirm it or cite 'CAD E s.v. eleppu' without pages."
    },
    {
      "glossary_id": "yima-yama-son-of-vivanghat-vivasvant-first-mortal-king-indo-iranian-cross-corpus (PROPOSED CENTRAL, direct)",
      "status": "approve",
      "citations": [
        "Christensen, Les types du premier homme et du premier roi, vol. 2 (1934)",
        "Lincoln, Death, War, and Sacrifice (1991), p. 28 (as cited in the avesta.org Darmesteter edition)",
        "Rigveda 10.14"
      ],
      "reasoning": "Direct confirmed: the Yima/Yama and Vīuuaŋhuuaṇt/Vivasvant correspondence is a standard datum of Indo-Iranian philology; divergent roles are honestly stated and Lincoln's comparison is reported, not adopted."
    },
    {
      "glossary_id": "vara-as-designed-preservation-habitat-woh-reading (PROPOSED CENTRAL, speculative)",
      "status": "flag-for-human",
      "citations": [
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 introduction and n. 29 ('artificial lights')",
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. vara-, taoxman-, x'aδāta-"
      ],
      "reasoning": "The rationale honestly says what the reading goes beyond (no single source; mainstream does not hold it; apparatus-only) and its lexical evidence is accurate: measured instruction (2.25), seeds selected for excellence (2.27-28), exclusions (2.29), sealed self-lit structure (2.30, 2.40), regulated births (2.41), Darmesteter n. 29 'artificial lights'. It still needs named human sign-off as a first extension of the lens into the Avestan corpus, and the phrase 'non-human authority' should be checked against the 2026-05 framing; suggested: 'on instruction from a superior authority (in the text, Ahura Mazda)'. Its glossaryRefs at VID-2:40/41 are apparatus-only and acceptable, but they attach the lens to the most technology-suggestive lines, which the human should be aware of."
    },
    {
      "glossary_id": "preservation-of-the-seed-of-humankind-and-animals-flood-aitia-cross-corpus (EXTEND appliesTo +VID-2:25,27,28,33,35,36)",
      "status": "approve",
      "citations": [
        "Bartholomae, Altiranisches Wörterbuch (1904) s.v. taoxman-",
        "Gilgamesh XI 27"
      ],
      "reasoning": "Extension sound: taoxman- 'seed' is a genuine lexical parallel. The appended sentence should note that the Avestan has no aitia (reward) clause, which is the entry's diagnostic Sumerian feature."
    },
    {
      "glossary_id": "paradise-by-negation-no-predation-no-illness-no-aging-cross-corpus (EXTEND appliesTo +VID-2:5,29,37)",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed) vv. 5, 29, 37"
      ],
      "reasoning": "v. 5 is a textbook instance; vv. 29/37 define the Vara by enumerated absence and fit, more loosely (selection rather than paradise-condition)."
    },
    {
      "glossary_id": "lacuna-bracket-convention-sumerian-mesopotamian-project-standard (EXTEND appliesTo +VID-2:12-14,30,38,43)",
      "status": "approve",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed) vv. 12-14, 43"
      ],
      "reasoning": "Approve, with the optional note recommended: in the Vendidad [ ] restores an abbreviated formula from earlier in the same text, not a reading from another manuscript witness."
    },
    {
      "glossary_id": "ab-bur-aptu-chalon-ha-tevah-flood-boat-window-cross-corpus (EXTEND appliesTo +VID-2:30,38)",
      "status": "revise",
      "citations": [
        "Geldner, Avesta (1886-96), vol. 3, Vd 2 (re-parsed) vv. 30, 38",
        "Darmesteter, SBE 4 (1880; American ed. 1898), Fargard 2 v. 30"
      ],
      "reasoning": "Do not extend. The entry is `direct` and documents a hull aperture opened or cut after the storm to observe the receded waters; the Vara's raocana- is built in at construction, self-shining, on a land enclosure, and is never opened after the catastrophe. Adding it would make a direct entry carry a loose comparandum. Drop this id from the VID-2:30/38 glossaryRefs and point the v. 30 commentary sentence to the inferred vara-tevah-eleppu entry instead (keeping its hedge 'Here the window is described as shining by itself')."
    }
  ],
  "lens-leakage-flags": [],
  "lensLeakageCheck": "Performed on all 41 paragraph objects against the re-parsed Avestan. No English line carries a Wheel of Heaven reading: no 'ark', no 'Flood', no 'two of every kind' (miθβairē is 'in pairs' at vv. 28/36), no 'habitat', 'designed', 'artificial' or 'underground'; 'Vara' is transliterated as in all Iranist practice; 'self-created lights' is the literal x'aδāta-. The one English 'flood' (v. 24) renders meltwater (āfš … vazaiδiiāi), is Darmesteter's own word and is not the Flood narrative. The Flood/ark comparison appears only in commentary (vv. 22, 25, 27, 30), hedged as comparative philology with the contested genetic status and the indigenous-winter-myth reading stated at v. 22. The WoH reading appears once, at v. 25, under an explicit 'Wheel of Heaven reading (interpretive; not part of the translation)' label.",
  "darmesteterCorrectionsCheck": "All confirmed against the re-parsed source: v. 19 θribiiō θrišuuaēibiiō 'three thirds' (SBE 'two-thirds' is an error); v. 23 θrižat- 'a third' (omitted by SBE); v. 40 hakərət 'once' (unrendered by SBE) and x'aδāta- 'self-created' (SBE 'uncreated'); vv. 6-7 numbering (Geldner v. 7 = yimō asti bərəθe xšaθraiiā̊); v. 32 in Geldner's text, rightly unbracketed. Bracket convention applied correctly at 12-14 and 43 ([ ] verbatim restoration), 30 and 38 (⟨ ⟩ supply), and 43 ('…' unrestorable incipit).",
  "escalationReportAdjustments": "Initial verdicts were formed before opening chapter-2-editor-report.md. After reading it: no per-verse verdict changed. The report added (a) the Editor's own offer to skip the ab-bur window extension, which supports the Reviewer's 'revise: do not extend'; (b) the full text of the three central proposals, which led to two concrete fixes for vara-tevah-eleppu (scope of 'in pairs'; unverified CAD page range) and confirmed the speculative entry is apparatus-only. The report's unattributed option-B glosses for the exclusion list (skin blemishes, stunted, deformed) were not verified by the Reviewer and should not be adopted without a named lexical source.",
  "summary": "41 paragraph verdicts: 35 approve, 3 revise (VID-2:22 'many clouds' contradicts the overlay's own pauruua- ruling; VID-2:24 and VID-2:30 commentary contains pipeline meta-language), 3 flag-for-human (VID-2:25 contingent on the speculative sign-off; VID-2:29/37 exclusion list). 33 overlay entries: 31 approve, 1 revise (aghem-zimo, same pauruua- point), 1 flag-for-human (exclusion list). Central proposals: yima-yama approve; vara-tevah-eleppu revise (two small fixes); vara-as-designed (speculative) flag-for-human; extensions: 3 approve, ab-bur window revise (do not extend). Escalated items: suwra transliteration approved; ⟨stroke⟩/⟨stroked⟩ approved. Translation quality is high and corrects the PD reference at every point checked. Status advanced to awaiting-human."
}
```

## Editor escalation report (inlined)

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
