# Isaiah wave I-4 (chapters 16–23) — sign-off package

**Status:** all eight chapters `awaiting-human` (20: `reviewer-approved`), version `1.0.0-rc1`. Source: Westminster
Leningrad Codex via Sefaria, `source-he-16..23.json`. Pipeline: Translator → Editor → independent Reviewer →
post-review corrections (2026-11-26); claude-opus-5-5 in every role. Cross-chapter rulings: `wave-i4-rulings.md`
(15 rules; rules 12–15 were set during the wave: Cush, scope of the gender-neutral rule, "as the years of a
hireling", "the Nile").

| Ch. | Title | Verses | Commentary | Reviewer |
|---|---|---:|---:|---|
| 16 | The oracle concerning Moab continued: the plea for refuge, the throne established in kindness, and the lament for the vine of Sibmah | 14 | 13 | 12 approve · 2 revise (notes, fixed) |
| 17 | The oracle concerning Damascus: the thinning of Jacob's glory, the pleasant plants, and the roaring of the peoples | 14 | 14 | 13 approve · 1 revise (note, fixed) |
| 18 | The land of rustling wings beyond the rivers of Cush, and the gift brought to Mount Zion | 7 | 7 | 6 approve · 1 revise (note, fixed) |
| 19 | The oracle concerning Egypt: YHWH on a swift cloud, the Nile dried up, and the altar in the land of Egypt | 25 | 25 | 23 approve · 1 revise (note, fixed) · 1 flag (19:12) |
| 20 | The prophet naked and barefoot for three years, a sign concerning Egypt and Cush | 6 | 6 | 6 approve |
| 21 | The oracle concerning the wilderness of the sea: the watchman, fallen Babylon, Dumah and Arabia | 17 | 17 | 14 approve · 3 revise (notes, fixed) |
| 22 | The oracle concerning the valley of vision, and the key of the house of David given from Shebna to Eliakim | 25 | 24 | 23 approve · 2 revise (22:16 note fixed; 22:15 below) |
| 23 | The oracle concerning Tyre: the ships of Tarshish wail, and Tyre's seventy years | 18 | 18 | 15 approve · 3 revise (notes, fixed) |
| | **Total** | **126** | **124** | |

No Reviewer asked for an English line to change except as listed below; no lens leakage in any line; no
speculative glossary entries. Reviewers verified NJPS 1985 and JPS 1917 (Sefaria), ASV, the LXX (Rahlfs, at 18 and
23), BDB (at 18), the project's Baal Cycle edition (19:1), and every canon quotation (TBWTT 3:107, 3:144–145,
3:259–260; LWTE 2:184–190). Reviewers caught and the Editors fixed: four misattributions of JPS 1917 as ASV (20:3,
20:5) and of NJPS (17:8, 21:5, 22:16), a wrong collation author (23), an overstated Adonis claim (17:10).
Unverified items are marked "not verified" in the notes (1QIsaᵃ, NRSV, HALOT, most commentators).

Dry-run merge (overlay 2.0.0 + 8 diffs + orchestrator ops): 22 new Isaiah entries, 56 extensions, 25 central
extensions; no collisions; every glossaryRef resolves, including the stable chapters that gain refs
(11:11, 43:3, 45:14 Cush; 24:16; 54:2; 1 Sam 17:46).

## Lines worth seeing

- **18:1** "Woe, land of the rustling of wings, which is beyond the rivers of Cush" — names no referent.
- **19:1** "Behold, YHWH rides on a swift cloud and comes to Egypt" — the clause, no epithet.
- **19:18** "the City of Destruction" (MT); "City of the Sun" in commentary.
- **21:11** "Watchman, what of the night? Watchman, what of the night?"
- **22:22** "And the key of the house of David I will lay on his shoulder…" (Rev 3:7 in commentary).
- **23:9** "to profane the pride of all beauty".

## Decisions (reply "sign-off ok" to accept every recommended default, or name the ones to change)

1. **Speculative reception notes** at 18:1 (wings; cites TBWTT 3:144–145 on 6:2 and LWTE 2:187–190, says the canon
   does not cite Isa 18) and 19:1 (cloud; TBWTT 3:107, 3:259–260; canon does not cite Isa 19) — **keep**
   (recommended), as at 4:5, 7:14, 9:5, 11:12.
2. **Shofar.** 18:3 "a shofar" (central rule, used across the corpus) — **keep, and revise stable 27:13 "a great
   trumpet" → "a great shofar"** (recommended, applied now as a stable patch).
3. **21:14** — **print the command "To meet the thirsty bring water!"** (recommended: JPS 1917, NJPS, the same form is
   imperative at Jer 12:9, the main pause falls after "water"), or keep ASV "they brought water".
4. **21:6 "lookout"** for mᵉṣappeh, distinct from "Watchman" (šōmēr) at 21:11–12 — **keep** (recommended; NJPS makes
   the same split).
5. **22:15** — **"steward"** (recommended by the Reviewer; JPS 1917, NJPS) or ASV "treasurer".
6. **16:11 "my inner parts … my inmost being"** for mēʿay, keeping "heart" for lēḇ — **keep** (recommended), or
   "my heart" as ASV/JPS/NJPS.
7. **19:12 "your wise men"** — **keep** (recommended: a specific professional class under rule 13; matches stable
   29:14 "its wise men"), or NJPS "your sages".
8. **ṣᵉḇî**: "beauty" (4:2; 23:9) is the default; **record 24:16 "Glory to the righteous one!" as an idiomatic
   departure, and revise stable 13:19 "the glory of kingdoms" → "the beauty of kingdoms"** (recommended).
9. **Book-wide entries** created at merge: **tip̄ʾereṯ "honor"** (4:2, 10:12, 20:5; 13:19 "splendor" recorded as a
   departure) and **non-divine kāḇôḏ "glory"** — recommended.
10. **Central corrections** (major): rider-of-the-clouds KTU sites (only 1.2 iv 6, 1.3 ii 40, 1.3 iv 23, 1.4 vi 10
    print rkb ʿrpt in the project edition); `yeor` "the Nile" Isaiah clause; `eretz` carrion-formula clause
    ("beasts of the earth") — **apply** (recommended).
11. **Stable revision already ruled** (wave I-3): 14:19 "a loathed branch" → "a loathed shoot" — applied with this
    sign-off.

## Merge work after sign-off (orchestrator)

`merge_wave_diffs.py --wave i4 --ops wave-i4-orchestrator-ops.json`; overlay 2.0.0 → 3.0.0 / central 3.0.0 → 4.0.0
if any existing entry's wohChoice/rationale is rewritten (decisions 8–10 do), else minor; stable patches 13:19, 14:19,
27:13 to 1.0.1 with glossary refs; transliterations regenerated by tool only; promote 16–23; `_meta.json`;
dataset rebuild and upload.
