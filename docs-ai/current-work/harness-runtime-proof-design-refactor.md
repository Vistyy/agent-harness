# Harness Runtime Proof And Design Refactor

## Scope

Refactor reusable harness ownership for completion claims, runtime proof, browser
proof mechanics, mobile proof mechanics, user-app design, and mobile-specific
design/boundary contracts.

## Planning Gate

- `planning_critic`: `019deecd-964c-7ac1-a1ad-fdb816f05a8a`
- Verdict: `REJECT` on the first umbrella `runtime-proof` proposal.
- Required correction: keep `runtime-proof` narrow as policy/verdict authority;
  keep `webapp-testing` and `mobileapp-testing` as platform mechanics owners;
  keep final claim authority in `verification-before-completion`; preserve
  mobile-specific design and boundary rules.

## Implementation Shape

- `runtime-proof` owns runtime-visible trigger, runtime claim map, entrypoint
  fidelity, verdict semantics, and blocking runtime findings.
- `webapp-testing` owns browser vehicles and evidence mechanics.
- `mobileapp-testing` owns emulator/device, Dart MCP, adb, and mobile evidence
  mechanics.
- `verification-before-completion` owns final claim assembly.
- `user-apps-design` owns general UI and mobile UI constraints.
- `system-boundary-architecture` owns mobile backend/offline/API/auth/version
  contracts.

## Review Loop

- `quality_guard`: `019deed6-91cb-7f03-8b0d-e38239baecb0`
- First verdict: `BLOCK`
- Required fixes:
  - move runtime proof trigger and tiny-local exemption into `runtime-proof`
  - add successor owner for mobile backend/offline rules
  - validate runtime trigger ownership
  - record planning-gate evidence here
- Final verdict: `APPROVE`
- Proof cited by reviewer: `uv run python scripts/validate_harness.py`,
  `uv run pytest tests/test_validate_harness.py -q`,
  `agent-harness governance check --repo-root .`, and `just quality-fast`.
