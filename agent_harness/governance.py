from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO
from urllib.parse import unquote

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MARKDOWN_LINK_SCAN_ROOTS = ("AGENTS.md", "docs-ai/docs", "docs-ai/current-work")
MARKDOWN_LINK_TEMPLATE_CHARS = ("<", ">", "{", "}", "*")


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


def _link_target_exists(markdown_file: Path, target: str) -> bool:
    if "://" in target or target.startswith("#"):
        return True
    raw_target = unquote(target.split("#", 1)[0])
    if not raw_target or any(char in raw_target for char in MARKDOWN_LINK_TEMPLATE_CHARS):
        return True
    if raw_target.startswith("/"):
        return Path(raw_target).exists()
    return (markdown_file.parent / raw_target).exists()


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
