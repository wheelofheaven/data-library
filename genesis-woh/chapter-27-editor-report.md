# Chapter 27 Editor Report

Genesis 27 — *The blessing-deception, Yitzchaq's two blessings, and Ya'aqov's flight to Haran*

Status moved `draft` → `editor-review`. Version `0.1.0-draft` → `1.0.0-rc1`. Glossary pinned at `2.25.0`.

All 13 of the Translator's `editorial_questions[]` were resolved into glossary entries; the array is now empty. Commentary written at twelve keystone verses (vv 1, 4, 22, 28, 29, 33, 34, 36, 39, 40, 41, 46) plus glossaryRef-only additions at the matamim/nefesh recurrence verses (vv 7, 9, 14, 17, 19, 25, 31).

No `claim_type=speculative` entries were created in this pass. All twelve new glossary entries are `direct` (lexical or grammatical features explicit in the source) except `rebekah-pretext-hittite-wives-cover` which is `inferred` (narrator-irony reading; consistent with Alter and Sternberg). **No human sign-off is required to ship**, but the Reviewer should sanity-check the five items flagged below.

## Items for Reviewer attention

### `ha-qol-qol-yaakov-deception-formula` (v 22)

**Source:** הַקֹּל קוֹל יַעֲקֹב וְהַיָּדַיִם יְדֵי עֵשָׂו
**WoH choice:** "The voice is the voice of Ya'aqov, but the hands are the hands of Esav" (ASV-baseline chiastic-doubling preserved).
**Status:** `direct`. The chiastic-doublet is grammatical; the rabbinic-reception (*Genesis Rabbah* 65:20: *qol* = Torah-study, *yadayim* = Esav-violence) is recorded in the rationale but not read into the running text.
**Reviewer check:** confirm the article-construct repetition reads cleanly in English; the alternative "this is Jacob's voice / these are Esau's hands" smoothing is recorded as an option but rejected.

### `mi-shemanei-ha-aretz-partitive-vs-separative` (vv 39–40) — LOAD-BEARING

