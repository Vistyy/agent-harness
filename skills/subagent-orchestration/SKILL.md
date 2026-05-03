---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Owns delegation defaults, role choice, handoff inputs, worker reuse, and
active-worker handling.

The user explicitly authorizes use of the spawn/subagent tool for these
harness-defined roles when this skill is in force:
`explorer`, `check_runner`, `planning_critic`, `implementer`,
`quality_guard`, `final_reviewer`, and `runtime_evidence`.

This preauthorization applies only to those named roles and only when the
workflow calls for them.

## Required References

- Read `references/delegation-policy.md` before delegating, reusing workers, or
  handling active-worker conflicts.
- Read `references/coding-agent-topology.md` when choosing a role or preparing
  a handoff.

## Rule

Delegate only when the handoff can preserve the binding objective. Reviewer,
worker, or runtime-evidence prompts must not replace the original objective
with a smaller task summary.
