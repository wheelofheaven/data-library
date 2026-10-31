# Sign-off package — Gospel of Thomas, Block A (incipit + logia 1–38)

**Status:** `awaiting-human` · `1.0.0-rc1` · central glossary 2.74.0 (+ proposals) · overlay `1.0.0`

The program's first Coptic text (NHC II,2; Dilley / Coptic Scriptorium, CC BY 4.0 source layer; English CC0). Blocks B (39–76) and C (77–114) follow; this block sets the book's binding conventions.

## Summary

| Item | Count |
|---|---|
| Units translated | 39 (n=0–38) |
| Units with commentary | 37 |
| Translator questions raised / resolved | 49 / 49 |
| Overlay entries | 39 — direct 33, inferred 5, speculative 1 |
| Central proposals | `cop` in sourceLanguages; appliesTo extensions: iēsous (35 units), kingdom-of-heaven (THOM-20), lacuna-bracket (5 units, with a Thomas-specific sentence) |
| Reviewer unit verdicts | approve 38, revise 1 |
| Lens-leakage flags | 0 |

## Items requiring decision

1. **Speculative overlay entry `woh-reading-kingdom-within-beginning-end-five-trees-thomas-woh`** (reviewer: flag-for-human). Three labelled Wheel of Heaven paragraphs in commentary at THOM-3, 18, 19; never in the English. The reviewer asks the founder whether a text the canon never cites should carry lens paragraphs at all, and requires a wording fix if kept ("a child of 'the living Father'", drop "and can become creators in turn"). **Options:** (a) keep with the fix; (b) drop the entry, the three paragraphs and three refs.
2. **"sons" for ϣⲏⲣⲉ in the filial formulas** (approved by the reviewer; the inclusive-language question is left to you). Binds Blocks B and C.
3. **Reviewer revise items (apply at ratification):**
   - THOM-3 commentary: the υἱοί of P.Oxy. 654 is "as usually restored (Attridge in Layton ed. 1989)".
   - `jitpe-mpmou-taste-death-thomas-woh`: logion 111 has a different verb ("will not see death"), not "taste"; correct the entry AND the Block B/C binding list in the editor report.
   - `shere-son-child-thomas-woh`: restate the criterion as the formula itself (ϣⲏⲣⲉ + genitive of the Father / humanity / the living one), and correct the Greek evidence (28 extant, 3 restored, 37 lost).
   - `lion-and-man-logion-7-…`: "proposed by a number of modern editors and commentators; discussed in Jackson 1985" (not "Patterson–Meyer, Plisch").
   - Central lacuna-bracket extension: only with the Thomas-specific sentence (single witness → [ ] = letters restored in a physical lacuna, papyrological usage).
   - Non-blocking: DeConick date unified to 2006.
4. **Approved, for completeness:** manuscript readings kept at the 7 (lion) and 30 (three gods) cruxes; 33 "measure" (ear/measure pun) vs matthew-woh "basket"; 21 robbers clause read as a scribal spelling of the negative (cf. 22); `cop` in sourceLanguages; iēsous and kingdom-of-heaven extensions; sower and beatitudes deliberately not extended (the central sower entry carries a Raëlian reading of Matthew that must not attach to Thomas).

## Reviewer report

