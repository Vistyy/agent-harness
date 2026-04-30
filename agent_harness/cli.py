from __future__ import annotations

import argparse
from pathlib import Path

from agent_harness import governance
from agent_harness import waves


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-harness")
    subparsers = parser.add_subparsers(dest="command", required=True)

    governance_parser = subparsers.add_parser("governance", help="Harness governance helpers.")
    governance_subparsers = governance_parser.add_subparsers(dest="governance_command", required=True)
    governance_check_parser = governance_subparsers.add_parser("check", help="Run project overlay governance checks.")
    governance_check_parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Target project root.")

    wave_parser = subparsers.add_parser("wave", help="Wave workflow helpers.")
    wave_subparsers = wave_parser.add_subparsers(dest="wave_command", required=True)

    bootstrap_parser = wave_subparsers.add_parser("bootstrap", help="Scaffold a discovery-required wave brief.")
    bootstrap_parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Target project repository root.")
    bootstrap_parser.add_argument("--wave", "--wave-id", dest="wave", required=True, help="Wave id.")
    bootstrap_parser.add_argument("--title", required=True, help="Human-readable wave title.")
    bootstrap_parser.add_argument(
        "--status",
        choices=("discovery-required",),
        default="discovery-required",
        help="Initial wave status. Only discovery-required scaffolding is supported.",
    )
    bootstrap_parser.add_argument("--task", action="append", dest="tasks", default=[], help="Task slug to prefill.")
    bootstrap_parser.add_argument("--force", action="store_true", help="Overwrite existing files.")

    refs_parser = wave_subparsers.add_parser("refs", help="List exact references to a wave brief.")
    refs_parser.add_argument("--repo-root", type=Path, required=True, help="Target project repository root.")
    refs_parser.add_argument("--wave", required=True, help="Wave id.")

    cleanup_parser = wave_subparsers.add_parser("cleanup", help="Delete a closed current-work wave packet directory.")
    cleanup_parser.add_argument("--repo-root", type=Path, required=True, help="Target project repository root.")
    cleanup_parser.add_argument("--wave", required=True, help="Wave id.")
    cleanup_parser.add_argument("--execute", action="store_true", help="Delete after validation.")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.command == "governance" and args.governance_command == "check":
        return governance.command_governance_check(repo_root=args.repo_root)
    if args.command == "wave" and args.wave_command == "bootstrap":
        return waves.command_wave_bootstrap(
            repo_root=args.repo_root,
            wave=args.wave,
            title=args.title,
            status=args.status,
            tasks=list(args.tasks),
            force=bool(args.force),
        )
    if args.command == "wave" and args.wave_command == "refs":
        return waves.command_wave_refs(repo_root=args.repo_root, wave=args.wave)
    if args.command == "wave" and args.wave_command == "cleanup":
        return waves.command_wave_cleanup(repo_root=args.repo_root, wave=args.wave, execute=args.execute)
    raise AssertionError("unreachable command route")


if __name__ == "__main__":
    raise SystemExit(main())
