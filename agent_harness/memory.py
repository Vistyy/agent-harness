from __future__ import annotations

import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO
from urllib.parse import unquote

WORK_NOTE_RELATIVE_ROOT = Path("docs-ai/current-work/work-notes")
CURRENT_WORK_RELATIVE_ROOT = Path("docs-ai/current-work")
ACTIVE_WORK_RELATIVE_ROOT = CURRENT_WORK_RELATIVE_ROOT / "active"
IGNORED_PARTS = frozenset({".fallow", ".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", "__pycache__"})
ITEM_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BACKTICK_PATH_PATTERN = re.compile(r"`([^`\s]+)`")
LOCAL_PATH_ROOTS = frozenset({"docs-ai", ".codex", "AGENTS.md", "README.md"})
MARKDOWN_LINK_TEMPLATE_CHARS = ("<", ">", "{", "}", "*")


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


@dataclass(frozen=True)
class LifecycleReport:
    item: str
    active_dir: Path
    active_note_exists: bool
    draft_notes: tuple[Path, ...]
    work_note: Path
    work_note_exists: bool
    backlog_details: tuple[Path, ...]
    delivery_map: Path
    delivery_map_exists: bool
    reference_report: ReferenceReport
    memory_refs: tuple[ReferenceHit, ...]


@dataclass(frozen=True)
class ActiveNoteStatus:
    item: str
    path: Path
    slice_statuses: tuple[tuple[str, int], ...]
    review_states: tuple[tuple[str, int], ...]
    invalid_slice_statuses: tuple[tuple[str, int], ...]
    invalid_review_states: tuple[tuple[str, int], ...]
    required_slices_missing_status: int
    required_slices_missing_review_state: int
    closeout: tuple[str, ...]


@dataclass(frozen=True)
class BacklogDetailStatus:
    item: str
    path: Path
    status: str
    owner: str
    bucket: str
    queue_state: str


@dataclass(frozen=True)
class QueuedItemStatus:
    item: str
    path: Path
    queue_state: str


@dataclass(frozen=True)
class MemoryOwnerConflict:
    item: str
    active_note: Path
    work_note: Path


@dataclass(frozen=True)
class MemoryStatusReport:
    delivery_map: Path
    delivery_map_exists: bool
    active_notes: tuple[ActiveNoteStatus, ...]
    work_notes: tuple[QueuedItemStatus, ...]
    owner_conflicts: tuple[MemoryOwnerConflict, ...]
    backlog_details: tuple[BacklogDetailStatus, ...]


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


def _read_text_file(path: Path) -> str | None:
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        return None
    if b"\0" in raw:
        return None
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return None


def _local_target_path(*, repo_root: Path, source_path: Path, target: str) -> Path | None:
    if "://" in target or target.startswith("#"):
        return None
    raw_target = unquote(target.split("#", 1)[0])
    if not raw_target or any(char in raw_target for char in MARKDOWN_LINK_TEMPLATE_CHARS):
        return None
    raw_path = Path(raw_target)
    if raw_path.is_absolute():
        return raw_path
    if raw_path.parts and raw_path.parts[0] in LOCAL_PATH_ROOTS:
        return repo_root / raw_path
    return source_path.parent / raw_path


def _line_references_path(*, repo_root: Path, source_path: Path, line: str, target_path: Path) -> bool:
    targets = [match.group(1) for match in MARKDOWN_LINK_PATTERN.finditer(line)]
    targets.extend(
        match.group(1)
        for match in BACKTICK_PATH_PATTERN.finditer(line)
        if "/" in match.group(1) and match.group(1).split("#", 1)[0].endswith(".md")
    )
    for target in targets:
        resolved = _local_target_path(repo_root=repo_root, source_path=source_path, target=target)
        if resolved is not None and resolved.resolve(strict=False) == target_path.resolve(strict=False):
            return True
    return False


