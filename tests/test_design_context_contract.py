from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.eval_design_context_fixture import validate_fixture


FIXTURE_DIR = Path("tests/fixtures/design_context")


def test_design_context_fixtures_pass() -> None:
    for fixture in sorted(FIXTURE_DIR.glob("*.json")):
        assert validate_fixture(fixture) == [], fixture


def test_missing_broad_context_must_block(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "missing-context-broad-ui.json").read_text(encoding="utf-8"))
    data["expected_outcome"] = "pass"
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    assert "missing or contradictory broad UI context must block" in validate_fixture(path)


def test_project_approved_taste_is_not_rejected_only_as_generic(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "project-approved-taste.json").read_text(encoding="utf-8"))
    data["expected_outcome"] = "reject"
    data["rejection_basis"] = ["generic-only"]
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    assert "project-approved taste must not reject solely as generic" in validate_fixture(path)


def test_design_judge_missing_context_handoff_must_block(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "design-judge-missing-context-handoff.json").read_text(encoding="utf-8"))
    data["expected_outcome"] = "pass"
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    errors = validate_fixture(path)

    assert "design_judge handoff missing context fields must block" in errors
    assert "design_judge handoff missing design_context_source" in errors
