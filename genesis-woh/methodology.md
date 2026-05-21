# Wheel of Heaven Translation — Genesis 1 (Pilot)

**Status:** Draft v1.0.0. Single-session pilot output. Pending human review and decision on whether to commit to Phase 2 (Genesis 1–11).

---

## What this document is

The first output of the [Wheel of Heaven Translation Program](../../../../.claude/plans/strategy-translation-program.md). It contains:

1. The methodology used to produce the translation.
2. The source material and licensing.
3. The translation glossary version pinned to this chapter.
4. **A parallel display of all 31 verses** — Hebrew, ASV (American Standard Version 1901), WoH Translation — with per-verse notes on the choices that diverge from the ASV.

The document is intended to be read end-to-end and then judged on a single question: **does this read better than the ASV under the WoH lens?** If yes, commit to Phase 2. If no, kill the pilot and proceed with the existing PD-hosting model.

---

## Source

| Field | Value |
|---|---|
| Source text | Tanach with Ta'amei Hamikra (Westminster Leningrad Codex with vowel points and cantillation marks) |
| License | Public Domain |
| Origin | http://www.tanach.us/Tanach.xml |
| Accessed via | sefaria.org/api/v3/texts/Genesis.1 on 2026-05-18 |
| Stored at | `data/library/genesis-woh/source-he.json` |

This is the Translation track per the [WoH Translation Program strategy](../../../../.claude/plans/strategy-translation-program.md) — the source is pointed Hebrew, not an existing English translation.

## Glossary

| Field | Value |
|---|---|
| Glossary file | `content/i18n/translation-glossary.json` |
| Version pinned to this chapter | 1.0.0 |
| Term count | 31 entries, covering all lexical decisions made in Genesis 1 |
| Claim-type distribution | 23 `direct` (grammatically explicit) + 8 `inferred` (defensible non-consensus readings) + 0 `speculative` |

The glossary is the actual product of this Program. Every WoH-specific choice in the translation below is recorded as a glossary entry with rationale and `claim_type`. The translation only ever applies what the glossary records.

## Pipeline

This pilot used **Claude Opus 4.7 (1M context)** as the first-pass drafter, with the Hebrew source + the full glossary loaded as input. Human review will revise the draft before promoting to v1.0.0 stable.

Multi-model comparison (Claude + GPT in parallel) is on the Phase 2 menu but was not used here — the goal of the pilot is to test whether the *single-model + glossary* pipeline produces output worth the effort. If yes, multi-model is a quality-multiplier; if no, multi-model can't save it.

---

## How to read the parallel display

For each verse:
- **He** — the pointed Hebrew source verbatim from the Westminster Leningrad text.
- **ASV** — the American Standard Version 1901, the most common PD English translation we already host in the Library.
- **WoH** — the Wheel of Heaven Translation, applying the glossary.
- **Notes** (only where divergent from ASV) — which glossary entries were applied and what the divergence rests on.

Where ASV and WoH agree on a verse, no notes — the choice is uncontested and the WoH translation has no edge over ASV.

Where they diverge, the notes name the glossary entry that drove the choice. Cross-reference into `content/i18n/translation-glossary.json` for the full rationale and `claim_type`.

---

## The parallel display

### Day One (v1–5)

#### v1

**He.** בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃

**ASV.** In the beginning God created the heavens and the earth.

**WoH.** When Elohim began to shape the skies and the land—

**Notes.**
- `bereshit`: the Hebrew is a construct form *without* the definite article (it would be בָּרֵאשִׁית for "in *the* beginning"). The verse is grammatically a temporal clause, not a freestanding declaration; the main clause arrives in v3 ("Elohim said"). The construct/temporal reading is the modern scholarly consensus (NJPS, NRSV, the recent Robert Alter translation) and was the dominant Jewish reading from Rashi onward. The ASV "In the beginning" carries a *creatio-ex-nihilo* doctrinal commitment the Hebrew doesn't grammatically support. The WoH lens benefits from the construct reading: the text describes a project beginning, not the absolute origin of all matter.
- `bara`: "shape", not "create". One of three creation verbs in this chapter (bara, asah, yatsar); flattening them to "create/make" loses a deliberate distinction.
- `elohim-as-translation`: untranslated, plural form preserved.
- `shamayim`: "skies" (grammatically dual in Hebrew), not "heavens".
- `eretz`: "land", not "earth" (which is a 17th-century English meaning of a planet).

