# Mobile Runtime Proof

Owns mobile-specific proof integrity. Android emulator/device mechanics come
from the Test Android Apps plugin. Flutter/Dart inspection may use Dart MCP
when available.

## Preflight

Name exact flow, platform, device/emulator, role, data, state set, UI behavior
risk, permission/OS/lifecycle posture, telemetry/trace IDs or `none`, and
unproved mobile/runtime boundaries or `none`.

If deterministic device targeting cannot be established, report `blocked` or
narrow the claim with user acceptance.

## Mechanics

- Use the project-owned deterministic mobile runtime recipe when present.
- Select exactly one emulator or device unless the claim needs multiple.
- Prefer Dart MCP for Flutter logs, runtime errors, widget tree, and controlled
  interaction.
- Use the Test Android Apps plugin for adb launch, UI-tree coordinate picking,
  screenshots, logcat, lifecycle recovery, and Android performance evidence.
- Keep adb serial-scoped.

Do not infer mobile runtime behavior from desktop web proof, a widget test
alone, or an unlaunched build artifact.

## Evidence

Capture only evidence the verdict relies on: selected device/emulator posture,
flow, reviewed widget tree/logs/screenshots/adb artifacts, and device-captured
visual artifacts for layout, safe-area, keyboard, permission, touch target, or
claimed UI behavior.

Widget-tree presence alone is not layout or interaction proof. Write flows need
one real mutation plus outcome proof.

Mobile proof does not approve broad product visual quality. For that, hand
fresh screenshot/contact-sheet artifacts to `design_judge` through
`../../user-apps-design/SKILL.md`.
