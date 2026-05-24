from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO
from urllib.parse import unquote

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BACKTICK_PATH_PATTERN = re.compile(r"`([^`\s]+)`")
MARKDOWN_LINK_SCAN_ROOTS = ("AGENTS.md", "docs-ai/docs", "docs-ai/current-work")
MARKDOWN_LINK_TEMPLATE_CHARS = ("<", ">", "{", "}", "*")
DOCTRINE_SCAN_ROOTS = ("AGENTS.md", "docs-ai/docs")
WORK_NOTE_MEMORY_PREFIXES = (
    Path("docs-ai/current-work"),
)
LEGACY_WORK_NOTE_ROOT = Path("docs-ai/docs/initiatives/work-notes")


class GovernanceCommandError(ValueError):
    pass


@dataclass(frozen=True)
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


def _relative_to_root(path: Path, repo_root: Path) -> Path | None:
    try:
        return path.resolve(strict=False).relative_to(repo_root.resolve())
    except ValueError:
        return None


def _is_work_note_memory_path(path: Path, repo_root: Path) -> bool:
    relative = _relative_to_root(path, repo_root)
    if relative is None:
        return False
    return any(relative == prefix or prefix in relative.parents for prefix in WORK_NOTE_MEMORY_PREFIXES)


def _iter_doctrine_scan_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for root in DOCTRINE_SCAN_ROOTS:
        path = repo_root / root
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(files)


def _work_note_memory_references(markdown_file: Path, repo_root: Path) -> list[str]:
    text = markdown_file.read_text(encoding="utf-8")
    targets = [match.group(1) for match in MARKDOWN_LINK_PATTERN.finditer(text)]
    targets.extend(
        match.group(1)
        for match in BACKTICK_PATH_PATTERN.finditer(text)
        if "/" in match.group(1) and match.group(1).split("#", 1)[0].endswith(".md")
    )
    references: list[str] = []
    for target in targets:
        target_path = _local_target_path(markdown_file, target)
        if target_path is not None and _is_work_note_memory_path(target_path, repo_root):
            references.append(target)
    return sorted(set(references))


def run_harness_checks(*, repo_root: Path) -> list[CheckFailure]:
    if not repo_root.exists():
        raise GovernanceCommandError(f"Repo root not found: {repo_root}")
    if not repo_root.is_dir():
        raise GovernanceCommandError(f"Repo root is not a directory: {repo_root}")

    failures: list[CheckFailure] = []
    legacy_work_notes = sorted((repo_root / LEGACY_WORK_NOTE_ROOT).glob("*.md"))
    if legacy_work_notes:
        failures.append(
            CheckFailure(
                check_id="docs.work-note-location",
                message=(
                    "work notes live under docs-ai/current-work/work-notes, not durable docs: "
                    + ", ".join(str(path.relative_to(repo_root)) for path in legacy_work_notes)
                ),
                remediation="Move active memory to docs-ai/current-work/work-notes, extract durable content to its owner, or delete completed run history.",
            )
        )
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
                    remediation="Retarget links to the owning local project doc or global overlay reference.",
                )
            )
    for markdown_file in _iter_doctrine_scan_files(repo_root):
        references = _work_note_memory_references(markdown_file, repo_root)
        if references:
            failures.append(
                CheckFailure(
                    check_id="docs.work-note-memory-reference",
                    message=(
                        f"{markdown_file.relative_to(repo_root)} references work-note/current-work memory: "
                        + ", ".join(references)
                    ),
                    remediation="Move retained doctrine to its durable owner or backlog; durable docs must not depend on work-note memory.",
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
