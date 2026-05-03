from __future__ import annotations

import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
SKILLS_HOME = CODEX_HOME / "skills"
AGENTS_HOME = CODEX_HOME / "agents"


def fail(message: str) -> None:
    raise AssertionError(message)


def assert_symlink(path: Path, expected_source: Path) -> None:
    if not path.is_symlink():
        fail(f"{path} is not a symlink")
    actual = Path(os.readlink(path))
    if actual != expected_source:
        fail(f"{path} points to {actual}, expected {expected_source}")


def planned_skills() -> dict[str, Path]:
    return {
        path.name: path
        for path in sorted((ROOT / "skills").iterdir())
        if path.is_dir()
    }


def planned_agents() -> dict[str, Path]:
    return {
        path.name: path
        for path in sorted((ROOT / "adapters" / "codex" / "agents").glob("*.toml"))
    }


def resolved_symlink_target(path: Path) -> Path:
    target = Path(os.readlink(path))
    try:
        if not target.is_absolute():
            target = path.parent / target
        return target.resolve(strict=False)
    except OSError as exc:
        fail(f"cannot resolve symlink target for {path}: {exc}")


def target_is_inside_repo(target: Path) -> bool:
    try:
        target.relative_to(ROOT)
    except ValueError:
        return False
    return True


def assert_no_stale_harness_symlinks(directory: Path, planned_names: set[str]) -> None:
    if not directory.exists():
        fail(f"{directory} is missing")
    for path in sorted(directory.iterdir()):
        if not path.is_symlink():
            continue
        if path.name == ".system":
            continue
        target = resolved_symlink_target(path)
        if target_is_inside_repo(target) and path.name not in planned_names:
            fail(f"{path} is a stale harness symlink to {target}")


def assert_backup_manifest() -> None:
    backup_root = CODEX_HOME / "backups"
    manifests = sorted(backup_root.glob("agent-harness-*/backup-manifest.json"))
    if not manifests:
        fail("no Codex install backup manifest found")
    data = json.loads(manifests[-1].read_text(encoding="utf-8"))
    pruned = data.get("pruned_symlinks")
    if not isinstance(pruned, list):
        fail("backup manifest missing pruned_symlinks list")


def main() -> int:
    skills = planned_skills()
    agents = planned_agents()

    assert_symlink(CODEX_HOME / "AGENTS.md", ROOT / "AGENTS.md")
    for name, source in skills.items():
        assert_symlink(SKILLS_HOME / name, source)
    for name, source in agents.items():
        assert_symlink(AGENTS_HOME / name, source)

    assert_no_stale_harness_symlinks(SKILLS_HOME, set(skills))
    assert_no_stale_harness_symlinks(AGENTS_HOME, set(agents))
    if (SKILLS_HOME / ".system").exists() and not (SKILLS_HOME / ".system").is_dir():
        fail(f"{SKILLS_HOME / '.system'} is not a directory")
    assert_backup_manifest()

    print("codex live install check passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"codex live install check failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
