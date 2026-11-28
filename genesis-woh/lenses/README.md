# Genesis lenses (lenses 3 and 4)

Data for the four-lens Genesis reader (`/library/genesis-woh/lenses/N/` on www).
Lenses 1 (Hebrew + transliteration) and 2 (Wheel of Heaven literal translation) live in `../chapter-N.json` and are never edited from here.
This folder holds the rest, plus the map of where the canon speaks:

| Lens | Name | Data (per passage) | What it is |
|---|---|---|---|
| 1 | Hebrew | `../chapter-N.json` | The Masoretic text with a transliteration |
| 2 | Literal | `../chapter-N.json` | The reviewed literal translation; its translator's note opens from the note icon |
| 3 | Reading | `decoded[]` | The literal sentence with the canon-decoded words swapped in (*Elohim* → "those who came from the sky", and so on). No visual marking of the swapped words. Written after the rest; the reader shows "Reading in preparation" until it exists |
| 4 | Meaning | `meaning[]` | Third-person retelling per verse or verse group, with claim labels and canon refs (one card each) |
| — | Note | `note` | The passage commentary: labelled paragraphs, canon refs, an optional visual. Folded under the Meaning cards, opened from the note icon |

`schemaVersion` 2 (founder decision 2026-11-28) renamed `readings` → `meaning` and `explanation` → `note`, and added `decoded`.
`scripts/migrate_genesis_lenses_v2.py` converts a v1 file losslessly (idempotent; it maps every file back to v1 and compares before writing).

Validate with:

```sh
python3 scripts/validate_genesis_lenses.py --core-catalog ../core/model/catalog.json
python3 scripts/validate_genesis_lenses.py --staged   # before a lens commit
python3 scripts/validate_genesis_lenses.py --digest 1 # layer-2 digest for basedOn
python3 scripts/validate_genesis_lenses.py --glossary genesis-woh/lenses/decoding-glossary.json  # lens-3 hook (stub)
python3 -m unittest discover -s scripts -p 'test_validate_genesis_lenses.py'
```

## Files

| File | Purpose |
|---|---|
| `canon-map.json` | Every verse of Gen 1–50 mapped once to the canon paragraphs that quote, comment on or allude to it |
| `_lenses.json` | Index: `schemaVersion`, `canonMapVersion`, `chapters[]` (one row per lens chapter file) |
| `schema.json` | JSON Schema (draft 2020-12) for `chapter-N.json` |
| `chapter-N.json` | Lenses 3–4 and the passage notes for chapter N (written by the authoring pipeline) |
| `chapter-N-editor-report.md`, `chapter-N-signoff-package.md` | Audit trail per chapter |

## Canon standing (ADR 0018)

The canon is the dictated Messages only.

| Standing | Source | Use |
|---|---|---|
| `canon` | *The Book Which Tells the Truth* (TBWTT) paragraphs spoken by Yahweh; *Extraterrestrials Took Me to Their Planet* (ETTMTTP) chapter 2 paragraphs spoken by Yahweh | May ground a `framework` claim |
| `narration` | Raël's narration in TBWTT and ETTMTTP | Not canon; cite the dictated paragraph instead |
| `check` | (none at present) | Reserved for a passage whose dictation status is unconfirmed; not canon until the founder rules |
| `author-opinion` | *Let's Welcome the Extraterrestrials* (LWTE); ETTMTTP chapter 3 ("The Keys"), author-written, not dictated (founder ruling 2026-11-27) | Raël's commentary. Always cited with this label; never the sole basis of a `framework` claim |

The rules are data (`standingRules` in `canon-map.json`); the validator derives each paragraph's standing from its book, chapter and `speaker` field.

## canon-map.json

```json
{
  "version": "1.0.0",
  "bookSlug": "genesis-woh",
  "standingRules": [{ "book": "TBWTT", "speaker": "Yahweh", "standing": "canon" }],
  "entries": [
    {
      "range": ["1:1", "1:1"],
      "relation": "quotes",
      "refs": [
        { "ref": "TBWTT-2:4", "relation": "quotes", "standing": "canon" },
        { "ref": "TBWTT-2:5", "relation": "comments", "standing": "canon" }
      ],
      "note": "optional"
    }
  ]
}
```

- `range` — inclusive `["C:V", "C:V"]`; it may cross chapters (long silent stretches). Every verse of Gen 1–50 is in exactly one entry.
- `refs[].ref` — the canon paragraph `refId` exactly as in the book's chapter files (`TBWTT-2:4`, `ETTMTTP-2:104`, `LWTE-1:69`).
- `refs[].relation` — `quotes` (the paragraph quotes this Genesis text), `comments` (it explains the quoted passage), `alludes` (it refers to the episode without quoting it), `opinion` (author-opinion refs only: LWTE and ETTMTTP chapter 3).
- `refs[].standing` — derived from `standingRules`; see above.
- `refs[].flags` — optional, e.g. `["sensitive"]` for the ETTMTTP descent passages (2:104, 2:123): editorial review before use.
- `relation` (entry level) — the strongest relation among the canon-standing refs (`quotes` > `comments` > `alludes`); `opinion` if only author-opinion refs; `check` if only unconfirmed refs; `silent` if `refs` is empty.

Quote-checked against the canon text on 2026-11-27. When the map changes, bump `version` and the `canonMapVersion` of every lens file and `_lenses.json`.

