from __future__ import annotations

import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO

WORK_NOTE_RELATIVE_ROOT = Path("docs-ai/docs/initiatives/work-notes")
CURRENT_WORK_RELATIVE_ROOT = Path("docs-ai/current-work")
IGNORED_PARTS = frozenset({".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", "__pycache__"})
ITEM_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class MemoryCommandError(ValueError):
    pass


@dataclass(frozen=True)
class ReferenceHit:
    path: Path
    line_number: int
    line: str


@dataclass(frozen=True)
class ReferenceReport:
    item: str
    target: Path
    note_refs: tuple[ReferenceHit, ...]
    non_note_refs: tuple[ReferenceHit, ...]


@dataclass(frozen=True)
class CleanupTarget:
    item: str
    item_dir: Path


@dataclass(frozen=True)
class BootstrapResult:
    note_path: Path


def validate_item_id(item: str) -> None:
    if not ITEM_ID_RE.fullmatch(item):
        raise MemoryCommandError(f"Invalid item id: {item!r}")


def resolve_repo_root(repo_root: Path) -> Path:
    resolved = repo_root.resolve()
    if not resolved.exists():
        raise MemoryCommandError(f"Repo root not found: {repo_root}")
    if not resolved.is_dir():
        raise MemoryCommandError(f"Repo root is not a directory: {repo_root}")
    return resolved


def _iter_repo_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for root, dirnames, filenames in os.walk(repo_root):
        root_path = Path(root)
        dirnames[:] = [dirname for dirname in dirnames if dirname not in IGNORED_PARTS]
        if any(part in IGNORED_PARTS for part in root_path.relative_to(repo_root).parts):
            continue
        files.extend(root_path / filename for filename in filenames)
    return sorted(files)


def collect_work_note_references(*, repo_root: Path, item: str) -> ReferenceReport:
    validate_item_id(item)
    resolved_root = resolve_repo_root(repo_root)
    target_relative_path = WORK_NOTE_RELATIVE_ROOT / f"{item}.md"
    target_token = str(target_relative_path)
    target_bytes = target_token.encode("utf-8")
    note_refs: list[ReferenceHit] = []
    non_note_refs: list[ReferenceHit] = []

    for path in _iter_repo_files(resolved_root):
        relative_path = path.relative_to(resolved_root)
        if relative_path == target_relative_path:
            continue
        try:
            raw = path.read_bytes()
        except FileNotFoundError:
            continue
        if target_bytes not in raw:
            continue
        text = raw.decode("utf-8", errors="ignore")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if target_token not in line:
                continue
            hit = ReferenceHit(path=relative_path, line_number=line_number, line=line.strip())
            if relative_path.parent == WORK_NOTE_RELATIVE_ROOT:
                note_refs.append(hit)
            else:
                non_note_refs.append(hit)

    return ReferenceReport(
        item=item,
        target=target_relative_path,
        note_refs=tuple(note_refs),
        non_note_refs=tuple(non_note_refs),
    )


def render_reference_report(report: ReferenceReport) -> str:
    lines = [
        f"item: {report.item}",
        f"target: {report.target}",
        f"note_refs: {len(report.note_refs)}",
    ]
    lines.extend(f"  W {hit.path}:{hit.line_number}: {hit.line}" for hit in report.note_refs)
    lines.append(f"non_note_refs: {len(report.non_note_refs)}")
    lines.extend(f"  N {hit.path}:{hit.line_number}: {hit.line}" for hit in report.non_note_refs)
    return "\n".join(lines)


def resolve_cleanup_target(*, repo_root: Path, item: str) -> CleanupTarget:
    validate_item_id(item)
    resolved_repo = resolve_repo_root(repo_root)
    current_work = resolved_repo / CURRENT_WORK_RELATIVE_ROOT
    return resolve_cleanup_target_from_current_work(current_work_root=current_work, item=item)


