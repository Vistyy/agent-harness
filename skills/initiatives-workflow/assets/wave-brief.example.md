# Example Wave

**Status:** execution-ready

## Objective Boundary

- original objective: simplify workflow harness docs without losing hard gates
- accepted reductions: no adapter topology change
- residual gaps: none

## Scope

- in scope: workflow skill bodies, workflow references, templates, adapter prompt
  references
- out of scope: project-specific overlays

## Closed Decisions

- route owner remains `work-routing`
- technical contracts remain with review, verification, packet, `agents/roles.md`,
  and subagent-orchestration owners

## Proof Plan

- line-count reduction: `wc -l <touched files>`
- harness validity: `just quality-fast`
- governance validity: `agent-harness governance check --repo-root .`

## Planning Gate

- planning_critic: `APPROVE, owner ledger accepted`
- quality_guard: `PENDING`

## Packet

- `docs-ai/current-work/example-wave/wave-execution.md`
