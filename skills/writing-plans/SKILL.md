---
name: writing-plans
description: Use after requirements are clear to produce an executable implementation plan for generic non-wave work before touching product code.
---

# Writing Plans

Use for standalone implementation plans under `docs/plans/**`. Not for waves.

If work belongs to an active/proposed wave, stop and use `planning-intake` or `wave-autopilot`.

Owners:
- standalone-plan policy: `references/standalone-plans.md`
- completion gate: `../verification-before-completion/SKILL.md`
- approval and review semantics:
  `../code-review/references/review-governance.md`

## Outcome

Create a durable standalone implementation plan only when the work is non-wave,
requirements are clear, and material decisions are already closed.

## Success Criteria

- plan has one short goal and architecture summary
- decision closure and scope coverage are explicit
- ordered tasks name exact paths and task proof
- required follow-up is recorded
- approval record reflects real `planning_critic` and `quality_guard` review

## Preconditions

- requirements are closed,
- material behavior/migration/runtime/verification decisions are closed,
- work is not better represented as a wave.

If any material decision is still open, send work back to planning.

## Output Path

- `docs/plans/YYYY-MM-DD-<feature-name>.md`

Template/example:
- template: `assets/standalone-plan-template.md`
- example: `assets/standalone-plan-example.md`

## Required Sections

- short goal
- short architecture summary
- `Decision Closure Check`
- `Scope Coverage Plan`
- ordered implementation tasks with exact paths
- verification commands and expected evidence per task
- required doc/backlog follow-up
- `## Approval Record`

## Continue Until

1. Map surfaces and owners.
2. Close material decisions first.
3. Write `Scope Coverage Plan` for all in-scope surfaces.
4. Break work into small ordered tasks with exact files, commands, proof.
5. Add `## Approval Record` only after actual `planning_critic` review and
   final `quality_guard` approval. Use `standalone-plans.md` for record shape
   and `review-governance.md` for approval/disposition semantics.
6. Re-read as executor. If implementer still needs discovery, plan is not
   ready.

## Stop Conditions

- no vague verbs like "handle" or "clean up"
- use exact file paths
- every claimed surface needs proof
- do not infer approval from prose; use the `standalone-plans.md` approval record
- non-trivial work does not move to implementation from memory-only planning
- `docs/plans/**` is for concrete approved plans only
- route execution to `executing-plans`
