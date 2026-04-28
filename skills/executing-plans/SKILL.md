---
name: executing-plans
description: "Use to execute an already-approved standalone implementation plan under docs/plans; route wave execution to wave-autopilot."
---

# Executing Plans

Execute approved standalone plans from `docs/plans/**`.

Use `../writing-plans/references/standalone-plans.md` for standalone-plan
approval record requirements.

## Outcome

Execute one approved standalone plan without reopening its material design, and
claim completion only after plan-scoped proof is fresh.

## Success Criteria

- plan readiness is confirmed before edits
- each task follows approved scope and preserves decision closure
- minor implementation choices remain within pre-authorized scope
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
3. keep minor implementation choices inside the approved scope
4. run plan-specified verification and required quality gate
5. capture required evidence paths
6. stop if missing required surface or unresolved decision appears
7. mark complete only after fresh proof exists

Use the fresh verification gate before claiming task or plan completion.

Memory-only planning is not executable for non-trivial work. If the approval
record is missing critic provenance, stop and return to planning.

## Output Shape

After each batch, report:
- tasks implemented
- verification commands and outcomes
- quality-gate command and outcome
- evidence paths
- unresolved material gaps
- workflow observations captured separately, if any

If user asked for checkpointed execution, stop after batch. Else continue.

## Stop Conditions

Stop and return to planning when:
- plan lacks decision closure or scope coverage
- plan lacks valid `## Approval Record`
- execution finds material unresolved decision
- required in-scope surface is missing from plan
- verification keeps failing for reasons plan does not resolve
