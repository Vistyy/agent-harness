---
name: mobileapp-testing
description: Use for live mobile runtime proof on emulator/device; prefer Dart MCP, keep adb serial-scoped for install, launch, screenshots, recovery, and device lifecycle.
---

# Mobile Application Testing

Goal: operate live mobile runtime proof mechanics with deterministic device
evidence.

Use `runtime_evidence` for live mobile/runtime proof. Use Dart MCP first. Use
adb only for install, launch, screenshot, recovery, or device lifecycle work.

Project overlays own service names, ports, device IDs, and host-specific
recovery recipes.

Does not own mobile design constraints or completion-gate verdict semantics.

## Required References

Read `references/mobile-runtime-proof-workflow.md` before mobile runtime proof.
It owns default stack, preflight, runtime-loop, interaction, recovery, and
reporting rules, plus direct owner handoffs for runtime evidence, durable
tests, artifacts, and completion fields.

Read `references/mobile-emulator-proof-contract.md` when parallel emulator or
device lifecycle exception guidance matters.

Do not stop at this file for mobile runtime proof.
