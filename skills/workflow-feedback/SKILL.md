---
name: workflow-feedback
description: "Use when work reveals workflow friction, recurring agent/process issues, or review patterns not fixed immediately."
---

# Workflow Feedback

Use this skill when implementation, review, verification, or repeated execution
reveals workflow friction or a recurring agent/process issue that is not fixed
in the current change.

Handle product bugs, approved implementation choices, and material scope gaps in
the active workflow: fix directly, follow the plan, or return to planning.

## Ledger

Project-specific observations belong in the target project:

- `docs-ai/current-work/workflow-feedback-ledger.md`

If the ledger is missing, create it from:

- `assets/workflow-feedback-ledger.md`

Keep entries compact:

- date
- reporter/context
- observed workflow issue
- affected project or harness surface
- suggested disposition: `project-fix`, `harness-candidate`, `skill-candidate`,
  `validation-candidate`, or `discard`
- status: `open`, `promoted`, `fixed`, or `discarded`

## Promotion

Use `../harness-governance/SKILL.md` when an entry may become reusable harness
policy, skill guidance, adapter posture, or validation.

Periodic review should promote reusable findings into the harness repository or
close them with a reason. Do not store reusable global policy only in a project
ledger.
