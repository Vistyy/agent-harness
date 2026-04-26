#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MARKDOWN_LINK_SCAN_ROOTS = ("AGENTS.md", "docs-ai/docs", "docs-ai/current-work")
MARKDOWN_LINK_TEMPLATE_CHARS = ("<", ">", "{", "}", "*")


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", nargs="?", default=".")
    args = parser.parse_args()
    failures = run_harness_checks(repo_root=Path(args.repo_root).resolve())
    for failure in failures:
        print(f"{failure.check_id}: {failure.message}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
