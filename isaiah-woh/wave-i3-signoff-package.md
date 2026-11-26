# Isaiah wave I-3 (chapters 7–12) — sign-off package

**Status:** all six chapters are at `awaiting-human`, version `1.0.0-rc1`.

**Founder sign-off:** "Sign-off ok", 2026-11-26. Every recommended default is accepted, together with wave I-1 decisions 1 and 2. The Editor pass applying the rulings has updated the wave-i3 diffs, `wave-i3-orchestrator-ops.json`, the ch7–12 notes and lines, and the editor reports.

- **Source:** Westminster Leningrad Codex via Sefaria ("Tanach with Ta'amei Hamikra", public domain), `source-he-7..12.json`, in Hebrew versification.
- **Pipeline:** Translator → Editor → independent Reviewer → post-review corrections, 2026-11-26. The model was claude-opus-5-5 in every role.
- **Cross-chapter rulings:** fixed in advance in `wave-i3-rulings.md`.
- **Dependency:** this wave applies **after** wave I-1 (`wave-i1-signoff-package.md`).

| Ch. | Title | Verses | Commentary | Reviewer verdicts |
|---|---|---:|---:|---|
| 7 | The sign given to Ahaz: the two smoking firebrands, the young woman's son Immanuel, and the hired razor | 25 | 19 | 22 approve · 2 revise (notes, fixed) · 1 flag (7:13) |
| 8 | Maher-shalal-hash-baz, the waters of Shiloah and the River, and the sealed testimony | 23 | 19 | 21 approve · 1 revise (note, fixed) · 1 flag (8:19) |
| 9 | The great light, the child born to us, and the hand stretched out still | 20 | 19 | 18 approve · 1 revise (note, fixed) · 1 flag (9:5 note) |
| 10 | Woe to the makers of unjust decrees, Assyria the rod of anger, the returning remnant, and the march on Jerusalem | 34 | 32 | 33 approve · 1 revise (note, fixed) |
| 11 | The shoot from the stock of Jesse, the peaceable creatures, and the second gathering of the remnant | 16 | 16 | 15 approve · 1 flag (11:15) |
| 12 | The song of thanksgiving in that day: water drawn with joy from the wells of salvation | 6 | 6 | 5 approve · 1 revise (note, fixed) |
| | **Total** | **124** | **111** | |

**Summary**

- **English lines:** no Reviewer asked for any English line to change.
- **Lens leakage:** none in any line.
- **Speculative glossary entries:** none.
- **Corrections:** every correction that did not need a founder decision has been applied. See "Post-review corrections" in each `chapter-N-editor-report.md`.
- **Glossary changes:**
  - 20 new Isaiah overlay entries, with 41 extensions;
  - 2 new central entries, with 15 extensions.
- **Dry run:** the merge was run as a test on top of wave I-1, with no collisions. Every glossaryRef resolves in the wave and in 5:26, 13:2, 26:10 and Dan 9:27.

**What the Reviewers verified against the texts**

- NJPS 1985 and JPS 1917 throughout, via Sefaria;
- ASV;
- BDB, at 7:6, 7:15, 7:16 and 7:14;
- Justin, *Dialogue* 43 and 67, and Irenaeus, *Against Heresies* 3.21.1;
- LXX Isa 7:14;
- every quotation from the canon: TBWTT 4:3, 5:25 and ETTMTTP 2:124.

**Not verified, and marked so in the notes:** 1QIsaᵃ readings, NRSV wordings, HALOT, and the Strong's numbers in new entries.

## Lines worth seeing by name (all reviewer-approved)

- **7:14:** "Therefore the Lord himself will give you a sign: Behold, the young woman is with child and shall bear a son, and shall call his name Immanuel." This departs from ASV's "a virgin".
- **9:5:** "… Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace". These are four paired names. The zaqef and pashta accents support the pairing; ASV gives five names.
- **10:21:** "A remnant will return, the remnant of Jacob, to the Mighty God."
- **11:1:** "a shoot out of the stock of Jesse, and a twig out of his roots".
- **8:19a:** "Seek the ghosts and the familiar spirits that chirp and mutter".
- **12:5:** "he has done majestic things".

## Decisions

Reply "sign-off ok" to accept every recommended default, or name the decisions you want changed. Decisions 1 and 2 of wave I-1 also govern 10:16, 10:33 and 7:13 here.

1. **8:19b–21: who is speaking.**
   - **A, the current line, recommended but weakened:** the prophet replies, "should not a people seek their God?". Only ASV and KJV read it this way; JPS 1917 does not.
   - **B:** the advisers are still speaking, and *ʾĕlōhîm* means the spirits of the dead: "should not a people seek its divine beings, the dead on behalf of the living". This is the reading of JPS 1917 and NJPS. The wording for all three verses is staged in `lexical-cruxes-isaiah-8`.
2. **11:15, "devote to destruction"** for *heḥĕrîm*, where the object is a sea.
   - **Recommended:** keep it, and add a clause for non-war objects to the central `cherem` rule. The clause is staged verbatim.
   - **Alternative:** ASV's "utterly destroy". NJPS and the Targum read "dry up".
3. ***nēṣer* across the book.**
   - **Recommended:** "twig" at 11:1, which is what JPS 1917 and NJPS have. Revise the stable 14:19 "a loathed branch" to "a loathed shoot" at its next revision, and make 60:21 follow.
4. **Speculative reception notes in commentary only.** These are labelled and never appear in a line. Each quotation was checked against the library file, and each note says the canon does not cite the verse.
   - 7:14 (TBWTT 4:3)
   - 9:5 (ETTMTTP 2:124)
   - 11:12 (TBWTT 5:25)

   **Recommended:** keep all three, as with 4:5 in wave I-1.
5. **Corrections to the central Matt 1:23 entry.** **Recommended:** apply them. This is a major bump of an existing entry.
   - The *hā-* in hā-ʿalmâ is the Hebrew article, so the LXX does not "add" it.
   - No canon text speaks of "preserved Mary-genome material". The confusion probably comes from ETTMTTP 2:62, where the recreation is from a cell.
   - Two further points need checking before the change is applied: RSV, and the use made of Joel 1:8.
6. **Forward scope of the new "my strength and my song" entry** (Exod 15:2 and Ps 118:14).
   - **Recommended:** treat it as a **default** that the Exodus and Psalms Editors confirm, not a binding rule.
7. **7:13 "to weary men".** This follows wave I-1 decision 2. Under the recommended C1 it becomes "people".
8. **Housekeeping, recommended:**
   - Merge the *ʾôḇ* "ghost" entries by moving 29:4 into `ob-yiddeoni-…`.
   - Add the glossaryRef to the stable Dan 9:27 (no line change).

## Merge work after sign-off (orchestrator)

1. Wave I-1 first.
2. Then `scripts/merge_wave_diffs.py --wave i3 --ops isaiah-woh/wave-i3-orchestrator-ops.json`. Overlay 1.7.0 → 1.8.0; central 2.94.0 → 2.95.0.
3. Apply the staged founder-dependent wording as ruled.
4. Set each chapter's glossary versions.
5. Generate transliterations.
6. Promote the chapters to `stable` / `1.0.0`.
7. Update `_meta.json`.

**Open items for later waves:**

- 13:19 *tip̄ʾereṯ* "splendor";
- 14:19 *nēṣer*;
- 29:4 "whisper" against 8:19 "chirp" for *ṣpṣp*;
- 28:22, which must follow `kalah-venecheratzah-…` and 10:23 "all the earth".