#### v2

**He.** וְהָאָ֗רֶץ הָיְתָ֥ה תֹ֙הוּ֙ וָבֹ֔הוּ וְחֹ֖שֶׁךְ עַל־פְּנֵ֣י תְה֑וֹם וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת עַל־פְּנֵ֥י הַמָּֽיִם׃

**ASV.** And the earth was waste and void; and darkness was upon the face of the deep: and the Spirit of God moved upon the face of the waters

**WoH.** —the land being wasteland and emptiness, with darkness over the face of the deep, and the breath of Elohim hovering over the face of the waters—

**Notes.**
- `tohu-vavohu`: "wasteland and emptiness". KJV "without form and void" reads philosophical (Aristotelian matter without form); Hebrew is concrete (cf. Jer 4:23). The alliteration of *tohu/vohu* is preserved by the *wasteland/emptiness* echo.
- `ruach-elohim`: **"breath of Elohim", not "Spirit of God"**. רוּחַ has three lexical fields (breath / wind / spirit) and Hebrew does not disambiguate; ASV's choice imports the Christian Trinitarian "Spirit" onto a verse that does not require it. Combined with the *merachefet* (hovering, bird-like) verb following, the physical reading is the natural one. This is the single most contested choice in this chapter and is the place to test the WoH lens against your own ear.
- `merachefet`: "hovering over", not "moved upon". The Hebrew verb (cf. Deut 32:11, an eagle hovering over its young) is specifically aerial.
- Em-dashes at the start and end signal the temporal-clause structure begun in v1 — the main clause lands in v3.

#### v3

**He.** וַיֹּ֥אמֶר אֱלֹהִ֖ים יְהִ֣י א֑וֹר וַֽיְהִי־אֽוֹר׃

**ASV.** And God said, Let there be light: and there was light.

**WoH.** Elohim said, "Let there be light"; and there was light.

**Notes.**
- This is the main clause of the v1–v3 temporal structure ("When Elohim began to shape … the land being wasteland and emptiness … Elohim said, 'Let there be light' "). The "And" of ASV v3 is dropped — under the construct reading, this is the *first* clause, not a continuation.

#### v4

**He.** וַיַּ֧רְא אֱלֹהִ֛ים אֶת־הָא֖וֹר כִּי־ט֑וֹב וַיַּבְדֵּ֣ל אֱלֹהִ֔ים בֵּ֥ין הָא֖וֹר וּבֵ֥ין הַחֹֽשֶׁךְ׃

**ASV.** And God saw the light, that it was good: and God divided the light from the darkness.

**WoH.** And Elohim saw that the light was good; and Elohim separated between the light and the darkness.

**Notes.** Substantively unchanged from ASV. "Separated between … and between …" preserves the Hebrew doubled *ben … u-ven …* structure (ASV smooths to "divided X from Y").

#### v5

**He.** וַיִּקְרָ֨א אֱלֹהִ֤ים ׀ לָאוֹר֙ י֔וֹם וְלַחֹ֖שֶׁךְ קָ֣רָא לָ֑יְלָה וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם אֶחָֽד׃

**ASV.** And God called the light Day, and the darkness he called Night. And there was evening and there was morning, one day.

**WoH.** And Elohim called the light Day, and the darkness he called Night. And there was evening and there was morning, day one.

**Notes.** "Day one" (cardinal *echad*) rather than "first day" (ordinal *rishon*) — Hebrew uses the cardinal here uniquely, then switches to ordinals (*sheni, shlishi, …*) for days 2–6. The ASV smooths to "one day" / "a second day" which loses the deliberate signaling. NJPS renders "first day" anyway; the WoH choice preserves the Hebrew oddity, which the methodology then surfaces.

---

### Day Two (v6–8)

#### v6

**He.** וַיֹּ֣אמֶר אֱלֹהִ֔ים יְהִ֥י רָקִ֖יעַ בְּת֣וֹךְ הַמָּ֑יִם וִיהִ֣י מַבְדִּ֔יל בֵּ֥ין מַ֖יִם לָמָֽיִם׃

**ASV.** And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.

**WoH.** And Elohim said, "Let there be a dome in the midst of the waters, and let it separate between waters and waters."

