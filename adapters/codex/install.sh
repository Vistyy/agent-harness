#!/usr/bin/env bash
set -euo pipefail

MODE="dry-run"
STAGE_ONLY="false"
REPLACE_CONFLICTING_SYMLINKS="false"

usage() {
  cat <<'EOF'
Usage: install.sh [--dry-run|--apply] [--stage-harness-governance] [--replace-conflicting-symlinks]

Installs Codex skills/agents with individual symlinks only.
Baseline excludes config, prompts, Copilot, and Gemini homes.
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
    --stage-harness-governance)
      STAGE_ONLY="true"
      ;;
    --replace-conflicting-symlinks)
      REPLACE_CONFLICTING_SYMLINKS="true"
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

BACKUP_ROOT="$CODEX_HOME/backups"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
RUN_DIR="$BACKUP_ROOT/agent-harness-$RUN_ID"

planned_skills() {
  if [[ "$STAGE_ONLY" == "true" ]]; then
    printf '%s\t%s\n' "$SKILLS_HOME/harness-governance" "$ROOT/skills/harness-governance"
  else
    while IFS= read -r skill_dir; do
      name="$(basename "$skill_dir")"
      printf '%s\t%s\n' "$SKILLS_HOME/$name" "$skill_dir"
    done < <(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | sort)
  fi
}

planned_agents() {
  if [[ "$STAGE_ONLY" == "true" ]]; then
    return
  fi
  while IFS= read -r agent_file; do
    name="$(basename "$agent_file")"
    printf '%s\t%s\n' "$AGENTS_HOME/$name" "$agent_file"
  done < <(find "$SCRIPT_DIR/agents" -mindepth 1 -maxdepth 1 -type f -name '*.toml' | sort)
}

target_matches() {
  local target="$1"
  local source="$2"
  [[ -L "$target" && "$(readlink "$target")" == "$source" ]]
}

CONFLICTS=()

collect_conflicts() {
  CONFLICTS=()
  local failed="false"
  while IFS=$'\t' read -r target source; do
    [[ -z "$target" ]] && continue
    if [[ -e "$target" || -L "$target" ]]; then
      if ! target_matches "$target" "$source"; then
        CONFLICTS+=("$target"$'\t'"$source")
        if [[ "$REPLACE_CONFLICTING_SYMLINKS" != "true" || ! -L "$target" ]]; then
          echo "conflict: $target exists and does not point to $source" >&2
        fi
        failed="true"
      fi
    fi
  done
  if [[ "$failed" == "false" ]]; then
    return 0
  fi
  if [[ "$REPLACE_CONFLICTING_SYMLINKS" == "true" ]]; then
    local conflict
    for conflict in "${CONFLICTS[@]}"; do
      local target="${conflict%%$'\t'*}"
      if [[ ! -L "$target" ]]; then
        echo "conflict: $target is not a symlink; refusing replacement" >&2
        return 1
      fi
    done
    return 0
  fi
  return 1
}

write_inventory() {
  local path="$1"
  {
    for item in "$CODEX_HOME/config.toml" "$CODEX_HOME/prompts" "$HOME/.copilot" "$HOME/.gemini" "$AGENTS_HOME"; do
      if [[ -e "$item" || -L "$item" ]]; then
        printf '%s\t%s\t%s\n' "$item" "$(stat -c '%F:%s' "$item")" "$(readlink "$item" || true)"
      else
        printf '%s\tmissing\t\n' "$item"
      fi
    done
  } > "$path"
}

write_manifests() {
  mkdir -p "$RUN_DIR"
  write_inventory "$RUN_DIR/pre-inventory.tsv"
  {
    echo "{"
    echo "  \"mode\": \"$MODE\","
    echo "  \"stage_only\": $STAGE_ONLY,"
    echo "  \"replaced_symlinks\": ["
    local first_backup="true"
    local conflict
    for conflict in "${CONFLICTS[@]}"; do
      local target="${conflict%%$'\t'*}"
      local source="${conflict#*$'\t'}"
      local old_source
      old_source="$(readlink "$target")"
      if [[ "$first_backup" == "false" ]]; then
        echo ","
      fi
      first_backup="false"
      printf '    {"target": "%s", "old_source": "%s", "new_source": "%s", "type": "symlink"}' "$target" "$old_source" "$source"
    done
    echo
    echo "  ]"
    echo "}"
  } > "$RUN_DIR/backup-manifest.json"
  {
    echo "{"
    echo "  \"mode\": \"$MODE\","
    echo "  \"stage_only\": $STAGE_ONLY,"
    echo "  \"symlinks\": ["
    local first="true"
    while IFS=$'\t' read -r target source; do
      [[ -z "$target" ]] && continue
      if [[ "$first" == "false" ]]; then
        echo ","
      fi
      first="false"
      printf '    {"target": "%s", "source": "%s"}' "$target" "$source"
    done
    echo
    echo "  ]"
    echo "}"
  } < <({ planned_skills; planned_agents; }) > "$RUN_DIR/symlink-manifest.json"
}

apply_symlinks() {
  while IFS=$'\t' read -r target _source; do
    [[ -z "$target" ]] && continue
    mkdir -p "$(dirname "$target")"
  done
  local conflict
  for conflict in "${CONFLICTS[@]}"; do
    local target="${conflict%%$'\t'*}"
    if [[ -L "$target" ]]; then
      rm "$target"
    fi
  done
  while IFS=$'\t' read -r target source; do
    [[ -z "$target" ]] && continue
    if [[ -L "$target" ]]; then
      continue
    fi
    ln -s "$source" "$target"
  done
}

echo "mode: $MODE"
echo "root: $ROOT"
echo "codex_home: $CODEX_HOME"
echo "excluded: $CODEX_HOME/config.toml"
echo "excluded: $CODEX_HOME/prompts"
echo "excluded: $HOME/.copilot"
echo "excluded: $HOME/.gemini"

echo "planned skills:"
while IFS=$'\t' read -r target source; do
  [[ -z "$target" ]] && continue
  echo "$target -> $source"
done < <(planned_skills)

echo "planned agents:"
if [[ "$STAGE_ONLY" == "true" ]]; then
  echo "none"
else
  while IFS=$'\t' read -r target source; do
    [[ -z "$target" ]] && continue
    echo "$target -> $source"
  done < <(planned_agents)
fi

echo "conflict policy: stop before replacing non-matching live targets"

if ! collect_conflicts < <({ planned_skills; planned_agents; }); then
  exit 1
fi

if [[ "$MODE" == "apply" ]]; then
  write_manifests
  { planned_skills; planned_agents; } | apply_symlinks
  write_inventory "$RUN_DIR/post-inventory.tsv"
  echo "manifest_dir: $RUN_DIR"
fi
