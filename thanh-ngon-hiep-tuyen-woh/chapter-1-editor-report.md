# Chapter 1 Editor Report

**Book:** Thánh Ngôn Hiệp Tuyển, Quyển Nhứt (Compilation of Divine Messages, Volume One), WoH-Translation (TNHT-WOH) — the Caodai séance canon of 1925–26
**Chapter:** 1 (the opening 10 dated messages, Noël 1925 → 24 Avril 1926; 111 paragraphs, TNHT-1:1…TNHT-1:111)
**Editor pass:** 2026-07 (claude-opus-4-8)
**Status at end of pass:** `editor-review` (advanced from `draft`; version `1.0.0-draft` → `1.0.0-rc1`)

---

## Summary

TNHT is **the pipeline's first Vietnamese source text** and its first
Latin-script (quốc ngữ) source, so several conventions established for the
Arabic and Hebrew sources do not apply and their absence is documented
rather than left implicit: there is **no transliteration layer** (the `vi`
field is self-transliterating), and the composition-specific decisions
instead concern rendering conventions, a large retain-vs-translate divine-name
and sacerdotal vocabulary, and a single-witness collation framework.

The pass (i) created a new per-book overlay glossary
(`thanh-ngon-hiep-tuyen-woh/_translation-glossary.json`, v1.0.0) with
**14 entries** (4 `direct`, 10 `inferred`, **0 `speculative` committed**);
(ii) resolved **all 17 editorial questions** into glossary entries,
commentary, and consensus readings; (iii) applied per-verse `notes.official`
commentary to **65 paragraphs**, leaving purely-logistical ceremony verses
empty per the commentary-discipline rule; (iv) made **3 authorized English
edits** (the Tam Kỳ Phổ Độ standardization, each backed by a glossary entry);
(v) recorded the single working witness and **8 retained cruxes** in a
collation entry and in per-verse commentary; (vi) added `glossaryRefs[]` to
**107 paragraphs**.

The surface English is a defensible independent scholarly rendering and does
**not** lift the existing English Caodai translations (daotam.info / Sydney
Centre for Studies in Caodaism). **No Wheel of Heaven / Raëlian vocabulary
was injected into any line**; the lens-resonance loci are escalated below as
wiki/article material, not translation-apparatus material.

**Counts after pass:**
- Overlay glossary: new file at **v1.0.0** — **14 entries** (4 `direct`, 10 `inferred`)
- **0 `speculative` entries committed**; **0 escalated as proposed glossary entries** (the lens loci are escalated as routing decisions, not as candidate entries — see below)
- **65 paragraphs with commentary**; **107 with `glossaryRefs[]`**
- **17 of 17 editorial questions resolved**; `editorial_questions[]` cleared to `[]`
- **3 authorized English edits** (all Amnesty standardization); no other `i18n.en` changed; no `vi` changed except the NFC/ETH→Đ normalization already in the source file

---

## The two decisions the reviewer must confirm by name

### 1. `Tam Kỳ Phổ Độ` → **"Third Universal Amnesty"** (committed; confirm)

**Entry:** `tam-ky-pho-do-third-universal-amnesty-tnht-woh` (`inferred`)
**Source:** *Tam-Kỳ Phổ-Độ* (三期普度), vv. 55, 73, 75
**Decision:** Standardized to **"Third Universal Amnesty"** (the project
standard — this book's `_meta` subtitle, the catalog, the site), superseding
the draft's "Third Universal Salvation." Three English edits made (vv. 55,
73, 75).
**Why not simply literal:** the plain lexical value of *Phổ-Độ* is "universal
deliverance / to ferry all beings across" (*Phổ* 普 "universal" + *Độ* 度 "to
ferry across, save"). "Amnesty" is **not** the etymology; it is the
established doctrinal rendering, grounded in the movement's own contemporaneous
French self-presentation (*la Grande Amnistie* / *la Troisième Amnistie de
Dieu*, Gobron 1949) — a general pardon granted to all souls in this third and
final epoch. The literal "deliverance/save" sense is preserved in commentary
**and in the surface text at v. 75**, where the séance dialogue itself parses
the two graphs (*Phổ* "to spread abroad," *Độ* "to save living beings") — that
etymological exposition must not be overwritten by the fixed name, so v. 75
reads "Third Universal Amnesty" for the title but keeps the literal gloss for
the component words.
**Recommendation:** **Ship "Third Universal Amnesty"** and standardize
project-wide. This reconciles the draft with the `_meta` subtitle as
instructed; the one residual judgement is whether the reviewer prefers the
name to track the doctrine ("Amnesty," recommended) or the etymology
("Universal Deliverance/Salvation").

