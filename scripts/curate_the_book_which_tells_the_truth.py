#!/usr/bin/env python3
"""Curate the canonical JSON for The Book Which Tells The Truth."""

from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


BOOK_SLUG = "the-book-which-tells-the-truth"
BOOK_CODE = "TBWTT"
LANG_KEYS = ("en", "de", "es", "ru", "ja", "zh")

ARTIFACT_TEXTS = {
    "LA ToUR DE BABEL",
    "SoDoME ET GoMoRRHE",
    "MoÏSE",
    "LES TRoMPETTES DE JÉRICHo",
    "SAMSoN LE TÉLÉPATHE",
    "LA PREMIÈRE RÉSIDENCE PoUR L’ACCUEIL DES ELoHIM",
    "LA MULTIPLICATIoN DES PAINS",
    "LES SoUCoUPES VoLANTES D’ÉZÉCHIEL",
    "LES HoMMES NE PoUVAIENT PAS CoMPRENDRE",
    "LA CoNCEPTIoN",
    "L’INITIATIoN",
    "LA FIN DU MoNDE",
    "1946, AN 1 DE L’ÈRE NoUVELLE",
    "LA CRÉATIoN DE L’ÉTAT D’ISRAËL",
    "À L’oRIGINE DE ToUTES LES RELIGIoNS",
    "L’HoMME: UNE MALADIE DE L’UNIVERS",
    "L’ÉVoLUTIoN: UN MYTHE",
    "GÉNIoCRATIE",
    "GoUVERNEMENT MoNDIAL",
    "VoTRE MISSIoN",
    "LES NoUVEAUX CoMMANDEMENTS",
    "LES BoMBES AToMIQUES",
    "LA SURPoPULATIoN",
    "L’ÉDUCATIoN CHIMIQUE",
    "MoUVEMENT RAÉLIEN",
    "LES ELoHIM",
}

CAPTION_PREFIXES = (
    "Raël, photographié",
    "Un dessin d’architecte",
    "Un modèle à l’échelle",
    "Raël affirme qu’",
    "1N.D.L.R.",
)

HEADING_NORMALIZATIONS = {
    "Le déluge": "Le déluge",
    "La Tour de babel": "La Tour de Babel",
    "sodome et Gomorrhe": "Sodome et Gomorrhe",
    "Le sacrifice d’abraham": "Le sacrifice d’Abraham",
    "moïse": "Moïse",
    "Les trompettes de Jéricho": "Les trompettes de Jéricho",
    "samson le télépathe": "Samson le télépathe",
    "La première résidence pour l’accueil des elohim": "La première résidence pour l’accueil des Elohim",
    "elie le messager": "Élie le messager",
    "La multiplication des pains": "La multiplication des pains",
    "Les soucoupes volantes d’ezéchiel": "Les soucoupes volantes d’Ézéchiel",
    "Le jugement dernier": "Le jugement dernier",
    "satan": "Satan",
    "Les hommes ne pouvaient pas comprendre": "Les hommes ne pouvaient pas comprendre",
    "La conception": "La conception",
    "L’initiation": "L’initiation",
    "Les humanités parallèles": "Les humanités parallèles",
    "des miracles scientifiques": "Des miracles scientifiques",
    "mériter l’héritage": "Mériter l’héritage",
    "1946, an 1 de l’ère nouvelle": "1946, an 1 de l’ère nouvelle",
    "La fin de l’Église": "La fin de l’Église",
    "La création de l’État d’israël": "La création de l’État d’Israël",
    "Les erreurs de l’Église": "Les erreurs de l’Église",
    "a l’origine de toutes les religions": "À l’origine de toutes les religions",
    "L’homme : une maladie de l’univers": "L’homme : une maladie de l’univers",
    "L’évolution : un mythe": "L’évolution : un mythe",
    "Gouvernement mondial": "Gouvernement mondial",
    "Votre mission": "Votre mission",
    "Les bombes atomiques": "Les bombes atomiques",
    "La surpopulation": "La surpopulation",
    "Le secret de l’éternité": "Le secret de l’éternité",
    "L’éducation chimique": "L’éducation chimique",
    "mouvement Raélien": "Mouvement Raélien",
}

TEXT_REPLACEMENTS = {
    "Puy-de- Lassolas": "Puy-de-Lassolas",
    "embryon- naires": "embryonnaires",
    "mys- tifiant": "mystifiant",
    "semi- primitif": "semi-primitif",
    "som- met": "sommet",
    "rendez- vous": "rendez-vous",
    "s’ar- rêtait": "s’arrêtait",
    "émetteur- récepteur": "émetteur-récepteur",
    "équi- valent": "équivalent",
    "peut- être": "peut-être",
    "s’ap- parentant": "s’apparentant",
    "cer- tains": "certains",
    "radio- phoniques": "radiophoniques",
    "appren- dre": "apprendre",
    "faites- vous": "faites-vous",
    "ennuyez- vous": "ennuyez-vous",
    "eux- mêmes": "eux-mêmes",
    "peutêtre": "peut-être",
    "dixhuit": "dix-huit",
    "Ils n’amènerait": "Il n’amènerait",
    "Mouvement Raélien1": "Mouvement Raélien",
}

