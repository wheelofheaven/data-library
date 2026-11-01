# Sign-off package — Gospel of Thomas, Block B (logia 39–76)

**Status:** `awaiting-human` · `1.1.0-rc1` · central 2.75.0 (+ proposals → 2.76.0) · overlay v1.1.0 (as reviewed)

Block A (0–38) is signed off and live in the data repos. At ratification Block B is merged into `chapter-1.json` (→ 1.1.0).

## Summary

| Item | Count |
|---|---|
| Units translated | 38 (n=39–76) |
| Units with commentary | 37 |
| Translator questions raised / resolved | 47 / 47 |
| New overlay entries | 31 (28 direct, 2 inferred, 1 speculative); 23 ratified Block A entries extended by appliesTo/scopeNote only (reviewer-verified) |
| Central proposals | appliesTo extensions only: iēsous (30 units), lacuna-bracket (9), beatitudes (54, 68, 69), kingdom-of-the-heavens (54) → 2.76.0 |
| Reviewer unit verdicts | approve 33, revise 5 |
| Lens-leakage flags | 0 |

## Items requiring decision

1. **Speculative overlay entry `woh-reading-logion-50-origin-from-the-light-thomas-woh`** — one labelled paragraph in THOM-50's commentary ("we came from the light … they… our image" read alongside the canon); reviewer: approve, apparatus only. Optional refinement: note that mainstream scholarship (DeConick 2006) already links logion 50 to Gen 1, so only reading "their" as the Elohim is speculative. **Options:** (a) keep (with the refinement); (b) drop the paragraph and ref.
2. **THOM-61 — "⟨Salome said:⟩"** (reviewer: flag-for-human). Only the feminine ⲧⲉⲕ- marks Salome as the speaker of "I am your disciple"; without a formula an English reader takes it as Jesus. Reviewer recommends admitting ⟨Salome said:⟩ under the ratified ⟨ ⟩ convention, as a narrow exception (not a licence to supply formulas generally). **Options:** (a) supply ⟨Salome said:⟩; (b) leave as is.
3. **Reviewer revise items (apply at ratification):**
   - THOM-47: "new wine is not put into old wineskins, lest they burst" (zero article; plural subject).
   - THOM-59 commentary: the diplomatic text writes the negative optative with a single ⲛ (as at 21/22) — it is not missing; retitle the paragraph and fix the report's anomaly row.
   - THOM-61: "Two will rest on a bed" (ⲙ̄ⲙⲁⲩ here is the reflexive object of ⲙ̄ⲧⲟⲛ, not "there").
   - THOM-66: drop `topos-ma-place-thomas-woh` (ⲙⲁ- there is the imperative of ϯ, not "place").
   - THOM-74: "Lord, there are many around the drinking trough(?), but there is no one in the sickness(?)." — **verified at orchestration:** ϣⲱⲛⲉ "sickness" is masculine (Crum, CD 571a) and ϣⲱⲧⲉ "well, cistern" feminine (CD 595a), so the feminine article ⲧ- supports the "well" emendation; add that to the crux paragraph and entry, citing Crum.
   - Restored-text convention scopeNote (d): "Negative optatives written defectively in the manuscript (single ⲛ, THOM-59 as at 21/22) or supplied only in the normalised layer (THOM-46) are read as negatives without brackets."
4. **Approved, for completeness:** "repose" for ⲁⲛⲁⲡⲁⲩⲥⲓⲥ vs "rest" for ⲙ̄ⲧⲟⲛ (binds logion 90); English ⟨ ⟩ for a whole supplied word (60 "⟨They saw⟩"); 76 "his treasure"; 65 "[good]" with the alternative left unattributed (reviewer recalls Bethge et al. 1996 / Plisch 2008 — unverified, not cited); 49 "the solitary and chosen ones"; 46 "lowered", 67 parse; all four central extensions.

## Reviewer report (Block B)

