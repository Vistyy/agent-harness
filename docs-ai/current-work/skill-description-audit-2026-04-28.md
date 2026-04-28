# Skill Description Audit - 2026-04-28

Audit focus:

- event-shaped triggers that should fire during ordinary work,
- broad triggers that are acceptable only with lean hot paths and exclusions,
- always-visible descriptions that should not hide critical invocation behavior
  in the skill body.

## Changes

| Skill | Disposition |
|---|---|
| `systematic-debugging` | Made the description more event-shaped for failing checks, build failures, performance issues, and unexpected behavior that appears during work. |
| `subagent-orchestration` | Made invocation/routing visible in the description and default prompt, matching the automatic-approval policy. |
| `code-review` | Made user-requested review an explicit description trigger instead of relying on body text. |

## No New Skill

No additional event deserves a separate skill after `workflow-feedback`.
Existing owners already cover review feedback, debugging, completion proof,
subagent routing, and work-route selection. The better correction was to make
their descriptions expose the event trigger more clearly.
