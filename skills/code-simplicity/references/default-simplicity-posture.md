# Default Simplicity Posture

Use for planning, design, architecture, workflow, tests, implementation, and
review.

The rule: complete the required outcome with the least structure that can
honestly make it true.

Prefer, in order:
1. delete
2. collapse
3. demote to manual or breakglass
4. reuse an existing owner
5. add only the structure a real constraint requires

Block or reshape when the plan:
- treats a symptom as the root problem
- preserves the wrong owner or duplicated authority
- patches around a defect that affects the current objective
- moves complexity instead of removing it
- keeps optional workflow, proof, adapter, flag, or compatibility ceremony
- narrows breadth, quality, runtime behavior, or review surface without
  accepted reduction
- defers debt that belongs to the current objective or touched owner

Accepted complexity needs the constraint that requires it. Accepted debt needs
owner, risk, and removal condition.
