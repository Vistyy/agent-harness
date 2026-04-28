# Default Simplicity Posture

Use this for all planning, design, architecture, workflow, tests,
implementation, and review.

The rule is simple: keep the smallest honest shape that satisfies the required
outcome. Complexity must prove necessity. Simplicity does not.

Prefer, in order:
1. delete
2. collapse
3. demote to manual or breakglass
4. reuse an existing owner
5. add the smallest new structure that a real constraint requires

Do not preserve inherited ceremony, abstractions, tests, workflow steps,
compatibility paths, flags, adapters, or proof scaffolding because they already
exist.

Block or reshape when the plan:
- treats a symptom as the root problem
- moves complexity instead of removing it
- adds structure before proving direct reuse is insufficient
- keeps optional automation that can honestly stay manual
- preserves obsolete paths without owner and removal condition
- creates proof or process machinery instead of reducing the system
- narrows scope to avoid the owner that actually holds the problem

For accepted complexity, state the constraint that requires it. If that
constraint is absent, delete, collapse, demote, or block.
