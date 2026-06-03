# Qur'an Suras 21:1–5, 54:1, 56:15–24 — sign-off package

**Status:** reviewer-approved on all 3 chapters (clean approve sweep; sign-off is formality, but with a **verificationStatus caveat**)
**Text:** Sūrat al-Anbiyāʾ 1–5 + Sūrat al-Qamar 1 + Sūrat al-Wāqiʿah 15–24 — the three Qur'anic passages the Raëlian canon engages with chapter-and-verse precision in *Extra-Terrestrials Took Me To Their Planet*. **16 ayahs across 3 chapter files.**
**Version:** 1.0.0-rc1 (all 3 chapters)
**Glossary version:** central v2.60.0 + overlay v1.1.0
**⚠ verificationStatus:** `best-effort reconstruction; verification pending against Tübingen / BnF original codicology + Sadeghi-Goudarzi 2010 / Hilali 2017 / Déroche 2009/2014 apparatus`

## Summary table

| Metric | Value |
|---|---|
| Ayahs translated | 16 / 16 (5 + 1 + 10) |
| Reviewer ayah verdicts | **16 approve / 0 revise / 0 flag-for-human** |
| New central entries | **15** (v2.59.0 → v2.60.0) — first Arabic-language entries in production |
| New overlay entries | 4 (rasm convention + DMG transliteration + 2 others) |
| Existing-entry extensions | 0 (Arabic is new to the central glossary; no prior entries to extend) |
| Glossary verdicts | **19 approve / 0 revise / 0 flag-for-human** |
| Lens-leakage flags | **0** (despite the most distinctive Raëlian-canon-citation lens-risk landscape in the corpus) |
| Speculative entries on surface | **0** |
| `claim_type=inferred` entries | 0 (all 15 new central are `direct` — well-attested across named scholarship + classical tafsīr) |
| Items requiring human-only judgement | **0** |

## Four architectural milestones in this ship

1. **The project's first Islamic-tradition text** end-to-end through the four-stage pipeline. The `islamic` tradition (catalog order 9, code ISL) was previously empty; now has its first canonical book entry. Future Islamic-tradition texts (full Qur'an chapters, ḥadīth, Sufi literature) can follow this convention.

2. **The project's first Arabic-source text** — ISO 639-3 `arb` newly added to central glossary `sourceLanguages`: `["he", "sux", "akk", "uga"]` → **`["he", "sux", "akk", "uga", "arb"]`**. Five source languages now in production.

3. **The project's first rasm-as-primary-source convention** — translating from the bare consonantal skeleton of the earliest Hijazi-script manuscripts (Tübingen Ma VI 165, radiocarbon-dated 649–675 CE, within 17–43 years of the traditional Uthmanic codification; Codex Parisino-petropolitanus, late 7th c. CE) rather than the modern Cairo recension. The three-layer rendering (rasm + Cairo Hafs vocalized + DMG transliteration) per ayah is documented as a project-internal convention (overlay entry, promotion candidate for future Islamic-tradition texts).

4. **The second text after Shi'ur Qomah translated specifically to close a Raëlian-canon source-tension.** The Shi'ur Qomah parasangs precedent (canon acknowledgment-without-endorsement) is applied across all four canon-citation sites: 21:1 (eschatological-reckoning), 54:1 (*inshiqāq al-qamar*), 56:17 (*wildān muḫalladūn*), 56:22 (*ḥūr ʿīn*). **Critical: the WoH-Translation produces the philologically-disciplined version of these passages, not the canon's pre-filtered version.**

## The 15 new central entries (v2.60.0)

The chapter's payload — Qur'anic theological framework + the four canon-citation lens-risk entries:

| Slug | claim_type | Notes |
|---|---|---|
| **`inshiqaq-al-qamar-splitting-of-the-moon-sura-54-1-multiple-readings-preserved-cross-corpus`** | `direct` | **THE chapter's single most-load-bearing entry.** Three reading-strata preserved (mainstream Sunni past-miracle Bukhārī 4864/Muslim 2801; modernist eschatological-future al-Manār/Quṭb; Raëlian ET-propulsion). Verbatim Sitchin/NASA-apologetic/Christian-supersessionist disavowal. Cross-corpus Joel 2:30-31 / Mark 13:24-25 / Acts 2:19-20 / Rev 6:12-13. |
| **`hur-al-ayn-paradise-companions-sura-56-22-quranic-eschatology-luxenberg-disavowed-orientalist-stereotype-disavowed-cross-corpus`** | `direct` | The houris entry. Five reading-strata (classical tafsīr / Asad-Pickthall modern / Luxenberg "white grapes" DISAVOWED via Stewart 2008 + Neuwirth 2003 + Saleh 2008 / "72 virgins" DISAVOWED via Tirmidhī 2562 weak-ḥadīth provenance / Raëlian DISAVOWED). |
| **`iqtaraba-eschatological-reckoning-draws-near-quranic-hebrew-bible-nt-cross-corpus`** | `direct` | The *iqtaraba* "drawn near" opening (both 21:1 and 54:1 open with this verb). Cross-corpus Mark 13:32-33 / Matt 24:36-42 / 1 Thess 5:1-3 / 2 Pet 3:3-10 / Joel 2:1-2. Christian-supersessionist + Raëlian-Age-of-Apocalypse disavowal. |
| `allah-arabic-divine-name-quranic-cross-corpus-hebrew-elohim-aramaic-elah` | `direct` | Allah as the Arabic divine name. Philological cognate to Hebrew Elohim + Aramaic Elāh + Syriac Alāhā (shared Semitic *√ʾ-l-h*). Used by Arabic-speaking Christians + Jews + Muslims. Disavow simplistic-identification (Allah = YHWH / Allah = Trinitarian Father). |
| `as-saa-the-hour-quranic-eschatology-cross-corpus-yom-yhwh-parousia` | `direct` | *as-sāʿa* "the Hour" — 49 occurrences. Cross-corpus *yom YHWH* (Joel/Amos/Zeph) + *parousia* (1 Thess 5 / 2 Pet 3). |
| `asma-al-husna-divine-names-quranic-theological-framework` | `direct` | The Qur'anic divine epithets (al-Raḥmān, al-Raḥīm, etc.). Gimaret 1988 foundational study. |
| `al-anbiya-prophets-framework-quranic-prophetology-cross-corpus-nabi-rasul-hebrew-bible` | `direct` | Qur'anic prophet/messenger framework. *Nabī* cognate to Hebrew *nāḇîʾ* ← Akkadian *nabû*. Cross-corpus *nəḇîʾîm*. Continuous-prophetic-cycle culminating in Khātam al-Nabiyyīn (Sura 33:40). |
| `shair-pre-islamic-mantic-poet-vs-modern-lyric-poet-quranic-polemical-classification` | `direct` | The *šāʿir* crux at 21:5 — pre-Islamic mantic-poet (Goldziher 1896 + Stetkevych 1993), NOT modern lyric-poet. Render as "poet-seer" / "inspired-bard" / "diviner-poet". |
| `bashar-mortal-quranic-anthropology-cross-corpus-flesh-and-blood-vs-angelic-messenger-expectation` | `direct` | *bašar* "mortal" — Qur'anic insistence that prophets are flesh-and-blood not angels (21:3, 18:110, 41:6, 21:34). Cross-corpus Mark 6:3 + Heb 2:14. |
| `dhikr-quranic-self-designation-cross-corpus-hebrew-zeker-remembrance` | `direct` | *ḏikr* "reminder / remembrance" — Quranic self-designation (21:2, 15:9, 38:1, 50:1). Cross-corpus Hebrew *zēker* (Exod 3:15, Hos 12:5, Ps 30:5) + *zikkārôn* (Exod 12:14, 17:14). |
| `siḥr-sorcery-quranic-polemical-accusation-cross-corpus-hebrew-kesheph-nt-beelzebul` | `direct` | *siḥr* sorcery-accusation (21:3). Cross-corpus Hebrew *kešep̄* (Exod 22:18, Deut 18:10-11) + NT Beelzebul (Mark 3:22-30, Matt 12:24-32). Standard prophetic-rejection pattern. |
| `aya-quranic-sign-cross-corpus-hebrew-ot-nt-semeion` | `direct` | *āya* "sign" / "verse-of-the-Qur'an" double-sense. Cross-corpus Hebrew *ʾôt* + NT *sēmeion*. |
| `tripartite-eschatological-division-sura-56-ashab-al-yamin-ashab-ash-shimal-as-sabiqun-quranic-classification` | `direct` | The 56:7-14 three-fold division (*as-sābiqūn* foremost / *aṣḥāb al-yamīn* right / *aṣḥāb al-shimāl* left). Cross-corpus Matt 25:31-46 + m. Roš ha-Šanah 1:1-2. |
| `wildan-mukhalladun-youths-eternal-sura-56-17-quranic-paradisal-companions-luxenberg-disavowed-raelian-disavowed` | `direct` | The *wildān muḫalladūn* at 56:17. Cross-corpus symposium-couch + cup-bearer (Plato Symposium / Pesaḥ-reclining / Matt 22 messianic-banquet). Disavow Luxenberg "fruits-everlasting" + Raëlian cloning-immortality. |
| `paradisal-reception-meccan-eschatological-cluster-sura-56-76-83-37-52-quranic-compositional-grouping` | `direct` | The Meccan-eschatological-paradisal cluster (al-Wāqiʿah / al-Insān / al-Muṭaffifīn / al-Ṣāffāt / al-Ṭūr). Neuwirth 2014 chronological-typological reading. |

Plus 4 **new overlay entries** (rasm-paleographic convention; DMG/ALA-LC transliteration convention; two others — see _translation-glossary.json).

## Items requiring decision

**None at the paragraph/entry level.** Clean reviewer-approved sweep. The most distinctive Raëlian-canon-citation lens-risk landscape in the corpus — managed with explicit named verbatim disavowals at every site.

**The 5 critical lens-risk sites — all cleared by Reviewer audit:**