**Notes.**
- `raqia`: **"dome", not "firmament"**. The Hebrew is from the verb רקע "to hammer out / beat thin (a metal sheet)". The ANE cosmology is a solid vault hammered out across the sky to hold back the upper waters. ASV's "firmament" (via Vulgate *firmamentum* < LXX στερέωμα) preserves the solid-thing register; modern translations soften to "expanse" (ESV, NIV) which papers over the cosmology. The WoH choice is "dome" — accurate to the Hebrew, honest about the cosmology, and lets the reader make their own peace with the picture.

#### v7

**He.** וַיַּ֣עַשׂ אֱלֹהִים֮ אֶת־הָרָקִיעַ֒ וַיַּבְדֵּ֗ל בֵּ֤ין הַמַּ֙יִם֙ אֲשֶׁר֙ מִתַּ֣חַת לָרָקִ֔יעַ וּבֵ֣ין הַמַּ֔יִם אֲשֶׁ֖ר מֵעַ֣ל לָרָקִ֑יעַ וַֽיְהִי־כֵֽן׃

**ASV.** And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.

**WoH.** And Elohim made the dome, and separated between the waters which were under the dome and the waters which were above the dome. And it was so.

**Notes.** "Made" (asah), not "shaped" (bara). The chapter alternates these verbs deliberately — the dome is *made*, humanity is *shaped*. ASV uses "made" here and "created" for bara elsewhere, so the distinction is preserved in ASV too — but inconsistently across verses. The WoH version applies the rule uniformly via the glossary.

#### v8

**He.** וַיִּקְרָ֧א אֱלֹהִ֛ים לָֽרָקִ֖יעַ שָׁמָ֑יִם וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם שֵׁנִֽי׃

**ASV.** And God called the firmament Heaven. And there was evening and there was morning, a second day.

**WoH.** And Elohim called the dome Skies. And there was evening and there was morning, day two.

**Notes.** *Note the absence of "Elohim saw that it was good" on day 2.* This is a textual feature, not an error — it's been the subject of rabbinic and modern scholarly comment for centuries. The WoH translation preserves the absence without comment in the text; the methodology surfaces it here. The standard explanations: (1) the project of separating the waters is not completed until day 3 when the dry land appears, so the "good" lands then; (2) day 2's work is structural plumbing, not a result. The omission is deliberate and intelligible under the lens.

---

### Day Three (v9–13)

#### v9

**He.** וַיֹּ֣אמֶר אֱלֹהִ֗ים יִקָּו֨וּ הַמַּ֜יִם מִתַּ֤חַת הַשָּׁמַ֙יִם֙ אֶל־מָק֣וֹם אֶחָ֔ד וְתֵרָאֶ֖ה הַיַּבָּשָׁ֑ה וַֽיְהִי־כֵֽן׃

**ASV.** And God said, Let the waters under the heavens be gathered together unto one place, and let the dry land appear: and it was so.

**WoH.** And Elohim said, "Let the waters under the skies be gathered to one place, and let the dry ground appear." And it was so.

#### v10

**He.** וַיִּקְרָ֨א אֱלֹהִ֤ים ׀ לַיַּבָּשָׁה֙ אֶ֔רֶץ וּלְמִקְוֵ֥ה הַמַּ֖יִם קָרָ֣א יַמִּ֑ים וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃

**ASV.** And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.

**WoH.** And Elohim called the dry ground Land, and the gathering of the waters he called Seas. And Elohim saw that it was good.

**Notes.** Capitalized *Land* here is a proper name (Elohim is naming the dry ground), parallel to *Seas*. This is a naming moment, not an ordinary noun usage.

#### v11

**He.** וַיֹּ֣אמֶר אֱלֹהִ֗ים תַּֽדְשֵׁ֤א הָאָ֙רֶץ֙ דֶּ֔שֶׁא עֵ֚שֶׂב מַזְרִ֣יעַ זֶ֔רַע עֵ֣ץ פְּרִ֞י עֹ֤שֶׂה פְּרִי֙ לְמִינ֔וֹ אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ עַל־הָאָ֑רֶץ וַֽיְהִי־כֵֽן׃

**ASV.** And God said, Let the earth put forth grass, herbs yielding seed, and fruit-trees bearing fruit after their kind, wherein is the seed thereof, upon the earth: and it was so.

**WoH.** And Elohim said, "Let the land sprout vegetation: seed-bearing plants, and fruit trees making fruit according to their kind, in which is their seed, upon the land." And it was so.

#### v12

