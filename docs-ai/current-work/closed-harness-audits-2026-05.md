# Closed Harness Audits - 2026-05

This is a compact archive of completed harness audit and cleanup records.
There is no active execution plan in this file.

## Closed Records

### Runtime Evidence Guard Policy - 2026-05-01

- Made `runtime_evidence` the bounded live validation guard for handed-off
  runtime-visible UI, API, service, and mobile claims.
- Clarified single owners:
  `verification-before-completion` for completion gating,
  `runtime-proof-escalation.md` for runtime proof triggers,
  `runtime-evidence-contract.md` for verdict/report shape,
  `webapp-testing` for browser proof mechanics,
  `mobileapp-testing` for emulator/device proof mechanics,
  `user-apps-design` for end-user design direction, and
  `mobile-design` for mobile design constraints.
- Anchored browser one-shot proof on Microsoft `playwright-cli`
  (`microsoft/playwright-cli`, `@playwright/cli`) and kept generic adapter
  browser tooling as diagnostics unless it explicitly exposes that channel.
- Tightened mobile proof around deterministic device targeting, Dart MCP first,
  serial-scoped adb, and screenshot/device artifacts for mobile UI quality
  claims.
- Updated adapter prompts and Codex adapter role descriptions so
  `runtime_evidence` returns `pass | reject | blocked` with claim boundary and
  block impact, without debugging, planning, code review, or project-local
  design doctrine.
- Added lightweight validation for runtime_evidence project-doc leakage,
  wrapped stale optional-helper runtime wording, and Microsoft playwright-cli
  browser-proof anchors.
- Deferred only report-only behavioral skill eval exploration to:
  `docs-ai/current-work/backlog/harness__skill-evals__report-only.md`.
- Final verification passed:
  `uv run pytest tests/test_validate_harness.py`,
  `uv run python scripts/validate_harness.py`, `git diff --check`, and
  `just quality-fast`.
