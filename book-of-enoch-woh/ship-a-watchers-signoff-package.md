# Ship A (Book of the Watchers, 1 Enoch 1-36) — Sign-off Package

**Status:** `reviewer-approved` — ready for human sign-off.
**Version:** `1.0.0-rc2` across all 36 chapters.
**Editorial pass:** `2026-06`.
**Glossary versions:** central `v2.66.0`; overlay `v1.1.0`.

---

## Summary table

| Metric | Count |
|---|---|
| Chapters translated | 36 |
| Verses translated | 248 |
| Editorial questions raised by Translator | 131 |
| Editorial questions resolved by Editor | 131 (100%) |
| New central glossary entries | 17 (all `claim_type=direct`) |
| Existing central glossary extensions | 17 |
| New per-translation overlay entries | 7 |
| Verses with per-verse commentary | 46 |
| Reviewer verdicts: approve | 248 (100%) |
| Reviewer verdicts: revise-suggested | 0 |
| Reviewer verdicts: flag-for-human | 0 |
| Lens-leakage flags | 0 |
| Speculative entries pending sign-off | 0 |

---

## What was done

**Translator (woh-translator)** drafted English at ASV/RSV-baseline register for 36 chapters / 248 verses. Layered-witness source schema (Aramaic DSS where preserved, Greek Akhmim Panopolitanus secondary, Ge'ez tertiary; Ge'ez becomes primary at ch 32:6 where Akhmim breaks off). Aramaic onomastics preserved (Šemiḥazah, ʿAśāʾēl/ʿAzazʾēl, Bărāqʾēl, Kōkabʾēl, archangel theophorics). 131 editorial questions flagged for the Editor.

**Editor (woh-editor)** resolved all 131 questions, added 17 new central glossary entries + 17 existing-entry extensions + 7 overlay entries, drafted commentary on 46 high-priority verses, bumped central glossary v2.65.0 → v2.66.0 and overlay v1.0.0 → v1.1.0, advanced all 36 chapters draft → editor-review at v1.0.0-rc1.

**Reviewer (woh-reviewer)** independently verified all 248 verses against sources, verified all 17 new central entries against named scholarship (Nickelsburg 2001, Milik 1976, Black 1985, Charles 1912, Knibb 1978, Reed 2005, Stuckenbruck 1997/2014, VanderKam 1984, Annus 2010, Halperin 1988, Bauckham 1983/1990/1993), ran lens-leakage check across all surface text, verified Aramaic onomastics against Milik 1976 4Q201/4Q202/4Q204, verified the layered-witness convention, verified the mid-ch-32 Greek→Ge'ez transition. **Zero revisions required.** All chapters advanced editor-review → reviewer-approved at v1.0.0-rc2.

---

## Cross-corpus reach achieved this pass

1. **First 4-tradition throne-vision wire** in the WoH glossary: Ezek 1 → Dan 7 → 1 En 14 → Shi'ur Qomah → Rev 1+4 (extending the existing 3-tradition wire). Anchored at `enoch-throne-vision-14-cross-corpus-ezek-1-dan-7-rev-4-shiur-qomah-four-tradition-wire`.
2. **6-tradition cosmic-mountain cluster**: Sinai/Horeb + Ṣapunu + Nimush/Ararat/Jūdī + Eden-mountain + Hermon + 1 Enoch 18+24-25 seven-mountains.
3. **Watcher canonical-engagement framework**: Watchers + Asael + Nephilim + Dudael/Azazel + giants-evil-spirits + Enoch-as-scribe — acknowledgment-without-endorsement, framework parallel to v2.65.0 Anunnaki/apkallū precedent.
4. **NT × 1 Enoch wire**: Jude 14-15 quotation + Jude 6 + 2 Pet 2:4 + Rev 6:9-10 + Rev 8:2 + Rev 22 + 12 NT *geenna* references.
5. **Enoch-Metatron tradition wire**: 1 En 12-13 → 3 Enoch Sefer Hekhalot, bidirectional with v2.59.0 `metatron-shar-ha-panim`.
6. **Sophia / Hokhmah fountainhead**: 1 En 32 tree-of-wisdom → Prov 8 + Wis Sol 7-9.

---

## Items requiring decision

**None.** No reviewer `flag-for-human` verdicts. No open Editor escalations. Three deferred-to-Reviewer decisions from the Editor report (Jude tense-shift at 1:9; Asael/Azazel onomastic transition; 300-vs-3000 cubits at 7:2) were all confirmed shipping as-is by the Reviewer.

---

## Editor escalation report (inlined)

See `ship-a-watchers-editor-report.md` in this directory for the full report. Key points already extracted above; principal sections:

- **Speculative entries requiring sign-off:** None.
- **Glossary changes:** 17 central new (all `direct`) + 17 extensions + 7 overlay (all `direct` composition-conventions).
- **Recommendation:** Advance to Reviewer stage. (Done; Reviewer approved.)

---

## Reviewer report (inlined highlights)

Full reviewer reports are appended in each chapter file under `translation.reviewerReport`. Aggregate findings:

- **Per-chapter verdicts:** 248 approve / 0 revise-suggested / 0 flag-for-human.
- **Glossary review:** 24 new entries (17 central + 7 overlay) approve; 0 downgrade; 0 revise; 0 flag-for-human.
- **Existing-entry extensions:** 17 extensions spot-checked across 7 entries (`chayyot`, `nephilim`, `adapa-apkallu`, `chanoch-vayithallech`, `b-nei-ha-elohim`, `shiur-qomah`, `metatron-shar-ha-panim`); all extensions correctly point at verses where the entry's lemma materially applies.
- **Lens-leakage:** zero verses flagged across all 248. Surface `i18n.en` reads as defensible scholarly translation mainstream-defensible against Nickelsburg 2001 + Black 1985 + Knibb 1978.
- **Aramaic onomastics:** preserved correctly per Milik 1976 4Q201/4Q202/4Q204.
- **Layered-witness convention:** spot-checked chs 1-2, 7-8, 17-19, 33-36; witness attribution correct per scholarly consensus.
- **Greek-to-Ge'ez transition at ch 32:6:** verified.
- **Deferred decisions:** all three confirmed shipping as-is.

---

## On sign-off

Confirming sign-off advances all 36 chapter files:
- `translation.status`: `reviewer-approved` → `stable`
- `translation.version`: `1.0.0-rc2` → `1.0.0`
- `translation.reviewer`: → `zarazinsfuss`
- `translation.reviewedAt`: → 2026-06-05 ISO timestamp

Then library page is committed to `data-content/library/book-of-enoch-woh.md`, catalog flipped to `verificationStatus: stable`, and bundle synced to api + www.

**Ship B (chapters 72-82, the Astronomical Book) remains a future ship** — DSS 4Q208-4Q212 are the oldest Enoch fragments overall (late 3rd c. BCE), and the DSS Astronomical Book is significantly longer than the Ge'ez. Separate ship.
