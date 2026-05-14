---
name: webapp-testing
description: "Use for browser runtime proof mechanics: Playwright vehicles, browser sessions, screenshots, artifacts, console/network diagnostics, and viewport evidence."
---

# Browser UI Testing

Owns browser proof mechanics for browser-visible behavior.

Claim scope routes to `../readiness-claim/SKILL.md`; runtime mechanics route to
`../runtime-proof/SKILL.md`. Use `runtime_evidence` only when the runtime proof
plan requires an independent live-use verifier.

Does not own claim completeness, completion triggers, or visual approval.
Use `../readiness-claim/SKILL.md` for claim scope and
`../runtime-proof/SKILL.md` for entrypoint fidelity, blocking verdicts, and
evidence-of-record mechanics.

Project overlays own ports, services, upload-provider recipes, and runtime
topology.

## Required References

Read `references/browser-runtime-proof-workflow.md` before browser proof. It
owns browser preflight, runtime-loop mechanics, delegation inputs, browser
reporting, and direct owner handoffs.

Read `references/browser-proof-layering-contract.md` before choosing the proof
channel.

Do not stop at this file for browser proof.
