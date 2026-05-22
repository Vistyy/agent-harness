# Browser Proof Layering

Owns browser vehicle choice and reviewed-versus-diagnostic artifact posture.
`../SKILL.md` owns proof selection and verdict.

## Vehicles

| Vehicle | Use when |
| --- | --- |
| Existing durable spec | A current browser spec already proves the claim. |
| Add/extend durable spec | The flow is regression-worthy, deterministic, and expected to recur. |
| `$playwright-interactive` | The proof needs live browser/Electron exploration, screenshots, UI inventory, or manual QA-style interaction. |
| `$playwright` | The proof is CLI-first browser automation through Playwright refs/snapshots. |
| `$screenshot` | The task needs OS-level capture or browser tooling cannot capture the surface. |
| Raw script | The standard routes cannot express the flow cleanly. |

Use existing durable proof first. Use upstream Playwright skills for mechanics
instead of restating their workflows here.

## Artifacts

Reviewed artifacts are intentionally selected, stable enough to cite, small,
stored under an explicit reviewed path, and sufficient to prove the claim.

Diagnostic artifacts are runner output, screenshots, traces, videos, console
dumps, and network logs used for triage. They are not evidence of record unless
cited in the verification report.

Do not promote every captured artifact. Do not shrink the reviewed set below
what proves the claim.
