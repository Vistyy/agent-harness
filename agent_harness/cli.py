from __future__ import annotations

import argparse
from pathlib import Path

from agent_harness import governance
from agent_harness import memory


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-harness")
    subparsers = parser.add_subparsers(dest="command", required=True)

    governance_parser = subparsers.add_parser("governance", help="Workflow overlay governance helpers.")
    governance_subparsers = governance_parser.add_subparsers(dest="governance_command", required=True)
    governance_check_parser = governance_subparsers.add_parser("check", help="Run project overlay governance checks.")
    governance_check_parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Target project root.")

    memory_parser = subparsers.add_parser("memory", help="Delivery memory helpers.")
    memory_subparsers = memory_parser.add_subparsers(dest="memory_command", required=True)

    bootstrap_parser = memory_subparsers.add_parser("bootstrap", help="Scaffold a work note.")
    bootstrap_parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Target project root.")
    bootstrap_parser.add_argument("--item", "--item-id", dest="item", required=True, help="Item id.")
    bootstrap_parser.add_argument("--title", required=True, help="Human-readable item title.")
    bootstrap_parser.add_argument("--task", action="append", dest="tasks", default=[], help="Starting-point slug.")
    bootstrap_parser.add_argument("--force", action="store_true", help="Overwrite existing files.")

    refs_parser = memory_subparsers.add_parser("refs", help="List exact references to a work note.")
    refs_parser.add_argument("--repo-root", type=Path, required=True, help="Target project root.")
    refs_parser.add_argument("--item", required=True, help="Item id.")

    lifecycle_parser = memory_subparsers.add_parser("lifecycle", help="Inspect memory artifacts before closeout.")
    lifecycle_parser.add_argument("--repo-root", type=Path, required=True, help="Target project root.")
    lifecycle_parser.add_argument("--item", required=True, help="Item id.")

    cleanup_parser = memory_subparsers.add_parser("cleanup", help="Delete a current-work active note directory.")
    cleanup_parser.add_argument("--repo-root", type=Path, required=True, help="Target project root.")
    cleanup_parser.add_argument("--item", required=True, help="Item id.")
    cleanup_parser.add_argument("--execute", action="store_true", help="Delete after validation.")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.command == "governance" and args.governance_command == "check":
        return governance.command_governance_check(repo_root=args.repo_root)
    if args.command == "memory" and args.memory_command == "bootstrap":
        return memory.command_bootstrap(
            repo_root=args.repo_root,
            item=args.item,
            title=args.title,
            tasks=list(args.tasks),
            force=bool(args.force),
        )
    if args.command == "memory" and args.memory_command == "refs":
        return memory.command_refs(repo_root=args.repo_root, item=args.item)
    if args.command == "memory" and args.memory_command == "lifecycle":
        return memory.command_lifecycle(repo_root=args.repo_root, item=args.item)
    if args.command == "memory" and args.memory_command == "cleanup":
        return memory.command_cleanup(repo_root=args.repo_root, item=args.item, execute=args.execute)
    raise AssertionError("unreachable command route")


if __name__ == "__main__":
    raise SystemExit(main())
