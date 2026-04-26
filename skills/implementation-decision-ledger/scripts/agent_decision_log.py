#!/usr/bin/env python3
# ruff: noqa: T201,TRY003,TRY004
from __future__ import annotations

import argparse
import json
import os
import re
from collections.abc import Callable, Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import cast

DEFAULT_OUTPUT_DIR = Path(".artifacts/agent-decisions")
ACTIVE_RUNS_FILE = ".active-runs-by-scope.json"
ENTRY_TYPES = ("meta", "decision", "assumption")
IMPACT_LEVELS = ("low", "medium", "high")
DURABILITY_LEVELS = ("ephemeral", "restart-safe", "multi-instance-safe")
CONFIDENCE_MIN = 1
CONFIDENCE_MAX = 5
JsonObject = dict[str, object]


def _utc_timestamp_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _utc_timestamp_compact() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")
    return slug or "workspace"


def _generate_run_id() -> str:
    workspace_slug = _slugify(Path.cwd().name)
    return f"{_utc_timestamp_compact()}-{workspace_slug}-{os.getpid()}"


def _validate_confidence(value: str) -> int:
    parsed = int(value)
    if parsed < CONFIDENCE_MIN or parsed > CONFIDENCE_MAX:
        raise argparse.ArgumentTypeError("confidence must be between 1 and 5")
    return parsed


def _resolve_log_path(*, output_dir: Path, run_id: str) -> Path:
    return output_dir / f"{run_id}.jsonl"


def _resolve_review_path(*, output_dir: Path, run_id: str) -> Path:
    return output_dir / f"{run_id}-review.md"


def _resolve_active_runs_path(*, output_dir: Path) -> Path:
    return output_dir / ACTIVE_RUNS_FILE


