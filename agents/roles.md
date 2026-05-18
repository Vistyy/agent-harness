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
- `planning_critic`: strategy reviewer before non-trivial execution; challenges
  whether the proposed route and simplest correct end state should exist.
- `implementer`: one bounded assigned implementation slice.
- `quality_guard`: in-thread planning/implementation reviewer; pressures the
  current work while it is still cheap to reshape.
- `final_reviewer`: final isolated closeout reviewer; judges whether the whole
  changed slice is merge-ready for the binding objective.
- `runtime_evidence`: independent live-use verifier for non-trivial
  runtime-visible claims when tests/reviews could pass while the app or service
  still fails.
- `design_judge`: screenshot-led visual-quality approval gate for broad
  product-facing UI claims.

Adapter configs must preserve these role names unless a reviewed migration
updates every consumer, validator, and live-install check together.
