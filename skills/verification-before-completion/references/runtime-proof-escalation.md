# Runtime Proof Escalation

Use runtime proof when the completion claim is user-visible, API-visible,
service-visible, integration-visible, or depends on live state.

## Entrypoint Fidelity

- `real-entrypoint`: the actual user/operator path.
- `scripted-entrypoint`: a project-supported command that exercises the same
  boundary.
- `adjacent-component`: nearby component or mocked boundary only.
- `artifact-only`: screenshot, build output, or static artifact without live
  behavior.

Broad readiness, end-to-end, or user-flow claims require `real-entrypoint` or a
clearly accepted narrower claim. Simulated or adjacent proof must name the
unproved boundary.

## Escalate To `runtime_evidence`

Use `runtime_evidence` for non-trivial runtime-visible claims unless the claim
is tiny, local, and has no public-behavior or cross-boundary runtime risk.

`reject`, `blocked`, or incomplete runtime evidence blocks or narrows the
affected claim.

Runtime proof does not replace code review or static quality gates.
