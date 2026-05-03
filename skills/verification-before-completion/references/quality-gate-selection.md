# Quality Gate Selection

Choose the smallest gate that proves the claim.

- Harness/workflow changes: `just quality-fast` plus
  `agent-harness governance check --repo-root .`.
- Project code changes: use the project `just ... quality*` owner command when
  present.
- Test-only changes: run the affected tests and any test-doctrine validation.
- Docs-only changes: run harness/project validation that checks those docs.
- Runtime-visible changes: static checks are not enough; add runtime evidence.

Do not substitute a cheaper gate when the claim depends on broader behavior.