**Source:** מִשְׁמַנֵּי הָאָרֶץ ... מִטַּל הַשָּׁמַיִם
**WoH choice:** separative reading at the running text — "away from the fatness of the land ... and away from the dew of the skies." The partitive reading ("of the fatness ... of the dew") is preserved in the glossary apparatus as a defensible alternative.
**Status:** `direct` on both readings; the rationale records both with their scholarly sponsors.
**Why noted:** the same Hebrew preposition does both jobs, and v 39 lacks the partitive-forcing parallel that fixes v 28. Westermann, Speiser, Sarna (apparatus), and NRSV read separative; ASV, KJV, NJPS main text, and rabbinic-harmonizing tradition read partitive. **The WoH translation departs from the *nivrakhu*-precedent here because modern critical scholarship is broadly aligned (not split as at Gen 12:3)**: the context-favoring argument is decisive (Esav gets the *lesser* blessing; the partitive reading produces a near-duplicate of Ya'aqov's v 28 blessing, losing the chapter's central irony); the geographical reading (Edom = arid/marginal Seir-mountain region per Gen 36) is supported by the *cherev tichye* immediately following at v 40. Human reviewer ratified the separative choice 2026-05-25.
**Reviewer check:** confirmed; the partitive alternative is recorded in the glossary apparatus.

### `cherev-tichye-by-the-sword-edom-tradition` (v 40)

**Source:** וְעַל־חַרְבְּךָ תִחְיֶה ... וּפָרַקְתָּ עֻלּוֹ מֵעַל צַוָּארֶךָ
**WoH choice:** "by your sword shall you live ... that you shall break his yoke from off your neck" (ASV-baseline; *tarid* as "break loose").
**Status:** `direct`. The Edom-Israel typology is recorded in the rationale — 2 Kgs 8:20–22 (Edomite revolt under Yehoram), Mal 1:2–5, Obadiah, 1 Macc 5:3.
**Reviewer check:** *tarid* (תָּרִיד) has three philological options (a) "break loose / wander" from *rud* per ASV; (b) "have dominion" linked to *radah* per KJV-Targum and some medieval Jewish exegesis; (c) "grow restive" per NJPS. Default is (a). Confirm.

### `nefesh-blessing-transfer` (vv 4, 19, 25, 31)

**Source:** תְּבָרֶכְךָ נַפְשִׁי / תְּבָרֲכַנִּי נַפְשֶׁךָ
**WoH choice:** transliterate *nefesh* (per project convention with other *nefesh*-cluster entries) rather than render "soul" (post-Hellenistic baggage) or smooth to "innermost blessing" (NJPS).
**Status:** `direct`. *Nefesh* as grammatical subject of "bless" is explicit in the Hebrew at all four verses; the WoH-relevant point is that the blessing is a transfer of vital-self, not a transfer of utterance.
**Reviewer check:** confirm the transliteration reads cleanly in English running prose across all four occurrences, or request a translated equivalent ("vital-self" / "innermost being").

### `rebekah-pretext-hittite-wives-cover` (v 46)

**Source:** קַצְתִּי בְחַיַּי מִפְּנֵי בְּנוֹת חֵת
**WoH choice:** the running translation is straight ("I am weary of my life because of the daughters of Het"); the narrator-irony reading is entirely in the commentary and glossary.
**Status:** `inferred` (the only inferred entry added this chapter). The pretext-reading is consistent with Alter (*Art of Biblical Narrative* ch. 6) and Sternberg (*Poetics of Biblical Narrative*); it is not stated by the narrator in so many words, but the information-asymmetry it tracks (Yitzchaq is not informed of Esav's death-threat; Rivkah recycles the Gen 26:34–35 Hittite-wives complaint as cover) is on the textual surface.
**Reviewer check:** confirm the inferred classification is correct — the alternative would be `direct` (the pretext is grammatically explicit in the chapter's information-distribution) or `speculative` (no, because Alter and Sternberg both read it this way without strain).

## Speculative entries requiring sign-off

None. No `claim_type=speculative` entries were created in this pass.

## Unresolved editorial questions

None. All 13 of the Translator's editorial_questions were resolved into glossary entries.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`, v 2.25.0)

Twelve new entries (all chapter-specific or first-appearance-chapter-27; promoted to central because the *nefesh*-blessing, the *charadah*-trembling, the bitter-cry, the curse-blessing-protection formula, and the *kahah-eynayim* blindness-trigger all recur cross-corpus):

- Added: `kahah-eynayim-patriarchal-blindness-narrative-trigger` (claim_type: `direct`)
- Added: `matamim-savory-food-blessing-meal` (claim_type: `direct`)
- Added: `nefesh-blessing-transfer` (claim_type: `direct`)
- Added: `ha-qol-qol-yaakov-deception-formula` (claim_type: `direct`)
- Added: `tal-shamayim-shemanei-aretz-blessing-formula` (claim_type: `direct`)
- Added: `yaavdukha-amim-peoples-shall-serve-formula` (claim_type: `direct`)
- Added: `cursed-cursers-blessed-blessers-echo` (claim_type: `direct`)
- Added: `va-yecherad-charadah-trembling-formula` (claim_type: `direct`)
- Added: `tzaaqah-gedolah-u-marah-bitter-cry` (claim_type: `direct`)
- Added: `mi-shemanei-ha-aretz-partitive-vs-separative` (claim_type: `direct`)
- Added: `cherev-tichye-by-the-sword-edom-tradition` (claim_type: `direct`)
- Added: `rebekah-pretext-hittite-wives-cover` (claim_type: `inferred`)

Additive `appliesTo` expansions to existing entries (no claim-type or rationale changes):

- `bnei-het-hittites-canaanite-anatolian-question` — added `GEN-WOH-27:46` to appliesTo.
- `morat-ruach-bitterness-of-spirit-esau-hittite-wives` — already includes `GEN-WOH-27:46` (no change needed).
- `yaakov-name-etymology-aqev-supplant` — already includes `GEN-27:36` (no change needed; pre-existing cross-corpus entry using the non-`-WOH` refId convention).
- `bekhorah-birthright-firstborn-status` — already includes `GEN-27:36` (no change needed).

Glossary version: `2.24.0` → `2.25.0` (semver-minor; additive only).

### Per-translation overlay

No overlay changes this chapter. Each new entry is generalizable enough — and the cross-corpus footprint of the formulas is broad enough — to belong in the central glossary.

## Validation

- All glossaryRefs in `chapter-27.json` resolve against `translation-glossary.json` v 2.25.0 (20 unique refs, 0 unresolved).
- `editorial_questions[]` is empty.
- 12 verses have commentary; 8 additional verses received glossaryRefs without commentary (the matamim / nefesh recurrence verses).
- `translation.status` = `editor-review`; `translation.version` = `1.0.0-rc1`; `translation.glossaryVersion` = `2.25.0`.

Ready for the Reviewer agent.
