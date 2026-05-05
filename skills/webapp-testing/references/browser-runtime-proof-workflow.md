# Browser Runtime Proof Workflow

Owns browser preflight, live operation, browser evidence, and reporting
mechanics. Runtime verdict authority belongs to `../../runtime-proof/SKILL.md`.

## Handoffs

- Runtime claim map, entrypoint fidelity, verdict, and reviewed-evidence rules:
  `../../runtime-proof/SKILL.md`
- Durable test versus one-shot proof: `../../testing-best-practices/SKILL.md`
- Route or state ownership: `../../system-boundary-architecture/references/web-boundaries.md`

## Preflight

Add browser-specific claim-map inputs: exact flow, state, role, data, viewport,
UI behavior risks when claimed, material telemetry/trace IDs or `none`, and
unproved browser/runtime boundaries or `none`.

Same route with different auth, authority, session, or persistence behavior is
a different proof. Anonymous browse proof does not cover authenticated writes.
Server-owned writes need mutation plus follow-up read or reload in the same
authenticated posture.

## Vehicle

Use `browser-proof-layering-contract.md` to choose:
- existing durable spec
- added/extended durable spec
- Microsoft `playwright-cli`
- raw script fallback

Do not call generic browser tools the Playwright CLI channel unless they expose
`microsoft/playwright-cli` or `@playwright/cli`.

## Runtime Loop

Use the project-owned runtime recipe for dependencies, app serving, readiness,
proof command, and shutdown. If live data is required, discover candidates and
prove the flow against active runtime data in the same execution window.

When the runtime proof plan calls for `runtime_evidence`, pass the binding
objective, accepted reductions, target flow, recipe, variants, constraints, and
states to inspect. Do not pass prewritten conclusions.

Use `check_runner` for large logs, traces, HTML dumps, console output, and
network output.

## Evidence

Capture only evidence the verdict relies on: channel, pages/flows, screenshots
with viewport when layout or UI behavior is part of the runtime claim, bounded
console/network findings, and diagnostic paths when needed for triage.

Prefer snapshots over screenshots for state checks. Use screenshots when visual
layout, hit testing, transitions, or responsive behavior is part of the runtime
claim.

For broad UI design claims, browser mechanics may capture screenshot/contact
sheets for `design_judge` handoff: path, screen/state, viewport, freshness, and
claimed surface must be inspectable. Browser proof does not approve product UI
design.

Write flows need one real mutation plus request/response or follow-up UI proof.

For `runtime-risk-ui`, prove hit testing, expected transition, responsive states
covered by the claim, and any screenshot-backed behavior evidence the runtime
claim needs.
