# Genesis 21 — sign-off package

**Status:** reviewer-approved (clean approve sweep; sign-off is formality; two non-blocking cleanup flags for future passes)
**Chapter:** 21 — Isaac's birth + third laughter-play; Hagar/Ishmael expulsion + *malakh Elohim*; Beersheba covenant
**Version:** 1.0.0-rc1
**Glossary version:** 2.18.0

## Summary table

| Metric | Value |
|---|---|
| Verses translated | 34 / 34 |
| Reviewer verdicts | **34 approve / 0 revise / 0 flag** |
| New glossary entries | 7 (all `direct`, 0 inferred, 0 speculative) |
| Existing-entry corrections | 1 (`malakh-yhwh-messenger` appliesTo: -GEN-21:17) |
| Glossary verdicts | 7/7 new approve · 1/1 correction approve |
| Verses with commentary | 8 / 34 |
| Verses with glossaryRefs | 18 / 34 |
| Lens-leakage flags | **0** |
| Items requiring human-only judgement | 0 |

## The three load-bearing entries

### `metzacheq-ishmael-debate` (v 9)

Sarah sees Ishmael *metzacheq* — and Sarah demands the expulsion of Hagar and Ishmael on the basis of whatever *metzacheq* means. Four readings preserved in parallel:
- **Playing** (Sarna, Alter, NJPS, Westermann, Hamilton — modern critical default)
- **Playing-with-Isaac** (LXX adds *meta Isaak tou huiou autēs*; NRSV; Paul Gal 4:29)
- **Mocking** (ASV, KJV — traditional rendering implying disrespect)
- **Maximal rabbinic** (Gen Rab 53:11, b. Sotah 26b, Rashi — idolatry / sexual immorality / inheritance-threat)

**WoH chose "playing."** Reviewer-verified: *"Editorial principle of not importing rabbinic-tradition harshness on Yishma'el explicitly stated."* The chapter doesn't tell us what Ishmael was doing — the milder reading respects the lexical default and the narrative ambiguity.

### `malakh-elohim-messenger` (v 17)

First occurrence in the Hebrew Bible of the *malakh Elohim* phrasing — **distinct from** *malakh YHWH* (existing entry covers that). The source-critical reading: this Hagar scene (Gen 21) is the E-document version; the first Hagar scene (Gen 16) is the J-document version. Westermann pp. 339-340 documents the divine-name split as the principal source-critical evidence for E in the Hagar narrative.

Reviewer-verified: *"Parallel-but-distinct framing from `malakh-yhwh-messenger` (not a sub-variant) is editorially correct. J/E source-critical reading presented as standard modern critical, with post-documentary critique (Van Seters, Carr, Schmid) also presented."*

### `yhwh-el-olam` (v 33)

First *El Olam* in HB. Joins the patriarchal El-compound pattern:
- **El Elyon** at Gen 14 (Melchizedek)
- **El Roi** at Gen 16 (Hagar)
- **El Shaddai** at Gen 17 (Abraham)
- **El Olam** at Gen 21 (now)

Religious-historical-syncretism reading (Alt 1929 *Der Gott der Väter*, Cross 1973 *Canaanite Myth and Hebrew Epic* ch. 1, Smith 2001, Day 2000, Köckert 1988) framed as mainstream scholarship. The appositional *YHWH El Olam* parallels Gen 14:22 *YHWH El Elyon* — same Yahwistic-harmonization editorial move.

Reviewer-verified: *"Olam read in temporal-duration register per HALOT, BDB, TDOT/Preuss, Jenni 1952-53; abstract-eternity overreading correctly rejected."*

## The appliesTo correction

The `malakh-yhwh-messenger` entry from v2.13.0 (Gen 16) had **GEN-21:17 incorrectly in its appliesTo array**. Re-parse confirmed: Gen 21:17 uses *malakh Elohim*, not *malakh YHWH*. The Editor removed GEN-21:17 from `malakh-yhwh-messenger.appliesTo` and added it to the new `malakh-elohim-messenger.appliesTo`.

**Semver judgment:** Editor and Reviewer concur on semver-minor (v2.18.0) rather than semver-major. The change is metadata correction; both entries render *mal'akh* identically as "messenger"; no downstream translation text changes.

## All 7 new entries (v2.18.0)

| Slug | Notes |
|---|---|
| `metzacheq-ishmael-debate` | LOAD-BEARING; four readings; WoH chose "playing" |
| `malakh-elohim-messenger` | LOAD-BEARING; J/E source-critical; distinct from malakh-yhwh |
| `paqach-eynayim-revelatory-perception` | Well-was-always-there vs. well-created |
| `elohim-imkha-divine-presence-formula` | Cross-corpus through patriarchs/Moses/Joshua/David |
| `be-er-sheva-folk-etymology` | *sheva* (seven) / *shava* (oath) double-etymology |
| `yhwh-el-olam` | LOAD-BEARING; first El Olam; completes patriarchal El-compound pattern |
| `eshel-tamarisk-cultic-site` | *Tamarix aphylla* sacred-tree-cultic register |

## Non-blocking cleanup flags (for future passes)

Reviewer surfaced two items worth noting for downstream work:

1. **`malakh-yhwh-messenger` rationale narrative** still mentions "Gen 21:17 (Hagar at the well at Beer-Lachai-Roi, second encounter)" — stale narrative contradicted by the corrected appliesTo. Worth a one-line cleanup pass.

2. **`malakh-yhwh-messenger.appliesTo` still includes GEN-31:11**, but the new `malakh-elohim-messenger` rationale explicitly identifies Gen 31:11 as *malakh ha-Elohim*. A parallel correction will be needed **when Gen 31 is processed**.

Both items are out-of-scope for this chapter; flagged for visibility.

## Production note: pipeline recovery

The Translator pass failed once on a ConnectionRefused error before producing any output, then succeeded cleanly on retry. No partial artifacts; audit trail intact.

## Sign-off requested

No contested decisions. Sign-off is formality.

## Editor escalation report

See `/Users/zara/Development/github.com/wheelofheaven/data-library/genesis-woh/chapter-21-editor-report.md`.

## Reviewer report

Embedded in chapter JSON at `translation.reviewerReport`. Citations from Westermann, Sarna, Wenham, Hamilton, Speiser, Alter, Skinner ICC (standard Genesis); Sarna/Alter/NJPS + Genesis Rabbah 53:11, b. Sotah 26b, Rashi, Paul Gal 4:29 (*metzacheq*); Westermann pp. 339-340, Friedman 1987, Skinner 1910, Van Seters/Carr/Schmid (*malakh Elohim* source-critical); Alt 1929 *Der Gott der Väter*, Cross 1973, Smith 2001, Day 2000, Köckert 1988, HALOT/BDB/TDOT/Jenni 1952-53 (*El Olam*); Preuss 1968 *Jahweglaube und Zukunftserwartung* (divine-presence formula); Pope 1985 (sacred-tree-cultic-site); Aharoni, Herzog (Tell es-Seba archaeology).
