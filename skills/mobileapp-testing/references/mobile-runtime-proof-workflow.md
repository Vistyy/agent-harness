# Mobile Runtime Proof Workflow

Use before mobile runtime proof. This reference owns default stack, preflight,
runtime-loop mechanics, interaction, recovery, and mobile-specific reporting
details.

## Direct Owner Handoffs

Load only when the condition applies:
- runtime proof affects claim strength:
  `../../verification-before-completion/references/runtime-proof-escalation.md`
- producing or reviewing runtime evidence:
  `../../verification-before-completion/references/runtime-evidence-contract.md`
- placing proof artifacts:
  `../../verification-before-completion/references/verification-evidence.md`
- deciding durable tests versus one-shot mobile proof:
  `../../testing-best-practices/references/testing-strategy.md`
- completing review/closeout fields:
  `../../code-review/references/review-governance.md`

## Default Stack

1. Start the project-owned deterministic mobile runtime recipe.
2. Use one emulator/device path only.
3. Use Dart MCP first.
4. Use adb only for install, launch, screenshot, recovery, or device lifecycle.

For diagnostics-heavy mobile work, keep the default agent loop on the
observability-enabled repo runtime unless the task is explicitly narrow.

Do not infer mobile runtime behavior from a desktop web proof, a widget test
alone, or an unlaunched build artifact.

## Preflight

- Classify UI as `low-risk-ui`, `interaction-risk-ui`, or `runtime-risk-ui`.
- Default overlays, sheets, IME, safe-area, and hit-test-sensitive flows to
  `runtime-risk-ui`.
- Gather design-intent anchors for UI quality claims.
- Gather approved archetype or justified exception when design scoring applies.
- Decide whether telemetry evidence matters; if yes, carry trace/correlation
  IDs plus artifact paths or say unavailable.
- Run proof in the same execution window as the claim.

Pass `runtime_evidence`:
- target flow and runtime recipe
- material branches and states
- surface brief and anchors
- approved archetype or justified exception when design scoring applies
- constraints or states to inspect

## Runtime Loop

Use the project-owned mobile runtime recipe. It must state how to:
- start dependencies
- select exactly one device or emulator
- verify readiness
- install or launch the app
- collect screenshots or logs
- shut down cleanly

If the recipe cannot establish a deterministic device target, report blocked
or narrow the claim; do not continue with ambiguous emulator targeting.

## Interaction Rules

- Prefer Dart MCP for logs, runtime errors, widget tree, and controlled
  interaction.
- Use adb when DTD is unavailable, unstable, or device lifecycle work is needed.
- Keep adb serial-scoped.
- For text-heavy flows, prefer Dart MCP or deterministic app automation over raw
  adb typing.
- For camera, picker, permission, or OS-mediated flows, record the device
  posture and permission state that was actually exercised.

## Proof Notes

For `runtime-risk-ui`, prove both:
- screen/widget/integration test for composed hit-testable surface
- live emulator/device proof in the same execution window

For interactive surfaces, check when relevant:
- interaction completeness
- failure and edge states
- one-source-of-truth across visible state and downstream handoff
- runtime leg of any `multi-proof-required` claim

Write flows need one real mutation plus outcome proof.

Mobile UI quality claims need screenshots or device-captured visual artifacts
for the states under review. Widget-tree presence alone is not enough for
layout, safe-area, keyboard, permission, or touch-target claims.

## Recovery

Recovery is project and host specific. Durable guidance is limited to explicit
device targeting, deterministic restart, and artifact capture. Record one-off
recovery commands only in current-work evidence.

## Reporting

Runtime evidence reports must follow the runtime evidence owner and add
mobile-specific details when material:
- selected device or emulator posture
- UI risk class
- flow verified
- widget tree, log, screenshot, or adb artifacts reviewed

Include completion claim fields required by review governance.
