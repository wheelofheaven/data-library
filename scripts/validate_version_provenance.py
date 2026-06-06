#!/usr/bin/env python3
"""Validate structured version/provenance metadata in library records."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANG_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Za-z0-9]+)?$")

LEGACY_FIELDS = {
    "versionSource",
    "versionLicense",
    "versionTitles",
    "shortVersionTitles",
    "sourceCitation",
    "reviewer",
}

TYPE_VALUES = {
    "source-text",
    "translation",
    "curated-translation",
    "edition",
    "adaptation",
    "composite",
}

LICENSE_STATUS_VALUES = {
    "project-cc0",
    "public-domain",
    "licensed",
    "source-restricted",
    "mixed",
    "unknown",
}

PROVENANCE_CORE_FIELDS = {
    "sourceRecordId",
    "sourceUrl",
    "baseText",
    "citation",
}

RESPONSIBILITY_FIELDS = {
    "translator",
    "reviewer",
    "editor",
    "curator",
    "generator",
    "signoff",
}


class ValidationRun:
    def __init__(self, strict: bool) -> None:
        self.strict = strict
        self.errors: list[str] = []
        self.structured = 0
        self.legacy_only = 0
        self.unversioned = 0

    def add_error(self, path: Path, message: str) -> None:
        relpath = path.relative_to(ROOT)
        self.errors.append(f"{relpath}: {message}")


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_string(run: ValidationRun, path: Path, obj: dict[str, Any], key: str) -> None:
    if not is_nonempty_string(obj.get(key)):
        run.add_error(path, f"`version.{key}` must be a non-empty string")


def optional_string(
    run: ValidationRun,
    path: Path,
    obj: dict[str, Any],
    prefix: str,
    key: str,
) -> None:
    if key in obj and not is_nonempty_string(obj.get(key)):
        run.add_error(path, f"`{prefix}.{key}` must be a non-empty string when present")


def validate_language(run: ValidationRun, path: Path, obj: dict[str, Any], key: str) -> None:
    value = obj.get(key)
    if not is_nonempty_string(value) or not LANG_RE.match(value):
        run.add_error(path, f"`version.{key}` must be an ISO-like language code")


def validate_string_or_list(
    run: ValidationRun,
    path: Path,
    value: Any,
    field_name: str,
) -> None:
    if is_nonempty_string(value):
        return
    if isinstance(value, list) and value and all(is_nonempty_string(item) for item in value):
        return
    run.add_error(path, f"`{field_name}` must be a non-empty string or list of strings")


def validate_license(run: ValidationRun, path: Path, version: dict[str, Any]) -> None:
    license_data = version.get("license")
    if not isinstance(license_data, dict):
        run.add_error(path, "`version.license` must be an object")
        return

    status = license_data.get("status")
    if status not in LICENSE_STATUS_VALUES:
        allowed = ", ".join(sorted(LICENSE_STATUS_VALUES))
        run.add_error(path, f"`version.license.status` must be one of: {allowed}")

    for key in ("spdx", "url", "detail"):
        optional_string(run, path, license_data, "version.license", key)

    if status == "project-cc0" and license_data.get("spdx") != "CC0-1.0":
        run.add_error(path, '`version.license.spdx` must be "CC0-1.0" for project-cc0 records')


def validate_witnesses(run: ValidationRun, path: Path, provenance: dict[str, Any]) -> None:
    witnesses = provenance.get("witnesses")
    if witnesses is None:
        return
    if not isinstance(witnesses, list) or not witnesses:
        run.add_error(path, "`version.provenance.witnesses` must be a non-empty list when present")
        return
    for index, witness in enumerate(witnesses, start=1):
        field_prefix = f"version.provenance.witnesses[{index}]"
        if not isinstance(witness, dict):
            run.add_error(path, f"`{field_prefix}` must be an object")
            continue
        for key in ("role", "language", "label", "description"):
            optional_string(run, path, witness, field_prefix, key)
        if not any(is_nonempty_string(witness.get(key)) for key in ("label", "description")):
            run.add_error(path, f"`{field_prefix}` must include `label` or `description`")


def validate_provenance(run: ValidationRun, path: Path, version: dict[str, Any]) -> None:
    provenance = version.get("provenance")
    if not isinstance(provenance, dict):
        run.add_error(path, "`version.provenance` must be an object")
        return

    if not any(is_nonempty_string(provenance.get(key)) for key in PROVENANCE_CORE_FIELDS):
        fields = ", ".join(sorted(PROVENANCE_CORE_FIELDS))
        run.add_error(path, f"`version.provenance` must include one of: {fields}")

    for key in ("sourceRecordId", "sourceUrl", "baseText", "citation", "method"):
        optional_string(run, path, provenance, "version.provenance", key)

    validate_witnesses(run, path, provenance)


def validate_responsibility(run: ValidationRun, path: Path, version: dict[str, Any]) -> None:
    responsibility = version.get("responsibility")
    if responsibility is None:
        return
    if not isinstance(responsibility, dict):
        run.add_error(path, "`version.responsibility` must be an object when present")
        return
    for key, value in responsibility.items():
        field_name = f"version.responsibility.{key}"
        if key not in RESPONSIBILITY_FIELDS:
            run.add_error(path, f"`{field_name}` is not a recognized responsibility field")
            continue
        validate_string_or_list(run, path, value, field_name)


def validate_version(run: ValidationRun, path: Path, data: dict[str, Any]) -> None:
    version = data.get("version")
    if version is None:
        if any(field in data for field in LEGACY_FIELDS):
            run.legacy_only += 1
            if run.strict:
                run.add_error(path, "legacy provenance fields are present without `version`")
        else:
            run.unversioned += 1
        return

    run.structured += 1

    if not isinstance(version, dict):
        run.add_error(path, "`version` must be an object")
        return

    schema_version = version.get("schemaVersion")
    if not isinstance(schema_version, int) or schema_version < 1:
        run.add_error(path, "`version.schemaVersion` must be a positive integer")

    require_string(run, path, version, "title")
    optional_string(run, path, version, "version", "shortTitle")
    optional_string(run, path, version, "version", "scope")
    validate_language(run, path, version, "language")
    validate_language(run, path, version, "sourceLanguage")
    require_string(run, path, version, "refSystem")

    version_type = version.get("type")
    if version_type not in TYPE_VALUES:
        allowed = ", ".join(sorted(TYPE_VALUES))
        run.add_error(path, f"`version.type` must be one of: {allowed}")

    validate_license(run, path, version)
    validate_provenance(run, path, version)
    validate_responsibility(run, path, version)


def iter_record_paths(root: Path) -> list[Path]:
    meta_paths = sorted(root.glob("*/_meta.json"))
    single_file_paths = [
        path
        for path in sorted(root.glob("*.json"))
        if path.name not in {"catalog.json", "en.json", "output.json", "target_all_fr_clean_nosubheads.json"}
    ]
    return meta_paths + single_file_paths


def load_json(run: ValidationRun, path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        run.add_error(path, f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return None
    if not isinstance(data, dict):
        run.add_error(path, "record root must be a JSON object")
        return None
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate structured version/provenance metadata in data-library records.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail when legacy provenance fields are present without a structured `version` object",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run = ValidationRun(strict=args.strict)

    paths = iter_record_paths(ROOT)
    for path in paths:
        data = load_json(run, path)
        if data is not None:
            validate_version(run, path, data)

    print(
        "version provenance: "
        f"{run.structured} structured, "
        f"{run.legacy_only} legacy-only, "
        f"{run.unversioned} unversioned records"
    )

    if run.errors:
        for error in run.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
