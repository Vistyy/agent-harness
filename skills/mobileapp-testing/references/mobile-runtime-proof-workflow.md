# Mobile Runtime Proof Workflow

Owner for live mobile runtime mechanics: stack setup, device targeting,
interaction, recovery, and mobile-specific evidence. Runtime verdict authority
belongs to `../../runtime-proof/SKILL.md`.

## Handoffs

- Runtime claim map, entrypoint fidelity, verdict, and reviewed-evidence rules:
  `../../runtime-proof/SKILL.md`
- Durable test versus one-shot proof: `../../testing-best-practices/SKILL.md`
- Review/closeout approval: `../../code-review/references/review-governance.md`

## Default Stack

1. Use the project-owned deterministic mobile runtime recipe.
2. Select exactly one emulator or device.
3. Use Dart MCP first.
4. Use adb only for install, launch, screenshot, recovery, or device lifecycle.

Do not infer mobile runtime behavior from desktop web proof, a widget test
alone, or an unlaunched build artifact.

## Preflight

Before mobile proof, name:
- binding objective and accepted reductions
- exact flow, platform, device/emulator, role, data, and state set
- design anchors when UI quality is claimed
- permission, OS-mediated, or lifecycle posture when material
- telemetry or trace IDs when material, or `none`
- unproved mobile/runtime boundaries, or `none`

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

For mobile proof, capture only evidence the verdict relies on:
- selected device/emulator posture
- flow exercised
- widget tree, logs, screenshots, or adb artifacts reviewed
- screenshot/device-captured visual artifacts for layout, safe-area, keyboard,
  permission, touch-target, or UI quality claims

Widget-tree presence alone is not layout or interaction proof.

For `runtime-risk-ui`, prove both composed hit-testable surface and live
emulator/device behavior in the same execution window.

Write flows need one real mutation plus outcome proof.

Recovery is project and host specific. Record one-off recovery commands only in
current-work evidence.
