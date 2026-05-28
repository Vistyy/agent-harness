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


def fake_project(tmp_path: Path, item: str = "example-item") -> Path:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "work-notes" / f"{item}.md", "# Work Note\n")
    write(
        project / "docs-ai" / "current-work" / "active" / item / "active-work-note.md",
        "# Context Note\n",
    )
    write(
        project / "docs-ai" / "current-work" / "delivery-map.md",
        f"Context: [{item}](work-notes/{item}.md)\n",
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


def test_refs_reports_non_work_note_references_from_target_repo(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["memory", "refs", "--repo-root", str(project), "--item", "example-item"])

    assert result.returncode == 0
    assert "item: example-item" in result.stdout
    assert "target: docs-ai/current-work/work-notes/example-item.md" in result.stdout
    assert "non_note_refs: 1" in result.stdout
    assert "delivery-map.md:1" in result.stdout
    assert "[example-item](work-notes/example-item.md)" in result.stdout


def test_refs_ignores_cache_files(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    write(
        project / "__pycache__" / "cached.pyc",
        "docs-ai/current-work/work-notes/example-item.md\n",
    )

    result = run_cli(["memory", "refs", "--repo-root", str(project), "--item", "example-item"])

    assert result.returncode == 0
    assert "__pycache__" not in result.stdout
    assert "non_note_refs: 1" in result.stdout


def test_refs_ignores_generated_binary_files(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    binary_path = project / "apps" / "web" / ".fallow" / "churn.bin"
    binary_path.parent.mkdir(parents=True)
    binary_path.write_bytes(b"\0docs-ai/current-work/work-notes/example-item.md\n")

    result = run_cli(["memory", "refs", "--repo-root", str(project), "--item", "example-item"])

    assert result.returncode == 0
    assert ".fallow" not in result.stdout
    assert "non_note_refs: 1" in result.stdout


def test_lifecycle_reports_memory_artifacts_and_refs(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    write(
        project / "docs-ai" / "current-work" / "active" / "example-item" / "active-work-note.draft.md",
        "# Draft\n",
    )
    write(
        project / "docs-ai" / "current-work" / "backlog" / "initiative__feature__example-item.md",
        "# Backlog\n",
    )
    write(
        project / "docs-ai" / "docs" / "handoff.md",
        "See docs-ai/current-work/active/example-item/active-work-note.md\n",
    )

    result = run_cli(["memory", "lifecycle", "--repo-root", str(project), "--item", "example-item"])

    assert result.returncode == 0
    assert "item: example-item" in result.stdout
    assert "active_note: present" in result.stdout
    assert "draft_notes: 1" in result.stdout
    assert "active-work-note.draft.md" in result.stdout
    assert "work_note: present docs-ai/current-work/work-notes/example-item.md" in result.stdout
    assert "owner_conflict: active note and work note both exist" in result.stdout
    assert "backlog_details: 1" in result.stdout
    assert "initiative__feature__example-item.md" in result.stdout
    assert "delivery_map: present docs-ai/current-work/delivery-map.md" in result.stdout
    assert "work_note_non_note_refs: 1" in result.stdout
    assert "active_or_backlog_refs:" in result.stdout
    assert "handoff.md:1" in result.stdout
    assert "choose one disposition per artifact: delete | extract | backlog | keep active" in result.stdout
    assert "agent-harness memory cleanup --repo-root <project-root> --item example-item" in result.stdout


def test_status_reports_active_work_note_and_backlog_memory(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    write(
        project / "docs-ai" / "current-work" / "active" / "example-item" / "active-work-note.md",
        """
        # Active Work Note

        ## Required Slices

        - `slice one: review state = quality_guard pending; status = implementing`
        - `slice two: review state = blocked; status = blocked`
        - `slice three: review state = pending`
        - `slice four: review state = custom review; status = custom status`

        ## Required Claims

        - `claim one: review state = pending; status = completed`

        ## Closeout

        - required slices closed: `status = closed should not count`
        """,
    )
    write(
        project / "docs-ai" / "current-work" / "backlog" / "initiative__feature__example-item.md",
        """
        # Backlog Entry: initiative/feature/example-item

        ## Metadata

        - status: `open`
        - owner: `work-memory`
        - bucket: `discovered separate debt`
        - location: `skills/work-memory`
        """,
    )

    result = run_cli(["memory", "status", "--repo-root", str(project)])

    assert result.returncode == 0
    assert "work_state_status:" in result.stdout
    assert "active_control_sheets: 1" in result.stdout
    assert "A example-item: docs-ai/current-work/active/example-item/active-work-note.md" in result.stdout
    assert "claim_statuses: blocked=1, completed=1, implementing=1" in result.stdout
    assert "review_states: blocked=1, pending=2, quality_guard pending=1" in result.stdout
    assert "invalid_claim_statuses: custom status=1" in result.stdout
    assert "invalid_review_states: custom review=1" in result.stdout
    assert "required_claims_missing_status: 1" in result.stdout
    assert "queued_items: 1" in result.stdout
    assert "Q example-item: docs-ai/current-work/work-notes/example-item.md queue_state=unknown" in result.stdout
    assert "owner_conflicts: 2" in result.stdout
    assert "! example-item: active=docs-ai/current-work/active/example-item/active-work-note.md queued=docs-ai/current-work/work-notes/example-item.md" in result.stdout
    assert "! example-item: active=docs-ai/current-work/active/example-item/active-work-note.md queued=docs-ai/current-work/backlog/initiative__feature__example-item.md" in result.stdout
    assert "backlog_details: 1" in result.stdout
    assert (
        "B initiative/feature/example-item: docs-ai/current-work/backlog/initiative__feature__example-item.md "
        "status=open owner=work-memory bucket=discovered separate debt queue_state=unknown"
    ) in result.stdout


def test_work_state_status_aliases_memory_status(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    legacy = run_cli(["memory", "status", "--repo-root", str(project)])
    current = run_cli(["work-state", "status", "--repo-root", str(project)])

    assert current.returncode == 0
    assert current.stdout == legacy.stdout


def test_work_state_check_reports_mechanical_state_errors(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    write(
        project / "docs-ai" / "current-work" / "active" / "example-item" / "active-work-note.md",
        """
        # Active Control Sheet

        ## Required Claims

        - `claim one: review state = custom review; status = custom status`
        - `claim two: review state = pending`
        """,
    )
    write(
        project / "docs-ai" / "current-work" / "backlog" / "initiative__feature__example-item.md",
        """
        # Backlog Entry

        ## Metadata

        - status: `open`
        - owner: `work-memory`
        - bucket: `discovered separate debt`
        - queue state: `ready`
        """,
    )

    result = run_cli(["work-state", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "work_state_check: fail" in result.stderr
    assert "owner conflict for example-item" in result.stderr
    assert "queued=docs-ai/current-work/backlog/initiative__feature__example-item.md" in result.stderr
    assert "docs-ai/current-work/work-notes/example-item.md: invalid or missing queue state 'unknown'" in result.stderr
    assert "invalid claim status 'custom status'" in result.stderr
    assert "invalid review state 'custom review'" in result.stderr
    assert "required claims missing status (1)" in result.stderr


def test_work_state_check_passes_clean_state(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "delivery-map.md", "# Delivery Map\n")
    write(
        project / "docs-ai" / "current-work" / "active" / "example-item" / "active-work-note.md",
        """
        # Active Control Sheet

        ## Required Claims

        - `claim one: review state = pending; status = pending`
        """,
    )

    result = run_cli(["work-state", "check", "--repo-root", str(project)])

    assert result.returncode == 0
    assert result.stdout.strip() == "work_state_check: pass"


def test_work_state_check_reports_invalid_backlog_queue_state(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "delivery-map.md", "# Delivery Map\n")
    write(
        project / "docs-ai" / "current-work" / "backlog" / "initiative__feature__item.md",
        """
        # Backlog Entry

        ## Metadata

        - status: `open`
        - owner: `work-memory`
        - bucket: `discovered separate debt`
        """,
    )

    result = run_cli(["work-state", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs-ai/current-work/backlog/initiative__feature__item.md: invalid or missing queue state 'unknown'" in result.stderr


def test_lifecycle_rejects_path_like_item_without_traceback(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["memory", "lifecycle", "--repo-root", str(project), "--item", "../evil"])

    assert_user_error(result, "Invalid item id")


def test_cleanup_dry_run_does_not_delete(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    item_dir = project / "docs-ai" / "current-work" / "active" / "example-item"

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item"])

    assert result.returncode == 0
    assert f"DRY RUN: {item_dir}" in result.stdout
    assert item_dir.exists()


def test_cleanup_execute_deletes_valid_item_dir_only(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    item_dir = project / "docs-ai" / "current-work" / "active" / "example-item"

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item", "--execute"])

    assert result.returncode == 0
    assert f"DELETED: {item_dir}" in result.stdout
    assert not item_dir.exists()
    assert (project / "docs-ai" / "current-work").exists()


def test_cleanup_execute_does_not_follow_symlink_contents(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    external = tmp_path / "external-sentinel.txt"
    external.write_text("keep me", encoding="utf-8")
    item_dir = project / "docs-ai" / "current-work" / "active" / "example-item"
    (item_dir / "external-link").symlink_to(external)

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item", "--execute"])

    assert result.returncode == 0
    assert not item_dir.exists()
    assert external.read_text(encoding="utf-8") == "keep me"


def test_refs_rejects_missing_repo_root_without_traceback(tmp_path: Path) -> None:
    result = run_cli(["memory", "refs", "--repo-root", str(tmp_path / "missing"), "--item", "example-item"])

    assert_user_error(result, "Repo root not found")


def test_refs_rejects_file_repo_root_without_traceback(tmp_path: Path) -> None:
    repo_file = tmp_path / "repo-file"
    repo_file.write_text("not a repo", encoding="utf-8")

    result = run_cli(["memory", "refs", "--repo-root", str(repo_file), "--item", "example-item"])

    assert_user_error(result, "Repo root is not a directory")


def test_refs_rejects_path_like_work_note_id_without_traceback(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["memory", "refs", "--repo-root", str(project), "--item", "../evil"])

    assert_user_error(result, "Invalid item id")


def test_cleanup_rejects_missing_repo_root_without_traceback(tmp_path: Path) -> None:
    result = run_cli(["memory", "cleanup", "--repo-root", str(tmp_path / "missing"), "--item", "example-item"])

    assert_user_error(result, "Repo root not found")


def test_cleanup_rejects_file_repo_root_without_traceback(tmp_path: Path) -> None:
    repo_file = tmp_path / "repo-file"
    repo_file.write_text("not a repo", encoding="utf-8")

    result = run_cli(["memory", "cleanup", "--repo-root", str(repo_file), "--item", "example-item"])

    assert_user_error(result, "Repo root is not a directory")


def test_cleanup_rejects_path_like_work_note_ids_before_resolution(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    dotdot = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "../evil"])
    slash = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "evil/name"])

    assert_user_error(dotdot, "Invalid item id")
    assert_user_error(slash, "Invalid item id")


def test_cleanup_rejects_missing_current_work_root_without_traceback(tmp_path: Path) -> None:
    project = tmp_path / "project"
    (project / "docs-ai").mkdir(parents=True)

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item"])

    assert_user_error(result, "Current-work root not found")


def test_cleanup_rejects_file_current_work_root_without_traceback(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work", "not a directory")

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item"])

    assert_user_error(result, "Current-work root is not a directory")


def test_cleanup_rejects_symlink_current_work_root_and_deletes_nothing(tmp_path: Path) -> None:
    project = tmp_path / "project"
    target = tmp_path / "real-current-work"
    write(target / "active" / "example-item" / "active-work-note.md", "# Context Note\n")
    (project / "docs-ai").mkdir(parents=True)
    (project / "docs-ai" / "current-work").symlink_to(target)

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item", "--execute"])

    assert_user_error(result, "Refusing symlink current-work root")
    assert (target / "active" / "example-item" / "active-work-note.md").exists()


def test_cleanup_rejects_symlink_active_work_root_and_deletes_nothing(tmp_path: Path) -> None:
    project = tmp_path / "project"
    target = tmp_path / "real-active-work"
    write(target / "example-item" / "active-work-note.md", "# Context Note\n")
    (project / "docs-ai" / "current-work").mkdir(parents=True)
    (project / "docs-ai" / "current-work" / "active").symlink_to(target)

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "example-item", "--execute"])

    assert_user_error(result, "Refusing symlink active-work root")
    assert (target / "example-item" / "active-work-note.md").exists()


def test_cleanup_rejects_missing_item_dir_without_traceback(tmp_path: Path) -> None:
    project = fake_project(tmp_path)

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "missing-item"])

    assert_user_error(result, "Item directory not found")


def test_cleanup_rejects_symlink_item_dir_and_deletes_nothing(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    active_work = project / "docs-ai" / "current-work" / "active"
    real_item = tmp_path / "real-item"
    write(real_item / "active-work-note.md", "# Context Note\n")
    symlink_item = active_work / "linked-item"
    symlink_item.symlink_to(real_item)

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "linked-item", "--execute"])

    assert_user_error(result, "Refusing symlink item directory")
    assert (real_item / "active-work-note.md").exists()


def test_cleanup_rejects_item_dir_without_marker_and_deletes_nothing(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    markerless = project / "docs-ai" / "current-work" / "active" / "markerless-item"
    markerless.mkdir()

    result = run_cli(["memory", "cleanup", "--repo-root", str(project), "--item", "markerless-item", "--execute"])

    assert_user_error(result, "Directory is not an active work-note directory")
    assert markerless.exists()


def test_installed_console_script_runs_outside_checkout_against_project_without_justfile(tmp_path: Path) -> None:
    project = fake_project(tmp_path)
    venv = tmp_path / "venv"
    subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)
    python = venv / "bin" / "python"
    agent_harness = venv / "bin" / "agent-harness"
    subprocess.run([str(python), "-m", "pip", "install", "-e", str(ROOT)], check=True)

    refs = subprocess.run(
        [str(agent_harness), "memory", "refs", "--repo-root", str(project), "--item", "example-item"],
        cwd=tmp_path,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    cleanup = subprocess.run(
        [str(agent_harness), "memory", "cleanup", "--repo-root", str(project), "--item", "example-item"],
        cwd=tmp_path,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert refs.returncode == 0
    assert "non_note_refs: 1" in refs.stdout
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
        [str(shim), "memory", "refs", "--repo-root", str(project), "--item", "example-item"],
        cwd=tmp_path,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert result.returncode == 0
    assert "non_note_refs: 1" in result.stdout


def test_work_note_bootstrap_creates_work_note(tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()

    result = run_cli(
        [
            "memory",
            "bootstrap",
            "--repo-root",
            str(project),
            "--item",
            "new-item-1",
            "--title",
            "New Work Note",
            "--task",
            "initiative/feature/task",
        ]
    )

    brief = project / "docs-ai" / "current-work" / "work-notes" / "new-item-1.md"
    assert result.returncode == 0
    assert f"CREATED: {brief}" in result.stdout
    text = brief.read_text(encoding="utf-8")
    assert "# Queued Work Item: new-item-1" in text
    assert "This queued item is memory, not authority." in text
    assert "not active progress state" in text
    assert "solution-shaping" in text
    assert "delivery workflow" not in text
    assert "## Queue" in text
    assert "- queue state: `ready`" in text
    assert "## Starting Points" in text
    assert "- `initiative/feature/task`" in text
    assert "## Recheck During Discovery" in text
    assert "## Possible Sequence" in text


def test_work_note_bootstrap_refuses_overwrite_without_force(tmp_path: Path) -> None:
    project = tmp_path / "project"
    brief = project / "docs-ai" / "current-work" / "work-notes" / "new-item-1.md"
    write(brief, "existing\n")

    result = run_cli(
        [
            "memory",
            "bootstrap",
            "--repo-root",
            str(project),
            "--item",
            "new-item-1",
            "--title",
            "New Work Note",
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


def test_governance_check_allows_agents_delivery_map_pointer(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "delivery-map.md", "# Delivery Map\n")
    write(project / "AGENTS.md", "`docs-ai/current-work/delivery-map.md`\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 0
    assert result.stdout == ""


def test_governance_check_rejects_durable_work_note_memory_link(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "work-notes" / "old-note.md", "# Work Note\n")
    write(project / "docs-ai" / "docs" / "policy.md", "[Old](../current-work/work-notes/old-note.md)\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs.work-note-memory-reference" in result.stdout
    assert "docs-ai/docs/policy.md references work-note/current-work memory" in result.stdout


def test_governance_check_rejects_root_style_durable_current_work_path(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "delivery-map.md", "# Delivery Map\n")
    write(project / "docs-ai" / "docs" / "policy.md", "`docs-ai/current-work/delivery-map.md`\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs.work-note-memory-reference" in result.stdout
    assert "docs-ai/current-work/delivery-map.md" in result.stdout


def test_governance_check_rejects_legacy_durable_work_note_location(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "docs" / "initiatives" / "work-notes" / "old-note.md", "# Old Note\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs.work-note-location" in result.stdout
    assert "docs-ai/docs/initiatives/work-notes/old-note.md" in result.stdout


def test_governance_check_rejects_backticked_current_work_memory_path(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "active" / "old" / "active-work-note.md", "# Old Note\n")
    write(project / "docs-ai" / "docs" / "policy.md", "See `../current-work/active/old/active-work-note.md`.\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs.work-note-memory-reference" in result.stdout
    assert "../current-work/active/old/active-work-note.md" in result.stdout


def test_governance_check_rejects_anchored_backticked_memory_path(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "active" / "old" / "active-work-note.md", "# Old Note\n")
    write(project / "docs-ai" / "docs" / "policy.md", "See `../current-work/active/old/active-work-note.md#closeout`.\n")

    result = run_cli(["governance", "check", "--repo-root", str(project)])

    assert result.returncode == 1
    assert "docs.work-note-memory-reference" in result.stdout
    assert "../current-work/active/old/active-work-note.md#closeout" in result.stdout


def test_governance_check_allows_work_notes_to_link_each_other(tmp_path: Path) -> None:
    project = tmp_path / "project"
    write(project / "docs-ai" / "current-work" / "work-notes" / "old-note.md", "# Work Note\n")
    write(
        project / "docs-ai" / "current-work" / "work-notes" / "new-note.md",
        "[Old](old-note.md)\n",
    )

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


def test_cli_main_returns_nonzero_for_user_errors_without_traceback(tmp_path: Path, capsys) -> None:
    status = cli.main(["memory", "refs", "--repo-root", str(tmp_path / "missing"), "--item", "example-item"])

    captured = capsys.readouterr()
    assert status == 1
    assert "Repo root not found" in captured.err
    assert "Traceback" not in captured.err