**He.** וַתּוֹצֵ֨א הָאָ֜רֶץ דֶּ֠שֶׁא עֵ֣שֶׂב מַזְרִ֤יעַ זֶ֙רַע֙ לְמִינֵ֔הוּ וְעֵ֧ץ עֹֽשֶׂה־פְּרִ֛י אֲשֶׁ֥ר זַרְעוֹ־ב֖וֹ לְמִינֵ֑הוּ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃

**ASV.** And the earth brought forth grass, herbs yielding seed after their kind, and trees bearing fruit, wherein is the seed thereof, after their kind: and God saw that it was good.

**WoH.** And the land brought forth vegetation: seed-bearing plants according to their kind, and trees making fruit in which is their seed according to their kind. And Elohim saw that it was good.

#### v13

**He.** וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם שְׁלִישִֽׁי׃

**ASV.** And there was evening and there was morning, a third day.

**WoH.** And there was evening and there was morning, day three.

---

### Day Four (v14–19)

#### v14

**He.** וַיֹּ֣אמֶר אֱלֹהִ֗ים יְהִ֤י מְאֹרֹת֙ בִּרְקִ֣יעַ הַשָּׁמַ֔יִם לְהַבְדִּ֕יל בֵּ֥ין הַיּ֖וֹם וּבֵ֣ין הַלָּ֑יְלָה וְהָי֤וּ לְאֹתֹת֙ וּלְמ֣וֹעֲדִ֔ים וּלְיָמִ֖ים וְשָׁנִֽים׃

**ASV.** And God said, Let there be lights in the firmament of heaven to divide the day from the night; and let them be for signs, and for seasons, and for days and years:

**WoH.** And Elohim said, "Let there be luminaries in the dome of the skies to separate between the day and the night; and let them be for signs and for appointed times, and for days and years;

**Notes.**
- `meorot`: "luminaries", not "lights". The Hebrew is a technical word for *light-source objects* (cf. ASV gets this right in some verses, wrong here).
- `moadim`: **"appointed times", not "seasons"**. The Hebrew has a technical calendrical sense — fixed times, festival appointments, predetermined astronomical occasions. ASV "seasons" reads natural-cycles; the Hebrew is structural-calendrical. This is one of the verses where the WoH lens specifically benefits: the luminaries are positioned as functional time-keepers, not as deities.

#### v15

**He.** וְהָי֤וּ לִמְאוֹרֹת֙ בִּרְקִ֣יעַ הַשָּׁמַ֔יִם לְהָאִ֖יר עַל־הָאָ֑רֶץ וַֽיְהִי־כֵֽן׃

**ASV.** and let them be for lights in the firmament of heaven to give light upon the earth: and it was so.

**WoH.** and let them be as luminaries in the dome of the skies, to give light upon the land." And it was so.

#### v16

**He.** וַיַּ֣עַשׂ אֱלֹהִ֔ים אֶת־שְׁנֵ֥י הַמְּאֹרֹ֖ת הַגְּדֹלִ֑ים אֶת־הַמָּא֤וֹר הַגָּדֹל֙ לְמֶמְשֶׁ֣לֶת הַיּ֔וֹם וְאֶת־הַמָּא֤וֹר הַקָּטֹן֙ לְמֶמְשֶׁ֣לֶת הַלַּ֔יְלָה וְאֵ֖ת הַכּוֹכָבִֽים׃

**ASV.** And God made the two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.

**WoH.** And Elohim made the two great luminaries: the greater luminary for the governance of the day, and the lesser luminary for the governance of the night; and the stars.

**Notes.**
- The deliberate refusal to use שֶׁמֶשׁ shemesh (sun) or יָרֵחַ yareach (moon) is the textual feature this verse exists to surface. Both terms were divinized in ANE traditions (Shamash, Sin); Genesis demythologizes by naming them only by function. *The greater luminary / the lesser luminary* preserves the polemic.
- `memshelet`: "governance", not "rule". Technical-political term — the luminaries are functional jurisdictions, not sovereign agents.

#### v17

**He.** וַיִּתֵּ֥ן אֹתָ֛ם אֱלֹהִ֖ים בִּרְקִ֣יעַ הַשָּׁמָ֑יִם לְהָאִ֖יר עַל־הָאָֽרֶץ׃

**ASV.** And God set them in the firmament of heaven to give light upon the earth,

**WoH.** And Elohim set them in the dome of the skies to give light upon the land,

#### v18

