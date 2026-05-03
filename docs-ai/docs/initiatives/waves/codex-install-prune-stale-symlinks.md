# Wave codex-install-prune-stale-symlinks - Codex install stale symlink pruning

**Status:** done

## Problem

Codex reinstall creates and refreshes current harness symlinks but leaves stale
harness-owned skill/agent symlinks from removed or refactored skills.

## Objective

Codex install prunes only stale harness-owned skill/agent symlinks and records
the pruning without touching user-owned files, directories, `.system`, or
external symlinks.

## In Scope

- `codex/install-prune-stale-symlinks`

## Out Of Scope

- Removing regular files or directories from `$CODEX_HOME`.
- Mutating prompts, Copilot, Gemini, or project overlays.

## Constraints / Non-Goals

- Only prune symlinks under `$CODEX_HOME/skills` and `$CODEX_HOME/agents`.
- Only prune links whose target resolves inside this harness repo and whose
  basename is not in the current planned install set.
- Keep `.system` and external symlinks.
- `--stage-harness-governance` does not prune stale symlinks.

## Risks / Dependencies

- Risk: destructive installer behavior. Disposition: exact symlink-only scope,
  dry-run output, manifest entry, smoke test, and live verification.

## References

- Codex installer script
- Codex install smoke test
- Codex install scope doc
- Codex live install check script

## Planning Gate

- planning_critic: APPROVE on 2026-05-04 after destructive proof fixes.
- planning quality_guard: APPROVE on 2026-05-04 after stage-only and live
  inventory proof fixes.

## Closeout

- Implemented symlink-only stale prune for Codex full install.
- Stage-only install does not prune.
- Isolated smoke, live reinstall/check, harness validation, governance check,
  validator tests, and `just quality-fast` passed.
- final_reviewer: APPROVE on 2026-05-04 after exact repo-root symlink fix.
