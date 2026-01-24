# Wheel of Heaven Library Data

A curated collection of religious, philosophical, and ancient texts exploring humanity's origins and cosmic connections.

## Overview

This repository contains structured book data for the [Wheel of Heaven](https://www.wheelofheaven.io) library reader. Texts are organized by tradition and include multilingual translations.

### Traditions

| Tradition | Description | Status |
|-----------|-------------|--------|
| **Raëlian** | The Messages from the Elohim | Active |
| **Biblical** | Hebrew Bible, New Testament, Apocrypha | Planned |
| **Ancient Astronaut** | Key works in the genre | Planned |
| **Ancient Texts** | Sumerian, Egyptian, Vedic sources | Planned |

### Current Books

- **The Book Which Tells the Truth** (1973) - Raël's first contact account

## Directory Structure

```
data/library/
├── README.md                           # This file
├── catalog.json                        # Central index of all books
│
├── book-slug.json                      # Single-file format (small books)
│
└── book-slug/                          # Split format (large books >100KB)
    ├── _meta.json                      # Book metadata
    ├── chapter-1.json                  # Chapter 1 content
    ├── chapter-2.json                  # Chapter 2 content
    └── ...
```

## Formats

### Single-File Format
For smaller books (<100KB), all content is in one JSON file:

```json
{
  "slug": "book-slug",
  "code": "BSL",
  "titles": {
    "en": "English Title",
    "fr": "Titre Français"
  },
  "primaryLang": "fr",
  "publicationYear": 1973,
  "chapters": [
    {
      "n": 1,
      "refId": "BSL-1",
      "title": "Chapter Title",
      "paragraphs": [...]
    }
  ]
}
```

### Split Format
For larger books (>100KB), content is split into separate files:

**`_meta.json`** - Book metadata:
```json
{
  "slug": "book-slug",
  "code": "BSL",
  "titles": {...},
  "primaryLang": "fr",
  "chapterCount": 7,
  "paragraphCount": 1029,
  "chapterFiles": [
    {"n": 1, "file": "chapter-1.json", "title": "...", "paragraphs": 62},
    {"n": 2, "file": "chapter-2.json", "title": "...", "paragraphs": 113}
  ]
}
```

**`chapter-N.json`** - Chapter content:
```json
{
  "n": 1,
  "bookSlug": "book-slug",
  "bookCode": "BSL",
  "refId": "BSL-1",
  "title": "Chapter Title",
  "paragraphs": [...]
}
```

## Catalog Schema

The `catalog.json` file is the central index:

```json
{
  "version": "1.0",
  "updated": "2025-01-24",
  "traditions": [...],      // Religious/philosophical traditions
  "collections": [...],     // Book collections within traditions
  "books": [...],           // All books with metadata
  "referenceFormats": {...} // Canonical reference format templates
}
```

### Traditions
```json
{
  "id": "raelian",
  "code": "RAE",
  "name": {"en": "Raëlian Corpus", "fr": "Corpus Raëlien"},
  "description": {"en": "..."},
  "order": 1,
  "icon": "message-circle"
}
```

### Collections
```json
{
  "id": "raelian-messages",
  "tradition": "raelian",
  "code": "MSG",
  "name": {"en": "The Messages"},
  "order": 1,
  "books": ["the-book-which-tells-the-truth", "..."]
}
```

### Book Entries
```json
{
  "slug": "the-book-which-tells-the-truth",
  "code": "TBWTT",
  "tradition": "raelian",
  "collection": "raelian-messages",
  "order": 1,
  "author": "Raël (Claude Vorilhon)",
  "publicationYear": 1973,
  "primaryLang": "fr",
  "availableLangs": ["fr", "en"],
  "completeLangs": ["fr", "en"],
  "chapters": 7,
  "paragraphs": 1029,
  "tags": ["contact", "genesis", "elohim"],
  "status": "complete",
  "format": "split"
}
```

**Status values:**
- `complete` - Fully digitized and translated
- `partial` - Some chapters or translations available
- `planned` - Scheduled for future digitization
- `draft` - Work in progress

**Format values:**
- `single` - Single JSON file (default)
- `split` - Directory with per-chapter files

## Paragraph Schema

```json
{
  "n": 1,
  "refId": "TBWTT-1:1",
  "speaker": "Narrator",
  "text": "Original language text...",
  "i18n": {
    "en": "English translation...",
    "de": "German translation..."
  }
}
```

## Canonical References

Format: `{BookCode} {Chapter}:{Paragraph}`

Examples:
- `TBWTT 1:5` - The Book Which Tells the Truth, Chapter 1, Paragraph 5
- `GEN 1:1` - Genesis, Chapter 1, Paragraph 1

Reference IDs in data:
- Book: `TBWTT`
- Chapter: `TBWTT-1`
- Paragraph: `TBWTT-1:5`

## Adding a New Book

1. **Add catalog entry** in `catalog.json`:
   ```json
   {
     "slug": "new-book-slug",
     "code": "NBS",
     "tradition": "tradition-id",
     "collection": "collection-id",
     "status": "planned"
   }
   ```

2. **Create book JSON** as `new-book-slug.json` (single format) or directory (split format)

3. **Run canonical refs script**:
   ```bash
   python scripts/add-canonical-refs.py new-book-slug
   ```

4. **Split if large** (>100KB):
   ```bash
   python scripts/split-book-chapters.py new-book-slug
   ```

5. **Update status** in catalog to `complete` or `partial`

## Validation

JSON Schema files are in `/schemas/`:
- `catalog.schema.json` - Catalog validation
- `book.schema.json` - Single-file book validation
- `book-meta.schema.json` - Split format metadata
- `chapter.schema.json` - Split format chapter
- `study-data.schema.json` - User study data export

Validate with any JSON Schema validator:
```bash
npx ajv validate -s schemas/book.schema.json -d data/library/book.json
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/add-canonical-refs.py` | Add refId fields to paragraphs |
| `scripts/split-book-chapters.py` | Split large books into chapters |

## Multilingual Support

- `primaryLang` - Original language of the text
- `i18n` object in paragraphs contains translations
- `availableLangs` - Languages with any content
- `completeLangs` - Languages with full translation

Language codes follow ISO 639-1/639-2 (e.g., `en`, `fr`, `he`, `gez`).

## Contributing

We welcome contributions of:
- New book digitizations
- Translation improvements
- Corrections to existing texts

Please ensure texts are either in the public domain or properly licensed for redistribution.

## License

Content is provided under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain) where applicable. Individual texts may have their own licensing requirements noted in their metadata.
