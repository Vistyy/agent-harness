from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.eval_design_antipattern_fixture import validate_fixture


FIXTURE_DIR = Path("tests/fixtures/design_antipattern")


def test_design_antipattern_fixtures_pass() -> None:
    for fixture in sorted(FIXTURE_DIR.glob("*.json")):
        assert validate_fixture(fixture) == [], fixture


def test_missing_report_broad_ui_must_block(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "missing-report-broad-ui.json").read_text(encoding="utf-8"))
    data["expected_outcome"] = "pass"
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    assert "missing anti_generic_report for broad UI must block" in validate_fixture(path)


def test_detector_only_pass_is_invalid(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "detector-only-pass.json").read_text(encoding="utf-8"))
    data["expected_outcome"] = "pass"
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    assert "detector-only pass is invalid" in validate_fixture(path)


def test_vague_not_applicable_reason_blocks(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "not-applicable-valid.json").read_text(encoding="utf-8"))
    data["anti_generic_report"]["reason"] = "n/a"
    data["expected_outcome"] = "pass"
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    assert "not-applicable reason is too vague" in validate_fixture(path)


def test_report_shape_requires_project_context_and_artifact(tmp_path: Path) -> None:
    data = json.loads((FIXTURE_DIR / "product-system-font-allowed.json").read_text(encoding="utf-8"))
    del data["anti_generic_report"]["project_context"]
    del data["anti_generic_report"]["artifact"]
    path = tmp_path / "fixture.json"
    path.write_text(json.dumps(data), encoding="utf-8")

    errors = validate_fixture(path)

    assert "anti_generic_report missing project_context" in errors
    assert "anti_generic_report missing artifact" in errors
