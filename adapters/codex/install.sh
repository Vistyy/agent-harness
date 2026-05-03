#!/usr/bin/env bash
set -euo pipefail

MODE="dry-run"
STAGE_ONLY="false"
REPLACE_CONFLICTING_SYMLINKS="false"

usage() {
  cat <<'EOF'
Usage: install.sh [--dry-run|--apply] [--stage-harness-governance] [--replace-conflicting-symlinks]

Installs Codex skills/agents and global AGENTS.md with individual symlinks.
Full apply also merges the required Codex agent-role config into
$CODEX_HOME/config.toml after writing a backup.
Baseline excludes prompts, Copilot, and Gemini homes.
Full apply also links the `agent-harness` CLI into
${AGENT_HARNESS_BIN_DIR:-$HOME/.local/bin} when not using staged install.
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
GLOBAL_AGENTS_PATH="$CODEX_HOME/AGENTS.md"
CONFIG_PATH="$CODEX_HOME/config.toml"
CONFIG_SOURCE="$SCRIPT_DIR/config.toml"
CLI_BIN_DIR="${AGENT_HARNESS_BIN_DIR:-$HOME/.local/bin}"
CLI_TARGET="$CLI_BIN_DIR/agent-harness"
CLI_SOURCE="$SCRIPT_DIR/bin/agent-harness"

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

planned_global_agents_md() {
  if [[ "$STAGE_ONLY" == "true" ]]; then
    return
  fi
  printf '%s\t%s\n' "$GLOBAL_AGENTS_PATH" "$ROOT/AGENTS.md"
}

planned_cli() {
  if [[ "$STAGE_ONLY" == "true" ]]; then
    return
  fi
  printf '%s\t%s\n' "$CLI_TARGET" "$CLI_SOURCE"
}

target_matches() {
  local target="$1"
  local source="$2"
  [[ -L "$target" && "$(readlink "$target")" == "$source" ]]
}

resolved_symlink_target() {
  local target="$1"
  local source="$2"
  if [[ "$source" = /* ]]; then
    realpath -m -- "$source"
  else
    realpath -m -- "$(dirname "$target")/$source"
  fi
}

CONFLICTS=()
PRUNES=()

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

planned_basenames() {
  local kind="$1"
  case "$kind" in
    skills)
      planned_skills | while IFS=$'\t' read -r target _source; do
        [[ -z "$target" ]] && continue
        basename "$target"
      done
      ;;
    agents)
      planned_agents | while IFS=$'\t' read -r target _source; do
        [[ -z "$target" ]] && continue
        basename "$target"
      done
      ;;
  esac
}

is_planned_basename() {
  local name="$1"
  shift
  local planned
  for planned in "$@"; do
    if [[ "$name" == "$planned" ]]; then
      return 0
    fi
  done
  return 1
}

collect_stale_symlink_prunes() {
  PRUNES=()
  if [[ "$STAGE_ONLY" == "true" ]]; then
    return
  fi
  local skill_names=()
  local agent_names=()
  while IFS= read -r name; do
    [[ -z "$name" ]] && continue
    skill_names+=("$name")
  done < <(planned_basenames skills)
  while IFS= read -r name; do
    [[ -z "$name" ]] && continue
    agent_names+=("$name")
  done < <(planned_basenames agents)

  local spec
  for spec in "$SKILLS_HOME|skills|${skill_names[*]}" "$AGENTS_HOME|agents|${agent_names[*]}"; do
    local dir="${spec%%|*}"
    local rest="${spec#*|}"
    local kind="${rest%%|*}"
    local names_string="${rest#*|}"
    local planned_names=()
    if [[ -n "$names_string" ]]; then
      read -r -a planned_names <<< "$names_string"
    fi
    [[ -d "$dir" ]] || continue
    local target
    while IFS= read -r target; do
      local name source
      name="$(basename "$target")"
      [[ "$name" == ".system" ]] && continue
      if is_planned_basename "$name" "${planned_names[@]}"; then
        continue
      fi
      source="$(readlink "$target")"
      local resolved_source
      resolved_source="$(resolved_symlink_target "$target" "$source")"
      case "$resolved_source" in
        "$ROOT")
          PRUNES+=("$target"$'\t'"$source"$'\t'"$kind")
          ;;
        "$ROOT"/*)
          PRUNES+=("$target"$'\t'"$source"$'\t'"$kind")
          ;;
      esac
    done < <(find "$dir" -mindepth 1 -maxdepth 1 -type l | sort)
  done
}

write_inventory() {
  local path="$1"
  {
    for item in "$CODEX_HOME/config.toml" "$CODEX_HOME/AGENTS.md" "$CODEX_HOME/prompts" "$HOME/.copilot" "$HOME/.gemini" "$AGENTS_HOME" "$CLI_TARGET"; do
      if [[ -e "$item" || -L "$item" ]]; then
        printf '%s\t%s\t%s\n' "$item" "$(stat -c '%F:%s' "$item")" "$(readlink "$item" || true)"
      else
        printf '%s\tmissing\t\n' "$item"
      fi
    done
  } > "$path"
}

merge_config() {
  if [[ "$STAGE_ONLY" == "true" ]]; then
    return
  fi
  mkdir -p "$CODEX_HOME" "$RUN_DIR"
  if [[ -e "$CONFIG_PATH" || -L "$CONFIG_PATH" ]]; then
    cp -a "$CONFIG_PATH" "$RUN_DIR/config.toml.before"
  else
    : > "$CONFIG_PATH"
    cp -a "$CONFIG_PATH" "$RUN_DIR/config.toml.before"
  fi
  CONFIG_PATH="$CONFIG_PATH" CONFIG_SOURCE="$CONFIG_SOURCE" python3 - <<'PY'
from __future__ import annotations

import os
import re
from pathlib import Path

config_path = Path(os.environ["CONFIG_PATH"])
source_path = Path(os.environ["CONFIG_SOURCE"])
text = config_path.read_text(encoding="utf-8")
source = source_path.read_text(encoding="utf-8")


def table_body(raw: str, table: str) -> str | None:
    pattern = re.compile(rf"^\[{re.escape(table)}\]\s*$", re.MULTILINE)
    match = pattern.search(raw)
    if match is None:
        return None
    next_match = re.search(r"^\[[^\]]+\]\s*$", raw[match.end() :], re.MULTILINE)
    end = match.end() + next_match.start() if next_match else len(raw)
    return raw[match.end() : end]


def ensure_features(raw: str) -> str:
    table_pattern = re.compile(r"^\[features\]\s*$", re.MULTILINE)
    match = table_pattern.search(raw)
    if match is None:
        suffix = "\n" if raw and not raw.endswith("\n") else ""
        return raw + suffix + "\n[features]\nmulti_agent = true\n"

    body_start = match.end()
    next_match = re.search(r"^\[[^\]]+\]\s*$", raw[body_start:], re.MULTILINE)
    body_end = body_start + next_match.start() if next_match else len(raw)
    body = raw[body_start:body_end]
    key_pattern = re.compile(r"^multi_agent\s*=.*$", re.MULTILINE)
    if key_pattern.search(body):
        body = key_pattern.sub("multi_agent = true", body, count=1)
    else:
        if body and not body.endswith("\n"):
            body += "\n"
        body += "multi_agent = true\n"
    return raw[:body_start] + body + raw[body_end:]


def source_agent_blocks(raw: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    for match in re.finditer(r"^\[agents\.([A-Za-z0-9_]+)\]\s*$", raw, re.MULTILINE):
        name = match.group(1)
        body_start = match.end()
        next_match = re.search(r"^\[[^\]]+\]\s*$", raw[body_start:], re.MULTILINE)
        body_end = body_start + next_match.start() if next_match else len(raw)
        blocks[name] = raw[match.start() : body_end].strip() + "\n"
    return blocks


updated = ensure_features(text)
existing_agents = set(re.findall(r"^\[agents\.([A-Za-z0-9_]+)\]\s*$", updated, re.MULTILINE))
missing_blocks = [block for name, block in source_agent_blocks(source).items() if name not in existing_agents]
if missing_blocks:
    suffix = "\n" if updated and not updated.endswith("\n") else ""
    updated = updated + suffix + "\n" + "\n".join(missing_blocks)

config_path.write_text(updated, encoding="utf-8")
PY
  cp -a "$CONFIG_PATH" "$RUN_DIR/config.toml.after"
}

write_manifests() {
  mkdir -p "$RUN_DIR"
  write_inventory "$RUN_DIR/pre-inventory.tsv"
  {
    echo "{"
    echo "  \"mode\": \"$MODE\","
    echo "  \"stage_only\": $STAGE_ONLY,"
    if [[ "$STAGE_ONLY" == "true" ]]; then
      echo "  \"config_merge\": false,"
    else
      echo "  \"config_merge\": true,"
    fi
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
    echo "  ],"
    echo "  \"pruned_symlinks\": ["
    local first_prune="true"
    local prune
    for prune in "${PRUNES[@]}"; do
      local target="${prune%%$'\t'*}"
      local rest="${prune#*$'\t'}"
      local source="${rest%%$'\t'*}"
      local kind="${rest#*$'\t'}"
      if [[ "$first_prune" == "false" ]]; then
        echo ","
      fi
      first_prune="false"
      printf '    {"target": "%s", "old_source": "%s", "kind": "%s", "type": "symlink"}' "$target" "$source" "$kind"
    done
    echo
    echo "  ]"
    echo "}"
  } > "$RUN_DIR/backup-manifest.json"
  {
    echo "{"
    echo "  \"mode\": \"$MODE\","
    echo "  \"stage_only\": $STAGE_ONLY,"
    if [[ "$STAGE_ONLY" == "true" ]]; then
      echo "  \"config_merge\": false,"
    else
      echo "  \"config_merge\": true,"
    fi
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
  } < <({ planned_global_agents_md; planned_skills; planned_agents; planned_cli; }) > "$RUN_DIR/symlink-manifest.json"
}

apply_symlinks() {
  local entries=()
  while IFS=$'\t' read -r target source; do
    [[ -z "$target" ]] && continue
    entries+=("$target"$'\t'"$source")
    mkdir -p "$(dirname "$target")"
  done
  local conflict
  for conflict in "${CONFLICTS[@]}"; do
    local target="${conflict%%$'\t'*}"
    if [[ -L "$target" ]]; then
      rm "$target"
    fi
  done
  local prune
  for prune in "${PRUNES[@]}"; do
    local target="${prune%%$'\t'*}"
    if [[ -L "$target" ]]; then
      rm "$target"
    fi
  done
  local entry
  for entry in "${entries[@]}"; do
    local target="${entry%%$'\t'*}"
    local source="${entry#*$'\t'}"
    if [[ -L "$target" ]]; then
      continue
    fi
    ln -s "$source" "$target"
  done
}

echo "mode: $MODE"
echo "root: $ROOT"
echo "codex_home: $CODEX_HOME"
if [[ "$STAGE_ONLY" == "true" ]]; then
  echo "config merge: skipped for staged install"
else
  echo "config merge: $CONFIG_PATH <= $CONFIG_SOURCE"
fi
echo "excluded: $CODEX_HOME/prompts"
echo "excluded: $HOME/.copilot"
echo "excluded: $HOME/.gemini"
if [[ "$STAGE_ONLY" != "true" && ":$PATH:" != *":$CLI_BIN_DIR:"* ]]; then
  echo "warning: $CLI_BIN_DIR is not on PATH; agent-harness CLI link will be installed there but may not be directly invokable" >&2
fi

echo "planned global AGENTS.md:"
if [[ "$STAGE_ONLY" == "true" ]]; then
  echo "none"
else
  while IFS=$'\t' read -r target source; do
    [[ -z "$target" ]] && continue
    echo "$target -> $source"
  done < <(planned_global_agents_md)
fi

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

echo "planned CLI:"
if [[ "$STAGE_ONLY" == "true" ]]; then
  echo "none"
else
  while IFS=$'\t' read -r target source; do
    [[ -z "$target" ]] && continue
    echo "$target -> $source"
  done < <(planned_cli)
fi

collect_stale_symlink_prunes

echo "planned stale symlink prunes:"
if [[ "${#PRUNES[@]}" -eq 0 ]]; then
  echo "none"
else
  prune=""
  for prune in "${PRUNES[@]}"; do
    target="${prune%%$'\t'*}"
    rest="${prune#*$'\t'}"
    source="${rest%%$'\t'*}"
    echo "$target -> $source"
  done
fi

echo "conflict policy: stop before replacing non-matching live targets"

if ! collect_conflicts < <({ planned_global_agents_md; planned_skills; planned_agents; planned_cli; }); then
  exit 1
fi

if [[ "$MODE" == "apply" ]]; then
  write_manifests
  { planned_global_agents_md; planned_skills; planned_agents; planned_cli; } | apply_symlinks
  merge_config
  write_inventory "$RUN_DIR/post-inventory.tsv"
  echo "manifest_dir: $RUN_DIR"
fi
