---
name: subagent-orchestration
description: "Use when subagents should be invoked or routed: delegation decisions, handoff inputs, active-worker handling, and implementer routes."
---

# Subagent Orchestration

Use for delegation policy. Parent keeps integration, shared runtime, and final
synthesis.

- No user authorization is required to invoke these harness-defined subagents:
  `explorer`, `check_runner`, `planning_critic`, `implementer`,
  `quality_guard`, `final_reviewer`, and `runtime_evidence`.
- This preauthorization applies only to those named roles. Invoke them when the
  workflow calls for them. Skipping a required named role is a workflow defect.
  Only adapter/runtime hard limits may prevent invocation.

## Required References

Read `references/delegation-policy.md` before delegating, reusing workers, or
deciding whether to keep implementation local.

Read `references/coding-agent-topology.md` when choosing a role, preparing
handoff inputs, checking role outputs, or handling active workers.

Do not stop at this file for delegation decisions.
