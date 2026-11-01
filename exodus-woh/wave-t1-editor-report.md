# Torah wave T1 Editor Report — Exodus 24, 25, 33; Numbers 18, 21, 33; Deuteronomy 4

Editor pass, 2026-11-01 (claude-opus-5-5 acting as woh-editor). Founder-commissioned canon-cited program: every biblical chapter cited in Raël's first three books, whole chapters.

## Summary

- 7 chapters, 253 verses, advanced from `draft` 0.1.0 to `editor-review` `1.0.0-rc1`; `claude-opus-5-5 (editor)` added to modelDrafts; glossaryVersion `2.84.0` (pending this wave's central diff); overlayGlossaryVersion exodus-woh `1.2.0`, numbers-woh `1.0.0`, deuteronomy-woh `1.0.0`.
- 99 editorial questions resolved (table below); none left unresolved. Ten points are flagged for the founder (F1-F10), none of which blocks the Reviewer.
- 38 English-line changes, each tied to a glossary entry and explained in the verse commentary. Commentary on all 253 verses except Ex 25:24, 26 (identical to the ASV, nothing to note).
- Reception notes (labelled '**Wheel of Heaven reading (reception note, not a translation claim).**') at every canon-cited verse: Ex 24:2, 10, 17; 25:2 (for vv 2-7), 9, 22; 33:9, 11, 20; Num 18:13; 21:8, 9; 33:52, 53; Deut 4:37. The Translator's reception remarks were moved out of the question text into these notes. No English line encodes a canon reading.
- Overlays: exodus-woh 1.1.0 -> 1.2.0 (9 entries added, 1 rationale appended); numbers-woh 1.0.0 created (11 entries); deuteronomy-woh 1.0.0 created (10 entries). The four shared Torah conventions are identical in all three overlays; the pairwise-shared ones are identical in the two overlays that carry them.
- Central diff `wave-t1-central-diff.json` (base 2.83.0 -> recommended 2.84.0): 3 new entries, 40 modifications (8 with text, 32 appliesTo-only). No central file was edited.
- Speculative entries: none.

## Speculative entries requiring sign-off

None. All 3 new central entries and all 21 new overlay entries are `claim_type: direct`: each records either the ASV rendering, the rendering of the major current versions (NRSV, NJPS), or a presentation convention, with the alternatives in the rationale. The canon's readings (craft, pedestal, provisions for the creators, serum injections, atmosphere, the destruction of idols on the creators' advice) appear only in the labelled reception notes and are not asserted by any entry.

---

## Founder decisions

### F1. Proper names: two corpus practices

The Torah volumes now share exodus-woh's practice: transliterated names with the grandfathered English 'Moses' and 'Pharaoh'; 'Mitsrayim' (ts, central `mitsrayim`) for the country but 'the Egyptians' for the population (exodus-woh 3:9 and Ex 14 passim, applied at Num 33:3-4); tz elsewhere (Baal-Tzefon, Etzyon-Gever, Tzin); 'Baal-' without apostrophe (exodus-woh 14:2, 9; Deut 4:3, 46). The Kings volumes (ratified 2026-11-01) print 'Moshe', 'Par'oh', 'Mitzrayim', 'Ba'al'. The central `mitsrayim` entry also specifies the gentilic 'Mitsri', which neither exodus-woh nor numbers-woh uses. Signed-off chapters were not retro-edited. Options: (a) keep the split, with a corpus normalization pass later (recommended for this wave); (b) move the Torah volumes to 'Moshe'/'Mitzrayim' (would require re-editing signed-off exodus-woh); (c) move Kings to 'Moses'. A corpus note recording the split is appended to central `mitsrayim`; the full spelling list and ASV equivalence table are in `hebrew-proper-name-transliteration-convention-torah`.

### F2. tôrâ: 'law' vs exodus-woh 'torah'

New central `torah-law-instruction-rendering-cross-corpus` rules by sense: 'law' where tôrâ is a written body of law (Ex 24:12; Deut 4:8, 44; the Kings sites). exodus-woh 13:9 'the torah of YHWH' and 16:4 'my torah' (signed off) are left standing as the 'instruction' sense. Decide at the next Exodus pass: keep 'torah', change to 'law', or change to 'instruction'. The Kings overlay entry `torah-law-deuteronomistic-kings` is subsumed and can be retired or kept as a pointer at merge.

### F3. bārāʾ outside Genesis 1

