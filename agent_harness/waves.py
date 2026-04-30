from __future__ import annotations

import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO

WAVE_BRIEF_RELATIVE_ROOT = Path("docs-ai/docs/initiatives/waves")
CURRENT_WORK_RELATIVE_ROOT = Path("docs-ai/current-work")
DISCOVERY_TEMPLATE_REFERENCE = "skills/initiatives-workflow/assets/wave-brief-discovery-required.md"
IGNORED_PARTS = frozenset({".git"})
WAVE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class WaveCommandError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class ReferenceHit:
    path: Path
    line_number: int
    line: str


@dataclass(frozen=True, slots=True)
class ReferenceReport:
    wave: str
    target: Path
    wave_refs: tuple[ReferenceHit, ...]
    non_wave_refs: tuple[ReferenceHit, ...]


@dataclass(frozen=True, slots=True)
class CleanupTarget:
    wave: str
    wave_dir: Path


@dataclass(frozen=True, slots=True)
class BootstrapResult:
    brief_path: Path
    packet_path: Path | None


def validate_wave_id(wave: str) -> None:
    if not WAVE_ID_RE.fullmatch(wave):
        raise WaveCommandError(f"Invalid wave id: {wave!r}")


def resolve_repo_root(repo_root: Path) -> Path:
    resolved = repo_root.resolve()
    if not resolved.exists():
        raise WaveCommandError(f"Repo root not found: {repo_root}")
    if not resolved.is_dir():
        raise WaveCommandError(f"Repo root is not a directory: {repo_root}")
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


def collect_wave_brief_references(*, repo_root: Path, wave: str) -> ReferenceReport:
    validate_wave_id(wave)
    resolved_root = resolve_repo_root(repo_root)
    target_relative_path = WAVE_BRIEF_RELATIVE_ROOT / f"{wave}.md"
    target_token = str(target_relative_path)
    target_bytes = target_token.encode("utf-8")
    wave_refs: list[ReferenceHit] = []
    non_wave_refs: list[ReferenceHit] = []

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
            if relative_path.parent == WAVE_BRIEF_RELATIVE_ROOT:
                wave_refs.append(hit)
            else:
                non_wave_refs.append(hit)

    return ReferenceReport(
        wave=wave,
        target=target_relative_path,
        wave_refs=tuple(wave_refs),
        non_wave_refs=tuple(non_wave_refs),
    )


def render_reference_report(report: ReferenceReport) -> str:
    lines = [
        f"wave: {report.wave}",
        f"target: {report.target}",
        f"wave_refs: {len(report.wave_refs)}",
    ]
    lines.extend(f"  W {hit.path}:{hit.line_number}: {hit.line}" for hit in report.wave_refs)
    lines.append(f"non_wave_refs: {len(report.non_wave_refs)}")
    lines.extend(f"  N {hit.path}:{hit.line_number}: {hit.line}" for hit in report.non_wave_refs)
    return "\n".join(lines)


def resolve_cleanup_target(*, repo_root: Path, wave: str) -> CleanupTarget:
    validate_wave_id(wave)
    resolved_repo = resolve_repo_root(repo_root)
    current_work_raw = resolved_repo / CURRENT_WORK_RELATIVE_ROOT
    return resolve_cleanup_target_from_current_work(current_work_root=current_work_raw, wave=wave)


def resolve_cleanup_target_from_current_work(*, current_work_root: Path, wave: str) -> CleanupTarget:
    validate_wave_id(wave)
    if current_work_root.is_symlink():
        raise WaveCommandError(f"Refusing symlink current-work root: {current_work_root}")
    current_work = current_work_root.resolve()
    if not current_work.exists():
        raise WaveCommandError(f"Current-work root not found: {current_work_root}")
    if not current_work.is_dir():
        raise WaveCommandError(f"Current-work root is not a directory: {current_work_root}")

    wave_dir_raw = current_work / wave
    if wave_dir_raw.is_symlink():
        raise WaveCommandError(f"Refusing symlink wave directory: {wave_dir_raw}")
    if not wave_dir_raw.exists():
        raise WaveCommandError(f"Wave directory not found: {wave_dir_raw}")
    wave_dir = wave_dir_raw.resolve()
    if not wave_dir.is_dir():
        raise WaveCommandError(f"Wave path is not a directory: {wave_dir_raw}")
    try:
        wave_dir.relative_to(current_work)
    except ValueError:
        raise WaveCommandError(f"Resolved wave directory escapes current-work root: {wave_dir}") from None
    if not (wave_dir / "wave-execution.md").exists():
        raise WaveCommandError(f"Directory is not a wave execution directory: {wave_dir_raw}")
    return CleanupTarget(wave=wave, wave_dir=wave_dir)


