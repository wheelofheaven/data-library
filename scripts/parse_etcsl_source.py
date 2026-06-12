#!/usr/bin/env python3
r"""Parse an ETCSL composite/critical text page into a WoH source-sux-N.json.

ETCSL (etcsl.orinst.ox.ac.uk) renders each line of a composition as an
HTML table row: the line number + an anchor (`c554.N`), then a cell of
glossed `<span onMouseover="doTooltip(event, 'lemma (POS) gloss')">word</span>`
tokens. Manuscript variants appear in `{...}` with a "N mss. have
instead:" note; citations appear as a trailing `(Cited in ...)` note.

This script reproduces the transliteration convention already used by
the project's Sumerian sources (e.g. enki-and-ninmah-woh/source-sux-1.json):

  - subscripts (`<sub>3</sub>`) → inline digits  (e3, du7, šag4)
  - determinatives (`<sup>d</sup>`) → caret prefix (^den-lil2, ^ĝišal-e)
  - manuscript variants kept in `{...}`; the "N mss." note reduced to `()`
  - special letters via HTML entities → Unicode (ĝ, š, ḫ)
  - editorial sigla preserved verbatim ([...] restoration, /...\ damage, […] lacuna)
  - per-token {translit, lemma, pos, gloss} captured from the tooltip
  - trailing "(Cited in ...)" apparatus moved to the line's notes[]

Usage:
  python parse_etcsl_source.py <html_file> <anchor_prefix> <book_slug> <code> <composition_n> <out_json>
  e.g. python parse_etcsl_source.py /tmp/soth_crit.html c554 song-of-the-hoe-woh SOTH-WOH 1 \
         song-of-the-hoe-woh/source-sux-1.json
"""

import html
import json
import re
import sys


def clean_fragment(frag: str) -> str:
    """Convert an inner-HTML fragment of transliteration to plain text,
    honouring the project's sub/sup/entity conventions."""
    # superscripts (determinatives) → caret prefix
    frag = re.sub(r"<sup>(.*?)</sup>", r"^\1", frag, flags=re.DOTALL)
    # subscripts → inline digit/text
    frag = re.sub(r"<sub>(.*?)</sub>", r"\1", frag, flags=re.DOTALL)
    # drop the gloss/proper wrapper spans (keep inner text)
    frag = re.sub(r"<span\b[^>]*>", "", frag)
    frag = frag.replace("</span>", "")
    # any stray anchors → keep their text
    frag = re.sub(r"<a\b[^>]*>", "", frag)
    frag = frag.replace("</a>", "")
    frag = html.unescape(frag)
    return frag


def parse_tokens(cell_html: str):
    """Extract {translit, lemma, pos, gloss} for each glossed word."""
    tokens = []
    for tip, inner in re.findall(
        r"doTooltip\(event, '(.*?)'\)\"[^>]*>(.*?)</span>", cell_html, flags=re.DOTALL
    ):
        translit = clean_fragment(inner).strip()
        m = re.match(r"^(.*?)\s*\((.*?)\)\s*(.*)$", tip, flags=re.DOTALL)
        if m:
            lemma = clean_fragment(m.group(1)).strip()
            pos = html.unescape(m.group(2)).strip()
            gloss = clean_fragment(m.group(3)).strip()
        else:
            lemma, pos, gloss = clean_fragment(tip).strip(), "", ""
        tokens.append(
            {"translit": translit, "lemma": lemma, "pos": pos, "gloss": gloss}
        )
    return tokens


def parse_line_translit(cell_html: str):
    """Build the full-line transliteration string and pull out the
    trailing citation apparatus into a note (if present)."""
    notes = []
    # Extract + remove the trailing "(Cited in ...)" parenthetical note.
    def _grab_citation(m):
        note_html = m.group(1)
        note_text = clean_fragment(note_html).strip()
        notes.append(note_text)
        return ""

    cell = re.sub(
        r"\(\s*<span class=\"note\">(Cited in.*?)</span>\s*\)",
        _grab_citation,
        cell_html,
        flags=re.DOTALL,
    )
    # Reduce in-line "N mss. have instead:" variant notes to an empty marker,
    # matching the existing {() variant} convention.
    cell = re.sub(
        r"<span class=\"note\">[^<]*?(?:have instead|ms\.|mss\.)[^<]*?</span>",
        "",
        cell,
        flags=re.DOTALL,
    )
    translit = clean_fragment(cell)
    # tidy whitespace (collapse runs, fix space-before-brace artefacts)
    translit = re.sub(r"[ \t]+", " ", translit).strip()
    translit = translit.replace("( )", "()")
    return translit, notes


def main():
    html_file, prefix, slug, code, comp_n, out = sys.argv[1:7]
    raw = open(html_file, encoding="utf-8").read()

    # Each line: <a name='PREFIX.N'></a> in a row; the content cell is the
    # second <td> of that row. Split on the line anchors.
    row_re = re.compile(
        r"<a name='" + re.escape(prefix) + r"\.([0-9A-Za-z.]+)'></a>\s*</td>\s*<td>(.*?)</td>\s*</tr>",
        re.DOTALL,
    )
    lines = []
    for n_str, cell in row_re.findall(raw):
        translit, notes = parse_line_translit(cell)
        tokens = parse_tokens(cell)
        entry = {
            "n": n_str,
            "refId": f"{code}-{comp_n}:{n_str}",
            "translit": translit,
            "tokens": tokens,
        }
        if notes:
            entry["notes"] = notes
        lines.append(entry)

    # Renumber `n` to ints where the anchor is a bare integer (most lines).
    for ln in lines:
        if re.fullmatch(r"[0-9]+", ln["n"]):
            ln["n"] = int(ln["n"])

    doc = {
        "schemaVersion": 2,
        "bookSlug": slug,
        "composition": int(comp_n) if comp_n.isdigit() else comp_n,
        "source": {
            "type": "sumerian-composite",
            "versionTitle": "ETCSL composite text",
            "license": "ETCSL terms (scholarly use; © The ETCSL project, University of Oxford) — see book licensing note",
            "versionSource": "https://etcsl.orinst.ox.ac.uk/",
            "fetchedFrom": "ETCSL critical/composite display (display=Crit)",
            "fetchedAt": "2026-06-11",
        },
        "lines": lines,
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"wrote {out}: {len(lines)} lines")


if __name__ == "__main__":
    main()