```json
{
  "reviewer": "claude-opus-5-5 acting as woh-reviewer",
  "reviewedAt": "2026-10-31T20:20:46Z",
  "verdicts": [
    {
      "refId": "THOM-0",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲱⲡ",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "Re-parsed: ⲛⲁⲉⲓ ⲛⲉ ⲛ̄ϣⲁϫⲉ ⲉⲧ-ϩⲏⲡ (relative + stative of ϩⲱⲡ) ⲉⲛⲧⲁ-ⲓ︤ⲥ︥ ⲉⲧⲟⲛϩ ϫⲟⲟⲩ, ⲁϥⲥϩⲁⲓ̈-ⲥⲟⲩ ⲛ̄ϭⲓ + triple name. 'Hidden' is the literal stative; Lambdin's 'secret' follows the restored Greek ἀπόκρυφοι, as the note says. The note's date-and-setting paragraph lays out Patterson/DeConick against Gathercole/Goodacre without deciding between them. No lens."
    },
    {
      "refId": "THOM-1",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ⲁⲩⲱ ⲡⲉϫⲁϥ has no named subject, and the English correctly keeps it open (as does P.Oxy. 654 καὶ εἶπεν). ⲡⲉⲧⲁϩⲉ = Lycopolitan for ⲡⲉⲧⲛⲁϩⲉ (Dilley); 'whoever finds' is standard; 'will not taste death' is the literal idiom."
    },
    {
      "refId": "THOM-2",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Clement of Alexandria, Stromateis 2.9.45; 5.14.96"
      ],
      "reasoning": "ⲙⲛ̄ⲧⲣⲉϥⲗⲟ (normalised ⲙⲡⲣⲧⲣⲉϥⲗⲟ, negative jussive) … ϥⲛⲁϣⲧⲣ̄ⲧⲣ̄ … ϥⲛⲁⲣ̄ϣⲡⲏⲣⲉ … ϥⲛⲁⲣ̄ⲣ̄ⲣⲟ ⲉϫⲙ̄ⲡⲧⲏⲣϥ is rendered exactly. The Greek 'rest' and the missing 'troubled' stage stay in the commentary. 'The All' is capitalised as Lambdin does."
    },
    {
      "refId": "THOM-3",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲡⲉ, ϣⲏⲣⲉ"
      ],
      "reasoning": "The line is correct. ⲛⲉⲧⲥⲱⲕ ϩⲏⲧ-ⲧⲏⲩⲧⲛ̄ 'those who lead you'; ⲧⲡⲉ 'sky' twice keeps the joke (Lambdin agrees); ⲥⲙ̄ⲡⲉⲧⲛ̄ϩⲟⲩⲛ/ⲃⲁⲗ 'inside/outside you'; ⲥⲉⲛⲁⲥⲟⲩⲱⲛ-ⲧⲏⲛⲉ 'you will be known'. The source finding (diplomatic ⲉⲩϣⲁϫⲟⲟⲥ, normalised ⲉⲩϣⲁⲛϫⲟⲟⲥ) is confirmed. One commentary fix, under the Editor's own rule that restored Greek must be labelled: as far as the Reviewer can tell, υἱοί at P.Oxy. 654 l. 17 is an editorial restoration, not extant text. EXACT CHANGE in notes.official: replace \"'The sons of the living Father' keeps the υἱοί of the Greek (see `shere-son-child-thomas-woh`).\" with \"'The sons of the living Father' agrees with the Greek of P.Oxy. 654 as usually restored (υἱοί; Attridge in Layton ed. 1989) (see `shere-son-child-thomas-woh`).\" If the Editor checks Attridge and finds υἱοί extant, delete 'as usually restored'. The labelled WoH paragraph is governed by the flag on the speculative overlay entry."
    },
    {
      "refId": "THOM-4",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ϥⲛⲁϫⲛⲁⲩ ⲁⲛ … ⲉϫⲛⲉ ⲟⲩⲕⲟⲩⲉⲓ ⲛ̄ϣⲏⲣⲉ ϣⲏⲙ ⲉϥϩⲛ̄ ⲥⲁϣϥ̅ ⲛ̄ϩⲟⲟⲩ … ⲛ̄ⲥⲉϣⲱⲡⲉ ⲟⲩⲁ ⲟⲩⲱⲧ is rendered literally. The Coptic has only the first half of the proverb, and the English does not complete it from the Greek or Mk 10:31."
    },
    {
      "refId": "THOM-5",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ⲥⲟⲩⲱⲛ ⲡⲉⲧⲙ̄ⲡⲙ̄ⲧⲟ ⲙ̄ⲡⲉⲕϩⲟ ⲉⲃⲟⲗ 'what is in front of your face' is literal. The Greek clause 'buried … raised' stays out of the line."
    },
    {
      "refId": "THOM-6",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲡⲉ"
      ],
      "reasoning": "Re-parsed: ⲕⲟⲩⲱϣ ⲉⲧⲣⲛ̄ⲣ̄ⲛⲏⲥⲧⲉⲩⲉ 'do you want us to fast'; ⲉϣ ⲧⲉ ⲑⲉ ⲉⲛⲁϣⲗⲏⲗ (focalising); ⲙ̄ⲡⲉⲙⲧⲟ ⲉⲃⲟⲗ ⲛ̄ⲧⲡⲉ 'in the sight of heaven' (Lambdin). 'Heaven' here is right under the context rule. The Greek 'truth' is labelled as partly restored."
    },
    {
      "refId": "THOM-7",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Jackson, The Lion Becomes Man (SBLDS 81, 1985)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲃⲱⲧⲉ",
        "Plisch, The Gospel of Thomas: Original Text with Commentary (2008)"
      ],
      "reasoning": "The manuscript reads ⲡⲙⲟⲩⲉⲓ ⲛⲁϣⲱⲡⲉ ⲣ̄ⲣⲱⲙⲉ twice, and the English prints it with no emendation in the line. That is the program's crux rule, and it agrees with Lambdin's own rendering. The conjecture 'the man will become lion' sits only in commentary, labelled as conjecture. 'Loathsome' for the stative ϥⲃⲏⲧ (ⲃⲱⲧⲉ 'be abhorrent') is more exact than 'cursed'."
    },
    {
      "refId": "THOM-8",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939)"
      ],
      "reasoning": "Re-parsed with the normalisation (ⲉⲣⲉ ⲡⲣⲱⲙⲉ ⲧⲛ̄ⲧⲱⲛ ⲉⲩⲟⲩⲱϩⲉ …; ⲁϥϩⲉ ⲉⲩⲛⲟϭ ⲛ̄ⲧⲃⲧ). '[down]' correctly brackets ⲉ[ⲡⲉ]ⲥⲏⲧ under the bracket convention. 'Without difficulty' = ⲭⲱⲣⲓⲥ ϩⲓⲥⲉ. The English does not harmonise to Mt 13:47-48."
    },
    {
      "refId": "THOM-9",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϥⲛⲧ, ⲥⲟⲧⲉ"
      ],
      "reasoning": "ⲁϥⲙⲉϩ-ⲧⲟⲟⲧϥ 'filled his hand'; singular ⲧⲡⲉⲧⲣⲁ 'the rock'; ⲁⲡϥⲛ︤ⲧ︥ ⲟⲩⲟⲙⲟⲩ 'the worm ate them'; ⲁϥⲉⲓ ⲛ̄ⲥⲉ ⲉⲥⲟⲧⲉ 'sixty per measure' (Lambdin). There is no 'to sow' and no allegory. Matthean wording is not imported beyond the shared 'Behold, the sower went out', which is the correct presentative for ⲉⲓⲥϩⲏⲏⲧⲉ."
    },
    {
      "refId": "THOM-10",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲁⲉⲓⲛⲟⲩϫⲉ ⲛ̄ⲟⲩⲕⲱϩⲧ ⲉϫⲛ̄ⲡⲕⲟⲥⲙⲟⲥ … ϯ(ϩ)ⲁⲣⲉϩ ⲉⲣⲟϥ ϣⲁⲛⲧⲉϥϫⲉⲣⲟ is rendered literally. The source finding (diplomatic ϯⲁⲣⲉϩ, normalised ϯϩⲁⲣⲉϩ) is confirmed. Lk 12:49's 'earth' is not imported."
    },
    {
      "refId": "THOM-11",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲧⲉⲉⲓⲡⲉ … ⲁⲩⲱ ⲧⲉⲧⲛ̄ⲧⲡⲉ ⲙ̄ⲙⲟⲥ 'this heaven … and the one above it' (cosmological, so 'heaven'). The imperfects ⲛⲉⲧⲉⲧⲛ̄ⲟⲩⲱⲙ … ⲛⲉⲧⲉⲧⲛ̄ⲉⲓⲣⲉ are rendered as simple past, which is acceptable English for the habitual past. ⲁⲧⲉⲧⲛ̄ⲉⲓⲣⲉ ⲙ̄ⲡⲥⲛⲁⲩ 'you became two' (Lambdin)."
    },
    {
      "refId": "THOM-12",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (3rd ed. 2011) on focalising conversion"
      ],
      "reasoning": "ⲉⲧⲛⲁⲣ̄ⲛⲟϭ ⲉϩⲣⲁⲓ̈ ⲉϫⲱⲛ 'will be great over us' is literal. ⲉⲧⲉⲧⲛⲁⲃⲱⲕ is the focalising future, and its directive 'you are to go' follows Lambdin. 'James the Righteous' keeps the ⲇⲓⲕⲁⲓⲟⲥ concordance with 13. The inferred clause reading is defensible."
    },
    {
      "refId": "THOM-13",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲥⲁϩ, ϣⲓ"
      ],
      "reasoning": "ⲧⲛ̄ⲧⲱⲛⲧ … ⲉⲉ⟨ⲓ⟩ⲛⲉ ⲛ̄ⲛⲓⲙ; 'Teacher' = ⲥⲁϩ in both places, which keeps the point of the exchange (Lambdin has 'Master'); ⲛ̄ⲧⲁⲉⲓϣⲓⲧⲥ 'that I have measured out' (Lambdin; ϣⲓ 'measure'). ⲉⲡⲉⲓ ⲁⲕⲥⲱ ⲁⲕϯϩⲉ is rendered 'for you have drunk, you have become drunk', which is acceptable. The ⟨ ⟩ letters are rendered silently, as the convention allows."
    },
    {
      "refId": "THOM-14",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϫⲡⲟ"
      ],
      "reasoning": "ⲧⲉⲧⲛⲁϫⲡⲟ ⲛⲏⲧⲛ̄ ⲛ̄ⲟⲩⲛⲟⲃⲉ 'beget a sin'; ⲥⲉⲛⲁⲣ̄ⲕⲁⲧⲁⲕⲣⲓⲛⲉ ⲙ̄ⲙⲱⲧⲛ̄ as impersonal → passive; ⲛ̄ⲛⲉⲧⲙ(=ⲛ)ⲡ︤ⲛ︥︤ⲁ︥ 'your spirits', lower case. The source finding about the stray U+0027 is confirmed in `text`. The Lk 10 / Mk 7 parallels are not imported."
    },
    {
      "refId": "THOM-15",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲡⲉⲧⲉⲙ̄ⲡⲟⲩϫⲡⲟϥ ⲉⲃⲟⲗ ϩⲛ̄ⲧⲥϩⲓⲙⲉ as passive 'not born of woman' is standard. The prostration formula is literal. 'Father' is capitalised for the divine referent."
    },
    {
      "refId": "THOM-16",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Klijn, 'The \"Single One\" in the Gospel of Thomas', JBL 81 (1962)"
      ],
      "reasoning": "ⲧⲁⲭⲁ, ⲡⲱⲣϫ 'divisions', fire/sword/war; ⲛⲁϣⲱ[ⲡⲉ] gives '[be]', partly restored and correctly bracketed; ⲉⲩⲟ ⲙ̄ⲙⲟⲛⲁⲭⲟⲥ 'as solitary ones' with no anachronistic 'monks'. The Luke/Matthew wording is not imported."
    },
    {
      "refId": "THOM-17",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Coptic ⲙ̄ⲡⲉϥⲉⲓ ⲉϩⲣⲁⲓ̈ ϩⲓⲫⲏⲧ ⲣ̄ⲣⲱⲙⲉ 'has not come up into the heart of man' is literal. The added 'hand has not touched' is kept, and 1 Cor 2:9 wording is not imposed."
    },
    {
      "refId": "THOM-18",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲁⲏ"
      ],
      "reasoning": "ⲁⲧⲉⲧⲛ̄ϭⲱⲗⲡ ⲅⲁⲣ ⲉⲃⲟⲗ ⲛ̄ⲧⲁⲣⲭⲏ … ϫⲉ ϩⲙ̄ⲡⲙⲁ ⲉⲧⲉ ⲧⲁⲣⲭⲏ ⲙ̄ⲙⲁⲩ ⲉⲑⲁϩⲏ ⲛⲁϣⲱⲡⲉ ⲙ̄ⲙⲁⲩ is rendered exactly. The source findings (ⲧⲛ̄ϩⲁⲏ → ⲧⲉⲛϩⲁⲏ; rasura in ⲥⲟⲩⲱⲛⲑϩⲁⲏ) are confirmed. The colon for ⲁⲩⲱ before 'he will know' is a tolerable English choice. The labelled WoH paragraph is governed by the speculative-entry flag; the English line carries no lens."
    },
    {
      "refId": "THOM-19",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939)"
      ],
      "reasoning": "ⲟⲩⲙⲁⲕⲁⲣⲓⲟⲥ ⲡⲉⲛⲧⲁϩϣⲱⲡⲉ ϩⲁⲧⲉϩⲏ ⲉⲙⲡⲁⲧⲉϥϣⲱⲡⲉ; ⲛⲉⲉⲓⲱⲛⲉ ⲛⲁⲣ̄ⲇⲓⲁⲕⲟⲛⲉⲓ; ϯⲟⲩ ⲛ̄ϣⲏⲛ ϩⲙ̄ⲡⲁⲣⲁⲇⲓⲥⲟⲥ … ⲛ̄ϣⲱⲙ ⲙ̄ⲡⲣⲱ are all rendered literally. 'Paradise' is the LXX term and carries no lens. The labelled WoH paragraph is governed by the speculative-entry flag."
    },
    {
      "refId": "THOM-20",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲧⲁⲣ"
      ],
      "reasoning": "The plural ⲛ̄ⲙ̄ⲡⲏⲩⲉ is kept as 'the heavens', consistent with matthew-woh and with Thomas 54 and 114. ⟨ⲥ⟩ⲥⲟⲃ︤ⲕ︥ is rendered silently; 'a great branch' (ⲧⲁⲣ) and 'tilled' soil are Thomas's own, not Mt/Lk's 'tree'. 'Birds of the sky' follows the context rule."
    },
    {
      "refId": "THOM-21",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (3rd ed. 2011) on the negative optative ⲛ̄ⲛⲉ-",
        "Crum, A Coptic Dictionary (1939) s.v. ⲭⲣⲉⲓⲁ"
      ],
      "reasoning": "Re-parsed in full. The robbers clause ϣⲓⲛⲁ ϫⲉ ⲛⲉ-ⲛ̄ⲗⲏⲥⲧⲏⲥ ϩⲉ ⲉϩⲓⲏ can only be negative purpose (Lambdin 'lest'), so printing it unbracketed is justified. The same scribe writes the negative optative ⲛ̄ⲛⲉ- with a single ⲛ in 22 (ϫⲉⲕⲁⲁⲥ ⲛⲉⲫⲟⲟⲩⲧ, which the corpus itself normalises to ⲛⲛⲉ ⲡϩⲟⲟⲩⲧ). This is a manuscript spelling, not an emendation. 'His house of his domain' (Lambdin) and 'they will find it' (object ⲉⲣⲟⲥ) are both exact."
    },
    {
      "refId": "THOM-22",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Klijn, JBL 81 (1962)"
      ],
      "reasoning": "ⲉⲩϫⲓ ⲉⲣⲱⲧⲉ 'being nursed'; ⲉⲧⲉⲧⲛ̄ϣⲁⲣ̄ ⲡⲥⲛⲁⲩ ⲟⲩⲁ; ⲡⲥⲁ ⲛ̄ⲧⲡⲉ / ⲡⲥⲁ ⲙ̄ⲡⲓⲧⲛ̄ 'upper/lower side'; ϣⲓⲛⲁ + focalising future 'and so that you make'; ⲙ̄ⲡⲓⲟⲩⲁ ⲟⲩⲱⲧ 'the single one'; ϫⲉⲕⲁⲁⲥ ⲛⲉ(ⲛⲛⲉ)-ⲫⲟⲟⲩⲧ negative optative. '[the kingdom]' is correctly bracketed. The source findings (span count; ⲙ̄ⲫⲟ·ⲟⲩⲧ dot) are confirmed."
    },
    {
      "refId": "THOM-23",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ϯⲛⲁⲥⲉⲧⲡ-ⲧⲏⲛⲉ ⲟⲩⲁ ⲉⲃⲟⲗ ϩⲛ̄ ϣⲟ … ⲥⲛⲁⲩ ⲉⲃⲟⲗ ϩⲛ̄ ⲧⲃⲁ is literal. The shift to 'they' is in the Coptic and is kept."
    },
    {
      "refId": "THOM-24",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "There is no ⲉⲥⲱⲧⲙ̄ in this hearing formula, and the English correctly omits 'to hear'. The ϥ- of ϥⲣ̄ⲟⲩⲟⲉⲓⲛ is ambiguous: 'he' is printed and 'it' is given in commentary, as Lambdin prints both. Unsmoothed."
    },
    {
      "refId": "THOM-25",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939)"
      ],
      "reasoning": "ⲙⲉⲣⲉ ⲡⲉⲕⲥⲟⲛ ⲛ̄ⲑⲉ ⲛ̄ⲧⲉⲕⲯⲩⲭⲏ 'as your soul' is not harmonised to 'as yourself'. ⲧⲉⲗⲟⲩ ⲙ̄ⲡⲉⲕⲃⲁⲗ 'the pupil of your eye' is literal."
    },
    {
      "refId": "THOM-26",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "The Coptic order (speck in your brother's eye seen; beam in yours not seen) is kept. ⲛⲁⲩ ⲉⲃⲟⲗ 'see clearly' is standard."
    },
    {
      "refId": "THOM-27",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "Correctly no 'Jesus said' (absent in Coptic, present in P.Oxy. 1). ⲛⲏⲥⲧⲉⲩⲉ ⲉⲡⲕⲟⲥⲙⲟⲥ 'fast from the world'; ⲉⲓⲣⲉ ⲙ̄ⲡⲥⲁⲃⲃⲁⲧⲟⲛ ⲛ̄ⲥⲁⲃⲃⲁⲧⲟⲛ 'keep the Sabbath as Sabbath'. 'The kingdom' is kept, not the Greek 'of God'."
    },
    {
      "refId": "THOM-28",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ⲁⲉⲓⲱϩⲉ ⲉⲣⲁⲧ … ⲁⲉⲓⲟⲩⲱⲛϩ ⲉⲃⲟⲗ ⲛⲁⲩ ϩⲛ̄ ⲥⲁⲣⲝ; ⲛ̄ϣⲏⲣⲉ ⲛ̄ⲣ̄ⲣⲱⲙⲉ 'sons of men' (the Greek υἱοῖς τῶν ἀνθρώπων is extant). ⲛⲉϩ-ⲡⲟⲩⲏⲣⲡ 'shake off their wine'. Literal throughout."
    },
    {
      "refId": "THOM-29",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ⲉϣϫⲉ … ⲟⲩϣⲡⲏⲣⲉ ⲧⲉ … ⲟⲩϣⲡⲏⲣⲉ ⲛ̄ϣⲡⲏⲣⲉ ⲡⲉ; ⲥⲁⲣⲝ and ⲥⲱⲙⲁ are kept distinct; '[how]' brackets ⲡⲱ[ⲥ]. Correct."
    },
    {
      "refId": "THOM-30",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Grenfell & Hunt, The Oxyrhynchus Papyri (P.Oxy. 1, 654, 655)"
      ],
      "reasoning": "ⲡⲙⲁ ⲉⲩⲛ̄ ϣⲟⲙⲧ ⲛ̄ⲛⲟⲩⲧⲉ ⲙ̄ⲙⲁⲩ ϩⲛ̄ⲛⲟⲩⲧⲉ ⲛⲉ is the manuscript reading, and the English prints it unemended (as Lambdin does). The Greek θεοί/ἄθεοι (restored) and the stone/wood sentence (Coptic 77b) are kept in commentary. Mt 18:20 is not imported."
    },
    {
      "refId": "THOM-31",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ⲙⲛ̄ ⲡⲣⲟⲫⲏⲧⲏⲥ ϣⲏⲡ 'is accepted'; ϩⲙ̄ⲡⲉϥϯⲙⲉ 'in his village' (not Luke's 'hometown'); negative aorist ⲙⲁⲣⲉ- 'does not heal'. Exact."
    },
    {
      "refId": "THOM-32",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ⲉⲩⲕⲱⲧ ⲙ̄ⲙⲟⲥ … ⲉⲥⲧⲁϫⲣⲏⲩ 'being built … and fortified'. The source finding is confirmed: diplomatic ⲥⲛⲁϣϩⲱⲡ ⲁⲛ, while the corpus normalisation ⲟⲛ is a normalisation choice. The English follows the manuscript."
    },
    {
      "refId": "THOM-33",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲙⲁⲁϫⲉ (ear) and ⲙⲁ(ⲁ)ϫⲉ (dry measure)",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "The manuscript sequence ϩⲙ̄ⲡⲉⲕⲙⲁⲁϫⲉ ϩⲙ̄ⲡⲕⲉⲙⲁⲁϫⲉ is kept, and P.Oxy. 1 'in your one ear' supports a real two-ear contrast. ϩⲁ ⲙⲁⲁϫⲉ 'under a measure' is the literal sense of the Coptic noun (a dry measure, like μόδιος). The pun on the same noun in one saying justifies diverging from matthew-woh 'basket', which renders a different source word."
    },
    {
      "refId": "THOM-34",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲟⲩⲃⲗ̄ⲗⲉ ⲉϥϣⲁⲛⲥⲱⲕ ϩⲏⲧϥ̄ ⲛ̄ⲟⲩⲃⲗ̄ⲗⲉ ϣⲁⲩϩⲉ ⲙ̄ⲡⲉⲥⲛⲁⲩ ⲉⲡⲉⲥⲏⲧ ⲉⲩϩⲓⲉⲓⲧ is rendered exactly. No commentary is needed."
    },
    {
      "refId": "THOM-35",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲙⲛ̄ϭⲟⲙ ⲛ̄ⲧⲉ ⲟⲩⲁ … ⲛ̄ϥϫⲓⲧϥ̄ ⲛ̄ϫⲛⲁϩ ⲉⲓⲙⲏⲧⲓ ⲛ̄ϥⲙⲟⲩⲣ ⲛ̄ⲛⲉϥϭⲓϫ … ϥⲛⲁⲡⲱⲱⲛⲉ ⲉⲃⲟⲗ 'ransack' (Lambdin). Thomas's 'binds his hands' is kept against Mark's 'binds the strong man'."
    },
    {
      "refId": "THOM-36",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "Lycopolitan prohibitive ⲙⲛ̄ϥⲓⲣⲟⲟⲩϣ; ⲡⲉ⟨ⲧ⟩ⲉⲧⲛⲁⲧⲁⲁϥ ϩⲓⲱⲧ-ⲧⲏⲩⲧⲛ̄ 'what you will put on'. The short Coptic form is kept, and the long Greek (P.Oxy. 655) stays in commentary only."
    },
    {
      "refId": "THOM-37",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲓⲡⲉ"
      ],
      "reasoning": "Re-parsed: ϩⲟⲧⲁⲛ ⲉⲧⲉⲧⲛ̄ϣⲁⲕⲉⲕ-ⲧⲏⲩⲧⲛ̄ ⲉϩⲏⲩ ⲙ̄ⲡⲉⲧⲛ̄ϣⲓⲡⲉ, where ⲙ̄ⲡⲉ- is the negative perfect, so 'without being ashamed'. The Greek μὴ αἰσχυνθῆτε agrees, so 'strip off your shame' is not required. ⲧⲟⲧ[ⲉ] [ⲧⲉⲧⲛ̄]ⲁⲛⲁⲩ gives '[then you will]', correctly bracketed. 'The son of the living one' is lower case and not the 'Son of Man' formula. Manuscript reading kept."
    },
    {
      "refId": "THOM-38",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "ϩⲁϩ ⲛ̄ⲥⲟⲡ ⲁⲧⲉⲧⲛ̄ⲣ̄ⲉⲡⲓⲑⲩⲙⲉⲓ … ⲙⲛ̄ⲧⲏⲧⲛ̄ ⲕⲉⲟⲩⲁ ⲉⲥⲟⲧⲙⲟⲩ ⲛ̄ⲧⲟⲟⲧϥ … ⲟⲩⲛ̄ ϩⲛ̄ϩⲟⲟⲩ ⲛⲁϣⲱⲡⲉ is rendered literally."
    }
  ],
  "glossaryReview": [
    {
      "glossary_id": "register-sayings-format-and-proper-names-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. This is a house-style convention. The no-harmonisation clause was checked verse by verse and holds (27 with no formula, 31 'village', 25 'as your soul', 20 'branch', 36 short form)."
    },
    {
      "glossary_id": "restored-text-bracket-and-sigla-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Leiden conventions as used in Dilley's edition (source siglaNote)"
      ],
      "reasoning": "Direct confirmed. The mechanical rule is applied correctly at 8, 16, 22, 29 and 37, and the silent rendering of ⟨ ⟩/( ) letter supplies is right. Its rationale says it 'adopts' the central [ ]/⟨ ⟩ distinction, but in Thomas [ ] means a single-witness conjectural restoration (Leiden sense), not the central 'restored from another witness'. See the central-proposal revise below; no change is needed in the overlay itself."
    },
    {
      "glossary_id": "nomina-sacra-and-abbreviation-expansion-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. Silent expansion of ⲓ︤ⲥ︥/ⲓⲏ︤ⲥ︥/ⲡ︤ⲛ︥︤ⲁ︥ and non-sacral contractions (ⲧⲃ︤ⲧ︥, ϩⲏⲃ︤ⲥ︥, ϥⲛ︤ⲧ︥) is universal editorial practice; `text` keeps the overlines."
    },
    {
      "glossary_id": "greek-loanword-rendering-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton, A Coptic Grammar (3rd ed. 2011)"
      ],
      "reasoning": "Direct confirmed. Greek loans are ordinary Sahidic vocabulary; translating them is standard and lens-neutral."
    },
    {
      "glossary_id": "coptic-base-text-and-oxyrhynchus-greek-witnesses-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Grenfell & Hunt, The Oxyrhynchus Papyri (P.Oxy. 1, 654, 655)",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. The Coptic is in the line throughout, and every Greek divergence I checked (2, 3, 4, 5, 6, 27, 30, 31, 33, 36) is in commentary and labelled as restored where it is."
    },
    {
      "glossary_id": "shaje-ethep-hidden-sayings-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲱⲡ",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. ϩⲏⲡ is the stative of ϩⲱⲡ, and 'hidden' at every occurrence (0, 5, 6, 33) is literal."
    },
    {
      "glossary_id": "etonh-the-living-lowercase-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. ⲉⲧⲟⲛϩ is an ordinary relative stative, and Lambdin also has lower-case 'the living one'. Forward references 52, 59 and 111 were verified in the source."
    },
    {
      "glossary_id": "didymos-judas-thomas-name-thomas-woh",
      "status": "approve",
      "citations": [
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. The triple name is in the Coptic, and the Greek 'Judas who is also Thomas' is correctly labelled as restored."
    },
    {
      "glossary_id": "hermeneia-interpretation-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed: standard rendering of ϩⲉⲣⲙⲏⲛⲉⲓⲁ."
    },
    {
      "glossary_id": "jitpe-mpmou-taste-death-thomas-woh",
      "status": "revise",
      "citations": [
        "Source-cop-1.json, THOM-111 (ϥⲛⲁⲛⲁⲩ ⲁⲛ ⲉⲙⲟⲩ)",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "The forward reference is wrong. Logion 111 reads ϥⲛⲁⲛⲁⲩ ⲁⲛ ⲉⲙⲟⲩ 'will not SEE death' (ⲛⲁⲩ, not ϫⲓϯⲡⲉ). Binding 'taste' at 111 would harmonise Block C against the Coptic. EXACT CHANGE in wohChoice: replace \"(THOM-1, 18, 19; later 85, 111)\" with \"(THOM-1, 18, 19; later 85). Logion 111 has a different verb, ϥⲛⲁⲛⲁⲩ ⲁⲛ ⲉⲙⲟⲩ, rendered 'will not see death'.\" The same correction is needed in the editor report's binding list for Blocks B/C ('will not taste death' (85, 111) → (85); 111 'will not see death')."
    },
    {
      "glossary_id": "ptirf-the-all-reign-over-the-all-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. 'The All' is Lambdin's established rendering of ⲡⲧⲏⲣϥ."
    },
    {
      "glossary_id": "mntero-the-kingdom-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed, including Lambdin's 'domain' at 21 with the lexical identity kept in commentary."
    },
    {
      "glossary_id": "tpe-sky-heaven-context-rule-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲡⲉ",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Inferred confirmed. ⲡⲉ covers sky and heaven (Crum), and Lambdin uses 'sky' at 3. The split is a context judgement and is honestly labelled. Each assignment was checked (3/9/20 sky; 6/11/12 heaven)."
    },
    {
      "glossary_id": "shere-son-child-thomas-woh",
      "status": "revise",
      "citations": [
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Grenfell & Hunt, The Oxyrhynchus Papyri (P.Oxy. 1, 654, 655)",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲏⲣⲉ",
        "matthew-woh 5:45"
      ],
      "reasoning": "'Sons' is philologically defensible and matches matthew-woh, so the choice is approved. The rationale overstates the Greek: P.Oxy. 1 at 28 has υἱοῖς extant; at 3, υἱοί is (to the Reviewer's knowledge) restored; at 37 the Greek ending in P.Oxy. 655 is lost, so the entry cannot claim a Greek υἱός there. Also, the criterion 'where the Greek witness has υἱοί' cannot decide Blocks B/C (no Greek after 39 except 77b). EXACT CHANGES: (1) in wohChoice replace \"'sons' where Thomas uses the inherited filial formulas and the Greek witness has υἱοί:\" with \"'sons' in the filial formulas (ϣⲏⲣⲉ + genitive of the Father, of humanity, or of 'the living one'):\"; (2) in rationale replace \"For the filial formulas the Greek witnesses, which are earlier, have υἱοί / υἱοῖς,\" with \"For the filial formulas the earlier Greek, where it survives, has υἱοῖς (P.Oxy. 1 at 28, extant) and is restored with υἱοί at 3 (P.Oxy. 654); at 37 the Greek is lost,\". The inclusive-register question ('children') stays open for the human reviewer as the Editor framed it."
    },
    {
      "glossary_id": "eiot-father-capitalisation-thomas-woh",
      "status": "approve",
      "citations": [
        "matthew-woh 5:45; 6:26"
      ],
      "reasoning": "Direct confirmed. This is a typographic convention matching the program's NT practice, and it carries no lens."
    },
    {
      "glossary_id": "mnthke-poverty-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲏⲕⲉ"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "oua-ouot-a-single-one-thomas-woh",
      "status": "approve",
      "citations": [
        "Klijn, JBL 81 (1962)",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. 'A single one' is literal for ⲟⲩⲁ ⲟⲩⲱⲧ (Lambdin uses it at 4 and 23); keeping it at 22 avoids the interpretive 'one and the same'."
    },
    {
      "glossary_id": "topos-ma-place-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "rome-man-human-person-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. The generic 'man' follows matthew-woh, and 'human' for predicative ⲣ̄ⲣⲱⲙⲉ at 7 is exact."
    },
    {
      "glossary_id": "makarios-blessed-singular-formula-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. Not extending the central beatitudes entry to 7, 18 and 19 is correct: those sayings have no synoptic counterpart."
    },
    {
      "glossary_id": "lion-and-man-logion-7-manuscript-reading-thomas-woh",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Jackson, The Lion Becomes Man (1985)",
        "Patterson & Meyer, Scholars Version, in The Complete Gospels (1992/1994)"
      ],
      "reasoning": "Keeping the manuscript reading in the line is approved. The standardEnglish attribution, however, appears inaccurate: to the Reviewer's knowledge the Scholars Version (Patterson–Meyer) keeps the transmitted text ('… and the lion still will become human'), and the Reviewer cannot confirm Plisch's choice. EXACT CHANGE in standardEnglish: replace \"emendation 'and the man will become lion' (many modern translations, e.g. Patterson–Meyer, Plisch)\" with \"emendation 'and the man will become lion' (proposed by a number of modern editors and commentators; discussed in Jackson 1985)\". Do not name individual translators without checking them."
    },
    {
      "glossary_id": "sower-parable-coptic-form-and-eisheete-behold-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "matthew-woh 13:3"
      ],
      "reasoning": "Direct confirmed. The Thomas form is kept, and the central sower entry (which carries a Raëlian-canon reading of Matthew's text) is correctly not applied."
    },
    {
      "glossary_id": "kosmos-world-kah-earth-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲕⲁϩ"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "ouoein-light-man-of-light-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed, and the 24 ambiguity is stated in commentary."
    },
    {
      "glossary_id": "iakobos-pdikaios-james-the-righteous-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (3rd ed. 2011) on focalising conversion",
        "Eusebius, Hist. eccl. 2.23"
      ],
      "reasoning": "Inferred confirmed. Lambdin's 'you are to go' supports the directive reading of the focalising future."
    },
    {
      "glossary_id": "logion-13-sah-angelos-pege-vocabulary-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲥⲁϩ, ϣⲓ",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. 'Measured out' is literal (Lambdin), and 'Teacher' for ⲥⲁϩ is lexically exact."
    },
    {
      "glossary_id": "pneuma-sarx-soma-spirit-flesh-body-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "jpo-not-born-of-woman-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "monachos-solitary-thomas-woh",
      "status": "approve",
      "citations": [
        "Klijn, JBL 81 (1962)",
        "Gathercole, The Gospel of Thomas: Introduction and Commentary (2014)",
        "DeConick, The Original Gospel of Thomas in Translation (2006)"
      ],
      "reasoning": "Inferred confirmed. The meaning of ⲙⲟⲛⲁⲭⲟⲥ in Thomas is debated in the named commentaries, and 'solitary ones' is Lambdin-adjacent and avoids 'monks'. Housekeeping: the DeConick date (2007 here and in oua-ouot / THOM-18; 2006 at THOM-0) should be made consistent."
    },
    {
      "glossary_id": "arche-hae-beginning-end-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "five-trees-in-paradise-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "LXX Gen 2:8"
      ],
      "reasoning": "Direct confirmed. The rendering is literal and carries no lens."
    },
    {
      "glossary_id": "mariham-name-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. ⲙⲁⲣⲓϩⲁⲙ is the manuscript spelling, and the identification sits in commentary only."
    },
    {
      "glossary_id": "logion-21-robbers-clause-and-chreia-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (3rd ed. 2011) on the negative optative ⲛ̄ⲛⲉ-"
      ],
      "reasoning": "Inferred confirmed, with stronger support than the entry gives. At 22 the same scribe writes the negative optative ⲛ̄ⲛⲉ- with a single ⲛ (ϫⲉⲕⲁⲁⲥ ⲛⲉⲫⲟⲟⲩⲧ ⲣ̄ϩⲟⲟⲩⲧ, normalised by the corpus itself to ⲛⲛⲉ ⲡϩⲟⲟⲩⲧ). The unbracketed negative at 21 is therefore a reading of a spelling, not an emendation. Optional addition to the rationale: \"The same single-ⲛ spelling of ⲛ̄ⲛⲉ- occurs at 22 (ϫⲉⲕⲁⲁⲥ ⲛⲉⲫⲟⲟⲩⲧ), where the corpus normalises it as negative.\""
    },
    {
      "glossary_id": "eikon-image-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "psyche-soul-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed. Not harmonising to 'as yourself' is correct."
    },
    {
      "glossary_id": "logion-27-fast-from-the-world-sabbath-as-sabbath-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "three-gods-logion-30-manuscript-reading-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)"
      ],
      "reasoning": "Direct confirmed. The line prints the manuscript text, and the restored Greek key word is labelled as restored."
    },
    {
      "glossary_id": "other-ear-and-maaje-measure-logion-33-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲙⲁⲁϫⲉ / ⲙⲁϫⲉ",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "matthew-woh 5:15"
      ],
      "reasoning": "Inferred confirmed. The Coptic noun means a dry measure as well as an ear, and the cross-text difference from matthew-woh 'basket' rests on different source words."
    },
    {
      "glossary_id": "woh-reading-kingdom-within-beginning-end-five-trees-thomas-woh",
      "status": "flag-for-human",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "TBWTT ch. 1 (Genesis creation and Eden read as the Elohim's work)"
      ],
      "reasoning": "Speculative test applied. The cited Coptic (3, 18, 19) is accurate, the entry has no effect on any English line, and the commentary paragraphs are labelled and honestly limited (3 denies support for a sky-located kingdom; 18 says the saying is not about cosmic cycles; 19 says the canon does not cite the saying). One inaccuracy needs fixing before sign-off. EXACT CHANGE in wohChoice: replace \"as recognising oneself as a child of the creating Father\" with \"as recognising oneself as a child of 'the living Father'\" (Thomas 3 says 'living', not 'creating'), and drop \", and can become creators in turn\" (the THOM-3 commentary paragraph does not say it). Flagged rather than approved because putting lens paragraphs into a text the canon never cites, in the program's first Coptic book (binding Blocks B/C), is a project-stance call for the founder. The removal path is one decision, as the entry states."
    },
    {
      "glossary_id": "CENTRAL proposal 0: add 'cop' to sourceLanguages + scopeNote line (v2.75.0)",
      "status": "approve",
      "citations": [
        "Source-cop-1.json source.type 'coptic-sahidic'"
      ],
      "reasoning": "Mechanical and correct."
    },
    {
      "glossary_id": "CENTRAL proposal 1a: extend iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus to 35 THOM refIds",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Verified: the 35 listed units are exactly those containing ⲓ︤ⲥ︥/ⲓⲏ︤ⲥ︥ (1, 8, 24 and 27 correctly excluded), and they match the chapter glossaryRefs. 'Jesus' is the entry's surface rendering, and the extension is lens-neutral."
    },
    {
      "glossary_id": "CENTRAL proposal 1b: extend kingdom-of-heaven-basileia-tōn-ouranōn-… to THOM-20",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ is plural, so 'the kingdom of the heavens' fits. The optional sentence ('also occurs in Coptic Thomas (20, 54, 114), so it is not exclusively Matthean') is recommended, because the entry's id calls the phrase Matthean-distinctive."
    },
    {
      "glossary_id": "CENTRAL proposal 1c: extend lacuna-bracket-convention-sumerian-mesopotamian-project-standard to THOM-8, 16, 22, 29, 37",
      "status": "revise",
      "citations": [
        "Central entry rationale (ETCSL: [word] = 'restored from another manuscript witness'; <word> = conjectural editorial supply)",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "As written, the central [word] means 'other manuscripts have it'. Thomas has one witness, so its [ ] are conjectural Leiden-style restorations of physical lacunae, which the central definition would class as <word>. Extending appliesTo without a note would tell readers that '[down]' or '[the kingdom]' is attested elsewhere. EXACT CHANGE: extend appliesTo only together with an adoption sentence appended to the rationale (the same pattern as the existing Vendidad sentence): \"Adopted for the Gospel of Thomas (gospel-of-thomas-woh overlay): NHC II,2 is the only Coptic witness, so [ ] there follows papyrological (Leiden) usage and encloses English words standing on letters restored by modern editors in a physical lacuna, from context or occasionally from the Greek fragments; ⟨ ⟩ remains reserved for English words supplied where no source wording exists.\" If the orchestrator does not want a rationale change at a minor bump, do not extend and leave the convention overlay-only."
    },
    {
      "glossary_id": "CENTRAL non-extension: parable-of-the-sower-mt-13-3-23-raelian-panspermia-… not applied to THOM-9",
      "status": "approve",
      "citations": [
        "matthew-woh 13:3",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Correct. The entry governs Matthew's wording ('to sow', 'rocky ground'), which Thomas lacks, and it carries a Raëlian-canon reception of Matthew that must not be attached to an uncited text. The overlay records the Thomas form."
    },
    {
      "glossary_id": "CENTRAL non-extension: beatitudes-mt-5-3-12-… not applied to THOM-7, 18, 19",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Correct, because these are singular, non-synoptic macarisms. The recommendation to extend it to Thomas's synoptic-parallel beatitudes (54, 68, 69) in Blocks B/C is sound."
    }
  ],
  "lens-leakage-flags": [],
  "lensLeakageCheck": "Performed on all 39 English lines against the re-parsed Coptic (diplomatic text plus the Coptic Scriptorium normalisation and lemma layer). No English line carries a Wheel of Heaven reading. There is no 'Elohim', 'creators', 'planet', 'messenger' or capitalised 'Living One'. 'Sky' at 3, 9 and 20 is a context decision that cuts against a sky-located kingdom (3). 'Paradise' at 19 is the LXX term. No canonical-gospel wording was imported where the Coptic differs: 9 (no 'to sow', singular rock, worm), 20 (branch, not tree), 25 ('as your soul'), 27 (no 'Jesus said'), 31 ('village'), 35 ('binds his hands'), 36 (short form). The hard sayings keep the manuscript reading in the line: 7 ('the lion will become human' twice), 21 (negative robbers clause, a manuscript spelling paralleled at 22), 30 ('three gods … gods'), 37 ('without being ashamed'; '[then you will]' bracketed). Emendations and the Greek appear only in commentary. The lens appears in exactly three labelled paragraphs (3, 18, 19) pointing to the single speculative overlay entry.",
  "sourceFindingsCheck": "All seven Translator/Editor source findings were confirmed against source-cop-1.json and the lemma aid: 3 (ⲉⲩϣⲁϫⲟⲟⲥ → ⲉⲩϣⲁⲛϫⲟⲟⲥ), 8 (one bracket against two supplied spans; ⲁⲩ- → ⲉⲩ-), 10 (ϯⲁⲣⲉϩ → ϯϩⲁⲣⲉϩ), 14 (stray U+0027 before ⲛ̄ⲧⲉⲧⲙ̄ⲙⲟⲟϣⲉ), 18 (ⲧⲛ̄ϩⲁⲏ → ⲧⲉⲛϩⲁⲏ; rasura in ⲥⲟⲩⲱⲛⲑϩⲁⲏ), 22 (two brackets against six spans; ⲙ̄ⲫⲟ·ⲟⲩⲧ), 32 (diplomatic ⲁⲛ, normalised ⲟⲛ). The chapter `text` is byte-identical to source-cop-1.json for n=0–38. Conventions verified: [ ] at 8, 16, 22, 29 and 37 only; nomina sacra expanded silently; sky/heaven rule applied consistently; 'sons' only in the filial formulas (3, 28, 37), 'little child(ren)' for ϣⲏⲣⲉ ϣⲏⲙ (4, 21, 37).",
  "escalationReportAdjustments": "Initial verdicts were formed before opening chapter-1-editor-report.md. After reading it, no per-unit verdict changed. The report added three things. (a) Its binding Blocks B/C list repeats \"'will not taste death' (85, 111)\", so the jitpe-mpmou revise now also asks for that list to be corrected (111 = 'will not see death'). (b) The 'sons' escalation looks ahead to Block B (logion 50), which exposed that the overlay's Greek-based criterion cannot decide sayings with no Greek; the shere-son-child revise now restates the criterion as the filial-formula pattern. (c) The text of the CENTRAL proposals: the lacuna-bracket extension was checked against the central rationale and found to conflict with its 'another witness' definition (revise: add an adoption sentence or keep the convention overlay-only); the other proposals and both deliberate non-extensions are approved.",
  "summary": "39 unit verdicts: 38 approve, 1 revise (THOM-3: the commentary should label Greek υἱοί as restored), 0 flag-for-human. 39 overlay entries: 35 approve, 3 revise (jitpe-mpmou: 111 is 'see death', not 'taste'; shere-son-child: Greek υἱοί claim overstated at 3 and 37, criterion restated for Blocks B/C; lion-and-man: Patterson–Meyer attribution appears wrong), 1 flag-for-human (the speculative WoH-reading entry, with a 'creating' → 'living' Father wording fix). Central proposals: add 'cop' approve; iēsous extension approve; kingdom-of-heaven → THOM-20 approve; lacuna-bracket extension revise (add Thomas adoption sentence or keep overlay-only); sower and beatitudes non-extensions approve. Escalated items: 7/30 manuscript readings approved; 'sons' approved (register question left open for the human); 33 'measure' approved; 21 unbracketed negative approved (supported by the same spelling at 22). Lens leakage: none in the English. Housekeeping (non-blocking): make the DeConick date consistent (2006 at THOM-0, 2007 at THOM-18 and two overlay entries). Translation quality is high: literal, unsmoothed, and faithful to the Coptic at every point checked. Status advanced to awaiting-human."
}
```

