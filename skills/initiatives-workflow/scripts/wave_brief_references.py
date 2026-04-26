#!/usr/bin/env python3
# ruff: noqa: T201
from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path

WAVE_BRIEF_RELATIVE_ROOT = Path("docs-ai/docs/initiatives/waves")
IGNORED_PARTS = frozenset(
    {
        ".git",
    }
)


class WaveBriefReferenceError(ValueError):
    @classmethod
    def invalid_wave_id(cls, wave_id: str) -> WaveBriefReferenceError:
        return cls(f"Invalid wave id: {wave_id!r}")

    @classmethod
    def escaped_repo_root(cls, path: Path) -> WaveBriefReferenceError:
        return cls(f"Path escapes repo root: {path}")


@dataclass(frozen=True, slots=True)
class ReferenceHit:
    path: Path
    line_number: int
    line: str


@dataclass(frozen=True, slots=True)
class ReferenceReport:
    wave_refs: tuple[ReferenceHit, ...]
    non_wave_refs: tuple[ReferenceHit, ...]


@dataclass(frozen=True, slots=True)
class _Args:
    wave: str
    repo_root: Path


def _validate_wave_id(wave_id: str) -> None:
    if not wave_id or any(char not in "abcdefghijklmnopqrstuvwxyz0123456789-" for char in wave_id):
        raise WaveBriefReferenceError.invalid_wave_id(wave_id)


def _iter_repo_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for root, dirnames, filenames in os.walk(repo_root):
        root_path = Path(root)
        dirnames[:] = [dirname for dirname in dirnames if dirname not in IGNORED_PARTS]
        if any(part in IGNORED_PARTS for part in root_path.relative_to(repo_root).parts):
            continue
        files.extend(root_path / filename for filename in filenames)
    return sorted(files)


def _read_path_bytes(path: Path) -> bytes | None:
    try:
        return path.read_bytes()
    except FileNotFoundError:
        return None


def collect_wave_brief_references(*, repo_root: Path, wave_id: str) -> ReferenceReport:
    _validate_wave_id(wave_id)
    target_relative_path = WAVE_BRIEF_RELATIVE_ROOT / f"{wave_id}.md"
    target_token = str(target_relative_path)
    target_bytes = target_token.encode("utf-8")
    wave_refs: list[ReferenceHit] = []
    non_wave_refs: list[ReferenceHit] = []

    for path in _iter_repo_files(repo_root):
        try:
            relative_path = path.relative_to(repo_root)
        except ValueError as exc:  # pragma: no cover - defensive only
            raise WaveBriefReferenceError.escaped_repo_root(path) from exc

        if relative_path == target_relative_path:
            continue

        raw = _read_path_bytes(path)
        if raw is None:
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

    return ReferenceReport(wave_refs=tuple(wave_refs), non_wave_refs=tuple(non_wave_refs))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="List exact repo references to one wave brief path.")
    _ = parser.add_argument("--wave", required=True, help="Wave id, for example: hd-9")
    _ = parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Target project repository root.")
    return parser


def _parse_args(parser: argparse.ArgumentParser) -> _Args:
    args = parser.parse_args()
    wave = getattr(args, "wave", None)
    if not isinstance(wave, str):
        raise TypeError
    repo_root = getattr(args, "repo_root", None)
    if not isinstance(repo_root, Path):
        raise TypeError
    return _Args(wave=wave, repo_root=repo_root)


def main() -> int:
    parser = _build_parser()
    args = _parse_args(parser)
    wave_id = args.wave
    repo_root = args.repo_root.resolve()
    report = collect_wave_brief_references(repo_root=repo_root, wave_id=wave_id)

    print(f"wave: {wave_id}")
    print(f"target: {WAVE_BRIEF_RELATIVE_ROOT / f'{wave_id}.md'}")
    print(f"wave_refs: {len(report.wave_refs)}")
    for hit in report.wave_refs:
        print(f"  W {hit.path}:{hit.line_number}: {hit.line}")
    print(f"non_wave_refs: {len(report.non_wave_refs)}")
    for hit in report.non_wave_refs:
        print(f"  N {hit.path}:{hit.line_number}: {hit.line}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
