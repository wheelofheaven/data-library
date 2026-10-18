# Reviewed paragraph repairs

## 2026-10-18: first two Messages books

`2026-10-18-paragraph-boundaries.json` records exact before/after text for
22 boundary moves across six adjacent-reference boundaries, plus nine newly
identified continuation fragments. Each move preserves all non-whitespace
characters and their order. Paragraph numbers and reference IDs are unchanged.

The French reference used for checking quotation layout was the workspace PDF
`data-sources/pdf/_combined/le-message-donne-par-les-extra-terrestres.pdf`.
For example, PDF page 26 (printed page 28) has the Genesis 10:32 quotation as
one sentence; TBWTT 2:69–70 had split it immediately before “Déluge”. The
translations were checked against the meaning of each French boundary rather
than against relative character positions.

### The Book Which Tells the Truth

New continuation records: 2:82; 3:17, 21, 80, 81, 244, 256, 281; 4:14.
These repair detached scripture citations and interrupted quotations. Together
with existing tags, the reader now joins 21 groups containing 23 continuation
records. The book retains its 759 individually addressable reference units.

The tracked single-file bundle was rebuilt from the chapters. This also brings
its previously stale Hebrew translations into parity with those chapter files.

### Extraterrestrials Took Me to Their Planet

| Boundary | Correct division | Languages repaired |
|---|---|---|
| 1:3–4 | The question about the seven hundred supporters begins 1:4 | ja, ko |
| 2:14–15 | The arrival at the bathtub begins 2:15 | ru, ja, ko, zh, zh-Hant |
| 2:30–31 | Stars and planets as atoms begins 2:31 | ja, ko |
| 2:37–38 | “The boss” completes 2:37; the following labor discussion begins 2:38 | fr, es, ru, he, ja, ko, zh, zh-Hant |
| 2:38–39 | The appeal to discard old principles begins 2:39 | ru, zh, zh-Hant |
| 2:39–40 | The warning about fighting for the fatherland begins 2:40 | de, ja |

Its existing 3:193–194 continuation also benefits from the reader fix. The book
retains 475 reference units. English wording and English text boundaries are
unchanged in both books. Existing audio was not regenerated.

### Apply and verify

```sh
python3 scripts/repair_paragraph_boundaries.py
python3 scripts/repair_paragraph_boundaries.py --apply
python3 scripts/rebuild_book_bundle.py the-book-which-tells-the-truth extraterrestrials-took-me-to-their-planet
python3 -m unittest discover -s scripts -p 'test_paragraph_boundaries.py' -v
```

The repair checks the entire manifest before writing. It refuses changed source
text and is idempotent. The tests cover word/reference conservation, a changed
source aborting without writes, and chapter/catalog/bundle consistency. The
rebuild script now updates catalog totals as well as chapter metadata.

Validation: the English preview, full ten-language website, API, and docs builds
pass. Rendered-output checks cover 20 reader pages and 70 API chapter responses
(the seven languages currently advertised by these catalog entries). Desktop
and 390px mobile visuals, continuation deep links, and interlinear rows were
checked in the browser. Direct click-selection automation was inconclusive:
the browser connection repeatedly timed out. Existing selection handlers remain
on every reference unit. No deployment or audio regeneration was performed.

### Separate follow-up: third book

The first-two-book repair does not change *Let's Welcome the Extraterrestrials*.
Its English importer (`fill_en_from_epub.py`) assigned paragraphs proportionally
by French/English paragraph counts. This cannot establish semantic alignment.
The English EPUB and French PDF also differ in headings, lists, and edition
content, especially chapter 4. A chapter-by-chapter collation and citation
migration are needed; applying a fixed numeric offset would be incorrect.
