---
name: webapp-testing
description: "Use for browser runtime proof and browser-visible UI validation; choose durable specs versus Microsoft playwright-cli one-shot proof, artifacts, screenshots, and diagnostics."
---

# Browser UI Testing

Goal: operate browser proof mechanics for browser-visible behavior.

Use `runtime_evidence` for live browser/runtime proof. Use `check_runner` for
targeted automated checks, log/trace sweeps, and large output triage.

Does not own completion-gate triggers, runtime verdict schema, or product
design anchors.

Project overlays own ports, services, upload-provider recipes, and runtime
topology.

## Required References

Read `references/browser-runtime-proof-workflow.md` before browser proof. It
owns preflight, runtime-loop, delegation, reporting, and direct owner handoffs
for runtime evidence, durable tests, artifacts, completion fields, and
route/state boundaries.

Read `references/browser-proof-layering-contract.md` before choosing the proof
channel.

Do not stop at this file for browser proof.
