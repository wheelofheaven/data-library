# Ship A (Jubilees 1-12) — Sign-off Package

**Status:** `reviewer-approved` — ready for human sign-off.
**Version:** `1.0.0-rc2` across all 12 chapters.
**Editorial pass:** `2026-06`.
**Glossary versions:** central `v2.68.0`; overlay `v1.1.0`.

---

## Summary table

| Metric | Count |
|---|---|
| Chapters translated | 12 |
| Verses translated | 373 |
| Editorial questions raised by Translator | 165 |
| Editorial questions resolved by Editor | 165 (100%) |
| New central glossary entries | 12 (all `claim_type=direct`) |
| Existing central glossary extensions | 10 |
| New per-translation overlay entries | 7 |
| Verses with per-verse commentary | 30 |
| Glossary refs applied to chapter verses | 95 |
| Reviewer verdicts: approve | 373 (100%) |
| Reviewer verdicts: revise-suggested | 0 |
| Reviewer verdicts: flag-for-human | 0 |
| Lens-leakage flags | 0 |
| Speculative entries pending sign-off | 0 |

---

## What was done

**Translator** drafted English at ASV/RSV-baseline register for 12 chapters / 373 verses (across two batches: chs 1-7 + 3-7 resume after socket-crash + chs 8-12). Three-layer witness convention: Hebrew DSS (4Q216/4Q218/11Q12 primary where preserved); Greek patristic (Epiphanius De mensuris et ponderibus at chs 8-9); Ge'ez (VanderKam 1989 + Charles 1902 PD) tertiary/fallback. 165 editorial questions flagged.

**Editor** resolved all 165 questions, added 12 new central entries (`claim_type=direct`) + 10 existing-entry extensions + 7 overlay entries, drafted commentary on 30 high-priority verses, applied 95 glossary refs across chapters, bumped central v2.67.0 → **v2.68.0** and overlay v1.0.0 → **v1.1.0**. (Editor work performed via direct Python scripting after three woh-editor agent socket-crashes — the 4.4MB central glossary exceeded the agent's effective Read+Edit budget.)

**Reviewer** independently verified all 373 verses against sources, verified all 12 new central entries against named scholarship (VanderKam 1989 + 2018 Hermeneia, Milik-VanderKam 1994 DJD XIII, Charles 1902 PD, Kugel 2012, Segal 2007, García Martínez 1997, Najman 1999, Beckwith 1996, Glessmer 1999, VanderKam 1998, van Ruiten 2000, Reed 2005, Stuckenbruck 2014, Orlov 2005, Schaefer 2009), ran lens-leakage check across all 373 verses (programmatic scan for 14 trigger terms across all 12 chapters — zero hits), verified Hebrew DSS witness handling against Milik-VanderKam DJD XIII apparatus, verified Greek Epiphanius witness handling per Dean 1935, verified calendrical claims preserved without harmonization, confirmed all 5 deferred Editor decisions. **Zero revisions required.** All chapters advanced editor-review → reviewer-approved at v1.0.0-rc2.

---

## Cross-corpus reach achieved this pass

1. **Mastema as the earliest extant Satan-figure** — Jub 10:8 establishes Mastema as prince-of-the-spirits; bidirectional to CD 16:5 + 1QS 3:18-25 + 1QM 13:11 + Test. Levi 19; foundational text for Satan-figure development in 2nd Temple Judaism.

2. **Heavenly tablets densest extant articulation** — Jub deploys the motif 25+ times; extends v2.67.0 1 Enoch entry to make Jubilees the foundational text; bidirectional to 1 En 81/93/103 + Dan 7:10 + Rev 5:1 + Rev 20:12.

3. **Enoch-as-scribe foundation** — Jub 4:17-26 is the EARLIEST extant text systematizing Enoch-as-celestial-scribe + first-writer-of-humanity; bidirectional to v2.66.0 Enoch-Metatron entry + v2.59.0 metatron-shar-ha-panim Hekhalot entry.

4. **364-day calendar polemic foundation** — Jub 6:32-38 is the foundational polemical articulation (1 En 72-82 is the technical-astronomical implementation); CD 16:2-3 identifies Jubilees as calendrical authority; bidirectional to Qumran 4Q319-4Q330 Mishmarot + 4Q252 + 4QMMT.

5. **Abraham-iconoclasm-fire trans-Abrahamic tradition** — Jub 12:12-14 is the EARLIEST extant text of the Abraham-burns-idols + Haran-dies-in-fire tradition; bidirectional to Apoc. Abraham 1-8 + Genesis Rabbah 38:13 + b. Bava Batra 91a + Qur'an Sura 21:51-71 + Sura 37:83-98 + Sura 6:74-79 + Sura 19:41-50. Spans Jewish + Christian + Islamic Abrahamic-traditions.

6. **Three-holy-mountains omphalos extension** — Jub 8:19 (Zion + Sinai + Mt-of-the-East / Eden-mountain) extends the existing 7-tradition cosmic-mountain cluster (1 Enoch Ship A+B + Genesis + Exodus + Ugaritic).

7. **Giants-become-evil-spirits demonology foundation** — Jub 10:1-6 + 1 En 15:8-12 bidirectional; the more-detailed Jubilees version adds Mastema bargain + Noah's intercession + medicinal-book + 9/10 demon binding.

8. **Hebrew-as-creation-language tradition** — Jub 12:25-26 is the EARLIEST extant text for the tradition that Hebrew was the language of creation, forgotten at Babel, recovered through Abram; bidirectional to b. Sanhedrin 38b + Genesis Rabbah 18:4 + Jerome Ep. 18 + Augustine City of God 16:11.

9. **Tower-of-Babel wind-overthrow tradition** — Jub 10:21 is the earliest specific wind-overthrow detail; bidirectional to Pseudo-Philo Bib. Ant. 7:5 + Sibylline Oracles 3:97-109 + 3 Baruch 3:7-8 + b. Sanhedrin 109a.

10. **Sefer Refuot / Noah's medicinal book** — Jub 10:10-14 is the foundational text for the antediluvian-medicinal-book tradition; bidirectional to b. Pesachim 56a (Hezekiah's hiding) + Aramaic Levi 51-57 + Mesopotamian apkallū knowledge-transmission framework.