### 2. Book voice — `Thầy` = **third-person "the Master"** (committed; confirm or swap)

**Entry:** `thay-divine-self-designation-voice-tnht-woh` (`inferred`)
**Decision:** *Thầy* rendered **"the Master"** (third-person self-designation)
throughout the teaching-prose; *Ta* (imperial "I") rendered **"I / Me"** in
the high poetic register — a **deliberate register contrast** the draft had
already begun and the pass ratifies. *con / các con* = "my child / my
children"; *Môn-đệ / đệ-tử* = "disciples."
**The tension:** in the Vietnamese kinship-pronoun system *Thầy* ("Master/
Teacher") is grammatically a **first-person** self-reference (the speaker
naming himself by role), so "the Master" is a stylistic, not referential,
choice. First-person ("I, your Master") is more natural to direct address;
third-person "the Master" preserves the pedagogical role-noun that Caodai
foregrounds in every clause and keeps the clean contrast with the imperial
*Ta*. Both are defensible; neither violates accuracy-before-lens (the referent
is unambiguous to a Vietnamese reader either way).
**Recommendation:** **Keep third-person "the Master"** for role-foregrounding
(recommended, and lower-risk since it preserves the draft). **But this is a
whole-book stylistic lever** — if the reviewer prefers readability, the entire
book can be swapped to first-person "I / your Master" by editing this one
glossary entry and re-running the voice pass. Flagging by name so the choice
is made explicitly, not by default.

---

## `speculative` / lens discipline — nothing committed; loci escalated for routing

Per the hard rule that the WoH lens lives in the apparatus, **not** the line,
and that interpretive identifications are `speculative` and must be escalated:

- **No Raëlian/Elohim vocabulary was injected into any surface line**, and
  **no comparative-identification entry was committed to the glossary.** The
  translation reads as a Caodai text in its own terms.
- Three genuine **lens-resonance loci** exist and a WoH reader will notice
  them; the Editor deliberately **did not** surface them in the text or the
  commentary as identifications:
  1. **The descending-teacher motif** — God "came down into the world to teach
     the Way" (v. 4 *xuống trần dạy Đạo*; cf. v. 110 "come in his own person to
     save").
  2. **The séance / "higher intelligence" frame** — a self-identifying higher
     intelligence dictating dated, numbered messages through a material writing
     apparatus (the whole *cơ bút* production).
  3. **The syncretic single-identity formula** (v. 69) — one God declaring
     himself the source behind Dīpaṃkara, Śākyamuni, Laozi, now named Cao Đài.
- **Recommendation:** route any WoH-comparative reading of these loci to the
  **wiki / an Explainer article**, cross-linked from the book, **never** into
  `i18n.en` or `notes.official`. The commentary at vv. 4, 69 renders the motifs
  in the text's own terms and stops there. If the reviewer wants a
  comparative note anywhere in the apparatus, that is a `speculative`,
  human-authored decision requiring explicit sign-off — it is **not** taken
  here.

This is the project's accountability surface for this text: the lens went
**nowhere** in the line or the apparatus, by design.

---

## Resolution of the 17 editorial questions