```json
{
  "reviewer": "claude-opus-5-5 acting as woh-reviewer",
  "reviewedAt": "2026-11-01T07:34:28Z",
  "verdicts": [
    {
      "refId": "THOM-39",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (1989)",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲱⲡ"
      ],
      "reasoning": "Re-parsed: ⲁⲩϫⲓ ⲛ̄ϣⲁϣⲧ ⲛ̄ⲧⲅⲛⲱⲥⲓⲥ ⲁⲩϩⲟⲡⲟⲩ (perfect; plural object resumed by -ⲟⲩ), ⲟⲩⲧⲉ ⲙ̄ⲡⲟⲩⲃⲱⲕ ⲉϩⲟⲩⲛ, ⲛⲉⲧⲟⲩⲱϣ … ⲙ̄ⲡⲟⲩⲕⲁⲁⲩ, ϣⲱⲡⲉ ⲙ̄ⲫⲣⲟⲛⲓⲙⲟⲥ … ⲛ̄ⲁⲕⲉⲣⲁⲓⲟⲥ. Plural 'keys' kept against Lk 11:52; the Mt 10:16 wording is used only because the Coptic says exactly that. Confirmed that ⲅⲛⲱⲥⲓⲥ occurs only here in the source file."
    },
    {
      "refId": "THOM-40",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲟⲩⲃⲉⲛⲉⲗⲟⲟⲗⲉ ⲁⲩⲧⲟϭⲥ ⲙ̄ⲡⲥⲁ ⲛⲃⲟⲗ ⲙ̄ⲡⲉⲓⲱⲧ; circumstantial ⲉⲥⲧⲁϫⲣⲏⲩ ⲁⲛ read causally ('since'), which is within the range of the circumstantial; impersonal ⲥⲉⲛⲁⲡⲟⲣⲕⲥ̄ rendered passive as elsewhere. Father capitalised (divine referent)."
    },
    {
      "refId": "THOM-41",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲡⲉⲧⲉⲩⲛ̄ⲧⲁϥ ϩⲛ̄ⲧⲉϥϭⲓϫ ⲥⲉⲛⲁϯ ⲛⲁϥ: the English keeps the Coptic's lack of an object ('Whoever has in his hand'); slightly stiff but exact. No commentary needed."
    },
    {
      "refId": "THOM-42",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲱⲡⲉ",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)"
      ],
      "reasoning": "ϣⲱⲡⲉ + circumstantial ⲉⲧⲉⲧⲛ̄ⲣ̄ⲡⲁⲣⲁⲅⲉ is the regular 'become X' construction; 'Become passers-by' is Lambdin's rendering and the adverbial alternative is in the commentary. Hard saying kept in its manuscript form."
    },
    {
      "refId": "THOM-43",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ϩⲛ̄ⲛⲉϯϫⲱ ⲙ̄ⲙⲟⲟⲩ ⲛⲏⲧⲛ̄ ⲛ̄ⲧⲉⲧⲛ̄ⲉⲓⲙⲉ ⲁⲛ … may be a statement or an unmarked question; the statement reading is defensible. No speech formula is supplied, correctly. ⲛ̄ⲛⲓⲓ̈ⲟⲩⲇⲁⲓⲟⲥ 'the Jews' stated plainly, with the polemic acknowledged in commentary."
    },
    {
      "refId": "THOM-44",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Triad Father/Son/Holy Spirit; impersonal ⲥⲉⲛⲁⲕⲱ ⲉⲃⲟⲗ ⲛⲁϥ → 'he will be forgiven'. Thomas's triad is not harmonised to Mt 12:32's 'Son of Man'. ϩⲙ̄ⲡⲕⲁϩ … ϩⲛ̄ⲧⲡⲉ 'on earth … in heaven' per the context rule."
    },
    {
      "refId": "THOM-45",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲁϩⲟ, ϩⲟⲟⲩ"
      ],
      "reasoning": "Re-parsed; [ⲟⲩⲁ]ⲅⲁⲑⲟⲥ and ⲟⲩⲕⲁ[ⲕⲟ]ⲥ correctly give '[A good]' and '[bad]' under the mechanical bracket rule (ⲟⲩ of the first is restored, so 'A' is inside). No 'mouth' imported from Lk 6:45."
    },
    {
      "refId": "THOM-46",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲱϭⲡ",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (negative optative ⲛ̄ⲛⲉ-)"
      ],
      "reasoning": "ϫⲓⲛ ⲁⲇⲁⲙ ϣⲁ ⲓⲱϩⲁⲛⲛⲏⲥ … ⲙⲛ̄ ⲡⲉⲧϫⲟⲥⲉ ⲉ- ⲓⲱϩⲁⲛⲛⲏⲥ correct; 'lowered' for ⲟⲩⲱϭⲡ 'break' is Lambdin's and properly marked inferred with the literal sense in commentary. Advisory (non-blocking; initially a commentary revise, withdrawn after the escalation report showed the edition counts a supplied span here): the diplomatic ⲛⲟⲩⲱϭⲡ begins with ⲛ- and may be a defective writing of the negative ⲛ̄ⲛⲉⲩ-, so 'with no negative' in the note is better put as 'with the negative written defectively or not at all'."
    },
    {
      "refId": "THOM-47",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (zero article with plural reference)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲁⲥⲕⲟⲥ"
      ],
      "reasoning": "Exact change: 'And new wine is not put into an old wineskin, lest they burst' → 'And new wine is not put into old wineskins, lest they burst'. ⲉ-ⲁⲥⲕⲟⲥ has the zero article (indefinite, number unmarked) and the purpose clause ⲛ̄ⲛⲟⲩ-/ⲛ̄ⲛⲉⲩ-ⲡⲱϩ is 3rd plural, so the English must be plural to agree; the converse case (ⲛⲉϥⲧⲉⲕⲁϥ, masc. sing.) correctly stays 'a new wineskin … lest it spoil it'. Rest of the saying (two horses/bows, reversed patch) is exact and unharmonised."
    },
    {
      "refId": "THOM-48",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲉⲣϣⲁ ⲥⲛⲁⲩ ⲣ̄ⲉⲓⲣⲏⲛⲏ ⲙⲛ̄ ⲛⲟⲩⲉⲣⲏⲩ ϩⲙ̄ ⲡⲉⲓⲏⲉⲓ ⲟⲩⲱⲧ: 'this single house' renders adjectival ⲟⲩⲱⲧ; exact."
    },
    {
      "refId": "THOM-49",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (relative ⲉⲧ- requires an antecedent; substantivised relative takes the article)"
      ],
      "reasoning": "Bare ⲉⲧⲥⲟⲧⲡ after ⲁⲩⲱ can only qualify ⲛ̄ⲙⲟⲛⲁⲭⲟⲥ, so 'the solitary and chosen ones' (one group) is grammatically required; Lambdin likewise 'the solitary and elect'. The second future ⲉⲧⲉⲧⲛⲁⲃⲱⲕ ⲉⲙⲁⲩ is properly rendered as a cleft ('it is there that you will go')."
    },
    {
      "refId": "THOM-50",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲱϩⲉ, ⲙⲁⲉⲓⲛ",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Re-parsed: ⲛ̄ⲧⲁⲧⲉⲧⲛ̄ϣⲱⲡⲉ ⲉⲃⲟⲗ ⲧⲱⲛ (focalised 'from where'), ⲁϥⲱϩ[ⲉ ⲉⲣⲁⲧϥ] 'stood', ⲁϥⲟⲩⲱⲛϩ ⲉ[ⲃ]ⲟⲗ ϩⲛ̄ ⲧⲟⲩϩⲓⲕⲱⲛ 'appeared in their image' with 'their' left unresolved; 'Is it you?', 'its sons' (ratified rule), 'movement and repose'. Bracketing '[appeared]' for one restored letter is over-cautious but is what the ratified mechanical rule requires. The WoH paragraph is labelled, placed after the mainstream reading, and does not touch the line."
    },
    {
      "refId": "THOM-51",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϭⲱϣⲧ"
      ],
      "reasoning": "ⲉ-ⲧⲁⲛⲁⲡⲁⲩⲥⲓⲥ … ⲛⲁϣⲱⲡⲉ (focalising future) 'on what day will the repose … come about'; ⲛⲏⲩ present 'is coming'; ⲧⲏ ⲉⲧⲉⲧⲛ̄ϭⲱϣⲧ ⲉⲃⲟⲗ ϩⲏⲧⲥ̄ ⲁⲥⲉⲓ. The ἀνάστασις conjecture is correctly kept out of the line."
    },
    {
      "refId": "THOM-52",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "'all of them spoke in you' keeps ϩⲣⲁⲓ̈ ⲛ̄ϩⲏⲧⲕ literal with alternatives in commentary; ⲕⲱ 'left aside', ⲙ̄ⲡⲉⲧⲛ̄ⲙ̄ⲧⲟ ⲉⲃⲟⲗ 'in your presence'. Exact."
    },
    {
      "refId": "THOM-53",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϭⲛ̄ϩⲏⲩ"
      ],
      "reasoning": "Question ⲡⲥⲃ̄ⲃⲉ ⲣ̄ⲱⲫⲉⲗⲉⲓ ⲏ ⟨ⲙ̄⟩ⲙⲟⲛ (letter supply rendered silently, correct); unreal conditional ⲛⲉϥⲣ̄ⲱⲫⲉⲗⲉⲓ … ⲛⲉⲡⲟⲩⲉⲓⲱⲧ ⲛⲁϫⲡⲟⲟⲩ; ⲁϥϭⲛ̄ϩⲏⲩ ⲧⲏⲣϥ 'has become profitable in every respect'. 'their father' lower case (human); 'in spirit' lower case per the pneuma rule."
    },
    {
      "refId": "THOM-54",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ϫⲉ ⲧⲱⲧⲛ̄ ⲧⲉ ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ: possessive pronoun 'yours' and plural 'heavens' both kept; not harmonised to either Mt 5:3 ('in spirit') or Lk 6:20 ('of God')."
    },
    {
      "refId": "THOM-55",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Hurtado, The Earliest Christian Artifacts (2006), on the staurogram"
      ],
      "reasoning": "ⲡⲉⲧⲁ- = Lycopolitan future relative (lemma aid ⲛⲁ/FUT); 'will not be able to become a disciple to me' is literal; staurogram in ⲥⳁⲟⲥ expanded 'cross' silently under the nomina-sacra convention."
    },
    {
      "refId": "THOM-56",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲡⲉⲧⲁϩⲥⲟⲩⲱⲛ ⲡⲕⲟⲥⲙⲟⲥ ⲁϥϩⲉ ⲉⲩⲡⲧⲱⲙⲁ … ⲡⲕⲟⲥⲙⲟⲥ ⲙ̄ⲡϣⲁ ⲙ̄ⲙⲟϥ ⲁⲛ. Advisory only: the second ⲁ-ⲡⲧⲱⲙⲁ has the definite (anaphoric) article, so 'the corpse' is the more literal option; 'a corpse' is acceptable English and follows Lambdin."
    },
    {
      "refId": "THOM-57",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Restorations bracketed correctly ('[good] seed', '[darnel]', 'the [good seed]'); ϫⲉ ⲉⲛⲁϩⲱⲗⲉ (quoted 1pl intention) rendered as purpose with the literal form in commentary; 'darnel' concordant with matthew-woh; ⲛⲙ̄ⲙⲁϥ 'with it' correct (masc. sing. ⲍⲓⲍⲁⲛⲓⲟⲛ)."
    },
    {
      "refId": "THOM-58",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲓⲥⲉ"
      ],
      "reasoning": "ⲟⲩⲙⲁⲕⲁⲣⲓⲟⲥ ⲡⲉ ⲡⲣⲱⲙⲉ ⲛ̄ⲧⲁϩϩⲓⲥⲉ ⲁϥϩⲉ ⲁⲡⲱⲛϩ: 'who has suffered; he has found life'; 'toil' alternative in commentary."
    },
    {
      "refId": "THOM-59",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (negative optative ⲛ̄ⲛⲉ-, with degeminated spellings)"
      ],
      "reasoning": "English line is correct ('so that you do not die … and be unable to see'). Commentary-only revise: the note headed 'The unwritten negative' says the diplomatic ϩⲓⲛⲁ ϫⲉⲛⲉⲧⲙ̄ⲙⲟⲩ 'lacks the negative optative'. It does not: ⲛⲉ-ⲧⲙ̄-ⲙⲟⲩ is the 2pl negative optative ⲛ̄ⲛⲉⲧⲛ̄- written with a single ⲛ (and ⲧⲛ̄ assimilated before ⲙ), the same spelling Block A accepted at 21/22; the lemma aid accordingly counts no supplied span. Exact change: retitle the paragraph 'The negative' and replace its first two sentences with 'The diplomatic ϩⲓⲛⲁ ϫⲉⲛⲉⲧⲙ̄ⲙⲟⲩ writes the negative optative with a single ⲛ (ⲛⲉ- for ⲛ̄ⲛⲉ-, as at THOM-21 and 22); the normalised layer reads ⲛ̄ⲛⲉⲧⲛ̄ⲙⲟⲩ.' Make the matching correction to scopeNote (d) of the restored-text convention and to the THOM-59 row of the Editor report's source-anomaly table."
    },
    {
      "refId": "THOM-60",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes",
        "Crum, A Coptic Dictionary (1939) s.v. ⲕⲱⲧⲉ"
      ],
      "reasoning": "Manuscript has no main verb before ⲁⲩⲥⲁⲙⲁⲣⲉⲓⲧⲏⲥ (ⲁ- = ⲉ-); the edition's whole-word supply ⟨ⲁⲩⲛⲁⲩ⟩ is marked '⟨They saw⟩', which matches Lambdin's '<They saw>'. ⲡⲏ ⲙ̄ⲡⲕⲱⲧⲉ ⲙ̄ⲡⲉϩⲓⲉⲓⲃ is a complete nominal sentence and is printed literally, supplements in commentary. ϣⲓⲛⲉ ⲛ̄ⲥⲁ ⲟⲩⲧⲟⲡⲟⲥ ⲛⲏⲧⲛ̄ ⲉϩⲟⲩⲛ ⲉⲩⲁⲛⲁⲡⲁⲩⲥⲓⲥ exact."
    },
    {
      "refId": "THOM-61",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲙ̄ⲧⲟⲛ (reflexive ⲙ̄ⲧⲟⲛ ⲙ̄ⲙⲟ=)",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Exact change: 'Two will rest there on a bed' → 'Two will rest on a bed'. In ⲟⲩⲛ̄ ⲥⲛⲁⲩ ⲛⲁⲙ̄ⲧⲟⲛ ⲙ̄ⲙⲁⲩ the ⲙ̄ⲙⲁⲩ is not the adverb 'there': ⲙ̄ⲧⲟⲛ 'rest' is construed reflexively (ⲙ̄ⲧⲟⲛ ⲙ̄ⲙⲟ=), and the corpus normalises the form to ⲙ̄ⲙⲟⲩ and parses it ⲛ̄ + 3pl object pronoun ('rest themselves'); Lambdin likewise has 'Two will rest on a bed'. Everything else stands: ϩⲱⲥ ⲉⲃⲟⲗ ϩⲛ̄ ⲟⲩⲁ 'as though from someone', ⲡⲉⲧϣⲏϣ 'the one who is equal', manuscript ⲉϥϣⲏϥ 'destroyed' kept with the ϣⲏϣ emendation in commentary (Dilley citing Layton 1989). The separate question of a supplied ⟨Salome said:⟩ is flagged for the human (see escalation verdicts)."
    },
    {
      "refId": "THOM-62",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (focalising conversion)"
      ],
      "reasoning": "ⲉⲓ̈ϫⲱ parsed as focalising present (lemma aid CFOC), so the cleft 'It is to [those who are worthy] of [my] mysteries that I tell my mysteries' is grammatically motivated; brackets on ⲛ̄ⲛⲉ̣[ⲧⲙⲡϣⲁ], ⲛ̣[ⲛⲁ]-, ⲡ̣ⲉ̣[ⲧ]ⲉ correct. 'does' for future ⲛⲁⲁϥ is acceptable English."
    },
    {
      "refId": "THOM-63",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Exact; the rasura ⲛ̄ⲧⲁⲱ[[ϩ]]ⲥϩ correctly produces no bracket (scribal erasure, not restoration)."
    },
    {
      "refId": "THOM-64",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲙ̄ⲙⲟ, ϩⲟⲙⲧ"
      ],
      "reasoning": "Each refusal checked against the Coptic: the second excuse correctly lacks 'I ask to be excused'; ⲁϥⲉⲓ vs ⲁϥⲃⲱⲕ distinguished ('came' / 'went'); ⲡⲁϣⲃⲏⲣ ⲛⲁⲣ̄ϣⲉⲗⲉⲉⲧ 'is going to be married'; ⲕⲱⲙⲏ 'village'. Closing line brackets '[merchants will] … [enter]' follow the restored tokens. No Lukan wording imported."
    },
    {
      "refId": "THOM-65",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes",
        "Liddell-Scott-Jones s.v. χρήστης"
      ],
      "reasoning": "'[good]' prints the edition's restoration ⲭⲣⲏ[ⲥⲧⲟ]ⲥ (Lambdin: 'a good man'), bracketed; the χρήστης 'creditor' alternative is reported in commentary. Manuscript ⲙ̄ⲡⲉϥⲥⲟⲩⲱⲛⲟⲩ kept as 'he did not know them' with the emendation (Dilley citing Layton 1989) in commentary. 'farmers', 'feel shame before' avoid Mk 12 harmonisation."
    },
    {
      "refId": "THOM-66",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϯ (imperative ⲙⲁ-)",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (imperative ⲙⲁ- + infinitive)"
      ],
      "reasoning": "English is exact ('Show me the stone that the builders rejected: that one is the cornerstone'). Glossary-only revise: THOM-66 cites `topos-ma-place-thomas-woh`, but the ⲙⲁ- of ⲙⲁⲧⲥⲉⲃⲟⲉⲓ is the imperative of ϯ 'give, cause' (ⲙⲁ-ⲧⲥⲉⲃⲟ- 'teach, show'), not the noun ⲙⲁ 'place'. Exact change: remove `topos-ma-place-thomas-woh` from THOM-66 glossaryRefs, remove THOM-66 from that entry's appliesTo, and delete \"; ⲧⲥⲁⲃⲟ 'Show me' (66)\" from its scopeNote."
    },
    {
      "refId": "THOM-67",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϭⲣⲱϩ, ⲟⲩⲁⲁ="
      ],
      "reasoning": "⟨ϥ⟩ is a one-letter supply, silent. The parse (ⲟⲩⲁⲁϥ with the circumstantial; ⲙ̄ⲡⲙⲁ ⲧⲏⲣϥ as totality) agrees with Lambdin ('still feels a personal deficiency, he is completely deficient'); marked inferred, alternatives in commentary."
    },
    {
      "refId": "THOM-68",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Literal 'they will not find a place in the place where they have persecuted you' keeps the obscurity of ⲥⲉⲛⲁϩⲉ ⲁⲛ ⲉⲧⲟⲡⲟⲥ ϩⲙ̄ ⲡⲙⲁ ⲉⲛⲧⲁⲩⲇⲓⲱⲕⲉ … without Lambdin-type smoothing; the Pella suggestion is reported as a suggestion."
    },
    {
      "refId": "THOM-69",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ϩⲣⲁⲓ̈ ϩⲙ̄ ⲡⲟⲩϩⲏⲧ 'within their heart'; ⲉⲩⲛⲁⲧⲥⲓⲟ ⲛ̄ⲑϩⲏ ⲙ̄ⲡⲉⲧⲟⲩⲱϣ impersonal → passive 'will be filled' (Lambdin likewise); ϩⲛ̄ ⲟⲩⲙⲉ 'truly'."
    },
    {
      "refId": "THOM-70",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ϩⲟⲧⲁⲛ ⲉⲧⲉⲧⲛ̄ϣⲁ(ⲛ)ϫⲡⲉ ⲡⲏ ϩⲛ̄ⲧⲏⲩⲧⲛ̄ … ϥ̣[ⲛⲁⲙ]ⲟ̣ⲩ̣ⲧ̣ ⲧⲏⲛⲉ; brackets '[you]', '[will kill]' correct. 'what you have' slightly flattens ⲡⲁⲓ̈ ⲉⲧⲉⲩⲛ̄ⲧⲏⲧⲛ̄ϥ ('this which you have') but is accurate."
    },
    {
      "refId": "THOM-71",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲟⲣϣⲣ̄, ⲕⲱⲧ"
      ],
      "reasoning": "'I will [destroy this] house, and no one will be able to build it …': restored span bracketed as one; ⲕⲱⲧ 'build' not 'rebuild' (no Mk 14:58 / Jn 2:19 harmonisation); unrestored gap '…' per rule 3; no conjecture printed."
    },
    {
      "refId": "THOM-72",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲡⲱϣ"
      ],
      "reasoning": "'A [man said] to him' correct for [ⲡⲉ]ϫⲉ ⲟⲩⲣ[ⲱⲙ]ⲉ (ⲟⲩ extant, underdotted); ⲣⲉϥⲡⲱϣⲉ 'divider'; ⲙⲏ question rendered as a tag question expecting 'no'; 'my father's' lower case."
    },
    {
      "refId": "THOM-73",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "'the lord' lower case because the Coptic lacks Mt 9:38's 'of the harvest'; a defensible refusal to decide the referent."
    },
    {
      "refId": "THOM-74",
      "status": "revise",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲱⲛⲉ and s.v. ϣⲱⲧⲉ",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011) (gender of the definite article)",
        "Origen, Contra Celsum 8.15-16"
      ],
      "reasoning": "Manuscript reading in the line is right under the crux rule, but the claim that ϣⲱⲛⲉ is 'certain as a word' here overlooks the article: ⲧ-ϣⲱⲛⲉ is feminine, while the noun ϣⲱⲛⲉ 'sickness' is masculine in Sahidic (ⲡϣⲱⲛⲉ; to be confirmed against Crum s.v. ϣⲱⲛⲉ before applying) and ϣⲱⲧⲉ 'well, cistern' is feminine; the article is therefore itself evidence for the emendation, and the identification of the manuscript word, not only its sense, is uncertain. Exact change: line → 'Lord, there are many around the drinking trough(?), but there is no one in the sickness(?).'; add to the crux paragraph: 'The feminine article ⲧ- does not suit ϣⲱⲛⲉ \"sickness\", a masculine noun, but suits feminine ϣⲱⲧⲉ \"well, cistern\"; this supports the emendation.'; revise the '(?)' paragraph and `logion-74-jote-shone-crux-thomas-woh` accordingly. If Crum shows ϣⲱⲛⲉ attested as feminine, this revise lapses and the Editor's version stands."
    },
    {
      "refId": "THOM-75",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲉⲗⲉⲉⲧ"
      ],
      "reasoning": "ⲟⲩⲛ̄ ϩⲁϩ ⲁϩⲉⲣⲁⲧⲟⲩ ϩⲓ ⲣⲙ̄ⲡⲣⲟ … ⲙ̄ⲙⲟⲛⲁⲭⲟⲥ ⲛⲉⲧⲛⲁⲃⲱⲕ ⲉϩⲟⲩⲛ (cleft) 'it is the solitary ones who will enter'; ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ 'the bridal chamber' is a compound, standard rendering; the Valentinian rite is disclaimed in commentary."
    },
    {
      "refId": "THOM-76",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes",
        "Crum, A Coptic Dictionary (1939) s.v. ⲁϩⲟ, ⲉϣⲱⲧ"
      ],
      "reasoning": "'his treasure': the manuscript writes ⲡⲉϥ- with a supralinear ⲉ (= ⲡⲉϥⲉϩⲟ), the normalised layer reads ⲡⲉϥⲁϩⲟ, and Lambdin has 'his unfailing and enduring treasure'; the edition's {ⲉϥ} is a modern deletion and is properly reported in commentary. 'a man, a merchant', 'this single pearl' exact; Mt 13:45-46 / 6:19-20 wording not imported."
    }
  ],
  "glossaryReview": [
    {
      "glossary_id": "whole-word-supply-angle-brackets-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Direct confirmed. The refinement is principled (letters silent, whole words marked) and uses the English ⟨ ⟩ exactly as Block A defined it ('English words with no manuscript basis'); Lambdin also prints '<They saw>'. Approve the convention as written; whether it extends to speaker formulas (61) is a separate human question."
    },
    {
      "glossary_id": "gnosis-knowledge-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲱⲡ",
        "BDAG s.v. γνῶσις"
      ],
      "reasoning": "Direct confirmed; plural 'keys' is grammatical (ⲁⲩϩⲟⲡⲟⲩ resumes a plural); sole occurrence verified in the source file."
    },
    {
      "glossary_id": "parage-passers-by-logion-42-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)"
      ],
      "reasoning": "Direct confirmed: ϣⲱⲡⲉ + circumstantial = 'become'; Lambdin 'Become passers-by'."
    },
    {
      "glossary_id": "ioudaioi-the-jews-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "BDAG s.v. Ἰουδαῖος"
      ],
      "reasoning": "Direct confirmed; standard rendering, alternative recorded without softening the polemic."
    },
    {
      "glossary_id": "son-and-holy-spirit-triad-logion-44-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct confirmed; capital 'Son' justified by the triad; Mt 12:32's 'Son of Man' not imported."
    },
    {
      "glossary_id": "kakos-poneron-hoou-bad-evil-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲟⲟⲩ"
      ],
      "reasoning": "Direct; the fixed pairing is a transparent lexical convention with no lens."
    },
    {
      "glossary_id": "hmhal-slave-joeis-master-lord-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲙϩⲁⲗ, ϫⲟⲉⲓⲥ"
      ],
      "reasoning": "Direct confirmed; concordance with matthew-woh 'slave'; lower-case 'lord' at 73 is the more neutral choice."
    },
    {
      "glossary_id": "sotp-chosen-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)"
      ],
      "reasoning": "Direct confirmed; the syntactic argument for one group at 49 is correct."
    },
    {
      "glossary_id": "kim-anapausis-mton-movement-repose-rest-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲙ̄ⲧⲟⲛ, ⲕⲓⲙ",
        "BDAG s.v. ἀνάπαυσις"
      ],
      "reasoning": "Direct confirmed. 'Repose' for the loan and 'rest' for native ⲙ̄ⲧⲟⲛ is lexically exact, removes the 'remainder' misreading at 51 and keeps the 50→51 link; binding 90 to 'repose' is acceptable with the Mt 11:28-29 difference noted. Note for 61: ⲙ̄ⲧⲟⲛ there is reflexive (see the THOM-61 revise)."
    },
    {
      "glossary_id": "logion-50-light-and-interrogation-vocabulary-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲱϩⲉ"
      ],
      "reasoning": "Direct confirmed: 'stood' is literal, 'their' unresolved, 'Is it you?' and 'its sons' grammatical."
    },
    {
      "glossary_id": "woh-reading-logion-50-origin-from-the-light-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation (ϩⲛ̄ ⲧⲟⲩϩⲓⲕⲱⲛ, plural possessive)",
        "Gen 1:26 (MT נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ; LXX κατ' εἰκόνα ἡμετέραν)",
        "TBWTT (Raël, The Book Which Tells the Truth, 1974), commentary on Gen 1:26-27"
      ],
      "reasoning": "Speculative test met: the lexical evidence is real (ⲧⲟⲩ- = ⲧⲉⲩ- is a 3pl possessive with no expressed antecedent; Gen 1:26 has the plural 'our image'), and the rationale states plainly that Thomas names no makers and the canon does not cite the saying. Apparatus only, labelled, after the mainstream reading. Advisory: the Gen 1:26-27 background of logion 50 is itself discussed in mainstream scholarship (e.g. DeConick 2006), so the paragraph could say that the speculative step is only the identification of 'their' with the Elohim."
    },
    {
      "glossary_id": "logion-46-eyes-lowered-and-little-one-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲱϭⲡ"
      ],
      "reasoning": "Inferred confirmed by a named scholar: Lambdin (in Layton ed. 1989) renders 'his eyes should not be lowered'. Literal 'broken' in commentary."
    },
    {
      "glossary_id": "ptoma-corpse-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "BDAG s.v. πτῶμα"
      ],
      "reasoning": "Direct confirmed; the ⲡⲧⲱⲙⲁ/ⲥⲱⲙⲁ distinction for the 56/80 doublet is useful."
    },
    {
      "glossary_id": "logion-57-darnel-parable-vocabulary-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Direct confirmed; matches matthew-woh; the quoted-intention parse follows Dilley's note."
    },
    {
      "glossary_id": "hise-suffer-toil-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϩⲓⲥⲉ"
      ],
      "reasoning": "Direct confirmed; both senses within the lexeme, Lambdin 'suffered'."
    },
    {
      "glossary_id": "goosht-look-watch-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϭⲱϣⲧ"
      ],
      "reasoning": "Direct; sense set by the preposition, concordant with THOM-21."
    },
    {
      "glossary_id": "logion-60-samaritan-crux-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲕⲱⲧⲉ"
      ],
      "reasoning": "Direct; literal nominal sentence printed, supplements in commentary."
    },
    {
      "glossary_id": "salome-name-thomas-woh",
      "status": "approve",
      "citations": [
        "Mk 15:40; 16:1",
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct; feminine ⲧⲉⲕ- correctly identified. The speaker-formula question it escalates is flagged for the human (see escalation verdicts)."
    },
    {
      "glossary_id": "shesh-equal-and-logion-61-crux-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲱϣ, ϣⲱϥ, ⲡⲱϣ"
      ],
      "reasoning": "Direct confirmed; statives correctly identified; Layton 1989 p. 74 is Dilley's own citation, not an invented page."
    },
    {
      "glossary_id": "mysterion-mysteries-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)"
      ],
      "reasoning": "Direct; cleft justified by the corpus's CFOC parse."
    },
    {
      "glossary_id": "logion-64-dinner-parable-vocabulary-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲙ̄ⲙⲟ"
      ],
      "reasoning": "Direct; each rendering lexically exact."
    },
    {
      "glossary_id": "logion-65-vineyard-restoration-and-crux-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes",
        "Liddell-Scott-Jones s.v. χρήστης"
      ],
      "reasoning": "Direct for the printed restoration and the manuscript crux. On the unattributed alternative: the reviewer's recollection is that ⲭⲣⲏ[ⲥⲧⲏ]ⲥ 'usurer/creditor' is the reading of the Berlin working group (Bethge et al., 1996 synopsis) and of Plisch 2008, not of Layton/Lambdin; verify before attributing. Leaving it unattributed is acceptable meanwhile."
    },
    {
      "glossary_id": "logion-67-lacking-entirely-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϭⲣⲱϩ"
      ],
      "reasoning": "Inferred confirmed by a named scholar: Lambdin's 'still feels a personal deficiency, he is completely deficient' takes the same parse (ⲟⲩⲁⲁϥ with the lack; ⲙ̄ⲡⲙⲁ ⲧⲏⲣϥ as totality)."
    },
    {
      "glossary_id": "logia-68-69-persecution-beatitudes-wording-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct; literal renderings, smoothing avoided."
    },
    {
      "glossary_id": "logion-71-destroy-and-build-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲕⲱⲧ"
      ],
      "reasoning": "Direct; 'build' not 'rebuild'."
    },
    {
      "glossary_id": "refposhe-divider-logion-72-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ⲡⲱϣ"
      ],
      "reasoning": "Direct."
    },
    {
      "glossary_id": "logion-74-jote-shone-crux-thomas-woh",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲱⲛⲉ, ϣⲱⲧⲉ",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "The rationale 'ϣⲱⲛⲉ is … securely attested … the word itself is certain' does not account for the feminine article ⲧ-, which fits feminine ϣⲱⲧⲉ 'well, cistern' and not masculine ϣⲱⲛⲉ 'sickness' (gender to be confirmed in Crum). Proposed change: wohChoice '(?)' on both nouns ('drinking trough(?)', 'sickness(?)'); rationale to add the article-gender argument as support for the emendation, while keeping the manuscript reading in the line."
    },
    {
      "glossary_id": "ma-nsheleet-bridal-chamber-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲉⲗⲉⲉⲧ"
      ],
      "reasoning": "Direct; compound correctly not rendered 'place'."
    },
    {
      "glossary_id": "logion-76-merchant-pearl-and-treasure-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Direct; 'his treasure' is the manuscript reading as the scribe corrected it, and Lambdin's."
    },
    {
      "glossary_id": "logion-52-twenty-four-prophets-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct."
    },
    {
      "glossary_id": "logion-53-circumcision-in-spirit-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Direct; not citing the central brit-milah entry is correct."
    },
    {
      "glossary_id": "register-sayings-format-and-proper-names-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "nomina-sacra-and-abbreviation-expansion-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "greek-loanword-rendering-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "coptic-base-text-and-oxyrhynchus-greek-witnesses-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "shaje-ethep-hidden-sayings-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "etonh-the-living-lowercase-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "ptirf-the-all-reign-over-the-all-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "mntero-the-kingdom-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "tpe-sky-heaven-context-rule-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "shere-son-child-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "eiot-father-capitalisation-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "mnthke-poverty-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "oua-ouot-a-single-one-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "rome-man-human-person-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "makarios-blessed-singular-formula-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "kosmos-world-kah-earth-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "ouoein-light-man-of-light-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "pneuma-sarx-soma-spirit-flesh-body-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "jpo-not-born-of-woman-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "monachos-solitary-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "eikon-image-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Ratified Block A entry: diffed against v1.0.0 (git HEAD); only appliesTo (Block B units added, none removed) and the new scopeNote changed; wohChoice, rationale and claim_type unchanged. The Block B applications listed in the scopeNote were checked against the lines and hold."
    },
    {
      "glossary_id": "topos-ma-place-thomas-woh",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϯ (imperative ⲙⲁ-)",
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)"
      ],
      "reasoning": "Diff confirmed appliesTo/scopeNote only. But THOM-66 is wrongly listed: ⲙⲁⲧⲥⲉⲃⲟⲉⲓ is imperative ⲙⲁ- (of ϯ) + ⲧⲥⲉⲃⲟ-, not ⲙⲁ 'place'. Remove THOM-66 from appliesTo and the phrase \"ⲧⲥⲁⲃⲟ 'Show me' (66)\" from the scopeNote. Rendering policy otherwise approved (idiomatic/compound ⲙⲁ at 65, 67, 75 correctly excluded)."
    },
    {
      "glossary_id": "restored-text-bracket-and-sigla-convention-thomas-woh",
      "status": "revise",
      "citations": [
        "Layton, A Coptic Grammar (2000; 3rd ed. 2011)",
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Diff confirmed appliesTo/scopeNote only; clauses (a), (b), (c), (e), (f) approved (the { } override at 76 is justified by the scribe's own correction). Clause (d) should be reworded: at 59 the negative is written (ⲛⲉ- = ⲛ̄ⲛⲉ- degeminated, as at 21/22) and at 46 the edition counts a supplied span. Proposed (d): 'Negative optatives written defectively in the manuscript (single ⲛ, THOM-59 as at 21/22) or supplied only in the normalised layer (THOM-46) are read as negatives without brackets.'"
    },
    {
      "glossary_id": "CENTRAL: iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus (+30 THOM units)",
      "status": "approve",
      "citations": [
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Verified programmatically: exactly the 30 Block B source texts containing ⲓ︤ⲥ︥ (incl. underdotted at 62); 43, 51-53, 60, 65, 72, 74 correctly excluded."
    },
    {
      "glossary_id": "CENTRAL: lacuna-bracket-convention-sumerian-mesopotamian-project-standard (+9 THOM units)",
      "status": "approve",
      "citations": [
        "Dilley (ed.), Coptic SCRIPTORIUM thomas-gospel corpus v6.2.0, editorial notes"
      ],
      "reasoning": "Verified: the nine units with single [ ] in the source (45, 50, 57, 62, 64, 65, 70, 71, 72); 63 ([[ ]], erasure) correctly excluded. The Thomas adoption sentence ratified for Block A covers these."
    },
    {
      "glossary_id": "CENTRAL: beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus (+THOM-54, 68, 69)",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "Synoptic-parallel beatitudes (Mt 5:3/Lk 6:20; Mt 5:11/Lk 6:22; Mt 5:10, 5:6/Lk 6:21); the central wohChoice ('Blessed are …') is compatible with the Thomas lines, and Thomas's differences live in the overlay. Exclusion of 49 and 58 correct."
    },
    {
      "glossary_id": "CENTRAL: kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim (+THOM-54)",
      "status": "approve",
      "citations": [
        "Layton (ed.), Nag Hammadi Codex II,2-7, vol. 1 (NHS 20, 1989): Coptic text with Lambdin's translation"
      ],
      "reasoning": "ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ is plural; the central wohChoice 'the kingdom of the heavens' matches the line, as at the ratified THOM-20 extension."
    }
  ],
  "lens-leakage-flags": [],
  "lensLeakageCheck": "Performed on all 38 English lines against the re-parsed Coptic (diplomatic text, Coptic Scriptorium normalisation and lemma layer). No English line carries a Wheel of Heaven reading: no 'Elohim', 'creators', 'planet', capitalised 'Living One' or 'Light'; 'their image' (50) is left unresolved; 'the light', 'the places of my Father' (64) and 'the bridal chamber' (75) are standard. No canonical wording is imported where the Coptic differs: 39 plural 'keys'; 44 'the Son', not 'Son of Man'; 45 no 'mouth'; 47 reversed patch and the converse wineskin case; 54 'the poor … yours … the heavens'; 57 Thomas's shortened parable; 65 'farmers', 'feel shame', no Isa 5; 71 'build', not 'rebuild'; 73 'the lord', no 'of the harvest'. The hard sayings keep the manuscript reading in the line: 42, 60 ('That one is around the lamb'), 61 ('destroyed'), 65 ('he did not know them'), 67, 68, 71 ('…'), 74 ('sickness'), 75, 76 ('his treasure'); emendations appear only in commentary. The only supplied English word is the edition's ⟨ⲁⲩⲛⲁⲩ⟩ at 60, marked '⟨They saw⟩'. The lens appears once, in the labelled last paragraph of THOM-50 pointing to the single speculative overlay entry.",
  "sourceFindingsCheck": "The `text` field of all 38 units is byte-identical to source-cop-1.json (n=39-76). Confirmed: ⲅⲛⲱⲥⲓⲥ only at 39; [ ] restorations at 45, 50, 57, 62, 64, 65, 70, 71, 72 only; [[ ]] erasure at 63; ⟨ ⟩ letter supplies at 53, 57, 67 and the whole-word supply at 60; ( ) at 47, 57, 64; {ⲉϥ} with supralinear ⲉ at 76; the 454-space run at 57; middle dots at 45, 51. Correction to the Editor's finding at 59: the diplomatic ϫⲉⲛⲉⲧⲙ̄ⲙⲟⲩ does write the negative optative (degeminated ⲛⲉ-), so it is not 'negative only in normalisation'.",
  "glossaryDiffCheck": "The 23 ratified Block A entries were diffed against `git show HEAD:gospel-of-thomas-woh/_translation-glossary.json` (v1.0.0): every difference is in appliesTo (Block B ids added only; nothing removed; no non-Block-B ids added) or the new scopeNote field; wohChoice, rationale, claim_type and all other fields are unchanged. The live overlay was byte-identical to the frozen v1.1.0 snapshot at review time.",
  "escalationVerdicts": {
    "speculative woh-reading-logion-50-origin-from-the-light-thomas-woh": "approve (apparatus only); the lexical evidence (3pl possessive with no antecedent; Gen 1:26 plural) is real and the rationale is candid. Human sign-off by name still required.",
    "repose (ⲁⲛⲁⲡⲁⲩⲥⲓⲥ) vs rest (ⲙ̄ⲧⲟⲛ), binding 90": "approve.",
    "English ⟨ ⟩ whole-word convention (60 '⟨They saw⟩')": "approve.",
    "61 no supplied '⟨Salome said:⟩'": "flag-for-human. The present English is defensible under the ratified register convention, but the Coptic marks the speaker grammatically (feminine ⲧⲉⲕ-) and the English, without a formula, invites the misreading that Jesus says 'I am your disciple'. Block A defined English ⟨ ⟩ as 'English words supplied by the Editor where no Coptic wording exists', which covers this case. Reviewer's recommendation: admit '⟨Salome said:⟩' and record it as a narrow exception (speaker identity carried by Coptic grammar alone), not as a general licence to supply formulas.",
    "76 'his treasure' vs {ⲉϥ}": "approve.",
    "74 ϣⲱⲛⲉ 'sickness' and 'drinking trough(?)' for ϫⲱⲧⲉ": "revise: '(?)' on both nouns, plus the article-gender note (see THOM-74). 'drinking trough(?)' for ϫⲱⲧⲉ approved as Lambdin's contextual rendering.",
    "65 '[good]'": "approve; alternative stays unattributed until verified (reviewer's recollection: Bethge et al. 1996 / Plisch 2008).",
    "49 'the solitary and chosen ones'": "approve; grammatically required.",
    "46 'lowered' (inferred) and 67 parse (inferred)": "approve both, each matched by Lambdin.",
    "four CENTRAL proposals (-> 2.76.0)": "approve all four; deliberate non-extensions (brit-milah, sower) also approved."
  },
  "escalationReportAdjustments": "Initial verdicts were formed from the chapter, overlay snapshot, source and lemma aid before opening chapter-1-editor-report-block-b.md. After reading it, one verdict changed: THOM-46 had been a commentary-only revise (the diplomatic ⲛⲟⲩⲱϭⲡ might contain the negative); the report shows that the lemma aid counts a supplied span at 46, so the edition itself treats the negative as supplied, and the verdict is now approve with an advisory wording note. THOM-59 stays revise: the report confirms that the lemma aid counts no supplied span there, which supports the reading that the negative is written. The report's question 7 (attribution at 65) and question 6 (ϫⲱⲧⲉ) are answered in the escalation verdicts; nothing in the report bears on the 47, 61 ('there') or 66 revises.",
  "summary": "38 unit verdicts: 33 approve, 5 revise (47 'old wineskins' plural; 59 commentary: the negative is written, degeminated; 61 delete 'there', reflexive ⲙ̄ⲧⲟⲛ ⲙ̄ⲙⲟ=; 66 drop the topos-ma glossary link, ⲙⲁ- is the imperative of ϯ; 74 'sickness(?)' + feminine-article note), 0 flag-for-human. 31 new overlay entries: 30 approve (incl. the speculative logion-50 entry and both inferred entries), 1 revise (logion-74). 23 extended entries: verified changed only in appliesTo/scopeNote; 21 approve, 2 revise (topos-ma: remove THOM-66; restored-text scopeNote (d) wording). Central: all four appliesTo extensions approved. Escalations: 61 speaker formula flagged for human with a recommendation to admit '⟨Salome said:⟩'. Lens leakage: none. Translation quality is high: literal, unsmoothed, and faithful to the Coptic; the revise items are small. Status advanced to awaiting-human."
}
```

