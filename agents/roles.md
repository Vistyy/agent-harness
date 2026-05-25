# Agent Roles

This overlay defines reusable coding-agent roles for adapters that support
named subagents.

Codex adapter role sources live under `adapters/codex/agents/`.
`skills/subagent-handoff/SKILL.md` owns invocation, handoff, and reuse
policy.
`AGENTS.md` is the standing user authorization to use these roles in a fresh
conversation. Agents must not wait for the user to mention subagents again when
`subagent-handoff` says to delegate.

## Roles

- `explorer`: read-only repository discovery and context compression; maps
  files, owners, call paths, risks, and open questions, but never returns code
  review findings or approval/block verdicts.
- `planning_critic`: strategy reviewer before non-trivial execution; challenges
  whether the proposed route and simplest correct end state should exist.
- `implementer`: one bounded assigned implementation slice.
- `quality_guard`: default bounded code-review role and early ruthless
  code-quality gate after implementation has a direction or draft diff, before
  bugs, drift, unreadable code, or bad structure compound.
- `final_reviewer`: final isolated closeout reviewer; judges whether the whole
  changed surface is merge-ready for the binding objective.
- `runtime_evidence`: independent live-use verifier for non-trivial
  runtime-visible claims when tests/reviews could pass while the app or service
  still fails.
- `design_judge`: screenshot-led visual-quality approval gate for broad
  product-facing UI claims.

Adapter configs must preserve these role names unless a reviewed migration
updates every consumer, validator, and live-install check together.
