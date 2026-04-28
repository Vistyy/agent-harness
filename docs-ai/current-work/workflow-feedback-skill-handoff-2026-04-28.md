# Workflow Feedback Skill Handoff - 2026-04-28

## Scope

Touched surfaces:

- `AGENTS.md`
- `skills/workflow-feedback/**`
- `skills/harness-governance/**`
- `skills/executing-plans/SKILL.md`
- `skills/subagent-orchestration/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- `adapters/codex/README.md`
- `adapters/codex/install-scope.md`
- `../../scripts/validate_harness.py`
- `tests/test_validate_harness.py`
- `skills/github-diagnostics/**` removal
- `skills/implementation-decision-ledger/**` removal
- `docs-ai/current-work/*audit-2026-04-27.md`

## Invariants

- `workflow-feedback` captures ambient workflow observations only.
- Material scope gaps still return to planning.
- Product bugs are fixed or routed through the owning project workflow.
- Reusable policy promotion remains owned by `harness-governance`.
- No run-scoped decision ledger or script-backed logging path remains.
- Subagent invocation is automatically approved when the active adapter supports
  subagents; omission of required subagents is a workflow defect,
  `subagent-orchestration` owns the reusable default, and runtime/tool
  constraints still apply.
- Non-trivial work has global planning/quality gates and global midstream
  design-change handling. Harness-governance adds only the harness-specific
  threshold and harness closeout fields.
- Generic closeout reporting is owned by `verification-before-completion`.
- Stale removed-skill references in live routing surfaces are validation
  failures.

## Proof Rows

| Claim | Proof |
|---|---|
| Removed skills no longer route. | `rg -n "implementation-decision-ledger\|github-diagnostics\|agent_decision\|agent-decisions" AGENTS.md skills agents adapters` returns no matches. |
| New workflow feedback route is discoverable. | `rg -n "workflow-feedback\|Workflow Feedback" AGENTS.md skills docs-ai/current-work` shows `AGENTS.md`, skill entrypoint, metadata, and audit notes. |
| No orphaned skill directories or metadata remain. | `uv run python ./scripts/validate_harness.py` passes. |
| Markdown and patch hygiene are clean. | `git diff --check` passes. |
| Repo quality gate remains green. | `just quality` passes. |
| Subagent authorization route is owned. | `rg -n "automatically approved|workflow defect" AGENTS.md skills/subagent-orchestration/SKILL.md` shows both the global map and owner skill. |
| Stale skill references are enforced. | `uv run pytest tests/test_validate_harness.py` covers stale skill tokens and missing skill-path references. |

## Counterfactual Probes

- A stale reference to either removed skill in live routing surfaces should be
  caught by targeted `rg`.
- An empty removed skill directory should fail `validate_harness.py`.
- Missing or malformed skill metadata should fail `validate_harness.py`.
- Low-level whitespace or conflict-marker issues should fail `git diff --check`.
- Removing the `subagent-orchestration` owner text should make the `AGENTS.md`
  rule unowned during review.
