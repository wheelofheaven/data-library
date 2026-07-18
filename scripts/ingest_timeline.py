#!/usr/bin/env python3
"""Ingest Wheel of Heaven Timeline prose (.md) into pipeline chapter JSON.

The Timeline book lives as scholarly prose-essay markdown in the content
submodule (`content/timeline/*.md`), NOT as a data-library verse book. This
adapter derives `data-library/wheel-of-heaven-timeline/chapter-N.json` in the
exact shape `generate_audio.py` consumes, so the Timeline can ride the same
audio + cinematic pipeline as the Library books — as an audiobook.

The `.md` files stay the human-edited source of truth; the JSON is a derived
artifact (regenerate on content change). English-only `text` for now; i18n comes
from the existing woh-fan-* timeline translations later.

Gradient casting (audiobook-first):
  - section headings (## / ###)          -> kind=title,     speaker=Narrator
  - paired {% scripture %}English{% end %} -> kind=scripture, speaker=Scripture
  - everything else                        -> kind=body,      speaker=Narrator

Known gap (surfaced, not silently resolved): self-closing
{{ scripture(...translit="...") }} verses carry only transliterated Hebrew as an
arg; their English is rendered from data at build time and is absent from the
markdown. v1 DROPS them and records their refs in the diagnostics report. See
`.claude/plans/timeline-audiobook.md`.

Usage:
    ingest_timeline.py age-of-taurus                  # one chapter
    ingest_timeline.py --all                          # whole book + _meta.json
    ingest_timeline.py age-of-taurus --dry-run        # print diagnostics only
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve()
REPO = HERE.parents[2]  # .../wheelofheaven
DATA_LIBRARY = HERE.parents[1]  # .../data-library (home of the verse books)
DEFAULT_SRC = REPO / "www.wheelofheaven.world" / "content" / "timeline"
DEFAULT_OUT = REPO / "data-library" / "wheel-of-heaven-timeline"

BOOK_SLUG = "wheel-of-heaven-timeline"
BOOK_CODE = "WOHT"

# Reading order: prologue, the 12 ages earliest-first (by start_year), epilogue.
ORDER = [
    "preamble",
    "in-the-beginning",
    "age-of-capricorn",
    "age-of-sagittarius",
    "age-of-scorpio",
    "age-of-libra",
    "age-of-virgo",
    "age-of-leo",
    "age-of-cancer",
    "age-of-gemini",
    "age-of-taurus",
    "age-of-aries",
    "age-of-pisces",
    "age-of-aquarius",
    # NOTE: `chronology` is intentionally excluded — it's a data-driven visual
    # reference page (timeline-chronology.html), not a narratable chapter.
    "the-wheel-keeps-turning",
]
CHAP_N = {slug: i + 1 for i, slug in enumerate(ORDER)}

# --- sentinels: mark paired-scripture English so it survives cleaning and can
#     later be split into its own Scripture-voiced paragraph. ---
S_OPEN, S_CLOSE = "\x00SCRIP\x00", "\x00/SCRIP\x00"

# paired {% scripture(...) %}English{% end %}  -> keep English, wrapped
RE_SCRIPTURE_PAIRED = re.compile(
    r"\{%\s*scripture\([^%]*?%\}(.*?)\{%\s*end\s*%\}", re.DOTALL)
# self-closing {{ scripture(...) }} -> drop (record ref)
RE_SCRIPTURE_SELF = re.compile(r"\{\{\s*scripture\((?P<args>[^}]*?)\}\}")
# paired {% footnote(...) %}...{% end %} -> drop entirely (not spoken)
RE_FOOTNOTE_PAIRED = re.compile(
    r"\{%\s*footnote\([^%]*?%\}.*?\{%\s*end\s*%\}", re.DOTALL)
# paired keep-label shortcodes {% wiki|libref(...) %}LABEL{% end %} -> LABEL
RE_KEEP_LABEL = re.compile(
    r"\{%\s*(?:wiki|libref)\([^%]*?%\}(.*?)\{%\s*end\s*%\}", re.DOTALL)
# inline drops {{ cite|figure|footnote(...) }}
RE_INLINE_DROP = re.compile(r"\{\{\s*(?:cite|figure|footnote)\([^}]*?\}\}")
# any stray shortcode leftover (opening/closing/self)
RE_STRAY = re.compile(r"\{[%{].*?[%}]\}")
# Hebrew-script runs incl. combining points and maqaf; keep the (*translit*)
RE_HEBREW = re.compile(r"[֐-׿יִ-ﭏ]+")

RE_ARG = lambda name: re.compile(rf"{name}\s*=\s*[\"']?([^,\"')]+)")


def strip_frontmatter(text: str) -> tuple[dict, str]:
    if not text.lstrip().startswith("+++"):
        return {}, text
    parts = text.split("+++", 2)
    if len(parts) != 3:
        return {}, text
    try:
        fm = tomllib.loads(parts[1])
    except tomllib.TOMLDecodeError:
        fm = {}
    return fm, parts[2]


def scripture_args(args: str) -> tuple[str | None, str | None, str | None]:
    def g(n):
        m = RE_ARG(n).search(args)
        return m.group(1).strip() if m else None
    return g("book"), g("chapter"), g("verse")


def scripture_ref(args: str) -> str:
    book, ch, v = scripture_args(args)
    return f"{book or '?'} {ch or '?'}:{v or '?'}"


# cache: (book, chapter) -> {verse_n: english} ; None marks a missing book/chapter
_verse_cache: dict[tuple[str, int], dict | None] = {}


def _load_verse_book(book: str, chapter: int) -> dict | None:
    """Load a data-library verse book chapter as {verse_n: english}.

    English resolution handles both book families:
      - `-woh` books carry the WoH translation in i18n.en (text = original script)
      - plain source books carry English in `text` (i18n.en empty)
    so english = i18n.en or text.
    """
    key = (book, chapter)
    if key in _verse_cache:
        return _verse_cache[key]
    path = DATA_LIBRARY / book / f"chapter-{chapter}.json"
    if not path.exists():
        _verse_cache[key] = None
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        _verse_cache[key] = None
        return None
    verses: dict[int, str] = {}
    for p in data.get("paragraphs", []):
        en = ((p.get("i18n") or {}).get("en") or "").strip() or (p.get("text") or "").strip()
        if p.get("n") is not None and en:
            verses[int(p["n"])] = en
    _verse_cache[key] = verses
    return verses


def resolve_verse(book: str | None, chapter: str | None, verse: str | None) -> str | None:
    """English text for a scripture ref, trying the named book then ±-woh."""
    if not (book and chapter and verse):
        return None
    try:
        ch, v = int(chapter), int(verse)
    except ValueError:
        return None
    candidates = [book]
    if book.endswith("-woh"):
        candidates.append(book[:-4])
    else:
        candidates.append(f"{book}-woh")
    for cand in candidates:
        verses = _load_verse_book(cand, ch)
        if verses and v in verses:
            return verses[v]
    return None


def clean(body: str, diag: dict) -> str:
    """Resolve shortcodes + strip Hebrew/markdown. Preserves lines + headings."""
    # paired scripture -> sentinel-wrapped English (spoken in Scripture voice)
    def _paired(m):
        diag["scripture_paired"] += 1
        return f"{S_OPEN}{m.group(1).strip()}{S_CLOSE}"
    body = RE_SCRIPTURE_PAIRED.sub(_paired, body)

    # self-closing scripture -> resolve English from the data-library verse
    # books and voice it as Scripture; drop + record ref if unresolvable.
    def _self(m):
        args = m.group("args")
        english = resolve_verse(*scripture_args(args))
        if english:
            diag["scripture_resolved"] += 1
            return f"{S_OPEN}{english}{S_CLOSE}"
        diag["scripture_dropped"].append(scripture_ref(args))
        return ""
    body = RE_SCRIPTURE_SELF.sub(_self, body)

    body = RE_FOOTNOTE_PAIRED.sub("", body)
    body = RE_KEEP_LABEL.sub(r"\1", body)
    body = RE_INLINE_DROP.sub("", body)
    body = RE_STRAY.sub("", body)

    def _heb(m):
        diag["hebrew_runs"] += 1
        return ""
    body = RE_HEBREW.sub(_heb, body)

    # markdown: links -> label, bold/italic/code strip
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    body = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", body)
    body = re.sub(r"_([^_]+)_", r"\1", body)
    body = body.replace("`", "")
    # tidy: collapse spaces, fix " (" left by stripped Hebrew, orphan punctuation
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\(\s+", "(", body)
    body = re.sub(r"\s+([,.;:])", r"\1", body)
    return body


RE_HEADING = re.compile(r"^(#{2,6})\s+(.*)$")
RE_ENUM = re.compile(r"^(?:[IVXLC]+|[0-9]+)(?:\.[0-9]+)*\.\s*")  # "I. " / "X.1. "


def to_paragraphs(cleaned: str, diag: dict) -> list[dict]:
    paras: list[dict] = []
    n = 0

    def emit(text: str, speaker: str, kind: str):
        nonlocal n
        text = re.sub(r"\s+", " ", text).strip()
        if not text:
            return
        n += 1
        paras.append({"n": n, "speaker": speaker, "kind": kind, "text": text})

    for block in re.split(r"\n\s*\n", cleaned):
        block = block.strip()
        if not block:
            continue
        hm = RE_HEADING.match(block)
        if hm:
            title = RE_ENUM.sub("", hm.group(2).strip())
            emit(title, "Narrator", "title")
            diag["titles"] += 1
            continue
        # split prose block on scripture sentinels -> alternating voices
        segments = re.split(f"({re.escape(S_OPEN)}.*?{re.escape(S_CLOSE)})",
                            block, flags=re.DOTALL)
        for seg in segments:
            if not seg.strip():
                continue
            if seg.startswith(S_OPEN):
                inner = seg[len(S_OPEN):-len(S_CLOSE)]
                emit(inner, "Scripture", "scripture")
                diag["scripture"] += 1
            else:
                emit(seg, "Narrator", "body")
                diag["body"] += 1
    return paras


def ingest_chapter(slug: str, src_dir: Path) -> tuple[dict, dict]:
    path = src_dir / f"{slug}.md"
    raw = path.read_text(encoding="utf-8")
    fm, body = strip_frontmatter(raw)
    diag = {"slug": slug, "titles": 0, "body": 0, "scripture": 0,
            "scripture_paired": 0, "scripture_resolved": 0, "hebrew_runs": 0,
            "scripture_dropped": []}
    paras = to_paragraphs(clean(body, diag), diag)

    extra = fm.get("extra", {})
    chapter = {
        "n": CHAP_N.get(slug, 0),
        "bookSlug": BOOK_SLUG,
        "bookCode": BOOK_CODE,
        "refId": BOOK_CODE,
        "slug": slug,
        "title": fm.get("title", slug),
        "extra": {k: extra.get(k) for k in
                  ("symbol", "color", "start_year", "end_year")
                  if extra.get(k) is not None},
        "paragraphs": paras,
    }
    diag["paragraphs"] = len(paras)
    return chapter, diag


def print_diag(d: dict) -> None:
    dropped = d["scripture_dropped"]
    print(f"  {d['slug']:26s} ch{CHAP_N.get(d['slug'],0):<2d} "
          f"{d['paragraphs']:3d} paras "
          f"(title {d['titles']}, body {d['body']}, scripture {d['scripture']}) "
          f"· Hebrew stripped {d['hebrew_runs']} "
          f"· verses resolved {d['scripture_resolved']}, unresolved {len(dropped)}")
    if dropped:
        print(f"      unresolved refs: {', '.join(dropped[:8])}"
              + (f" … (+{len(dropped)-8} more)" if len(dropped) > 8 else ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?", help="chapter slug (e.g. age-of-taurus)")
    ap.add_argument("--all", action="store_true", help="ingest the whole book")
    ap.add_argument("--src", type=Path, default=DEFAULT_SRC)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--dry-run", action="store_true",
                    help="print diagnostics; write nothing")
    args = ap.parse_args()

    if args.all:
        slugs = ORDER
    elif args.slug:
        slugs = [args.slug]
    else:
        ap.error("give a chapter slug or --all")

    if not args.dry_run:
        args.out.mkdir(parents=True, exist_ok=True)

    print(f"Ingesting {len(slugs)} chapter(s) from {args.src}")
    meta_chapters = []
    for slug in slugs:
        chapter, diag = ingest_chapter(slug, args.src)
        print_diag(diag)
        meta_chapters.append({"n": chapter["n"], "slug": slug,
                              "file": f"chapter-{chapter['n']}.json",
                              "title": chapter["title"],
                              "paragraphs": diag["paragraphs"]})
        if not args.dry_run:
            out = args.out / f"chapter-{chapter['n']}.json"
            out.write_text(json.dumps(chapter, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")

    if args.all and not args.dry_run:
        meta = {
            "slug": BOOK_SLUG, "code": BOOK_CODE, "refId": BOOK_CODE,
            "titles": {"en": "The Wheel of Heaven Timeline"},
            "primaryLang": "en", "schema": ["book", "chapters", "paragraphs"],
            "chapterCount": len(meta_chapters),
            "paragraphCount": sum(c["paragraphs"] for c in meta_chapters),
            "chapterFiles": sorted(meta_chapters, key=lambda c: c["n"]),
        }
        (args.out / "_meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote _meta.json — {meta['chapterCount']} chapters, "
              f"{meta['paragraphCount']} paragraphs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
