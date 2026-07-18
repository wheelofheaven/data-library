#!/usr/bin/env python3
"""Package the CC0 Wheel of Heaven Translation Program books as HuggingFace datasets.

For each `-woh` book, emits a HuggingFace-ready folder under scripts/dist-hf/<slug>/:
  <slug>.jsonl  — one row per verse: the aligned parallel corpus
  glossary.json — the per-book translation glossary
  README.md     — the dataset card (methodology, provenance, sign-off, CC0)

The parallel row joins the translation side (chapter-N.json: original `text`,
English `i18n.en`, `notes`, `glossaryRefs`) with the source apparatus
(source-*-N.json: transliteration, manuscript witnesses) by `refId`.

Stdlib only. Run from the data-library repo root:
    python scripts/build_translation_datasets.py
Then upload (see docs), e.g.:
    hf upload wheelofheaven/<slug> scripts/dist-hf/<slug> --repo-type=dataset
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = Path(__file__).resolve().parent / "dist-hf"
WWW = "https://www.wheelofheaven.world"

# Only the CC0 Translation Program books (versionLicense == CC0-1.0).
# The Raëlian canon (the-book-which-tells-the-truth, extraterrestrials-took-me-
# to-their-planet) is deliberately excluded: versionLicense is unset (not CC0).
BOOKS = ["daniel-woh", "jubilees-woh", "book-of-enoch-woh", "genesis-woh"]

# ISO-639 code -> human name (for the card).
LANG_NAME = {"he": "Hebrew", "arc": "Aramaic", "grc": "Ancient Greek",
             "akk": "Akkadian", "sux": "Sumerian", "ar": "Arabic"}


def load_source_map(book_dir):
    """refId -> {transliteration, text_lang, witness_primary, witness_secondary}
    built from every source-*.json in the book (naming varies: source-N.json,
    source-he-N.json, source-grc-N.json)."""
    m = {}
    for f in glob.glob(str(book_dir / "source-*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for seg in d.get("verses") or d.get("paragraphs") or []:
            rid = seg.get("refId")
            if not rid:
                continue
            m[rid] = {
                "transliteration": seg.get("translit") or "",
                "source_lang": seg.get("text_lang") or "",
                "witness_primary": seg.get("witness_primary") or "",
                "witness_secondary": seg.get("witness_secondary") or "",
            }
    return m


def rows_for(book_dir, meta):
    src = load_source_map(book_dir)
    orig_lang = meta.get("originalLang") or meta.get("primaryLang") or ""
    rows = []
    chapters = sorted(glob.glob(str(book_dir / "chapter-*.json")),
                      key=lambda p: int(re.search(r"chapter-(\d+)\.json", p).group(1)))
    for cf in chapters:
        ch = json.load(open(cf, encoding="utf-8"))
        cn = ch.get("n")
        for p in ch.get("paragraphs", []):
            rid = p.get("refId")
            s = src.get(rid, {})
            notes = p.get("notes") or {}
            commentary = notes.get("official") if isinstance(notes, dict) else ""
            rows.append({
                "ref": rid,
                "chapter": cn,
                "verse": p.get("n"),
                "original": p.get("text") or "",
                "original_lang": p.get("text_lang") or s.get("source_lang") or orig_lang,
                "transliteration": p.get("translit") or s.get("transliteration") or "",
                "english": (p.get("i18n") or {}).get("en") or "",
                "commentary": commentary or "",
                "glossary_refs": p.get("glossaryRefs") or [],
                "witness_primary": s.get("witness_primary", ""),
                "witness_secondary": s.get("witness_secondary", ""),
            })
    return rows


def clean_desc(d):
    """Strip internal batch codenames ('Ship A/B') from a public description."""
    reps = [
        (r"OUTSIDE Ship [A-Z] scope", "outside the scope of this edition"),
        (r"Ship [A-Z] scope:\s*", "Scope: "),
        (r"Ship [A-Z] covers", "This edition covers"),
        (r"follows as a separate ship", "is a separate edition"),
        (r"as a separate ship", "as a separate edition"),
        (r"\bShip [A-Z]\b", "this edition"),
    ]
    for pat, rep in reps:
        d = re.sub(pat, rep, d)
    return d


def glossary_terms(gloss):
    if isinstance(gloss, dict):
        return gloss.get("terms") or gloss.get("entries") or []
    return gloss or []


def card(slug, meta, n_rows, n_gloss):
    titles = meta.get("titles") or {}
    en_title = titles.get("en") or slug
    orig_lang = meta.get("originalLang") or meta.get("primaryLang") or ""
    orig_name = LANG_NAME.get(orig_lang, orig_lang or "the source language")
    desc = clean_desc((meta.get("descriptions") or {}).get("en") or "")
    provenance = meta.get("sourceCitation") or meta.get("versionSource") or ""
    vstatus = meta.get("verificationStatus")
    signoff = ""
    if vstatus and vstatus.startswith("human-signed-off"):
        signoff = f"\n- **Review status:** editor + reviewer approved, human-signed-off ({vstatus.split('human-signed-off-')[-1]})."
    langs = "\n".join(f"- {c}" for c in dict.fromkeys(["en", orig_lang]) if c)
    pretty = f"{en_title} — Wheel of Heaven Translation"
    front = (
        "---\n"
        "license: cc0-1.0\n"
        f"pretty_name: \"{pretty}\"\n"
        "language:\n" + langs + "\n"
        "task_categories:\n- translation\n"
        "tags:\n- translation\n- parallel-corpus\n- religious-text\n"
        f"- {orig_name.lower().replace(' ', '-')}\n- biblical-studies\n- digital-humanities\n"
        "---\n\n"
    )
    body = (
        f"# {pretty}\n\n"
        f"A verse-aligned parallel corpus of **{en_title}** — the {orig_name} source text "
        f"alongside the Wheel of Heaven English translation, with transliteration, "
        f"manuscript-witness attribution, per-verse translator commentary, and a translation "
        f"glossary. {desc}\n\n"
        "## Files\n\n"
        f"- **`{slug}.jsonl`** — {n_rows} rows, one per verse.\n"
        f"- **`glossary.json`** — the {n_gloss}-entry translation glossary (the lexical "
        "decisions that make this a *Wheel of Heaven* translation rather than a generic one).\n\n"
        "## Columns\n\n"
        "`ref`, `chapter`, `verse`, `original` (source script), `original_lang`, "
        "`transliteration`, `english` (WoH translation), `commentary` (translator's note; "
        "populated only for verses the editor annotated), `glossary_refs`, `witness_primary`, "
        "`witness_secondary`.\n\n"
        "## Method & provenance\n\n"
        f"Produced under the Wheel of Heaven Translation Program (translator → editor → "
        f"reviewer → human sign-off).{signoff}\n\n"
        + (f"**Source:** {provenance}\n\n" if provenance else "")
        + "## License & citation\n\n"
        "CC0-1.0 (public domain). Documentation and the reading edition: "
        f"[{WWW}/library/{slug}/]({WWW}/library/{slug}/).\n\n"
        "```\n"
        f"Wheel of Heaven Translation Program. {en_title} (Wheel of Heaven Translation). "
        f"Wheel of Heaven, {meta.get('publicationYear', 2026)}. CC0-1.0. {WWW}/library/{slug}/\n"
        "```\n"
    )
    return front + body


def build(slug):
    bd = ROOT / slug
    meta = json.load(open(bd / "_meta.json", encoding="utf-8"))
    if meta.get("versionLicense") != "CC0-1.0":
        sys.exit(f"{slug}: versionLicense is {meta.get('versionLicense')!r}, not CC0 — refusing to package.")
    rows = rows_for(bd, meta)
    gpath = bd / "_translation-glossary.json"
    gloss = json.load(open(gpath, encoding="utf-8")) if gpath.exists() else {}
    if isinstance(gloss, dict):
        gloss.pop("$schema", None)  # broken relative ref, meaningless off-repo
    n_gloss = len(glossary_terms(gloss))

    out = DIST / slug
    out.mkdir(parents=True, exist_ok=True)
    with open(out / f"{slug}.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(out / "glossary.json", "w", encoding="utf-8") as fh:
        json.dump(gloss, fh, ensure_ascii=False, indent=2)
    (out / "README.md").write_text(card(slug, meta, len(rows), n_gloss), encoding="utf-8")
    filled = sum(1 for r in rows if r["english"].strip())
    print(f"  ✓ {slug}: {len(rows)} verses ({filled} with English), {n_gloss} glossary entries "
          f"→ dist-hf/{slug}/")
    return len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", metavar="SLUG")
    args = ap.parse_args()
    books = [args.only] if args.only else BOOKS
    if DIST.exists() and not args.only:
        shutil.rmtree(DIST)
    total = 0
    print(f"Packaging {len(books)} CC0 translation book(s) → {DIST.relative_to(ROOT)}/\n")
    for b in books:
        total += build(b)
    print(f"\n{total} verses across {len(books)} books.")
    print("Upload: hf upload wheelofheaven/<slug> scripts/dist-hf/<slug> --repo-type=dataset")


if __name__ == "__main__":
    main()
