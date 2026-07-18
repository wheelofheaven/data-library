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

# CC0 -woh books HELD from publication pending a rights/sensitivity review —
# these translate the scriptures of living religious movements. Do not publish
# without an explicit rights decision. (The Raëlian canon is already excluded by
# the versionLicense != CC0-1.0 gate.)
HELD = {"hidden-words-woh", "oomoto-shinyu-woh", "thanh-ngon-hiep-tuyen-woh"}


def discover_books():
    """Every *-woh book with versionLicense == CC0-1.0, minus HELD, sorted."""
    out = []
    for d in sorted(ROOT.glob("*-woh")):
        if not d.is_dir() or d.name in HELD:
            continue
        m = d / "_meta.json"
        try:
            if m.exists() and json.load(open(m, encoding="utf-8")).get("versionLicense") == "CC0-1.0":
                out.append(d.name)
        except Exception:
            continue
    return out

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


def load_reference(book_slug):
    """The aligned public-domain reference translation that sits beside a `-woh`
    book (the bare sibling directory, e.g. `genesis` next to `genesis-woh`).

    Returns (ref_map, version, license, status) where ref_map maps
    (chapter, verse) -> reference English, and status is one of:
      "ok"                 — a public-domain English reference was loaded
      "none"               — no sibling reference directory / metadata
      "unverified-license" — a reference exists but its licence isn't PD/CC0
      "non-english"        — a reference exists but carries no English text
                             (e.g. an Arabic-only source edition like the Quran)
    ref_map is non-empty only when status == "ok". We never attach a reference
    whose licence we can't vouch for — the corpus stays honestly licensed.
    """
    if not book_slug.endswith("-woh"):
        return {}, "", "", "none"
    ref_dir = ROOT / book_slug[:-4]
    mp = ref_dir / "_meta.json"
    if not ref_dir.is_dir() or not mp.exists():
        return {}, "", "", "none"
    try:
        rm = json.load(open(mp, encoding="utf-8"))
    except Exception:
        return {}, "", "", "none"
    ver = (rm.get("versionTitles") or {}).get("en") or ""
    lic = rm.get("versionLicense") or ""
    prim = rm.get("primaryLang") or ""
    ref_map = {}
    for cf in sorted(glob.glob(str(ref_dir / "chapter-*.json"))
                     + glob.glob(str(ref_dir / "tablet-*.json")),
                     key=lambda p: int(re.search(r"-(\d+)\.json", p).group(1))):
        try:
            ch = json.load(open(cf, encoding="utf-8"))
        except Exception:
            continue
        cn = ch.get("n")
        for p in ch.get("paragraphs", []):
            # English lives in `text` for an English edition, else in i18n.en.
            eng = (p.get("text") or "") if prim == "en" else ((p.get("i18n") or {}).get("en") or "")
            if eng.strip():
                ref_map[(cn, p.get("n"))] = eng.strip()
    # Accuracy of the status matters: report "no English available" before a
    # licence complaint, so an Arabic-only source edition (the Quran) isn't
    # mislabelled as merely needing a licence tag.
    if not ref_map:
        return {}, ver, lic, "non-english"
    if lic.strip().lower() not in ("public domain", "cc0-1.0", "cc0"):
        # An English reference exists but we can't vouch for its licence — never assert it.
        return {}, ver, lic, "unverified-license"
    return ref_map, ver, lic, "ok"


