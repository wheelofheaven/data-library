#!/usr/bin/env python3
"""
translit_to_cuneiform.py — back-render Unicode cuneiform from ETCSL transliteration.

For each line in a data-library chapter file (lines-shape or segments-shape),
populates two fields in-place:
  - cuneiform: Unicode cuneiform string built from OGSL sign-reading lookups
  - cuneiform_confidence: "full" | "partial" | "low"

The cuneiform is a back-derivation from the composite transliteration, not an
attested witness — ETCSL composites have no canonical cuneiform "score". A
confidence flag marks lines where annotation noise (lacunae, uncertain
readings, sign-names instead of readings) reduced coverage.

OGSL source: data-library/scripts/data/osl.asl (CC0, ORACC).

Usage:
    python3 translit_to_cuneiform.py --slug enki-and-ninmah-woh
    python3 translit_to_cuneiform.py --slug flood-story-woh --dry-run
    python3 translit_to_cuneiform.py --all
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent  # data-library/
OSL_PATH = Path(__file__).resolve().parent / "data" / "osl.asl"

# ETCSL writes subscript indices as ASCII digits (dim2). OGSL stores them as
# Unicode subscripts (dim₂). Both directions of normalization needed.
ASCII_TO_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUB_TO_ASCII = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")

# ETCSL uses ĝ (Latin small letter g with circumflex) for the Sumerian velar
# nasal; OGSL uses ŋ (Latin small letter eng) — same phoneme, different
# transliteration convention. Normalize ETCSL → OGSL form for lookup.
ETCSL_TO_OGSL = str.maketrans({"ĝ": "ŋ", "Ĝ": "Ŋ"})

# ETCSL-style determinative markers — single letters / short tokens that
# stand for classifier signs preceding the next morpheme. Detected via the
# `^` superscript marker (e.g. `^d`, `^lu2`, `^gish`, `^ki` for postfix).
KNOWN_DETERMINATIVES = {
    "d", "f", "m", "lu2", "ki", "dug", "gish", "ŋish", "gesz", "ŋesz",
    "tug2", "kush", "kuš", "udu", "urudu", "mush", "muš", "mul", "im",
    "iri", "uru", "uru2", "na4", "še", "sze", "munus", "id2", "i7",
    "ŋes", "geš",
}


def parse_osl(path: Path):
    """Return (readings, sign_names) lookup dicts.

    readings:   lowercase reading (ASCII-subscript form) -> cuneiform char
    sign_names: SIGN_NAME (as written in @sign) -> cuneiform char
    """
    readings = {}
    sign_names = {}
    cur_sign = None
    cur_cun = None
    skipped_no_cun = 0

    with path.open() as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.startswith("@sign "):
                cur_sign = line[len("@sign "):].strip()
                cur_cun = None
            elif line.startswith("@end sign"):
                if cur_sign and not cur_cun:
                    skipped_no_cun += 1
                cur_sign = None
                cur_cun = None
            elif cur_sign and line.startswith("@ucun"):
                # Format: "@ucun\t𒀭"  (tab + character)
                parts = line.split(None, 1)
                if len(parts) == 2:
                    cur_cun = parts[1].strip()
                    sign_names.setdefault(cur_sign, cur_cun)
            elif cur_sign and cur_cun and line.startswith("@v"):
                # Format: "@v\treading" or "@v\t%lang reading"
                parts = line.split(None, 1)
                if len(parts) != 2:
                    continue
                rest = parts[1].strip()
                # Skip language-tagged readings (Akkadian etc.) — we render
                # Sumerian text, so Akkadian readings of the same sign would
                # produce wrong cuneiform in this context.
                if rest.startswith("%") and not rest.startswith("%sux"):
                    continue
                if rest.startswith("%sux "):
                    rest = rest[len("%sux "):].strip()
                # Strip uncertainty marker `?` at end.
                rest = rest.rstrip("?")
                # Skip placeholder readings (xₓ subscript means unknown index).
                if rest.endswith("ₓ") or rest.endswith("x"):
                    continue
                # Normalize Unicode subscripts to ASCII (ETCSL convention).
                ascii_form = rest.translate(SUB_TO_ASCII).lower()
                # Lowest-index winning would matter; here we only set first.
                readings.setdefault(ascii_form, cur_cun)

    return readings, sign_names, skipped_no_cun


# Outer-wrapper characters that signal annotations rather than text content.
OUTER_STRIPPABLE = "[](){}/<>\\"
# Inner-noise characters we strip before lookup.
INNER_STRIPPABLE = "*"


def normalize_morpheme(morph: str):
    """Return (clean_morph, has_annotation).

    Strips wrapping brackets/slashes/etc. and records whether any annotation
    was present so the caller can flag confidence.
    """
    annotation = False
    s = morph
    while s and s[0] in OUTER_STRIPPABLE:
        s = s[1:]
        annotation = True
    while s and s[-1] in OUTER_STRIPPABLE:
        s = s[:-1]
        annotation = True
    # Also strip inner noise that doesn't affect lookup.
    for ch in INNER_STRIPPABLE:
        if ch in s:
            s = s.replace(ch, "")
            annotation = True
    # Trim trailing uncertainty marker `?` if present.
    if s.endswith("?"):
        s = s[:-1]
        annotation = True
    return s, annotation


def split_morphemes(word: str):
    """Split a hyphen-connected ETCSL word into morphemes, surfacing the
    superscript-determinative marker `^` as a separate prefix on the next
    morpheme.

    Example: '^dnin-maḫ' -> [('^', 'd'), ('', 'nin'), ('', 'maḫ')]
             except we collapse the determinative as part of the next:
             [('det', 'd'), ('plain', 'nin'), ('plain', 'maḫ')]

    Returns a list of (kind, morph) tuples where kind is 'det' or 'plain'.
    """
    out = []
    # First split on hyphens.
    raw_parts = word.split("-")
    for part in raw_parts:
        if not part:
            continue
        # A `^X` prefix marks a superscript-determinative. May be followed
        # by additional text fused into the same morpheme: `^dnin` =
        # determinative `d` + reading `nin`.
        if part.startswith("^"):
            # Strip the `^` and decide how much is the determinative.
            body = part[1:]
            # Try matching known determinatives at the start.
            matched = None
            for det in sorted(KNOWN_DETERMINATIVES, key=len, reverse=True):
                if body.startswith(det):
                    matched = det
                    break
            if matched and len(body) > len(matched):
                out.append(("det", matched))
                out.append(("plain", body[len(matched):]))
            elif matched:
                out.append(("det", matched))
            else:
                # Unknown determinative — render the body as plain to avoid
                # losing content; caller will mark as partial via annotation.
                out.append(("plain", body))
        else:
            out.append(("plain", part))
    return out


def translate_word(word: str, readings: dict, sign_names: dict):
    """Translate one whitespace-delimited ETCSL word to cuneiform.

    Returns (cuneiform_str, stats_dict) where stats are per-morpheme counts:
    mapped, unmapped, annotated.
    """
    stats = {"mapped": 0, "unmapped": 0, "annotated": 0}
    out_chars = []

    # If the whole word is a gap marker, surface as-is and bail.
    if word in ("[…]", "(…)", "[...]", "(...)", "[…]>", "[...]>", "…", "...", "<...>"):
        stats["annotated"] += 1
        return "", stats

    # If the word is a single ALL-CAPS sign-name (possibly compound with `.`),
    # try sign_names lookup directly. ETCSL convention for sign-names without
    # certain readings.
    if word.isupper() and word.replace(".", "").replace("X", "").isalnum():
        parts = word.split(".")
        all_mapped = True
        sub_out = []
        for p in parts:
            char = sign_names.get(p) or sign_names.get(p.upper())
            if char:
                sub_out.append(char)
                stats["mapped"] += 1
            else:
                stats["unmapped"] += 1
                all_mapped = False
                sub_out.append("")
        if all_mapped:
            return "".join(sub_out), stats
        # Fall through to morpheme handling if mixed.

    morphemes = split_morphemes(word)
    for kind, morph in morphemes:
        clean, annotated = normalize_morpheme(morph)
        if annotated:
            stats["annotated"] += 1
        if not clean:
            # Pure annotation token (e.g. just brackets) — nothing to render.
            continue
        # `X` is the ETCSL marker for "broken sign of unknown reading"
        if clean == "x" or clean.upper() == "X":
            stats["unmapped"] += 1
            continue
        # Determinative lookup uses the reading just like a normal morpheme.
        ascii_form = clean.translate(SUB_TO_ASCII).translate(ETCSL_TO_OGSL).lower()
        char = readings.get(ascii_form)
        if not char:
            # Try uppercase as a sign-name fallback.
            char = sign_names.get(clean.upper())
        if char:
            out_chars.append(char)
            stats["mapped"] += 1
        else:
            stats["unmapped"] += 1
    return "".join(out_chars), stats


def translate_line(translit: str, readings: dict, sign_names: dict):
    """Translate one ETCSL line. Returns (cuneiform_str, confidence)."""
    if not translit:
        return "", "low"
    # Strip line-continuation marker `>` at end of line (used by ETCSL when a
    # transcribed line wraps; not meaningful to the cuneiform).
    cleaned = translit.rstrip(">").strip()
    words = cleaned.split()
    word_chunks = []
    total = {"mapped": 0, "unmapped": 0, "annotated": 0}
    for w in words:
        chunk, stats = translate_word(w, readings, sign_names)
        # Always append, even when chunk is empty, so the cuneiform word
        # count stays parallel to the transliteration. The interlinear
        # renderer zips the two arrays by index; an empty cuneiform slot
        # under a `[…]` or unmapped sign-name reads as a gap-marker.
        word_chunks.append(chunk)
        for k in total:
            total[k] += stats[k]
    cun = " ".join(word_chunks)  # plain space — renderer zips word-pairs on split(pat=" ")
    # Confidence scoring.
    morpheme_total = total["mapped"] + total["unmapped"]
    if morpheme_total == 0:
        return "", "low"
    mapped_ratio = total["mapped"] / morpheme_total
    if mapped_ratio >= 0.95 and total["annotated"] == 0:
        confidence = "full"
    elif mapped_ratio >= 0.6:
        confidence = "partial"
    else:
        confidence = "low"
    return cun, confidence


def process_chapter(chapter_path: Path, readings, sign_names, dry_run=False):
    data = json.loads(chapter_path.read_text(encoding="utf-8"))
    confidence_counts = Counter()
    line_count = 0

    def process_lines(lines):
        nonlocal line_count
        for line in lines:
            translit = line.get("translit") or line.get("text") or ""
            cun, conf = translate_line(translit, readings, sign_names)
            line["cuneiform"] = cun
            line["cuneiform_confidence"] = conf
            confidence_counts[conf] += 1
            line_count += 1

    if "lines" in data:
        process_lines(data["lines"])
    elif "segments" in data:
        for seg in data["segments"]:
            if "lines" in seg:
                process_lines(seg["lines"])
    elif "paragraphs" in data:
        # Paragraphs-shape books (Hebrew/Greek) don't get cuneiform; skip.
        return None, line_count
    else:
        return None, 0

    if not dry_run:
        chapter_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return confidence_counts, line_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", action="append", default=[],
                        help="Book slug (repeatable). Default: all lines/segments books.")
    parser.add_argument("--all", action="store_true",
                        help="Process all lines/segments books in data-library.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Compute stats but don't write changes.")
    args = parser.parse_args()

    print(f"Loading OGSL from {OSL_PATH}…")
    readings, sign_names, no_cun = parse_osl(OSL_PATH)
    print(f"  parsed {len(sign_names)} signs, {len(readings)} reading values, "
          f"{no_cun} signs had no @ucun (skipped)")

    if args.all:
        slugs = []
        for d in sorted(LIB.iterdir()):
            if not d.is_dir() or d.name.startswith("."):
                continue
            meta = d / "_meta.json"
            if not meta.exists():
                continue
            for ch in sorted(d.glob("chapter-*.json")):
                if "editor-report" in ch.name or "signoff" in ch.name:
                    continue
                slugs.append((d.name, ch))
    elif args.slug:
        slugs = []
        for s in args.slug:
            book_dir = LIB / s
            if not book_dir.exists():
                print(f"  WARN: {s} not found", file=sys.stderr)
                continue
            for ch in sorted(book_dir.glob("chapter-*.json")):
                if "editor-report" in ch.name or "signoff" in ch.name:
                    continue
                slugs.append((s, ch))
    else:
        parser.error("provide --slug or --all")

    grand_total = Counter()
    grand_lines = 0
    for slug, ch in slugs:
        result, count = process_chapter(ch, readings, sign_names, dry_run=args.dry_run)
        if result is None:
            print(f"  skip {slug}/{ch.name} (not a lines/segments shape)")
            continue
        grand_total.update(result)
        grand_lines += count
        pct = lambda k: 100.0 * result[k] / count if count else 0
        print(f"  {slug}/{ch.name}: {count} lines "
              f"[full={result['full']} ({pct('full'):.0f}%) "
              f"partial={result['partial']} ({pct('partial'):.0f}%) "
              f"low={result['low']} ({pct('low'):.0f}%)]")

    if grand_lines:
        print(f"\nTotal: {grand_lines} lines across {len(slugs)} chapter file(s)")
        for k in ("full", "partial", "low"):
            print(f"  {k}: {grand_total[k]} ({100.0*grand_total[k]/grand_lines:.1f}%)")
    if args.dry_run:
        print("\n(dry run — no files written)")


if __name__ == "__main__":
    main()
