# Browser Proof Layering Contract

Owner for browser vehicle choice and browser-specific reviewed-versus-diagnostic
artifact posture. Runtime proof depth and verdict authority belong to
`../../runtime-proof/SKILL.md`.

## Rule

Choose the cheapest browser vehicle that honestly proves the runtime claim map.
Reviewed artifacts are the evidence of record; diagnostics are triage support.

## Vehicles

| Vehicle | Use when |
| --- | --- |
| Existing durable spec | A current browser spec already proves the claim. |
| Add/extend durable spec | The flow is regression-worthy, deterministic, and expected to recur. |
| Microsoft `playwright-cli` | The proof is one-shot, exploratory, or not worth durable spec coverage yet. |
| Raw script | Specs and `playwright-cli` cannot express the flow cleanly. |

Rules:
- vehicle follows claim shape and reuse value, not convenience
- use existing durable proof before adding new proof
- prefer durable specs for recurring regression risk
- prefer Microsoft `playwright-cli` (`microsoft/playwright-cli`,
  `@playwright/cli`) for one-shot browser proof
- raw script is last resort
- do not label generic adapter browser tools as `playwright-cli` unless they
  explicitly expose Microsoft `playwright-cli`

## Artifacts

Reviewed artifacts:
- intentionally selected
- stable enough to cite in a verdict
- small and overwriteable per named state
- stored under `.artifacts/runtime/**` or another explicit reviewed path
- sufficient to prove the claim

Diagnostic artifacts:
- default runner output, screenshots, traces, videos, console dumps, and network
  logs used for triage
- kept in tool-native placement unless promoted
- not evidence of record unless explicitly cited

Do not promote every captured artifact. Do not shrink the reviewed set below
what proves the claim.

## Reporting

Report selected vehicle, reviewed artifacts, diagnostic paths when material, and
unproved browser/runtime boundaries.
