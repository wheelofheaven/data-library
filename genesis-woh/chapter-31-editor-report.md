# Chapter 31 Editor Report

## Summary

Genesis 31 — Ya'aqov's flight from Lavan, the stolen teraphim, and
the covenant of Gal-Ed and Mitzpah.

- **54 verses** processed (Translator passed clean).
- **11 editorial_questions[] resolved** to empty.
- **8 new glossary entries added** to the central glossary (matches
  the brief's projected 8).
- **All 8 entries `claim_type: direct`** — no `speculative` entries
  this chapter, no `inferred` entries. Every divergence is grounded
  in mainstream modern-critical philology and the established
  scholarly literature.
- **One deferred editorial correction executed**: `GEN-31:11` removed
  from `malakh-yhwh-messenger.appliesTo` (the verse uses *mal'akh
  ha-Elohim*, not *mal'akh YHWH*) and added to
  `malakh-elohim-messenger.appliesTo`. The correction was flagged
  for deferred action in v2.18.0 when the `malakh-elohim-messenger`
  entry was first created; this release executes it.
- **AppliesTo expansions** on five existing entries
  (`matzevah-sacred-pillar-patriarchal-religion`,
  `anokhi-elohei-X-avikha-ancestral-god-formula`,
  `divine-dream-communication-formula`,
  `elohim-imkha-divine-presence-formula`, `camel-anachronism`).
- **Glossary bumped v2.28.0 → v2.29.0** (semver-minor; additions and
  one semver-major-equivalent appliesTo correction on
  `malakh-yhwh-messenger`, but the correction was already
  pre-announced in the v2.18.0 release-note).
- **Chapter advanced** to `editor-review` / `1.0.0-rc1` /
  `glossaryVersion: 2.29.0`.

## Speculative entries requiring sign-off

**None.** No `claim_type: speculative` entries were added for this
chapter.

All eight new entries were shippable as `direct` on the following
grammatical-and-philological grounds:

- **`ha-el-beit-el-divine-self-identification`** — the construction
  *anokhi ha-El Beit-El* is grammatically explicit in the MT; the
  patriarchal-El-compound pattern (El Elyon, El Ro'i, El Shaddai,
  El Olam, El Beit-El, El Elohei Yisra'el) is documentary-attested;
  the Alt 1929 / Cross 1973 / Smith 2001 religious-historical
  reconstruction is mainstream modern-critical.
- **`teraphim-household-gods`** — the lexeme is grammatically
  explicit at the seven chapter-31 occurrences and across the
  cross-corpus distribution (Judg 17-18, 1 Sam 15:23 and 19:13-16,
  2 Kgs 23:24, Hos 3:4, Ezek 21:26, Zech 10:2); the Nuzi-parallel
  inheritance-token reading is the standard background (Speiser
  1964; contested by Greenberg 1962; modified by van der Toorn
  1990); the modern critical synthesis (van der Toorn, Albertz,
  Smith) is documentary.
- **`ganav-et-lev-deceive-idiom`** — the idiom is grammatically
  explicit at Gen 31:20, 26 and at 2 Sam 15:6; the chapter's seven
  *g-n-v* deployments are HB-internal-explicit and documented in
  the Alter / Sarna / Westermann commentary.
- **`tov-ra-merism`** — the construction *mi-tov ad-ra* is
  grammatically explicit; the merism device is documented in the
  foundational rhetorical-criticism literature (Honeyman 1952;
  Watson 1984; Krašovec 1977).
- **`derekh-nashim-menstrual-period-euphemism`** — the construction
  is grammatically explicit; the Gen 18:11 parallel and the
  Lev 15:19-30 *niddah* legislation are documentary; the
  ritual-purity reading of Rachel's speech-act is mainstream modern
  critical (Sarna, Westermann, Hamilton, Wenham, Alter, Speiser).
- **`pachad-yitzchaq-fear-of-isaac-divine-epithet`** — the
  construction is grammatically explicit at the two HB occurrences;
  the two readings (Alt 1929 / Albright 1935-Cross 1973 vs. Hillers
  1972-73) are documented in the foundational scholarly literature.
  Both readings preserved; ASV-baseline default adopted.
- **`yegar-sahaduta-galed-bilingual-witness-heap`** — the Aramaic
  and Hebrew phrases are grammatically explicit; the
  morpheme-for-morpheme correspondence is verifiable lexically; the
  hapax-status of Aramaic in the Pentateuch is documentary.
- **`mitzpah-blessing-formula`** — the etymology on the *tz-p-h*
  root is grammatically explicit; the treaty-surveillance reading
  is HB-internal-explicit (vv 50-52 specify the surveillance
  content); the modern Christian benediction-reception is
  well-documented in hymnology and devotional literature.

## Reviewer attention requested

While none of the new entries are `speculative`, four are
**load-bearing chapter-anchors** that the Reviewer should examine
with particular care:

### `teraphim-household-gods` — LOAD-BEARING

The lexeme is one of the HB's most editorially-load-bearing
cultic-material-culture nouns and is high lens-leverage for the
Wheel of Heaven project. The entry as written stays within the
mainstream modern-critical philological landscape (van der Toorn
ancestor-cult-statue reading, Speiser Nuzi-parallel
inheritance-token reading, the form-and-function dispute). **Any
WoH-distinctive synthesis on the teraphim — e.g., reading them as
physical-markers of patriarchal-period extraterrestrial-encounter,
or as preserved-artifacts of an earlier civilization's material
culture — is reserved for the wiki and long-form material and is
not in the glossary entry.** The Reviewer should verify that the
wiki-side WoH synthesis is in place separately and that nothing
WoH-distinctive has leaked into the glossary entry.

The entry's `appliesTo` covers GEN-WOH-31:19, 30, 32, 34, 35 (the
five chapter-31 verbal references); cross-corpus expansion to
Judges 17-18, Samuel, Kings, Hosea, Zechariah, Ezekiel is deferred
to those chapters' translations.

### `pachad-yitzchaq-fear-of-isaac-divine-epithet`

The two readings (Alt 1929 traditional *Fear* vs. Albright 1935 /
Cross 1973 *Kinsman*) are both defensible and have not converged in
two generations of scholarship. The Reviewer should verify:

1. The ASV-baseline *the Fear of Yitzchaq* is the right default
   (vs. the kinship-reading or full transliteration *Pachad
   Yitzchaq*). The decision matters because *Pachad Yitzchaq*
   recurs in Christian-and-Jewish theological tradition under the
   *Fear* reading; the kinship-reading would be a more substantial
   departure.
2. The entry's representation of the Hillers 1972-73 dispute is
   fair — the kinship-reading remains contested and is not
   consensus.

The entry preserves both readings in the rationale and uses the
*Fear* default; the kinship-reading is documented but not adopted.
This is the editorially-conservative choice.

### `yegar-sahaduta-galed-bilingual-witness-heap`

The only continuous Aramaic phrase in Genesis (and in the
Pentateuch). The Reviewer should verify:

1. The authenticity-question (archaic vs. late editorial insertion)
   is preserved as agnostic — the entry does not adjudicate. This
   matches the Sarna / Wenham / Westermann scholarly posture.
2. The narrative-functional reading of the bilingual contrast (as
   ethno-cultural-pivot rather than dialect-confusion) is the
   default — this is mainstream Speiser / Westermann / Sarna.
3. The cross-corpus framing of the Aramean-Hebrew distinction
   (Bethuel and Lavan as *Aramim*; Deut 26:5 *Arami oved avi*) is
   accurate.

### `mitzpah-blessing-formula` — RECEPTION-INVERSION FLAG

The chapter-31 verse is the source of the modern Christian *Mizpah
blessing* — and the reception **inverts** the original force. In
context the *yitzef YHWH* clause is a mutual-surveillance
treaty-formula; in modern devotional use it has become a
parting-affection-blessing. The Reviewer should verify:

1. The reception-inversion is named clearly and the original
   treaty-surveillance force is preserved as primary in the entry.
2. The continuation at vv 50-52 (which specifies the surveillance
   content — non-aggression, no additional wives, no boundary
   crossing for harm) is presented as the load-bearing evidence
   for the original reading.
3. The modern reception is documented but not preempted — readers
   should be able to recover both the in-context reading and the
   reception-tradition.

The reception-inversion note is editorially significant because the
Mitzpah-blessing is one of the most-quoted Genesis verses in modern
Christian devotional culture, and the gap between the original and
the reception is wide.

## Unresolved editorial questions

**None.** All eleven editorial_questions[] from the Translator have
been resolved — eight into new glossary entries, one into the
`malakh-yhwh-messenger` / `malakh-elohim-messenger` correction, and
the remaining (v 13 *anokhi ha-El Beit-El* default; v 32
Rachel-death-anticipation; v 53 *Elohei Avraham v-Elohei Nachor*
collateral-deity treatment) into per-verse commentary and existing
entry expansions.

## Glossary changes for review

### Central glossary (`data-content/i18n/translation-glossary.json`)

**Version bump**: v2.28.0 → v2.29.0 (semver-minor for additions; the
`malakh-yhwh-messenger` appliesTo correction is in effect a
semver-major change on that single entry but was pre-announced in
v2.18.0 and is executed here).

**Added**:

- `ha-el-beit-el-divine-self-identification` (claim_type: `direct`)
- `teraphim-household-gods` (claim_type: `direct`)
- `ganav-et-lev-deceive-idiom` (claim_type: `direct`)
- `tov-ra-merism` (claim_type: `direct`)
- `derekh-nashim-menstrual-period-euphemism` (claim_type: `direct`)
- `pachad-yitzchaq-fear-of-isaac-divine-epithet` (claim_type: `direct`)
- `yegar-sahaduta-galed-bilingual-witness-heap` (claim_type: `direct`)
- `mitzpah-blessing-formula` (claim_type: `direct`)

**Modified — appliesTo corrections**:

- `malakh-yhwh-messenger.appliesTo`: removed `GEN-31:11` (was
  erroneously included; the verse uses *mal'akh ha-Elohim*, not
  *mal'akh YHWH*). Deferred-correction from v2.18.0.

**Modified — appliesTo expansions**:

- `malakh-elohim-messenger.appliesTo`: added `GEN-WOH-31:11`.
- `matzevah-sacred-pillar-patriarchal-religion.appliesTo`: added
  `GEN-WOH-31:13`, `GEN-WOH-31:45`, `GEN-WOH-31:51`,
  `GEN-WOH-31:52`.
- `anokhi-elohei-X-avikha-ancestral-god-formula.appliesTo`: added
  `GEN-WOH-31:5`, `GEN-WOH-31:29`, `GEN-WOH-31:42`,
  `GEN-WOH-31:53`.
- `divine-dream-communication-formula.appliesTo`: added
  `GEN-WOH-31:24`.
- `elohim-imkha-divine-presence-formula.appliesTo`: added
  `GEN-WOH-31:3`.
- `camel-anachronism.appliesTo`: added `GEN-31:34` (Rachel sitting
  on the camel's saddle — the second camel-reference in the
  chapter).

### Per-translation overlay (`_translation-glossary.json`)

**No overlay file created.** All eight new entries cover cross-corpus
lexemes or project-wide conventions (teraphim across HB; *ganav et-lev*
across Genesis / 2 Sam; *tov-ra* merism corpus-wide; *derekh nashim*
with the Lev 15 *niddah* cross-link; *Pachad Yitzchaq* across Genesis;
*Yegar Sahaduta* hapax but the bilingual-witness-heap principle is
cross-tradition; Mitzpah is the eponym for multiple cross-corpus
toponyms; *ha-El Beit-El* within the patriarchal-El-compound pattern).
All eight are appropriate for the central glossary.

## Commentary written

Substantial per-verse commentary added to:

- **v 11** — *mal'akh ha-Elohim* with the editorial-correction note
  (deferred from Gen 21).
- **v 13** — *ha-El Beit-El* with the patriarchal-El-compound
  pattern and the cross-link to Gen 28.
- **v 19** — *teraphim* (substantial; the LOAD-BEARING entry's
  commentary covers cross-corpus distribution, Nuzi-parallel,
  van der Toorn synthesis).
- **v 20** — *ganav et-lev* with the chapter's seven *g-n-v*
  deployments cataloged.
- **v 24** — *Gen 20:3 parallel* + *tov-ra* merism.
- **v 32** — Rachel-death-anticipation (the Gen 35:18-20 link); the
  *elohim*-as-category lexeme.
- **v 35** — *derekh nashim* (substantial; ritual-purity speech-act,
  chapter-deepest narrative-irony).
- **v 42** — *Pachad Yitzchaq* (substantial; the Alt / Albright /
  Cross / Hillers two-generation debate).
- **v 47** — *Yegar Sahaduta / Gal-Ed* (substantial; only continuous
  Aramaic in Genesis; authenticity-debate).
- **v 49** — *Mitzpah blessing* with the reception-inversion note.
- **v 53** — *Pachad Yitzchaq* recurrence; *Elohei Avraham v-Elohei
  Nachor* collateral-deity treatment with the harmonizing-apposition
  *Elohei avihem* note.

## Editorial pass markers

This is a 2026-05 editorial-pass output. The chapter reflects:

- The current WoH framing (the patriarchal narratives as preserving
  authentic pre-Mosaic patriarchal-El-religion strata; the teraphim
  as material-culture of household-cult-religion with both religious
  and legal dimensions; the *Pachad Yitzchaq* and *El Beit-El* as
  evidence for the Alt / Cross ancestral-and-local-El-religion
  reconstruction).
- The current WoH register (scholarly-but-accessible; comparative
  claims hedged; canon-internal claims direct; reception-history
  surfaced where reception inverts original meaning, as at v 49).
- The current WoH editorial discipline (no speculative entries; all
  divergences from PD baseline grounded in mainstream modern
  critical scholarship; project-specific synthesis explicitly
  reserved for the wiki, not the glossary or the translation).

## Ready for Reviewer

Chapter is ready for the Reviewer agent and then human sign-off.
The four load-bearing entries — `teraphim-household-gods`,
`pachad-yitzchaq-fear-of-isaac-divine-epithet`,
`yegar-sahaduta-galed-bilingual-witness-heap`, and
`mitzpah-blessing-formula` — are the focus of Reviewer attention.
The deferred `malakh-yhwh-messenger` / `malakh-elohim-messenger`
correction is executed and verified.