## Editor escalation report, Block B (inlined)

# Chapter 1 Editor Report — Gospel of Thomas, Block B (logia 39-76)

## Overview

Block B covers logia 39-76 of Nag Hammadi Codex II,2: 38 paragraph objects in the separate file `chapter-1.blockB.draft.json`.
That file stays separate through review; the orchestrator merges it into `chapter-1.json` at sign-off.
Block A (`chapter-1.json`, signed off) was read only and has not been touched; neither has `_meta.json` or `source-cop-1.json`.

The Translator submitted **47 editorial_questions[]**.
This pass resolves all 47 and clears the array.
One speculative overlay entry needs sign-off by name, and nine rulings are flagged for human review.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.1.0-rc1`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.1.0`
- `translation.glossaryVersion`: `2.74.0` → `2.75.0` (the central version the Block A extensions were applied at; the central file was not touched by this pass)
- `translation.modelDrafts`: editor appended

**Commentary.** Written to `notes: {"official": …, "community": []}` as in Block A.
37 of 38 paragraphs carry commentary.
THOM-41 has none: it is a short synoptic parallel (Mk 4:25) with no divergence or source issue.

**English changes.** Seven edits in six paragraphs, each governed by an overlay entry:

| refId | Draft | Now | Entry |
|---|---|---|---|
| THOM-49 | 'the solitary ones and the chosen' | 'the solitary and chosen ones' | `sotp-chosen` |
| THOM-50 | 'movement and rest' | 'movement and **repose**' | `kim-anapausis-mton-movement-repose-rest` |
| THOM-51 | 'the rest of the dead' | 'the **repose** of the dead' | same |
| THOM-60 | 'They saw a Samaritan'; 'within rest' | '**⟨They saw⟩** a Samaritan'; 'within **repose**' | `whole-word-supply-angle-brackets-convention`; `kim-anapausis-…` |
| THOM-62 | 'I tell my mysteries to [those who are worthy] of [my] mysteries' | '**It is to** [those who are worthy] of [my] mysteries **that I tell my mysteries**' (focalising present → cleft) | `mysterion-mysteries` |
| THOM-74 | 'in the sickness(?)' | 'in the sickness' ('(?)' kept on 'drinking trough' only) | `logion-74-jote-shone-crux` |

