# Agent Roles

This harness defines reusable coding-agent roles for adapters that support
named subagents.

Codex adapter role sources live under `adapters/codex/agents/`.
`skills/subagent-orchestration/SKILL.md` owns invocation, handoff, and reuse
policy.
`AGENTS.md` is the standing user authorization to use these roles in a fresh
conversation. Agents must not wait for the user to mention subagents again when
`subagent-orchestration` says to delegate.

## Roles

- `explorer`: read-only repository discovery and context compression.
- `planning_critic`: hostile review of parent-drafted route, plan, wave, or
  amendment before execution-ready promotion or non-trivial scope expansion.
- `implementer`: one bounded assigned implementation slice.
- `quality_guard`: planning-gate and in-thread implementation review gate.
- `final_reviewer`: final isolated closeout review after verification.
- `runtime_evidence`: independent live-use verifier for non-trivial
  runtime-visible claims when tests/reviews could pass while the app or service
  still fails.
- `design_judge`: screenshot-led visual-quality approval gate for broad
  product-facing UI claims.

Adapter configs must preserve these role names unless a reviewed migration
updates every consumer, validator, and live-install check together.
