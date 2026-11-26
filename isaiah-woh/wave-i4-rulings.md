# Isaiah wave I-4 (chapters 16–23) — orchestrator rulings for Translators and Editors

The founder signed off waves I-1 (1–5) and I-3 (7–12) on 2026-11-26. Their rulings are now merged into the glossaries: the Isaiah overlay is at **2.0.0** and the central glossary at **3.0.0**. The rulings below are in force. If a ruling seems indefensible at a particular verse, keep it in the line and escalate the problem.

1. **Merged house rules.** The glossary entries carry these:
   - `ha-adon-articular-title-isaiah`: hā-ʾāḏôn → "the Sovereign" (19:4).
   - `adam-humankind-ish-man-isaiah`: ʾāḏām and ʾîš pairs → "humankind … everyone". Generic human nouns take gender-neutral English ("people").
   - `hoy-woe-isaiah`: hôy → "Woe" (17:12; 18:1).
   - `nes-signal-isaiah`: nēs → "signal" (18:3).
   - `massa-oracle-superscription-isaiah`: maśśāʾ → "The oracle concerning …", as at 13:1 and 15:1.
   - `aram-names-isaiah`: "Aram" and "Damascus" (17:1–3).
   - `sharaq-whistle-isaiah`.
   - `cherem-devote-to-destruction-cross-corpus`, central.
   - `el-gibbor-mighty-god-isaiah`.
   - `tzalmavet-deep-darkness-isaiah`.
2. **Concordance.**
   - "glory" for kāḇôḏ is strict.
   - "splendor" for hāḏār, "honor" for tip̄ʾereṯ and "majesty" for gāʾôn / gēʾûṯ are the defaults. Where the idiom forbids one, the departure is allowed if it is recorded.
3. **Consistency with the stable neighbours.** Chapters 13, 14, 15 and 24 are stable. Chapter 16 continues the Moab oracle of chapter 15: keep its place names, its "Moab" constructions and its lament vocabulary (wailing, baldness; the Arnon fords appear at 16:2, not in ch. 15). 16:6–12 runs parallel to Jer 48:29–38; flag the parallel in commentary.
4. **Names.** English forms for Egypt, Assyria, Babylon, Ethiopia/Cush and Tyre/Sidon. The Translator flags Cush against Ethiopia, and the chapter 18 and 20 Editors keep it consistent. Other names take the ASV spelling unless a glossary entry fixes another form.
5. **Chapter 19.**
   - 19:18 ʿîr haheres "City of Destruction" (MT) against ʿîr haḥeres "City of the Sun" (1QIsaᵃ and some manuscripts): MT in the line; the variant goes in commentary.
   - 19:19–25 (the altar in Egypt; "Egypt my people, Assyria the work of my hands") is lens-salient. Any reception reading belongs in labelled commentary only.
6. **Chapter 21.**
   - 21:1 midbar-yām "the wilderness of the sea".
   - 21:11–12 Dumah, "Watchman, what of the night?".
   - Keep the watchman and lookout vocabulary consistent within the chapter.
7. **Chapter 22.**
   - 22:1 gêʾ ḥizzāyôn "the valley of vision".
   - 22:15–25 Shebna and Eliakim; the key of the house of David (22:22, quoted in Rev 3:7). The Revelation parallel goes in commentary.
8. **Chapter 23.** Tyre's seventy years (23:15–18); Tarshish ships as at 2:16 ("ships of Tarshish").
9. **Lens.** Lens-neutral English in every line. Any Wheel of Heaven reading appears only in a final commentary paragraph labelled speculative. That paragraph quotes the canon only after checking the data-library text, and says plainly whether the canon cites the verse. The founder ruled to keep such notes, as at 4:5, 7:14, 9:5 and 11:12.
10. **Citations.**
    - NJPS means "Tanakh: The Holy Scriptures, published by JPS" (1985) on Sefaria, not the Gender-Sensitive Edition. Fetch with `/api/v3/texts/Isaiah.N?version=english|all`. Sefaria's JPS English editions use Hebrew versification.
    - Cite NRSV, LXX, 1QIsaᵃ or a lexicon only when confident. Otherwise write "not verified".
11. **Files.**
    - Translators write `chapter-N.json`, copying the shape of `chapter-12.json` exactly: status "draft", version "0.1.0", glossaryVersion "3.0.0", overlayGlossaryVersion "2.0.0".
    - Editors write `wave-i4-ch<N>-overlay-diff.json` and `wave-i4-ch<N>-central-diff.json` as a list of ops (version / add / modify with appliesToAdded, optional changes, optional rationaleAppend). Proposed versions: overlay 2.1.0, central 3.1.0.
    - Never edit a shared glossary. Never touch `wave-i1-*`, `wave-i2-*` or `wave-i3-*` files, or any other chapter.
12. **Cush** (ruled during drafting): כּוּשׁ → "Cush" (as 11:11; 43:3; 45:14), not ASV "Ethiopia"; ASV / NJPS "Nubia" go in commentary.
13. **Scope of the gender-neutral rule** (ruled during drafting): it governs GENERIC human nouns (ʾāḏām, ʾîš/ʾănāšîm meaning "people", "anyone"). Nouns for specific male groups — warriors, riders, "mighty men" (gibbôrîm, as stable 13:3 "my mighty men") — keep "men".
14. **kišnê śāḵîr** (16:14; 21:16), ruled during drafting: "as the years of a hireling" at both sites. Chapter 16 Editor adds the overlay entry `shnei-sakhir-years-of-hireling-isaiah`; chapter 21 Editor extends it.
15. **yᵉʾôr** (ruled during editing): singular yᵉʾôr → "the Nile" in Isaiah (ASV prints "the Nile" at 19:7–8; 23:3, 10); plural yᵉʾōrîm "rivers/streams"; nāhār "the River" = Euphrates. The chapter 23 Editor owns the context clause on central `yeor-nile-egyptian-loanword`; other Editors emit appliesTo only.
