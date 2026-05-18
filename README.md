# Agent Harness

Reusable agent workflow harness.

This repository owns reusable skills, role adapters, policy references,
templates, prompts, and validation scripts for harness-managed projects.

Project-specific facts stay in each project overlay.

## Architecture

Keep this section high-level. It should describe the harness shape and owner
relationships, not restate skill bodies, adapter prompts, context-note fields, or
project-specific doctrine.

The harness is a contract kernel, not a project playbook. It gives agents a
small set of reusable owners and leaves product facts, runtime topology,
roadmap, queue state, local commands, and exceptions in each project.

The core workflow is:

1. `work-routing` chooses the route that can reach the simplest correct end
   state.
2. `design-integrity` selects the owner/interface that should make the
   objective true.
3. `readiness-claim` names exactly what may be claimed and what evidence must
   cross the selected interface.
4. `initiatives-workflow` stores durable context only when state must survive
   handoff, interruption, queueing, review, or multiple slices. That state is
   memory, not authority.
5. Execution happens through the selected owner/interface.
6. Evidence mechanisms report to the readiness claim:
   `runtime-proof`, `testing-best-practices`, `code-review`,
   `webapp-testing`, `mobileapp-testing`, and `user-apps-design`.
7. `readiness-claim` produces the final delivery brief for non-trivial work:
   outcome, end-state shape, plan coverage, evidence, reviewer verdicts,
   residuals, and context closeout.

Mechanism skills should not redefine readiness. Platform and tool skills
(`flutter-expert`, `svelte-code-writer`, `tailwind-design-system`,
`just-recipe-routing`, `uv`, `github-cli`) provide local execution mechanics.
Governance skills (`harness-governance`, `documentation-stewardship`) decide
where reusable rules live and keep one durable owner per concept.

Subagents are engineering capacity, not ceremony. Use `explorer` for bounded
repository discovery and `implementer` for bounded implementation slices once
the design interface, readiness claim, and owned scope are clear enough to
handoff. Use `planning_critic`, `quality_guard`, and `final_reviewer` to
challenge strategy, implementation, and merge readiness against the user
objective and repo reality, not against artifact shape. The parent thread keeps
orchestration, shared runtime lifecycle, final claim synthesis, and review
routing.

The intended shape is shallow at the top and precise at the edges: route to the
simplest correct end state, design the owner/interface, execute through that
owner, prove the claim, review the final shape, and close with a delivery brief
a non-code owner can trust.

Adapter:
- Codex: `adapters/codex/install.sh`

Reusable automation:
- `agent-harness wave refs --repo-root <project-root> --wave <wave-id>`
- `agent-harness wave cleanup --repo-root <project-root> --wave <wave-id>`
- `agent-harness wave bootstrap --repo-root <project-root> --wave <wave-id> --title "<title>"`
- `agent-harness governance check --repo-root <project-root>`