**He.** וְלִמְשֹׁל֙ בַּיּ֣וֹם וּבַלַּ֔יְלָה וּֽלֲהַבְדִּ֔יל בֵּ֥ין הָא֖וֹר וּבֵ֣ין הַחֹ֑שֶׁךְ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃

**ASV.** and to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.

**WoH.** and to rule in the day and in the night, and to separate between the light and the darkness. And Elohim saw that it was good.

#### v19

**He.** וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם רְבִיעִֽי׃

**WoH.** And there was evening and there was morning, day four.

---

### Day Five (v20–23)

#### v20

**He.** וַיֹּ֣אמֶר אֱלֹהִ֔ים יִשְׁרְצ֣וּ הַמַּ֔יִם שֶׁ֖רֶץ נֶ֣פֶשׁ חַיָּ֑ה וְעוֹף֙ יְעוֹפֵ֣ף עַל־הָאָ֔רֶץ עַל־פְּנֵ֖י רְקִ֥יעַ הַשָּׁמָֽיִם׃

**ASV.** And God said, Let the waters swarm with swarms of living creatures, and let birds fly above the earth in the open firmament of heaven.

**WoH.** And Elohim said, "Let the waters swarm with swarms of living beings, and let birds fly above the land across the face of the dome of the skies."

**Notes.** `nefesh-chayah`: "living being", not "living creature" or "living soul". *Nefesh* is famously hard — its lexical core is breath/throat/self/life, not a Platonic-detachable soul. ASV's "creature" is acceptable; "soul" (which appears in some translations) is the retrojection to avoid. "Living being" preserves the Hebrew without taking sides.

#### v21

**He.** וַיִּבְרָ֣א אֱלֹהִ֔ים אֶת־הַתַּנִּינִ֖ם הַגְּדֹלִ֑ים וְאֵ֣ת כָּל־נֶ֣פֶשׁ הַֽחַיָּ֣ה ׀ הָֽרֹמֶ֡שֶׂת אֲשֶׁר֩ שָׁרְצ֨וּ הַמַּ֜יִם לְמִֽינֵהֶ֗ם וְאֵ֨ת כָּל־ע֤וֹף כָּנָף֙ לְמִינֵ֔הוּ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃

**ASV.** And God created the great sea-monsters, and every living creature that moveth, wherewith the waters swarmed, after their kind, and every winged bird after its kind: and God saw that it was good.

**WoH.** And Elohim shaped the great dragons, and every living being that moves, with which the waters swarmed, according to their kinds, and every winged bird according to its kind. And Elohim saw that it was good.

**Notes.**
- The verb here is *bara* (shape), not *asah* (made) — used reflectively for the dragons specifically. Why bara for these? *Tanninim* is the Hebrew Bible's standard word for the serpent-dragon class (Job 7:12; Isa 27:1 paired with Leviathan; Ps 74:13; Ezek 29:3 of Pharaoh); the deliberate use of bara here is a demythologizing move — the same dragon-class beings other ANE traditions deify (Akkadian Tiamat, Ugaritic Lotan, Egyptian Apep) are something Elohim *shaped*, not fought. *Tehom* in v2 is etymologically cognate with Tiamat; the chapter brackets the polemic.
- `taninim`: **"great dragons"** (revised from "great sea-creatures" in glossary v2.0.0). The Hebrew word contains no aquatic morpheme — the sea-association in this verse is positional, not lexical. KJV renders the same word "dragon(s)" almost everywhere else in the corpus (Deut 32:33, Ps 91:13, Isa 13:22, Jer 9:11, Mal 1:3) and only dodges to "whales" in Gen 1:21. Modern translations soften to "sea-monsters" or "great sea-creatures"; the lexical case for dragon is the same here as in the prophets. "Great dragons" lets the demythologization polemic show in the translation itself.

#### v22

**He.** וַיְבָ֧רֶךְ אֹתָ֛ם אֱלֹהִ֖ים לֵאמֹ֑ר פְּר֣וּ וּרְב֗וּ וּמִלְא֤וּ אֶת־הַמַּ֙יִם֙ בַּיַּמִּ֔ים וְהָע֖וֹף יִ֥רֶב בָּאָֽרֶץ׃

**ASV.** And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let birds multiply on the earth.

**WoH.** And Elohim blessed them, saying, "Be fruitful and multiply, and fill the waters in the seas; and let the birds multiply on the land."

#### v23

**He.** וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם חֲמִישִֽׁי׃

