from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "adapters" / "codex" / "install.sh"
SOURCE_CONFIG = ROOT / "adapters" / "codex" / "config.toml"


def fail(message: str) -> None:
    raise AssertionError(message)


def run_install(codex_home: Path) -> None:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    result = subprocess.run(
        ["bash", str(INSTALLER), "--apply"],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        fail(f"installer exited {result.returncode}")


def assert_symlink(path: Path, expected_source: Path) -> None:
    if not path.is_symlink():
        fail(f"{path} is not a symlink")
    actual = Path(os.readlink(path))
    if actual != expected_source:
        fail(f"{path} points to {actual}, expected {expected_source}")


def assert_config(codex_home: Path) -> None:
    target_config = codex_home / "config.toml"
    if not target_config.is_file():
        fail("config.toml was not created")
    target = tomllib.loads(target_config.read_text(encoding="utf-8"))
    source = tomllib.loads(SOURCE_CONFIG.read_text(encoding="utf-8"))
    if target.get("features", {}).get("multi_agent") is not True:
        fail("config.toml missing [features] multi_agent = true")
    source_agents = source.get("agents", {})
    target_agents = target.get("agents", {})
    for agent_name, source_block in source_agents.items():
        target_block = target_agents.get(agent_name)
        if target_block != source_block:
            fail(f"config.toml missing or changed agents.{agent_name} block")


def assert_repo_codex_not_regular_file() -> None:
    repo_codex = ROOT / ".codex"
    if repo_codex.exists() and repo_codex.is_file() and not repo_codex.is_symlink():
        fail("repo root contains a regular-file .codex stub")


def assert_install(codex_home: Path) -> None:
    assert_symlink(codex_home / "AGENTS.md", ROOT / "AGENTS.md")
    assert_symlink(codex_home / "skills" / "webapp-testing", ROOT / "skills" / "webapp-testing")
    assert_symlink(
        codex_home / "agents" / "runtime-evidence.toml",
        ROOT / "adapters" / "codex" / "agents" / "runtime-evidence.toml",
    )
    assert_config(codex_home)
    assert_repo_codex_not_regular_file()


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="codex-install-smoke-") as temp_dir:
        codex_home = Path(temp_dir) / "codex-home"
        run_install(codex_home)
        assert_install(codex_home)
        run_install(codex_home)
        assert_install(codex_home)
        shutil.rmtree(codex_home)
    print("codex install smoke passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"codex install smoke failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
