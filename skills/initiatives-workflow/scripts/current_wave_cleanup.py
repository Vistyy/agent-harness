#!/usr/bin/env python3
# ruff: noqa: T201
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path
from typing import cast

_WAVE_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class WaveCleanupError(ValueError):
    @classmethod
    def invalid_wave(cls, wave: str) -> WaveCleanupError:
        return cls(f"Invalid wave id: {wave!r}")

    @classmethod
    def missing_directory(cls, path: Path) -> WaveCleanupError:
        return cls(f"Wave directory not found: {path}")

    @classmethod
    def symlink_directory(cls, path: Path) -> WaveCleanupError:
        return cls(f"Refusing symlink directory: {path}")

    @classmethod
    def escaped_current_work_root(cls, path: Path) -> WaveCleanupError:
        return cls(f"Resolved path escapes current-work root: {path}")

    @classmethod
    def not_wave_directory(cls, path: Path) -> WaveCleanupError:
        return cls(f"Directory is not a wave execution directory (missing wave-execution.md): {path}")

    @classmethod
    def not_directory(cls, path: Path) -> WaveCleanupError:
        return cls(f"Not a directory: {path}")


def _validate_wave(wave: str) -> None:
    if not _WAVE_RE.fullmatch(wave):
        raise WaveCleanupError.invalid_wave(wave)


def resolve_wave_dir(*, current_work_root: Path, wave: str) -> Path:
    _validate_wave(wave)

    root = current_work_root.resolve()
    candidate_raw = root / wave
    if candidate_raw.is_symlink():
        raise WaveCleanupError.symlink_directory(candidate_raw)
    candidate = candidate_raw.resolve()

    if not candidate.is_dir():
        raise WaveCleanupError.missing_directory(candidate)

    try:
        _ = candidate.relative_to(root)
    except ValueError:
        raise WaveCleanupError.escaped_current_work_root(candidate) from None

    if not (candidate / "wave-execution.md").exists():
        raise WaveCleanupError.not_wave_directory(candidate)

    return candidate


def delete_wave_dir(wave_dir: Path) -> int:
    if wave_dir.is_symlink():
        raise WaveCleanupError.symlink_directory(wave_dir)
    target = wave_dir.resolve()
    if not target.is_dir():
        raise WaveCleanupError.not_directory(target)

    removed_entries = sum(1 for _ in target.rglob("*"))
    shutil.rmtree(target)
    return removed_entries


def _default_current_work_root() -> Path:
    return Path.cwd() / "docs-ai" / "current-work"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Safely delete a docs-ai/current-work wave directory.")
    _ = parser.add_argument("--wave", required=True, help="Wave id, for example: hd-9")
    _ = parser.add_argument(
        "--execute",
        action="store_true",
        help="Delete the resolved directory. Without this flag the command is a dry-run.",
    )
    _ = parser.add_argument(
        "--current-work-root",
        type=Path,
        default=_default_current_work_root(),
        help="Target docs-ai/current-work directory.",
    )
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    wave = cast(str, args.wave)
    execute = cast(bool, args.execute)
    current_work_root = cast(Path, args.current_work_root)

    wave_dir = resolve_wave_dir(
        current_work_root=current_work_root,
        wave=wave,
    )
    if not execute:
        print(f"DRY RUN: {wave_dir}")
        return 0

    removed_entries = delete_wave_dir(wave_dir)
    print(f"DELETED: {wave_dir} (removed_entries={removed_entries})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
