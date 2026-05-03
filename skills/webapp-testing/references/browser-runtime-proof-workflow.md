# Browser Runtime Proof Workflow

Owner for browser preflight, live browser operation, browser-specific evidence,
and reporting details. Runtime verdict authority belongs to
`../../runtime-proof/SKILL.md`.

## Handoffs

- Runtime claim map, entrypoint fidelity, verdict, and reviewed-evidence rules:
  `../../runtime-proof/SKILL.md`
- Durable test versus one-shot proof: `../../testing-best-practices/SKILL.md`
- Route or state ownership: `../../system-boundary-architecture/references/web-boundaries.md`
- Review/closeout approval: `../../code-review/references/review-governance.md`

## Preflight

Before browser proof, name:
- binding objective and accepted reductions
- exact browser flow, state, role, data, and viewport set
- design anchors when UI quality is claimed
- telemetry or trace IDs when material, or `none`
- unproved browser/runtime boundaries, or `none`

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

Use the project-owned runtime recipe. It must cover starting dependencies,
serving the app, readiness, proof command, and shutdown. If live data is
required, discover candidates first, then prove the flow against actual runtime
data in the same execution window.

Pass `runtime_evidence` the binding objective, accepted reductions, target
flow, runtime recipe, variants, design anchors, constraints, and states to
inspect. Do not pass prewritten conclusions.

Use `check_runner` for large logs, traces, HTML dumps, console output, and
network output.

## Evidence

For browser proof, capture only evidence the verdict relies on:
- selected channel
- pages and flows exercised
- reviewed screenshots with viewport when visual quality is claimed
- bounded console/network findings when material
- diagnostic paths only when needed for triage

Prefer snapshots over screenshots for state checks. Use screenshots when visual
review, layout, hierarchy, responsive behavior, or design quality is claimed.

Write flows need one real mutation plus request/response or follow-up UI proof.

For `runtime-risk-ui`, prove hit testing, expected transition, responsive states
covered by the claim, and screenshot-backed UI quality.
