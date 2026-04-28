---
name: webapp-testing
description: "Use for browser-visible UI or web runtime proof, including internal/admin surfaces; choose the strongest supported browser proof channel."
---

# Browser UI Testing

Goal: prove browser-visible behavior with live runtime evidence.

Reference loading:
- route/state doctrine: `../system-boundary-architecture/references/web-route-and-state-boundary-doctrine.md`
- runtime proof escalation: `../verification-before-completion/references/runtime-proof-escalation.md`
- browser-proof layering: `references/browser-proof-layering-contract.md`
- UI risk classes: `the project UI verification strategy, when present`
- design anchors: `the project surface-discovery contract, when present`
- runtime evidence contract: `../verification-before-completion/references/runtime-evidence-contract.md`
- artifact placement: `../verification-before-completion/references/verification-evidence.md`

Use `runtime_evidence` for live browser/runtime proof. Use `check_runner` for
targeted automated checks, log/trace sweeps, and large output triage. If
runtime proof produces a large response, HTML dump, trace bundle, or console
blob, keep only the selected proof artifact in `runtime_evidence` and hand bulk
reading to `check_runner`.
For diagnostics or runtime-proof-heavy browser work, start from the
observability-enabled agent runtime by default. Keep observability enabled unless
the task is explicitly narrow enough not to need trace/log queryability.
Project-specific runtime recipes, upload-provider proof helpers, ports, and service topology stay in the project overlay.

## Preflight

Before browser proof:
- classify UI risk,
- gather design anchors for UI quality claims,
- gather chosen approved archetype or justified exception when end-user design
  scoring is in scope,
- name material behavior variants first: auth posture, capability posture,
  local-vs-server authority, and any other branch that changes owned behavior,
- decide whether telemetry evidence matters for this proof; when it does, carry
  trace/correlation IDs plus log/trace artifact paths or state they were
  unavailable,
- split data-dependent flows into candidate discovery then proof,
- inspect live runtime data before choosing probes,
- run proof in same execution window as claim.

Variant rule:
- if route is same but behavior differs by session or authority, treat each
  branch as separate proof target
- anonymous-safe browse proof does not cover authenticated persistence flow
- for server-owned write flows, include mutation and follow-up read/reload while
  still in authenticated posture

If runtime data is missing, report `Runtime evidence: blocked` plus next repo-supported step.

When delegating to `runtime_evidence`, pass:
- target flow and runtime recipe,
- material variants to exercise,
- relevant surface brief and anchors,
- chosen approved archetype or justified exception when end-user design
  scoring applies,
- constraints or must-check states,
- actual states to inspect rather than prewritten conclusions
- Use the browser-proof layering contract to decide the proof channel before
  delegating.

## Runtime Loop

Use the project-owned runtime recipe for the target web surface. It must state how to start dependencies, serve the browser app, verify readiness, run durable browser specs or Playwright CLI against the live base URL, and shut down cleanly.

Project overlays own ports, service names, upload-provider recipes, and topology
details.

## Browser Proof Layers

Select the proof channel in this order:
1. reuse an existing durable spec
2. extend or add a durable spec
3. use Playwright CLI for one-shot or weakly reusable proof
4. use a raw script only when durable specs and Playwright CLI cannot express the
   flow cleanly

## Playwright CLI Loop

Default loop:
1. open target page
2. capture baseline snapshot
3. execute real flow
4. capture post-action snapshot
5. gather bounded console/network evidence
6. capture screenshots only when visual review is required
7. close session

Rules:
- one named session per flow
- prefer snapshots over screenshots for state checks
- preserve only selected evidence under `.artifacts/runtime/**`
- use stable overwriteable screenshot filenames for reviewed states

Clean orphaned session when needed:

```bash
pkill -f 'run-cli-server --daemon-session='
```

## Chrome DevTools MCP

Use with Playwright CLI when the flow needs:
- deep request inspection
- targeted DOM probing
- performance analysis

## Helper Paths

Use these helpers when project runtime recipes, durable specs, and Playwright CLI
do not cover the proof need.

- `scripts/with_server.py`: starts trusted local server commands around one
  proof command when no project runtime recipe exists. Do not use it for
  untrusted command strings or when project topology is already documented.
- `examples/console_logging.py`: example for bounded console capture.
- `examples/element_discovery.py`: example for exploratory element inventory.
- `examples/static_html_automation.py`: example for local static HTML probing.

## Proof Notes

Apply `runtime-proof-escalation.md` for runtime proof bar and
`testing-strategy.md` as the persistent-test doctrine router.

For `runtime-risk-ui`, prove:
- visible surface is hit-testable,
- underlying content does not steal interaction,
- expected transition occurs,
- reviewed screenshots are acceptable product evidence.

For interactive browser surfaces, also prove when relevant:
- interaction completeness,
- failure and edge states,
- one-source-of-truth consistency across UI and request posture,
- route-shell versus screen-authority consistency,
- runtime leg of any `multi-proof-required` claim.

Write flows need one real mutating action plus request/response evidence.

## Reporting

Runtime evidence reports should follow
`../verification-before-completion/references/runtime-evidence-contract.md` and
add browser-specific details when material:
- selected browser proof channel,
- UI risk class,
- pages/flows verified,
- reviewed viewport screenshots,
- bounded console/network evidence.

Include completion claim fields required by
`../code-review/references/review-governance.md`.
