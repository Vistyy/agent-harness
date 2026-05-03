---
name: webapp-testing
description: "Use for browser runtime proof mechanics: Playwright vehicles, browser sessions, screenshots, artifacts, console/network diagnostics, and viewport evidence."
---

# Browser UI Testing

Owns browser proof mechanics for browser-visible behavior.

Use `runtime_evidence` for live browser/runtime proof. Use `check_runner` for
targeted automated checks, log/trace sweeps, and large output triage.

Does not own runtime verdicts, completion triggers, or product design anchors.
Use `../runtime-proof/SKILL.md` for claim maps, entrypoint fidelity, blocking
verdicts, and evidence-of-record rules.

Project overlays own ports, services, upload-provider recipes, and runtime
topology.

## Required References

Read `references/browser-runtime-proof-workflow.md` before browser proof. It
owns browser preflight, runtime-loop mechanics, delegation inputs, browser
reporting, and direct owner handoffs.

Read `references/browser-proof-layering-contract.md` before choosing the proof
channel.

Do not stop at this file for browser proof.
