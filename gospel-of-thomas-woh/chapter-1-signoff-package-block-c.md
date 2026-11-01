# Sign-off package — Gospel of Thomas, Block C (logia 77–114)

**Status:** `awaiting-human` · `1.2.0-rc1` · central 2.76.0 (+ proposals → 2.77.0) · overlay v1.2.0 (to be rebased, see item 3)

Blocks A (0–38) and B (39–76) are signed off and merged (chapter 1.1.0). Ratifying Block C completes the Gospel of Thomas (chapter → 1.2.0, 115 units).

## Summary

| Item | Count |
|---|---|
| Units translated | 38 (n=77–114) |
| Units with commentary | 38 |
| Translator questions raised / resolved | 41 / 41 |
| New overlay entries | 35 (31 direct, 3 inferred, 1 speculative); 30 existing entries extended by appliesTo/scopeNote only |
| Central proposals | appliesTo only: iēsous (32), lacuna-bracket (15), son-of-man (THOM-86), kingdom-of-the-heavens (THOM-114) → 2.77.0 (re-derived from the source by the reviewer) |
| Reviewer unit verdicts | revise 5, approve 33 |
| Lens-leakage flags | 0 |
| New chapter field | `translation.subscriptTitle` = 'The Gospel according to Thomas' (the manuscript's closing title) |

## Items requiring decision

1. **Speculative overlay entry `woh-reading-logion-88-angels-and-prophets-thomas-woh`** — one labelled paragraph after the mainstream readings at THOM-88; English keeps "angels". Reviewer: approve, apparatus only. **Options:** keep / drop.
2. **Reviewer revise items (apply at ratification):**
   - THOM-78: "To see a reed shaken [by] the wind?" — the restored ⲉ[ⲃⲟⲗ] belongs to the preposition ⲉⲃⲟⲗ ϩⲓⲧⲛ̄ "by" (Crum CD 429b), not to the verb; fix commentary, the restored-morph convention (a), the logion-78 entry, the kim entry.
   - THOM-88: "they will give you what you have" (ⲛⲉⲧⲉⲩⲛ̄ⲧⲏⲧⲛ̄ⲥⲉ, contrasting ⲡⲉⲧⲉⲡⲱⲟⲩ "what is theirs"); commentary + angelos entry.
   - THOM-77: cite "P.Oxy. 1.27-30" (as in Block A), in commentary, the logion-77 entry and the base-text convention.
   - THOM-82: remove "Origen quotes it (Homilies on Jeremiah 20.3)" — not in the Greek homily (reviewer checked Klostermann's text).
   - THOM-102: replace "a form for which the Editor knows no meaning" with Crum CD 480a (ⲟⲩⲟⲙϥ "manger", spellings ⲟⲩⲟⲛϩϥ, ⲟⲩⲁⲛϥ) — ⲡⲟⲩⲟⲛⲉϥ read as a variant spelling.
   - Overlay quotation fixes: 97 Lambdin "she had noticed no accident"; 98 Lambdin "wanted to kill … stuck it into the wall" and "KoptHWb 311 s.v. ϣⲱⲗⲙ" for the unverifiable Crum citation; 101 remove the "[gave me falsehood]" attribution to Lambdin; 107 "When he had gone".
3. **Overlay rebase (orchestrator):** v1.2.0 was built on the pre-sign-off Block B overlay; committing it as is would silently revert five ratified Block B rulings (logion-50 refinement, logion-74 "sickness(?)", ⟨Salome said:⟩ note, topos-ma minus 66, restored-text note (d)). At ratification the ratified Block B fixes are re-applied on top (scripted), then the Block C changes stay.
4. **Approved, for completeness:** 103 "domain" (21's exception by its own criterion; Lambdin agrees); 111 rhetorical question; 102 "manger"; clefts at 77/85; the restored-letter-without-English-word convention; 86 "the Son of Man"; 104 one term for both bridal-chamber words; 105 "whore"; 90 "repose"; the subscriptTitle field; no ⟨Jesus said:⟩ at 113 (the speaker change is shown by sense alone, as at 43); all four central extensions. Confirmed citations: Lambdin at 84, 97, 98, 103, 105, 107, 111; Lucian, Timon 14 (dog and horse, not oxen); P.Oxy. 1 at 77.

## Reviewer report (Block C)

```json
{
  "reviewer": "claude-opus-5-5 acting as woh-reviewer",
  "reviewedAt": "2026-11-01T08:10:00Z",
  "verdicts": [
    {
      "refId": "THOM-77",
      "status": "revise",
      "citations": [
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (NHS 20, 1989): translation of P.Oxy. 1 (30 + 77b)",
        "Crum, A Coptic Dictionary (1939), CD 280ab s.v. ⲡⲱϩ 'break, divide' and CD 281ab s.v. ⲡⲱϩ 'reach, attain' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C2973, C2979)",
        "Layton, A Coptic Grammar (on the focalising conversion / second tenses)"
      ],
      "reasoning": "English approved: nominal sentences, two focalising second perfects as clefts, ⲡⲱϩ 'reached' / 'split' (two homonymous lemmas, confirmed), Coptic order wood-then-stone kept. Citation fix only: the Greek wording (stone first, 'the wood', 'you will find me there', 'I am there') agrees with Attridge's translation of P.Oxy. 1, but the locator 'verso, ll. 27-30' is not confirmable and conflicts with Block A's style ('P.Oxy. 1.23-30' for logion 30, no side named); change 'P.Oxy. 1 (verso, ll. 27-30)' to 'P.Oxy. 1.27-30' here, in the logion-77 entry's strongs field and in the base-text scopeNote."
    },
    {
      "refId": "THOM-78",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 429b s.v. ⲉⲃⲟⲗ ϩⲓⲧⲛ̄- 'by, through' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C4489, a compound-preposition lemma)",
        "Crum, A Coptic Dictionary (1939), CD 108ab s.v. ⲕⲓⲙ (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C1215: no compound ⲕⲓⲙ ⲉⲃⲟⲗ is listed)",
        "Crum, A Coptic Dictionary (1939), CD 377a s.v. ⲥⲱϣⲉ 'field, meadow, country'"
      ],
      "reasoning": "Exact change: 'To see a reed [shaken] by the wind?' → 'To see a reed shaken [by] the wind?'. The restored ⲉ̣[ⲃⲟⲗ] is the first half of the compound preposition ⲉⲃⲟⲗ ϩⲓⲧⲛ̄ 'by' (agent), not part of a compound verb ⲕⲓⲙ ⲉⲃⲟⲗ, so under the Editor's own morph rule the bracket belongs on 'by' and ⲕⲓⲙ (extant) is unbracketed; fix the 'Brackets' sentence of the commentary to match. Everything else stands: 'countryside' for ⲥⲱϣⲉ (not synoptic 'wilderness'), '[man who]', '[like your]', '[the soft]' (article and relative partly restored), '[will]'."
    },
    {
      "refId": "THOM-79",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲛⲁⲓⲁⲧ= (native beatitude)",
        "Lk 11:27-28; 23:29 (comparison only)"
      ],
      "reasoning": "Re-parsed: ⲛⲉⲉⲓⲁⲧⲥ ⲛ̄ⲑϩⲏ ⲛ̄ⲧⲁϩϥⲓ ϩⲁⲣⲟⲕ, relative perfects, ⲁⲩⲁⲣⲉϩ ⲉⲣⲟϥ ϩⲛ̄ⲟⲩⲙⲉ 'kept it in truth', ⲧⲁⲉⲓ ⲉⲧⲉⲙ̄ⲡⲥⲱ, ⲉⲙⲡⲟⲩϯⲉⲣⲱⲧⲉ. 'Blessed' for native ⲛⲁⲓⲁⲧ= is exact; brackets '[woman]', '[breasts]', '[her]' follow the morph rule and the unbracketed 'the womb' ([ⲛ̄] only) is correct."
    },
    {
      "refId": "THOM-80",
      "status": "approve",
      "citations": [],
      "reasoning": "ⲡⲉⲛⲧⲁϩⲥⲟⲩⲱⲛ ⲡⲕⲟⲥⲙⲟⲥ ⲁϥϩⲉ ⲉⲡⲥⲱⲙⲁ … ⲡⲕⲟⲥⲙⲟⲥ ⲙ̄ⲡϣⲁ ⲙ̄ⲙⲟϥ ⲁⲛ: literal, and the doublet difference from 56 ('a corpse' / 'the body', article included) is kept rather than harmonised."
    },
    {
      "refId": "THOM-81",
      "status": "approve",
      "citations": [
        "BDAG s.v. ἀρνέομαι"
      ],
      "reasoning": "ⲙⲁⲣⲉϥⲣ̄ⲣⲣⲟ 'let him reign' / ⲙⲁⲣⲉϥⲁⲣⲛⲁ 'let him renounce' (jussives); no object supplied where the Coptic has none; same English as 110."
    },
    {
      "refId": "THOM-82",
      "status": "revise",
      "citations": [
        "Origen, Homily 20 on Jeremiah, Greek text (Klostermann, GCS Origenes Werke 3; First1KGreek tlg2042.tlg021): section 3 checked, the saying is not there",
        "Layton, A Coptic Grammar (on the focalising conversion / second tenses)"
      ],
      "reasoning": "English approved ('Whoever is near me is near the fire, and whoever is far from me is far from the kingdom'). Citation fix: 'Origen quotes it (Homilies on Jeremiah 20.3)' could not be confirmed: the Greek Homily 20.3 does not contain the saying, and the Latin-homily locator given in secondary lists could not be checked. Remove the parenthesis and the Origen clause (e.g. 'The saying has no canonical parallel.'), unless the human verifies a locator in the Latin homilies. Advisory: the reason given for not using a cleft (ⲉϥϩⲏⲛ homographic with the circumstantial) is weak, since after the extraposed ⲡⲉⲧϩⲏⲛ ⲉⲣⲟⲉⲓ the clause must be a main clause; the parallel with ϥⲟⲩⲏⲩ is the better reason and suffices."
    },
    {
      "refId": "THOM-83",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϭⲱⲗⲡ; s.v. ⲟⲩⲱⲛϩ"
      ],
      "reasoning": "ϥⲛⲁϭⲱⲗⲡ ⲉⲃⲟⲗ: masculine subject ambiguous between ⲡⲉⲓⲱⲧ and ⲟⲩⲟⲉⲓⲛ (m.); 'He' with the alternative 'It … its' stated in commentary, as ruled at 24. 'is hidden' keeps the stative (Lambdin's 'will remain concealed' is interpretive)."
    },
    {
      "refId": "THOM-84",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲏⲣ 'how much?' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C5113)"
      ],
      "reasoning": "ϣⲁⲣⲉⲧⲛ̄ⲣⲁϣⲉ habitual 'you rejoice'; ⲉⲓⲛⲉ 'likeness' vs ϩⲓⲕⲱⲛ 'images' kept apart; negative aorists 'neither die nor become manifest'; ⲧⲉⲧⲛⲁϥⲓ ϩⲁⲟⲩⲏⲣ 'how much you will bear!' renders the plain future. Lambdin 'will have to bear' confirmed."
    },
    {
      "refId": "THOM-85",
      "status": "approve",
      "citations": [
        "Layton, A Coptic Grammar (on the focalising conversion / second tenses)"
      ],
      "reasoning": "Second perfect ⲛ̄ⲧⲁⲁⲇⲁⲙ ϣⲱⲡⲉ … focalising, so the cleft is right; ⲛⲉⲩⲁⲝⲓⲟⲥ ⲅⲁⲣ ⲡⲉ unreal protasis + preterite future apodosis 'he would not have tasted death' (tense correct). The duplicated ϯ̣ⲡ̣[ⲉ in `text` is an encoding artefact (token layer has it once); reading it once is right."
    },
    {
      "refId": "THOM-86",
      "status": "approve",
      "citations": [
        "central son-of-man-bar-enash-dan-7-13-mt-cross-corpus (v2.75.0)",
        "Mt 8:20 / Lk 9:58 (comparison only)"
      ],
      "reasoning": "ⲛⲟⲩ- plural possessive 'their [holes]', singular ⲡⲉⲩⲙⲁϩ 'their nest' kept against synoptic 'nests', 'and rest' (ⲙ̄ⲧⲟⲛ, native) kept. 'the Son of Man' follows the central convention, which explicitly does not pre-resolve the debate, and the commentary states the self-reference / 'a human being' reading; no overlay override is warranted."
    },
    {
      "refId": "THOM-87",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 88b-89a s.v. ⲁϣⲉ (ⲛ-) 'hang from, depend on' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C1019)"
      ],
      "reasoning": "ⲉⲧⲁϣⲉ ⲛ̄- 'that depends on'; ⲧⲁⲗⲁⲓⲡⲱⲣⲟⲛ/-ⲟⲥ 'wretched'; same verb and English as 112."
    },
    {
      "refId": "THOM-88",
      "status": "revise",
      "citations": [
        "BDAG s.v. ἄγγελος (1 human messenger; 2 angel)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲛ̄ⲧⲉ- (possessive 'have')",
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Exact change: 'and they will give you what is yours' → 'and they will give you what you have'. ⲛⲉⲧⲉⲩⲛ̄ⲧⲏⲧⲛ̄ⲥⲉ is 'the things that you have' (relative + possessive ⲟⲩⲛ̄ⲧⲉ-), which the Coptic contrasts with ⲡⲉⲧⲉⲡⲱⲟⲩ 'what is theirs' (possessive pronoun); 'what is yours' flattens the two constructions into a symmetry the text lacks and loses the paradox (they bring what you already have; Lambdin marks it with '(already)'). Update the 'Wording' sentence and the angelos entry's wohChoice. Lens check passed: 'angels' is the plain rendering, as at 13, and the WoH paragraph is labelled and apparatus-only."
    },
    {
      "refId": "THOM-89",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲧⲁⲙⲓⲟ 'make, create' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C4311)"
      ],
      "reasoning": "'made', not 'created', for ⲧⲁⲙⲓⲟ in a cup image (lexically exact, keeps creator vocabulary out of the line); ⲧⲉⲧⲛ̄ⲣ̄ⲛⲟⲉⲓ ⲁⲛ as a question is the standard reading."
    },
    {
      "refId": "THOM-90",
      "status": "approve",
      "citations": [
        "BDAG s.v. χρηστός (Mt 11:30 'easy')",
        "Crum, A Coptic Dictionary (1939) s.v. ⲣⲙ̄ⲣⲁϣ 'mild, gentle' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C3218)"
      ],
      "reasoning": "'easy' for ⲭⲣⲏⲥⲧⲟⲥ of a yoke is the lexicon's sense, not an import; Thomas's 'lordship' kept against Matthew's 'burden'; 'repose' applies the ratified ἀνάπαυσις rule (Block B), consistent with 50, 51, 60 and distinct from native ⲙ̄ⲧⲟⲛ 'rest' at 86."
    },
    {
      "refId": "THOM-91",
      "status": "approve",
      "citations": [
        "BDAG s.v. πειράζω"
      ],
      "reasoning": "ⲣ̄ⲡⲓⲣⲁⲍⲉ 'test' (not Luke's δοκιμάζω 'interpret'); 'the sky' under the context rule; 'the one who is in your presence you have not known' keeps the negative perfect and ⲙ̄ⲡⲉⲧⲛ̄ⲙ̄ⲧⲟ ⲉⲃⲟⲗ as at 52."
    },
    {
      "refId": "THOM-92",
      "status": "approve",
      "citations": [],
      "reasoning": "'In those days' / 'on that day' kept apart; ⲉϩⲛⲁⲓ̈ circumstantial of ϩⲛⲉ- 'be willing'; ⲧⲉⲧⲛ̄ϣⲓⲛⲉ ⲁⲛ ⲛ̄ⲥⲱⲟⲩ 'you do not seek them'."
    },
    {
      "refId": "THOM-93",
      "status": "approve",
      "citations": [
        "Coptic SCRIPTORIUM lemma layer: ⲛ- tagged ANEGOPT (negative optative) in ϫⲉⲕⲁⲥ ⲛⲟⲩⲛⲟϫⲟⲩ and ϫⲉⲛⲟⲩⲁⲁϥ"
      ],
      "reasoning": "'lest' is grammatically exact (negative optative after ϫⲉⲕⲁⲥ / ϣⲓⲛⲁ ϫⲉ). No formula supplied; pronoun mismatches kept; the gap printed '…'; '[pearls to]' (ⲥ of ⲙⲁⲣⲅⲁⲣⲓⲧⲏⲥ and the preposition restored) correct under the morph rule."
    },
    {
      "refId": "THOM-94",
      "status": "approve",
      "citations": [],
      "reasoning": "'[whoever knocks]' marks the substantial restoration; the impersonal ⲥⲉⲛⲁⲟⲩⲱⲛ ⲛⲁϥ as a passive is the normal English for the Coptic impersonal plural, not a Matthean import."
    },
    {
      "refId": "THOM-95",
      "status": "approve",
      "citations": [
        "Coptic SCRIPTORIUM lemma layer: ⲡ-ⲉⲧ-ⲉⲧⲛ-ⲛⲁ (the restored ⲉ belongs to the 2pl pronoun)"
      ],
      "reasoning": "'[it]' (ⲙ[ⲙⲟϥ]) and '[you]' (ⲧ[ⲉ]ⲧⲛ) are right under the morph rule; singular 'it' / plural 'them' kept; no 'back' added."
    },
    {
      "refId": "THOM-96",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲱⲧⲉ 'dough' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C6102)"
      ],
      "reasoning": "Kingdom compared to the woman (not the leaven); 'large loaves' kept against Matthew's three measures; brackets match restored morphs ('[is like a]', '[she hid]', '[large]', '[let]'); attributive [ⲛ] unbracketed."
    },
    {
      "refId": "THOM-97",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939), CD 212b s.v. ⲙⲁⲁϫⲉ 'ear', also 'handle' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C2328)",
        "Crum, A Coptic Dictionary (1939), CD 711b-712a s.v. ϩⲓⲥⲉ (n. m. 'labour, suffering')"
      ],
      "reasoning": "'handle' for ⲙⲁⲁϫⲉ is a lexicon sense; ϭⲉⲗⲙⲉⲉⲓ masculine resumed by ⲉϥϣⲟⲩⲉⲓⲧ 'it … empty'; 'still far off' renders the circumstantial idiomatically; Lambdin 'accident' confirmed (the overlay quote needs correcting, see glossaryReview)."
    },
    {
      "refId": "THOM-98",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 403a s.v. ⲧⲱⲕ 'be strong, firm' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C4190; C4192 ⲧⲱⲕ ⲉϩⲟⲩⲛ 'persist')",
        "KoptHWb 311 s.v. ϣⲱⲗⲙ 'draw forth' (via CDO C5833)"
      ],
      "reasoning": "Hard saying kept: the kingdom is compared to a man preparing a killing; 'great man' links ⲙⲉⲅⲓⲥⲧⲁⲛⲟⲥ to 78; 'hold firm' for ⲧⲱⲕ ⲉϩⲟⲩⲛ is within the lexical range ('be firm, persist'). Overlay attribution and Lambdin quote need correcting (see glossaryReview)."
    },
    {
      "refId": "THOM-99",
      "status": "approve",
      "citations": [],
      "reasoning": "ⲛⲁⲉⲓ ⲛⲉ resumptive 'these are'; the Coptic cleft ⲛ̄ⲧⲟⲟⲩ ⲡⲉ ⲉⲧⲛⲁⲃⲱⲕ 'It is they who will enter' kept; Thomas's extra line not harmonised away."
    },
    {
      "refId": "THOM-100",
      "status": "approve",
      "citations": [],
      "reasoning": "'a gold coin' (ⲟⲩⲛⲟⲩⲃ, not 'denarius'); ⲛⲉⲧⲏⲡ ⲁⲕⲁⲓⲥⲁⲣ 'Those who belong to Caesar'; 'God' for ⲡⲛⲟⲩⲧⲉ (no 'Elohim'); the third member 'what is mine, give it to me' kept."
    },
    {
      "refId": "THOM-101",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Hard saying kept: 'hate' and the contradictory 'love' clause both in the line; no formula supplied; gaps '…' without conjecture; brackets match restorations. The overlay's Lambdin quote wrongly includes a conjecture (see glossaryReview)."
    },
    {
      "refId": "THOM-102",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 480a s.v. ⲟⲩⲟⲙϥ 'manger' (n. m.; forms ⲟⲩⲟⲙϥ, ⲟⲩⲟⲛϩϥ, ⲟⲩⲁⲙϥ, ⲟⲩⲁⲛϥ, via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C5037)",
        "Lucian, Timon 14 (Greek text, Harmon, LCL; Perseus tlg0062.tlg022): καθάπερ τὴν ἐν τῇ φάτνῃ κύνα μήτε αὐτὴν ἐσθίουσαν τῶν κριθῶν μήτε τῷ ἵππῳ πεινῶντι ἐπιτρέπουσαν"
      ],
      "reasoning": "English approved ('a dog sleeping on the manger of oxen'). Commentary fix: replace 'a form for which the Editor knows no meaning' (and the same phrase in the logion-102 entry's rationale) with a statement that Crum lists ⲟⲩⲟⲙϥ 'manger' with variant spellings in ⲛ (ⲟⲩⲟⲛϩϥ, ⲟⲩⲁⲛϥ; CD 480a), so the diplomatic ⲡⲟⲩⲟⲛⲉϥ is best taken as a variant spelling of the same noun. `inferred` may stay (the exact spelling is unattested). Lucian, Timon 14 confirmed; note that Lucian's dog keeps a horse, not oxen, from the barley."
    },
    {
      "refId": "THOM-103",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲣⲣⲟ (ⲙⲛ̄ⲧⲉⲣⲟ 'kingdom, kingship')",
        "Lk 12:39 / Mt 24:43 (comparison only)"
      ],
      "reasoning": "'domain' for ⲙⲛ̄ⲧⲉⲣⲟ in the householder-and-robbers image is the ratified logion-21 exception applied by its own criterion (same ⲗⲏⲥⲧⲏⲥ, same girding ⲙⲟⲩⲣ … ⲉϫⲛ̄ ϯⲡⲉ); Lambdin's 'muster his domain' confirmed; the lexical identity with 'kingdom' is stated in commentary. Brackets narrowed correctly ('[he] may', ⲛ̣ⲁ extant)."
    },
    {
      "refId": "THOM-104",
      "status": "approve",
      "citations": [
        "BDAG s.v. νυμφών"
      ],
      "reasoning": "Second perfect interrogative ⲛ̄ⲧⲁⲩϫⲣⲟ ⲉⲣⲟⲉⲓ ϩⲛ̄ⲟⲩ as a passive question; pray/fast and fast/pray order kept; one English term for ⲛⲩⲙⲫⲱⲛ and native ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ (same referent) with the pair recorded in the apparatus."
    },
    {
      "refId": "THOM-105",
      "status": "approve",
      "citations": [
        "BDAG s.v. πόρνη"
      ],
      "reasoning": "Hard saying kept; lower-case 'the father and the mother' leaves the referent open (consistent with the eiot criterion); 'whore' carries the insult register of 'son of a …' and is defensible; 'son' under the ratified filial rule."
    },
    {
      "refId": "THOM-106",
      "status": "approve",
      "citations": [],
      "reasoning": "ⲛ̄ϣⲏⲣⲉ ⲙ̄ⲡⲣⲱⲙⲉ plural, zero article: 'sons of man', lower case, outside the central title convention; 'Mountain, move away' as at 48."
    },
    {
      "refId": "THOM-107",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲱϣ 'wish, desire, love' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C5257)"
      ],
      "reasoning": "'a man, a shepherd' (apposition as 76); 'it was the largest'; 'Having toiled'; ϯⲟⲩⲟϣⲕ 'I love you' within the lexical range; Lambdin 'I care for you' confirmed (overlay quote has one wording error, see glossaryReview)."
    },
    {
      "refId": "THOM-108",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Literal 'drinks from my mouth'; ⲁⲛⲟⲕ ϩⲱ ϯⲛⲁϣⲱⲡⲉ ⲉⲛⲧⲟϥ ⲡⲉ 'I myself will become he' (Lambdin's wording confirmed); ⲟⲩⲱⲛϩ ⲉⲣⲟϥ 'appear to him'."
    },
    {
      "refId": "THOM-109",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939), CD 377a s.v. ⲥⲱϣⲉ (n. f.; the restored ⲧⲁⲁ[ⲥ] agrees)"
      ],
      "reasoning": "Hard ending kept (moneylending, against 95, same English); brackets narrowed correctly at 'the one [who]' and 'to [those whom]'; '[being]' and '[did]' render partly restored converters and are acceptable."
    },
    {
      "refId": "THOM-110",
      "status": "approve",
      "citations": [],
      "reasoning": "'Whoever has found the world and become rich, let him renounce the world'; restored object marker unbracketed under the morph rule; same verb as 81."
    },
    {
      "refId": "THOM-111",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "'The heavens will be rolled up, and the earth, in your presence' keeps Coptic order; ⲡⲉⲧⲟⲛϩ ⲉⲃⲟⲗ ϩⲛ̄ⲡⲉⲧⲟⲛϩ verbal + substantive; 'will not see death' (ⲛⲁⲩ). 'Does not Jesus say …?' is Lambdin's parse (confirmed) and is marked `inferred` with the 'not that' alternative in commentary; not marking the gloss in the line is correct (text-historical claims belong in the apparatus)."
    },
    {
      "refId": "THOM-112",
      "status": "approve",
      "citations": [],
      "reasoning": "Symmetrical ⲟⲩⲟⲉⲓ … ⲉⲧⲟϣⲉ ⲛ̄- 'woe … that depends on', paired with 87."
    },
    {
      "refId": "THOM-113",
      "status": "approve",
      "citations": [
        "Block B sign-off ruling (humanRulingBlockB, 2026-11-01): ⟨Salome said:⟩ at 61 admitted only where grammar identifies the speaker"
      ],
      "reasoning": "Topicalised question kept; no formula for the reply, as at 43. Under the ratified 61 criterion 113 does not qualify (speaker change marked by sense, not grammar), so no ⟨Jesus said:⟩. 'watching out for it', 'Behold, here / there', 'spread out upon the earth', 'people' all exact."
    },
    {
      "refId": "THOM-114",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲥⲱⲕ 'draw, lead' (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C3408)"
      ],
      "reasoning": "Manuscript reading kept: 'make her male', 'makes herself male', 'women are not worthy of life'; ⲛⲁⲩ 'to them' kept (not Lambdin's 'to him'); 'Mariham'; 'the kingdom of the heavens' per central entry. Subscript title correctly kept out of the saying."
    }
  ],
  "glossaryReview": [
    {
      "glossary_id": "focalising-conversion-cleft-convention-thomas-woh",
      "status": "approve",
      "citations": [
        "Layton, A Coptic Grammar (on the focalising conversion / second tenses)"
      ],
      "reasoning": "Direct confirmed: the corpus tags CFOC at 77 and 85, and clefts continue THOM-12/62. Restricting clefts to clear contrastive cases is sound. Advisory only: at 82 the better ground for no cleft is the parallel with ϥⲟⲩⲏⲩ, not homography with the circumstantial."
    },
    {
      "glossary_id": "restored-morph-without-english-word-convention-thomas-woh",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 429b s.v. ⲉⲃⲟⲗ ϩⲓⲧⲛ̄- (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C4489)"
      ],
      "reasoning": "Convention approved as a faithful codification of Blocks A/B practice. One example is wrong: remove \"'[shaken]' 78\" from clause (a); ⲉ̣[ⲃⲟⲗ] there belongs to the compound preposition ⲉⲃⲟⲗ ϩⲓⲧⲛ̄, so 78 reads 'shaken [by] the wind' under the same rule."
    },
    {
      "glossary_id": "subscript-title-gospel-according-to-thomas-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Direct confirmed: the field mirrors source.subscriptTitle and keeps units aligned 0-114; 'The Gospel according to Thomas' renders ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲡⲕⲁⲧⲁ ⲑⲱⲙⲁⲥ. The renderer needs a template change to display it."
    },
    {
      "glossary_id": "logion-77-light-above-all-and-poh-reach-split-thomas-woh",
      "status": "revise",
      "citations": [
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (NHS 20, 1989): translation of P.Oxy. 1 (30 + 77b)",
        "Crum, A Coptic Dictionary (1939), CD 280ab and 281ab s.v. ⲡⲱϩ"
      ],
      "reasoning": "Lexical content approved (two homonymous ⲡⲱϩ verbs confirmed). Change the strongs locator 'P.Oxy. 1 verso ll. 27-30' to 'P.Oxy. 1.27-30' (side not confirmable; Block A cites the same passage without a side)."
    },
    {
      "glossary_id": "logion-78-countryside-shaken-reed-and-megistanos-great-men-thomas-woh",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 429b s.v. ⲉⲃⲟⲗ ϩⲓⲧⲛ̄-",
        "Crum, A Coptic Dictionary (1939), CD 377a s.v. ⲥⲱϣⲉ"
      ],
      "reasoning": "'countryside' and 'great men' approved. In wohChoice change 'a reed [shaken] by the wind' to 'a reed shaken [by] the wind'; in literal change 'a reed moving out by the wind' to 'a reed moving by the wind'."
    },
    {
      "glossary_id": "naiat-native-beatitude-blessed-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲛⲁⲓⲁⲧ="
      ],
      "reasoning": "Direct confirmed; native/loan pair recorded, not marked in the English."
    },
    {
      "glossary_id": "logos-word-of-the-father-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. λόγος"
      ],
      "reasoning": "Direct confirmed; capital 'Father' fits the context."
    },
    {
      "glossary_id": "arna-renounce-dynamis-power-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. ἀρνέομαι"
      ],
      "reasoning": "Direct confirmed; absolute 'renounce' at 81 avoids supplying an object."
    },
    {
      "glossary_id": "ouonh-ebol-bolp-ebol-manifest-revealed-appear-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲱⲛϩ; s.v. ϭⲱⲗⲡ (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C7668)"
      ],
      "reasoning": "Direct confirmed; state/event split for ⲟⲩⲱⲛϩ ⲉⲃⲟⲗ is consistent with Blocks A/B."
    },
    {
      "glossary_id": "logion-84-likeness-images-and-bearing-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; Lambdin quote verified verbatim."
    },
    {
      "glossary_id": "axios-mpsha-worthy-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Direct confirmed; 85 uses both forms in one sentence with no difference of sense."
    },
    {
      "glossary_id": "ashe-depend-talaiporos-wretched-ouoei-woe-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 88b-89a s.v. ⲁϣⲉ (ⲛ-)",
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; Lambdin quote verified ('dependent upon a body')."
    },
    {
      "glossary_id": "angelos-angels-and-prophets-logion-88-thomas-woh",
      "status": "revise",
      "citations": [
        "BDAG s.v. ἄγγελος",
        "Crum, A Coptic Dictionary (1939) s.v. ⲟⲩⲛ̄ⲧⲉ-"
      ],
      "reasoning": "'angels' approved (direct). In wohChoice replace \"'what is yours'\" with \"'what you have'\" to match the THOM-88 revise."
    },
    {
      "glossary_id": "woh-reading-logion-88-angels-and-prophets-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. ἄγγελος (both 'messenger' and 'angel' are real senses)",
        "Raëlian canon: TBWTT (messengers and prophets sent by the Elohim), cited by the entry only in general terms"
      ],
      "reasoning": "Speculative, apparatus only. The lexical evidence the rationale relies on is accurate (the 'messenger' range of ἄγγελος; the saying names no sender), the rationale states plainly what the reading goes beyond, the paragraph is labelled and placed after the mainstream readings, and the English keeps 'angels'. Approve; human sign-off by name still required."
    },
    {
      "glossary_id": "tamio-made-logion-89-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ⲧⲁⲙⲓⲟ"
      ],
      "reasoning": "Direct confirmed; 'made' keeps creator vocabulary out of a household image."
    },
    {
      "glossary_id": "logion-90-chrestos-easy-yoke-and-lordship-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. χρηστός",
        "Crum, A Coptic Dictionary (1939) s.v. ⲣⲙ̄ⲣⲁϣ",
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; Lambdin 'my yoke is easy and my lordship is mild' verified."
    },
    {
      "glossary_id": "logion-91-test-the-face-of-the-sky-and-kairos-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. πειράζω"
      ],
      "reasoning": "Direct confirmed; 'test' keeps Thomas's verb distinct from Luke's."
    },
    {
      "glossary_id": "logion-93-holy-to-dogs-pronouns-and-gap-thomas-woh",
      "status": "approve",
      "citations": [
        "Coptic SCRIPTORIUM lemma layer (ANEGOPT)"
      ],
      "reasoning": "Direct confirmed; 'lest' is the negative optative."
    },
    {
      "glossary_id": "homt-money-mese-interest-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Direct confirmed; shared English at 95 and 109 makes the tension visible."
    },
    {
      "glossary_id": "logion-96-leaven-parable-vocabulary-thomas-woh",
      "status": "approve",
      "citations": [
        "Crum, A Coptic Dictionary (1939) s.v. ϣⲱⲧⲉ"
      ],
      "reasoning": "Direct confirmed."
    },
    {
      "glossary_id": "logion-97-jar-of-meal-vocabulary-thomas-woh",
      "status": "revise",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939), CD 212b s.v. ⲙⲁⲁϫⲉ"
      ],
      "reasoning": "Lexical choices approved. Attribution fix in standardEnglish: Lambdin reads 'she had noticed no accident', not 'She had not noticed an accident'; quote it exactly or drop the quotation marks."
    },
    {
      "glossary_id": "logion-98-assassin-parable-vocabulary-thomas-woh",
      "status": "revise",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "KoptHWb 311 s.v. ϣⲱⲗⲙ 'draw forth' (via CDO C5833, which gives no Crum page for this sense)"
      ],
      "reasoning": "Lexical choices approved. Two attribution fixes: (1) standardEnglish misquotes Lambdin, who reads 'a certain man who wanted to kill a powerful man. In his own house he drew his sword and stuck it into the wall in order to find out whether his hand could carry through. Then he slew the powerful man' (not 'wished', 'thrust'); (2) in strongs replace \"Crum s.v. ϣⲱⲗⲙ 'draw (sword)'\" with \"KoptHWb 311 s.v. ϣⲱⲗⲙ 'draw forth'\", since the dictionary data give no Crum page for this sense."
    },
    {
      "glossary_id": "noute-god-and-logion-100-caesar-vocabulary-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Direct confirmed; 'God' without article is the exact equivalent; 'Elohim' rightly excluded."
    },
    {
      "glossary_id": "logion-101-hate-love-and-true-mother-gap-thomas-woh",
      "status": "revise",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Treatment approved. Attribution fix in standardEnglish: Lambdin prints 'For my mother [...], but my true mother gave me life'; the conjecture '[gave me falsehood]' is not his and must be removed from the quotation (and '(Lambdin, with a conjectural completion)' changed to '(Lambdin)')."
    },
    {
      "glossary_id": "logion-102-dog-in-the-manger-normalised-reading-thomas-woh",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 480a s.v. ⲟⲩⲟⲙϥ (via Coptic Dictionary Online (coptic-dictionary.org, Crum-based) C5037)",
        "Lucian, Timon 14 (Harmon, LCL; Perseus Greek text)"
      ],
      "reasoning": "`inferred` approved; Lucian, Timon 14 confirmed. In rationale replace 'for which the Editor knows no meaning' with the Crum evidence: ⲟⲩⲟⲙϥ 'manger' is listed with ⲛ-spellings ⲟⲩⲟⲛϩϥ and ⲟⲩⲁⲛϥ (CD 480a), so ⲡⲟⲩⲟⲛⲉϥ is best read as a variant spelling. This answers the Editor's question 4; whether to upgrade to `direct` is optional."
    },
    {
      "glossary_id": "logion-103-householder-domain-and-robbers-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "`inferred` approved: the widening meets the exception's own criterion (identical householder-and-robbers image as 21), Lambdin's 'muster his domain' is verified, and the lexical identity is kept visible."
    },
    {
      "glossary_id": "nymphios-nymphon-bridegroom-bridal-chamber-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. νυμφών"
      ],
      "reasoning": "Direct confirmed; same referent, pair recorded, no Valentinian import."
    },
    {
      "glossary_id": "logion-105-father-mother-son-of-a-whore-thomas-woh",
      "status": "approve",
      "citations": [
        "BDAG s.v. πόρνη",
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; 'whore' defensible for the insult register; Lambdin 'harlot' verified."
    },
    {
      "glossary_id": "logion-106-sons-of-man-plural-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; Lambdin 'the sons of man' verified."
    },
    {
      "glossary_id": "logion-107-shepherd-and-largest-sheep-thomas-woh",
      "status": "revise",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Choices approved. Attribution fix in standardEnglish: Lambdin reads 'When he had gone to such trouble', not 'After he had gone to such trouble'."
    },
    {
      "glossary_id": "logion-108-drink-from-my-mouth-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; Lambdin quote verified."
    },
    {
      "glossary_id": "logion-109-hidden-treasure-parable-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; Lambdin quote verified."
    },
    {
      "glossary_id": "logion-111-the-living-one-and-gloss-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "`inferred` approved; Lambdin quote verified; the οὐχ ὅτι alternative is stated."
    },
    {
      "glossary_id": "logion-113-kingdom-spread-out-upon-the-earth-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)"
      ],
      "reasoning": "Direct confirmed; consistent with the ratified 61 criterion (no supplied formula at 113)."
    },
    {
      "glossary_id": "logion-114-make-her-male-manuscript-reading-thomas-woh",
      "status": "approve",
      "citations": [
        "Lambdin's translation of Thomas (Layton ed., Nag Hammadi Codex II,2-7, NHS 20, 1989; wording checked against the reprint in The Nag Hammadi Library in English at gnosis.org/naghamm/gthlamb.html)",
        "Crum, A Coptic Dictionary (1939) s.v. ⲥⲱⲕ"
      ],
      "reasoning": "Direct confirmed; Lambdin quote verified."
    },
    {
      "glossary_id": "register-sayings-format-and-proper-names-convention-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "nomina-sacra-and-abbreviation-expansion-convention-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "greek-loanword-rendering-convention-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "shaje-ethep-hidden-sayings-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "etonh-the-living-lowercase-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "jitpe-mpmou-taste-death-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "ptirf-the-all-reign-over-the-all-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "mntero-the-kingdom-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "tpe-sky-heaven-context-rule-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "shere-son-child-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "eiot-father-capitalisation-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "oua-ouot-a-single-one-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "rome-man-human-person-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "makarios-blessed-singular-formula-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "sower-parable-coptic-form-and-eisheete-behold-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "kosmos-world-kah-earth-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "ouoein-light-man-of-light-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "pneuma-sarx-soma-spirit-flesh-body-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "mariham-name-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "eikon-image-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "psyche-soul-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "hmhal-slave-joeis-master-lord-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "ptoma-corpse-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "hise-suffer-toil-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "goosht-look-watch-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "ma-nsheleet-bridal-chamber-thomas-woh",
      "status": "approve",
      "citations": [],
      "reasoning": "Extension verified: only appliesTo (Block C ids added) and appended scopeNote text differ from the Block B snapshot; the Block C scope note is accurate."
    },
    {
      "glossary_id": "restored-text-bracket-and-sigla-convention-thomas-woh",
      "status": "revise",
      "citations": [],
      "reasoning": "Block C appendix approved. Rebase required (see glossaryDiffCheck): the live entry carries the pre-sign-off wording of note (d); restore the signed-off (HEAD 5cbd4f2) wording and re-append the v1.2.0 Block C text."
    },
    {
      "glossary_id": "topos-ma-place-thomas-woh",
      "status": "revise",
      "citations": [],
      "reasoning": "Block C addition (THOM-86) approved. Rebase required: the live entry re-adds THOM-66 and its scope note, which the Block B sign-off removed; take the HEAD 5cbd4f2 entry and add only THOM-86 and the Block C scope sentence."
    },
    {
      "glossary_id": "kim-anapausis-mton-movement-repose-rest-thomas-woh",
      "status": "revise",
      "citations": [
        "Crum, A Coptic Dictionary (1939), CD 429b s.v. ⲉⲃⲟⲗ ϩⲓⲧⲛ̄-"
      ],
      "reasoning": "90 'repose' and 86 'rest' approved. In the Block C scope sentence replace 'The verb ⲕⲓⲙ ⲉⲃⲟⲗ of a reed in the wind is 'shaken' (78)' with 'The verb ⲕⲓⲙ of a reed moved by (ⲉⲃⲟⲗ ϩⲓⲧⲛ̄) the wind is 'shaken' (78)'."
    },
    {
      "glossary_id": "coptic-base-text-and-oxyrhynchus-greek-witnesses-convention-thomas-woh",
      "status": "revise",
      "citations": [
        "Attridge, 'The Greek Fragments', in Layton (ed.), Nag Hammadi Codex II,2-7 (NHS 20, 1989): translation of P.Oxy. 1 (30 + 77b)"
      ],
      "reasoning": "Block C appendix approved in substance; change 'P.Oxy. 1 verso ll. 27-30' to 'P.Oxy. 1.27-30' (side not confirmable)."
    },
    {
      "glossary_id": "central: iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus (appliesTo + 32 THOM ids)",
      "status": "approve",
      "citations": [],
      "reasoning": "Verified by script: exactly the 32 Block C units whose `text` has the name (incl. ⲓⲏ︤ⲥ︥ 90, ⲓⲥ 94, restored 95, 111); 79, 91, 93, 99, 101, 113 correctly excluded; glossaryRefs match."
    },
    {
      "glossary_id": "central: lacuna-bracket-convention-sumerian-mesopotamian-project-standard (appliesTo + 15 THOM ids)",
      "status": "approve",
      "citations": [],
      "reasoning": "Verified by script: exactly the 15 units with [ ] restorations or gaps; 107 ([[ ]] only) correctly excluded."
    },
    {
      "glossary_id": "central: son-of-man-bar-enash-dan-7-13-mt-cross-corpus (appliesTo + THOM-86)",
      "status": "approve",
      "citations": [],
      "reasoning": "Singular arthrous ⲡϣⲏⲣⲉ ⲙ̄ⲡⲣⲱⲙⲉ; entry does not pre-resolve the debate; 106 correctly excluded."
    },
    {
      "glossary_id": "central: kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim (appliesTo + THOM-114)",
      "status": "approve",
      "citations": [],
      "reasoning": "ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛⲙ̄ⲡⲏⲩⲉ, completing 20, 54, 114. Version note: central is now 2.76.0 in chapter-1.json (Block B applied), so this is 2.77.0."
    }
  ],
  "lens-leakage-flags": [],
  "lensLeakageCheck": "Performed on all 38 English lines against the re-parsed Coptic (diplomatic text, normalisation and lemma layer). No English line carries a Wheel of Heaven reading: 77 'the light', 'the All'; 88 'angels' (lexical; the WoH paragraph is labelled, apparatus-only, after the mainstream readings); 89 'made'; 100 'God'; 114 'a living spirit' lower case. No canonical wording is imported where the Coptic differs: 78 'countryside', not 'wilderness'; 86 singular 'nest'; 90 'lordship', not 'burden'; 91 'test', not 'interpret'; 96 'large loaves'; 100 'a gold coin' plus the third member; 107 'the largest' and 'more than the ninety-nine'; 113 no supplied formula. 'easy' (90) and the passive at 94 are lexical/grammatical, not imports. Hard sayings stand in the manuscript reading: 93 (no formula, pronoun mismatches, gap), 98, 101 (hate and love), 105 ('son of a whore'), 109 (moneylending against 95), 111 (unmarked third-person clause), 114 ('make her male'). The only smoothing found is 88 'what is yours' (not lens-related), handled as a revise.",
  "citationVerification": [
    {
      "citation": "Lambdin 84 'will have to bear'",
      "result": "confirmed",
      "note": "verbatim"
    },
    {
      "citation": "Lambdin 97 'accident'",
      "result": "confirmed (commentary)",
      "note": "Lambdin: 'she had noticed no accident'. The overlay standardEnglish misquotes it ('She had not noticed an accident'): fix"
    },
    {
      "citation": "Lambdin 98 'carry through'",
      "result": "confirmed (commentary)",
      "note": "overlay standardEnglish has 'wished' and 'thrust' where Lambdin has 'wanted' and 'stuck': fix"
    },
    {
      "citation": "Lambdin 103 'domain'",
      "result": "confirmed",
      "note": "'muster his domain'"
    },
    {
      "citation": "Lambdin 105 'harlot'",
      "result": "confirmed",
      "note": "'the son of a harlot'"
    },
    {
      "citation": "Lambdin 107 'I care for you'",
      "result": "confirmed (commentary)",
      "note": "overlay standardEnglish has 'After he had gone' where Lambdin has 'When he had gone': fix"
    },
    {
      "citation": "Lambdin 111 'Does not Jesus say'",
      "result": "confirmed",
      "note": "'Does not Jesus say, \"Whoever finds himself is superior to the world?\"'"
    },
    {
      "citation": "Lambdin 101 (overlay standardEnglish) '[gave me falsehood]'",
      "result": "not confirmable: remove",
      "note": "not in the Editor's list; Lambdin prints 'For my mother [...]'"
    },
    {
      "citation": "Origen, Homilies on Jeremiah 20.3 (82)",
      "result": "not confirmable: remove",
      "note": "Greek Hom. 20.3 (Klostermann GCS, First1KGreek tlg2042.tlg021) checked and does not contain the saying; the Latin-homily locator in secondary lists was not checked"
    },
    {
      "citation": "Lucian, Timon 14 (102)",
      "result": "confirmed",
      "note": "Perseus Greek (Harmon): τὴν ἐν τῇ φάτνῃ κύνα μήτε αὐτὴν ἐσθίουσαν τῶν κριθῶν μήτε τῷ ἵππῳ πεινῶντι ἐπιτρέπουσαν"
    },
    {
      "citation": "P.Oxy. 1 Greek at 77b",
      "result": "wording confirmed in substance; locator not confirmable",
      "note": "the order (stone, then wood), 'the stone', 'the wood', 'you (sg.) will find me there' and 'I am there' agree with Attridge's and Doresse's translations; 'verso, ll. 27-30' should become 'P.Oxy. 1.27-30'"
    },
    {
      "citation": "Crum s.v. ϣⲱⲗⲙ 'draw (sword)' (98 entry)",
      "result": "not confirmable: replace",
      "note": "CDO C5833 gives this sense from KoptHWb 311 only, with no Crum page"
    }
  ],
  "sourceFindingsCheck": "The `text` of all 38 units is byte-identical to source-cop-1.json (77-114). Confirmed: duplicated ϯ̣ⲡ̣[ⲉ at 85 (token layer once); ⲓⲥ without overline at 94; ⲡⲟⲩⲟⲛⲉϥ at 102; stray '/' at 103; [[ ]] at 79, 107; { }/⟨ ⟩ metathesis at 90. Added: ⲡⲟⲩⲟⲛⲉϥ is close to Crum's variant spellings of ⲟⲩⲟⲙϥ (ⲟⲩⲟⲛϩϥ, ⲟⲩⲁⲛϥ; CD 480a). The iēsous (32) and lacuna-bracket (15) unit lists were re-derived from `text` by script and match the glossaryRefs and the CENTRAL proposals; every glossaryRef resolves, and glossaryRefs equal the overlay appliesTo arrays.",
  "glossaryDiffCheck": "Against the Block B snapshot (v1.1.0-blockB-snapshot.json) the live overlay v1.2.0 adds 35 entries and changes 30 existing entries only in appliesTo (additions) and appended scopeNote text, as claimed. BUT Block B was signed off and merged after the Editor's pass (commit 5cbd4f2, overlay v1.1.0 at HEAD), and the live v1.2.0 is built on the pre-sign-off snapshot. Committed as is, it would silently revert five ratified Block B sign-off changes: woh-reading-logion-50-origin-from-the-light-thomas-woh (rationale sentence on DeConick/Genesis 1 deleted), logion-74-jote-shone-crux-thomas-woh (wohChoice 'sickness(?)' and the ratified rationale lost), whole-word-supply-angle-brackets-convention-thomas-woh (THOM-61 and the '⟨Salome said:⟩' ruling dropped), topos-ma-place-thomas-woh (THOM-66 re-added), restored-text-bracket-and-sigla-convention-thomas-woh (old note (d)). Required before commit: rebase v1.2.0 on HEAD's v1.1.0. Take those five entries from HEAD and re-apply only the Block C appliesTo/scopeNote additions (topos-ma: +THOM-86 and its sentence; restored-text: +Block C ids and its sentence; the other three have no Block C change).",
  "escalationVerdicts": {
    "1 speculative woh-reading-logion-88": "approve (apparatus only); lexical evidence accurate and rationale candid. Human sign-off by name still required.",
    "2 103 'domain'": "approve. Same image and criterion as the ratified 21 exception; Lambdin verified.",
    "3 111 rhetorical question, no gloss marking": "approve. Lambdin's parse, `inferred`, alternative stated; marking a gloss in the line would be a text-historical claim.",
    "4 102 'manger' from the normalised layer": "approve the English; revise the commentary/rationale with Crum's ⲛ-spellings (CD 480a). `inferred` may stay; `direct` is optional.",
    "5 clefts at 77/85": "approve.",
    "6 morph-level bracket convention and five bracket fixes": "approve the convention and the fixes at 93, 97, 103, 109 and 78 '[man who]'; revise 78 '[shaken] by' → 'shaken [by]' (ⲉⲃⲟⲗ ϩⲓⲧⲛ̄ compound preposition).",
    "7 86 'the Son of Man'": "approve under the central convention; no overlay override.",
    "8 104 one term for both bridal-chamber words": "approve.",
    "9 105 'whore', lower-case father/mother": "approve.",
    "10 90 'repose'": "approve (ratified Block B rule).",
    "11 subscriptTitle field": "approve; orchestrator carries it into chapter-1.json at the merge; display needs a template change.",
    "12 hard sayings": "approve: all seven in the manuscript reading.",
    "13 citations": "see citationVerification: four removals or replacements (Origen locator; the [gave me falsehood] attribution; Crum for ϣⲱⲗⲙ; P.Oxy. side) and three overlay misquotes corrected; no English line changes.",
    "14 113 vs 61 ⟨Salome said:⟩": "The human adopted ⟨Salome said:⟩ at 61 (humanRulingBlockB) as a narrow exception where grammar identifies the speaker. 113 does not meet it (speaker change by sense only, as at 43), so no ⟨Jesus said:⟩. Optional: cite the 61 ruling in the 113 commentary.",
    "15 CENTRAL (four appliesTo extensions)": "approve all four; central is 2.76.0 at HEAD, so this is 2.77.0 and the Block C translation.glossaryVersion should be updated at application."
  },
  "escalationReportAdjustments": "Initial verdicts were formed from the chapter, overlay, source, lemma aid, Block A/B files and the external checks before opening chapter-1-editor-report-block-c.md. After reading it no verdict changed. The report's question 4 (102) is answered by the Crum forms found independently. Its review 11 says Block B's revises 'can be applied on top'. They now must be, because Block B was signed off after the report was written; that point is recorded in glossaryDiffCheck. Its statement that 113 is 'marked by sense, not by grammar' agrees with the 113 verdict.",
  "summary": "38 unit verdicts: 33 approve, 5 revise (77 citation locator; 78 'shaken [by]'; 82 remove the unconfirmed Origen locator; 88 'what you have'; 102 commentary on ⲟⲩⲟⲙϥ spellings), 0 flag-for-human. Two revises change English lines (78, 88). 35 new overlay entries: 26 approve (including the speculative 88 entry and the 103 and 111 inferred entries), 9 revise (restored-morph example; logion-77 locator; logion-78 wording; angelos wohChoice; 97, 98, 101 and 107 Lambdin quotes or attributions; logion-102 rationale). 30 extended entries: 26 approve, 4 revise (kim and base-text scope sentences; topos-ma and restored-text rebase). Blocking finding: the live overlay v1.2.0 predates the Block B sign-off (HEAD 5cbd4f2) and would revert five ratified changes if committed; it must be rebased. Central: all four appliesTo extensions approved (now 2.77.0). Lens leakage: none. Status advanced to awaiting-human."
}
```

## Editor escalation report, Block C (inlined)

# Chapter 1 Editor Report — Gospel of Thomas, Block C (logia 77-114)

## Overview

Block C covers logia 77-114 of Nag Hammadi Codex II,2: 38 paragraph objects in the separate file `chapter-1.blockC.draft.json`.
That file stays separate through review; the orchestrator merges it into `chapter-1.json` at sign-off.
`chapter-1.json` (Block A, signed off), `chapter-1.blockB.draft.json` (Block B, under review), `_meta.json` and `source-cop-1.json` were read only and not touched.

The Translator submitted **41 editorial_questions[]**.
This pass resolves all 41 and clears the array.
One speculative overlay entry needs sign-off by name, and the rulings listed under "Decisions for review" are flagged for human review.

The draft was made against overlay v1.0.0, before the Block B edit.
It has been brought into line with the v1.1.0 conventions: 'repose' for ⲁⲛⲁⲡⲁⲩⲥⲓⲥ at 90; English ⟨ ⟩ reserved for an editor-supplied whole word (no such case in Block C); Block B's bracket merging (78, 93); 'the body' at 80 against 'corpse' at 56/60; one English term for the two bridal-chamber words at 75/104; and the appositive 'a man, a shepherd' (107) as at 76.

## Status advance

- `translation.status`: `draft` → `editor-review`
- `translation.version`: `1.0.0-draft` → `1.2.0-rc1`
- `translation.overlayGlossaryVersion`: `1.0.0` → `1.2.0`
- `translation.glossaryVersion`: `2.75.0`, unchanged (the central file was not touched)
- `translation.modelDrafts`: editor appended
- `translation.subscriptTitle`: **new** chapter-level field (see "Subscript title" below)
- `translation.scope`: updated to say that Block B is under review and that `subscriptTitle` must be carried over at the merge

**Commentary.** Written to `notes: {"official": …, "community": []}` as in Blocks A and B.
All 38 paragraphs carry commentary.
Every Block C unit has either a divergence from the standard reading, a bracket or source issue, or a cross-reference that the reader needs.

**English changes.** Eight paragraphs changed, each governed by an overlay entry:

| refId | Draft | Now | Entry |
|---|---|---|---|
| THOM-77 | 'From me the All came forth, and to me the All has reached' | '**It is** from me **that** the All came forth, and **it is** to me **that** the All has reached' | `focalising-conversion-cleft-convention`; `logion-77-…` |
| THOM-78 | 'a [man] [who] has' | 'a [man who] has' (adjacent brackets merged, as at 72) | `restored-morph-without-english-word-convention` |
| THOM-85 | 'From a great power and a great wealth Adam came into being' | '**It is** from a great power and a great wealth **that** Adam came into being' | `focalising-conversion-cleft-convention` |
| THOM-90 | 'you will find rest' | 'you will find **repose**' | `kim-anapausis-mton-movement-repose-rest` (Block B rule) |
| THOM-93 | 'the [pearls] [to] the swine' | 'the [pearls to] the swine' | `restored-morph-…` |
| THOM-97 | 'The kingdom of the [Father is like]' | 'The kingdom of the [Father] is like' (the restored ⲉⲥ- has no English word; 'is like' renders the extant stative) | `restored-morph-…` |
| THOM-103 | 'so that [he may] rise, gather his [kingdom]' | 'so that [he] may rise, gather his [**domain**]' | `logion-103-householder-domain-and-robbers` (**inferred**); `restored-morph-…` |
| THOM-109 | '[the one who] bought'; '[to those whom]' | 'the one [who] bought'; 'to [those whom]' (extant ⲡ̣ and ⲛ̣ moved outside the brackets) | `restored-morph-…` |

Every other line keeps the Translator's draft, which was accurate.
No line was harmonised toward the synoptics.
The hard sayings keep the manuscript reading in the English: 93 (pronouns, gap), 98 (the assassin), 101 (hate and love), 105 ('the son of a whore'), 109 (the moneylender ending, against 95), 111 (the third-person clause) and 114 ('make her male').

---

## Rulings on the 41 editorial questions

All overlay ids carry the suffix `-thomas-woh`; it is omitted in the table.
Numbering follows the order of the Translator's array.

| # | refId | Question | Ruling | Overlay entry (claim_type) |
|---|---|---|---|---|
| 1 | 77 | Greek overlap (P.Oxy. 1, 77b joined to 30) | Coptic in the line. Commentary gives the Greek text, its order (stone, then wood), the definite 'the wood', ἔγειρον, and the ⲡⲱϩ catchword. The THOM-30 commentary (Block A, read only) already records the overlap from the other side. | `coptic-base-text-…-convention` (extended); `logion-77-light-above-all-and-poh-reach-split` (direct) |
| 2 | 77 | 'above them all'; cleft vs fronting; 'reached' | 'above them all' and 'the All' kept; **changed** to clefts for the two second perfects; 'has reached' and 'split' (pun in commentary); 'a piece of wood'. | same; `focalising-conversion-cleft-convention` (direct, new) |
| 3 | 78 | countryside / shaken / great men | All three kept. ⲥⲱϣⲉ stays 'field' at 21/109. 'Wilderness' is not imported. | `logion-78-countryside-shaken-reed-and-megistanos-great-men` (direct); `kim-anapausis-…` (extended) |
| 4 | 78 | Bracket mapping inside bound groups | Morph level, as drafted. **Changed:** adjacent '[man] [who]' merged to '[man who]'. | `restored-morph-without-english-word-convention` (direct, new) |
| 5 | 79 | Native ⲛⲉⲉⲓⲁⲧ= vs ⲙⲁⲕⲁⲣⲓⲟⲥ; λόγος | 'Blessed' kept (ⲛⲁⲓⲁⲧ= is the Sahidic NT word for μακάριος); pair recorded in the apparatus. 'the word of the Father' (λόγος, its only occurrence in Thomas). Central beatitudes not cited (Lk 11/23 parallel). | `naiat-native-beatitude-blessed` (direct); `logos-word-of-the-father` (direct) |
| 6 | 79 (86, 96, 102, 109, 110) | Restored morphs with no English word | **Ruled once:** morph level, consistent with Block A ('[then you will] see', 37) and Block B ('within [you]', 70). No bracket where no English word renders the restored morph; each such restoration is named in commentary. Restored adverbs in compound verbs bracket the verb (50, 78, 109). Extant letters never stand inside a bracket. | `restored-morph-without-english-word-convention` (direct) |
| 7 | 80 | Doublet of 56 | 'the body' kept (ⲥⲱⲙⲁ, definite). 'A corpse' (56) and 'the body' (80) stay apart. | `pneuma-sarx-soma-…` (extended); `ptoma-corpse` (extended, cited for the contrast); `axios-mpsha-worthy` (direct) |
| 8 | 81/110 | ⲁⲣⲛⲁ; object at 81; ⲇⲩⲛⲁⲙⲓⲥ | 'renounce' at both; no object supplied at 81; 'power' (21, 81, 85). | `arna-renounce-dynamis-power` (direct) |
| 9 | 82 | Focalising ⲉϥϩⲏⲛ? | Plain order: the ⲉ- form is homographic with the circumstantial and the parallel clause has the plain present ϥⲟⲩⲏⲩ. | `focalising-conversion-cleft-convention` |
| 10 | 83 | He/it; manifest/revealed/appear | 'He' (the Father), 'it' in commentary, as at 24. ⲟⲩⲱⲛϩ ⲉⲃⲟⲗ 'manifest', ϭⲱⲗⲡ ⲉⲃⲟⲗ 'revealed', ⲟⲩⲱⲛϩ ⲉ- 'appear to' (108). | `ouonh-ebol-bolp-ebol-manifest-revealed-appear` (direct); `ouoein-…` (extended) |
| 11 | 84 | likeness/images; before; exclamation | As drafted. | `logion-84-likeness-images-and-bearing` (direct) |
| 12 | 85 | Counterfactual tense with 'taste death' | **Ruled:** lexeme kept, tense rendered: 'had he been worthy, [he would] not [have tasted] death'. Recorded as a scope note on the ratified entry (consistent with the Block A sign-off correction '85 taste death'). | `jitpe-mpmou-taste-death` (extended) |
| 13 | 85 | Cleft; worthy pair | **Changed** to a cleft; 'worthy' for both ⲁⲝⲓⲟⲥ and ⲙ̄ⲡϣⲁ. | `focalising-…`; `axios-mpsha-worthy` |
| 14 | 86 | 'the Son of Man' | Central `son-of-man-bar-enash-dan-7-13-mt-cross-corpus` applied (id verified in central v2.75.0). Capital follows the central convention, not a ruling; the commentary says so and gives the self-reference / 'human being' readings. appliesTo extension proposed below. 'rest' for native ⲙ̄ⲧⲟⲛ. | CENTRAL; `kim-anapausis-…`, `topos-ma-place` (extended) |
| 15 | 87/112 | depend / hang | 'depends on' at both; 'wretched' / 'woe'. | `ashe-depend-talaiporos-wretched-ouoei-woe` (direct) |
| 16 | 88 | angels / messengers | 'angels' kept in the line. The 'messenger' sense is stated in commentary. The lens reading goes into one labelled paragraph and a separate speculative entry. | `angelos-angels-and-prophets-logion-88` (direct); `woh-reading-logion-88-angels-and-prophets` (**speculative**) |
| 17 | 89 | made / created | 'made'. | `tamio-made-logion-89` (direct) |
| 18 | 90 | easy, lordship, gentle, rest | 'easy', 'lordship', 'gentle' kept; **changed** 'rest' → 'repose' (binding Block B rule, approved by the Block B reviewer). | `logion-90-chrestos-easy-yoke-and-lordship` (direct); `kim-anapausis-…`, `hmhal-…` (extended) |
| 19 | 91 | sky/heaven; test; kairos | 'the sky' (weather image), 'test', 'this moment'. | `logion-91-test-the-face-of-the-sky-and-kairos` (direct); `tpe-…` (extended) |
| 20 | 93 | No formula; gap; pronouns | No formula supplied; possible continuation of 92 noted; 'lest they make it …' without conjecture; pronouns as written; **changed** bracket merge '[pearls to]'. | `logion-93-holy-to-dogs-pronouns-and-gap` (direct) |
| 21 | 94 | Restored second clause; ⲓⲥ without overline | Dilley's restoration printed in brackets, '[whoever knocks]'. ⲓⲥ expanded silently; recorded as a source finding. | `restored-text-…`, `nomina-sacra-…` (extended) |
| 22 | 95 | Pronouns; 'back' | As drafted: 'give [it] … receive them'; no 'back'. | `homt-money-mese-interest` (direct) |
| 23 | 96 | leaven parable | As drafted; 'leaven' (matthew-woh). | `logion-96-leaven-parable-vocabulary` (direct) |
| 24 | 97 | handle/ear; ϩⲓⲥⲉ | 'handle' (ear-word in commentary), 'any trouble'. **Changed** bracket: '[Father] is like'. | `logion-97-jar-of-meal-vocabulary` (direct); `hise-suffer-toil` (extended) |
| 25 | 98 | great man; hold firm; two 'kill' verbs | As drafted. | `logion-98-assassin-parable-vocabulary` (direct); `logion-78-…` |
| 26 | 100 | ⲡⲛⲟⲩⲧⲉ | 'God' (singular with article), as matthew-woh's θεός; 30 stays 'gods'. | `noute-god-and-logion-100-caesar-vocabulary` (direct) |
| 27 | 101 | No formula; love clause; gap | As drafted; no conjecture printed. | `logion-101-hate-love-and-true-mother-gap` (direct) |
| 28 | 102 | ⲡⲟⲩⲟⲛⲉϥ / ⲡⲟⲩⲟⲙϥ | Normalised reading 'manger' followed, without '(?)'; labelled inferred. | `logion-102-dog-in-the-manger-normalised-reading` (**inferred**) |
| 29 | 103 | 'kingdom' vs 21's 'domain' | **Changed** to 'gather his [domain]': the 21 exception applies by its own criterion to the identical householder-and-robbers image. Also **changed** '[he] may' (ⲛ̣ⲁ extant). | `logion-103-householder-domain-and-robbers` (**inferred**); `mntero-the-kingdom` (extended) |
| 30 | 104 | ⲛⲩⲙⲫⲱⲛ vs 75's ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ | 'the bridal chamber' for both; the loan/native pair is recorded in the apparatus, as for ⲧⲟⲡⲟⲥ/ⲙⲁ and ⲁⲝⲓⲟⲥ/ⲙ̄ⲡϣⲁ. Valentinian rite disclaimed, as at 75. | `nymphios-nymphon-bridegroom-bridal-chamber` (direct); `ma-nsheleet-bridal-chamber` (extended) |
| 31 | 105 | Capitals; whore/harlot | 'the father and the mother' lower case (referent unresolved); 'the son of a whore'. | `logion-105-father-mother-son-of-a-whore` (direct) |
| 32 | 106 | 'sons of man' | Lower case, plural, not the central title; link to 86 in commentary. | `logion-106-sons-of-man-plural` (direct); `shere-son-child` (extended) |
| 33 | 107 | a man, a shepherd; toiled; love | As drafted. | `logion-107-shepherd-and-largest-sheep` (direct) |
| 34 | 108 | 'become he'; 'appear to' | As drafted. | `logion-108-drink-from-my-mouth` (direct) |
| 35 | 109 | Eight restorations | Kept, with **two brackets narrowed** ('the one [who]', 'to [those whom]'); moneylender ending kept against 95. | `logion-109-hidden-treasure-parable` (direct); `homt-…` |
| 36 | 111 | 'the living one' twice | 'the one who lives from the living one' (first verbal, second substantive). 'will not see death' (corrected at sign-off). | `logion-111-the-living-one-and-gloss` (**inferred**); `etonh-…`, `jitpe-…` (extended) |
| 37 | 111 | ⲟⲩⲭ ϩⲟⲧⲓ gloss | Rhetorical question 'Does not Jesus say …?' with single quotes; **no gloss marking in the line**; the gloss reading and the 'not that …' parse are in commentary. | same (**inferred**) |
| 38 | 113 | No formula; 'watching out for it' | No formula (as 43); 'by watching out for it' (as 21/51). | `logion-113-kingdom-spread-out-upon-the-earth` (direct); `goosht-…` (extended) |
| 39 | 114 | 'make her male' | Manuscript reading kept: not softened or glossed in the line. 'lead her'; 'a living spirit'; 'the kingdom of the heavens' (central). | `logion-114-make-her-male-manuscript-reading` (direct) |
| 40 | 114 | Subscript title | Chapter-level field `translation.subscriptTitle`, explained in the 114 commentary; not a unit and not appended to 114. | `subscript-title-gospel-according-to-thomas` (direct) |
| 41 | — | Central extensions | See CENTRAL below. **Correction:** the Translator's iēsous list ('80-92') included THOM-91, whose `text` has no ⲓ︤ⲥ︥; 91 is not added. | CENTRAL |

---

## Specific rulings requested

### Logion 85 — past-conditional 'taste death'

ⲛⲉⲩⲁⲝⲓⲟⲥ ⲅⲁⲣ ⲡⲉ is an unreal condition, and the apodosis is the preterite future ⲛⲉϥⲛⲁϫⲓϯⲡⲉ ⲁⲛ ⲙ̄ⲡⲙⲟⲩ.
The formula's lexeme is kept ('taste death') and the tense is rendered faithfully: 'For had he been worthy, [he would] not [have tasted] death.'
A literal application of the entry's 'will not taste death' would mistranslate the tense.
The ratified `jitpe-mpmou-taste-death-thomas-woh` is extended by scope note only; its wohChoice is unchanged.

### Logion 86 — 'the Son of Man'

`son-of-man-bar-enash-dan-7-13-mt-cross-corpus` exists in central v2.75.0 (verified; wohChoice 'the Son of Man', debate not pre-resolved; appliesTo currently MAT-WOH only).
It is applied at THOM-86, and the appliesTo extension is proposed below.
The Daniel entry `son-of-man-bar-enash-dan-7-13-14-cross-corpus` governs the indefinite Aramaic and is not applied.
The commentary states that the capital follows the convention and that in this saying the phrase is often read as a self-reference or as 'a human being'.
The plural at 106 is not under the central entry.

### Restored letters with no English word (79, 86, 96, 97, 102, 109, 110)

**Ruled once, at morph level** (`restored-morph-without-english-word-convention-thomas-woh`).
Block A ('[then you will] see', 37) and Block B ('within [you]', 70) already bracket the English word that renders a restored morph, and Block B 50 brackets the verb when a restored adverb belongs to a compound verb.
Under the same rule, a restored morph that no English word renders produces no bracket:

- linking or attributive ⲛ̄ (79 [ⲛ̄]ⲑϩⲏ, 96 [ⲛ]ⲛⲟⲉⲓⲕ)
- reflexive and object markers (86 ⲙ̄[ⲙⲟ]ϥ, 110 [ⲙ̄]ⲡⲕⲟⲥⲙⲟⲥ)
- a preposition and an indefinite plural article (102)
- the existential ⲙ̄ⲙⲁⲩ and the causative ⲧⲣⲉ- (109)
- a converter with its resumptive pronoun (97 ⲉⲥ-)

Each such restoration is named in the unit's commentary.
Bound-group bracketing ('[the womb]', '[the world]') was rejected because it would make legible nouns look restored, the ground on which Block A rejected bracketing scribal slips.
The same rule moved extant underdotted letters out of brackets at 97, 103 and 109.

### Logion 103 — 'domain'

103 is the householder image of 21.
It has the same ⲗⲏⲥⲧⲏⲥ, the same ⲙⲟⲩⲣ … ⲉϫⲛ̄ ϯⲡⲉ 'gird the loins' and the same synoptic background (Lk 12:39 / Mt 24:43).
The mntero exception therefore applies by its own criterion: 'gather his [domain]'.
This widens a ratified exception, so it is recorded in a new `inferred` entry plus a scope note on `mntero-the-kingdom-thomas-woh`, and it is escalated (review 2).

### Logion 104 — ⲛⲩⲙⲫⲱⲛ vs 75's native phrase

Both are 'the bridal chamber'.
The two words mean the same thing.
The loanword convention records such pairs in the apparatus rather than splitting them in the English (as with 'place' and 'worthy'), and 'the wedding hall' for one of them would invent a difference.
The ma-nsheleet entry had anticipated recording the pair at 104; it is cited there by scope note.

### Logion 111 — the ⲟⲩⲭ ϩⲟⲧⲓ clause

The English prints 'Does not Jesus say, 'Whoever finds himself, the world is not worthy of him'?'.
The clause is not marked as a gloss in the line, because that would be a claim about the text's history.
The commentary gives the gloss reading and the 'not that …' parse of οὐχ ὅτι.
The entry is `inferred`.

### Logion 114 — 'make her male'

The manuscript reading is kept; nothing is softened or glossed in the line.
The interpretations (logion 22; ancient 'becoming male' language; the question whether 114 is a late addition) and the Peter–Mary parallels (Gospel of Mary, Pistis Sophia) are in commentary.

### Subscript title

The subscript ⲡⲉⲩⲁⲅⲅⲉⲗⲓⲟⲛ ⲡⲕⲁⲧⲁ ⲑⲱⲙⲁⲥ is carried in the new chapter-level field `translation.subscriptTitle` (`cop`, `en` 'The Gospel according to Thomas', `placement`, `glossaryRefs`).
It is explained in the 114 commentary.
It is not a numbered unit, because the source keeps its verse list at 0-114 with the title in `source.subscriptTitle`.
It is not appended to 114's English, because it is not part of the saying.
The lemma aid's appending of the title to 114's NORM is a feature of the aid, recorded in commentary.
**Orchestrator:** when merging into `chapter-1.json`, carry `translation.subscriptTitle` into that file's `translation` object.
If the site renderer should display it, a template change is needed (not in this pass).

---

## Greek vs Coptic (Block C)

| Logion | Greek witness | Material divergence | Treatment |
|---|---|---|---|
| 77 | P.Oxy. 1 verso ll. 27-30 (77b only, attached to 30) | No 77a. Order reversed (stone, then wood). 'the wood' (definite); ἔγειρον 'raise'; 'and I am there' (κἀγώ). The ⲡⲱϩ catchword is Coptic-only. | Coptic; commentary |
| 78-114 | none | — | Coptic |

---

## Source findings (source-cop-1.json stays immutable)

Recorded in the commentary of the affected units.
None changes the English beyond following the corpus normalisation.

| refId | Finding | Effect on English |
|---|---|---|
| THOM-78 | Lemma aid counts 6 supplied spans; `text` has 7 bracket groups | None |
| THOM-79 | Stray colon ⲁ:ⲡⲗⲟⲅⲟⲥ (normalised layer repeats it as ⲉ:ⲡⲗⲟⲅⲟⲥ). Scribal erasure ⲉⲛⲧⲁϩⲥⲁ[[ϩ]]ⲛⲟⲩϣⲕ: the corpus notes a rasura, but the source file's `siglaNote` does not document [[ ]] (also at 63, 107). | None |
| THOM-80 | Lemma-aid normalisation ⲡⲉⲛⲧⲁϩⲙϩⲉ contains a stray ⲙ (aid typo) | None |
| THOM-84 | Lycopolitan ⲁⲛⲉⲧⲛ̄ϩⲓⲕⲱⲛ (ⲁ- for ⲉ-); ⲙⲁⲩ- normalised to ⲙⲉⲩ- | Normalised reading followed |
| THOM-85 | `text` duplicates the partly restored word (ϯ̣ⲡ̣[ⲉ ϯ̣ⲡ̣[ⲉ), with 4 opening and 2 closing brackets. The normalised layer also duplicates it (ⲛⲉϥⲛⲁϫⲓϯⲡⲉ ϯⲡⲉ); the token layer has it once. | Read once |
| THOM-86 | Three combining dots below (U+0323) sit on a space or a bracket, not a letter (before ⲛ̣ⲟ̣ⲩ̣, before ⲁ̣ⲩ̣ⲱ̣, in ⲙ̄ⲡ̣[̣ⲉ]) | None |
| THOM-90 | Metathesis corrected with { } and ⟨ ⟩ (ⲁⲛⲁ{ⲩ}ⲡⲁ⟨ⲩ⟩ⲥⲓⲥ); normalised ⲉⲟⲩⲁⲛⲁⲡⲁⲩⲥⲓⲥ supplies preposition and article unmarked | Silent |
| THOM-91 | Diplomatic ϣⲓⲛⲁ / ⲉⲛⲁⲣ̄- / ⲡⲓⲣⲁⲍⲉ, normalised ϩⲓⲛⲁ / ⲉⲛⲛⲁⲣ- / ⲡⲉⲓⲣⲁⲍⲉ | None |
| THOM-93 | Lemma aid counts 0 supplied spans; `text` has 2 bracket groups | None |
| THOM-94 | Nomen sacrum written ⲓⲥ without overline | Expanded silently |
| THOM-97 | Lemma aid counts 4 spans; `text` has 5 bracket groups | None |
| THOM-98 | ϩⲱⲧⲃ written ϩⲱⲧⲙ̄ (both layers); no ϫⲉ after ⲡⲉϫⲉⲓ︤ⲥ︥ | None |
| THOM-100 | Diplomatic ⲁⲩⲛⲟⲩⲃ, normalised ⲉⲩⲛⲟⲩⲃ | None |
| THOM-101 | Combining dot below on a space before ⲛ̣ⲁ̣ⲉⲓ; lemma aid 6 spans vs 7 bracket groups; ⲡⲉⲧⲁ- / ⲡⲉⲧⲛⲁ- | None |
| THOM-102 | Diplomatic ⲡⲟⲩⲟⲛⲉϥ, normalised and lemmatised ⲡⲟⲩⲟⲙϥ 'manger' | Normalised reading (`inferred`) |
| THOM-103 | Stray '/' after ⲧⲱⲟⲩⲛ in all layers, including the lemma (probably a lost half of the \b…/ superscript notation; cf. 76). Rasura in ⲥⲱϩⲟⲩϩ noted by the corpus but not marked in `text` (normalised ⲥⲱⲟⲩϩ). Lemma aid 7 spans vs 5 bracket groups + 1 ( ). | None |
| THOM-107 | [[ⲩ]] scribal erasure; diplomatic ⲉⲡⲛⲟϭ, normalised ⲉⲣⲉⲡⲛⲟϭ | None |
| THOM-109 | Two combining dots below on spaces (before ⲁ̣ⲩ̣ⲱ̣ and before ⲡ̣[ⲉⲛ]) | None |
| THOM-111 | Diplomatic ⲡⲉⲧⲁϩⲉ, normalised ⲡⲉⲧⲛⲁϩⲉ; diplomatic ⲉ ⲓ︤ⲥ︥, tokenised as focalising ⲉⲣⲉ | None |
| THOM-113 | Normalised layer keeps a supralinear stroke in its second ⲉⲥⲛ̄ⲛⲏⲩ only | None |
| THOM-114 | The lemma aid appends the subscript title to logion 114's NORM; the source file keeps it in `source.subscriptTitle` | Title carried in `translation.subscriptTitle` |

Recommendation for the data maintainers (not this pass): re-fetch rather than hand-edit.
Check the following:

- the exporter's handling of combining marks attached to whitespace or brackets (86, 101, 109)
- the superscript notation (103; cf. 76)
- whether the overline at 94 is lost in export
- the duplicated restoration at 85
- documenting [[ ]] in `siglaNote`
- the supplied-span counts (78, 93, 97, 101, 103), as already recommended for Blocks A and B

---

## Speculative entries requiring sign-off

### `woh-reading-logion-88-angels-and-prophets-thomas-woh` (overlay)

**Source:** Thomas 88, ⲛ̄ⲁⲅⲅⲉⲗⲟⲥ ⲛⲏⲩ ϣⲁⲣⲱⲧⲛ̄ ⲙⲛ̄ⲛ̄ⲡⲣⲟⲫⲏⲧⲏⲥ … ⲁϣ ⲛ̄ϩⲟⲟⲩ ⲡⲉⲧⲟⲩⲛ̄ⲛⲏⲩ ⲛ̄ⲥⲉϫⲓⲡⲉⲧⲉⲡⲱⲟⲩ
**WoH choice:** No effect on any English line ('angels' stays).
One labelled paragraph, the last in the THOM-88 notes ('Wheel of Heaven reading (interpretive; not part of the translation)'), records one resonance.
Thomas pairs ⲁⲅⲅⲉⲗⲟⲥ with prophets as visitors who come, give, and will come again to take what is theirs, which can be read alongside the canon's account of messengers sent by the Elohim and of the prophets they instructed.
**Why speculative:** The saying does not say who sends the angels and prophets, where they come from, or what 'what is yours' and 'what is theirs' are, and the canon does not cite it.
Reading the visitors as envoys of the Elohim is a synthesis beyond any single source.
The commentary states the mainstream readings first (eschatological messengers; itinerant envoys received by the community), and the 'messenger' sense of ἄγγελος is reported lexically, without the lens.
**Recommendation:** ship as `speculative`, apparatus only.
If declined, delete the last paragraph of the THOM-88 notes and drop the id from THOM-88's glossaryRefs. Nothing else depends on it.

This is the only point at which the lens touches Block C.
Logion 77 ('I am the light that is above them all') was considered and deliberately left without a lens paragraph, to keep the use sparing.

---

## Unresolved editorial questions / decisions for review

None of the 41 questions is left open.
The following are judgement calls the reviewer should confirm.

### 1. `THOM-77`, `THOM-85` — clefts for focalising second perfects (English changed)

**Issue:** The draft used fronting; the program used clefts at 12 and 62.
**Options considered:** (A) cleft (adopted; new convention entry, which also records why 82 and the purpose-clause second futures at 91, 98 and 114 are not clefted); (B) fronting, as drafted.
**Why escalating:** It changes two lines and writes down as a convention a practice that was previously ruled case by case.

### 2. `THOM-103` — 'gather his [domain]' (English changed; `inferred`)

**Issue:** The draft applied the base 'kingdom'.
**Options considered:** (A) 'domain' (adopted; same image as 21, standard English translation); (B) 'kingdom' (entry base, as drafted).
**Why escalating:** It widens a ratified Block A exception from one logion to two.

### 3. `THOM-111` — rhetorical-question parse; no gloss marking (`inferred`)

**Options considered:** 'Does not Jesus say …?' (adopted); 'Not that Jesus says …'; marking the clause as a gloss in the line (rejected: a text-historical claim).
**Why escalating:** The parse of οὐχ ὅτι plus a focalising present is uncertain.

### 4. `THOM-102` — 'manger' from the normalised layer (`inferred`)

**Issue:** The diplomatic ⲡⲟⲩⲟⲛⲉϥ has no meaning known to the Editor, and the English depends on the normalisation ⲡⲟⲩⲟⲙϥ.
**Why escalating:** A Coptic specialist should confirm whether ⲡⲟⲩⲟⲛⲉϥ is a recognised variant spelling (then `direct`) or a corruption.

### 5. Morph-level bracket convention and five bracket corrections (78, 93, 97, 103, 109)

**Why escalating:** It is a new convention entry refining ratified rule 1, though it codifies what Blocks A and B did.

### 6. `THOM-86` — capital 'the Son of Man'

**Why escalating:** The capital follows the central convention, but in this saying the self-reference / 'human being' reading is strong and some translations use lower case.
The central entry is direct and explicitly does not pre-resolve the debate.
An overlay override would need a human decision.

### 7. `THOM-104` — one English term for ⲛⲩⲙⲫⲱⲛ and ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ

**Options considered:** (A) 'the bridal chamber' for both (adopted); (B) 'the wedding hall' for one of them.

### 8. `THOM-105` — 'whore'; lower-case 'father' and 'mother'

**Options considered:** 'whore' (adopted), 'harlot', 'prostitute'; lower case (adopted) vs 'the Father and the Mother'.

### 9. Hard sayings kept in the manuscript reading

93, 98, 101, 105, 109 (moneylender ending against 95), 111 and 114.
Readers who know popular translations will notice the unsmoothed pronouns at 93 and 95, the '…' gaps at 93 and 101, and 'make her male'.

### 10. Citations to verify against the printed sources

The Editor did not consult the printed volumes in this pass.
The following are cited from memory, with the same caution as Block B's review 7:

- Lambdin's wording quoted in commentary: 84 'will have to bear', 97 'accident', 98 'carry through', 103 'domain', 105 'harlot', 107 'I care for you', 111 'Does not Jesus say'
- Origen, Homilies on Jeremiah 20.3 (82)
- Lucian, Timon 14 (102)
- the P.Oxy. 1 Greek of 77b

If any of these fails a check, the fix is to drop the attribution, not to change a line.

### 11. Coordination with the Block B review (read, not acted on)

The Block B reviewer's package (`chapter-1-signoff-package-block-b.md`, written during this pass) asks for overlay revises:

- topos-ma: remove THOM-66
- restored-text scopeNote (d): rewording
- `logion-74-…`: 'sickness(?)'
- the 61 'there' and 59 notes in the Block B chapter

Overlay v1.2.0 is built on v1.1.0 and **does not include these revises**.
They touch different fields or entries from the v1.2.0 additions: the Block C text is appended after the v1.1.0 scopeNotes, and appliesTo entries are only added.
They can be applied on top without conflict, and the Block C glossaryRefs do not depend on them.

The reviewer also recommends '⟨Salome said:⟩' at 61 as a narrow exception for 'speaker identity carried by Coptic grammar alone'.
If the human adopts it, no Block C unit meets that criterion: 93 and 101 have no change of speaker.
At 113 the change of speaker after the disciples' question is marked by sense, not by grammar, and it currently runs on as at 43.
The human may wish to rule on 113 explicitly at the same time.

---

## Glossary changes for review

### Central glossary

None written. All proposals are in the CENTRAL section below.

### Per-translation overlay (v1.1.0 → **v1.2.0**, released 2026-11-01; semver-minor: additions and scope extensions only)

`gospel-of-thomas-woh/_translation-glossary.json`: 70 → **105 entries** (92 direct, 10 inferred, 3 speculative).
Ratified Block A and Block B entries were verified programmatically to be changed only in `appliesTo` (additions) and `scopeNote` (appended text); wohChoice, rationale and claim_type are unchanged.

**Added (35):** 31 `direct`, 3 `inferred`, 1 `speculative`.

- **Conventions (3, direct):** `focalising-conversion-cleft-convention`, `restored-morph-without-english-word-convention`, `subscript-title-gospel-according-to-thomas`
- **Lexical, direct (28):**
  - logia 77-89: `logion-77-light-above-all-and-poh-reach-split`, `logion-78-countryside-shaken-reed-and-megistanos-great-men`, `naiat-native-beatitude-blessed`, `logos-word-of-the-father`, `arna-renounce-dynamis-power`, `ouonh-ebol-bolp-ebol-manifest-revealed-appear`, `logion-84-likeness-images-and-bearing`, `axios-mpsha-worthy`, `ashe-depend-talaiporos-wretched-ouoei-woe`, `angelos-angels-and-prophets-logion-88`, `tamio-made-logion-89`
  - logia 90-101: `logion-90-chrestos-easy-yoke-and-lordship`, `logion-91-test-the-face-of-the-sky-and-kairos`, `logion-93-holy-to-dogs-pronouns-and-gap`, `homt-money-mese-interest`, `logion-96-leaven-parable-vocabulary`, `logion-97-jar-of-meal-vocabulary`, `logion-98-assassin-parable-vocabulary`, `noute-god-and-logion-100-caesar-vocabulary`, `logion-101-hate-love-and-true-mother-gap`
  - logia 104-114: `nymphios-nymphon-bridegroom-bridal-chamber`, `logion-105-father-mother-son-of-a-whore`, `logion-106-sons-of-man-plural`, `logion-107-shepherd-and-largest-sheep`, `logion-108-drink-from-my-mouth`, `logion-109-hidden-treasure-parable`, `logion-113-kingdom-spread-out-upon-the-earth`, `logion-114-make-her-male-manuscript-reading`
- **Inferred (3):** `logion-102-dog-in-the-manger-normalised-reading`, `logion-103-householder-domain-and-robbers`, `logion-111-the-living-one-and-gloss`
- **Speculative (1):** `woh-reading-logion-88-angels-and-prophets`

**Extended (30 existing entries; appliesTo additions + scopeNote text only):**

- Conventions: `register-sayings-format-and-proper-names-convention`, `restored-text-bracket-and-sigla-convention`, `nomina-sacra-and-abbreviation-expansion-convention`, `greek-loanword-rendering-convention`, `coptic-base-text-and-oxyrhynchus-greek-witnesses-convention`
- Ratified Block A lexical entries: `shaje-ethep-hidden-sayings`, `etonh-the-living-lowercase`, `jitpe-mpmou-taste-death` (85 tense; 111 contrast), `ptirf-the-all-reign-over-the-all`, `mntero-the-kingdom` (103 'domain'), `tpe-sky-heaven-context-rule`, `shere-son-child`, `eiot-father-capitalisation`, `oua-ouot-a-single-one`, `topos-ma-place`, `rome-man-human-person`, `makarios-blessed-singular-formula`, `sower-parable-coptic-form-and-eisheete-behold` ('Behold' only), `kosmos-world-kah-earth`, `ouoein-light-man-of-light`, `pneuma-sarx-soma-spirit-flesh-body`, `eikon-image`, `psyche-soul`, `mariham-name`
- Block B entries: `kim-anapausis-mton-movement-repose-rest` (90 'repose', 86 'rest', 78 'shaken'), `hise-suffer-toil`, `goosht-look-watch`, `ptoma-corpse` (cited at 80 for the contrast), `ma-nsheleet-bridal-chamber` (cited at 104 for the pair), `hmhal-slave-joeis-master-lord` (90 'lordship')

All ids end in `-thomas-woh`.
glossaryRefs on every Block C unit are generated from the overlay `appliesTo` arrays plus the four central ids below, so the two cannot drift.
Every id resolves in overlay v1.2.0 or central v2.75.0 (checked by script), as does every entry id cited in the commentary.

---

## CENTRAL — apply by orchestrator

Central v2.75.0 is not modified by this pass (read and grepped only).
The proposals add **no new entries** and extend `appliesTo` on **four** existing entries (semver-minor).
If Block B's 2.76.0 is applied first, this is **2.77.0**; otherwise both can be folded into one 2.76.0 bump.
The Block C glossaryRefs already cite all four ids.

### 1. EXTEND `appliesTo`

| Existing central id | Add to `appliesTo` | Reason |
|---|---|---|
| `iēsous-yehoshua-yhwh-saves-folk-etymology-cross-corpus` (direct) | `THOM-77`, `THOM-78`, `THOM-80`, `THOM-81`, `THOM-82`, `THOM-83`, `THOM-84`, `THOM-85`, `THOM-86`, `THOM-87`, `THOM-88`, `THOM-89`, `THOM-90`, `THOM-92`, `THOM-94`, `THOM-95`, `THOM-96`, `THOM-97`, `THOM-98`, `THOM-100`, `THOM-102`, `THOM-103`, `THOM-104`, `THOM-105`, `THOM-106`, `THOM-107`, `THOM-108`, `THOM-109`, `THOM-110`, `THOM-111`, `THOM-112`, `THOM-114` (32 units) | Every Block C unit whose `text` has the name: ⲓ︤ⲥ︥, ⲓⲏ︤ⲥ︥ (90), ⲓⲥ without overline (94), the wholly restored [ⲡⲉϫⲉⲓ︤ⲥ︥ ϫⲉ] (95), and the name inside the third-person clause (111). **Not** added: 79, 91, 93, 99, 101, 113 (no ⲓ︤ⲥ︥; the Translator's list wrongly included 91). |
| `lacuna-bracket-convention-sumerian-mesopotamian-project-standard` (direct) | `THOM-78`, `THOM-79`, `THOM-85`, `THOM-86`, `THOM-93`, `THOM-94`, `THOM-95`, `THOM-96`, `THOM-97`, `THOM-101`, `THOM-102`, `THOM-103`, `THOM-104`, `THOM-109`, `THOM-110` (15 units) | Units with real [ ] restorations or unrestored [ ] gaps (93, 101), including those where the restoration has no English word (110). **Not** THOM-107, whose only [[ ]] is a scribal erasure. |
| `son-of-man-bar-enash-dan-7-13-mt-cross-corpus` (direct) | `THOM-86` | First Coptic application: ⲡϣⲏⲣⲉ ⲙ̄ⲡⲣⲱⲙⲉ, 'the Son of Man' per the entry's capitalisation convention, debate not pre-resolved (Mt 8:20 / Lk 9:58 parallel). **Not** THOM-106 (plural, anarthrous ϣⲏⲣⲉ: 'sons of man', overlay). Not the Daniel entry. Suggested source-field addition (optional): "Coptic ⲡϣⲏⲣⲉ ⲙ̄ⲡⲣⲱⲙⲉ (Thomas 86)". |
| `kingdom-of-heaven-basileia-tōn-ouranōn-mt-distinctive-cross-corpus-hebrew-malkhut-shamayim` (direct) | `THOM-114` | ⲧⲙⲛ̄ⲧⲉⲣⲟ ⲛⲙ̄ⲡⲏⲩⲉ 'the kingdom of the heavens', as anticipated in Blocks A and B (completes 20, 54, 114). |

### 2. scopeNote line (suggested)

"v2.77.0 (or with 2.76.0): Gospel of Thomas Block C (logia 77-114): iēsous extended to 32 further THOM units; lacuna-bracket to 15; son-of-man (Mt convention) to THOM-86, its first Coptic occurrence; kingdom-of-the-heavens to THOM-114. Thomas-specific decisions live in the gospel-of-thomas-woh overlay v1.2.0."

### 3. NOT extended, deliberately

- `beatitudes-mt-5-3-12-makarios-formula-ethical-teaching-cross-corpus`: not extended. THOM-79 parallels Lk 11:27-28 / 23:29, not the Sermon beatitudes, and uses native ⲛⲁⲓⲁⲧ=. THOM-103's beatitude has no beatitude in its synoptic parallel (Lk 12:39 / Mt 24:43). Both are covered in the overlay.
- `son-of-man-bar-enash-dan-7-13-14-cross-corpus` (Daniel, indefinite): not applied.
- No central entry governs Coptic ⲛⲟⲩⲧⲉ; 'God' at 100 is decided in the overlay, consistent with matthew-woh's θεός.

### 4. Candidates for later promotion (no action now)

- `nymphios-nymphon-bridegroom-bridal-chamber-thomas-woh` together with `ma-nsheleet-bridal-chamber-thomas-woh`: νυμφών / νυμφίος recur in Mt 9:15 and Mk 2:19-20. Promote if those chapters are translated.
- `focalising-conversion-cleft-convention-thomas-woh` and `restored-morph-without-english-word-convention-thomas-woh`: promote when a second Coptic text enters the program.

---

## Lens-routing summary

- **No English line carries the lens.** No line uses 'Elohim', 'creators', 'messengers', 'planet' or similar.
  - 77 keeps 'the light' and 'the All'.
  - 88 keeps 'angels'.
  - 89 has 'made', not 'created'.
  - 100 has 'God', not 'Elohim'.
  - 91 has 'the sky' for a weather image, under the existing context rule.
- **WoH reading.** It appears once (88), as one labelled paragraph pointing to a single speculative overlay entry, placed after the mainstream reading.
- **Mainstream framing.** Debated items are stated without adjudication:
  - the Son-of-Man debate (86)
  - the referents of 'the father and the mother' (105)
  - the gloss at 111
  - the 'becoming male' interpretations and the late-addition question (114)
  - the Valentinian 'bridal chamber' (104)

## Escalation list (for human sign-off)

1. **SPECULATIVE:** `woh-reading-logion-88-angels-and-prophets-thomas-woh`. Sign off by name, or delete the labelled last paragraph of the THOM-88 notes and drop the id from THOM-88's glossaryRefs.
2. **Review:** 103 'gather his [domain]' (English changed; `inferred`; widens the ratified logion-21 exception).
3. **Review:** 111 rhetorical-question parse and no gloss marking (`inferred`).
4. **Review:** 102 'manger' from the normalised layer (`inferred`; Coptic specialist to confirm ⲡⲟⲩⲟⲛⲉϥ).
5. **Review:** clefts at 77 and 85 (English changed; new convention entry).
6. **Review:** morph-level bracket convention (new entry) and the five bracket corrections at 78, 93, 97, 103, 109.
7. **Review:** 86 capital 'the Son of Man' under the central convention.
8. **Review:** 104 'the bridal chamber' for both ⲛⲩⲙⲫⲱⲛ and 75's ⲡⲙⲁ ⲛ̄ϣⲉⲗⲉⲉⲧ.
9. **Review:** 105 'whore' and lower-case 'father' / 'mother'.
10. **Review:** 90 'repose' (applies the Block B rule; deliberate difference from 'rest' in Mt 11:28-29).
11. **Review:** subscript title in `translation.subscriptTitle` (not a unit). The orchestrator carries it into `chapter-1.json` at the merge.
12. **Review:** hard sayings kept in the manuscript reading (93, 98, 101, 105, 109, 111, 114).
13. **Verify:** the citations listed under review 10, before publication.
14. **Coordination:** the Block B reviewer's overlay revises are not in v1.2.0 and should be applied on top (no conflict). If '⟨Salome said:⟩' is adopted at 61, consider 113 explicitly.
15. **Orchestrator:** apply the CENTRAL section (four appliesTo extensions; 2.77.0 or folded into 2.76.0) and merge Block C into `chapter-1.json` at sign-off.
16. **Data maintainers:** the source findings at 78, 79, 80, 84, 85, 86, 90, 91, 93, 94, 97, 98, 100, 101, 102, 103, 107, 109, 111, 113 and 114 (source not edited).
