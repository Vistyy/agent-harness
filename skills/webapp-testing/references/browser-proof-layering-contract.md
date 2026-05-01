# Browser Proof Layering Contract

Owner for browser-proof channel selection, reviewed-vs-diagnostic artifact
posture, and browser-proof session conventions.

Does not own:
- proof classes or proof-depth selection:
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- screenshot anti-abuse policy:
  `../../verification-before-completion/references/runtime-evidence-contract.md`
- delegated screenshot verdict schema, severity language, or report shape:
  `../../verification-before-completion/references/runtime-evidence-contract.md`
- project smoke catalog selection
- flow-specific wrapper commands

## Purpose

Make browser proof path selection honest and predictable.

Contract:
- choose the cheapest durable proof that still proves the claim honestly
- keep reviewed evidence separate from diagnostic output
- keep the browser-proof decision matrix out of product-specific smoke design

## Browser Proof Channels

Select the first channel that honestly matches the claim and reuse posture.
Do not invent a surface-specific wrapper to avoid the matrix.

| Channel | Use when | Reviewed artifact posture | Diagnostic posture |
| --- | --- | --- | --- |
| `reuse spec` | A durable existing spec already proves the claim honestly. | Review the existing spec artifacts or promoted screenshots that prove the claim. | Keep normal runner output diagnostic unless explicitly promoted. |
| `extend/add spec` | The flow is regression-worthy, reasonably deterministic, and expected to recur. Use the project's durable browser spec stack, commonly Playwright Test. | Review the new or updated spec artifacts as the durable proof path. | Keep runner traces, videos, and transient logs diagnostic unless the claim needs them. |
| `playwright-cli` | The proof is one-shot, exploratory, weakly reusable, or not worth a durable spec yet. Use Microsoft playwright-cli (`microsoft/playwright-cli`, `@playwright/cli`). | Review the selected CLI screenshots or promoted CLI outputs only. | Keep default CLI output, console/network dumps, and other transient outputs diagnostic unless promoted. |
| `raw script` | Spec and CLI both cannot express the needed flow cleanly. | Review only the smallest stable artifacts worth promoting from the script run. | Treat script logs and ad hoc outputs as diagnostic by default. |

Selection rules:
- the channel follows claim shape and reuse value, not surface name
- if an existing durable spec is honest, use it before adding anything new
- if the flow is likely to recur, prefer extending or adding a durable spec
- if the proof is exploratory or triage-only, prefer Microsoft
  `playwright-cli`
- do not label generic adapter browser tools as `playwright-cli` unless they
  explicitly expose Microsoft `playwright-cli`
- raw script is the last resort only

## Reviewed Versus Diagnostic Artifacts

Reviewed artifacts:
- intentionally selected
- stable enough to cite in a verdict or packet
- kept small and overwriteable per named proof state
- live under `.artifacts/runtime/**` or another explicit reviewed-artifact path
- represent the evidence the reviewer is expected to inspect

Diagnostic artifacts:
- default runner output, screenshots, traces, videos, console dumps, and network
  logs used for triage
- keep their tool-native placement unless a reviewed artifact must be promoted
- are supporting material, not the evidence of record

Rules:
- do not promote every captured artifact into reviewed evidence
- do not treat diagnostic output as reviewed proof just because it exists
- when a proof is reviewed, name the reviewed artifact path explicitly
- when using browser proof for claim validation, keep the reviewed set small and
  intentional

## Session Conventions

- use a short stable browser-proof session name that encodes the target and
  state
- keep candidate-discovery and main-proof phases in the same session when the
  claim depends on runtime data
- when reporting proof, name selected channel, reviewed artifacts, and any
  diagnostic paths needed for triage
- do not add per-surface wrapper commands in this contract

## Related Owners

- runtime proof-depth policy:
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- runtime UI verdict schema:
  `../../verification-before-completion/references/runtime-evidence-contract.md`
- runtime artifact placement:
  `../../verification-before-completion/references/verification-evidence.md`
- browser proof entrypoint guidance:
  `webapp-testing`
