from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import codex_install_smoke


def test_role_names_are_loaded_from_roles_doc() -> None:
    roles = codex_install_smoke.role_names()

    assert "explorer" in roles
    assert "runtime_evidence" in roles


def test_assert_config_roles_rejects_missing_role(tmp_path: Path) -> None:
    codex_home = tmp_path / "codex-home"
    codex_home.mkdir()
    (codex_home / "config.toml").write_text(
        "[features]\nmulti_agent = true\n\n[agents.explorer]\nconfig_file = \"agents/explorer.toml\"\n",
        encoding="utf-8",
    )

    try:
        codex_install_smoke.assert_config_roles(codex_home)
    except AssertionError as exc:
        assert "config.toml missing role from agents/roles.md" in str(exc)
    else:
        raise AssertionError("assert_config_roles should reject missing roles")


def test_assert_stage_only_rejects_unexpected_full_install_surface(tmp_path: Path) -> None:
    codex_home = tmp_path / "codex-home"
    bin_dir = tmp_path / "bin"
    skills_home = codex_home / "skills"
    skills_home.mkdir(parents=True)
    (skills_home / "harness-governance").symlink_to(codex_install_smoke.ROOT / "skills" / "harness-governance")
    (codex_home / "AGENTS.md").write_text("unexpected\n", encoding="utf-8")

    try:
        codex_install_smoke.assert_stage_only(codex_home, bin_dir)
    except AssertionError as exc:
        assert "stage-only install unexpectedly created" in str(exc)
    else:
        raise AssertionError("assert_stage_only should reject full install surfaces")


def test_assert_stage_only_rejects_cli_link(tmp_path: Path) -> None:
    codex_home = tmp_path / "codex-home"
    bin_dir = tmp_path / "bin"
    skills_home = codex_home / "skills"
    skills_home.mkdir(parents=True)
    bin_dir.mkdir()
    (skills_home / "harness-governance").symlink_to(codex_install_smoke.ROOT / "skills" / "harness-governance")
    (bin_dir / "agent-harness").symlink_to(codex_install_smoke.ROOT / "adapters" / "codex" / "bin" / "agent-harness")

    try:
        codex_install_smoke.assert_stage_only(codex_home, bin_dir)
    except AssertionError as exc:
        assert "stage-only install unexpectedly created" in str(exc)
    else:
        raise AssertionError("assert_stage_only should reject CLI link")
