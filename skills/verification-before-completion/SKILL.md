---
name: verification-before-completion
description: Use before any completion or fix claim to gather fresh proof, run required just quality gates, and route runtime evidence when the claim needs it.
---

# Verification Before Completion

Fresh verification gate owner. No completion claim without fresh proof.

## Iron Law

`NO COMPLETION CLAIM WITHOUT FRESH VERIFICATION EVIDENCE`

If proving command or artifact is not from this execution window, claim is not proved.

## Owner Map

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
- structural doctrine: `../system-boundary-architecture/SKILL.md`
- delegation policy: `../subagent-orchestration/SKILL.md`

## Default Posture

- Validate, fix, re-run.
- Do not stop at findings-only unless user asked for audit-only, blocker is external, or product decision is unresolved.
- Runtime-visible failure in changed surface becomes next bug by default.

## Required Reporting

Use `review-governance.md` for required completion fields. This skill owns the
fresh verification posture and the verification/runtimes fields below.

Report when relevant:
- `Runtime evidence: satisfied | blocked | skipped | incomplete`
- `Diagnostics evidence: trace/log-linked | none-observed | limited-no-observability | not-needed`
- `Doc hygiene: updated | deferred (<reason>, <path>)`
- `System-boundary doctrine: satisfied | blocked | routed back to planning`

## Quality Gate Map

`references/quality-gate-selection.md` owns semantics. Use matching repo gate:

| Scope | Before completion | Higher bar when explicitly needed |
|---|---|---|
| Cross-stack / unclear impact | `just quality` | `just quality-full` |
| Python | `just python quality` or `just pt quality` | `just python quality-full` |
| Web | `just web quality` | `just web quality-full` |
| Mobile | `just mobile quality` or `just mob quality` | `just mobile quality-full` |
| Infra | `just infra quality` | `just infra quality-full` |

Use `quality-fast` during implementation. Do not replace completion gate with it.

## Gate Checklist

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
10. For runtime/debug/observability-heavy claims, cite selected trace/log
    artifact/query pointers and selected trace/correlation IDs, or explicit
    `none observed`, or why observability was intentionally not used.
11. State final-review status using `review-governance.md` terms.

If any step is missing, do not claim done.

## Guardrails

- Previous runs do not count.
- Passing tests do not prove unrelated claims.
- Small diff does not waive quality gate.
- Interrupted delegated runtime proof means `Runtime evidence: incomplete`, not "pending enough."
- For UI/runtime claims, proof must review actual surface quality, not only happy-path success.
- For runtime/debug/observability-heavy claims, start from the
  observability-enabled repo runtime unless the claim is explicitly narrow
  enough not to need it; when observability stays off, say so.
- For telemetry or diagnostics-heavy claims, cite selected artifact/query
  pointers instead of raw dump blobs.