def delete_cleanup_target(target: CleanupTarget) -> int:
    if target.wave_dir.is_symlink():
        raise WaveCommandError(f"Refusing symlink wave directory: {target.wave_dir}")
    if not target.wave_dir.is_dir():
        raise WaveCommandError(f"Wave path is not a directory: {target.wave_dir}")
    removed_entries = sum(1 for _ in target.wave_dir.rglob("*"))
    shutil.rmtree(target.wave_dir)
    return removed_entries


def _default_tasks(tasks: list[str]) -> list[str]:
    if tasks:
        return tasks
    return ["initiative/feature/task-1"]


def _ensure_writable(path: Path, *, force: bool) -> None:
    if path.exists() and not force:
        raise WaveCommandError(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)


def _render_discovery_brief(*, wave: str, title: str, tasks: list[str]) -> str:
    task_lines = "\n".join(f"- `{task}`" for task in tasks)
    return f"""# Wave {wave} - {title}

**Status:** discovery-required

## Problem

<why this wave exists and what current weakness it addresses>

## Objective

<what changes when this wave succeeds>

## In Scope

{task_lines}

## Out Of Scope

- `<explicitly deferred scope>`

## Constraints / Non-Goals

- `<constraint>`

## Risks / Dependencies

- `<dependency or risk with disposition>`

## References

- `<owner doc / prior wave / key code path>`
"""


def bootstrap_wave_docs(
    *,
    repo_root: Path,
    wave: str,
    title: str,
    status: str,
    tasks: list[str],
    force: bool,
) -> BootstrapResult:
    resolved_repo = resolve_repo_root(repo_root)
    validate_wave_id(wave)
    if status != "discovery-required":
        raise WaveCommandError(
            f"wave bootstrap only scaffolds `discovery-required` wave briefs. Refusing unsupported status `{status}`."
        )

    brief_path = resolved_repo / WAVE_BRIEF_RELATIVE_ROOT / f"{wave}.md"
    _ensure_writable(brief_path, force=force)
    brief_body = _render_discovery_brief(wave=wave, title=title, tasks=_default_tasks(tasks))
    brief_path.write_text(brief_body, encoding="utf-8")
    return BootstrapResult(brief_path=brief_path, packet_path=None)


def command_wave_refs(
    *,
    repo_root: Path,
    wave: str,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        report = collect_wave_brief_references(repo_root=repo_root, wave=wave)
    except WaveCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(render_reference_report(report), file=stdout)
    return 0


def command_wave_cleanup(
    *,
    repo_root: Path,
    wave: str,
    execute: bool,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        target = resolve_cleanup_target(repo_root=repo_root, wave=wave)
        if not execute:
            print(f"DRY RUN: {target.wave_dir}", file=stdout)
            return 0
        removed_entries = delete_cleanup_target(target)
    except WaveCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(f"DELETED: {target.wave_dir} (removed_entries={removed_entries})", file=stdout)
    return 0


def command_wave_bootstrap(
    *,
    repo_root: Path,
    wave: str,
    title: str,
    status: str,
    tasks: list[str],
    force: bool,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        result = bootstrap_wave_docs(
            repo_root=repo_root,
            wave=wave,
            title=title,
            status=status,
            tasks=tasks,
            force=force,
        )
    except WaveCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(f"CREATED: {result.brief_path}", file=stdout)
    return 0
