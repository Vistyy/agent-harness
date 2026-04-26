# Agent Roles

This harness defines reusable coding-agent roles for adapters that support
named subagents.

Codex adapter role sources live under `adapters/codex/agents/`.

## Roles

- `explorer`: read-only repository discovery and context compression.
- `check_runner`: targeted checks, logs, and diagnostics summary.
- `planning_critic`: hostile planning review before execution-ready promotion.
- `implementer`: one bounded approved task-card or standalone-plan slice.
- `quality_guard`: planning-gate and in-thread implementation gate.
- `final_reviewer`: final isolated closeout review after verification.
- `runtime_evidence`: live runtime/UI/API proof.

Adapter configs must preserve these role names unless a reviewed migration
updates every consumer and proof row together.