| # | Question (refIds) | Resolution |
|---|---|---|
| 1 | Divine-signature header, render-once (2,7,19,38,60,68,79,105) | **Resolved** → `divine-signature-header-tnht-woh` (`direct`). Rendered **in full and identically at each** occurrence (verse-keyed system may display paragraphs independently); explanatory **commentary written once** (v. 2), the other seven carry a one-line cross-ref. *Viết* = 曰 "styled"; *Cao Đài* retained. |
| 2 | `Thầy` voice + `con` (pervasive) | **Resolved + flagged** → `thay-divine-self-designation-voice-tnht-woh` (`inferred`). **Third-person "the Master"** for *Thầy*; **"I/Me"** for imperial *Ta*; "my child/children" for *con/các con*. First-person alternative flagged (decision #2 above). No English edits needed (draft already third-person). |
| 3 | Core divine names retain-vs-translate (2, …) | **Resolved** → `cao-dai-and-divine-names-tnht-woh` (`inferred`). Retain *Cao Đài* as proper name; translate *Ngọc-Hoàng Thượng-Đế* = "the Jade Emperor, the Supreme Being," *Ngọc Đế* = "the Jade Emperor," *Tiên Ông* = "the Immortal Elder," *Đức Chí Tôn* = "the Most High," *Đại-Từ-Phụ* = "the Great Merciful Father," *Bạch-Ngọc-Kinh* = "the White-Jade Capital." |
| 4 | **`Tam Kỳ Phổ Độ`** (55, 73, 75) | **Resolved (flagged, decision #1)** → `tam-ky-pho-do-third-universal-amnesty-tnht-woh` (`inferred`). **"Third Universal Amnesty."** 3 English edits. v. 75 keeps the literal *Phổ/Độ* exposition. |
| 5 | Séance apparatus `cơ / thủ cơ / chấp bút / phò cơ / phò loan / giáng cơ / cơ bút` (8, …) | **Resolved** → `seance-apparatus-co-but-tnht-woh` (`inferred`). Descriptive glosses + Vietnamese parenthesized; *cơ* = "planchette" (the *corbeille-à-bec* / *fuji* instrument); Western-spiritualist calques rejected. |
| 6 | `Chơn-Thần` / perisprit (11, 12, …) | **Resolved** → `chon-than-perisprit-tnht-woh` (`inferred`). **"True Spirit (Chơn-Thần)"** (literal 真神); the witness's own *périsprit* (Kardec) gloss preserved at v. 12; *phách* = "vital-body." |
| 7 | `Thần–Thánh–Tiên–Phật` hierarchy (13, 49, 50, 57, 107, …) | **Resolved** → `than-thanh-tien-phat-hierarchy-tnht-woh` (`inferred`). **Spirits – Saints – Immortals – Buddhas**; French-Caodai "génie" calque for *Thần* and "Angels" both rejected and recorded. *Ngũ chi* = the five Ways of Humanity/Spirits/Saints/Immortals/Buddhas. |
| 8 | Sacerdotal titles / Palaces (83, 111, …) | **Resolved** → `caodai-sacerdotal-hierarchy-tnht-woh` (`inferred`). Retain titles + bracket gloss: *Giáo-Tông* [Pope], *Đầu-Sư* [Cardinal], *Hộ-Pháp* [Defender of the Dharma], *Giáo-Hữu* [Priest]. The **v. 111 `Giáo-Hữu` crux** read as literal "religious brethren" (see cruxes). Palaces (Cửu Trùng / Hiệp Thiên / Bát Quái Đài) noted as implicit. |
| 9 | Acrostic (5, 39) | **Resolved** → commentary at vv. 5, 39. Plain-sense literal, names capitalized in situ, parenthetical preserved; flagged as only approximately coherent (words chosen for the names). Doubled reading impossible in English. |
| 10 | Poetry policy (3, 20, 21, 24, 29, 31, 34, …) | **Resolved** → `quoc-ngu-rendering-conventions-tnht-woh` (`direct`). Faithful-literal, one English line per source line, **no forced metre/rhyme** (Đường-luật tonal prosody uncarryable). |
| 11 | Classical Hán-Việt register (54, 69, 73, 85, 108) | **Resolved** → conventions entry (`direct`) + `han-viet-deity-and-loan-names-tnht-woh` (`direct`). Literal English with the romanized Hán-Việt bracketed; deity names given standard Sanskrit/Chinese forms. |
| 12 | Mantra (40) | **Resolved** → `han-viet-deity-and-loan-names-tnht-woh`. Retain *NAM-MÔ CAO-ĐÀI TIÊN-ÔNG ĐẠI-BỒ-TÁT MA-HA-TÁT* + bracketed gloss; *Nam-mô* = Skt *namaḥ*. Witness typo *Đ I*→*ĐẠI* handled (cruxes). |
| 13 | `Càn-Khôn` cosmology (15, 21, 46, 52, 109) | **Resolved** → `can-khon-cosmology-tnht-woh` (`inferred`). *Càn-Khôn* = "the Cosmos" where a totality (merism 乾坤); **unpacked** to "Heaven … Earth" at v. 108 where the trigrams are named singly. *Âm-Dương* = Yin-Yang; *Tinh-Khí-Thần* = Essence-Breath-Spirit; *Tam Bửu* = Three Treasures. |
| 14 | French date-lines (1, 6, 18, 44, 78, …) | **Resolved** → conventions entry (`direct`). English month-names for the French headers; Vietnamese lunar/sexagenary dates transliterated + glossed "[lunar]." |
| 15 | Witness typos / cruxes (26, 32, 40, 69/71-72, 92, +98, 111) | **Resolved** → `tnht-collation-witnesses-and-cruxes-tnht-woh` (`direct`) + per-verse commentary. `vi` verbatim; `en` renders intended reading; **all flagged pending a printed Tòa Thánh Tây Ninh witness.** (Six named + two added: v. 98 *Vi/vị Hộ-Pháp*, v. 111 *Giáo-Hữu*.) |
| 16 | `lạy` prostration + counts (45–52, …) | **Resolved** → `lay-prostration-and-counts-tnht-woh` (`inferred`). **"prostration"** (not "bow"/"kowtow"); counts 2/3/4/9/12 with the doctrinal rationale preserved (commentary vv. 45, 46, 49, 50, 52). |
| 17 | `Đạo` vs `-Giáo` (9, …) | **Resolved** → `dao-and-giao-the-way-and-religion-tnht-woh` (`inferred`). *Đạo* = **"the Way" uniformly** (religious sense kept by context, doubling deliberate); *Chánh-Giáo* = True Religion, *Thánh-Giáo* = Holy Teaching, *Phàm-Giáo* = Worldly Religion, *Đại-Đạo* = Great Way. |

All 17 `editorial_questions[]` cleared to `[]`.

---

## Authorized English edits (each backed by a glossary entry)

Per the hard rule that `i18n.en` may not change without a corresponding
glossary change, the **only** surface edits are the three Amnesty
standardizations (entry `tam-ky-pho-do-third-universal-amnesty-tnht-woh`):

- **v. 55** — "Third Universal Salvation (Tam-kỳ Phổ-độ)" → **"Third Universal Amnesty (Tam-Kỳ Phổ-Độ)"**
- **v. 73** — same
- **v. 75** — title → **"Third Universal Amnesty"**; "It is the Salvation of the third time" → **"It is the universal deliverance conferred for the third time"** (retaining the *Phổ/Độ* etymological exposition that follows)

No `vi` field was altered (the NFC + U+00D0→U+0110 normalization was already
applied in `source-vi-1.json`). The book-voice decision required **no** edits
(the draft was already third-person).

---

## Retained witness cruxes (all pending the second, printed witness)

Recorded in `tnht-collation-witnesses-and-cruxes-tnht-woh` and in per-verse
commentary. `vi` verbatim; `en` renders the intended reading; **none is
doctrinally load-bearing**, but all require a printed Tòa Thánh Tây Ninh
edition to confirm:

- (a) **v. 26** *tứ [riêng]* → *ý [riêng]* ("private mind"; probable homophone slip)
- (b) **v. 32** *Thiên-Điêu* → *Thiên-Điều* (天條, the Heavenly Law)
- (c) **v. 40** *Đ I-BỒ-TÁT* → *ĐẠI-BỒ-TÁT*
- (d) **v. 40** *mỗi gặt* — obscure; read "each [prostration/time]"
- (e) **v. 69 / vv. 71–72** *Mâu-Ni* vs *Mậu-Ni* — inconsistent spelling of Śākyamuni
- (f) **v. 92** *Xữ* → *Xử* (杵, "pestle"; the Giáng-Ma-Xử)
- (g) **v. 98** *Vi-Hộ Pháp* → *vị Hộ-Pháp* ("the Hộ-Pháp"; probable word-boundary slip) — **added by Editor**
- (h) **v. 111** *Đầu-Sư … nghĩa là Giáo-Hữu* — **semantic crux**, not a typo: read *Giáo-Hữu* as literal "religious brethren" (教友), not the rank "Priest," to avoid the anomaly of a Cardinal glossed by a lower rank. **This is the one crux where a printed witness could change the sense**; flagged for the reviewer. — **added by Editor**

---

## Glossary changes for review

### Central glossary
**No in-agent edits** (hard-rule compliance: the ~4 MB central production
glossary — Hebrew/Arabic only — was not loaded or modified). **No deferred
central action**: no Vietnamese lemma currently belongs in the central
glossary; all 14 entries are text-specific and correctly live in the overlay.
Promotion candidates (if the lemma recurs in future East-Asian-syncretic
texts): the `Thần–Thánh–Tiên–Phật` hierarchy and the `Càn-Khôn` cosmology.

### Per-translation overlay (new file, v1.0.0) — 14 entries

1. `quoc-ngu-rendering-conventions-tnht-woh` (`direct`) — no-translit, literal verse, Hán-Việt bracket-marking, French-date Englishing, NFC/ETH normalization
2. `divine-signature-header-tnht-woh` (`direct`) — render-in-full + comment-once
3. `thay-divine-self-designation-voice-tnht-woh` (`inferred`) — **book voice (decision #2)**
4. `cao-dai-and-divine-names-tnht-woh` (`inferred`)
5. `tam-ky-pho-do-third-universal-amnesty-tnht-woh` (`inferred`) — **Amnesty (decision #1)**
6. `seance-apparatus-co-but-tnht-woh` (`inferred`)
7. `chon-than-perisprit-tnht-woh` (`inferred`)
8. `than-thanh-tien-phat-hierarchy-tnht-woh` (`inferred`)
9. `caodai-sacerdotal-hierarchy-tnht-woh` (`inferred`)
10. `can-khon-cosmology-tnht-woh` (`inferred`)
11. `dao-and-giao-the-way-and-religion-tnht-woh` (`inferred`)
12. `lay-prostration-and-counts-tnht-woh` (`inferred`)
13. `han-viet-deity-and-loan-names-tnht-woh` (`direct`)
14. `tnht-collation-witnesses-and-cruxes-tnht-woh` (`direct`)

**Modified / promoted:** none (new file).

---

## Recommended next steps for the Reviewer

1. **Confirm decision #1** — "Third Universal Amnesty" (recommended) and
   authorize project-wide standardization against the `_meta` subtitle.
2. **Confirm or swap decision #2** — the book voice (third-person "the Master"
   recommended; first-person is a one-entry swap if readability is preferred).
3. **Confirm the lens discipline** — that the three resonance loci (vv. 4, 69,
   the *cơ bút* frame) stay **out** of the line and apparatus and are routed to
   wiki/article only. Nothing `speculative` is committed; confirm that is the
   intended posture for this text (it mirrors the Hidden Words ruling of
   keeping the lens neutral in the surface).
4. **Rule on the v. 111 `Giáo-Hữu` semantic crux** — accept the literal
   "religious brethren" reading, or hold for the printed witness.
5. **Commission the second witness** — a printed Tòa Thánh Tây Ninh edition of
   Volume One, to clear the 8 retained cruxes. Per
   strategy-library-acquisition.md this text is on a **single electronic
   witness** (daotam.info); it should **not** be signed off as textually
   verified until the second witness is collated.
6. **Confirm structural validation** — 111 paragraphs; all `glossaryRefs`
   resolve to real overlay entries (verified: 0 unresolved); commentary on the
   65 divergent paragraphs, empty on the purely-logistical ceremony verses;
   `editorial_questions[]` cleared.

After Reviewer sign-off (including explicit rulings on decisions #1 and #2 by
name and the lens-routing posture), the chapter advances from `editor-review`
to `reviewer-approved`, then to `published` after human sign-off.
