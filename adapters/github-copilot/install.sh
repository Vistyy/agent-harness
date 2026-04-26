#!/usr/bin/env bash
set -euo pipefail

MODE="dry-run"
REPLACE_CONFLICTING_SYMLINK="false"

usage() {
  cat <<'EOF'
Usage: install.sh [--dry-run|--apply] [--replace-conflicting-symlink]

Installs GitHub Copilot custom agents at user scope:

  ~/.copilot/agents -> adapters/github-copilot/agents

This makes the reusable agent profiles available across VS Code workspaces
without keeping `.github/agents` copies in each project repo.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      MODE="dry-run"
      ;;
    --apply)
      MODE="apply"
      ;;
    --replace-conflicting-symlink)
      REPLACE_CONFLICTING_SYMLINK="true"
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
SOURCE="$SCRIPT_DIR/agents"
COPILOT_HOME="${COPILOT_HOME:-$HOME/.copilot}"
TARGET="$COPILOT_HOME/agents"
BACKUP_ROOT="$COPILOT_HOME/backups"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
RUN_DIR="$BACKUP_ROOT/agent-harness-$RUN_ID"

target_matches() {
  [[ -L "$TARGET" && "$(readlink "$TARGET")" == "$SOURCE" ]]
}

echo "mode: $MODE"
echo "source: $SOURCE"
echo "target: $TARGET"
echo "conflict policy: stop before replacing non-matching live target"

if [[ -e "$TARGET" || -L "$TARGET" ]]; then
  if target_matches; then
    echo "status: already installed"
    exit 0
  fi
  if [[ "$REPLACE_CONFLICTING_SYMLINK" == "true" && -L "$TARGET" ]]; then
    echo "replace symlink: $TARGET -> $(readlink "$TARGET")"
  else
    echo "conflict: $TARGET exists and does not point to $SOURCE" >&2
    exit 1
  fi
fi

if [[ "$MODE" == "apply" ]]; then
  mkdir -p "$COPILOT_HOME" "$RUN_DIR"
  if [[ -L "$TARGET" ]]; then
    printf '%s\t%s\n' "$TARGET" "$(readlink "$TARGET")" > "$RUN_DIR/replaced-symlink.tsv"
    rm "$TARGET"
  fi
  ln -s "$SOURCE" "$TARGET"
  printf '%s\t%s\n' "$TARGET" "$SOURCE" > "$RUN_DIR/symlink.tsv"
  echo "manifest_dir: $RUN_DIR"
fi

