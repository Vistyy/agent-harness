# Mobile Runtime Proof Workflow

Owns mobile stack setup, device targeting, interaction, recovery, and
mobile-specific evidence. Runtime verdict authority belongs to
`../../runtime-proof/SKILL.md`.

## Handoffs

- Runtime claim map, entrypoint fidelity, verdict, and reviewed-evidence rules:
  `../../runtime-proof/SKILL.md`
- Durable test versus one-shot proof: `../../testing-best-practices/SKILL.md`

## Default Stack

1. Use the project-owned deterministic mobile runtime recipe.
2. Select exactly one emulator or device.
3. Use Dart MCP first.
4. Use adb only for install, launch, screenshot, recovery, or device lifecycle.

Do not infer mobile runtime behavior from desktop web proof, a widget test
alone, or an unlaunched build artifact.

## Preflight

Add mobile-specific claim-map inputs: exact flow, platform, device/emulator,
role, data, state set, UI behavior risks when claimed, material
permission/OS/lifecycle posture, telemetry/trace IDs or `none`, and unproved
mobile/runtime boundaries or `none`.

If the runtime recipe cannot establish deterministic device targeting, report
blocked or narrow the claim.

## Interaction

- Prefer Dart MCP for logs, runtime errors, widget tree, and controlled
  interaction.
- Keep adb serial-scoped.
- Prefer Dart MCP or deterministic app automation over raw adb typing.
- Record actual device posture for camera, picker, permission, lifecycle, and
  OS-mediated flows.

## Evidence

Capture only evidence the verdict relies on: selected device/emulator posture,
flow, reviewed widget tree/logs/screenshots/adb artifacts, and device-captured
visual artifacts for layout, safe-area, keyboard, permission, touch-target, or
claimed UI behavior.

Widget-tree presence alone is not layout or interaction proof.

For broad UI design claims, mobile mechanics may capture screenshot/contact
sheets for `design_judge` handoff: path, screen/state, device/viewport,
freshness, and claimed surface must be inspectable. Mobile proof does not
approve product UI design.

For `runtime-risk-ui`, prove both composed hit-testable surface and live
emulator/device behavior in the same execution window.

Write flows need one real mutation plus outcome proof.

Recovery is project and host specific. Record one-off recovery commands only in
current-work evidence.