def _load_active_runs(*, path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        loaded = cast(object, json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(loaded, dict):
        return {}
    loaded_mapping = cast(dict[object, object], loaded)
    return {
        raw_scope: raw_run_id
        for raw_scope, raw_run_id in loaded_mapping.items()
        if isinstance(raw_scope, str) and isinstance(raw_run_id, str) and raw_scope and raw_run_id
    }


def _save_active_runs(*, path: Path, runs: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _ = path.write_text(json.dumps(runs, sort_keys=True), encoding="utf-8")


def _resolve_or_create_run_id(*, output_dir: Path, scope: str, explicit_run_id: str | None) -> str:
    active_runs_path = _resolve_active_runs_path(output_dir=output_dir)
    active_runs = _load_active_runs(path=active_runs_path)

    if explicit_run_id is not None:
        active_runs[scope] = explicit_run_id
        _save_active_runs(path=active_runs_path, runs=active_runs)
        return explicit_run_id

    existing_run_id = active_runs.get(scope)
    if existing_run_id:
        existing_review_path = _resolve_review_path(output_dir=output_dir, run_id=existing_run_id)
        if not existing_review_path.exists():
            return existing_run_id

    new_run_id = _generate_run_id()
    active_runs[scope] = new_run_id
    _save_active_runs(path=active_runs_path, runs=active_runs)
    return new_run_id


def _resolve_run_id_from_scope(*, output_dir: Path, scope: str) -> str:
    active_runs_path = _resolve_active_runs_path(output_dir=output_dir)
    active_runs = _load_active_runs(path=active_runs_path)
    run_id = active_runs.get(scope)
    if run_id is None:
        raise ValueError(f"No active run found for scope: {scope}")
    return run_id


def _close_active_run_id(*, output_dir: Path, run_id: str) -> None:
    active_runs_path = _resolve_active_runs_path(output_dir=output_dir)
    active_runs = _load_active_runs(path=active_runs_path)
    updated_runs = {scope: active_run_id for scope, active_run_id in active_runs.items() if active_run_id != run_id}
    _save_active_runs(path=active_runs_path, runs=updated_runs)


def _close_active_scope(*, output_dir: Path, scope: str) -> None:
    active_runs_path = _resolve_active_runs_path(output_dir=output_dir)
    active_runs = _load_active_runs(path=active_runs_path)
    _ = active_runs.pop(scope, None)
    _save_active_runs(path=active_runs_path, runs=active_runs)


def _append_jsonl(*, path: Path, entry: JsonObject) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        _ = handle.write(json.dumps(entry, ensure_ascii=True))
        _ = handle.write("\n")


def _load_entries(path: Path) -> list[JsonObject]:
    if not path.exists():
        raise FileNotFoundError(f"Log path does not exist: {path}")

    entries: list[JsonObject] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                parsed = cast(object, json.loads(stripped))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL row at line {line_number}: {exc}") from exc
            if not isinstance(parsed, dict):
                raise ValueError(f"Invalid JSONL row at line {line_number}: row must be an object")
            entries.append(cast(JsonObject, parsed))
    return entries


def _build_review_markdown(*, log_path: Path, entries: list[JsonObject]) -> str:
    run_id = log_path.stem
    generated_at = _utc_timestamp_iso()

    counts: dict[str, int] = {}
    for entry in entries:
        entry_type = str(entry.get("entry_type", "unknown"))
        counts[entry_type] = counts.get(entry_type, 0) + 1

    needs_review = [entry for entry in entries if bool(entry.get("needs_review", False)) or not bool(entry.get("resolved", True))]

    lines = [
        "# Agent Decision Review",
        "",
        f"- Log path: `{log_path}`",
        f"- Generated at (UTC): `{generated_at}`",
        f"- Total entries: `{len(entries)}`",
        "",
        "## Counts By Type",
        "",
    ]

    if counts:
        lines.extend(f"- `{entry_type}`: `{counts[entry_type]}`" for entry_type in sorted(counts.keys()))
    else:
        lines.append("- _none_")

    durability_counts: dict[str, int] = {}
    for entry in entries:
        durability = str(entry.get("durability", "unknown"))
        durability_counts[durability] = durability_counts.get(durability, 0) + 1

    lines.extend(["", "## Counts By Durability", ""])
    if durability_counts:
        lines.extend(f"- `{durability}`: `{durability_counts[durability]}`" for durability in sorted(durability_counts.keys()))
    else:
        lines.append("- _none_")

    lines.extend(["", "## Needs Review", ""])
    if not needs_review:
        lines.append("- _none_")
    else:
        for entry in needs_review:
            details = (
                f"{entry.get('entry_type', 'unknown')} | "
                f"impact={entry.get('impact', 'unknown')} | "
                f"durability={entry.get('durability', 'unknown')} | "
                f"confidence={entry.get('confidence', 'unknown')} | "
                f"agent={entry.get('agent', 'unknown')} | "
                f"scope={entry.get('scope', 'unknown')}"
            )
            lines.append(f"- [open] {details}")
            lines.append(f"  - summary: {entry.get('summary', '')}")
            lines.append(f"  - rationale: {entry.get('rationale', '')}")
            lines.append(f"  - timestamp: {entry.get('timestamp', '')}")

    # Keep run_id visible for easy copy/paste in follow-up commands.
    lines.extend(["", f"<!-- run_id: {run_id} -->", ""])
    return "\n".join(lines)


def _cmd_log(args: argparse.Namespace) -> int:
    output_dir = Path(cast(str, args.output_dir))
    run_id = _resolve_or_create_run_id(
        output_dir=output_dir,
        scope=cast(str, args.scope),
        explicit_run_id=cast(str | None, args.run_id),
    )
    log_path = _resolve_log_path(output_dir=output_dir, run_id=run_id)

    if cast(bool, args.resolved):
        resolved = True
    elif cast(bool, args.unresolved):
        resolved = False
    else:
        resolved = not cast(bool, args.needs_review)

    entry: JsonObject = {
        "timestamp": _utc_timestamp_iso(),
        "run_id": run_id,
        "agent": cast(str, args.agent),
        "scope": cast(str, args.scope),
        "entry_type": cast(str, args.entry_type),
        "summary": cast(str, args.summary),
        "rationale": cast(str, args.rationale),
        "confidence": cast(int, args.confidence),
        "impact": cast(str, args.impact),
        "durability": cast(str, args.durability),
        "needs_review": cast(bool, args.needs_review),
        "resolved": resolved,
    }

    _append_jsonl(path=log_path, entry=entry)
    print(f"run_id={run_id}")
    print(f"log_path={log_path}")
    return 0


def _cmd_review(args: argparse.Namespace) -> int:
    output_dir = Path(cast(str, args.output_dir))
    log_path_arg = cast(str | None, args.log_path)
    run_id_arg = cast(str | None, args.run_id)
    scope_arg = cast(str | None, args.scope)
    review_path_arg = cast(str | None, args.review_path)

    if log_path_arg is not None:
        log_path = Path(log_path_arg)
        run_id = log_path.stem
    else:
        if run_id_arg is not None:
            run_id = run_id_arg
        elif scope_arg is not None:
            run_id = _resolve_run_id_from_scope(output_dir=output_dir, scope=scope_arg)
        else:
            raise ValueError("Either --run-id, --scope, or --log-path is required")
        log_path = _resolve_log_path(output_dir=output_dir, run_id=run_id)

    entries = _load_entries(log_path)
    review_path = (
        Path(review_path_arg) if review_path_arg is not None else _resolve_review_path(output_dir=output_dir, run_id=run_id)
    )
    review_path.parent.mkdir(parents=True, exist_ok=True)
    _ = review_path.write_text(_build_review_markdown(log_path=log_path, entries=entries), encoding="utf-8")
    if scope_arg is not None:
        _close_active_scope(output_dir=output_dir, scope=scope_arg)
    else:
        _close_active_run_id(output_dir=output_dir, run_id=run_id)

    print(f"run_id={run_id}")
    print(f"log_path={log_path}")
    print(f"review_path={review_path}")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append and summarize ephemeral implementation decision logs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    log_parser = subparsers.add_parser("log", help="Append one decision/assumption/meta entry to a run JSONL.")
    _ = log_parser.add_argument(
        "--run-id",
        help="Run identifier. If omitted, an active run is resolved by scope or created.",
    )
    _ = log_parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Output directory for decision artifacts.",
    )
    _ = log_parser.add_argument("--agent", required=True, help="Agent identifier responsible for this entry.")
    _ = log_parser.add_argument("--scope", required=True, help="Execution scope (for example wave/work-item).")
    _ = log_parser.add_argument("--entry-type", required=True, choices=ENTRY_TYPES, help="Entry type to append.")
    _ = log_parser.add_argument("--summary", required=True, help="Single-line summary of the assumption/decision.")
    _ = log_parser.add_argument("--rationale", required=True, help="Short explanation for why this entry exists.")
    _ = log_parser.add_argument(
        "--confidence",
        default=3,
        type=_validate_confidence,
        help="Confidence score in range 1..5 (default: 3).",
    )
    _ = log_parser.add_argument(
        "--impact",
        default="low",
        choices=IMPACT_LEVELS,
        help="Impact level (default: low).",
    )
    _ = log_parser.add_argument(
        "--durability",
        default="ephemeral",
        choices=DURABILITY_LEVELS,
        help="Durability classification: ephemeral, restart-safe, or multi-instance-safe (default: ephemeral).",
    )
    _ = log_parser.add_argument(
        "--needs-review",
        action="store_true",
        help="Mark this entry as requiring post-run human review.",
    )
    resolution_group = log_parser.add_mutually_exclusive_group()
    _ = resolution_group.add_argument("--resolved", action="store_true", help="Mark entry as resolved.")
    _ = resolution_group.add_argument("--unresolved", action="store_true", help="Mark entry as unresolved.")
    _ = log_parser.set_defaults(handler=_cmd_log)

    review_parser = subparsers.add_parser("review", help="Generate markdown review summary for a run JSONL log.")
    _ = review_parser.add_argument("--run-id", help="Run identifier to summarize.")
    _ = review_parser.add_argument("--scope", help="Resolve the active run for this scope and summarize it.")
    _ = review_parser.add_argument("--log-path", help="Direct path to JSONL log file.")
    _ = review_parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Output directory for decision artifacts.",
    )
    _ = review_parser.add_argument("--review-path", help="Optional explicit output path for markdown review summary.")
    _ = review_parser.set_defaults(handler=_cmd_review)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if (
        cast(str, args.command) == "review"
        and cast(str | None, args.run_id) is None
        and cast(str | None, args.scope) is None
        and cast(str | None, args.log_path) is None
    ):
        parser.error("review requires either --run-id, --scope, or --log-path")
    handler = cast(Callable[[argparse.Namespace], int], args.handler)
    return handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