## Editor escalation report (inlined)

# Chapter 1 Editor Report — Gospel of Thomas, Block A (incipit and logia 1-38)

## Overview

This is the program's first Coptic-source text.
Block A covers the incipit (THOM-0) and logia 1-38 of Nag Hammadi Codex II,2, 39 paragraph objects.
Blocks B (39-76) and C (77-114) follow, and every convention below binds them.

The Translator submitted **49 editorial_questions[]**.
This pass resolves all 49 and clears the array.
Four rulings are flagged below for human review, and one speculative overlay entry needs sign-off by name.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.0.0-rc1`
- `translation.overlayGlossaryVersion`: new, `1.0.0`
- `translation.glossaryVersion`: `2.74.0`, unchanged (the central file was not touched)
- `translation.modelDrafts`: editor appended
- `_meta.json`: not touched; `source-cop-1.json`: not touched

**Commentary.** Written to `notes: {"official": …, "community": []}` in the program's format.
37 of 39 paragraphs carry commentary.
THOM-34 and THOM-35 have none: they are short synoptic parallels with no divergence or source issue.

**English changes.** Six paragraphs changed, each governed by an overlay entry:

| refId | Draft | Now | Entry |
|---|---|---|---|
| THOM-3 | 'the kingdom is in heaven' … 'the birds of heaven' | 'the kingdom is in **the sky**' … 'the birds of **the sky**' | `tpe-sky-heaven-context-rule-thomas-woh` |
| THOM-9 | 'ears toward heaven', 'fruit up toward heaven' | 'toward **the sky**' (×2) | same |
| THOM-20 | 'the birds of heaven' | 'the birds of **the sky**' | same |
| THOM-12 | 'Wherever you have come, you will go to James' | 'Wherever you have come **to**, you **are to** go to James' | `iakobos-pdikaios-james-the-righteous-thomas-woh` |
| THOM-21 | 'his house of his kingdom'; 'they will find.' | 'his house of his **domain**'; 'they will find **it**.' (also 'watching **out** for') | `mntero-the-kingdom-thomas-woh`; `logion-21-robbers-clause-and-chreia-thomas-woh` |
| THOM-33 | 'under a basket' | 'under a **measure**' | `other-ear-and-maaje-measure-logion-33-thomas-woh` |

Every other line keeps the Translator's draft, which was accurate.
No line was harmonised toward the synoptic gospels.
The hard sayings keep the manuscript reading: 7 (the lion), 21 (the robbers clause), 30 (three gods) and 37.

---

## Rulings on the 49 editorial questions

| # | refId | Question | Ruling | Overlay entry (claim_type) |
|---|---|---|---|---|
| 0 | 0 | Central entries; 'cop' | Overlay opened. Central changes proposed below: add `cop`; extend `iēsous…` (35 units), `kingdom-of-heaven…` (THOM-20) and `lacuna-bracket…` (5 units). Do **not** extend `beatitudes…` or `parable-of-the-sower…`. | see CENTRAL |
| 1 | 0 | ϣⲁϫⲉ ⲉⲑⲏⲡ | 'the hidden sayings' kept. ϣⲁϫⲉ = 'sayings' for the collection and 'words' in narrative; ϩⲏⲡ = 'hidden' everywhere. | `shaje-ethep-hidden-sayings` (direct) |
| 2 | 0 | ⲉⲧⲟⲛϩ capitals | Lower case throughout, including 'the son of the living one' (37). | `etonh-the-living-lowercase` (direct) |
| 3 | 0 | Didymos Judas Thomas | Kept. The Greek form is 'Didymos', and neither by-name is translated. | `didymos-judas-thomas-name` (direct) |
| 4 | 0 | Nomina sacra | Expanded silently and recorded as an overlay convention. | `nomina-sacra-and-abbreviation-expansion-convention` (direct) |
| 5 | 0 | Greek loanwords | Translated, never transliterated; meaningful loan/native pairs are recorded in the apparatus. | `greek-loanword-rendering-convention` (direct) |
| 6 | 0 | Greek incipit | Coptic in the line; the Greek is in commentary. | `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention` (direct) |
| 7 | 1 | Speaker of 'And he said' | Ambiguity preserved. | `register-sayings-format-and-proper-names-convention` (direct) |
| 8 | 1 | ϩⲉⲣⲙⲏⲛⲉⲓⲁ | 'interpretation' kept. | `hermeneia-interpretation` (direct) |
| 9 | 1 | 'taste death' | Kept at every occurrence. | `jitpe-mpmou-taste-death` (direct) |
| 10 | 2 | ⲡⲧⲏⲣϥ | 'reign over the All', with 'the All' capitalised here and at 67 and 77. | `ptirf-the-all-reign-over-the-all` (direct) |
| 11 | 2 | Greek vs Coptic | Coptic followed; 'rest' and Clement's form are given in commentary. | base-text convention (direct) |
| 12 | 3 | ⲧⲙⲛ̄ⲧⲉⲣⲟ | 'the kingdom'; 'the kingdom of the heavens' for the plural (central); later 'the kingdom of the Father'. | `mntero-the-kingdom` (direct) |
| 13 | 3 | ⲧⲡⲉ | **Changed.** 'sky' in physical contexts (3, 9, 20), keeping concordance within a saying; 'heaven' in cosmological ones (6, 11, 12); 'the heavens' for the plural. | `tpe-sky-heaven-context-rule` (**inferred**) |
| 14 | 3 | ϣⲏⲣⲉ | 'sons' in the filial formulas (Greek υἱοί); 'little child(ren)' for ϣⲏⲣⲉ ϣⲏⲙ. **For review:** see escalation 3. | `shere-son-child` (direct) |
| 15 | 3 | 'Father' capitals | Capitalised for the divine referent, lower case at 16 (matthew-woh precedent). | `eiot-father-capitalisation` (direct) |
| 16 | 3 | ⲙⲛ̄ⲧϩⲏⲕⲉ | 'poverty', paired with 'poor' at 54. | `mnthke-poverty` (direct) |
| 17 | 3 | Greek vs Coptic | Coptic followed; the five differences are in commentary. | base-text convention (direct) |
| 18 | 4 | ⲟⲩⲁ ⲟⲩⲱⲧ | 'a single one' / 'the single one'; plain 'one' for ⲟⲩⲁ (11, 22). | `oua-ouot-a-single-one` (direct) |
| 19 | 4 | ⲧⲟⲡⲟⲥ / ⲙⲁ | 'place' for both; 'the place of life'. | `topos-ma-place` (direct) |
| 20 | 4 | ⲣⲱⲙⲉ | The draft's context-dependent mix is kept, with generic 'man' as the base (matthew-woh). | `rome-man-human-person` (direct) |
| 21 | 4 | Greek 'and the last first' | Coptic followed; the Greek is in commentary. | base-text convention (direct) |
| 22 | 5 | Greek 'buried … raised' | Coptic followed; the Greek is in commentary. | base-text convention (direct) |
| 23 | 6 | Greek vs Coptic | Coptic followed; 'in the sight of heaven' keeps 'heaven'. | base-text convention; `tpe-…` |
| 24 | 7 | Lion crux | **Manuscript reading kept** ('the lion will become human'); the emendation is in commentary; 'loathsome'. | `lion-and-man-logion-7-manuscript-reading` (direct) |
| 25 | 8 | Restoration convention | Proposal (a)+(b)+(c) adopted; details under Conventions. | `restored-text-bracket-and-sigla-convention` (direct) |
| 26 | 9 | Sower | 'Behold, the sower went out' kept from matthew-woh, with Thomas's soils kept. The central sower entry is **not** applied. | `sower-parable-coptic-form-and-eisheete-behold` (direct) |
| 27 | 10 | ⲕⲟⲥⲙⲟⲥ / ⲕⲁϩ | 'the world' / 'the earth', 'the soil'; 'keep watch against the world'. | `kosmos-world-kah-earth` (direct) |
| 28 | 11 | Light; subject in 24 | 'he gives light', with 'it' given in commentary. | `ouoein-light-man-of-light` (direct) |
| 29 | 12 | James | 'James the Righteous'. **Changed:** 'Wherever you have come to, you are to go' (focalising future). | `iakobos-pdikaios-james-the-righteous` (**inferred**) |
| 30 | 13 | Logion 13 vocabulary | 'Teacher', 'righteous angel', 'wise philosopher', 'measured out', 'wholly unable' all kept. | `logion-13-sah-angelos-pege-vocabulary` (direct) |
| 31 | 14 | ⲡⲛⲉⲩⲙⲁ | Lower case 'spirit'; 'flesh' ≠ 'body'; 'wonder' / 'marvel'. | `pneuma-sarx-soma-spirit-flesh-body` (direct) |
| 32 | 15 | 'not born of woman' | Kept. | `jpo-not-born-of-woman` (direct) |
| 33 | 16 | ⲙⲟⲛⲁⲭⲟⲥ | 'as solitary ones', kept distinct from ⲟⲩⲁ ⲟⲩⲱⲧ. | `monachos-solitary` (**inferred**) |
| 34 | 18 | ⲁⲣⲭⲏ / ϩⲁⲏ | 'the beginning' / 'the end'. | `arche-hae-beginning-end` (direct) |
| 35 | 19 | Paradise | 'five trees in Paradise' kept. | `five-trees-in-paradise` (direct) |
| 36 | 21 | ⲙⲁⲣⲓϩⲁⲙ | 'Mariham'; the identification is in commentary. | `mariham-name` (direct) |
| 37 | 21 | 'house of his kingdom' | **Changed** to 'his house of his domain' (Lambdin); the lexical identity is in commentary. | `mntero-the-kingdom` (direct) |
| 38 | 21 | Robbers clause | Negative sense kept, without brackets. **Changed:** 'they will find it'. | `logion-21-robbers-clause-and-chreia` (**inferred**) |
| 39 | 22 | ϩⲓⲕⲱⲛ | 'an image in place of an image'; 'being nursed'. | `eikon-image` (direct) |
| 40 | 24 | ⲧⲥⲉⲃⲟ | 'Show us the place' kept. | `topos-ma-place` (direct) |
| 41 | 25 | ⲯⲩⲭⲏ | 'soul' at both occurrences; the reflexive idiom is in commentary. | `psyche-soul` (direct) |
| 42 | 27 | No intro; Sabbath | No 'Jesus said' supplied; 'fast from the world'; 'keep the Sabbath as Sabbath'; 'the kingdom'. | `logion-27-fast-from-the-world-sabbath-as-sabbath` (direct) |
| 43 | 30 | Three-gods crux | **Manuscript reading kept**; the Greek and the emendations are in commentary. | `three-gods-logion-30-manuscript-reading` (direct) |
| 44 | 31 | 'village' | Kept (Coptic). | base-text convention (direct) |
| 45 | 33 | Other ear; ⲙⲁⲁϫⲉ | Manuscript sequence kept. **Changed:** 'under a measure' (keeps the ear/measure pun). | `other-ear-and-maaje-measure-logion-33` (**inferred**) |
| 46 | 36 | Short vs long form | Coptic followed; the long Greek is in commentary. | base-text convention (direct) |
| 47 | 37 | 'son of the living one' | Lower case. | `etonh-the-living-lowercase` (direct) |
| 48 | 38 | Greek scraps | Coptic followed. | base-text convention (direct) |

All overlay ids carry the suffix `-thomas-woh`; it is omitted in the table.

---

## Conventions for Blocks B and C (binding)

1. **Register.** Modern English as in matthew-woh.
   Each saying begins 'Jesus said:' with a colon and no quotation marks around the saying; quoted speech inside it takes single quotes.
   No introductory formula is supplied where the Coptic lacks one.
   The sayings keep their terseness, and the line is never harmonised to the synoptics.
2. **Base text.** The English translates the Coptic of NHC II,2.
   The Greek of P.Oxy. 1/654/655 goes in commentary only, with restored Greek labelled as restored.
   In Block C this covers logion 77b in P.Oxy. 1, joined to 30.
3. **Restored text.**
   - **[ ]** encloses any English word whose Coptic token is wholly or partly restored inside [ ] in the source.
   - **⟨ ⟩** and **( )** source sigla (scribal omissions, abbreviations) are rendered silently in the English and noted in commentary where relevant.
   - **{ }** scribal surplus is dropped silently and noted in commentary if it is significant.
   - **…** marks an unrestorable gap.
   - English **⟨ ⟩** is reserved for English words the Editor supplies where no Coptic wording exists. It is not used in Block A.
   - **(?)** after a word marks a reading kept from the reference for a term of uncertain meaning, as in vendidad-woh. It is not used in Block A.
4. **Nomina sacra and overlined contractions** are expanded silently. The `text` field keeps the overlines.
5. **Greek loanwords** are translated, never transliterated.
6. **Cruxes.** The manuscript reading stands in the line. Emendations, and the Greek where it exists, go in commentary.
7. **Fixed renderings carried forward:**
   - 'the kingdom'; 'the kingdom of the Father'; 'the kingdom of the heavens' (54, 114)
   - 'the All' (67, 77)
   - 'will not taste death' (85, 111)
   - 'solitary ones' (49, 75)
   - 'image(s)' (50, 83, 84)
   - 'the living one', lower case (52, 59, 111)
   - 'poor' / 'poverty' (54)
   - 'Mariham' (114)
   - 'the Son of Man' at 86, under the central `son-of-man-…` convention, to be checked when Block C is drafted
   - 'Blessed is/are' (54, 58, 68, 69, 103), with the synoptic-parallel beatitudes proposed for the central beatitudes entry
   - ⲧⲡⲉ by the sky/heaven context rule
   - 'Father' capitalised for the divine referent

---

## Greek vs Coptic (Block A)

| Logion | Greek witness | Material divergence | Treatment |
|---|---|---|---|
| incipit | P.Oxy. 654.1-3 | Greek 'secret' (restored); 'Judas who is also Thomas' without Didymos; 'spoke' | Coptic; commentary |
| 1 | 654.3-5 | Agreement (speaker equally open) | Coptic |
| 2 | 654.5-9 | Greek: amazed → reign → **rest**; no 'troubled', no 'over the All' | Coptic; commentary (+ Clement, Strom. 2.9.45; 5.14.96) |
| 3 | 654.9-21 | 'under the earth' vs 'in the sea'; fish 'enter'; extra 'whoever knows himself will find it'; no 'you will be known'; 'kingdom [of God]' | Coptic; commentary |
| 4 | 654.21-27 | Greek adds 'and the last first' | Coptic; commentary |
| 5 | 654.27-31 | Greek adds 'nothing buried that will not be raised' | Coptic; commentary |
| 6 | 654.32-40 | 'How shall we fast?' vs 'Do you want us to fast?'; 'before the truth' vs 'in the sight of heaven' | Coptic; commentary |
| 7 | 654.40-42 | Traces only | Coptic (crux) |
| 24 | 655 frag. d | Traces only | Coptic |
| 26 | P.Oxy. 1.1-4 | End of saying; agreement | Coptic |
| 27 | 1.4-11 | Greek has 'Jesus says'; 'kingdom of God' | Coptic; commentary |
| 28 | 1.11-21 | Agreement ('in flesh', 'sons of men') | Coptic |
| 29 | 1.22 | End only ('this poverty') | Coptic |
| 30 | 1.23-30 | 'three … [gods/without God]' (restored); 'one alone'; stone/wood sentence (= Coptic 77b) | Coptic (crux); commentary |
| 31 | 1.30-35 | 'homeland' vs 'village' | Coptic; commentary |
| 32 | 1.36-41 | Agreement | Coptic |
| 33 | 1.41-42 | 'in your one ear' (rest lost) | Coptic; commentary |
| 36 | 655 i.1-17 | Greek much longer (food, lilies, stature, garment) | Coptic; commentary |
| 37 | 655 i.17-ii.1 | Broad agreement, fragmentary | Coptic |
| 38 | 655 ii.2-11 | Scraps; usual restoration agrees | Coptic |

---

## Source findings (source-cop-1.json stays immutable)

These are recorded in the commentary of the affected units, for whoever maintains the source pipeline.
None of them changes the English beyond following the corpus normalisation.

| refId | Finding |
|---|---|
| THOM-3 | Lemma aid counts 1 supplied span; `text` has no sigla. Diplomatic ⲉⲩϣⲁϫⲟⲟⲥ, normalised ⲉⲩϣⲁⲛϫⲟⲟⲥ (conditional ⲛ supplied but unmarked). |
| THOM-8 | Lemma aid counts 2 supplied spans; `text` shows 1 ([ⲡⲉ]). The normalisation also changes ⲁⲩⲟⲩⲱϩⲉ / ⲁⲩⲛⲟϭ to ⲉⲩ-. |
| THOM-10 | Lemma aid counts 1; `text` has none. Diplomatic ϯⲁⲣⲉϩ, normalised ϯϩⲁⲣⲉϩ. |
| THOM-14 | Stray ASCII apostrophe (U+0027) before ⲛ̄ⲧⲉⲧⲙ̄ⲙⲟⲟϣⲉ, apparently an encoding artefact (the file otherwise uses ⳿ U+2CFF). |
| THOM-18 | Lemma aid counts 1; `text` has none. Rasura in ⲥⲟⲩⲱⲛⲑϩⲁⲏ (Dilley 'ϩ rasura'); the normalised layer reads ⲥⲟⲩⲱⲛⲧϩϩⲁⲏ. Diplomatic ⲧⲛ̄ϩⲁⲏ, normalised ⲧⲉⲛϩⲁⲏ 'our end'. |
| THOM-22 | Lemma aid counts 6 supplied spans; `text` shows 2 ([ⲉⲧ], [ⲧⲉⲣ]). There is also a middle dot inside ⲙ̄ⲫⲟ·ⲟⲩⲧ. |
| THOM-32 | Diplomatic ⲁⲛ, normalised ⲟⲛ; the sense is unchanged. |

Recommendation (data maintainers, not this pass): check whether the diplomatic `orig_group` export drops the sigla of normalisation-only supplements at 3, 10 and 18. The source file should be re-fetched if so; it should not be hand-edited.

---

## Speculative entries requiring sign-off

### `woh-reading-kingdom-within-beginning-end-five-trees-thomas-woh` (overlay)

**Source:** Thomas 3 (the kingdom inside and outside you), 18 (where the beginning is, there the end will be), 19 (five trees in Paradise)

**WoH choice:** No effect on any English line.
The entry records three interpretive resonances:
- (3) self-knowledge as recognising oneself as a child of the creating Father, read alongside the canon's teaching that humans were made in the image of the Elohim;
- (18) the identity of beginning and end, read alongside the precessional cycle from which the project takes its name;
- (19) the five unchanging trees, read alongside the canon's reading of Eden as the Elohim's place of work.

**Why speculative:**
- None of the three sayings refers to the Elohim, to precessional ages or to a physical garden of the creators, and the canon does not cite these sayings.
- The resonances are a synthesis beyond any single source.
- The commentary at 3 states explicitly that the saying gives **no** support to a reading of the kingdom as a place in the sky.

**Recommendation:** ship as `speculative`, apparatus only. Each mention is one labelled paragraph ('Wheel of Heaven reading (interpretive; not part of the translation)') in the notes of THOM-3, 18 and 19.
If the founder prefers no lens in Thomas Block A, delete those three paragraphs and drop the id from three glossaryRefs. Nothing else depends on it.

---

## Unresolved editorial questions / decisions for review

None of the 49 questions is left open. The following rulings are judgement calls that the reviewer should confirm.

### `THOM-7` and `THOM-30` — manuscript reading kept at both cruxes

**Issue:** 'and the lion will become human' (7) and 'Where there are three gods, they are gods' (30) are widely suspected corruptions.
**Options considered:** (A) manuscript reading in the line with emendation in commentary (adopted); (B) emend in the line; (C) emend with ⟨ ⟩ marking.
**Why escalating:** (A) follows the brief and the program's crux rule, but popular translations often print the emendation at 7, so readers will notice the difference.

### `THOM-3` / `THOM-28` / `THOM-37` — 'sons' vs 'children' for ϣⲏⲣⲉ

**Issue:** ϣⲏⲣⲉ is common-gender.
'Sons' was chosen because the earlier Greek has υἱοί / υἱοῖς and matthew-woh uses 'sons of your Father'.
**Options considered:** 'sons' (adopted); 'children' (Patterson–Meyer).
**Why escalating:** this is a register policy question that also affects Blocks B and C (e.g. 50 'children of the light', 'children of the living Father').

### `THOM-33` — 'measure' diverges from matthew-woh 'basket'

**Issue:** Thomas's ϩⲁⲙⲁⲁϫⲉ is now 'under a measure', to keep the ear/measure pun, while Mt 5:15 has 'basket' in matthew-woh.
**Options considered:** 'measure' (adopted; `inferred`); 'basket' (matthew-woh harmony); 'bushel' (Lambdin/KJV).
**Why escalating:** this is a deliberate cross-text difference.

### `THOM-21` — robbers clause

**Issue:** The negative sense rests on reading ⲛⲉ as the negative optative ⲛ̄ⲛⲉ.
It is printed without brackets because the context makes it certain (`inferred`).
**Why escalating:** this is the only place in Block A where the English depends on an unmarked editorial reinterpretation of a converter.

---

## Glossary changes for review

### Central glossary

None written. All proposals are in the CENTRAL section below.

### Per-translation overlay (new file, v1.0.0, released 2026-10-31)

`gospel-of-thomas-woh/_translation-glossary.json`: **39 entries**: 33 `direct`, 5 `inferred`, 1 `speculative`.

- **Conventions (5, direct):** `register-sayings-format-and-proper-names-convention`, `restored-text-bracket-and-sigla-convention`, `nomina-sacra-and-abbreviation-expansion-convention`, `greek-loanword-rendering-convention`, `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention`
- **Lexical, direct (28):** `shaje-ethep-hidden-sayings`, `etonh-the-living-lowercase`, `didymos-judas-thomas-name`, `hermeneia-interpretation`, `jitpe-mpmou-taste-death`, `ptirf-the-all-reign-over-the-all`, `mntero-the-kingdom`, `shere-son-child`, `eiot-father-capitalisation`, `mnthke-poverty`, `oua-ouot-a-single-one`, `topos-ma-place`, `rome-man-human-person`, `makarios-blessed-singular-formula`, `lion-and-man-logion-7-manuscript-reading`, `sower-parable-coptic-form-and-eisheete-behold`, `kosmos-world-kah-earth`, `ouoein-light-man-of-light`, `logion-13-sah-angelos-pege-vocabulary`, `pneuma-sarx-soma-spirit-flesh-body`, `jpo-not-born-of-woman`, `arche-hae-beginning-end`, `five-trees-in-paradise`, `mariham-name`, `eikon-image`, `psyche-soul`, `logion-27-fast-from-the-world-sabbath-as-sabbath`, `three-gods-logion-30-manuscript-reading`
- **Inferred (5):** `tpe-sky-heaven-context-rule`, `iakobos-pdikaios-james-the-righteous`, `monachos-solitary`, `logion-21-robbers-clause-and-chreia`, `other-ear-and-maaje-measure-logion-33`
- **Speculative (1):** `woh-reading-kingdom-within-beginning-end-five-trees`

(All ids end in `-thomas-woh`.)
Indexing: the `strongs` field carries Crum, *A Coptic Dictionary* (1939) headwords. For Greek loans it also carries the Strong's G-number of the Greek word.

---

## CENTRAL — apply by orchestrator

Central v2.74.0 has no Coptic entries.
The proposals below add no new entries.
They add one source language and extend `appliesTo` on three existing entries: a semver-minor bump to **2.75.0**.
The chapter's glossaryRefs already cite the three extended ids.

### 0. Top-level

- Add `"cop"` to `sourceLanguages`, giving `["he","sux","akk","uga","arb","grc","ave","cop"]`.
- Add a scopeNote line: "v2.75.0: first Coptic-source references (Gospel of Thomas, NHC II,2, Block A); three existing Greek-NT/project entries extended to THOM refIds; Thomas-specific decisions live in the gospel-of-thomas-woh overlay."

### 1. EXTEND `appliesTo`

| Existing central id | Add to `appliesTo` | Reason |
|---|---|---|
| `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus` (direct) | `THOM-0`, `THOM-2`, `THOM-3`, `THOM-4`, `THOM-5`, `THOM-6`, `THOM-7`, `THOM-9`, `THOM-10`, `THOM-11`, `THOM-12`, `THOM-13`, `THOM-14`, `THOM-15`, `THOM-16`, `THOM-17`, `THOM-18`, `THOM-19`, `THOM-20`, `THOM-21`, `THOM-22`, `THOM-23`, `THOM-25`, `THOM-26`, `THOM-28`, `THOM-29`, `THOM-30`, `THOM-31`, `THOM-32`, `THOM-33`, `THOM-34`, `THOM-35`, `THOM-36`, `THOM-37`, `THOM-38` | Coptic ⲓ︤ⲥ︥ / ⲓⲏ︤ⲥ︥ is the nomen sacrum of Greek Ἰησοῦς, rendered 'Jesus' as in the entry. Optional note for the `source` field: "Coptic ⲓⲏⲥⲟⲩⲥ (nomen sacrum ⲓ︤ⲥ︥)". |
| `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim` (direct) | `THOM-20` | Coptic ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ keeps the plural, rendered 'the kingdom of the heavens' per the entry. Suggested sentence (optional; adding it is a rationale modification, so apply it at the next major bump or skip it): "The plural form also occurs in Coptic Thomas (logia 20, 54, 114), so it is not exclusively Matthean." Blocks B/C will add THOM-54 and THOM-114. |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (direct) | `THOM-8`, `THOM-16`, `THOM-22`, `THOM-29`, `THOM-37` | The Thomas overlay adopts the central [restoration] / ⟨supply⟩ distinction for Dilley's papyrological sigla. |

### 2. NOT extended, deliberately

- `parable-of-the-sower-mt-13-3-23-raelian-panspermia-canon-citation-cross-corpus-with-disavowals` is not extended. Its wohChoice governs Matthew's wording ('went out *to sow*', 'rocky ground'), which Thomas does not share. Its apparatus records a Raëlian-canon reading of Matthew's text, and extending it would attach that reading to a text the canon does not cite. The Thomas form is recorded in the overlay, which only cross-references the central entry. The Translator's glossaryRef at THOM-9 has been removed.
- `beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus` is not extended to THOM-7/18/19. Those sayings have no synoptic counterpart, and the lexical choice 'Blessed is' sits in the overlay. Recommend extending it in Blocks B/C to Thomas's synoptic-parallel beatitudes (54, 68, 69). The Translator's glossaryRefs at 7/18/19 have been removed.

### 3. Candidates for later promotion (no action now)

- `jitpe-mpmou-taste-death-thomas-woh` could be promoted when Mt 16 / Mk 9 / Jn 8 are translated (cross-corpus idiom).
- `nomina-sacra-and-abbreviation-expansion-convention-thomas-woh` could be promoted when a second Coptic or Greek manuscript-based text arrives.

---

## Lens-routing summary

- **No English line carries the lens.** No line uses 'Elohim', 'creators', 'planet' or 'messenger' for ⲁⲅⲅⲉⲗⲟⲥ. 'Sky' at 3/9/20 is a context-of-the-saying decision, and the commentary at 3 states that the saying cuts against a sky-located kingdom.
- **Mainstream framing.** The disputed date, the dispute over dependence on the synoptics (Patterson, DeConick vs Gathercole, Goodacre) and the debated relation to 'gnosticism' are stated at THOM-0 without adjudication.
- **WoH reading.** It appears three times (3, 18, 19), each as one labelled paragraph pointing to the single speculative overlay entry.
- **Raëlian sower reception.** It is not imported into Thomas 9.

## Escalation list (for human sign-off)

1. **SPECULATIVE:** `woh-reading-kingdom-within-beginning-end-five-trees-thomas-woh`. It needs sign-off by name, or deletion of the three labelled paragraphs (THOM-3, 18, 19) and their glossaryRefs.
2. **Review:** the manuscript reading is kept at the logion 7 and logion 30 cruxes.
3. **Review:** 'sons' rather than 'children' for ϣⲏⲣⲉ in the filial formulas (binds Blocks B/C).
4. **Review:** 'under a measure' at 33, against matthew-woh's 'basket' (`inferred`).
5. **Review:** the unbracketed negative reading of the logion 21 robbers clause (`inferred`).
6. **Orchestrator:** apply the CENTRAL section (add `cop`; three appliesTo extensions; bump to 2.75.0).
7. **Data maintainers:** the source findings at 3, 8, 10, 14, 18, 22 and 32 (source not edited).
