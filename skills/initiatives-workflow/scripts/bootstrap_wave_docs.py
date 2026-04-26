#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import final

REPO_ROOT = Path.cwd()
WAVE_BRIEFS_ROOT = REPO_ROOT / "docs-ai" / "docs" / "initiatives" / "waves"
DISCOVERY_TEMPLATE_REFERENCE = "skills/initiatives-workflow/assets/wave-brief-discovery-required.md"


@dataclass(frozen=True, slots=True)
class BootstrapResult:
    brief_path: Path
    packet_path: Path | None


class BootstrapError(RuntimeError):
    def __init__(self, path: Path) -> None:
        super().__init__(f"Refusing to overwrite existing file without --force: {path}")


class UnsupportedWaveStatusError(RuntimeError):
    def __init__(self, status: str) -> None:
        super().__init__(
            f"bootstrap_wave_docs.py only scaffolds `discovery-required` wave briefs. Refusing unsupported status `{status}`."
        )


@final
class _Args(argparse.Namespace):
    def __init__(self) -> None:
        super().__init__()
        self.wave_id: str = ""
        self.title: str = ""
        self.status: str = "discovery-required"
        self.tasks: list[str] = []
        self.force: bool = False
        self.repo_root: Path = Path.cwd()


def _parse_args() -> _Args:
    parser = argparse.ArgumentParser(description="Scaffold a discovery-required wave brief.")
    _ = parser.add_argument("--wave-id", required=True, help="Durable wave identifier, for example area-topic-1.")
    _ = parser.add_argument("--title", required=True, help="Human-readable wave title.")
    _ = parser.add_argument(
        "--status",
        choices=("discovery-required",),
        default="discovery-required",
        help="Initial wave status. Only discovery-required scaffolding is supported.",
    )
    _ = parser.add_argument(
        "--task",
        action="append",
        dest="tasks",
        default=[],
        help="Task slug to prefill. Repeat for multiple tasks.",
    )
    _ = parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    _ = parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Target project repository root.")
    return parser.parse_args(namespace=_Args())


def _default_tasks(tasks: list[str]) -> list[str]:
    if tasks:
        return tasks
    return ["initiative/feature/task-1"]


def _ensure_writable(path: Path, *, force: bool) -> None:
    if path.exists() and not force:
        raise BootstrapError(path)
    path.parent.mkdir(parents=True, exist_ok=True)


def _render_discovery_brief(*, wave_id: str, title: str, tasks: list[str]) -> str:
    # Keep the scaffold aligned with the source-of-truth discovery template:
    # skills/initiatives-workflow/assets/wave-brief-discovery-required.md
    task_lines = "\n".join(f"- `{task}`" for task in tasks)
    return f"""# Wave {wave_id} - {title}

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


def bootstrap_wave_docs(*, wave_id: str, title: str, status: str, tasks: list[str], force: bool) -> BootstrapResult:
    if status != "discovery-required":
        raise UnsupportedWaveStatusError(status)

    resolved_tasks = _default_tasks(tasks)
    brief_path = WAVE_BRIEFS_ROOT / f"{wave_id}.md"
    packet_path = None

    _ensure_writable(brief_path, force=force)

    brief_body = _render_discovery_brief(wave_id=wave_id, title=title, tasks=resolved_tasks)
    _ = brief_path.write_text(brief_body, encoding="utf-8")

    return BootstrapResult(brief_path=brief_path, packet_path=packet_path)


def main() -> int:
    parser = _parse_args()
    global REPO_ROOT, WAVE_BRIEFS_ROOT
    REPO_ROOT = parser.repo_root.resolve()
    WAVE_BRIEFS_ROOT = REPO_ROOT / "docs-ai" / "docs" / "initiatives" / "waves"
    try:
        _ = bootstrap_wave_docs(
            wave_id=parser.wave_id,
            title=parser.title,
            status=parser.status,
            tasks=list(parser.tasks),
            force=bool(parser.force),
        )
    except (BootstrapError, UnsupportedWaveStatusError) as exc:
        raise SystemExit(str(exc)) from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
