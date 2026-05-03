# Browser Proof Layering Contract

Owns browser vehicle choice and browser reviewed-versus-diagnostic artifact
posture. Runtime proof depth and verdict authority belong to
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

Vehicle follows claim shape and reuse value, not convenience. Use existing
durable proof first; prefer durable specs for recurring regression risk;
prefer Microsoft `playwright-cli` (`microsoft/playwright-cli`,
`@playwright/cli`) for one-shot proof; raw script is last resort. Do not label
generic adapter browser tools as `playwright-cli` unless they expose Microsoft
`playwright-cli`.

## Artifacts

Reviewed artifacts are intentionally selected, stable enough to cite, small and
overwriteable per named state, stored under `.artifacts/runtime/**` or another
explicit reviewed path, and sufficient to prove the claim.

Diagnostic artifacts are runner output, screenshots, traces, videos, console
dumps, and network logs used for triage. Keep them in tool-native placement
unless promoted; they are not evidence of record unless cited.

Do not promote every captured artifact. Do not shrink the reviewed set below
what proves the claim.

## Reporting

Report selected vehicle, reviewed artifacts, diagnostic paths when material, and
unproved browser/runtime boundaries.
