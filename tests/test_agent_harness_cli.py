from __future__ import annotations

import os
import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agent_harness import cli


def write(path: Path, text: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")


def fake_project(tmp_path: Path, wave: str = "example-wave") -> Path:
    project = tmp_path / "project"
    write(project / "docs-ai" / "docs" / "initiatives" / "waves" / f"{wave}.md", "# Wave\n")
    write(
        project / "docs-ai" / "current-work" / wave / "wave-execution.md",
        "# Packet\n",
    )
    write(
        project / "docs-ai" / "current-work" / "delivery-map.md",
        f"Packet: docs-ai/docs/initiatives/waves/{wave}.md\n",
    )
    return project


def run_cli(args: list[str]) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT)
    return subprocess.run(
        [sys.executable, "-m", "agent_harness.cli", *args],
        cwd="/tmp",
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def assert_user_error(result: subprocess.CompletedProcess[str], expected: str) -> None:
    assert result.returncode != 0
    assert expected in result.stderr
    assert "Traceback" not in result.stderr


def test_refs_reports_non_wave_references_from_target_repo(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["wave", "refs", "--repo-root", str(project), "--wave", "example-wave"])

    assert result.returncode == 0
    assert "wave: example-wave" in result.stdout
    assert "target: docs-ai/docs/initiatives/waves/example-wave.md" in result.stdout
    assert "non_wave_refs: 1" in result.stdout
    assert "delivery-map.md:1" in result.stdout


def test_cleanup_dry_run_does_not_delete(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    wave_dir = project / "docs-ai" / "current-work" / "example-wave"

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave"])

    assert result.returncode == 0
    assert f"DRY RUN: {wave_dir}" in result.stdout
    assert wave_dir.exists()


def test_cleanup_execute_deletes_valid_wave_dir_only(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    wave_dir = project / "docs-ai" / "current-work" / "example-wave"

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave", "--execute"])

    assert result.returncode == 0
    assert f"DELETED: {wave_dir}" in result.stdout
    assert not wave_dir.exists()
    assert (project / "docs-ai" / "current-work").exists()


def test_cleanup_execute_does_not_follow_symlink_contents(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    external = tmp_path / "external-sentinel.txt"
    external.write_text("keep me", encoding="utf-8")
    wave_dir = project / "docs-ai" / "current-work" / "example-wave"
    (wave_dir / "external-link").symlink_to(external)

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave", "--execute"])

    assert result.returncode == 0
    assert not wave_dir.exists()
    assert external.read_text(encoding="utf-8") == "keep me"


def test_refs_rejects_missing_repo_root_without_traceback(tmp_path: Path) -> None:
    result = run_cli(["wave", "refs", "--repo-root", str(tmp_path / "missing"), "--wave", "example-wave"])

    assert_user_error(result, "Repo root not found")


def test_refs_rejects_file_repo_root_without_traceback(tmp_path: Path) -> None:
    repo_file = tmp_path / "repo-file"
    repo_file.write_text("not a repo", encoding="utf-8")

    result = run_cli(["wave", "refs", "--repo-root", str(repo_file), "--wave", "example-wave"])

    assert_user_error(result, "Repo root is not a directory")


def test_refs_rejects_path_like_wave_id_without_traceback(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["wave", "refs", "--repo-root", str(project), "--wave", "../evil"])

    assert_user_error(result, "Invalid wave id")


def test_cleanup_rejects_missing_repo_root_without_traceback(tmp_path: Path) -> None:
    result = run_cli(["wave", "cleanup", "--repo-root", str(tmp_path / "missing"), "--wave", "example-wave"])

    assert_user_error(result, "Repo root not found")


def test_cleanup_rejects_file_repo_root_without_traceback(tmp_path: Path) -> None:
    repo_file = tmp_path / "repo-file"
    repo_file.write_text("not a repo", encoding="utf-8")

    result = run_cli(["wave", "cleanup", "--repo-root", str(repo_file), "--wave", "example-wave"])

    assert_user_error(result, "Repo root is not a directory")


def test_cleanup_rejects_path_like_wave_ids_before_resolution(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    dotdot = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "../evil"])
    slash = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "evil/name"])

    assert_user_error(dotdot, "Invalid wave id")
    assert_user_error(slash, "Invalid wave id")


def test_cleanup_rejects_missing_current_work_root_without_traceback(tmp_path: Path) -> None:
    project = tmp_path / "project"
    (project / "docs-ai").mkdir(parents=True)

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave"])

    assert_user_error(result, "Current-work root not found")


def test_cleanup_rejects_file_current_work_root_without_traceback(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work", "not a directory")

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave"])

    assert_user_error(result, "Current-work root is not a directory")


def test_cleanup_rejects_symlink_current_work_root_and_deletes_nothing(tmp_path: Path) -> None:
    project = tmp_path / "project"
    target = tmp_path / "real-current-work"
    write(target / "example-wave" / "wave-execution.md", "# Packet\n")
    (project / "docs-ai").mkdir(parents=True)
    (project / "docs-ai" / "current-work").symlink_to(target)

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave", "--execute"])

    assert_user_error(result, "Refusing symlink current-work root")
    assert (target / "example-wave" / "wave-execution.md").exists()


def test_cleanup_rejects_missing_wave_dir_without_traceback(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "missing-wave"])

    assert_user_error(result, "Wave directory not found")


def test_cleanup_rejects_symlink_wave_dir_and_deletes_nothing(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    current_work = project / "docs-ai" / "current-work"
    real_wave = tmp_path / "real-wave"
    write(real_wave / "wave-execution.md", "# Packet\n")
    symlink_wave = current_work / "linked-wave"
    symlink_wave.symlink_to(real_wave)

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "linked-wave", "--execute"])

    assert_user_error(result, "Refusing symlink wave directory")
    assert (real_wave / "wave-execution.md").exists()


