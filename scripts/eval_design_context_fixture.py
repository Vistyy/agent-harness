#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_HANDOFF_FIELDS = {
    "design_context_source",
    "register",
    "anti_generic_taste_posture",
    "design_anchors",
    "artifact_paths",
}
ALLOWED_OUTCOMES = {"pass", "reject", "blocked", "narrowed"}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _missing(value: Any) -> bool:
    return value in (None, "", "missing", [])


def validate_fixture(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    outcome = data.get("expected_outcome")
    if outcome not in ALLOWED_OUTCOMES:
        errors.append("expected_outcome must be pass, reject, blocked, or narrowed")

    broad = bool(data.get("broad_ui_claim", True))
    narrowed = bool(data.get("explicitly_narrowed_claim"))
    context_missing = any(
        _missing(data.get(key))
        for key in (
            "design_context_source",
            "register",
            "product_context",
            "visual_context",
            "anti_generic_taste_posture",
        )
    )
    contradictory = bool(data.get("contradictory_context"))

    if broad and (context_missing or contradictory) and not narrowed and outcome != "blocked":
        errors.append("missing or contradictory broad UI context must block")
    if narrowed:
        if broad:
            errors.append("explicitly narrowed claim must not remain a broad UI claim")
        if outcome != "narrowed":
            errors.append("explicitly narrowed missing-context fixture must expect narrowed")

    rejection_basis = set(_as_list(data.get("rejection_basis")))
    if data.get("project_approved_taste") and outcome == "reject" and rejection_basis == {"generic-only"}:
        errors.append("project-approved taste must not reject solely as generic")
    if data.get("unsupported_generic_taste") and outcome != "reject":
        errors.append("unsupported generic AI taste must reject")

    if data.get("kind") == "design_judge_handoff":
        fields = set(_as_list(data.get("handoff_fields")))
        missing_fields = REQUIRED_HANDOFF_FIELDS - fields
        if missing_fields and outcome != "blocked":
            errors.append("design_judge handoff missing context fields must block")
            for field in sorted(missing_fields):
                errors.append(f"design_judge handoff missing {field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    args = parser.parse_args()

    errors = validate_fixture(Path(args.fixture))
    if errors:
        for error in errors:
            print(error)
        return 1
    print("design context fixture passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
