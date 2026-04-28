---
name: webapp-testing
description: "Use for browser-visible UI or web runtime proof, including internal/admin surfaces; choose the strongest supported browser proof channel."
---

# Browser UI Testing

Goal: prove browser-visible behavior with live runtime evidence.

Use `runtime_evidence` for live browser/runtime proof. Use `check_runner` for
targeted automated checks, log/trace sweeps, and large output triage.

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
