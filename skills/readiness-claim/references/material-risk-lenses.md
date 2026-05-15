# Material Risk Lenses

Owns material non-correctness risk disposition for readiness claims.

Use for non-trivial planning, handoff, proof, runtime evidence, review, or
completion claims when the risk can affect the binding objective, touched
owner/interface, proof path, runtime behavior, operator workflow, or approval
boundary.

## Lenses

Dispose material non-correctness risks across security/privacy, data integrity,
reliability, operability, observability/diagnosability, performance/cost,
compatibility, and accessibility when the changed surface affects UI, CLI, or
operator workflow.

- security/privacy
- data integrity
- reliability
- operability
- observability/diagnosability
- performance/cost
- compatibility
- accessibility when the changed surface affects UI, CLI, or operator workflow

Abuse resistance belongs under security/privacy. Legal/licensing/compliance
stays out of default scope; include it only when the binding objective, touched
owner, project overlay, regulation, dependency, or user explicitly triggers it.

## Planning Use

Planning does not mark future proof as `covered`. Before execution readiness,
record matched material risks, required evidence, current blockers or debt, and
any remaining proof owner. Final claims use the disposition labels below.

## Disposition

Use only these disposition labels:

- `not-applicable`: no credible path from the change to the lens.
- `covered`: proof/review crosses the claimed interface for the lens; the risk
  is proven for the claim.
- `blocked`: current-scope risk is unproved, mis-owned, rejected, or
  contradicts the claim. Narrowed claims map to `blocked` until the exact claim
  is revised and re-disposed.
- `separate debt`: concrete risk is outside the approval boundary and routed
  through the owning workflow.
- `accepted temporary debt`: user explicitly accepted the current-scope risk
  with owner, risk, removal condition, and backlog link.

Unassessed current-scope material risk blocks the claim. Routed debt, rejected
risks, and explicitly accepted temporary debt must still use one of the labels
above.

## Compatibility

Compatibility is rejected by default. Any current-scope compatibility path is a
blocker unless the user explicitly approves the specific protected surface,
owner, risk, and removal condition.

Do not preserve obsolete behavior, fallback paths, migration bridges, flags,
normalization aliases, or parallel interfaces as compatibility unless that
exception is explicit.

## Split Condition

Keep this reference as readiness disposition doctrine. Splitting becomes valid
only if it grows into procedure, scoring, domain-specific policy, or semantics
needed outside readiness, planning, proof, handoff, runtime evidence, review,
and completion claims.
