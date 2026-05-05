from __future__ import annotations

import json
import textwrap
from pathlib import Path

from scripts.eval_design_judge_fixture import validate_fixture


FIXTURE = Path("tests/fixtures/design_judge/bad-shopping-list.json")


def test_bad_shopping_list_fixture_rejects() -> None:
    assert validate_fixture(FIXTURE) == []


def test_bad_shopping_list_fixture_requires_reject(tmp_path: Path) -> None:
    source = json.loads(FIXTURE.read_text(encoding="utf-8"))
    source["expected_verdict"] = "pass"
    (tmp_path / "artifact.svg").write_text("<svg />", encoding="utf-8")
    source["artifact_path"] = "artifact.svg"
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(source), encoding="utf-8")

    assert "expected_verdict must be reject" in validate_fixture(path)


def test_bad_shopping_list_fixture_requires_visible_findings(tmp_path: Path) -> None:
    fixture = {
        "artifact_path": "artifact.svg",
        "runtime_verdict": "pass",
        "expected_verdict": "reject",
        "forbidden_pass_basis": ["selector-only", "score-only", "finding-free"],
        "design_anchors": ["dense workflow", "clear hierarchy", "product fit"],
        "visible_findings": [],
    }
    (tmp_path / "artifact.svg").write_text("<svg />", encoding="utf-8")
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(fixture), encoding="utf-8")

    errors = validate_fixture(path)

    assert "visible_findings missing oversized-low-information-rows" in errors
    assert "visible_findings missing non-shippable-composition" in errors


def test_bad_shopping_list_fixture_requires_artifact_path(tmp_path: Path) -> None:
    path = tmp_path / "fixture.json"
    path.write_text(
        textwrap.dedent(
            """
            {
              "artifact_path": "missing.svg",
              "runtime_verdict": "pass",
              "expected_verdict": "reject",
              "forbidden_pass_basis": ["selector-only", "score-only", "finding-free"],
              "design_anchors": ["dense workflow", "clear hierarchy", "product fit"],
              "visible_findings": [
                {"id": "oversized-low-information-rows", "evidence": "x", "repair_direction": "x"},
                {"id": "detached-search-action-grouping", "evidence": "x", "repair_direction": "x"},
                {"id": "weak-hierarchy", "evidence": "x", "repair_direction": "x"},
                {"id": "scaffold-like-material", "evidence": "x", "repair_direction": "x"},
                {"id": "non-shippable-composition", "evidence": "x", "repair_direction": "x"}
              ]
            }
            """
        ),
        encoding="utf-8",
    )

    assert "artifact_path does not exist: missing.svg" in validate_fixture(path)
