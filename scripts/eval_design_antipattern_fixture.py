#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ALLOWED_OUTCOMES = {"pass", "reject", "blocked"}
ALLOWED_DISPOSITIONS = {"none", "project-approved", "fix-required", "blocked"}
ALLOWED_SOURCES = {"manual checklist", "automated detector", "combined", "not-run"}
ALLOWED_REGISTERS = {"brand", "product", "mixed"}
REQUIRED_REPORT_FIELDS = {
    "source",
    "register",
    "project_context",
    "findings",
    "disposition",
    "artifact",
}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def validate_fixture(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    outcome = data.get("expected_outcome")
    if outcome not in ALLOWED_OUTCOMES:
        errors.append("expected_outcome must be pass, reject, or blocked")

    broad = bool(data.get("broad_ui_claim", True))
    report = data.get("anti_generic_report")
    if not isinstance(report, dict):
        if broad and outcome != "blocked":
            errors.append("missing anti_generic_report for broad UI must block")
        return errors

    missing_fields = REQUIRED_REPORT_FIELDS - set(report)
    for field in sorted(missing_fields):
        errors.append(f"anti_generic_report missing {field}")
    source = report.get("source")
    if source not in ALLOWED_SOURCES:
        errors.append("anti_generic_report source is invalid")
    if report.get("register") not in ALLOWED_REGISTERS:
        errors.append("anti_generic_report register is invalid")
    if not str(report.get("project_context", "")).strip():
        errors.append("anti_generic_report project_context is required")
    if not isinstance(report.get("findings"), list):
        errors.append("anti_generic_report findings must be a list")
    if not str(report.get("artifact", "")).strip():
        errors.append("anti_generic_report artifact is required")
    disposition = report.get("disposition")
    if disposition not in ALLOWED_DISPOSITIONS:
        errors.append("anti_generic_report disposition is invalid")
    if source == "not-run":
        reason = str(report.get("reason", "")).strip()
        valid_reason = bool(report.get("not_applicable")) and len(reason) >= 20
        narrowed = bool(data.get("explicitly_narrowed_claim"))
        if broad and not valid_reason and not narrowed and outcome != "blocked":
            errors.append("not-run broad UI report must block without named not-applicable or narrowed reason")
        if broad and report.get("not_applicable") and not valid_reason and outcome != "blocked":
            errors.append("not-applicable reason is too vague")
    if data.get("detector_only_pass") and outcome == "pass":
        errors.append("detector-only pass is invalid")
    if data.get("project_approved_finding") and disposition == "blocked":
        errors.append("project-approved finding must not block solely as generic")
    if data.get("unsupported_generic_finding") and disposition not in {"fix-required", "blocked"}:
        errors.append("unsupported generic finding must require fix or block")
    if data.get("product_system_font") and data.get("project_approved_finding") and outcome != "pass":
        errors.append("product system font with project approval must pass this anti-pattern gate")

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
    print("design anti-pattern fixture passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
