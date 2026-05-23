# Chapter 16 Editor Report

Chapter: Genesis 16 — Hagar, Ishmael, and the messenger of YHWH.

Translation version advanced `1.0.0-draft` → `1.0.0-rc1`. Status
advanced `draft` → `editor-review`. Glossary pin advanced `2.12.0` →
`2.13.0`.

All eight editorial questions from the Translator's pass were
resolved into glossary entries; none required escalation. No
`claim_type=speculative` entries were created in this pass. The
chapter is glossary-stable pending Reviewer pass and human sign-off.

The Reviewer's attention is directed below to four entries that
warrant particularly careful audit, all `claim_type=direct` but with
specific load-bearing positions — most notably the
`malakh-yhwh-messenger` entry, the chapter's and the corpus's
highest-lens-leverage call to date.

## Speculative entries requiring sign-off

None. All 8 entries added in this pass are `claim_type=direct`. The
chapter's high-lens-leverage moment (the first occurrence of *mal'akh
YHWH* at v 7) is handled by a direct entry whose load is in the
apparatus and whose translation choice (*messenger of YHWH* over
ASV's *angel of Jehovah*) is editorially neutral on the
messenger-identity scholarly question.

## Glossary changes for review

### Central glossary additions (v2.13.0)

All eight entries below were added to the central glossary
(`data-content/i18n/translation-glossary.json`). The per-translation
overlay (`data-library/genesis-woh/_translation-glossary.json`) was
not created; all entries are cross-corpus by design (the messenger
figure, the substitute-wife institution, the *chamas* register, the
doubled-infinitive intensive, the name-etymology pattern, the
seeing-God-and-living formula, and the well-naming pattern all recur
outside Genesis).

- Added: `shifchah-substitute-wife-arrangement` (claim_type:
  `direct`) — the ANE substitute-wife legal institution at Gen 16:1-8
  with cross-corpus forward-apply to the Bilhah and Zilpah narratives
  of Gen 30:3-13. See **Reviewer attention** below.
- Added: `chamas-forensic-curse-formula` (claim_type: `direct`) —
  Sarai's v 5 *chamasi alekha* paired with *yishpot YHWH beyni
  u-veynekha*, the formal legal speech-act; cross-corpus
  forward-apply to Gen 31:53, Judg 11:27, 1 Sam 24:13, 24:16, and the
  wider prophetic-indictment corpus.
- Added: `malakh-yhwh-messenger` (claim_type: `direct`) — the first
  occurrence of the messenger-of-YHWH figure at Gen 16:7, with the
  three modern critical positions on messenger-identity presented in
  parallel; `appliesTo` populated with 60+ cross-corpus occurrences
  across the patriarchal narratives, Exodus, Numbers, Joshua, Judges,
  Samuel-Kings, Isaiah, Zechariah, and Psalms. **See Reviewer
  attention below — this is the chapter's load-bearing call.**
- Added: `harbah-arbeh-doubled-infinitive-intensive` (claim_type:
  `direct`) — the Hebrew doubled-infinitive-absolute intensifying
  construction at v 10, with corpus-wide distribution. The
  Gesenius-Kautzsch-Cowley / Joüon-Muraoka / Waltke-O'Connor
  treatments are cited; the Hagar-promise's structurally distinctive
  position as the only seed-multiplication formula in Genesis
  addressed to a non-Israelite woman is documented.
- Added: `yishmael-name-etymology` (claim_type: `direct`) — the first
  in-text patriarchal name-etymology in the Hebrew Bible, with the
  cross-corpus pattern (Yitzchaq, Esav, Ya'aqov, Yosef, Re'uven,
  Shim'on, Yehuda) documented and the Knauf 1989 *Ismael*
  North-Arabian-tribal historical reconstruction included as direct
  documentary background.
- Added: `pere-adam-wild-ass-prophecy` (claim_type: `direct`) — the
  hapax compound at v 12, with the Westermann/Sarna/Wenham/Hamilton
  modern critical wilderness-pastoralist mode-of-life reading
  endorsed and the Islamic reception and Orientalist racializing
  reception explicitly framed. **See Reviewer attention below —
  careful editorial framing required.**
- Added: `el-roi-and-halom-elohim-variant` (claim_type: `direct`) —
  the v 13 divine-name *El Ro'i* (first divine-name-naming by a woman
  in the Hebrew Bible) and the MT *halom* / LXX-emended *Elohim*
  textual variant; the WoH translation preserves the MT consistent
  with established practice. **See Reviewer attention below.**
- Added: `beer-lachai-roi` (claim_type: `direct`) — the well-name at
  v 14, with cross-corpus recurrence at Gen 24:62 and 25:11
  (Isaac's residence at the Hagar-encounter site) and the patriarchal
  well-naming pattern documented.

### Central glossary modifications

None. No existing entries were modified in this pass. The
pre-existing `shachat-chamas` entry (chapter 6 only) is retained at
its narrower antediluvian scope; the new
`chamas-forensic-curse-formula` entry runs alongside it covering the
forensic-speech-act register. The pre-existing
`patriarchal-seed-comparison-triad` entry is retained at its
dust/stars/sand-comparison scope; the new
`harbah-arbeh-doubled-infinitive-intensive` entry runs alongside it
covering the intensifying syntactic construction.

### Per-translation overlay

Not created. All 8 entries are cross-corpus by design.

### Version bump

Glossary version `2.12.0` → `2.13.0`. Semver-minor (additions only,
no modifications). `scopeNote` extended with a v2.13.0 paragraph
summarizing the 8 entries and the chapter's lens-leverage points.
Chapter-16 `translation.glossaryVersion` pinned to `2.13.0`.

## Reviewer attention

### 1. `malakh-yhwh-messenger` (vv 7, 9, 10, 11) — the chapter's highest-lens-leverage entry

This is the load-bearing call of the chapter and one of the highest-
lens-leverage entries in the WoH Genesis project to date. The figure
recurs across the patriarchal cycle, the Exodus, the wilderness
narratives, Joshua, Judges, the Samuel-Kings cycle, the prophetic
corpus, and the Psalter — and the messenger-identity question is
genuinely contested in modern critical scholarship. The translation
choice *messenger of YHWH* (over ASV's *angel of Jehovah*) is
editorially significant.

The Reviewer should verify that:

- All three modern critical positions on the messenger-identity
  question are presented in the entry and in the v 7 commentary
  *in parallel* and *with no preemption*:
  - **Position (a) — distinct created envoy** (Heidt 1949; classic
    Christian-tradition reading; supported by passages where the
    *mal'akh* is distinguished from YHWH, e.g. Zech 1:11-12, 1 Kgs
    19:7).
  - **Position (b) — the *mal'akh* IS YHWH (the identity reading)**
    (Westermann 1985, von Rad 1972; supported by first-person speech
    AS YHWH at Gen 16:10, 22:12; recipient identification at Gen
    16:13, Judg 6:22-23, Judg 13:22; narrative interchange at Gen
    22:11/15, Exod 3:2/4).
  - **Position (c) — literary-theological device** (Hamori 2008,
    Sommer 2009, MacDonald 2009; the *mal'akh YHWH* as a device
    allowing YHWH to appear without theophanic risk).
- **No project-specific synthesis appears in the entry.** The entry
  is held to strict accuracy-above-lens discipline. The chapter
  commentary at v 7 explicitly states that *the WoH translation
  commits to none of the three positions* and reserves project-
  specific synthesis for *the wiki and long-form material
  downstream*. The Reviewer should confirm this is genuine and not
  merely formal.
- The translation choice *messenger of YHWH* (Hebrew-literal,
  pre-developed-angelology) is endorsed at the philological level
  and is editorially neutral on the messenger-identity question.
  The conventional *angel of the LORD* both imports later angelology
  (Greek *angelos* / Latin *angelus* as a class of created spiritual
  being) and tilts toward position (a).
- The note on the post-exilic developed angelology (Daniel's Gabriel
  and Michael, the named-angels of 1 Enoch, Tobit's Raphael, the
  Qumran corpus) is present and correctly flags the post-exilic
  developed class as a distinct stratum that the patriarchal
  *mal'akh YHWH* should not be read forward through.
- The `appliesTo[]` array's 60+ cross-corpus occurrences are
  accurate. The Reviewer is encouraged to spot-check at least the
  named-encounter clusters (Gideon at Judg 6:11-22, Manoah at Judg
  13:3-21, Balaam at Num 22:22-35, and the Zech 1-3 visions).

This is the chapter's most important Reviewer check. The Hebrew is
faithfully rendered; the apparatus carries the scholarly question
without preempting it; project-specific WoH synthesis is reserved
for downstream materials.

### 2. `pere-adam-wild-ass-prophecy` (v 12) — careful editorial framing

The verse has a heavy downstream reception history that the entry
must navigate carefully. The Reviewer should verify that:

- The Hebrew-philological reading is presented first and is the
  primary content of the entry. The wilderness-pastoralist mode-of-
  life reading (Westermann/Sarna/Wenham/Hamilton consensus) is
  explicitly endorsed; the *pere* lexeme's biblical distribution
  (Job 39:5-8, Jer 2:24, Hos 8:9, etc.) is documented as the basis
  for the positive *wild, free, untamed, of the wilderness* register.
- The Islamic reception (Quran Sura 14:39, 19:54-55, 2:125-129;
  early-Islamic tafsir tradition; Ishmael as ancestor of the Arabs)
  is flagged and presented as a *positive desert-freedom* reception
  of the Hebrew text — not preempted, not endorsed as the canonical
  reading, but accurately described as the Islamic-traditional
  reception.
- Genesis Rabbah on Ishmael (Gen Rab 45:9-11, 53:11, 71:9) is named
  to flag that the rabbinic tradition is not monolithic.
- **The 19th-20th century Orientalist racializing reception is
  explicitly named and explicitly rejected as not supported by the
  Hebrew.** Said *Orientalism* (1978) is cited as the standard
  scholarly critique. The Reviewer should specifically check that
  the entry does not ship implicit racialization or Islamophobic
  framing — the Ishmael oracle is the ancestor-oracle of a
  historical pastoralist tribal confederation, not a divine sanction
  of any modern racial-political claim.
- The *al-pnei kol echav yishkon* geographical-vs-relational
  ambiguity is preserved in translation (ASV-style *over against*)
  and discussed in commentary; the parallel use at Gen 25:18 (the
  Ishmaelite tribes *al-pnei kol echav yipol*) is cited for the
  geographical reading.

The entry is the most editorially delicate of the chapter. The
Reviewer should attend especially to register: the entry must not
even by accident read as endorsing or amplifying any racializing
reception of the verse.

### 3. `el-roi-and-halom-elohim-variant` (v 13) — verify MT chosen, LXX emendation noted

The Reviewer should verify:

- The Masoretic Text reading *halom* is preserved in the running
  English (ASV's *Have I even here looked after him that sees me?*).
- The LXX/Vulgate emendation *Elohim* (giving *have I really seen
  God and remained alive after seeing him?*) is explicitly noted in
  the entry and in v 13 commentary, with the seeing-God-and-living
  anxiety parallels at Exod 33:20, Judg 6:22-23, Judg 13:22 cited.
- The modern critical scholarly distribution is presented in three
  parts: (a) MT-priority position (Sarna 1989, Alter 2004, JPS 1985,
  NJPS, NIV); (b) emendation position (Westermann 1985, Speiser AB,
  NRSV); (c) agnostic position (Wenham 1994).
- The WoH choice (MT preserved) is justified by reference to the
  established WoH textual-conservative practice (cf. the chapter-15
  Tzeboim ketiv/qere resolution); the choice is editorial, not
  doctrinal.
- The first-divine-name-naming-by-a-woman feature is documented with
  Trible 1984 and Reis 2002 as the standard feminist-biblical-
  scholarship references.
- The implications for the messenger-identity question (the v 13
  Hagar-identifies-the-speaker-as-YHWH datum supports position (b)
  of the messenger-identity question but does not preempt positions
  (a) or (c)) are cross-linked to the `malakh-yhwh-messenger` entry.

### 4. `shifchah-substitute-wife-arrangement` — verify ANE legal parallel citations accurate

The Reviewer should verify the ANE parallel citations:

- **Code of Hammurabi §146** (Old Babylonian, c. 1750 BCE): the
  hierodule (*nadītu*) provides her slave-girl (*šugītum*) as
  substitute-wife; explicit provision for the case where the slave-
  girl *makes herself equal with her mistress* — paralleling the
  Gen 16:4-6 scenario (*vatekal gevirtah b-eyneha*). Pritchard
  *ANET* (1969), pp. 172-173 prints the text. The Reviewer is
  encouraged to spot-check against Pritchard.
- **Nuzi tablets, HSS V 67** (Middle Babylonian, c. 1500 BCE,
  Hurrian-Mesopotamian milieu): Hurrian marriage-contract provisions
  for substitute-wife arrangements; Speiser (*Anchor Bible Genesis*,
  1964, pp. 119-121) reads the Nuzi parallels as *closer in detail*
  to the patriarchal narratives than the Hammurabi parallel, and
  connects the patriarchal Aramean-Hurrian milieu (Harran, Padan-
  Aram) to the Nuzi legal tradition.
- The cross-corpus forward-apply to Gen 30:3-13 (Bilhah and Zilpah)
  is verifiable: the same *shifchah* lexeme governs both narratives
  and the same *ulai ibaneh mimenah* niphal idiom recurs (Gen 16:2,
  30:3).
- The *shifchah* / *amah* lexical distinction (Westermann 1985,
  Sarna 1989, Hamilton 1990) is accurately characterized.

The entry's claim_type=direct is justified on the grammatical
explicitness of the lexeme, the verifiability of the *shifchah*/*amah*
distinction, the documentary evidence of the Hammurabi and Nuzi
parallels, and the modern critical consensus reading.

## Unresolved editorial questions

None. All 8 questions from the Translator's pass were resolved into
glossary entries. The remaining commentary slots at vv 4, 6, 8, 9,
15, 16 are intentionally left empty — these are narrative-bridge
verses whose Translator-default rendering matches the standard PD
reading and where no editorially-divergent gloss is required. (Verses
6, 8, and 9 carry *shifchah-substitute-wife-arrangement* or
*malakh-yhwh-messenger* `glossaryRefs[]` attachments without
needing additional commentary, since the apparatus carries the
philological material at vv 1-3 and v 7 respectively.)
