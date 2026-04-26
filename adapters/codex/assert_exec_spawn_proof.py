#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path


def assert_spawn_proof(path: Path, expected_final: str) -> list[str]:
    errors: list[str] = []
    events = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not any(
        event.get("type") == "item.completed"
        and event.get("item", {}).get("type") == "collab_tool_call"
        and event.get("item", {}).get("tool") == "spawn_agent"
        and event.get("item", {}).get("status") == "completed"
        for event in events
    ):
        errors.append("missing completed spawn_agent tool call")
    if not any(
        event.get("type") == "item.completed"
        and event.get("item", {}).get("type") == "collab_tool_call"
        and event.get("item", {}).get("tool") == "wait"
        and "completed" in str(event.get("item", {}).get("agents_states", {}))
        for event in events
    ):
        errors.append("missing completed subagent wait")
    if not any(
        event.get("type") == "item.completed"
        and event.get("item", {}).get("type") == "agent_message"
        and event.get("item", {}).get("text") == expected_final
        for event in events
    ):
        errors.append(f"missing final agent message {expected_final!r}")
    return errors


def run_self_test() -> list[str]:
    lines = [
        {"type": "thread.started", "thread_id": "parent"},
        {
            "type": "item.completed",
            "item": {
                "type": "collab_tool_call",
                "tool": "spawn_agent",
                "status": "completed",
            },
        },
        {
            "type": "item.completed",
            "item": {
                "type": "collab_tool_call",
                "tool": "wait",
                "agents_states": {"child": {"status": "completed", "message": "ok"}},
            },
        },
        {"type": "item.completed", "item": {"type": "agent_message", "text": "done"}},
    ]
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "events.jsonl"
        path.write_text("\n".join(json.dumps(line) for line in lines), encoding="utf-8")
        errors = assert_spawn_proof(path, "done")
        if errors:
            return [f"self-test unexpectedly failed: {errors}"]
        missing_wait = [line for line in lines if line.get("item", {}).get("tool") != "wait"]
        path.write_text("\n".join(json.dumps(line) for line in missing_wait), encoding="utf-8")
        if "missing completed subagent wait" not in assert_spawn_proof(path, "done"):
            return ["self-test failed to reject missing wait"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonl", nargs="?")
    parser.add_argument("expected_final", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        errors = run_self_test()
    else:
        if not args.jsonl or not args.expected_final:
            parser.error("jsonl and expected_final are required unless --self-test is used")
        errors = assert_spawn_proof(Path(args.jsonl), args.expected_final)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("codex exec spawn proof assertion passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
