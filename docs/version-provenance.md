# Version Provenance Metadata

Library records may expose a structured `version` object alongside the older
`versionSource`, `versionLicense`, `versionTitles`, `sourceCitation`, and
`reviewer` fields. The older fields remain valid while records are migrated.

The goal of the `version` object is to answer four reader-facing questions:

- What version of this text am I reading?
- What language and reference system does this version use?
- What license or redistribution status applies?
- What source text, witness stack, or editorial process produced it?

## Shape

Add `version` to split-format `_meta.json` records. The same object may later be
used in single-file book records.

```json
{
  "version": {
    "schemaVersion": 1,
    "title": "Wheel of Heaven Translation",
    "shortTitle": "WoH, 2026",
    "type": "translation",
    "language": "en",
    "sourceLanguage": "he",
    "refSystem": "chapter-verse",
    "scope": "Genesis 1-50",
    "license": {
      "status": "project-cc0",
      "spdx": "CC0-1.0",
      "url": "https://creativecommons.org/publicdomain/zero/1.0/"
    },
    "provenance": {
      "sourceRecordId": "genesis",
      "sourceUrl": "https://github.com/wheelofheaven/www.wheelofheaven.io/issues/12",
      "baseText": "Pointed Hebrew of the Westminster Leningrad Codex",
      "method": "Wheel of Heaven translation from the Hebrew source text."
    },
    "responsibility": {
      "translator": "Wheel of Heaven",
      "reviewer": "zarazinsfuss"
    }
  }
}
```

## Required Fields

- `schemaVersion`: positive integer for this nested contract. Current value: `1`.
- `title`: human-readable version title.
- `type`: one of `source-text`, `translation`, `curated-translation`,
  `edition`, `adaptation`, or `composite`.
- `language`: language code for the readable version.
- `sourceLanguage`: language code for the primary source layer.
- `refSystem`: reference system used by this version, such as `chapter-verse` or
  `chapter-paragraph`.
- `license.status`: one of `project-cc0`, `public-domain`, `licensed`,
  `source-restricted`, `mixed`, or `unknown`.
- `provenance`: at least one of `sourceRecordId`, `sourceUrl`, `baseText`, or
  `citation`.

## Optional Fields

- `shortTitle`: compact display title.
- `scope`: coverage of this version when a record is partial.
- `license.spdx`: SPDX identifier where applicable.
- `license.url`: license URL where applicable.
- `license.detail`: human-readable licensing note.
- `provenance.method`: short statement of translation or curation method.
- `provenance.witnesses`: ordered witness list for layered reconstructions.
- `responsibility`: people, teams, or systems responsible for translation,
  review, curation, generation, or signoff.

## Migration Rules

- Do not remove legacy fields during migration unless the consuming apps have
  been updated to read `version`.
- Populate `version` first for records that are already curated, reader-facing,
  or cited from the main site.
- Keep `version.provenance` concise. Long bibliographies can remain in
  `sourceCitation` until a separate bibliography model exists.
- Use `license.status: "unknown"` when a record is not ready for redistribution
  claims. Do not infer a permissive license from the source language or age.

## Validation

Run:

```bash
python3 scripts/validate_version_provenance.py
```

The default mode validates only records that already contain `version` and
reports how many legacy provenance records remain. Use `--strict` to fail when a
record has legacy provenance fields but has not yet been migrated.