def rows_for(book_dir, meta, ref=None):
    src = load_source_map(book_dir)
    ref_map, ref_ver, ref_lic = ref or ({}, "", "")
    orig_lang = meta.get("originalLang") or meta.get("primaryLang") or ""
    rows = []
    chapters = sorted(glob.glob(str(book_dir / "chapter-*.json"))
                      + glob.glob(str(book_dir / "tablet-*.json")),
                      key=lambda p: int(re.search(r"-(\d+)\.json", p).group(1)))
    for cf in chapters:
        ch = json.load(open(cf, encoding="utf-8"))
        cn = ch.get("n")
        for p in ch.get("paragraphs", []):
            rid = p.get("refId")
            s = src.get(rid, {})
            notes = p.get("notes") or {}
            commentary = notes.get("official") if isinstance(notes, dict) else ""
            ref_text = ref_map.get((cn, p.get("n")), "")
            rows.append({
                "ref": rid,
                "chapter": cn,
                "verse": p.get("n"),
                "original": p.get("text") or "",
                "original_lang": p.get("text_lang") or s.get("source_lang") or orig_lang,
                "transliteration": p.get("translit") or s.get("transliteration") or "",
                "english": (p.get("i18n") or {}).get("en") or "",
                "reference_english": ref_text,
                "reference_version": ref_ver if ref_text else "",
                "reference_license": ref_lic if ref_text else "",
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


def review_status(book_dir, meta):
    """An honest one-line review status for the card (never overclaims sign-off)."""
    vs = meta.get("verificationStatus") or ""
    if vs.startswith("human-signed-off"):
        return f"editor + reviewer approved, human-signed-off ({vs.split('human-signed-off-')[-1]})"
    if "pending-verification" in vs:
        return ("best-effort manuscript reconstruction, **pending verification** — "
                "not yet through editor/reviewer sign-off")
    if list(book_dir.glob("*signoff-package*")) or list(book_dir.glob("*editor-report*")):
        return "editor + reviewer reviewed per chapter (sign-off packages on file)"
    return "**draft** — machine translation + glossary applied, not yet editor/reviewer signed off"


def card(slug, meta, n_rows, n_gloss, review, ref_ver="", ref_lic="", ref_status="none", n_ref=0):
    titles = meta.get("titles") or {}
    en_title = titles.get("en") or slug
    orig_lang = meta.get("originalLang") or meta.get("primaryLang") or ""
    orig_name = LANG_NAME.get(orig_lang, orig_lang or "the source language")
    desc = clean_desc((meta.get("descriptions") or {}).get("en") or "")
    provenance = meta.get("sourceCitation") or meta.get("versionSource") or ""
    langs = "\n".join(f"- {c}" for c in dict.fromkeys(["en", orig_lang]) if c)
    pretty = f"{en_title} — Wheel of Heaven Translation"
    has_ref = ref_status == "ok" and n_ref
    front = (
        "---\n"
        "license: cc0-1.0\n"
        f"pretty_name: \"{pretty}\"\n"
        "language:\n" + langs + "\n"
        "task_categories:\n- translation\n"
        "tags:\n- translation\n- parallel-corpus\n- religious-text\n"
        f"- {orig_name.lower().replace(' ', '-')}\n- biblical-studies\n- digital-humanities\n"
        + ("- public-domain\n" if has_ref else "")
        + "---\n\n"
    )
    if has_ref:
        cov = (f"all {n_rows} verses" if n_ref >= n_rows
               else f"{n_ref} of {n_rows} verses ({round(100 * n_ref / n_rows)}%); "
                    "the remaining verses differ in versification between the editions and are left blank")
        ref_section = (
            "## Reference translation\n\n"
            f"This edition bundles an aligned **reference translation** — *{ref_ver}* "
            f"({ref_lic}) — in the `reference_english` column, joined to the source verse-by-verse "
            f"and covering {cov}. It is the neutral control the Wheel of Heaven rendering can be read "
            "against: where `english` and `reference_english` diverge, the glossary and commentary "
            "explain why (e.g. *Elohim* kept as a plural, *taninim* as great dragons, *ruach* as "
            "breath rather than Spirit).\n\n"
        )
    else:
        ref_section = (
            "## Reference translation\n\n"
            "**No aligned public-domain English reference translation is bundled for this text.** "
            "The `reference_english` column is present but empty, so the schema is identical across the "
            "whole collection; a public-domain reference may be added in a later revision.\n\n"
        )
    body = (
        f"# {pretty}\n\n"
        f"A verse-aligned parallel corpus of **{en_title}** — the {orig_name} source text "
        f"alongside the Wheel of Heaven English translation, with transliteration, "
        f"manuscript-witness attribution, per-verse translator commentary, an aligned "
        f"public-domain reference translation, and a translation glossary. {desc}\n\n"
        "## Files\n\n"
        f"- **`{slug}.jsonl`** — {n_rows} rows, one per verse.\n"
        f"- **`glossary.json`** — the {n_gloss}-entry translation glossary (the lexical "
        "decisions that make this a *Wheel of Heaven* translation rather than a generic one).\n\n"
        "## Columns\n\n"
        "`ref`, `chapter`, `verse`, `original` (source script), `original_lang`, "
        "`transliteration`, `english` (WoH translation), `reference_english` (aligned "
        "public-domain translation; empty where none is available), `reference_version`, "
        "`reference_license`, `commentary` (translator's note; populated only for verses the "
        "editor annotated), `glossary_refs`, `witness_primary`, `witness_secondary`.\n\n"
        + ref_section
        + "## Method & provenance\n\n"
        f"Produced under the Wheel of Heaven Translation Program (translator → editor → "
        f"reviewer → human sign-off).\n- **Review status:** {review}.\n\n"
        + (f"**Source:** {provenance}\n\n" if provenance else "")
        + "## License & citation\n\n"
        "The Wheel of Heaven layer — source pointing, English translation, per-verse commentary, "
        "and glossary — is dedicated to the public domain under **CC0-1.0**. "
        + (f"The bundled `reference_english` column is *{ref_ver}*, itself in the **{ref_lic}** "
           "and carrying no additional restrictions. " if has_ref else "")
        + "Documentation and the reading edition: "
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
    ref_map, ref_ver, ref_lic, ref_status = load_reference(slug)
    rows = rows_for(bd, meta, (ref_map, ref_ver, ref_lic))
    if not any(r["english"].strip() for r in rows):
        print(f"  · {slug}: SKIPPED — 0 translated verses (stub or source-only)")
        return 0
    gpath = bd / "_translation-glossary.json"
    gloss = json.load(open(gpath, encoding="utf-8")) if gpath.exists() else {}
    if isinstance(gloss, dict):
        gloss.pop("$schema", None)  # broken relative ref, meaningless off-repo
    n_gloss = len(glossary_terms(gloss))
    n_ref = sum(1 for r in rows if r["reference_english"].strip())

    out = DIST / slug
    out.mkdir(parents=True, exist_ok=True)
    with open(out / f"{slug}.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(out / "glossary.json", "w", encoding="utf-8") as fh:
        json.dump(gloss, fh, ensure_ascii=False, indent=2)
    (out / "README.md").write_text(
        card(slug, meta, len(rows), n_gloss, review_status(bd, meta),
             ref_ver, ref_lic, ref_status, n_ref), encoding="utf-8")
    filled = sum(1 for r in rows if r["english"].strip())
    ref_note = (f", {n_ref} referenced ({ref_ver})" if n_ref
                else f", no reference [{ref_status}]")
    print(f"  ✓ {slug}: {len(rows)} verses ({filled} with English), {n_gloss} glossary entries"
          f"{ref_note} → dist-hf/{slug}/")
    return len(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", metavar="SLUG")
    args = ap.parse_args()
    books = [args.only] if args.only else discover_books()
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
