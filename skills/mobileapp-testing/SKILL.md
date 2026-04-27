---
name: mobileapp-testing
description: Use when validating mobile app runtime behavior; start deterministic agent runtime targets, prefer Dart MCP interaction, and use adb fallback with serial-scoped commands.
---

# Mobile Application Testing

Goal: prove mobile runtime behavior with deterministic device evidence.

Owners:
- runtime proof escalation: `../verification-before-completion/references/runtime-proof-escalation.md`
- UI risk classes: `the project UI verification strategy, when present`
- design anchors: `the project surface-discovery contract, when present`
- runtime evidence contract: `../verification-before-completion/references/runtime-evidence-contract.md`
- artifact placement: `../verification-before-completion/references/verification-evidence.md`
- delegation policy: `../subagent-orchestration/SKILL.md`

## Default Stack

1. Start the project-owned deterministic mobile runtime recipe.
2. Use single emulator/device path only.
3. Use Dart MCP first.
4. Use adb only for install/launch/screenshot/recovery.

For diagnostics or runtime-proof-heavy mobile work, keep the default agent loop
on the observability-enabled repo runtime. Use `OBSERVABILITY=false` only when
the task is explicitly narrow enough not to need trace/log queryability.

## Preflight

- Classify UI as `low-risk-ui`, `interaction-risk-ui`, or `runtime-risk-ui`.
- Default overlays, sheets, IME, safe-area, and hit-test sensitive flows to `runtime-risk-ui`.
- Gather design-intent anchors for UI quality claims.
- Gather chosen approved archetype or justified exception when end-user design
  scoring is in scope.
- Decide whether telemetry evidence matters for this proof; when it does, carry
  trace/correlation IDs plus log/trace artifact paths or state they were
  unavailable.
- Run proof in same execution window as claim.

When delegating to `runtime_evidence`, pass:
- target flow and runtime recipe,
- material branches and states to exercise,
- relevant surface brief and anchors,
- chosen approved archetype or justified exception when end-user design
  scoring applies,
- must-check constraints,
- not a prewritten list of design defects.

## Runtime Loop

Use the project-owned mobile runtime recipe for the target app. It must state how to start dependencies, select exactly one device or emulator, verify readiness, install or launch the app, collect screenshots or logs, and shut down cleanly.

Do not encode project service names, ports, device IDs, or host-specific recovery recipes in this global skill. Keep parallel-emulator exception guidance in `references/mobile-emulator-proof-contract.md`.

## Interaction Rules

- Prefer Dart MCP for logs, runtime errors, widget tree, controlled interaction.
- Use adb when DTD is unavailable, unstable, or device lifecycle work is needed.
- Keep adb serial-scoped.
- For text-heavy flows, prefer Dart MCP or deterministic app automation over raw adb typing.

## Proof Notes

Apply `runtime-proof-escalation.md` for runtime proof bar and
`testing-strategy.md` as the persistent-test doctrine router.

For `runtime-risk-ui`, prove both:
- screen/widget/integration test for composed hit-testable surface,
- live emulator/device proof in same execution window.

For interactive surfaces, also check when relevant:
- interaction completeness,
- failure and edge states,
- one-source-of-truth across visible state and downstream handoff,
- runtime leg of any `multi-proof-required` claim.

Write flows need one real mutation plus outcome proof.

## Recovery

Recovery steps are project and host specific. Keep durable guidance limited to explicit device targeting, deterministic restart, and artifact capture; record one-off recovery commands in current-work evidence only.

## Reporting

Runtime evidence reports should follow
`../verification-before-completion/references/runtime-evidence-contract.md` and
add mobile-specific details when material:
- selected device or emulator posture,
- UI risk class,
- flow verified,
- widget tree, log, screenshot, or adb artifacts reviewed.

Completion claim fields belong to `../code-review/references/review-governance.md`.