---

## The 5 deferred-to-Reviewer decisions

All five confirmed shipping as-is:

1. **Jub 1:1 verse-numbering**: VanderKam 1989 convention preserved (standard for modern critical scholarship).
2. **Mastema vs Beliar at Jub 1:20**: principal Ge'ez Bēlhārā reading "Beliar" preserved without harmonization.
3. **Jub 7:22 tripartite-giants** (Naphidim + Nephilim + Elyo): VanderKam 1989 reconstruction preserved.
4. **Jub 8:19 Mt-of-the-East identification**: ambiguity preserved in apparatus (three competing identifications — van Ruiten 2000 Eden-mountain; 1 En 24-25 eastern paradise; unnamed third peak).
5. **Jub 10:8-9 1/10 bargain**: bargain-narrative voice preserved; no harmonization with later cosmic-dualist Mastema-figure tradition.

---

## Items requiring decision

**None.** No reviewer `flag-for-human` verdicts. No open Editor escalations. Zero speculative-claim entries.

---

## On sign-off

Confirming sign-off advances all 12 chapter files:
- `translation.status`: `reviewer-approved` → `stable`
- `translation.version`: `1.0.0-rc2` → `1.0.0`
- `translation.reviewer`: → `zarazinsfuss`
- `translation.reviewedAt`: → 2026-06-06 ISO timestamp

Then library page is committed to `data-content/library/jubilees-woh.md` (separate slug from the existing imported-English `book-of-jubilees`), catalog flipped to `verificationStatus: stable`, bundle synced to www.

With Ship A done, **Jubilees + 1 Enoch together form the principal Second Temple Jewish apocalyptic-corpus framework in production**. The 47 1 Enoch Watchers+Astronomical chapters + the 12 Jubilees primeval+patriarchal chapters cover the foundational textual layer for the Qumran-Enochic-Jubilees-circle reception.

**Ship B (Jubilees 13-50, the patriarchal narrative through Moses and Sinai)** remains as a potential future ship. The patriarchal-narrative material (Abraham through Joseph through Moses) has lower density of original mythology + cross-corpus cross-wires than Ship A, but contains: the binding of Isaac through Mastema (Jub 17-18); Jacob's Bethel theophany (Jub 27); the Levi-priesthood etiology (Jub 30-32); Joseph (Jub 39-46); Moses + the Exodus + Sinai (Jub 47-50). Estimated scope: ~38 chapters, ~900+ verses — significantly larger than Ship A.