def collect_work_note_references(*, repo_root: Path, item: str) -> ReferenceReport:
    validate_item_id(item)
    resolved_root = resolve_repo_root(repo_root)
    target_relative_path = WORK_NOTE_RELATIVE_ROOT / f"{item}.md"
    target_path = resolved_root / target_relative_path
    note_refs: list[ReferenceHit] = []
    non_note_refs: list[ReferenceHit] = []

    for path in _iter_repo_files(resolved_root):
        relative_path = path.relative_to(resolved_root)
        if relative_path == target_relative_path:
            continue
        text = _read_text_file(path)
        if text is None:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not _line_references_path(
                repo_root=resolved_root,
                source_path=path,
                line=line,
                target_path=target_path,
            ):
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


def _collect_token_references(*, repo_root: Path, tokens: tuple[str, ...]) -> tuple[ReferenceHit, ...]:
    hits: list[ReferenceHit] = []
    for path in _iter_repo_files(repo_root):
        relative_path = path.relative_to(repo_root)
        text = _read_text_file(path)
        if text is None:
            continue
        if not any(token in text for token in tokens):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if any(token in line for token in tokens):
                hits.append(ReferenceHit(path=relative_path, line_number=line_number, line=line.strip()))
    return tuple(hits)


def collect_memory_lifecycle(*, repo_root: Path, item: str) -> LifecycleReport:
    validate_item_id(item)
    resolved_root = resolve_repo_root(repo_root)
    current_work = resolved_root / CURRENT_WORK_RELATIVE_ROOT
    active_dir = ACTIVE_WORK_RELATIVE_ROOT / item
    active_dir_path = resolved_root / active_dir
    active_note = active_dir_path / "active-work-note.md"
    draft_notes = tuple(
        path.relative_to(resolved_root)
        for path in sorted(active_dir_path.glob("active-work-note*.draft.md"))
    ) if active_dir_path.is_dir() else ()
    work_note = WORK_NOTE_RELATIVE_ROOT / f"{item}.md"
    backlog_root = resolved_root / CURRENT_WORK_RELATIVE_ROOT / "backlog"
    backlog_details = tuple(
        path.relative_to(resolved_root)
        for path in sorted(backlog_root.glob(f"*__{item}.md"))
    ) if backlog_root.is_dir() else ()
    delivery_map = CURRENT_WORK_RELATIVE_ROOT / "delivery-map.md"
    reference_report = collect_work_note_references(repo_root=resolved_root, item=item)
    memory_tokens = (
        str(active_dir),
        str(active_dir / "active-work-note.md"),
        *(str(path) for path in backlog_details),
    )
    memory_refs = _collect_token_references(repo_root=resolved_root, tokens=memory_tokens)
    return LifecycleReport(
        item=item,
        active_dir=active_dir,
        active_note_exists=active_note.exists(),
        draft_notes=draft_notes,
        work_note=work_note,
        work_note_exists=(resolved_root / work_note).exists(),
        backlog_details=backlog_details,
        delivery_map=delivery_map,
        delivery_map_exists=(current_work / "delivery-map.md").exists(),
        reference_report=reference_report,
        memory_refs=memory_refs,
    )


def _present(value: bool) -> str:
    return "present" if value else "missing"


def render_lifecycle_report(report: LifecycleReport) -> str:
    lines = [
        f"item: {report.item}",
        "artifacts:",
        f"  active_dir: {report.active_dir}",
        f"  active_note: {_present(report.active_note_exists)}",
        f"  draft_notes: {len(report.draft_notes)}",
    ]
    lines.extend(f"    {path}" for path in report.draft_notes)
    lines.extend(
        [
            f"  work_note: {_present(report.work_note_exists)} {report.work_note}",
        ]
    )
    if report.active_note_exists and report.work_note_exists:
        lines.append(
            "  owner_conflict: active note and work note both exist; "
            "promote retained context to the active note and delete or retire the work note"
        )
    lines.append(f"  backlog_details: {len(report.backlog_details)}")
    lines.extend(f"    {path}" for path in report.backlog_details)
    lines.extend(
        [
            f"  delivery_map: {_present(report.delivery_map_exists)} {report.delivery_map}",
            "references:",
            f"  work_note_peer_refs: {len(report.reference_report.note_refs)}",
        ]
    )
    lines.extend(
        f"    W {hit.path}:{hit.line_number}: {hit.line}"
        for hit in report.reference_report.note_refs
    )
    lines.append(f"  work_note_non_note_refs: {len(report.reference_report.non_note_refs)}")
    lines.extend(
        f"    N {hit.path}:{hit.line_number}: {hit.line}"
        for hit in report.reference_report.non_note_refs
    )
    lines.append(f"  active_or_backlog_refs: {len(report.memory_refs)}")
    lines.extend(f"    M {hit.path}:{hit.line_number}: {hit.line}" for hit in report.memory_refs)
    lines.extend(
        [
            "closeout:",
            "  choose one disposition per artifact: delete | extract | backlog | keep active",
            f"  active-note cleanup dry-run: agent-harness memory cleanup --repo-root <project-root> --item {report.item}",
        ]
    )
    return "\n".join(lines)


