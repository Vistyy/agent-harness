# Harness Testing Contract

**Status:** done

## Objective Boundary

- original objective: compact the testing/proof stack by making
  `testing-best-practices` own persistent tests only, while preserving the
  valuable layer, proof-strength, touched-test, waiting, and corpus-cleanup
  rules.
- accepted reductions: none.
- residual gaps: none.

## Scope

- in scope: `skills/testing-best-practices/**`, direct references from other
  harness skills, removed-path validation updates, validation tests.
- out of scope: runtime verdict semantics, final completion claims, browser or
  mobile proof mechanics, project-specific test strategy.

## Closed Decisions

- persistent tests protect durable boundaries and reject named weaker
  implementations.
- layer choice and red evidence in `testing-best-practices` are scoped to
  persistent tests or persistent static/contract checks.
- runtime proof, completion claims, browser mechanics, and mobile mechanics
  stay with their existing owners.
- merge the normal-test-edit rules into one persistent-test contract reference.
- keep corpus cleanup as a compact conditional section in
  `skills/testing-best-practices/SKILL.md` because repo-wide cleanup is a
  different mode from normal test edits but not enough to justify a separate
  reference.
- intentionally deleted invariant set: none.

## Proof Plan

- harness validation: `uv run python scripts/validate_harness.py`
- validator tests: `uv run pytest tests/test_validate_harness.py -q`
- quality fast: `just quality-fast`
- governance check: `agent-harness governance check --repo-root .`
- stale live-reference scan for retired testing references outside this packet.

## Planning Gate

- planning_critic: APPROVE on 2026-05-03. Packet treats the work as
  structural, scopes `testing-best-practices` to persistent tests/static
  contract checks, includes platform mechanics owners in owner-split proof, and
  names exact retired paths.
- planning quality_guard: APPROVE on 2026-05-03. Packet is execution-ready:
  successor readback preserves retained invariants, structural owner split is
  closed, exact retired paths are named, stale-reference proof is concrete, and
  no accepted debt remains.
- implementation quality_guard: APPROVE on 2026-05-03. Persistent-test-only
  owner split is coherent, successor rules are preserved, corpus cleanup
  remains conditional, and removed-path validation aligns with the packet.

## Packet

- closed after final review on 2026-05-03.
