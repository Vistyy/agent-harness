#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any


ROLE_PATTERNS = (
    re.compile(r"^\s*(?://\s*)?-\s*([A-Za-z0-9_]+):\s*\{", re.MULTILINE),
    re.compile(r'"([A-Za-z0-9_]+)"\s*:\s*\{'),
)


def _iter_registry_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        if "spawn_agent" in value and ("Available roles:" in value or "agent_type" in value):
            return [value]
        return []
    if isinstance(value, list):
        strings: list[str] = []
        for item in value:
            strings.extend(_iter_registry_strings(item))
        return strings
    if isinstance(value, dict):
        strings = []
        for item in value.values():
            strings.extend(_iter_registry_strings(item))
        return strings
    return []


def _extract_roles(registry_text: str) -> set[str]:
    roles: set[str] = set()
    for pattern in ROLE_PATTERNS:
        roles.update(match.group(1) for match in pattern.finditer(registry_text))
    return roles


def missing_agents(prompt_input: Any, expected_agents: list[str]) -> list[str]:
    roles: set[str] = set()
    for registry_text in _iter_registry_strings(prompt_input):
        roles.update(_extract_roles(registry_text))
    return [agent for agent in expected_agents if agent not in roles]


def run_self_test() -> list[str]:
    errors: list[str] = []
    prompt = {
        "items": [
            {
                "content": [
                    {
                        "text": "noise mentions runtime_evidence and final_reviewer only"
                    },
                    {
                        "text": (
                            "// Spawn a sub-agent.\n"
                            "// Available roles:\n"
                            "// - explorer: {\n"
                            "//   Use for discovery.\n"
                            "// }\n"
                            "// - check_runner: {\n"
                            "//   Use for checks.\n"
                            "// }\n"
                            "// - quality_guard: {\n"
                            "//   Use for review.\n"
                            "// }\n"
                            "type spawn_agent = (_: { agent_type?: string }) => any;"
                        )
                    }
                ]
            }
        ]
    }
    if missing_agents(prompt, ["explorer", "quality_guard"]):
        errors.append("self-test failed to find present agents")
    if missing_agents(prompt, ["runtime_evidence"]) != ["runtime_evidence"]:
        errors.append("self-test accepted unrelated text as registry")
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "prompt.json"
        path.write_text(json.dumps(prompt), encoding="utf-8")
        loaded = json.loads(path.read_text(encoding="utf-8"))
        if missing_agents(loaded, ["check_runner"]):
            errors.append("self-test failed to load prompt JSON")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt_input", nargs="?")
    parser.add_argument("agents", nargs="*")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        errors = run_self_test()
    else:
        if not args.prompt_input or not args.agents:
            parser.error("prompt_input and at least one agent are required unless --self-test is used")
        data = json.loads(Path(args.prompt_input).read_text(encoding="utf-8"))
        errors = [f"missing agent role {agent}" for agent in missing_agents(data, args.agents)]

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("agent role prompt-input assertion passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