MANUAL_TEXT_FIXES = {
    (6, "Votre mouvement vous l’appellerez le MoUVEMENT"): (
        "Votre mouvement vous l’appellerez le Mouvement Raélien."
    ),
}

BACK_MATTER_START = "Tout lecteur qui souhaite contacter"

LOWER_RE = re.compile(r"^[a-zàâäçéèêëîïôöùûüÿœ]")
DIALOGUE_RE = re.compile(r"^[–—-]\s*")
SPACE_RE = re.compile(r"[ \t\r\n]+")


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_json_from_git(root: Path, relative_path: str, ref: str) -> Any:
    content = subprocess.check_output(
        ["git", "show", f"{ref}:{relative_path}"],
        cwd=root,
        text=True,
        encoding="utf-8",
    )
    return json.loads(content)


def write_json(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def normalize_text(text: str) -> str:
    text = SPACE_RE.sub(" ", text).strip()
    for source, target in TEXT_REPLACEMENTS.items():
        text = text.replace(source, target)
    return text


def is_artifact(text: str) -> bool:
    if text in ARTIFACT_TEXTS:
        return True
    return any(text.startswith(prefix) for prefix in CAPTION_PREFIXES)


def is_heading(text: str) -> bool:
    return text in set(HEADING_NORMALIZATIONS.values())


def starts_lower(text: str) -> bool:
    return bool(LOWER_RE.match(text))


def strip_dialogue_marker(text: str) -> tuple[str, bool]:
    stripped = DIALOGUE_RE.sub("", text, count=1)
    return stripped, stripped != text


def clean_initial_case(text: str) -> str:
    if text.startswith("oui,"):
        return "Oui," + text[4:]
    if text.startswith("on peut"):
        return "On peut" + text[7:]
    return text


def should_keep_boundary_hyphen(previous: str, current: str) -> bool:
    tail = previous.rsplit(" ", 1)[-1].lower()
    head = current.split(" ", 1)[0].lower()
    return (tail, head) in {
        ("avez-", "vous"),
        ("faites-", "vous"),
        ("ennuyez-", "vous"),
    }


def join_text(previous: str, current: str) -> str:
    if previous.endswith("-"):
        if should_keep_boundary_hyphen(previous, current):
            return previous + current
        return previous[:-1] + current
    return f"{previous} {current}"


def merge_i18n(previous: dict[str, Any], current: dict[str, Any]) -> None:
    if "i18n" not in current:
        return
    previous_i18n = previous.setdefault("i18n", {})
    for lang in LANG_KEYS:
        current_value = current.get("i18n", {}).get(lang)
        if not current_value:
            continue
        if previous_i18n.get(lang):
            previous_i18n[lang] = join_text(previous_i18n[lang], current_value)
        else:
            previous_i18n[lang] = current_value


def should_merge(chapter_n: int, previous: dict[str, Any], current: dict[str, Any]) -> bool:
    if previous.get("_heading") or current.get("_heading"):
        return False
    if current.get("_dialogue"):
        return False

    previous_text = previous["text"]
    current_text = current["text"]

    if previous_text.endswith("-"):
        return True

    if chapter_n == 7 and previous_text.endswith("?") and current_text.endswith("?"):
        return True

    if starts_lower(current_text):
        return not previous_text.endswith("?")

    return False


def build_paragraph(chapter_n: int, source: dict[str, Any]) -> dict[str, Any] | None:
    text = normalize_text(source["text"])
    text = MANUAL_TEXT_FIXES.get((chapter_n, text), text)
    text = HEADING_NORMALIZATIONS.get(text, text)

    if is_artifact(text):
        return None

    text, had_dialogue_marker = strip_dialogue_marker(text)
    text = clean_initial_case(text)

    paragraph = {
        "speaker": source.get("speaker"),
        "text": text,
        "_heading": is_heading(text),
        "_dialogue": had_dialogue_marker,
    }
    if "i18n" in source:
        paragraph["i18n"] = copy.deepcopy(source["i18n"])
    return paragraph


def assign_speakers(chapter_n: int, paragraphs: list[dict[str, Any]]) -> None:
    in_narrator_close = False

    for paragraph in paragraphs:
        text = paragraph["text"]

        if chapter_n == 1:
            paragraph["speaker"] = paragraph.get("speaker") or "Narrator"
            continue

        if paragraph.get("_heading"):
            paragraph["speaker"] = "Narrator"
            if chapter_n == 7 and text == "Mouvement Raélien":
                in_narrator_close = True
            continue

        if chapter_n == 7:
            if text.startswith("Alors le petit homme") or in_narrator_close:
                paragraph["speaker"] = "Narrator"
            elif text.startswith("Avant que nous nous quittions"):
                paragraph["speaker"] = "Yahweh"
            elif text.endswith("?"):
                paragraph["speaker"] = "Raël"
            else:
                paragraph["speaker"] = "Yahweh"
            continue

        if text.startswith("Le lendemain"):
            paragraph["speaker"] = "Narrator"
        elif text.startswith("Et il repartit"):
            paragraph["speaker"] = "Narrator"
        elif text.startswith("Le petit homme prit"):
            paragraph["speaker"] = "Narrator"
        else:
            paragraph["speaker"] = "Yahweh"


def finalize_paragraphs(chapter_n: int, paragraphs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    assign_speakers(chapter_n, paragraphs)
    finalized = []
    for index, paragraph in enumerate(paragraphs, start=1):
        clean = {
            "n": index,
            "speaker": paragraph["speaker"],
            "text": paragraph["text"],
        }
        if "i18n" in paragraph:
            clean["i18n"] = paragraph["i18n"]
        clean["refId"] = f"{BOOK_CODE}-{chapter_n}:{index}"
        finalized.append(clean)
    return finalized


def curate_chapter(chapter: dict[str, Any], stats: Counter[str]) -> dict[str, Any]:
    chapter_n = chapter["n"]
    curated: list[dict[str, Any]] = []

    for source in chapter["paragraphs"]:
        if chapter_n == 7 and source["text"].startswith(BACK_MATTER_START):
            stats["back_matter_removed"] += len(chapter["paragraphs"]) - source["n"] + 1
            break

        paragraph = build_paragraph(chapter_n, source)
        if paragraph is None:
            stats["artifacts_removed"] += 1
            continue

        if curated and should_merge(chapter_n, curated[-1], paragraph):
            curated[-1]["text"] = join_text(curated[-1]["text"], paragraph["text"])
            merge_i18n(curated[-1], paragraph)
            stats["paragraphs_merged"] += 1
            continue

        curated.append(paragraph)

    result = copy.deepcopy(chapter)
    result["paragraphs"] = finalize_paragraphs(chapter_n, curated)
    return result


def update_meta(root: Path, book: dict[str, Any], updated_ts: str) -> None:
    meta_path = root / BOOK_SLUG / "_meta.json"
    meta = load_json(meta_path)
    meta["chapterCount"] = len(book["chapters"])
    meta["paragraphCount"] = book["paragraphCount"]
    meta["updated"] = updated_ts
    meta["chapterFiles"] = [
        {
            "n": chapter["n"],
            "file": f"chapter-{chapter['n']}.json",
            "title": chapter["title"],
            "paragraphs": len(chapter["paragraphs"]),
        }
        for chapter in book["chapters"]
    ]
    write_json(meta_path, meta)


def update_split_files(root: Path, book: dict[str, Any]) -> None:
    book_dir = root / BOOK_SLUG
    for chapter in book["chapters"]:
        split_chapter = {
            "n": chapter["n"],
            "bookSlug": book["slug"],
            "bookCode": book["code"],
            "refId": chapter["refId"],
            "title": chapter["title"],
            "i18n": copy.deepcopy(chapter.get("i18n", {})),
            "paragraphs": chapter["paragraphs"],
        }
        write_json(book_dir / f"chapter-{chapter['n']}.json", split_chapter)


def update_catalog(root: Path, paragraph_count: int, updated_ts: str) -> None:
    catalog_path = root / "catalog.json"
    catalog = load_json(catalog_path)
    for book in catalog["books"]:
        if book.get("slug") == BOOK_SLUG:
            book["paragraphs"] = paragraph_count
            break
    else:
        raise RuntimeError(f"{BOOK_SLUG} not found in catalog.json")

    catalog["updated"] = updated_ts[:10]
    write_json(catalog_path, catalog)


def curate(root: Path, updated_ts: str, source_ref: str | None = None) -> Counter[str]:
    book_path = root / f"{BOOK_SLUG}.json"
    if source_ref:
        book = load_json_from_git(root, f"{BOOK_SLUG}.json", source_ref)
    else:
        book = load_json(book_path)
    stats: Counter[str] = Counter()

    curated_book = copy.deepcopy(book)
    curated_book["chapters"] = [
        curate_chapter(chapter, stats) for chapter in book["chapters"]
    ]
    curated_book["chapterCount"] = len(curated_book["chapters"])
    curated_book["paragraphCount"] = sum(
        len(chapter["paragraphs"]) for chapter in curated_book["chapters"]
    )
    curated_book["updated"] = updated_ts

    write_json(book_path, curated_book)
    update_split_files(root, curated_book)
    update_meta(root, curated_book, updated_ts)
    update_catalog(root, curated_book["paragraphCount"], updated_ts)

    stats["paragraph_count"] = curated_book["paragraphCount"]
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to the data-library root.",
    )
    parser.add_argument(
        "--updated",
        default=datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        help="Timestamp to write into book metadata.",
    )
    parser.add_argument(
        "--source-ref",
        help="Optional git ref to use as the source monolithic book JSON.",
    )
    args = parser.parse_args()

    stats = curate(args.root, args.updated, args.source_ref)
    for key, value in sorted(stats.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
