# Isaiah wave I-3 (chapters 7–12) — orchestrator rulings for the Editors

These rulings span chapters and are fixed so that the six parallel Editors stay consistent. An Editor who finds one indefensible at a particular verse keeps the ruling in the line and escalates the problem in the editor report. Wave I-1's rulings (`wave-i1-signoff-package.md` and the `wave-i1-ch*-diff.json` files) are in force.

1. **Sign-names.**
   - In the English line, Shear-jashub (7:3), Immanuel (7:14; 8:8) and Maher-shalal-hash-baz (8:1, 3) are transliterated names. Their meaning goes in the commentary.
   - At 8:8 the name is a vocative: "O Immanuel".
   - At 8:10 the same two words are a clause: "for God is with us". The commentary links it to 7:14 and 8:8.
   - At 10:21 šᵉʾār yāšûḇ is a clause, "A remnant will return", and the commentary notes the echo of 7:3.
   - One overlay entry, `sign-names-isaiah-7-8`, covers all of these sites. The chapter 7 Editor adds it. The chapter 8 and 10 Editors propose `appliesToAdded` for their sites as a modify op on that id; the orchestrator resolves the order at merge.
2. **ʾēl gibbôr.** "Mighty God" at 9:5 and at 10:21 ("to the Mighty God"). The commentary records the alternatives ("God is a warrior", "mighty hero"). The chapter 9 Editor adds the overlay entry `el-gibbor-mighty-god-isaiah`, and the chapter 10 Editor extends it with a modify op.
3. **Hā-ʿalmâ (7:14).** "the young woman". Commentary covers ʿalmâ against bᵉṯûlâ, the LXX's *parthenos* and the reception in Matthew 1:23. Any Wheel of Heaven reading appears only as a labelled speculative note in commentary, never in the line.
4. **Names.**
   - "Aram" and "the Arameans", not ASV "Syria" or "the Syrians".
   - English forms for Ephraim, Manasseh, Egypt and Assyria.
   - Other place names take the ASV spelling unless a glossary entry fixes another form.
5. **ḥānēp̄.** "godless" at 9:16 and 10:6, matching the stable 32:6 "godlessness".
6. **Concordance.** "glory" for kāḇôḏ is strict. "splendor" for hāḏār, "honor" for tip̄ʾereṯ and "majesty" for gāʾôn are the defaults. Where the idiom forbids one (for example 10:12 tip̄ʾereṯ rûm ʿênāyw), the Editor may depart, provided the departure is recorded in commentary and in the diff.
7. **hā-ʾāḏôn (10:16, 33).** Provisionally "the Sovereign". Carry only `ha-adon-articular-title-isaiah`; the orchestrator merges `ha-adon-definite-title-isaiah` into it.
8. **Tense in the poem of 9:7–20.** The chapter 9 Editor decides. The chapter 10 oracle (10:1–4) is a separate woe-oracle and keeps its own tenses. Only its refrain is fixed.
9. **Citations.** Cite NRSV, NJPS, LXX, 1QIsaᵃ or a lexicon only when confident. Otherwise write "not verified".
10. **Diff files.** `wave-i3-ch<N>-overlay-diff.json` and `wave-i3-ch<N>-central-diff.json` take the list-of-ops format. Base versions: overlay 1.6.1 (to be 1.7.0 after wave I-1; propose 1.8.0) and central 2.93.0 (propose 2.95.0). Never edit a shared glossary, and never touch `wave-i1-*` or `wave-i2-*` files.
