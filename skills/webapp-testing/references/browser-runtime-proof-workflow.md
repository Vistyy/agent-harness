# Browser Runtime Proof Workflow

Use before browser proof. This reference owns browser preflight,
runtime-loop mechanics, browser channel operation, helper paths, and
browser-specific reporting details.

## Direct Owner Handoffs

Load only when the condition applies:
- runtime proof affects claim strength:
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- producing or reviewing runtime evidence:
  `../../verification-before-completion/references/runtime-evidence-contract.md`
- placing proof artifacts:
  `../../verification-before-completion/references/verification-evidence.md`
- deciding durable specs/tests versus one-shot browser proof:
  `../../testing-best-practices/references/testing-strategy.md`
- touching route or state ownership:
  `../../system-boundary-architecture/references/web-route-and-state-boundary-doctrine.md`
- completing review/closeout fields:
  `../../code-review/references/review-governance.md`

## Preflight

Before browser proof:
- classify UI risk
- gather design anchors for UI quality claims
- gather approved archetype or justified exception when design scoring applies
- name material variants: auth posture, capability posture, local-vs-server
  authority, and any branch that changes owned behavior
- decide whether telemetry evidence matters; if yes, carry trace/correlation
  IDs plus artifact paths or say unavailable
- split data-dependent flows into candidate discovery then proof
- inspect live runtime data before choosing probes
- run proof in the same execution window as the claim

Variant rule:
- same route with different session or authority behavior is separate proof
- anonymous browse proof does not cover authenticated persistence
- server-owned writes need mutation plus follow-up read/reload in the same
  authenticated posture

If runtime data is missing, report `Runtime evidence: blocked` and the next
repo-supported step.

## Channel Selection

Use `browser-proof-layering-contract.md` for the channel matrix and
reviewed-vs-diagnostic artifact posture.

Workflow note: generic adapter browser tools may support diagnostics, but they
are not the Microsoft `playwright-cli` channel unless they explicitly expose
`microsoft/playwright-cli` / `@playwright/cli`.

## Delegation

Pass `runtime_evidence`:
- target flow and runtime recipe
- variants to exercise
- surface brief and anchors
- approved archetype or justified exception when design scoring applies
- constraints and must-check states
- actual states to inspect, not prewritten conclusions

Use `check_runner` for large logs, traces, HTML dumps, and console/network
bulk reading.

For diagnostics-heavy browser work, start from the observability-enabled agent
runtime by default and keep it enabled unless the task is explicitly narrow.

## Runtime Loop

Use the project-owned runtime recipe. It must say how to:
- start dependencies
- serve the browser app
- verify readiness
- run durable specs or Microsoft `playwright-cli` against the live base URL
- shut down cleanly

## Browser Proof Loop

Default one-shot channel: Microsoft `playwright-cli`
(`microsoft/playwright-cli`, `@playwright/cli`).
Do not call generic adapter browser tools the Playwright CLI channel unless
they explicitly expose this tool.

Default `playwright-cli` loop:
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
- promote only artifacts that the verdict actually relies on
- include the viewport for every screenshot used in a visual verdict

Use Chrome DevTools MCP or adapter browser diagnostics only as sidecars for
deep request inspection, targeted DOM probing, or performance analysis.

Clean orphaned sessions only when needed:

```bash
pkill -f 'run-cli-server --daemon-session='
```

## Helper Paths

Use helpers only when project runtime recipes, durable specs, and Microsoft
`playwright-cli` do not cover the proof need.

- `../scripts/with_server.py`: trusted local server wrapper. Do not use it for
  untrusted command strings or documented project topology.
- `../examples/console_logging.py`: bounded console capture.
- `../examples/element_discovery.py`: exploratory element inventory.
- `../examples/static_html_automation.py`: local static HTML probing.

## Proof Notes

For `runtime-risk-ui`, prove:
- visible surface is hit-testable
- underlying content does not steal interaction
- expected transition occurs
- reviewed screenshots are acceptable product evidence
- responsive state is checked for every viewport the claim covers

For interactive browser surfaces, also prove when relevant:
- interaction completeness
- failure and edge states
- one-source-of-truth consistency across UI and request posture
- route-shell versus screen-authority consistency
- runtime leg of any `multi-proof-required` claim

Write flows need one real mutation plus request/response evidence.

## Reporting

Runtime evidence reports must follow the runtime evidence owner and add
browser-specific details when material:
- selected browser proof channel
- UI risk class
- pages/flows verified
- reviewed viewport screenshots
- bounded console/network evidence

Include completion claim fields required by review governance.
