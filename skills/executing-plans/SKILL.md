---
name: executing-plans
description: "Use to execute an already-approved standalone implementation plan under docs/plans; do not use for wave execution, which routes to wave-autopilot."
---

# Executing Plans

Execute approved standalone plan from `docs/plans/**`. Not for waves.

Owners:
- standalone-plan policy: `../writing-plans/references/standalone-plans.md`
- completion/evidence gate: `../verification-before-completion/SKILL.md`
- approval and review semantics: `../code-review/references/review-governance.md`
- minor local assumptions: `../implementation-decision-ledger/SKILL.md`

## Outcome

Execute one approved standalone plan without reopening its material design, and
claim completion only after plan-scoped proof is fresh.

## Success Criteria

- plan readiness is confirmed before edits
- each task follows approved scope and preserves decision closure
- minor local assumptions are logged only when pre-authorized
- verification evidence and quality gate outcomes are captured
- unresolved material gaps return to planning

## Preflight Constraints

Check plan only for readiness:
- `Decision Closure Check` closes material decisions
- `Scope Coverage Plan` covers all in-scope surfaces
- `## Approval Record` satisfies the standalone-plan policy; approval and
  disposition semantics come from `review-governance.md`
- requested work still matches approved scope

If material gap appears, stop and return to planning.

## Continue Until

For each task:
1. mark in progress
2. follow approved steps; do not reopen design
3. log only minor pre-authorized decisions when needed
4. run plan-specified verification and required quality gate
5. capture required evidence paths
6. stop if missing required surface or unresolved decision appears
7. mark complete only after fresh proof exists

Use `verification-before-completion` for gate selection and completion claim rules.

Memory-only planning is not executable for non-trivial work. If the approval
record is missing critic provenance, stop and return to planning.

## Output Shape

After each batch, report:
- tasks implemented
- verification commands and outcomes
- quality-gate command and outcome
- evidence paths
- unresolved ledger entries

If user asked for checkpointed execution, stop after batch. Else continue.

## Stop Conditions

Stop and return to planning when:
- plan lacks decision closure or scope coverage
- plan lacks valid `## Approval Record`
- execution finds material unresolved decision
- required in-scope surface is missing from plan
- verification keeps failing for reasons plan does not resolve