## chapter-N.json

See `schema.json`. In short:

- `basedOn` pins the layer-2 `translationVersion`, `layer2Digest` and `canonMapVersion` the lens was written against.
- `lens` carries track, version, status (`draft` → `editor-review` → `reviewer-approved` → `awaiting-human` → `stable`), `modelDrafts`, `reviewerReport`, `signedOffBy`, `signedOffAt` and `coreClaims` (`{"woh-claim-0009": "0.2.0"}`).
- `passages[]` — contiguous, non-overlapping verse ranges covering the chapter. Each has `canonCoverage`, the strongest canon relation over its verses (`quotes | comments | alludes | silent`; map relations `opinion` and `check` count as `silent`, so the reader shows the "Messages do not comment" marker).
- `decoded[]` (lens 3, Reading) — `{"refs": ["1:1"], "text": {"en": "…"}}`, nothing else: no claim label, no canon refs (the decoding is justified in the decoding glossary, not per sentence). Refs stay inside the passage. A chapter may have no decoded units at all; once it has one, every verse of the chapter is in exactly one. The reader shows a unit in the card of its first verse, so a unit should not reach into the next Meaning card (warning).
- `meaning[]` (lens 4, Meaning; v1 `readings`) — third-person rendering; each verse of the chapter is in exactly one Meaning unit, and each unit is one card in the reader. `basis` is `canon` or `synthesis`; `claim` is `direct | framework | inferred | speculative`; `canon` lists refs; `coreClaim` optional.
- `note.paragraphs[][]` (the passage note; v1 `explanation`) — paragraphs of claim-labelled segments, with optional `canon` and `coreClaim`; optional `visual`.

Example passage:

```json
{
  "id": "gen-1-day-1",
  "range": ["1:1", "1:5"],
  "title": { "en": "The First Day: Finding the Planet" },
  "canonCoverage": "quotes",
  "decoded": [{ "refs": ["1:1"], "text": { "en": "…" } }],
  "meaning": [{ "refs": ["1:1"], "text": { "en": "…" }, "basis": "canon", "claim": "framework", "canon": ["TBWTT-2:4"] }],
  "note": { "paragraphs": [[{ "text": { "en": "…" }, "claim": "direct" }]], "visual": { "kind": "diagram", "ref": "creation-week", "alt": { "en": "…" } } }
}
```

A canon ref is a plain string (`"TBWTT-2:4"`) only when its standing is `canon`. Any other standing must be written out: `{"ref": "LWTE-1:69", "standing": "author-opinion"}`.

### layer2Digest

For chapter N: take `../chapter-N.json`, sort its paragraphs by `n`, build one line per verse as `"<N>:<n>"` + TAB + `i18n.en` (byte-for-byte, no trimming or normalisation), join with `\n` (no trailing newline), UTF-8 encode, SHA-256. Value: `"sha256:" + hex`.
A mismatch means layer 2 changed after the lens was written: a warning for `draft` and `editor-review`, an error from `reviewer-approved` on.

## Validator rules

1. Canon map: semver `version`; every Gen 1–50 verse covered exactly once; every ref exists in the canon chapter files; stated standing equals the rule-derived standing; LWTE refs are `opinion` + `author-opinion`; every author-opinion ref (LWTE, ETTMTTP chapter 3) has relation `opinion`, and `opinion` is used for nothing else; no narration refs; entry `relation` consistent with its refs; silent entries have no refs.
2. Lens file: `schemaVersion` 2 (a v1 file or a v1 key name is an error that points at the migration), `bookSlug`, chapter matches file name; `basedOn.translationVersion` equals layer 2; `canonMapVersion` equals the map; digest matches (see above).
3. Coverage: passages and Meaning units each cover every verse of the chapter exactly once; Meaning units stay inside their passage. `decoded` is present on every passage (empty allowed); once any passage of the chapter has a decoded unit, decoded units cover every verse exactly once, inside their passage, with only `refs` and a non-empty `text.en`.
4. `canonCoverage` equals the canon-map value for the passage's verses.
5. Every canon ref exists; non-canon standings are written out; LWTE refs carry `author-opinion`.
6. A `framework` Meaning unit or note segment needs a canon-standing ref or a `coreClaim`, and cannot rest on author-opinion (LWTE, ETTMTTP chapter 3) or `check` refs alone.
7. A Meaning unit with `basis: "canon"` cites a canon-standing ref that the canon map attaches to one of its verses.
8. Every `coreClaim` is listed in `lens.coreClaims`, and every listed claim exists in `core/model/catalog.json` (version drift is a warning).
9. `stable` needs `signedOffBy` and `signedOffAt`, and a plain release version. Before sign-off `lens.version` may carry a pre-release tag (`1.1.0-rc1`) while a revision is under review.
10. `_lenses.json`: `schemaVersion` 2; `canonMapVersion` matches; each row matches its lens file (status, version, sign-off); every lens file is listed.
11. `--staged`: fails if `genesis-woh/chapter-*.json` is staged — lens commits never touch layer 2.
12. `--glossary PATH`: loads the decoding glossary (`decoding-glossary.json`, being drafted) and runs the lens-3 glossary hook on every decoded unit. The hook is a stub until the glossary's shape is settled; an unreadable file is an error.