**WoH.** And there was evening and there was morning, day five.

---

### Day Six (v24–31)

#### v24

**He.** וַיֹּ֣אמֶר אֱלֹהִ֗ים תּוֹצֵ֨א הָאָ֜רֶץ נֶ֤פֶשׁ חַיָּה֙ לְמִינָ֔הּ בְּהֵמָ֥ה וָרֶ֛מֶשׂ וְחַֽיְתוֹ־אֶ֖רֶץ לְמִינָ֑הּ וַֽיְהִי־כֵֽן׃

**ASV.** And God said, Let the earth bring forth living creatures after their kind, cattle, and creeping things, and beasts of the earth after their kind: and it was so.

**WoH.** And Elohim said, "Let the land bring forth living beings according to their kind: cattle, and creeping things, and beasts of the land according to their kind." And it was so.

#### v25

**He.** וַיַּ֣עַשׂ אֱלֹהִים֩ אֶת־חַיַּ֨ת הָאָ֜רֶץ לְמִינָ֗הּ וְאֶת־הַבְּהֵמָה֙ לְמִינָ֔הּ וְאֵ֛ת כָּל־רֶ֥מֶשׂ הָֽאֲדָמָ֖ה לְמִינֵ֑הוּ וַיַּ֥רְא אֱלֹהִ֖ים כִּי־טֽוֹב׃

**ASV.** And God made the beasts of the earth after their kind, and the cattle after their kind, and everything that creepeth upon the ground after its kind: and God saw that it was good.

**WoH.** And Elohim made the beasts of the land according to their kind, and the cattle according to their kind, and every creeping thing of the ground according to its kind. And Elohim saw that it was good.

**Notes.** The animals are *made* (asah), not *shaped* (bara). The sea-creatures of v21 were shaped (bara); the land animals of v25 are merely made. The reason emerges in v26-27.

#### v26

**He.** וַיֹּ֣אמֶר אֱלֹהִ֔ים נַֽעֲשֶׂ֥ה אָדָ֛ם בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ וְיִרְדּוּ֩ בִדְגַ֨ת הַיָּ֜ם וּבְע֣וֹף הַשָּׁמַ֗יִם וּבַבְּהֵמָה֙ וּבְכָל־הָאָ֔רֶץ וּבְכָל־הָרֶ֖מֶשׂ הָֽרֹמֵ֥שׂ עַל־הָאָֽרֶץ׃

**ASV.** And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the birds of the heavens, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.

**WoH.** And Elohim said, "Let us make humankind in our image, according to our likeness; and let them rule over the fish of the sea, and over the birds of the skies, and over the cattle, and over all the land, and over every creeping thing that creeps upon the land."

**Notes.**
- **`naaseh-adam`: "Let us make humankind"** — the cohortative first-person *plural* in נַעֲשֶׂה is grammatically unambiguous in Hebrew. This is the central textual datum for any reading of Elohim as more-than-one and is the WoH lens at full strength. The standard explanations: (i) "plural of majesty" (rare in Hebrew for divine speech, ad hoc), (ii) Trinitarian prefigure (Christian retrojection), (iii) divine-council reading (the modern scholarly consensus, cf. Job 1, Ps 82), or (iv) literal plural agency (the WoH reading). The translation does not adjudicate — it preserves the grammar. The methodology argues for the lens.
- *adam* → "humankind", not "man" — *ha-adam* is a category here, not a personal name (the proper name Adam appears later, in Gen 2-5). Gendered "man" (ASV) is corrected to "humankind" (also NJPS, NRSV).
- *yirdu* → "rule", not "have dominion". ASV's archaism is preserved as "rule" in modern register without losing the strength.

#### v27

**He.** וַיִּבְרָ֨א אֱלֹהִ֤ים ׀ אֶת־הָֽאָדָם֙ בְּצַלְמ֔וֹ בְּצֶ֥לֶם אֱלֹהִ֖ים בָּרָ֣א אֹת֑וֹ זָכָ֥ר וּנְקֵבָ֖ה בָּרָ֥א אֹתָֽם׃

**ASV.** And God created man in his own image, in the image of God created he him; male and female created he them.

**WoH.** And Elohim shaped humankind in his image; in the image of Elohim he shaped him; male and female he shaped them.

