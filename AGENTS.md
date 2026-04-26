# Agent Harness Global Instructions

Use this file as reusable cross-project baseline guidance. Project-local
`AGENTS.md` files own project facts and may add stricter local rules.

Precedence:
1. User instruction.
2. Project-local `AGENTS.md` loaded after this file.
3. Global harness skills.

## Scope

- Keep reusable workflow mechanics in harness skills.
- Keep reusable review, proof, planning, and architecture doctrine in harness
  skills and their references.
- Keep project identity, product facts, runtime topology, and active queue state
  in the target project.
- Do not put project-specific facts in this file.

## Routing

- Planning and wave shaping: use `planning-intake`.
- Full wave execution: use `wave-autopilot`.
- Durable documentation ownership: use `documentation-stewardship`.
- Review and completion claims: use `code-review`.
- Verification and gate selection: use `verification-before-completion`.
- Test design and test cleanup: use `testing-best-practices`.
- Architecture and owner-boundary changes: use `system-boundary-architecture`.
- Delegation and role boundaries: use `subagent-orchestration`.

## Operating Rules

- Prefer the simplest honest solution.
- Reuse or delete before adding.
- Do not leave reusable doctrine duplicated in project overlays.
- Do not replace project-local `AGENTS.md` with this global file.
- Project-local files should stay as concise overlays that point to the owning
  skills and project docs.
