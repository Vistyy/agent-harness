---
name: verification-before-completion
description: Use before any completion or fix claim to gather fresh proof, run required just quality gates, and route runtime evidence when the claim needs it.
---

# Verification Before Completion

Fresh verification gate owner. No completion claim without fresh proof.

## Iron Law

`NO COMPLETION CLAIM WITHOUT FRESH VERIFICATION EVIDENCE`

If proving command or artifact is not from this execution window, claim is not proved.

## Reference Loading

Load owner docs as needed:
- gate semantics: `references/quality-gate-selection.md`
- runtime proof escalation: `references/runtime-proof-escalation.md`
- runtime evidence reports and visual verdicts: `references/runtime-evidence-contract.md`
- artifact and evidence placement: `references/verification-evidence.md`
- persistent-test strategy router:
  `../testing-best-practices/references/testing-strategy.md`
- review approval, disposition, and completion fields:
  `../code-review/references/review-governance.md`
- wave closeout: `../initiatives-workflow/references/initiatives-workflow.md`

## Outcome

Convert a completion or fix claim into fresh, scoped proof before the claim is
reported as done.

## Success Criteria

- exact claim is named and scoped
- proof class, owner, material branches, and counterfactual are explicit
- proving command or artifact is fresh for this execution window
- required quality gate and review status are reported
- required `runtime_evidence` verdict is reported when the claim needs live
  runtime proof

## Constraints

- Validate, fix, re-run.
- Do not stop at findings-only unless user asked for audit-only, blocker is external, or product decision is unresolved.
- Runtime-visible failure in changed surface becomes next bug by default.

## Required Reporting

Use `review-governance.md` for required completion fields. This skill adds the
fresh verification posture and the verification/runtime fields below.

Report when relevant:
- `Runtime claim map: cited in <artifact/path> | not-needed`
- `Entrypoint fidelity: exact | faithful-wrapper | simulated-boundary | adjacent-only | not-needed`
- `Runtime evidence: satisfied | blocked | skipped | incomplete`
- `Unproved runtime boundaries: none | <boundary + claim narrowing/follow-up>`
- `Diagnostics evidence: trace/log-linked | none-observed | limited-no-observability | not-needed`
- `Doc hygiene: updated | deferred (<reason>, <path>)`
- `System-boundary doctrine: satisfied | blocked | routed back to planning`

For non-trivial work, report changed surfaces, verification commands, and
residual verification risks. Include review verdict fields from
`review-governance.md`.

## Quality Gate Map

Use the repo's matching standard completion gate. Load
`references/quality-gate-selection.md` only when choosing between `quality`,
`quality-fast`, `quality-full`, or reusable local completion-gate semantics.
Hosted CI workflow names, branch-protection checks, and stack-specific command
bodies belong to the project overlay or repo-local workflow docs.

Rule: `quality-fast` is for iteration and CI baseline. Do not replace the
completion gate with it.

## Continue Until

Before any completion claim:
1. Name exact claim.
2. Name proof class and owner.
3. Name material auth/capability/state-authority branches for that claim.
4. Run proving command or collect proving artifact fresh for each material
   branch, or narrow claim explicitly.
5. Name one realistic weaker impl/regression the proof would reject.
6. Run required `just ... quality*` gate for touched scope.
7. Confirm owner-doc proof obligations for slice.
8. Confirm edge/failure probes when claim class needs them.
9. Confirm applicable review approvals/dispositions per `review-governance.md`.
10. For non-trivial runtime-visible claims, route or cite `runtime_evidence`.
    Tiny parent-local runtime proof is allowed only when the claim is local and
    has no public-behavior or cross-boundary runtime risk.
11. For non-trivial runtime-visible claims, cite the Runtime Claim Map from
    `references/runtime-proof-escalation.md`. Use the literal value not-needed
    only for non-runtime claims or tiny local runtime claims with no
    public-behavior or cross-boundary runtime risk. Final wording cannot exceed
    covered entrypoint fidelity, action, variants, observable result, and
    unproved boundaries.
12. For runtime/debug/observability-heavy claims, cite selected trace/log
    artifact/query pointers and selected trace/correlation IDs, or explicit
    `none observed`, or why observability was intentionally not used.
13. State final-review status using `review-governance.md` terms.

If any step is missing, do not claim done.

## Stop Conditions

- Previous runs do not count.
- Passing tests do not prove unrelated claims.
- Small diff does not waive quality gate.
- Interrupted delegated runtime proof means `Runtime evidence: incomplete`, not "pending enough."
- A `reject`, `blocked`, or incomplete runtime verdict blocks or narrows the
  affected runtime-visible claim.
- If runtime evidence covers only an adjacent component, helper, or artifact
  while the final claim says `works`, `ready`, `end-to-end`, or user flow,
  narrow the claim or run exact/faithful-entrypoint proof first.
- Final runtime-visible claims fail when they exceed the cited Runtime Claim
  Map or runtime evidence verdict.
- For UI/runtime claims, proof must review actual surface quality, not only happy-path success.
- For runtime/debug/observability-heavy claims, start from the
  observability-enabled repo runtime unless the claim is explicitly narrow
  enough not to need it; when observability stays off, say so.
- For telemetry or diagnostics-heavy claims, cite selected artifact/query
  pointers instead of raw dump blobs.