def resolve_cleanup_target_from_current_work(*, current_work_root: Path, item: str) -> CleanupTarget:
    validate_item_id(item)
    if current_work_root.is_symlink():
        raise MemoryCommandError(f"Refusing symlink current-work root: {current_work_root}")
    current_work = current_work_root.resolve()
    if not current_work.exists():
        raise MemoryCommandError(f"Current-work root not found: {current_work_root}")
    if not current_work.is_dir():
        raise MemoryCommandError(f"Current-work root is not a directory: {current_work_root}")

    item_dir_raw = current_work / item
    if item_dir_raw.is_symlink():
        raise MemoryCommandError(f"Refusing symlink item directory: {item_dir_raw}")
    if not item_dir_raw.exists():
        raise MemoryCommandError(f"Item directory not found: {item_dir_raw}")
    item_dir = item_dir_raw.resolve()
    if not item_dir.is_dir():
        raise MemoryCommandError(f"Item path is not a directory: {item_dir_raw}")
    try:
        item_dir.relative_to(current_work)
    except ValueError:
        raise MemoryCommandError(f"Resolved item directory escapes current-work root: {item_dir}") from None
    if not (item_dir / "active-work-note.md").exists():
        raise MemoryCommandError(f"Directory is not an active work-note directory: {item_dir_raw}")
    return CleanupTarget(item=item, item_dir=item_dir)


def delete_cleanup_target(target: CleanupTarget) -> int:
    if target.item_dir.is_symlink():
        raise MemoryCommandError(f"Refusing symlink item directory: {target.item_dir}")
    if not target.item_dir.is_dir():
        raise MemoryCommandError(f"Item path is not a directory: {target.item_dir}")
    removed_entries = sum(1 for _ in target.item_dir.rglob("*"))
    shutil.rmtree(target.item_dir)
    return removed_entries


def _default_tasks(tasks: list[str]) -> list[str]:
    return tasks or ["initiative/feature/task-1"]


def _ensure_writable(path: Path, *, force: bool) -> None:
    if path.exists() and not force:
        raise MemoryCommandError(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)


def _render_work_note(*, item: str, title: str, tasks: list[str]) -> str:
    task_lines = "\n".join(f"- `{task}`" for task in tasks)
    return f"""# Work Note {item} - {title}

This note is memory, not authority. Picking it starts discovery through the
delivery workflow; it does not authorize direct execution.

## Remembered Intent

- `<why this map item exists>`

## Starting Points

{task_lines}

## Recheck During Discovery

- `<decision, risk, stale assumption, cleanup, or proof concern>`

## Possible Sequence

- `<rough next work item>`
"""


def bootstrap_work_note(
    *,
    repo_root: Path,
    item: str,
    title: str,
    tasks: list[str],
    force: bool,
) -> BootstrapResult:
    resolved_repo = resolve_repo_root(repo_root)
    validate_item_id(item)
    note_path = resolved_repo / WORK_NOTE_RELATIVE_ROOT / f"{item}.md"
    _ensure_writable(note_path, force=force)
    note_path.write_text(
        _render_work_note(item=item, title=title, tasks=_default_tasks(tasks)),
        encoding="utf-8",
    )
    return BootstrapResult(note_path=note_path)


def command_refs(
    *,
    repo_root: Path,
    item: str,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        report = collect_work_note_references(repo_root=repo_root, item=item)
    except MemoryCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(render_reference_report(report), file=stdout)
    return 0


def command_cleanup(
    *,
    repo_root: Path,
    item: str,
    execute: bool,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        target = resolve_cleanup_target(repo_root=repo_root, item=item)
        if not execute:
            print(f"DRY RUN: {target.item_dir}", file=stdout)
            return 0
        removed_entries = delete_cleanup_target(target)
    except MemoryCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(f"DELETED: {target.item_dir} (removed_entries={removed_entries})", file=stdout)
    return 0


def command_bootstrap(
    *,
    repo_root: Path,
    item: str,
    title: str,
    tasks: list[str],
    force: bool,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        result = bootstrap_work_note(
            repo_root=repo_root,
            item=item,
            title=title,
            tasks=tasks,
            force=force,
        )
    except MemoryCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(f"CREATED: {result.note_path}", file=stdout)
    return 0
