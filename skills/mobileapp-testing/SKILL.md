---
name: mobileapp-testing
description: "Use for mobile runtime proof mechanics: emulator/device execution, Dart MCP, serial-scoped adb, screenshots, logs, widget trees, recovery, and lifecycle."
---

# Mobile Application Testing

Owns live mobile runtime proof mechanics with deterministic device evidence.

Claim scope routes to `../readiness-claim/SKILL.md`; runtime mechanics route to
`../runtime-proof/SKILL.md`. Use `runtime_evidence` only when the runtime proof
plan requires an independent live-use verifier. Use Dart MCP first. Use adb
only for install, launch, screenshot, recovery, or device lifecycle work.

Project overlays own service names, ports, device IDs, and host-specific
recovery recipes.

Does not own mobile design constraints or claim completeness. Use
`../readiness-claim/SKILL.md` for claim scope and
`../runtime-proof/SKILL.md` for entrypoint fidelity, blocking verdicts, and
evidence-of-record mechanics.

## Required References

Read `references/mobile-runtime-proof-workflow.md` before mobile runtime proof.
It owns default stack, preflight, runtime-loop, interaction, recovery, and
reporting rules, plus direct owner handoffs.

Read `references/mobile-emulator-proof-contract.md` when parallel emulator or
device lifecycle exception guidance matters.

Do not stop at this file for mobile runtime proof.
