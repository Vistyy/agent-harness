---
name: mobileapp-testing
description: Use when validating mobile app runtime behavior; start deterministic runtime targets, prefer Dart MCP, and use serial-scoped adb for device lifecycle and recovery.
---

# Mobile Application Testing

Goal: prove mobile runtime behavior with deterministic device evidence.

Use `runtime_evidence` for live mobile/runtime proof. Use Dart MCP first. Use
adb only for install, launch, screenshot, recovery, or device lifecycle work.

Project overlays own service names, ports, device IDs, and host-specific
recovery recipes.

## Required References

Read `references/mobile-runtime-proof-workflow.md` before mobile runtime proof.
It owns default stack, preflight, runtime-loop, interaction, recovery, and
reporting rules, plus direct owner handoffs for runtime evidence, durable
tests, artifacts, and completion fields.

Read `references/mobile-emulator-proof-contract.md` when parallel emulator or
device lifecycle exception guidance matters.

Do not stop at this file for mobile runtime proof.
