# Review Lenses

Use during discovery, planning, decomposition, implementation review, final
review, evidence design, and closeout.

These lenses are binding when current-scope impact is credible. They are not
suggestions and not a checklist to satisfy with one sentence. Use them to
falsify whether the chosen target shape, proof path, and repository state are
acceptable for the binding objective.

Do not expand this file into full doctrine. When a lens needs specialized
rules, proof mechanics, or project facts, route to the owner skill or project
overlay.

## Material Risk Lenses

- security/privacy: changed access, secrets, personal data, authorization,
  trust boundary, or abuse path.
- data integrity: changed persistence, transactions, identifiers, ordering,
  idempotency, destructive behavior, or derived state.
- reliability: changed failure, retry, timeout, concurrency, recovery, or
  lifecycle assumptions.
- operability: changed deployment, support, operator workflow, rollback,
  configuration, or runbook expectation.
- observability/diagnosability: changed ability to detect, trace, explain, or
  debug important behavior.
- performance/cost: changed scale, latency, resource use, polling, fan-out,
  storage, or external-service cost.
- compatibility: changed public contract, persisted shape, migration path,
  flags, aliases, fallback, or parallel interface.
- accessibility: changed UI, CLI, or operator workflow that users must read,
  navigate, perceive, or operate.

Abuse resistance belongs under security/privacy. Legal/licensing/compliance is
out of default scope unless the objective, owner, project overlay, regulation,
dependency, or user triggers it.

## Engineering Quality Lenses

- simplicity: prefer the smallest coherent end state, not the smallest diff.
  Block avoidable owners, wrappers, flags, compatibility paths, private proof
  seams, duplicate state, or process/doc ceremony.
- cohesion/ownership: behavior belongs with the owner that controls its
  lifecycle, state, and failure behavior. Block wrong owners, split lifecycles,
  and wrappers that hide the real owner.
- testability/provability: behavior must be provable through honest public
  seams or real lifecycle entrypoints. Block private helper proof,
  over-mocking, hand-built state, impossible preconditions, and tests that pass
  while behavior is absent.
- evolvability: the target shape should make the next likely change easier or
  at least not harder. Block shapes that freeze temporary decisions, duplicate
  extension points, or create avoidable migration debt.
- maintainability/readability: names, boundaries, dependencies, and docs should
  make the new owner understandable. Block unclear ownership, hidden coupling,
  stale documentation, and cleanup skipped inside current scope.
- migration/cleanup: obsolete paths are removed or explicitly retained with
  owner, risk, and removal condition. Block zombie code, stale tests, stale
  docs, fake bridges, and backlog dumping of current-scope cleanup.
- slice integrity: narrow slices must honestly move the larger objective
  forward. Block slices that can pass while the end-to-end outcome remains
  incoherent or unstarted.
- dependency/tooling fit: new dependencies, tools, scripts, generated assets,
  and automation must be justified by the objective and repo conventions. Block
  avoidable tooling surface or dependencies used to bypass the real owner.

## Use

For each credible current-scope lens, decide:

- `not-applicable`: no credible path from the change to the lens.
- `covered`: planning, evidence, or review crosses the real owner/interface for
  the lens.
- `blocked`: current-scope risk is unproved, mis-owned, rejected, or
  contradicts the objective.
- `separate debt`: concrete risk is outside the active objective and routed to
  visible backlog.
- `accepted temporary debt`: user explicitly accepted the current-scope risk
  with owner, risk, removal condition, and backlog link.

Unassessed current-scope lens impact blocks planning approval, implementation
approval, and closeout.

Compatibility paths are rejected by default. Preserve obsolete behavior,
fallbacks, migration bridges, flags, aliases, or parallel interfaces only when
the user explicitly accepts the protected surface, owner, risk, and removal
condition.
