#!/usr/bin/env bash
set -euo pipefail

MODE="dry-run"
STAGE_ONLY="false"

usage() {
  cat <<'EOF'
Usage: install.sh [--dry-run] [--stage-harness-governance]

Installs Codex skills/agents with individual symlinks only.
Baseline excludes config, prompts, Copilot, and Gemini homes.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      MODE="dry-run"
      ;;
    --stage-harness-governance)
      STAGE_ONLY="true"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd -- "$SCRIPT_DIR/../.." && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
SKILLS_HOME="$CODEX_HOME/skills"
AGENTS_HOME="$CODEX_HOME/agents"

if [[ "$MODE" != "dry-run" ]]; then
  echo "only --dry-run is implemented in this adapter slice" >&2
  exit 2
fi

echo "mode: $MODE"
echo "root: $ROOT"
echo "codex_home: $CODEX_HOME"
echo "excluded: $CODEX_HOME/config.toml"
echo "excluded: $CODEX_HOME/prompts"
echo "excluded: $HOME/.copilot"
echo "excluded: $HOME/.gemini"

echo "planned skills:"
if [[ "$STAGE_ONLY" == "true" ]]; then
  echo "$SKILLS_HOME/harness-governance -> $ROOT/skills/harness-governance"
else
  while IFS= read -r skill_dir; do
    name="$(basename "$skill_dir")"
    echo "$SKILLS_HOME/$name -> $skill_dir"
  done < <(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | sort)
fi

echo "planned agents:"
if [[ "$STAGE_ONLY" == "true" ]]; then
  echo "none"
else
  while IFS= read -r agent_file; do
    name="$(basename "$agent_file")"
    echo "$AGENTS_HOME/$name -> $agent_file"
  done < <(find "$SCRIPT_DIR/agents" -mindepth 1 -maxdepth 1 -type f -name '*.toml' | sort)
fi

echo "conflict policy: stop before replacing non-matching live targets"
