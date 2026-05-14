# Agent Harness

Reusable agent workflow harness.

This repository owns reusable skills, role adapters, policy references,
templates, prompts, and validation scripts for harness-managed projects.

Project-specific facts stay in each project overlay.

## Architecture

The harness is a contract kernel, not a project playbook. It gives agents a
small set of reusable owners and leaves product facts, runtime topology,
roadmap, queue state, local commands, and exceptions in each project.

The core workflow is:

1. `work-routing` chooses direct work, planning, or wave execution.
2. `design-integrity` selects the owner/interface that should make the
   objective true.
3. `readiness-claim` names exactly what may be claimed and what evidence must
   cross the selected interface.
4. `initiatives-workflow` stores durable wave, packet, delivery-map, and
   backlog state only when state must survive handoff, interruption, queueing,
   review, or multiple slices.
5. Execution happens through the selected owner/interface.
6. Evidence mechanisms report to the readiness claim:
   `runtime-proof`, `testing-best-practices`, `code-review`,
   `webapp-testing`, `mobileapp-testing`, and `user-apps-design`.
7. Closeout cannot exceed the binding objective, accepted reductions, selected
   design interface, and evidence actually reviewed.

Mechanism skills should not redefine readiness. Platform and tool skills
(`flutter-expert`, `svelte-code-writer`, `tailwind-design-system`,
`just-recipe-routing`, `uv`, `github-cli`) provide local execution mechanics.
Governance skills (`harness-governance`, `documentation-stewardship`) decide
where reusable rules live and keep one durable owner per concept.

Subagents are execution capacity, not ceremony. Use `explorer` for bounded
repository discovery and `implementer` for bounded implementation slices once
the design interface, readiness claim, and owned scope are clear enough to
handoff. The parent thread keeps orchestration, shared runtime lifecycle, final
claim synthesis, and review routing.

The intended shape is shallow at the top and precise at the edges: route,
design, claim, state, execute, prove, review, close.

Adapter:
- Codex: `adapters/codex/install.sh`

Reusable automation:
- `agent-harness wave refs --repo-root <project-root> --wave <wave-id>`
- `agent-harness wave cleanup --repo-root <project-root> --wave <wave-id>`
- `agent-harness wave bootstrap --repo-root <project-root> --wave <wave-id> --title "<title>"`
- `agent-harness governance check --repo-root <project-root>`