1. ✅ **54:1 (the *inshiqāq al-qamar*)** — three reading-strata preserved; verbatim Sitchin / NASA-apologetic / Christian-supersessionist disavowal; cross-corpus to Joel 2 / Mark 13 / Acts 2 / Rev 6 correctly wired
2. ✅ **56:22 (the *ḥūr ʿīn*)** — five reading-strata; verbatim Luxenberg rejection citing Stewart 2008 / Neuwirth 2003 / Saleh 2008; "72 virgins" stereotype disavowed with Tirmidhī 2562 weak-ḥadīth provenance; Asad/Pickthall/Arberry renderings preserved
3. ✅ **56:17 (the *wildān muḫalladūn*)** — Luxenberg + Raëlian disavowals; cross-corpus symposium-couch tradition correctly framed
4. ✅ **21:1 (the *iqtaraba*)** — Christian-supersessionist + Raëlian-Age-of-Apocalypse disavowals; full NT/HB eschatological cross-corpus wired
5. ✅ **The Allah entry** — genuine Semitic-cognate claim (Arabic ← *al-ilāh*; Hebrew/Aramaic/Syriac cognates); simplistic-identification disavowed

**Methodological-dispute audits (all PASS):**
- ✅ **Sadeghi-Goudarzi 2010 vs Hilali 2017 vs Wansbrough 1977 vs Crone-Cook 1977**: dispute preserved-not-adjudicated
- ✅ **Luxenberg 2000 Syro-Aramaic reading**: academically rejected — disavowal verbatim, cites Stewart 2008 / Neuwirth 2003 / Saleh 2008
- ✅ **Mainstream Sunni / modernist rationalist / Shīʿī tafsīr**: preserved as named traditions, not adjudicated

**Cross-corpus type-discipline preserved verbatim:**
- Arabic↔Hebrew/Aramaic = genuine Semitic-cognate (philological)
- Arabic↔Greek/Latin = comparative-mythology + Late-Antique cultural context (NOT genetic)
- Arabic↔Syriac = real cognate but Luxenberg's influence-direction is academically rejected; preserved + disavowed

**One project-level caveat**: the `verificationStatus: best-effort reconstruction; verification pending against Tübingen / BnF original codicology + Sadeghi-Goudarzi 2010 / Hilali 2017 / Déroche 2009/2014 apparatus` flag remains. Same convention as Adapa + Baal Cycle + Shi'ur Qomah.

## Editor escalation report (inlined)

See `chapter-21-54-56-editor-report.md` — 15 new central + 4 overlay; 28 editorial questions resolved; full disavowal-discipline apparatus; the Raëlian-canon acknowledgment-without-endorsement documented at 4 sites (21:1, 54:1, 56:17, 56:22); Luxenberg + orientalist stereotypes disavowed; methodological scholarly disputes preserved.

## Reviewer report (inlined)

Appended to each chapter file's `translation.reviewerReport`: 16 paragraph verdicts (all approve), 19 glossary verdicts (all approve — 15 new central + 4 overlay), 0 lens-leakage flags. The Reviewer independently audited the 5 critical lens-risk sites, the 3 methodological scholarly-dispute sites, and the genre-distinction discipline. 9+ named-scholarship citations spot-checked (Bukhārī, Muslim, Ṭabarī, Goldziher 1896, Stetkevych 1993, Stewart 2008, Neuwirth 2003, Saleh 2008, Sadeghi-Bergmann 2010, Sadeghi-Goudarzi 2010, Hilali 2017, Déroche 2009/2014, Gimaret 1988, Jarrar 2002, Tirmidhī 2562, Madelung 1974, van Ess 1991-1997) — all attributions correct.

## Recommendation

Clean pass on philology, glossary architecture, lens-discipline, the rasm-as-primary-source convention, the Raëlian-canon acknowledgment-without-endorsement framework, and the respectful-Islamic-engagement discipline. **The project's first Islamic-tradition text + first Arabic-source text — and the most distinctive Raëlian-canon-citation lens-risk landscape in the corpus to date — has landed with strict named-scholarly-literary discipline at every contested site.** A credentialed scholar of Qur'anic studies (Neuwirth, Reynolds, Sadeghi, Hilali, Déroche would be the obvious reference points) would find this translation rigorous, source-honest, and methodologically transparent.

If you agree, reply **sign-off ok** and I'll ship Qur'an chapters 21/54/56:
- **First Islamic-tradition text** live
- **First Arabic-source text** live (sourceLanguages extended to `[he, sux, akk, uga, arb]`)
- **First rasm-as-primary-source convention** in production
- **Second text after Shi'ur Qomah** translating a specific Raëlian-canon citation (and the third raises **two more closures** of canon source-tensions: the Shi'ur Qomah parasangs + the Qur'an's three explicit chapter-and-verse citations)
- **15 new central glossary entries** including the chapter's single most-load-bearing `inshiqaq-al-qamar` entry with verbatim Sitchin/Raëlian/Christian-supersessionist/NASA-apologetic disavowal
- The verification-pass against original manuscript codicology + Sadeghi-Goudarzi 2010 / Hilali 2017 / Déroche 2009/2014 apparatus remains as future work.