Deut 4:32 echoes Gen 1:27. genesis-woh renders bārāʾ 'shape' under central `bara` (inferred, scoped to Gen 1). The line keeps 'created' (and adopts genesis-woh's 'humankind' for ʾāḏām); extending 'shape' to other books would carry an inferred lens rendering into Deuteronomy and, by implication, into Isa 40-48, which the parallel Isaiah wave is editing now. Recommend one corpus ruling taken with the Isaiah pass. Recorded in deuteronomy-woh `bara-elohim-adam-deuteronomy-4-32`.

### F4. tərûmâ 'oblation' corpus-wide (central qorbanot)

The deferred Torah clause of central `qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus` is resolved: tərûmâ 'oblation' in the Torah as in Ezekiel, with the verb hērîm 'set apart' (replacing ASV 'offering' at Ex 25:2-3 and 'heave-offering' / 'heave' / 'offer' in Num 18); tənûp̄â keeps 'wave-offering'. 14 lines change. Please ratify. Semver: the diff recommends 2.84.0 by the additive-clause precedent of the Kings and Ezekiel diffs; a strict reading of 'modifications are major' would give 3.0.0.

### F5. The cosmic merism

Deut 4:26 'the heavens and the earth' follows exodus-woh 20:11; Gen 1:1 has 'the skies and the land'. The `shamayim` and `eretz` notes in the diff record that the merism outside Gen 1 takes the Ex 20:11 form. Confirm, or rule a single form.

### F6. śārāp̄ and the Isaiah wave

Num 21:6, 8 keep the ASV 'fiery serpent(s)' (numbers-woh `saraf-fiery-serpent-numbers-21`). Isa 14:29 ('flying śārāp̄') is in the parallel Isaiah wave and Isa 6 will follow; one rendering should govern. The entry stays in the overlay until that decision.

### F7. ḥērem and the Former Prophets wave

numbers-woh `cherem-devoted-thing-utterly-destroy-numbers` keeps the ASV split ('devoted thing' / 'utterly destroy'). Josh 6-7 and 1 Sam 15 are in the parallel Former Prophets wave; promote to central once their decision is known.

### F8. Deuteronomy's discourse convention

Deut 4:1-40 is printed without outer quotation marks because Moses' discourse opens at 1:6; embedded speech takes double marks; the narrator resumes at 4:41 (`direct-speech-quotation-marks-convention-torah`). Confirm before Deut 1-3 and 5 are translated.

### F9. kappōreṯ

'mercy-seat' (ASV, NRSV) kept; NJPS 'cover' and 'place of atonement' recorded in `tabernacle-furnishings-vocabulary-exodus-25`. A founder preference for 'cover' would change Ex 25:17-22 (6 lines) mechanically.

### F10. Items for the next Exodus pass (no change made now)

exodus-woh 16:16 'according to the number of your souls' (nep̄āšôṯ) predates the nefesh rule now shared by Kings, Ezekiel and the Torah overlays; exodus-woh 'heavens' at 16:4; 17:14; 20:4, 11, 19 still await the `shamayim` register check; exodus-woh 13:9, 16:4 'torah' (F2).

---

## Decisions the Reviewer should check closely

- Deut 4:34 'has any elohim ventured' (generic class, lower case) against the ASV's YHWH referent, while 4:33 keeps 'the voice of the Elohim'. Basis: the comparison 'as all that YHWH your Elohim did for you' (NRSV, NJPS 'any god'); `elohim-referent-and-article-conventions-torah` clause 4.
- Ex 24:10 omission of the ASV's supplied 'stone'.
- Deut 4:16-18 'pattern' for taḇnîṯ (five occurrences), chosen to keep the Ezek 8:10 allusion and the one-word-one-lexeme rule.
- Num 18 'oblation' / 'set apart' throughout (12 lines).
- Num 33:3 'all the Egyptians' (no plural agreement in the Hebrew; population sense).

---

## Unresolved editorial questions

None. All 99 Translator questions are resolved as follows.

| refId | Question | Ruling |
|---|---|---|
| EXO-WOH-24:1 | Proper names not yet fixed for exodus-woh | Nadav, Avihu kept; 'Moses' kept as the grandfathered exodus-woh form, extended to numbers-woh and deuteronomy-woh (`hebrew-proper-name-transliteration-convention-torah`). Corpus split with Kings 'Moshe' -> founder point F1. |
| EXO-WOH-24:1 | וְהִשְׁתַּחֲוִיתֶם 'and you shall bow down / worship' (also Ex 33 | 'bow down' (line changed 24:1; also 33:10, Deut 4:19) under a Torah clause added to central `hishtachavah-bow-down-obeisance-worship`. |
| EXO-WOH-24:6 | זָרַק 'dash' is applied from the central qorbanot cluster (vv 6, 8), r | 'dash' kept at vv 6 and 8: same verb, same basins, one rite (central qorbanot appliesTo extended). |
| EXO-WOH-24:7 | נַעֲשֶׂה וְנִשְׁמָע | 'we will do, and we will obey' kept (sense); literal 'hear' and b. Shabbat 88a in commentary. |
| EXO-WOH-24:10 | כְּמַעֲשֵׂה לִבְנַת הַסַּפִּיר | 'stone' dropped: 'a paved work of sapphire' (line changed); new overlay `livnat-hassappir-pavement-of-sapphire-exodus-24-10`; correction appended to central `eben-sapir-kisse`; canon reading in reception note. |
| EXO-WOH-24:10 | וּכְעֶצֶם הַשָּׁמַיִם לָטֹהַר | 'the very skies' kept under the `shamayim` register rule (physical sky). |
| EXO-WOH-24:11 | וַיֶּחֱזוּ אֶת־הָאֱלֹהִים | 'beheld' kept (ḥāzâ vs rāʾâ contrast); LXX paraphrase recorded (`mt-baseline-...-torah`). |
| EXO-WOH-24:12 | וְהַתּוֹרָה וְהַמִּצְוָה | 'the law and the commandment' kept; new central `torah-law-instruction-rendering-cross-corpus` (sense rule: 'law' for a written body of law). exodus-woh 13:9, 16:4 'torah' -> founder point F2. |
| EXO-WOH-24:16 | וַיִּשְׁכֹּן כְּבוֹד־יְהוָה | 'dwelt' kept; central `shakhan` and `sinai-theophany-...` appliesTo extended to vv 15-18. |
| EXO-WOH-24:17 | כְּאֵשׁ אֹכֶלֶת 'like a devouring fire' (ASV 'like devouring fire'; NJ | 'like a devouring fire' kept; Deut 4:24 linked in commentary; canon reading in reception note. |
| EXO-WOH-25:2 | תְּרוּמָה (vv 2, 3; also Num 18 passim). The central qorbanot cluster  | tərûmâ 'oblation' (lines 25:2-3 changed; Num 18 likewise); central qorbanot Torah clause resolved (with hērîm 'set apart'). |
| EXO-WOH-25:3 | נְחֹשֶׁת | 'bronze' (line changed; also Num 21:9); new central `nechoshet-bronze-copper-alloy-cross-corpus`. |
| EXO-WOH-25:4 | The dye and textile terms תְּכֵלֶת / אַרְגָּמָן / תּוֹלַעַת שָׁנִי and | ASV dye terms kept; 'goats' hair' without brackets; recorded in `tabernacle-furnishings-vocabulary-exodus-25`. |
| EXO-WOH-25:5 | עֹרֹת תְּחָשִׁים | 'sealskins' kept (unidentified; candidates in commentary and overlay entry). |
| EXO-WOH-25:7 | אַבְנֵי־שֹׁהַם 'onyx stones' (ASV; identification uncertain | 'onyx stones ... breastplate' kept (overlay cluster entry). |
| EXO-WOH-25:9 | תַּבְנִית (vv 9 twice, 40) and מִשְׁכָּן. tabnît is 'pattern, model, p | 'pattern' kept and fixed corpus-wide by new central `tabnit-pattern-model-cross-corpus` (also Deut 4:16-18, changed there); 'tabernacle' kept for miškān (overlay cluster; dwelling-link in commentary). |
| EXO-WOH-25:13 | בַּדִּים | 'poles' kept (1-kings-woh 8:7-8). |
| EXO-WOH-25:16 | הָעֵדֻת (vv 16, 21, 22 'the ark of the Testimony'; also Num 18 | 'the Testimony' kept; `edut-the-testimony-capitalisation-torah` (exodus + numbers overlays). |
| EXO-WOH-25:17 | כַּפֹּרֶת (vv 17-22, seven times). ASV 'mercy-seat' (Tyndale, after Lu | 'mercy-seat' kept (ASV, NRSV); 'cover' / 'place of atonement' in commentary. Founder may prefer 'cover' (F9). |
| EXO-WOH-25:18 | כְּרֻבִים rendered 'cherubim' under the central `cherubim-ezek` entry  | 'cherubim ... hammered work' kept; central `cherubim-ezek` extended. |
| EXO-WOH-25:22 | וְנוֹעַדְתִּי לְךָ שָׁם 'and I will meet with you there' (the verb of  | 'meet ... speak' kept; reception note added. |
| EXO-WOH-25:30 | לֶחֶם פָּנִים לְפָנַי | 'the bread of the presence' (line changed; NRSV) via overlay cluster + `panim-presence-face-convention-torah`. |
| EXO-WOH-25:31 | מְנֹרָה (vv 31-35) | 'lampstand' (lines 25:31-35 changed; title updated). |
| EXO-WOH-25:37 | וְהֶעֱלָה אֶת־נֵרֹתֶיהָ וְהֵאִיר עַל־עֵבֶר פָּנֶיהָ | Draft kept ('set up its lamps ... its front'). |
| EXO-WOH-25:40 | אֲשֶׁר־אַתָּה מָרְאֶה בָּהָר | 'which you are being shown' kept (Hophal participle). |
| EXO-WOH-33:1 | נִשְׁבַּעְתִּי לְאַבְרָהָם לְיִצְחָק וּלְיַעֲקֹב | 'swore' kept; central oath-triple wohChoice gains a modern-register note. |
| EXO-WOH-33:2 | מַלְאָךְ 'a messenger' (ASV 'an angel') under the central `malakh-yhwh | 'a messenger' kept (central `malakh-yhwh-messenger` extended); English gentilics kept. |
| EXO-WOH-33:7 | וּמֹשֶׁה יִקַּח ... וְנָטָה־לוֹ | lô left unexpressed (ASV); 'for himself' / 'for it' in commentary. |
| EXO-WOH-33:9 | וְדִבֶּר עִם־מֹשֶׁה has no expressed subject | Subject left unexpressed ('he'); ambiguity and canon's 'He' in reception note. |
| EXO-WOH-33:10 | וְהִשְׁתַּחֲווּ 'and worship / bow down' (as Ex 24 | 'bow down' (line changed), as 24:1. |
| EXO-WOH-33:11 | פָּנִים אֶל־פָּנִים 'face to face' under the central Peni'el entry (ca | 'face to face ... his attendant' kept; central `peniel-...` extended; tension with v 20 in commentary. |
| EXO-WOH-33:14 | פָּנַי יֵלֵכוּ (v 14) / פָּנֶיךָ הֹלְכִים (v 15) and בְּפָנָיו at Deut | 'My presence shall go' kept without supplement; `panim-presence-face-convention-torah` (exodus + deuteronomy). |
| EXO-WOH-33:16 | וְנִפְלֵינוּ 'and we are distinguished / set apart' (ASV 'separated'); | 'set apart ... face of the earth' kept; `adamah-earth-land-ground-scope-torah`. |
| EXO-WOH-33:18 | כְּבֹדֶךָ / כְּבֹדִי (vv 18, 22) rendered 'your glory / my glory' with | 'your glory / my glory' kept; central `kavod-yhwh` extended. |
| EXO-WOH-33:19 | עַל־פָּנֶיךָ 'before you' (ASV; literally 'before your face') and וְקָ | ASV kept; qara-b-shem-yhwh not applied (YHWH is subject). |
| EXO-WOH-33:20 | כִּי לֹא־יִרְאַנִי הָאָדָם וָחָי | 'man shall not see me and live' kept (generic ASV; ha-adam is Gen 2-scoped); canon readings (TBWTT, LWTE) in reception note. |
| EXO-WOH-33:22 | כַּפִּי (vv 22, 23) 'my palm / hand' (ASV 'hand'); נִקְרַת הַצּוּר 'a  | 'my hand' kept. |
| EXO-WOH-33:23 | אֲחֹרָי 'my back' (ASV; literally 'my hinder parts / what is behind me | 'my back' kept; later interpretive readings in commentary only. |
| NUM-WOH-18:1 | New book | Torah house style adopted for the new book (overlay v1.0.0 created). |
| NUM-WOH-18:2 | אֹהֶל הָעֵדֻת 'the tent of the Testimony' (ASV lower-case 'testimony') | 'the tent of the Testimony' kept; Levi pun in commentary. |
| NUM-WOH-18:4 | זָר (vv 4, 7) | 'an outsider' (lines 18:4, 18:7 changed); new overlay `zar-outsider-cultic-numbers-18`. |
| NUM-WOH-18:7 | עֲבֹדַת מַתָּנָה אֶתֵּן אֶת־כְּהֻנַּתְכֶם 'I give your priesthood as a | ASV kept ('a service of gift', 'the veil'); `priestly-dues-vocabulary-numbers-18`. |
| NUM-WOH-18:8 | תְּרוּמָה (vv 8, 11, 19, 24, 26-29) and the verb הֵרִים (vv 19, 24, 26 | 'oblation' / 'set apart' (lines 18:8, 11, 19, 24, 26-30, 32 changed); central qorbanot ruling. |
| NUM-WOH-18:8 | לְמָשְׁחָה | 'by reason of the anointing' kept; 'as a portion' recorded. |
| NUM-WOH-18:9 | קָרְבָּן 'offering' (central qorbanot; ASV 'oblation'), מִנְחָה 'meal- | ASV sense kept, no supplement; locative reading recorded. |
| NUM-WOH-18:12 | חֵלֶב (vv 12, 29, 30, 32) literally 'fat', figuratively 'the best' (AS | Kept; rēʾšîṯ / bikkûrîm distinction recorded; canon reading at v 13 in reception note. |
| NUM-WOH-18:14 | כָּל־חֵרֶם 'every devoted thing' (ASV 'everything devoted') | 'Every devoted thing' kept; new overlay `cherem-devoted-thing-utterly-destroy-numbers` (promotion candidate, F7). |
| NUM-WOH-18:15 | פֶּטֶר רֶחֶם / בְּכוֹר | 'bring near' kept; central pesach-pidyon extended. |
| NUM-WOH-18:17 | אִשֶּׁה 'an offering made by fire' (ASV; the etymology from אֵשׁ 'fire | 'an offering made by fire' kept; 'food-gift' recorded; reach-hannichoach and qorbanot extended. |
| NUM-WOH-18:19 | בְּרִית מֶלַח עוֹלָם 'a covenant of salt forever' (ASV) | Kept ('covenant of salt forever ... a portion forever'). |
| NUM-WOH-18:31 | שָׂכָר 'wage' (ASV 'reward'); the sense is payment for service. | 'your reward' kept; 'wage' in commentary. |
| NUM-WOH-21:1 | Toponyms and personal names (vv 1, 3, 10-20, 23-33) are transliterated | Draft spellings adopted as the Torah spelling list (in `hebrew-proper-name-transliteration-convention-torah`, with ASV equivalence table). |
| NUM-WOH-21:1 | דֶּרֶךְ הָאֲתָרִים | 'Atarim' kept (MT); 'the spies' recorded. |
| NUM-WOH-21:2 | וְהַחֲרַמְתִּי / וַיַּחֲרֵם (vv 2-3) | 'utterly destroy ... Chormah' kept, unglossed (no causal clause); wordplay in commentary. |
| NUM-WOH-21:4 | נֶפֶשׁ (vv 4, 5) | nep̄eš idioms rendered by sense (lines 21:4, 21:5 changed); `nefesh-scope-torah` (numbers + deuteronomy; same rule as Kings and Ezekiel). |
| NUM-WOH-21:4 | יַם־סוּף rendered 'the Sea of Reeds' under the central `yam-suf-...` e | 'Sea of Reeds ... Mount Hor' kept; central yam-suf extended. |
| NUM-WOH-21:5 | וַיְדַבֵּר הָעָם בֵּאלֹהִים וּבְמֹשֶׁה | Kept ('against the Elohim ... worthless bread'); `elohim-referent-and-article-conventions-torah`. |
| NUM-WOH-21:6 | הַנְּחָשִׁים הַשְּׂרָפִים (v 6) and שָׂרָף alone (v 8) | 'fiery serpents ... a fiery serpent' kept; new overlay `saraf-fiery-serpent-numbers-21`; Isaiah harmonization flagged (F6). |
| NUM-WOH-21:8 | עַל־נֵס 'upon a standard / pole' (ASV 'standard'; NJPS 'standard', NRS | 'standard' kept. |
| NUM-WOH-21:9 | נְחַשׁ נְחֹשֶׁת 'a serpent of brass' (ASV; NRSV/NJPS 'a serpent of bro | 'a serpent of bronze' (line changed); central nechoshet; canon 'brass' in reception note. |
| NUM-WOH-21:14 | סֵפֶר מִלְחֲמֹת יְהוָה 'the Book of the Wars of YHWH' (a lost source); | Kept as unfinished fragment. |
| NUM-WOH-21:16 | בְּאֵרָה ... הִוא הַבְּאֵר | Kept, no supplement, unglossed. |
| NUM-WOH-21:18 | בִּמְחֹקֵק בְּמִשְׁעֲנֹתָם | Kept; LXX 'from the well' recorded. |
| NUM-WOH-21:20 | הַיְשִׁימֹן | 'the desert ... the field of Moab' kept. |
| NUM-WOH-21:27 | הַמֹּשְׁלִים 'those who speak in proverbs / the bards' (ASV); the Hesh | Kept. |
| NUM-WOH-21:28 | בַּעֲלֵי בָּמוֹת אַרְנֹן 'the lords of the high places of the Arnon' ( | MT kept; LXX recorded. |
| NUM-WOH-21:30 | Textual crux, and a Masoretic extraordinary point | MT kept; extraordinary point and Sam/LXX 'fire' recorded in commentary and `mt-baseline-...-torah`. |
| NUM-WOH-21:32 | Ketiv/Qere | Qere 'drove out' kept, plural subject; Ketiv recorded. |
| NUM-WOH-21:34 | אַל־תִּירָא אֹתוֹ 'Do not fear him' | Kept; central al-tira extended (war-oracle motive clause noted). |
| NUM-WOH-33:1 | The itinerary names (vv 3-49) are transliterated on the exodus-woh pat | Exodus-woh transliteration, unglossed; ASV forms in the equivalence table and at first occurrence in commentary; 'Qadesh' by the qof rule. |
| NUM-WOH-33:2 | וַיִּכְתֹּב מֹשֶׁה אֶת־מוֹצָאֵיהֶם לְמַסְעֵיהֶם | ASV wording kept (chiasm). |
| NUM-WOH-33:4 | וּבֵאלֹהֵיהֶם עָשָׂה יְהוָה שְׁפָטִים | 'the Egyptians' where miṣrayim is the population (lines 33:3, 33:4 changed), following exodus-woh 3:9 / Ex 14; 'Mitsrayim' for the country; corpus note appended to central `mitsrayim` (F1). |
| NUM-WOH-33:8 | מִפְּנֵי הַחִירֹת 'from before haChirot' | MT 'haChirot' kept. |
| NUM-WOH-33:9 | שִׁבְעִים תְּמָרִים 'seventy palm-trees' (ASV 'threescore and ten'). T | 'seventy' kept. |
| NUM-WOH-33:40 | This verse repeats Num 21 | 'the Negev' kept. |
| NUM-WOH-33:52 | Canon-cited (TBWTT ch. 3 quotes vv 52-53 as the destruction of the pri | ASV kept; new overlay `maskit-masekhah-bamah-cult-objects-numbers-33-52`; reception note. |
| NUM-WOH-33:53 | וְהוֹרַשְׁתֶּם אֶת־הָאָרֶץ | 'take possession of the land' kept; alternative recorded; reception note. |
| NUM-WOH-33:55 | לְשִׂכִּים בְּעֵינֵיכֶם וְלִצְנִינִם בְּצִדֵּיכֶם 'as pricks in your e | Kept. |
| DEU-WOH-4:1 | New book | Torah house style; quotation convention for the Mosaic discourse recorded (`direct-speech-quotation-marks-convention-torah`, F8). |
| DEU-WOH-4:1 | חֻקִּים וּמִשְׁפָּטִים 'statutes and ordinances' (ASV; vv 1, 5, 8, 14, | 'statutes and ordinances' kept; central mishmeret entry extended. |
| DEU-WOH-4:7 | אֱלֹהִים קְרֹבִים אֵלָיו | Lower-case 'elohim' kept (clause 4 of `elohim-referent-and-article-conventions-torah`). |
| DEU-WOH-4:8 | הַתּוֹרָה הַזֹּאת (vv 8, 44) | 'this law' kept (central torah entry). |
| DEU-WOH-4:9 | וּשְׁמֹר נַפְשְׁךָ מְאֹד (v 9), וְנִשְׁמַרְתֶּם מְאֹד לְנַפְשֹׁתֵיכֶם  | 'guard yourself' / 'with all your being' (lines 4:9, 4:29 changed); 'yourselves' at 4:15 kept. |
| DEU-WOH-4:10 | עַל־הָאֲדָמָה (vv 10, 40) 'upon the earth / ground' and the cosmic use | Kept as drafted ('earth' cosmic, 'land' territory); 4:40 'ground' -> 'land' (line changed) under `adamah-earth-land-ground-scope-torah`; cosmic clause added to central `eretz`. |
| DEU-WOH-4:11 | šāmayim register (central `shamayim`, ratified 2026-11-01 | Register split kept; central shamayim note records the Deut 4 application. |
| DEU-WOH-4:11 | חֹשֶׁךְ עָנָן וַעֲרָפֶל 'darkness, cloud, and thick darkness' (ASV); ע | Kept; central arafel extended. |
| DEU-WOH-4:12 | תְּמוּנָה (vv 12, 15, 16, 23, 25) rendered 'likeness' under the centra | təmûnâ 'likeness', pesel 'carved image', semel 'figure' kept; taḇnîṯ 'form' -> 'pattern' (lines 4:16-18 changed) under central `tabnit-pattern-model-cross-corpus`. |
| DEU-WOH-4:13 | עֲשֶׂרֶת הַדְּבָרִים | 'the ten words' (line changed); central aseret entry extended. |
| DEU-WOH-4:19 | וְנִדַּחְתָּ וְהִשְׁתַּחֲוִיתָ לָהֶם וַעֲבַדְתָּם 'and be drawn away a | 'bow down to them and serve them' (line changed), matching Ex 20:5. |
| DEU-WOH-4:24 | אֵשׁ אֹכְלָה הוּא אֵל קַנָּא 'a devouring fire, a jealous El' (ASV 'a  | 'a devouring fire, a jealous El' kept; new overlay `el-qanna-el-rachum-bare-el-predicate-deuteronomy`. |
| DEU-WOH-4:26 | הַעִידֹתִי בָכֶם הַיּוֹם אֶת־הַשָּׁמַיִם וְאֶת־הָאָרֶץ | 'the heavens and the earth' kept (Ex 20:11 form); recorded in central shamayim note (F5). |
| DEU-WOH-4:30 | בַּצַּר לְךָ 'when you are in distress' (central `tzarah-...` 'distres | MT accent division kept. |
| DEU-WOH-4:32 | לְמִן־הַיּוֹם אֲשֶׁר בָּרָא אֱלֹהִים אָדָם עַל־הָאָרֶץ | 'humankind' (line changed; genesis-woh 1:26-27); 'created' kept, bārāʾ scope escalated (F3); new overlay `bara-elohim-adam-deuteronomy-4-32`. |
| DEU-WOH-4:33 | קוֹל אֱלֹהִים מְדַבֵּר (v 33) and הֲנִסָּה אֱלֹהִים (v 34) | v 33 YHWH referent kept; v 34 'any elohim' (line changed; NRSV, NJPS). |
| DEU-WOH-4:36 | לְיַסְּרֶךָּ 'that he might instruct you' (ASV) — יסר is 'discipline,  | 'instruct' kept; 'discipline' in commentary. |
| DEU-WOH-4:37 | Textual variant (canon-cited | MT 'his seed after him' kept; versions and canon plural in reception note. |
| DEU-WOH-4:42 | רוֹצֵחַ אֲשֶׁר יִרְצַח אֶת־רֵעֵהוּ בִּבְלִי־דַעַת | 'manslayer ... kills' kept; new overlay `rotseach-manslayer-unintentional-killing-deuteronomy-4-42`; scope sentence appended to the exodus-woh ratsach entry. |
| DEU-WOH-4:43 | בְּאֶרֶץ הַמִּישֹׁר 'in the plain country' (ASV; 'the tableland', the  | Kept. |
| DEU-WOH-4:48 | הַר שִׂיאֹן הוּא חֶרְמוֹן 'Mount Si'on — that is Chermon' (ASV 'mount  | MT 'Si'on' kept; Peshitta 'Sirion' recorded. |

---

## English-line changes (38)

- **EXO-WOH-24:1** — And to Moses he said, "Come up to YHWH, you and Aharon, Nadav and Avihu, and seventy of the elders of Yisra'el, and bow down from afar.
- **EXO-WOH-24:10** — And they saw the Elohim of Yisra'el; and under his feet there was as it were a paved work of sapphire, and as it were the very skies for clearness.
- **EXO-WOH-25:2** — "Speak to the children of Yisra'el, that they take for me an oblation; from every man whose heart makes him willing you shall take my oblation.
- **EXO-WOH-25:3** — And this is the oblation which you shall take from them: gold, and silver, and bronze;
- **EXO-WOH-25:30** — And you shall set upon the table the bread of the presence before me continually.
- **EXO-WOH-25:31** — And you shall make a lampstand of pure gold; of hammered work shall the lampstand be made, its base and its shaft; its cups, its knobs, and its flowers shall be of one piece with it.
- **EXO-WOH-25:32** — And six branches shall go out from its sides: three branches of the lampstand out of its one side, and three branches of the lampstand out of its other side;
- **EXO-WOH-25:33** — three cups made like almond-blossoms on the one branch, a knob and a flower; and three cups made like almond-blossoms on the other branch, a knob and a flower; so for the six branches going out from the lampstand.
- **EXO-WOH-25:34** — And on the lampstand four cups made like almond-blossoms, its knobs and its flowers;
- **EXO-WOH-25:35** — and a knob under two branches of one piece with it, and a knob under two branches of one piece with it, and a knob under two branches of one piece with it, for the six branches going out from the lampstand.
- **EXO-WOH-33:10** — And all the people would see the pillar of cloud standing at the entrance of the tent, and all the people would rise up and bow down, each man at the entrance of his tent.
- **NUM-WOH-18:4** — And they shall be joined to you and keep the charge of the tent of meeting, for all the service of the tent; and an outsider shall not come near to you.
- **NUM-WOH-18:7** — And you and your sons with you shall keep your priesthood for everything of the altar and for what is within the veil, and you shall serve. I give you your priesthood as a service of gift; and the outsider who comes near shall be put to death."
- **NUM-WOH-18:8** — And YHWH spoke to Aharon, "And I, behold, I have given you the charge of my oblations, of all the holy things of the children of Yisra'el; to you I have given them by reason of the anointing, and to your sons, as a portion forever.
- **NUM-WOH-18:11** — And this is yours: the oblation of their gift, all the wave-offerings of the children of Yisra'el; to you I have given them, and to your sons and to your daughters with you, as a portion forever; everyone who is clean in your house shall eat of it.
- **NUM-WOH-18:19** — All the oblations of the holy things which the children of Yisra'el set apart for YHWH I have given to you, and to your sons and to your daughters with you, as a portion forever; it is a covenant of salt forever before YHWH for you and for your seed with you."
- **NUM-WOH-18:24** — For the tithe of the children of Yisra'el, which they set apart for YHWH as an oblation, I have given to the Levites for an inheritance; therefore I have said to them, 'Among the children of Yisra'el they shall have no inheritance.'"
- **NUM-WOH-18:26** — "And to the Levites you shall speak and say to them, 'When you take from the children of Yisra'el the tithe which I have given you from them for your inheritance, then you shall set apart from it an oblation for YHWH, a tithe of the tithe.
- **NUM-WOH-18:27** — And your oblation shall be reckoned to you as though it were the grain of the threshing-floor and as the fullness of the winepress.
- **NUM-WOH-18:28** — Thus you also shall set apart an oblation for YHWH from all your tithes which you receive from the children of Yisra'el; and from it you shall give YHWH's oblation to Aharon the priest.
- **NUM-WOH-18:29** — Out of all your gifts you shall set apart every oblation of YHWH, of all the best of it, the hallowed part of it, out of it.'
- **NUM-WOH-18:30** — And you shall say to them, 'When you have set apart the best of it from it, then it shall be reckoned to the Levites as the produce of the threshing-floor and as the produce of the winepress.
- **NUM-WOH-18:32** — And you shall bear no sin because of it, when you have set apart the best of it from it; and you shall not profane the holy things of the children of Yisra'el, that you not die.'"
- **NUM-WOH-21:4** — And they journeyed from Mount Hor by the way to the Sea of Reeds, to go around the land of Edom; and the people became impatient because of the way.
- **NUM-WOH-21:5** — And the people spoke against the Elohim and against Moses: "Why have you brought us up out of Mitsrayim to die in the wilderness? For there is no bread and there is no water, and we loathe this worthless bread."
- **NUM-WOH-21:9** — And Moses made a serpent of bronze and set it upon the standard; and it came to pass that if a serpent had bitten any man, when he looked to the serpent of bronze, he lived.
- **NUM-WOH-33:3** — And they journeyed from Ra'meses in the first month, on the fifteenth day of the first month; on the morrow of the Passover the children of Yisra'el went out with a high hand before the eyes of all the Egyptians,
- **NUM-WOH-33:4** — while the Egyptians were burying those whom YHWH had struck among them, all the firstborn; and upon their elohim YHWH had executed judgments.
- **DEU-WOH-4:9** — Only take heed to yourself, and guard yourself diligently, lest you forget the things which your eyes have seen, and lest they depart from your heart all the days of your life; but make them known to your children and your children's children —
- **DEU-WOH-4:13** — And he declared to you his covenant, which he commanded you to perform, the ten words; and he wrote them upon two tablets of stone.
- **DEU-WOH-4:16** — lest you act corruptly and make for yourselves a carved image, the likeness of any figure, the pattern of male or female,
- **DEU-WOH-4:17** — the pattern of any beast that is on the earth, the pattern of any winged bird that flies in the skies,
- **DEU-WOH-4:18** — the pattern of anything that creeps on the ground, the pattern of any fish that is in the water beneath the earth;
- **DEU-WOH-4:19** — and lest you lift up your eyes to the skies and see the sun and the moon and the stars, all the host of the heavens, and be drawn away and bow down to them and serve them, which YHWH your Elohim has allotted to all the peoples under the whole of the skies.
- **DEU-WOH-4:29** — But from there you shall seek YHWH your Elohim, and you shall find him, if you search after him with all your heart and with all your being.
- **DEU-WOH-4:32** — For ask now of the days that are past, which were before you, since the day that the Elohim created humankind upon the earth, and from one end of the skies to the other end of the skies, whether there has been anything like this great thing, or whether anything like it has been heard.
- **DEU-WOH-4:34** — Or has any elohim ventured to go and take for himself a nation from the midst of a nation, by trials, by signs, and by wonders, and by war, and by a mighty hand and by an outstretched arm, and by great terrors, according to all that YHWH your Elohim did for you in Mitsrayim before your eyes?
- **DEU-WOH-4:40** — And you shall keep his statutes and his commandments which I command you this day, that it may go well with you and with your children after you, and that you may prolong your days upon the land which YHWH your Elohim gives you, for all time.

Titles updated: Ex 25 ('lampstand', 'oblation'), Num 18 ('oblations'), Num 21 ('serpent of bronze', with ASV names).

---

## Glossary changes for review

### Central glossary (proposals in `exodus-woh/wave-t1-central-diff.json`; not applied)

- Added: `torah-law-instruction-rendering-cross-corpus` (claim_type: `direct`; appliesTo 9)
- Added: `nechoshet-bronze-copper-alloy-cross-corpus` (claim_type: `direct`; appliesTo 3)
- Added: `tabnit-pattern-model-cross-corpus` (claim_type: `direct`; appliesTo 5)
- Modified (text): `aseret-ha-dvarim-decalogue-enumeration-jewish-vs-augustinian-orthodox-cross-corpus` (wohChoice, rationale; appliesTo +1) — Extends the entry to the name of the Decalogue (wohChoice and rationale appended).
- Modified (text): `eben-sapir-kisse` (rationale; appliesTo +0) — Factual correction appended to the rationale; wohChoice and appliesTo unchanged.
- Modified (text): `eretz` (wohChoice, rationale; appliesTo +36) — Adds a cosmic context clause (wohChoice and rationale appended) describing existing exodus-woh and Kings practice; the default 'land' is unchanged.
- Modified (text): `hishtachavah-bow-down-obeisance-worship` (wohChoice, rationale; appliesTo +3) — Adds a Torah clause (wohChoice and rationale appended); the Genesis rendering is unchanged.
- Modified (text): `mitsrayim` (rationale; appliesTo +11) — Corpus note appended to the rationale recording the gentilic and spelling variants; wohChoice unchanged.
- Modified (text): `nishba-la-avraham-le-yitzchaq-u-le-yaaqov-patriarchal-oath-triple-formula-cross-corpus` (wohChoice; appliesTo +1) — Records the modern-register verb form at the Exodus site the rationale already names.
- Modified (text): `qorbanot-sacrificial-offering-vocabulary-cluster-cross-corpus` (wohChoice, rationale; appliesTo +17) — Resolves the deferred clause of the wohChoice ('the Torah's tərûmâ to be reviewed when Leviticus and Numbers are translated') with the Torah ruling and adds the verb rule; the Ezekiel rendering 'oblation' is unchanged, so no shipped line changes.
- Modified (text): `shamayim` (rationale; appliesTo +8) — Records the Torah application of the ratified register rule; wohChoice unchanged.
- appliesTo-only extensions (32): `adam-adamah` (+1), `al-tira-fear-not-divine-encouragement-formula` (+1), `arafel-thick-darkness-divine-presence-cross-corpus` (+1), `be-acharit-ha-yamim-latter-days-temporal-eschatological-horizon-cross-corpus` (+1), `cherubim-ezek` (+4), `elohei-yisrael` (+1), `elohim-aherim-other-gods-monolatry-vs-monotheism-scholarly-dispute-cross-corpus` (+3), `elohim-as-translation` (+27), `goy-gadol-great-nation-promise-formula` (+3), `har-sinai-horev-the-mountain-of-Elohim-divine-mountain-cross-corpus` (+5), `karat-brit-cut-covenant` (+2), `kavod-yhwh` (+4), `maaser-first-pre-sinai` (+4), `malakh-yhwh-messenger` (+1), `matza-chen-be-einei-x-favor-formula` (+4), `matzevah-sacred-pillar-patriarchal-religion` (+1), `mishmeret-mitzvot-chuqim-torot-fourfold-covenant` (+6), `olah-burnt-offering` (+1), `peniel-panim-el-panim-divine-face-encounter` (+2), `pesach-pidyon-firstborn-passover-firstborn-redemption-cross-corpus` (+1), `pesel-utemunah-graven-image-iconographic-prohibition-cross-corpus` (+5), `pillar-of-cloud-and-fire-ammud-ha-anan-ve-esh-divine-presence-marker-cross-corpus` (+2), `raamses-eastern-delta-store-city-toponym` (+2), `reach-hannichoach` (+1), `shakhan-dwell-divine-presence-verb-cross-corpus` (+2), `shesh-fine-linen-egyptian-loanword` (+1), `shivtei-yisrael-shenim-asar-twelve-tribes-institutional-political-formula-cross-corpus` (+1), `sinai-theophany-ex-19-elohim-craft-descent-disavowals-volcanic-hypothesis-cross-corpus` (+4), `sukkot-toponym-and-festival-etymology` (+2), `tzarah-distress-tribulation-vocabulary` (+1), `tzeva-ha-shamayim-host-of-the-heavens-divine-council-cross-corpus` (+1), `yam-suf-sea-of-reeds-vs-red-sea-geographical-textual-cross-corpus` (+3).

### Per-translation overlay: exodus-woh (v1.2.0)

- Modified: `ratsach-murder-vs-kill-decalogue-translation-convention-exodus-overlay` (scope sentence appended: 'murder' limited to the Decalogue; asylum-law rṣḥ is 'manslayer' / 'kill')
- Added: `hebrew-proper-name-transliteration-convention-torah` (claim_type: `direct`; appliesTo 17)
- Added: `direct-speech-quotation-marks-convention-torah` (claim_type: `direct`; appliesTo 1)
- Added: `mt-baseline-ketiv-qere-and-accent-division-torah` (claim_type: `direct`; appliesTo 2)
- Added: `elohim-referent-and-article-conventions-torah` (claim_type: `direct`; appliesTo 3)
- Added: `panim-presence-face-convention-torah` (claim_type: `direct`; appliesTo 5)
- Added: `adamah-earth-land-ground-scope-torah` (claim_type: `direct`; appliesTo 1)
- Added: `edut-the-testimony-capitalisation-torah` (claim_type: `direct`; appliesTo 3)
- Added: `tabernacle-furnishings-vocabulary-exodus-25` (claim_type: `direct`; appliesTo 16)
- Added: `livnat-hassappir-pavement-of-sapphire-exodus-24-10` (claim_type: `direct`; appliesTo 1)

### Per-translation overlay: numbers-woh (v1.0.0)

- Added: `hebrew-proper-name-transliteration-convention-torah` (claim_type: `direct`; appliesTo 92)
- Added: `direct-speech-quotation-marks-convention-torah` (claim_type: `direct`; appliesTo 4)
- Added: `mt-baseline-ketiv-qere-and-accent-division-torah` (claim_type: `direct`; appliesTo 8)
- Added: `elohim-referent-and-article-conventions-torah` (claim_type: `direct`; appliesTo 2)
- Added: `nefesh-scope-torah` (claim_type: `direct`; appliesTo 2)
- Added: `edut-the-testimony-capitalisation-torah` (claim_type: `direct`; appliesTo 1)
- Added: `zar-outsider-cultic-numbers-18` (claim_type: `direct`; appliesTo 2)
- Added: `cherem-devoted-thing-utterly-destroy-numbers` (claim_type: `direct`; appliesTo 3)
- Added: `saraf-fiery-serpent-numbers-21` (claim_type: `direct`; appliesTo 3)
- Added: `priestly-dues-vocabulary-numbers-18` (claim_type: `direct`; appliesTo 9)
- Added: `maskit-masekhah-bamah-cult-objects-numbers-33-52` (claim_type: `direct`; appliesTo 1)

### Per-translation overlay: deuteronomy-woh (v1.0.0)

- Added: `hebrew-proper-name-transliteration-convention-torah` (claim_type: `direct`; appliesTo 16)
- Added: `direct-speech-quotation-marks-convention-torah` (claim_type: `direct`; appliesTo 4)
- Added: `mt-baseline-ketiv-qere-and-accent-division-torah` (claim_type: `direct`; appliesTo 4)
- Added: `elohim-referent-and-article-conventions-torah` (claim_type: `direct`; appliesTo 22)
- Added: `nefesh-scope-torah` (claim_type: `direct`; appliesTo 3)
- Added: `panim-presence-face-convention-torah` (claim_type: `direct`; appliesTo 1)
- Added: `adamah-earth-land-ground-scope-torah` (claim_type: `direct`; appliesTo 3)
- Added: `el-qanna-el-rachum-bare-el-predicate-deuteronomy` (claim_type: `direct`; appliesTo 2)
- Added: `rotseach-manslayer-unintentional-killing-deuteronomy-4-42` (claim_type: `direct`; appliesTo 1)
- Added: `bara-elohim-adam-deuteronomy-4-32` (claim_type: `direct`; appliesTo 1)

---

## Merge and sequencing notes

- Base 2.83.0. The parallel isaiah-woh and Former Prophets (joshua-woh, judges-woh, 1-samuel-woh) diffs also target 2.83.0. Apply in any order and renumber; merge appliesTo of shared entries as a set union using each op's `appliesToAdded`, and apply text appends to the then-current field (details in the diff's version note).
- Lexical overlaps to reconcile with the parallel waves: tôrâ (Isa 42; Josh 1:7-8), nəḥōšeṯ (1 Sam 17:5-6), śārāp̄ (Isa 14:29), ḥērem (Josh 6-7; 1 Sam 15), bārāʾ (Isa 40-45), hištaḥăwâ (1 Sam 1:3, 19, 28), malʾāḵ (Judg 6, 13).
- Overlay merge: the three Torah overlays are complete files and need no diff. When the orchestrator merges the central diff, the Kings overlay entry `torah-law-deuteronomistic-kings` and the tabnîṯ clause of the ezekiel-woh `tabnit-toknit-tekhunah-pattern-plan-arrangement-ezekiel` become pointers to the new central entries; no Kings or Ezekiel file was touched in this wave.
- The central `malakh-yhwh-messenger`, `karat-brit-cut-covenant` and similar entries hold older refIds (EXOD-33:2, EXOD-24:8, DEUT-4:23); the new EXO-WOH- / DEU-WOH- refIds are added beside them, as the Ezekiel diff did for EZK-.

## Files written

- `exodus-woh/chapter-24.json`
- `exodus-woh/chapter-25.json`
- `exodus-woh/chapter-33.json`
- `numbers-woh/chapter-18.json`
- `numbers-woh/chapter-21.json`
- `numbers-woh/chapter-33.json`
- `deuteronomy-woh/chapter-4.json`
- `exodus-woh/_translation-glossary.json`
- `numbers-woh/_translation-glossary.json`
- `deuteronomy-woh/_translation-glossary.json`
- `exodus-woh/wave-t1-central-diff.json`
- `exodus-woh/wave-t1-editor-report.md`
