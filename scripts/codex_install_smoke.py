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


def run_install(codex_home: Path, bin_dir: Path, *args: str) -> None:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    env["AGENT_HARNESS_BIN_DIR"] = str(bin_dir)
    result = subprocess.run(
        ["bash", str(INSTALLER), "--apply", *args],
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
        config_file = source_block.get("config_file")
        if not isinstance(config_file, str):
            fail(f"source config agents.{agent_name}.config_file must be a string")
        if not (codex_home / config_file).is_file():
            fail(f"config.toml agents.{agent_name}.config_file points to missing {config_file}")


def role_names() -> set[str]:
    roles_path = ROOT / "agents" / "roles.md"
    roles: set[str] = set()
    for line in roles_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("- `") and "`:" in line:
            roles.add(line.split("`", 2)[1])
    if not roles:
        fail("agents/roles.md defines no roles")
    return roles


def assert_all_skills(codex_home: Path) -> None:
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir():
            assert_symlink(codex_home / "skills" / skill_dir.name, skill_dir)


def assert_all_agents(codex_home: Path) -> None:
    for agent_file in sorted((ROOT / "adapters" / "codex" / "agents").glob("*.toml")):
        assert_symlink(codex_home / "agents" / agent_file.name, agent_file)


def assert_config_roles(codex_home: Path) -> None:
    target = tomllib.loads((codex_home / "config.toml").read_text(encoding="utf-8"))
    target_agents = target.get("agents", {})
    if not isinstance(target_agents, dict):
        fail("config.toml missing [agents] table")
    for role in sorted(role_names()):
        if role not in target_agents:
            fail(f"config.toml missing role from agents/roles.md: {role}")


def assert_repo_codex_not_regular_file() -> None:
    repo_codex = ROOT / ".codex"
    if repo_codex.exists() and repo_codex.is_file() and not repo_codex.is_symlink():
        fail("repo root contains a regular-file .codex stub")


def assert_install(codex_home: Path, bin_dir: Path) -> None:
    assert_symlink(codex_home / "AGENTS.md", ROOT / "AGENTS.md")
    assert_all_skills(codex_home)
    assert_all_agents(codex_home)
    assert_symlink(bin_dir / "agent-harness", ROOT / "adapters" / "codex" / "bin" / "agent-harness")
    assert_config(codex_home)
    assert_config_roles(codex_home)
    assert_repo_codex_not_regular_file()


def assert_stage_only(codex_home: Path, bin_dir: Path) -> None:
    assert_symlink(codex_home / "skills" / "harness-governance", ROOT / "skills" / "harness-governance")
    excluded = (
        codex_home / "AGENTS.md",
        codex_home / "config.toml",
        codex_home / "agents",
        codex_home / "skills" / "webapp-testing",
        bin_dir / "agent-harness",
    )
    for path in excluded:
        if path.exists() or path.is_symlink():
            fail(f"stage-only install unexpectedly created {path}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="codex-install-smoke-") as temp_dir:
        codex_home = Path(temp_dir) / "codex-home"
        bin_dir = Path(temp_dir) / "bin"
        run_install(codex_home, bin_dir)
        assert_install(codex_home, bin_dir)
        run_install(codex_home, bin_dir)
        assert_install(codex_home, bin_dir)
        shutil.rmtree(codex_home)
        stage_codex_home = Path(temp_dir) / "stage-codex-home"
        stage_bin_dir = Path(temp_dir) / "stage-bin"
        run_install(stage_codex_home, stage_bin_dir, "--stage-harness-governance")
        assert_stage_only(stage_codex_home, stage_bin_dir)
    print("codex install smoke passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"codex install smoke failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
