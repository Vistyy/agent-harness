#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_REQUIRED_FINDING_IDS = {
    "oversized-low-information-rows",
    "detached-search-action-grouping",
    "weak-hierarchy",
    "scaffold-like-material",
    "non-shippable-composition",
}
ALLOWED_EXPECTED_VERDICTS = {"pass", "reject", "blocked"}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def validate_fixture(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    base = path.parent

    artifact = data.get("artifact_path")
    if not isinstance(artifact, str) or not artifact:
        errors.append("missing artifact_path")
    elif not (base / artifact).is_file():
        errors.append(f"artifact_path does not exist: {artifact}")

    if data.get("runtime_verdict") != "pass":
        errors.append("runtime_verdict must be pass")
    expected_verdict = data.get("expected_verdict")
    if expected_verdict not in ALLOWED_EXPECTED_VERDICTS:
        errors.append("expected_verdict must be pass, reject, or blocked")
    if data.get("forbidden_pass_basis"):
        forbidden = set(_as_list(data["forbidden_pass_basis"]))
        for required in ("selector-only", "score-only", "finding-free"):
            if required not in forbidden:
                errors.append(f"forbidden_pass_basis missing {required}")
    else:
        errors.append("missing forbidden_pass_basis")

    anchors = _as_list(data.get("design_anchors"))
    if len([anchor for anchor in anchors if isinstance(anchor, str) and anchor.strip()]) < 3:
        errors.append("design_anchors must include at least three anchors")

    preservation_required = bool(data.get("preservation_anchors_required"))
    preservation_anchors = _as_list(data.get("preservation_anchors"))
    approved_replacement = bool(data.get("approved_visual_language_replacement"))
    approved_identity_cues = _as_list(data.get("approved_identity_cues"))
    rejection_basis = set(_as_list(data.get("rejection_basis")))
    if preservation_required and not approved_replacement:
        if not [
            anchor
            for anchor in preservation_anchors
            if isinstance(anchor, str) and anchor.strip()
        ]:
            if expected_verdict != "blocked":
                errors.append("missing preservation_anchors requires expected_verdict blocked")
        elif data.get("generic_replacement") and expected_verdict != "reject":
            errors.append("generic replacement without approved replacement must reject")
    if (
        approved_replacement
        and expected_verdict == "reject"
        and approved_identity_cues
        and rejection_basis == {"distinctiveness-only"}
    ):
        errors.append("approved identity cues must not be rejected solely for distinctiveness")

    findings = _as_list(data.get("visible_findings"))
    finding_ids = {
        finding.get("id")
        for finding in findings
        if isinstance(finding, dict) and isinstance(finding.get("id"), str)
    }
    required_findings = set(_as_list(data.get("required_visible_findings")))
    if not required_findings and expected_verdict == "reject":
        required_findings = DEFAULT_REQUIRED_FINDING_IDS
    for finding_id in sorted(required_findings - finding_ids):
        errors.append(f"visible_findings missing {finding_id}")
    for finding in findings:
        if not isinstance(finding, dict):
            errors.append("visible_findings entries must be objects")
            continue
        if not str(finding.get("evidence", "")).strip():
            errors.append(f"visible finding {finding.get('id', '<unknown>')} missing evidence")
        if not str(finding.get("repair_direction", "")).strip():
            errors.append(f"visible finding {finding.get('id', '<unknown>')} missing repair_direction")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture")
    args = parser.parse_args()

    errors = validate_fixture(Path(args.fixture))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("design_judge fixture rejected bad UI as expected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