def _extract_heading_section(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    in_section = False
    section: list[str] = []
    for line in lines:
        if line.startswith("## "):
            in_section = line.strip() == f"## {heading}"
            continue
        if in_section:
            section.append(line)
    return section


def _section_list_items(lines: list[str]) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    for line in lines:
        if line.startswith("- "):
            if current:
                items.append(" ".join(part.strip() for part in current))
            current = [line]
            continue
        if current and line.startswith((" ", "\t")):
            current.append(line)
    if current:
        items.append(" ".join(part.strip() for part in current))
    return items


SLICE_STATUS_VALUES = frozenset(
    {"pending", "implementing", "completed", "blocked", "removed by user-accepted reduction"}
)
REVIEW_STATE_VALUES = frozenset({"pending", "quality_guard pending", "passed", "blocked"})
QUEUE_STATE_VALUES = frozenset({"ready", "waiting", "deferred"})


def _field_value(item: str, field: str) -> str | None:
    pattern = re.compile(rf"{re.escape(field)}\s*=\s*([^;,.`]+)")
    match = pattern.search(item)
    return match.group(1).strip() if match else None


def _count_values(values: list[str]) -> tuple[tuple[str, int], ...]:
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return tuple(sorted(counts.items()))


def _extract_active_note_status(path: Path, repo_root: Path) -> ActiveNoteStatus:
    text = _read_text_file(path) or ""
    required_slice_items = [
        item
        for heading in ("Required Slices", "Required Claims")
        for item in _section_list_items(_extract_heading_section(text, heading))
        if not item.startswith("- blocker/escape hatch:")
    ]
    raw_slice_statuses = [_field_value(item, "status") for item in required_slice_items]
    raw_review_states = [_field_value(item, "review state") for item in required_slice_items]
    slice_statuses = [value for value in raw_slice_statuses if value in SLICE_STATUS_VALUES]
    review_states = [value for value in raw_review_states if value in REVIEW_STATE_VALUES]
    invalid_slice_statuses = [
        value for value in raw_slice_statuses if value is not None and value not in SLICE_STATUS_VALUES
    ]
    invalid_review_states = [
        value for value in raw_review_states if value is not None and value not in REVIEW_STATE_VALUES
    ]
    missing_status_count = sum(1 for value in raw_slice_statuses if value is None)
    missing_review_state_count = sum(1 for value in raw_review_states if value is None)
    closeout = tuple(
        line.strip()
        for line in _extract_heading_section(text, "Closeout")
        if line.strip().startswith("- ")
    )
    return ActiveNoteStatus(
        item=path.parent.name,
        path=path.relative_to(repo_root),
        slice_statuses=_count_values(slice_statuses),
        review_states=_count_values(review_states),
        invalid_slice_statuses=_count_values(invalid_slice_statuses),
        invalid_review_states=_count_values(invalid_review_states),
        required_slices_missing_status=missing_status_count,
        required_slices_missing_review_state=missing_review_state_count,
        closeout=closeout,
    )


def _metadata_value(text: str, field: str) -> str:
    pattern = re.compile(rf"^-\s*{re.escape(field)}:\s*`?([^`\n]+?)`?\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else "unknown"


def _extract_backlog_detail_status(path: Path, repo_root: Path) -> BacklogDetailStatus:
    text = _read_text_file(path) or ""
    return BacklogDetailStatus(
        item=path.stem.replace("__", "/"),
        path=path.relative_to(repo_root),
        status=_metadata_value(text, "status"),
        owner=_metadata_value(text, "owner"),
        bucket=_metadata_value(text, "bucket"),
        queue_state=_metadata_value(text, "queue state"),
    )


def _extract_queued_item_status(path: Path, repo_root: Path) -> QueuedItemStatus:
    text = _read_text_file(path) or ""
    return QueuedItemStatus(
        item=path.stem,
        path=path.relative_to(repo_root),
        queue_state=_metadata_value(text, "queue state"),
    )


def collect_memory_status(*, repo_root: Path) -> MemoryStatusReport:
    resolved_root = resolve_repo_root(repo_root)
    delivery_map = CURRENT_WORK_RELATIVE_ROOT / "delivery-map.md"
    active_notes: list[ActiveNoteStatus] = []
    active_root = resolved_root / ACTIVE_WORK_RELATIVE_ROOT
    if active_root.is_dir():
        for child in sorted(active_root.iterdir()):
            if not child.is_dir():
                continue
            active_note = child / "active-work-note.md"
            if active_note.is_file():
                active_notes.append(_extract_active_note_status(active_note, resolved_root))
    work_notes_root = resolved_root / WORK_NOTE_RELATIVE_ROOT
    work_notes = tuple(
        _extract_queued_item_status(path, resolved_root)
        for path in sorted(work_notes_root.glob("*.md"))
    ) if work_notes_root.is_dir() else ()
    backlog_root = resolved_root / CURRENT_WORK_RELATIVE_ROOT / "backlog"
    backlog_details = tuple(
        _extract_backlog_detail_status(path, resolved_root)
        for path in sorted(backlog_root.glob("*.md"))
    ) if backlog_root.is_dir() else ()
    active_by_item = {note.item: note.path for note in active_notes}
    owner_conflicts = tuple(
        MemoryOwnerConflict(
            item=queued.item,
            active_note=active_by_item[queued.item],
            work_note=queued.path,
        )
        for queued in work_notes
        if queued.item in active_by_item
    )
    return MemoryStatusReport(
        delivery_map=delivery_map,
        delivery_map_exists=(resolved_root / delivery_map).exists(),
        active_notes=tuple(active_notes),
        work_notes=work_notes,
        owner_conflicts=owner_conflicts,
        backlog_details=backlog_details,
    )


def render_memory_status(report: MemoryStatusReport) -> str:
    lines = [
        "work_state_status:",
        f"  delivery_map: {_present(report.delivery_map_exists)} {report.delivery_map}",
        f"  active_control_sheets: {len(report.active_notes)}",
    ]
    for note in report.active_notes:
        lines.append(f"    A {note.item}: {note.path}")
        if note.slice_statuses:
            statuses = ", ".join(f"{status}={count}" for status, count in note.slice_statuses)
            lines.append(f"      claim_statuses: {statuses}")
        else:
            lines.append("      claim_statuses: none")
        if note.review_states:
            review_states = ", ".join(f"{state}={count}" for state, count in note.review_states)
            lines.append(f"      review_states: {review_states}")
        else:
            lines.append("      review_states: none")
        if note.invalid_slice_statuses:
            invalid_statuses = ", ".join(f"{status}={count}" for status, count in note.invalid_slice_statuses)
            lines.append(f"      invalid_claim_statuses: {invalid_statuses}")
        if note.invalid_review_states:
            invalid_states = ", ".join(f"{state}={count}" for state, count in note.invalid_review_states)
            lines.append(f"      invalid_review_states: {invalid_states}")
        if note.required_slices_missing_status:
            lines.append(f"      required_claims_missing_status: {note.required_slices_missing_status}")
        if note.required_slices_missing_review_state:
            lines.append(f"      required_claims_missing_review_state: {note.required_slices_missing_review_state}")
        if note.closeout:
            closeout = "; ".join(line.removeprefix("- ").strip() for line in note.closeout)
            lines.append(f"      closeout: {closeout}")
    lines.append(f"  queued_items: {len(report.work_notes)}")
    lines.extend(f"    Q {queued.item}: {queued.path} queue_state={queued.queue_state}" for queued in report.work_notes)
    lines.append(f"  owner_conflicts: {len(report.owner_conflicts)}")
    lines.extend(
        f"    ! {conflict.item}: active={conflict.active_note} queued={conflict.work_note}; "
        "promote retained context to active and delete or retire the queued item"
        for conflict in report.owner_conflicts
    )
    lines.append(f"  backlog_details: {len(report.backlog_details)}")
    lines.extend(
        f"    B {detail.item}: {detail.path} status={detail.status} owner={detail.owner} "
        f"bucket={detail.bucket} queue_state={detail.queue_state}"
        for detail in report.backlog_details
    )
    return "\n".join(lines)


def collect_work_state_check_errors(report: MemoryStatusReport) -> tuple[str, ...]:
    errors: list[str] = []
    if not report.delivery_map_exists:
        errors.append(f"missing delivery map: {report.delivery_map}")
    errors.extend(
        f"owner conflict for {conflict.item}: active={conflict.active_note} queued={conflict.work_note}"
        for conflict in report.owner_conflicts
    )
    for queued in report.work_notes:
        if queued.queue_state not in QUEUE_STATE_VALUES:
            errors.append(f"{queued.path}: invalid or missing queue state {queued.queue_state!r}")
    for detail in report.backlog_details:
        if detail.queue_state not in QUEUE_STATE_VALUES:
            errors.append(f"{detail.path}: invalid or missing queue state {detail.queue_state!r}")
    for note in report.active_notes:
        for status, count in note.invalid_slice_statuses:
            errors.append(f"{note.path}: invalid claim status {status!r} ({count})")
        for state, count in note.invalid_review_states:
            errors.append(f"{note.path}: invalid review state {state!r} ({count})")
        if note.required_slices_missing_status:
            errors.append(f"{note.path}: required claims missing status ({note.required_slices_missing_status})")
        if note.required_slices_missing_review_state:
            errors.append(
                f"{note.path}: required claims missing review state ({note.required_slices_missing_review_state})"
            )
    return tuple(errors)


def render_work_state_check(errors: tuple[str, ...]) -> str:
    if not errors:
        return "work_state_check: pass"
    lines = ["work_state_check: fail", "errors:"]
    lines.extend(f"  - {error}" for error in errors)
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

    active_root_raw = current_work / "active"
    if active_root_raw.is_symlink():
        raise MemoryCommandError(f"Refusing symlink active-work root: {active_root_raw}")
    if not active_root_raw.exists():
        raise MemoryCommandError(f"Active-work root not found: {active_root_raw}")
    if not active_root_raw.is_dir():
        raise MemoryCommandError(f"Active-work root is not a directory: {active_root_raw}")

    item_dir_raw = active_root_raw / item
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
    return f"""# Queued Work Item: {item}

This queued item is memory, not authority. Picking it starts discovery through
solution-shaping; it does not authorize direct execution. It is queued starting
context, not active progress state.

## Queue

- problem: {title}
- queue state: `ready`
- owner or suspected owner: `<owner>`
- next discovery move: `<smallest useful probe>`

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


def command_lifecycle(
    *,
    repo_root: Path,
    item: str,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        report = collect_memory_lifecycle(repo_root=repo_root, item=item)
    except MemoryCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(render_lifecycle_report(report), file=stdout)
    return 0


def command_status(
    *,
    repo_root: Path,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        report = collect_memory_status(repo_root=repo_root)
    except MemoryCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    print(render_memory_status(report), file=stdout)
    return 0


def command_work_state_check(
    *,
    repo_root: Path,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    stdout = sys.stdout if stdout is None else stdout
    stderr = sys.stderr if stderr is None else stderr
    try:
        report = collect_memory_status(repo_root=repo_root)
    except MemoryCommandError as exc:
        print(str(exc), file=stderr)
        return 1
    errors = collect_work_state_check_errors(report)
    output = render_work_state_check(errors)
    print(output, file=stderr if errors else stdout)
    return 1 if errors else 0


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