Every other line keeps the Translator's draft, which was accurate.
No line was harmonised toward the synoptics.
The hard sayings keep the manuscript reading in the English: 42, 60, 61, 65, 67, 68, 71, 74, 75 (and 76 'his treasure').

---

## Rulings on the 47 editorial questions

All overlay ids carry the suffix `-thomas-woh`; it is omitted in the table.

| # | refId | Question | Ruling | Overlay entry (claim_type) |
|---|---|---|---|---|
| 0 | 39 | Greek overlap (P.Oxy. 655) | Coptic in the line; commentary states the Greek is largely restored and shows no secure divergence. | `coptic-base-text-…-convention` (direct, extended) |
| 1 | 39 | ⲅⲛⲱⲥⲓⲥ; ϩⲱⲡ | 'the keys of knowledge'; 'have hidden them'. | `gnosis-knowledge` (direct); `shaje-ethep-hidden-sayings` (extended) |
| 2 | 42 | Crux | 'Become passers-by.' kept; alternatives in commentary. | `parage-passers-by-logion-42` (direct) |
| 3 | 43 / 61 | Missing speech formula | No formula supplied at either place (binding register convention). 43 is clear from 'I say'. **61 escalated** (see review 4). | register convention (extended); `salome-name` (direct) |
| 4 | 43 | Jews / Judeans | 'the Jews'. | `ioudaioi-the-jews` (direct) |
| 5 | 44 | Triad; passive | 'the Father … the Son … the Holy Spirit'; 'he will be forgiven'. | `son-and-holy-spirit-triad-logion-44` (direct) |
| 6 | 45 | bad / evil | 'bad' (ⲕⲁⲕⲟⲥ, ϩⲟⲟⲩ), 'evil things' (ⲡⲟⲛⲏⲣⲟⲛ). | `kakos-poneron-hoou-bad-evil` (direct) |
| 7 | 46 | Unwritten negative; 'lowered' | Normalised negative followed, no brackets (as THOM-21); 'lowered' kept, literal 'broken' in commentary. | `logion-46-eyes-lowered-and-little-one` (**inferred**) |
| 8 | 46 | ⲉϥⲟ ⲛ̄ⲕⲟⲩⲉⲓ | 'becomes a little one'. | same; `shere-son-child` (extended) |
| 9 | 47 | ϩⲙϩⲁⲗ | 'slave' throughout (47, 64, 65). | `hmhal-slave-joeis-master-lord` (direct) |
| 10 | 47 | ϫⲟⲉⲓⲥ | 'master' (47, 64, 65); 'the lord' lower case (73); vocative 'Lord' (74). | same |
| 11 | 48 | Adjectival ⲟⲩⲱⲧ | 'single' (48, 76). | `oua-ouot-a-single-one` (extended) |
| 12 | 49 | ⲥⲱⲧⲡ; syntax | 'chosen' (49, 50). **Changed** at 49 to one group: 'the solitary and chosen ones' (bare relative ⲉⲧⲥⲟⲧⲡ needs ⲙⲟⲛⲁⲭⲟⲥ as antecedent). | `sotp-chosen` (direct) |
| 13 | 49 / 58 | Beatitude coverage | Overlay makarios entry at 49 and 58, scope extended to plural 'Blessed are' for non-synoptic beatitudes. | `makarios-blessed-singular-formula` (extended) |
| 14 | 50 | Pronouns, filial | 'its sons' (ratified 'sons' rule); 'It [stood]'; 'their image' unresolved; 'Is it you?'. | `logion-50-light-and-interrogation-vocabulary` (direct) |
| 15 | 50 | Mechanical brackets | 'It [stood] and [appeared]' kept (rule is mechanical); 'stood' is literal for ⲱϩⲉ ⲉⲣⲁⲧ=. | same |
| 16 | 50 | rest / repose | **Changed.** ⲁⲛⲁⲡⲁⲩⲥⲓⲥ = 'repose' (50, 51, 60; 90 in Block C); native ⲙ̄ⲧⲟⲛ = 'rest' (61; 86 in Block C); ⲕⲓⲙ = 'movement'. | `kim-anapausis-mton-movement-repose-rest` (direct) |
| 17 | 51 | anapausis vs anastasis | Manuscript: 'the repose of the dead'. The 'resurrection' conjecture is not printed. | same |
| 18 | 52 | 'in you'; ⲕⲱ | 'spoke in you', 'left aside' kept. | `logion-52-twenty-four-prophets` (direct) |
| 19 | 53 | Circumcision | 'in spirit' lower case; 'useful' / 'profitable'; central brit-milah **not** cited; ⟨ⲙ̄⟩ silent. | `logion-53-circumcision-in-spirit` (direct) |
| 20 | 54 | Central refs; 'yours' | Central beatitudes (54, 68, 69) and kingdom-of-the-heavens (54) cited; 'yours' kept. | CENTRAL |
| 21 | 55 | Staurogram | Silent expansion 'cross'; nomina-sacra entry scope extended to the staurogram. | `nomina-sacra-…-convention` (extended) |
| 22 | 56 | ⲡⲧⲱⲙⲁ | 'corpse' (56, 60) vs 'body' (80). | `ptoma-corpse` (direct) |
| 23 | 57 | Darnel parable | 'darnel'; 'in order to pull up'; passive for the impersonal plural; sigla silent; restorations bracketed. | `logion-57-darnel-parable-vocabulary` (direct) |
| 24 | 58 | ϩⲓⲥⲉ | 'who has suffered'. | `hise-suffer-toil` (direct) |
| 25 | 59 | ϭⲱϣⲧ ⲛ̄ⲥⲁ; negative | 'Look to the living one'; normalised negative followed, no brackets. | `goosht-look-watch` (direct) |
| 26 | 60 | ⟨ⲁⲩⲛⲁⲩ⟩ | **Changed.** '⟨They saw⟩' in English angle brackets: rule 2 covers supplied letters, not a supplied whole word. | `whole-word-supply-angle-brackets-convention` (direct) |
| 27 | 60 | Crux | Manuscript kept: 'That one is around the lamb.' | `logion-60-samaritan-crux` (direct) |
| 28 | 61 | ϩⲱⲥ ⲉⲃⲟⲗ ϩⲛ̄ⲟⲩⲁ | 'As though from someone' (indefinite ⲟⲩⲁ). | `shesh-equal-and-logion-61-crux` (direct) |
| 29 | 61 | ⲡⲉⲧϣⲏϣ | 'the one who is equal' (literal); 'the undivided' in commentary. | same |
| 30 | 61 | ϣⲏϥ crux | Manuscript kept: 'When he is destroyed'; ϣⲏϣ emendation in commentary (Dilley, citing Layton 1989, p. 74). | same |
| 31 | 61 | Salome | 'Salome', unidentified in the line; feminine ⲧⲉⲕ- explained in commentary. | `salome-name` (direct) |
| 32 | 62 | ⲙⲩⲥⲧⲏⲣⲓⲟⲛ | 'mysteries'. **Changed** to a cleft for the focalising present ⲉⲓ̈ϫⲱ. | `mysterion-mysteries` (direct) |
| 33 | 64 | Banquet vocabulary | 'guests' / 'village' / 'money due from' / 'dinner' kept. | `logion-64-dinner-parable-vocabulary` (direct) |
| 34 | 64 | Closing line | 'Buyers and [merchants will] not [enter] the places of my Father'; both merchant words 'merchants'; speaker left open. | same |
| 35 | 65 | ⲭⲣⲏ[ⲥⲧⲟ]ⲥ | Edition's restoration '[good]' kept; 'creditor/usurer' restoration in commentary, **unattributed** (see review 7). | `logion-65-vineyard-restoration-and-crux` (direct) |
| 36 | 65 | ⲙ̄ⲡⲉϥⲥⲟⲩⲱⲛⲟⲩ | Manuscript kept: 'Perhaps he did not know them'; 'farmers'; 'feel shame before'. | same |
| 37 | 67 | Parse | 'Whoever knows the All but is lacking in himself is lacking entirely.'; topos entry not applied; ⟨ϥ⟩ silent. | `logion-67-lacking-entirely` (**inferred**) |
| 38 | 68 | Crux | Literal kept; Pella allusion noted as a commentators' suggestion; ϩⲟⲧⲁ(ⲛ) finding recorded. | `logia-68-69-persecution-beatitudes-wording` (direct) |
| 39 | 69 | Wording | 'within their heart'; 'the belly of the one who desires will be filled'. | same |
| 40 | 70 | ϫⲡⲟ | 'bring forth' (context rule recorded on the jpo entry); 'within you'. | `jpo-not-born-of-woman` (extended) |
| 41 | 71 | Gap | 'build it …'; no conjecture printed. | `logion-71-destroy-and-build` (direct) |
| 42 | 72 | Brackets | 'A [man said]' (adjacent restored words share brackets, as at THOM-37). | `refposhe-divider-logion-72` (direct); restored-text (extended) |
| 43 | 74 | ϫⲱⲧⲉ / ϣⲱⲛⲉ | Editor's Coptic check below. 'drinking trough(?)' kept; **'sickness' without '(?)'**. | `logion-74-jote-shone-crux` (direct) |
| 44 | 75 | ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ | 'the bridal chamber'; the Valentinian rite is disclaimed in commentary. | `ma-nsheleet-bridal-chamber` (direct) |
| 45 | 76 | Merchant vocabulary | 'a man, a merchant … merchandise … wise … this single pearl' kept. | `logion-76-merchant-pearl-and-treasure` (direct) |
| 46 | 76 | {ⲉϥ} conflict | 'his treasure' kept: the manuscript reading (with the scribe's correction) stands; Dilley's { } deletion is reported in commentary. | same |

---

## Specific rulings requested

### Logion 74 — Coptic check of ϫⲱⲧⲉ / ϣⲱⲛⲉ

- **ϣⲱⲛⲉ is certain as a word.** It is the common Coptic for 'sickness' (Crum s.v.). The corpus lemmatises it so, and the same lemma gives ⲛⲉⲧϣⲱⲛⲉ 'the sick' at THOM-14.
  The difficulty is that the sense fits the image poorly, which is a question of suspected corruption, not of meaning.
  Dilley records the conjecture ϣⲱⲧⲉ 'well, cistern' as uncertain (Layton 1989, p. 80). Lambdin prints 'cistern'.
  The Greek saying reported by Origen (Contra Celsum 8.15-16: many around the well, no one in the well) supports the sense of the emendation.
  Ruling: manuscript in the line, 'sickness', **no '(?)'**; the emendation goes in commentary under the crux rule.
- **ϫⲱⲧⲉ is genuinely uncertain.** The Editor could not identify an attested Coptic noun of this form with a sense that fits; 'drinking trough' (Lambdin) is a contextual guess.
  Ruling: '(?)' kept on 'drinking trough', the vendidad-woh use of '(?)' for a term of uncertain meaning.
- **Source finding.** Dilley's emendation note is attached to *both* tokens in the corpus. The emendation in the literature concerns ϣⲱⲛⲉ; the duplication looks like an annotation error.
- ϣⲱⲧⲉ does occur elsewhere in Thomas (logion 96) in its other sense, 'dough'. That gives no support either way.

### Logion 60 — the whole-word supply ⟨ⲁⲩⲛⲁⲩ⟩ (rule 2 vs ⟨ ⟩)

Block A's rule 2 justifies silent rendering because bracketing a whole English word for a one-letter scribal slip would make an intact text look damaged.
That reasoning does not cover a supplied whole word: here the manuscript has no main verb, and a silent 'They saw' would tell the reader that it does.
The ⟨ ⟩ that Block A reserved for 'English words the Editor supplies where no Coptic wording exists' fits the case exactly.
Ruling: '⟨They saw⟩'. This is recorded as a refinement in a new convention entry; the ratified entry is extended only by a scope note.
This is the first use of English ⟨ ⟩ in Thomas (review 3).

### Logion 72 — the bracket merge

'A [man said]' is kept.
Both ⲟⲩⲣ[ⲱⲙ]ⲉ and [ⲡⲉ]ϫⲉ are partly restored, and adjacent bracketed English words share one pair, as in Block A's '[then you will]' (THOM-37).
'A' stands on ⲟⲩ, which is extant (underdotted only), so it is outside the bracket.

### Logia 46 and 59 — unmarked negatives

Both follow the normalised layer, without brackets, as the restored-text convention requires and as Block A ruled at THOM-21.
They differ in one respect.
At 46 the lemma aid counts a supplied span (ⲛ̄ⲛⲉⲩ-), so the edition supplies letters that `text` does not mark.
At 59 the lemma aid counts no supplied span; the negative exists only in the normalisation of ϫⲉⲛⲉⲧⲙ̄ⲙⲟⲩ to ⲛ̄ⲛⲉⲧⲛ̄ⲙⲟⲩ, as at THOM-21.
In both cases every standard translation has the negative and the context requires it.
Claim types: 46 is `inferred`, because of 'lowered', not because of the negative; 59 falls under the direct convention.

### Source anomalies (source stays immutable)

| refId | Finding | Effect on English |
|---|---|---|
| THOM-45 | Word-internal middle dot ϣⲁϥ·ⲉⲓⲛⲉ (also in the normalised layer; cf. THOM-22) | None |
| THOM-46 | Negative optative supplied in the normalised layer, unmarked in `text` (lemma aid: 1 span) | Negative followed |
| THOM-51 | Word-internal middle dot ⲛⲁ·ϥ; diplomatic ⲉⲡⲕⲟⲥⲙⲟⲥ, normalised ⲉⲣⲉⲡⲕⲟⲥⲙⲟⲥ | None |
| THOM-55 | Staurogram encoded as U+2CC1 COPTIC SMALL LETTER SAMPI instead of U+2CE8 COPTIC SYMBOL TAU RO (look-alike substitution) | None ('cross') |
| THOM-57 | A run of **454 spaces** inside `text` (offset 253, between ⲛⲧⲉⲧⲛϩⲱⲗⲉ and ⲙ̄ⲡⲥⲟⲩⲟ); the normalised layer is continuous, so nothing is missing | None |
| THOM-59 | Negative only in normalisation (lemma aid: no supplied span) | Negative followed |
| THOM-60 | ⟨ⲁⲩⲛⲁⲩ⟩ is a whole-word supply | '⟨They saw⟩' |
| THOM-63 | Rasura ⲛ̄ⲧⲁⲱ[[ϩ]]ⲥϩ with metathesis; normalised ⲛ̄ⲧⲁⲱϩⲥ; [[ ]] is a scribal erasure, not a restoration | None ('reap', no bracket) |
| THOM-65 | Lemma aid counts 4 supplied spans, `text` shows 2; normalisation supplies ⲉⲣⲉ- | None |
| THOM-68 | `text` reads ϩⲟⲧⲁⲛ unmarked; lemma aid has ϩⲟⲧⲁ(ⲛ) (1 span) | None |
| THOM-71 | Lemma aid counts 1 span, `text` shows 2 bracket groups (restoration + unrestored gap) | None |
| THOM-74 | Dilley's ϣⲱⲧⲉ note attached to both ϫⲱⲧⲉ and ϣⲱⲛⲉ | None |
| THOM-76 | {ⲉϥ}: the `orig` attribute reads ⲡ{ⲉϥ}, the token content ⲡⲉ{ϥ} (internal inconsistency); the normalised layer reads ⲡⲉϥⲁϩⲟ; the superscript ⲉ is encoded as ASCII `\bⲉ/` (literal backslash, Latin b, slash) in `text`; first ⲙⲁⲣⲅⲁⲣⲓⲧⲏⲥ POS-tagged V | 'his treasure' kept |

Recommendation for the data maintainers (not this pass): re-fetch rather than hand-edit.
Check the exporter's handling of `hi_rend="superscript"` (76), whitespace runs (57) and the staurogram code point (55), and re-check the supplied-span counts against the diplomatic sigla (65, 68, 71), as already recommended for Block A.

### The {ⲉϥ} conflict at 76 — reasoning

The manuscript has ⲡⲉϥ with an ⲉ written above the line. That scribal correction produces ⲡⲉϥⲉϩⲟ 'his treasure'.
Dilley's { } is the modern editor's deletion, not a scribal cancellation; Dilley marks scribal erasure with [[ ]], as at 63.
The normalised layer and Lambdin both read 'his treasure'.
Rule 2 (drop { } silently) was written for evident scribal surplus; here the bracket deletes a meaningful morpheme against the scribe's own correction.
Convention 6 (the manuscript reading stands; emendations in commentary) therefore governs.
The ruling is recorded in a scope note on the ratified restored-text entry and in `logion-76-merchant-pearl-and-treasure-thomas-woh` (review 5).

---

## Greek vs Coptic (Block B)

| Logion | Greek witness | Material divergence | Treatment |
|---|---|---|---|
| 39 | P.Oxy. 655 col. ii | None secure; the Greek is largely restored | Coptic; commentary |
| 40-76 | none | — | Coptic |

---

## Speculative entries requiring sign-off

### `woh-reading-logion-50-origin-from-the-light-thomas-woh` (overlay)

**Source:** Thomas 50, ⲛ̄ⲧⲁⲛⲉⲓ ⲉⲃⲟⲗ ϩⲙ̄ⲡⲟⲩⲟⲉⲓⲛ ⲡⲙⲁ ⲉⲛⲧⲁⲡⲟⲩⲟⲉⲓⲛ ϣⲱⲡⲉ ⲙ̄ⲙⲁⲩ … ⲁϥⲟⲩⲱⲛϩ ⲉ[ⲃ]ⲟⲗ ϩⲛ̄ⲧⲟⲩϩⲓⲕⲱⲛ
**WoH choice:** No effect on any English line.
One labelled paragraph in the notes of THOM-50 ('Wheel of Heaven reading (interpretive; not part of the translation)') records one resonance.
The saying answers a question of origin with a place and says that the light 'appeared in their image', with an unresolved plural; this can be read alongside Gen 1:26 'in our image' and the canon's teaching that humans were made in the image of the Elohim.
**Why speculative:** The saying names no makers, no planet and no place in the sky, and the canon does not cite it.
Reading the plural 'their' as the Elohim is an interpretive synthesis beyond any single source.
The commentary states the mainstream reading first (a catechism of origin and return, with 'the light' as the realm of origin), and the English keeps 'their' unresolved.
**Recommendation:** ship as `speculative`, apparatus only.
If declined, delete the last paragraph of the THOM-50 notes and drop the id from THOM-50's glossaryRefs. Nothing else depends on it.

This is the only point at which the lens touches Block B.
Logion 49 ('you are from it, and … you will go again') was considered and deliberately left without a lens paragraph, to keep the use sparing.

---

## Unresolved editorial questions / decisions for review

None of the 47 questions is left open. The following are judgement calls the reviewer should confirm.

### 1. `THOM-50/51/60` — 'repose' for ⲁⲛⲁⲡⲁⲩⲥⲓⲥ (English changed)

**Issue:** The draft's 'the rest of the dead' (51) reads in English as 'the remainder of the dead'.
**Options considered:** (A) 'repose' for the Greek loan, 'rest' for native ⲙ̄ⲧⲟⲛ (adopted; Lambdin's rendering); (B) 'rest' throughout; (C) 'repose' at 51 only.
**Why escalating:** (A) binds Block C (logion 90, ⲁⲛⲁ{ⲩ}ⲡⲁ⟨ⲩ⟩ⲥⲓⲥ) and creates a deliberate difference from 'rest' in Mt 11:28-29, while (C) would break the 50 → 51 link.

### 2. `THOM-49` — 'the solitary and chosen ones' (English changed)

**Issue:** The bare relative ⲉⲧⲥⲟⲧⲡ makes the blessed one group; the draft had two groups.
**Why escalating:** It is a change of the draft's syntax and touches the ratified 'solitary ones' wording, adjusted only by word order.

### 3. `THOM-60` — first use of English ⟨ ⟩ in Thomas

**Issue:** The convention is refined: supplied letters stay silent, supplied whole words are marked.
**Options considered:** '⟨They saw⟩' (adopted); silent 'They saw' (rule 2 applied literally); no verb (unidiomatic).
**Why escalating:** It refines a ratified convention. Block C should apply it, and the Block C draft already exists in the workspace.

### 4. `THOM-61` — no speech formula before 'I am your disciple'

**Issue:** The feminine ⲧⲉⲕ- shows Salome is speaking; the English cannot show it and, under the binding register convention, supplies no formula, so a reader may take Jesus as the speaker.
**Options considered:** (A) no formula, speaker explained in commentary (adopted, per the binding convention); (B) '⟨Salome said:⟩' in English angle brackets.
**Why escalating:** (B) is arguably more accurate for an English reader, but it would breach convention 1 as ratified. The Editor recommends that the human reviewer decide; if (B) is chosen, extend `whole-word-supply-angle-brackets-convention-thomas-woh` to 'speaker identification carried by Coptic grammar alone'.

### 5. `THOM-76` — 'his treasure' against the diplomatic {ⲉϥ}

**Issue:** The two corpus layers disagree. The manuscript reading (with the scribal correction) is kept over the editor's deletion.
**Why escalating:** It is the first case where convention 6 is ruled to override the silent-drop rule for { }.

### 6. `THOM-74` — '(?)' on 'drinking trough' only

**Issue:** The draft had '(?)' on both nouns. 'Sickness' is a certain word in a suspect context.
**Why escalating:** The Editor could not verify the meaning of ϫⲱⲧⲉ against Crum directly and relies on its absence from the Editor's knowledge of the lexicon; a Coptic specialist should confirm.

### 7. `THOM-65` — restoration and attribution

**Issue:** The line prints the edition's '[good]'.
The Translator attributed the alternative restoration 'usurer' to Layton/Lambdin. The Editor could not confirm that attribution, so the commentary reports the alternative restoration ⲭⲣⲏ[ⲥⲧⲏ]ⲥ without naming anyone.
**Why escalating:** It is a restoration crux with two serious options, and the attribution needs checking before anyone cites it.

### 8. `THOM-46` and `THOM-67` — the two `inferred` entries

46 'lowered' interprets ⲟⲩⲱϭⲡ 'break'; 67's parse of ⲟⲩⲁⲁϥ and ⲙ̄ⲡⲙⲁ ⲧⲏⲣϥ is one of several.
Both follow the crux rule in spirit (literal sense or alternatives in commentary), but the line takes a position.

### 9. Hard sayings kept in the manuscript reading

42, 60, 61 (ϣⲏϥ), 65 (ⲙ̄ⲡⲉϥⲥⲟⲩⲱⲛⲟⲩ), 67, 68, 71, 74, 75 and 76 keep the manuscript reading; the emendations, with attribution only where it is certain (Dilley's notes citing Layton 1989; Lambdin where the Editor is confident of the wording), are in commentary.
As in Block A, readers who know popular translations (74 'well', 65 'they did not know him') will notice the difference.

---

## Glossary changes for review

### Central glossary

None written. All proposals are in the CENTRAL section below.

### Per-translation overlay (v1.0.0 → **v1.1.0**, released 2026-11-01; semver-minor: additions and scope extensions only)

`gospel-of-thomas-woh/_translation-glossary.json`: 39 → **70 entries** (61 direct, 7 inferred, 2 speculative).

**Added (31):** 28 `direct`, 2 `inferred`, 1 `speculative`.

- **Convention (1, direct):** `whole-word-supply-angle-brackets-convention`
- **Lexical, direct (27):** `gnosis-knowledge`, `parage-passers-by-logion-42`, `ioudaioi-the-jews`, `son-and-holy-spirit-triad-logion-44`, `kakos-poneron-hoou-bad-evil`, `hmhal-slave-joeis-master-lord`, `sotp-chosen`, `kim-anapausis-mton-movement-repose-rest`, `logion-50-light-and-interrogation-vocabulary`, `ptoma-corpse`, `logion-57-darnel-parable-vocabulary`, `hise-suffer-toil`, `goosht-look-watch`, `logion-60-samaritan-crux`, `salome-name`, `shesh-equal-and-logion-61-crux`, `mysterion-mysteries`, `logion-64-dinner-parable-vocabulary`, `logion-65-vineyard-restoration-and-crux`, `logia-68-69-persecution-beatitudes-wording`, `logion-71-destroy-and-build`, `refposhe-divider-logion-72`, `logion-74-jote-shone-crux`, `ma-nsheleet-bridal-chamber`, `logion-76-merchant-pearl-and-treasure`, `logion-52-twenty-four-prophets`, `logion-53-circumcision-in-spirit`
- **Inferred (2):** `logion-46-eyes-lowered-and-little-one`, `logion-67-lacking-entirely`
- **Speculative (1):** `woh-reading-logion-50-origin-from-the-light`

**Extended (23 ratified entries; appliesTo + new `scopeNote` field only; wohChoice, rationale and claim_type unchanged):**
`register-sayings-format-and-proper-names-convention`, `restored-text-bracket-and-sigla-convention`, `nomina-sacra-and-abbreviation-expansion-convention` (staurogram), `greek-loanword-rendering-convention`, `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention`, `shaje-ethep-hidden-sayings`, `etonh-the-living-lowercase`, `ptirf-the-all-reign-over-the-all`, `mntero-the-kingdom`, `tpe-sky-heaven-context-rule`, `shere-son-child`, `eiot-father-capitalisation`, `mnthke-poverty`, `oua-ouot-a-single-one` (adjectival ⲟⲩⲱⲧ), `topos-ma-place`, `rome-man-human-person`, `makarios-blessed-singular-formula` (plural non-synoptic 'Blessed are'), `kosmos-world-kah-earth`, `ouoein-light-man-of-light`, `pneuma-sarx-soma-spirit-flesh-body`, `jpo-not-born-of-woman` (ϫⲡⲟ context rule), `monachos-solitary`, `eikon-image`.
(All ids end in `-thomas-woh`.)

glossaryRefs on every Block B unit are generated from the overlay `appliesTo` arrays plus the four central ids below, so the two cannot drift; every id resolves in the overlay v1.1.0 or central v2.75.0.

---

## CENTRAL — apply by orchestrator

Central v2.75.0 is not modified by this pass.
The proposals add no new entries and extend `appliesTo` on four existing entries: a semver-minor bump to **2.76.0**.
The Block B glossaryRefs already cite all four ids.

### 1. EXTEND `appliesTo`

| Existing central id | Add to `appliesTo` | Reason |
|---|---|---|
| `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus` (direct) | `THOM-39`, `THOM-40`, `THOM-41`, `THOM-42`, `THOM-44`, `THOM-45`, `THOM-46`, `THOM-47`, `THOM-48`, `THOM-49`, `THOM-50`, `THOM-54`, `THOM-55`, `THOM-56`, `THOM-57`, `THOM-58`, `THOM-59`, `THOM-61`, `THOM-62`, `THOM-63`, `THOM-64`, `THOM-66`, `THOM-67`, `THOM-68`, `THOM-69`, `THOM-70`, `THOM-71`, `THOM-73`, `THOM-75`, `THOM-76` (30 units) | Every Block B unit whose `text` contains the nomen sacrum ⲓ︤ⲥ︥ (including 62, where the letters are underdotted). Not added: 43, 51, 52, 53, 60, 65, 72, 74, which have no ⲓ︤ⲥ︥. |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (direct) | `THOM-45`, `THOM-50`, `THOM-57`, `THOM-62`, `THOM-64`, `THOM-65`, `THOM-70`, `THOM-71`, `THOM-72` | Units with real [ ] restorations or an unrestored [ ] gap (71). Not THOM-63, whose [[ ]] is a scribal erasure. |
| `beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus` (direct) | `THOM-54`, `THOM-68`, `THOM-69` | Confirmed synoptic-parallel beatitudes: 54 = Mt 5:3 / Lk 6:20; 68 = Mt 5:11 / Lk 6:22; 69 = Mt 5:10 and Lk 6:21 / Mt 5:6. Thomas's wording differs ('the poor', 'yours'); the Thomas form is recorded in the overlay. Not extended to 49 or 58, which have no synoptic counterpart. |
| `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim` (direct) | `THOM-54` | ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛ̄ⲙ̄ⲡⲏⲩⲉ keeps the plural: 'the kingdom of the heavens'. Thomas 54 pairs it with Luke's 'yours', which shows the plural is not tied to Matthew's wording. (Block C will add THOM-114.) |

### 2. scopeNote line (suggested)

"v2.76.0: Gospel of Thomas Block B (logia 39-76): iēsous extended to 30 further THOM units; lacuna-bracket to 9; beatitudes extended to the synoptic-parallel beatitudes THOM-54/68/69; kingdom-of-the-heavens to THOM-54. Thomas-specific decisions live in the gospel-of-thomas-woh overlay v1.1.0."

### 3. NOT extended, deliberately

- `brit-milah-circumcision-covenant` is not extended to THOM-53. It governs the Hebrew covenant term of Gen 17, and Thomas's saying has no lexical link to it (the Translator did not cite it either).
- `parable-of-the-sower-…` is not applicable to Block B.

### 4. Candidates for later promotion (no action now)

- `kim-anapausis-mton-movement-repose-rest-thomas-woh`: ἀνάπαυσις recurs in Mt 11:28-29 and across Nag Hammadi texts. Promote if a second Coptic text or Mt 11 is translated.
- `ma-nsheleet-bridal-chamber-thomas-woh`: νυμφών (Mt 9:15; Thomas 104). Promote if Mt 9 or a further Coptic text arrives.
- `hmhal-slave-joeis-master-lord-thomas-woh`: the 'slave' convention for δοῦλος already holds de facto in matthew-woh and could become a central cross-corpus entry.

No new cross-corpus entry is proposed now.

---

## Lens-routing summary

- **No English line carries the lens.** No line uses 'Elohim', 'creators', 'planet' or similar. 'Their image' (50) stays unresolved; 'the light' stays 'the light'; 'the places of my Father' (64) and 'the bridal chamber' (75) are standard renderings.
- **WoH reading.** It appears once (50), as one labelled paragraph pointing to a single speculative overlay entry, placed after the mainstream reading.
- **Mainstream framing.** Polemical and debated items are stated, not softened or adjudicated: 'the Jews' (43), the Pella suggestion (68), the Valentinian 'bridal chamber' (75).

## Escalation list (for human sign-off)

1. **SPECULATIVE:** `woh-reading-logion-50-origin-from-the-light-thomas-woh`. Sign off by name, or delete the labelled last paragraph of the THOM-50 notes and drop the id from THOM-50's glossaryRefs.
2. **Review:** 'repose' for ⲁⲛⲁⲡⲁⲩⲥⲓⲥ (English changed at 50, 51, 60; binds logion 90).
3. **Review:** '⟨They saw⟩' at 60, the first English ⟨ ⟩ and a refinement of rule 2.
4. **Review:** no '⟨Salome said:⟩' at 61 (binding convention kept; option B offered).
5. **Review:** 'his treasure' at 76 against the diplomatic {ⲉϥ}.
6. **Review:** logion 74, '(?)' on 'drinking trough' only; ϫⲱⲧⲉ to be confirmed by a Coptic specialist.
7. **Review:** logion 65, '[good]' and the unconfirmed 'usurer' attribution.
8. **Review:** 'the solitary and chosen ones' at 49 (English changed).
9. **Review:** the two `inferred` entries (46 'lowered', 67 parse).
10. **Review:** hard sayings kept in the manuscript reading (42, 60, 61, 65, 67, 68, 71, 74, 75, 76).
11. **Orchestrator:** apply the CENTRAL section (four appliesTo extensions; bump to 2.76.0) and merge Block B into `chapter-1.json` at sign-off.
12. **Data maintainers:** the source findings at 45, 46, 51, 55, 57, 59, 63, 65, 68, 71, 74 and 76 (source not edited).