**Notes.**
- Three uses of bara (shape) here in tight succession — the verb pattern is deliberate. Humankind is *shaped*, not just *made*. The chapter has now used bara four times: v1 (skies and land), v21 (sea-creatures), v27 (humankind ×3). The pattern: bara is reserved for the categorical creation moments — the initial setting, the unprecedented (sea-creatures, since the demythologized tanninim require special verbal weight), and humankind. Everything else is asah.
- **The plural-singular shift v26→v27**: v26 has plural "Let us make … in our image" (*na'aseh … b'tsalmenu*), v27 has singular "in his image" (*b'tsalmo*) and singular subject *bara* x3. The shift is textually real and the methodology must surface it. Under the WoH lens, the natural reading is: deliberative project speech (plural) → executing agency assignment (singular) within the Elohim group. The text supports a divine-council reading (the modern scholarly consensus) and supports the WoH reading equally well; neither is forced.
- `tselem-demut`: *image / likeness*. The lexical core in Hebrew is *physical* resemblance (cf. Num 33:52, 1 Sam 6:5 — *tselem* as a statue; Ezek 1:5,10 — *demut* as bodily likeness). Traditional readings spiritualize ("man bears God's moral image"); the Hebrew supports physical resemblance directly. The translation preserves the standard rendering and lets the methodology surface the lexical evidence.
- *zachar uneqevah* → "male and female" — biological-anatomical terms. The dimorphic original-act is asserted here (not the sequential Gen 2 reading). Preserved standardly.

#### v28

**He.** וַיְבָ֣רֶךְ אֹתָם֮ אֱלֹהִים֒ וַיֹּ֨אמֶר לָהֶ֜ם אֱלֹהִ֗ים פְּר֥וּ וּרְב֛וּ וּמִלְא֥וּ אֶת־הָאָ֖רֶץ וְכִבְשֻׁ֑הָ וּרְד֞וּ בִּדְגַ֤ת הַיָּם֙ וּבְע֣וֹף הַשָּׁמַ֔יִם וּבְכָל־חַיָּ֖ה הָֽרֹמֶ֥שֶׂת עַל־הָאָֽרֶץ׃

**ASV.** And God blessed them: and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it; and have dominion over the fish of the sea, and over the birds of the heavens, and over every living thing that moveth upon the earth.

**WoH.** And Elohim blessed them. And Elohim said to them, "Be fruitful and multiply, and fill the land, and subdue it; and rule over the fish of the sea, and over the birds of the skies, and over every living thing that moves upon the land."

**Notes.** *kivshuha* "subdue it" and *redu* "rule" are strong verbs and not softened. The verses are the subject of intense exegetical debate in environmental ethics (Lynn White Jr. 1967 and after); the WoH translation does not paper over the strength.

#### v29

**He.** וַיֹּ֣אמֶר אֱלֹהִ֗ים הִנֵּה֩ נָתַ֨תִּי לָכֶ֜ם אֶת־כָּל־עֵ֣שֶׂב ׀ זֹרֵ֣עַ זֶ֗רַע אֲשֶׁר֙ עַל־פְּנֵ֣י כָל־הָאָ֔רֶץ וְאֶת־כָּל־הָעֵ֛ץ אֲשֶׁר־בּ֥וֹ פְרִי־עֵ֖ץ זֹרֵ֣עַ זָ֑רַע לָכֶ֥ם יִֽהְיֶ֖ה לְאָכְלָֽה׃

**ASV.** And God said, Behold, I have given you every herb yielding seed, which is upon the face of all the earth, and every tree, in which is the fruit of a tree yielding seed; to you it shall be for food:

**WoH.** And Elohim said, "Behold, I have given you every seed-bearing plant upon the face of all the land, and every tree in which is the fruit of a tree bearing seed; to you it shall be for food.

#### v30

**He.** וּֽלְכָל־חַיַּ֣ת הָ֠אָרֶץ וּלְכָל־ע֨וֹף הַשָּׁמַ֜יִם וּלְכֹ֣ל ׀ רוֹמֵ֣שׂ עַל־הָאָ֗רֶץ אֲשֶׁר־בּוֹ֙ נֶ֣פֶשׁ חַיָּ֔ה אֶת־כָּל־יֶ֥רֶק עֵ֖שֶׂב לְאָכְלָ֑ה וַֽיְהִי־כֵֽן׃

**ASV.** and to every beast of the earth, and to every bird of the heavens, and to everything that creepeth upon the earth, wherein there is life, I have given every green herb for food: and it was so.

**WoH.** And to every living thing of the land, and to every bird of the skies, and to every thing that moves upon the land in which is a living being—every green plant for food." And it was so.

#### v31

**He.** וַיַּ֤רְא אֱלֹהִים֙ אֶת־כָּל־אֲשֶׁ֣ר עָשָׂ֔ה וְהִנֵּה־ט֖וֹב מְאֹ֑ד וַֽיְהִי־עֶ֥רֶב וַֽיְהִי־בֹ֖קֶר י֥וֹם הַשִּׁשִּֽׁי׃

**ASV.** And God saw everything that he had made, and, behold, it was very good. And there was evening and there was morning, the sixth day.

**WoH.** And Elohim saw all that he had made, and behold, it was very good. And there was evening and there was morning, the sixth day.

**Notes.** Day six closes with the definite article — *yom ha-shishi* "the sixth day", not "a sixth day". The ordinal pattern (days 2–5 lack the article, day 6 has it) marks day 6 as the culminating day, parallel to *day one* being marked by the cardinal. The numbered-day structure is deliberate and bookended.

---

## What the methodology surfaces

Reading the chapter end-to-end through this translation makes several patterns visible that the ASV obscures or smooths:

1. **The verb pattern.** *bara* (shape) is reserved for v1 (skies and land), v21 (the unprecedented sea-creatures), v27 (humankind x3). Everything else is *asah* (make). The chapter is doing categorical work with its verbs.
2. **The "Let us make" v26.** Grammatically plural, textually load-bearing for any reading of Elohim that doesn't pre-commit to singular. The v26 plural → v27 singular shift is real and intelligible under the WoH lens.
3. **The deliberate refusal to use *shemesh* (sun) or *yareach* (moon).** The luminaries are named only by function. This is an ANE polemic against sun/moon deities — preserved by translating *meorot* as "luminaries" and *ha-ma'or ha-gadol/ha-qaton* as "the greater/lesser luminary".
4. **The cosmology of the dome.** The *raqia* is a solid hammered-out vault holding back the upper waters. ASV ("firmament") preserves the solidity in archaic vocabulary; modern translations soften to "expanse" and lose it. WoH says "dome" — accurate and unambiguous.
5. **The construct *bereshit* in v1.** A temporal clause, not an independent declaration of *creatio ex nihilo*. The text describes a project beginning.
6. **The *ruach Elohim* in v2.** "Breath of Elohim" hovering over the waters. The Christian "Spirit of God" reading is one possibility the Hebrew permits but does not require; the WoH choice is the physical reading.
7. **The numbered-day structure.** *Yom echad* (day one, cardinal), then ordinals (sheni–chamishi, days 2–5 without definite article), then *yom ha-shishi* (the sixth day, with article). Bookended, deliberate.
8. **The absence of "good" on day 2.** Preserved without comment in the translation; surfaced here.

These are textual features, not WoH editorializing. Every one of them is grammatically explicit in the Hebrew or attested in modern scholarly consensus. The WoH translation lets them surface; the ASV smooths them out.

The **genuinely WoH-specific** moves — the ones that go beyond consensus — are: the construct *bereshit* (consensus modern; not consensus traditional); *ruach* as breath rather than Spirit (defensible but not consensus); *dome* rather than firmament (modern academic; not the popular English-language reading). Everything else is reading the Hebrew straight and refusing the smoothings the ASV inherited.

---

## What's open / next-step

- **Human review** of this draft before promoting to v1.0.0 stable.
- **Display in the Library reader** — extending `library-book.html` to render parallel WoH + ASV when a chapter has both available. Out of scope for the pilot; on the Phase 2 list.
- **Multi-model comparison.** Running this same chapter through GPT-5 with the same glossary and comparing line-by-line is the next quality multiplier — but only if this pilot is judged worth committing to.
- **Phase 2 trigger.** If this reads better than the ASV under the lens, commit to Genesis 1–11 (the WoH-densest block: creation, Eden, Cain/Abel, antediluvians, Nephilim, flood, Babel). Expand the glossary as those chapters require new entries.

---

## The question

Read v1–v3, v6–v8, v14–v16, v26–v27. These are the verses where the WoH translation does the most work distinct from the ASV. The decision rests on whether they read *better* — more accurate to the Hebrew, more transparent in their methodology, more useful to the WoH reader — than the ASV.

If yes: Phase 2.
If no: the pilot has done its job by killing a cheap option that didn't work. The existing PD-hosting model continues unchanged.