def test_cleanup_rejects_wave_dir_without_marker_and_deletes_nothing(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    markerless = project / "docs-ai" / "current-work" / "markerless-wave"
    markerless.mkdir()

    result = run_cli(["wave", "cleanup", "--repo-root", str(project), "--wave", "markerless-wave", "--execute"])

    assert_user_error(result, "Directory is not a wave execution directory")
    assert markerless.exists()


def test_installed_console_script_runs_outside_checkout_against_project_without_justfile(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    venv = tmp_path / "venv"
    subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)
    python = venv / "bin" / "python"
    agent_harness = venv / "bin" / "agent-harness"
    subprocess.run([str(python), "-m", "pip", "install", "-e", str(ROOT)], check=True)

    refs = subprocess.run(
        [str(agent_harness), "wave", "refs", "--repo-root", str(project), "--wave", "example-wave"],
        cwd=tmp_path,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    cleanup = subprocess.run(
        [str(agent_harness), "wave", "cleanup", "--repo-root", str(project), "--wave", "example-wave"],
        cwd=tmp_path,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert refs.returncode == 0
    assert "non_wave_refs: 1" in refs.stdout
    assert cleanup.returncode == 0
    assert "DRY RUN:" in cleanup.stdout
    assert not (project / "justfile").exists()


def test_codex_install_shim_runs_outside_checkout_against_project_without_pythonpath(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    shim = bin_dir / "agent-harness"
    shim.symlink_to(ROOT / "adapters" / "codex" / "bin" / "agent-harness")
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)

    result = subprocess.run(
        [str(shim), "wave", "refs", "--repo-root", str(project), "--wave", "example-wave"],
        cwd=tmp_path,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert result.returncode == 0
    assert "non_wave_refs: 1" in result.stdout


def test_wave_bootstrap_creates_discovery_required_brief(tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()

    result = run_cli(
        [
            "wave",
            "bootstrap",
            "--repo-root",
            str(project),
            "--wave",
            "new-wave-1",
            "--title",
            "New Wave",
            "--task",
            "initiative/feature/task",
        ]
    )

    brief = project / "docs-ai" / "docs" / "initiatives" / "waves" / "new-wave-1.md"
    assert result.returncode == 0
    assert f"CREATED: {brief}" in result.stdout
    text = brief.read_text(encoding="utf-8")
    assert "# Wave new-wave-1 - New Wave" in text
    assert "**Status:** discovery-required" in text
    assert "- `initiative/feature/task`" in text


def test_wave_bootstrap_refuses_overwrite_without_force(tmp_path: Path) -> None:
    project = tmp_path / "project"
    brief = project / "docs-ai" / "docs" / "initiatives" / "waves" / "new-wave-1.md"
    write(brief, "existing\n")

    result = run_cli(
        [
            "wave",
            "bootstrap",
            "--repo-root",
            str(project),
            "--wave",
            "new-wave-1",
            "--title",
            "New Wave",
        ]
    )

    assert_user_error(result, "Refusing to overwrite existing file without --force")
    assert brief.read_text(encoding="utf-8") == "existing\n"


def test_governance_check_reports_broken_project_doc_links(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "AGENTS.md", "[Broken](missing.md)\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs.cross-doc-links" in result.stdout
    assert "AGENTS.md has broken markdown links: missing.md" in result.stdout


def test_governance_check_passes_valid_project_doc_links(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "target.md", "ok\n")
    write(project / "AGENTS.md", "[Target](target.md)\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 0
    assert result.stdout == ""


def test_governance_check_rejects_missing_repo_root_without_traceback(tmp_path: Path) -> None:
    result = run_cli(["governance", "check", "--repo-root", str(tmp_path / "missing")])

    assert_user_error(result, "Repo root not found")


def test_governance_check_rejects_file_repo_root_without_traceback(tmp_path: Path) -> None:
    repo_file = tmp_path / "repo-file"
    repo_file.write_text("not a repo", encoding="utf-8")

    result = run_cli(["governance", "check", "--repo-root", str(repo_file)])

    assert_user_error(result, "Repo root is not a directory")


def test_replaced_skill_scripts_are_removed() -> None:
    assert not (ROOT / "skills" / "initiatives-workflow" / "scripts").exists()
    assert not (ROOT / "skills" / "harness-governance" / "scripts").exists()


def test_cli_main_returns_nonzero_for_user_errors_without_traceback(tmp_path: Path, capsys) -> None:
    status = cli.main(["wave", "refs", "--repo-root", str(tmp_path / "missing"), "--wave", "example-wave"])

    captured = capsys.readouterr()
    assert status == 1
    assert "Repo root not found" in captured.err
    assert "Traceback" not in captured.err
