# Objective-First Harness Prompt Contracts

## Backlog Item

Reshape process-heavy harness skills and adapter role prompts into
objective-first contracts where that reduces noise without weakening hard
invariants.

## Current Bucket

Deferred Backlog.

## Scope

Candidate files:
- `skills/planning-intake/SKILL.md`
- `skills/wave-autopilot/SKILL.md`
- `skills/verification-before-completion/SKILL.md`
- `skills/executing-plans/SKILL.md`
- `skills/writing-plans/SKILL.md`
- `adapters/codex/agents/*.toml`
- `adapters/github-copilot/agents/*.agent.md`

## Required Planning Shape

Before edits, inventory per-file invariants to preserve:
- planning gate and decision-closure semantics
- proof allocation and fresh-verification obligations
- stop-and-handback triggers
- role read/write limits
- ownership and boundary constraints
- final approval limits

Counterfactual proof must reject removing an invariant unless it is rehomed to
the owning skill or reference doc.
