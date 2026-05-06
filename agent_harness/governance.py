from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO
from urllib.parse import unquote

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_LOCAL_PATH_PATTERN = re.compile(r"`([^`]+)`")
MARKDOWN_LINK_SCAN_ROOTS = ("AGENTS.md", "docs-ai/docs", "docs-ai/current-work")
MARKDOWN_LINK_TEMPLATE_CHARS = ("<", ">", "{", "}", "*")
COMPLETED_WAVE_STATUS_PATTERN = re.compile(r"^\*\*Status:\*\*\s*done\s*$", re.MULTILINE)


class GovernanceCommandError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class CheckFailure:
    check_id: str
    message: str
    remediation: str


def _iter_markdown_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for root in MARKDOWN_LINK_SCAN_ROOTS:
        path = repo_root / root
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(files)


def _local_target_path(markdown_file: Path, target: str) -> Path | None:
    if "://" in target or target.startswith("#"):
        return None
    raw_target = unquote(target.split("#", 1)[0])
    if not raw_target or any(char in raw_target for char in MARKDOWN_LINK_TEMPLATE_CHARS):
        return None
    if raw_target.startswith("/"):
        return Path(raw_target)
    return markdown_file.parent / raw_target


def _link_target_exists(markdown_file: Path, target: str) -> bool:
    target_path = _local_target_path(markdown_file, target)
    if target_path is None:
        return True
    return target_path.exists()


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _iter_completed_wave_reference_sources(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    agents_path = repo_root / "AGENTS.md"
    if agents_path.is_file():
        files.append(agents_path)
    docs_path = repo_root / "docs-ai" / "docs"
    wave_dir = docs_path / "initiatives" / "waves"
    if docs_path.is_dir():
        for markdown_file in sorted(docs_path.rglob("*.md")):
            if _is_relative_to(markdown_file.resolve(), wave_dir.resolve()):
                continue
            files.append(markdown_file)
    return sorted(files)


def _is_done_wave_brief(repo_root: Path, target_path: Path) -> bool:
    wave_dir = (repo_root / "docs-ai" / "docs" / "initiatives" / "waves").resolve()
    resolved_target = target_path.resolve()
    if not _is_relative_to(resolved_target, wave_dir):
        return False
    if resolved_target.suffix != ".md" or not resolved_target.is_file():
        return False
    return bool(COMPLETED_WAVE_STATUS_PATTERN.search(resolved_target.read_text(encoding="utf-8")))


def _completed_wave_references(markdown_file: Path, repo_root: Path) -> list[str]:
    text = markdown_file.read_text(encoding="utf-8")
    targets = [match.group(1) for match in MARKDOWN_LINK_PATTERN.finditer(text)]
    targets.extend(match.group(1) for match in INLINE_LOCAL_PATH_PATTERN.finditer(text))
    completed_wave_targets: list[str] = []
    for target in targets:
        target_path = _local_target_path(markdown_file, target)
        if target_path is None:
            continue
        if _is_done_wave_brief(repo_root, target_path):
            completed_wave_targets.append(target)
    return completed_wave_targets


def run_harness_checks(*, repo_root: Path) -> list[CheckFailure]:
    if not repo_root.exists():
        raise GovernanceCommandError(f"Repo root not found: {repo_root}")
    if not repo_root.is_dir():
        raise GovernanceCommandError(f"Repo root is not a directory: {repo_root}")

    failures: list[CheckFailure] = []
    for markdown_file in _iter_markdown_files(repo_root):
        text = markdown_file.read_text(encoding="utf-8")
        broken_links = [
            match.group(1)
            for match in MARKDOWN_LINK_PATTERN.finditer(text)
            if not _link_target_exists(markdown_file, match.group(1))
        ]
        if broken_links:
            failures.append(
                CheckFailure(
                    check_id="docs.cross-doc-links",
                    message=f"{markdown_file.relative_to(repo_root)} has broken markdown links: {', '.join(broken_links)}",
                    remediation="Retarget links to the owning local project doc or global harness reference.",
                )
            )
    for markdown_file in _iter_completed_wave_reference_sources(repo_root):
        completed_wave_targets = _completed_wave_references(markdown_file, repo_root)
        if completed_wave_targets:
            failures.append(
                CheckFailure(
                    check_id="docs.completed-wave-doctrine-reference",
                    message=(
                        f"{markdown_file.relative_to(repo_root)} references completed wave files as durable "
                        f"doctrine: {', '.join(completed_wave_targets)}"
                    ),
                    remediation="Extract retained context to the owning durable doc or valid backlog, then remove the completed-wave reference.",
                )
            )
    return failures


def command_governance_check(
    *,
    repo_root: Path,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        failures = run_harness_checks(repo_root=repo_root.resolve())
    except GovernanceCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    for failure in failures:
        print(f"{failure.check_id}: {failure.message}", file=stdout)
    return 1 if failures else 0
