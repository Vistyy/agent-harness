# Agent Harness

Reusable agent workflow harness.

This repository owns reusable skills, role adapters, policy references,
templates, prompts, and validation scripts for harness-managed projects.

Project-specific facts stay in each project overlay.

## Architecture

Keep this section high-level. It should describe the harness shape and owner
relationships, not restate skill bodies, adapter prompts, work-note fields, or
project-specific doctrine.

The harness is a contract kernel, not a project playbook. It gives agents a
small set of reusable owners and leaves product facts, runtime topology,
roadmap, queue state, local commands, and exceptions in each project.

The core workflow is `delivery-workflow`:

1. Start from the user objective or delivery-map memory.
2. Discover current repo reality and owner context.
3. Define objective coverage from entrypoint through production trigger,
   lifecycle owner, state, proof, cleanup, and closeout.
4. Choose the simplest coherent target system shape.
5. Decompose implementation slices from that shape.
6. Use adversarial planning review to test whether the note correctly
   interprets the objective.
7. Execute slices through the selected owner/interface.
8. Prove real behavior through the real interface or lifecycle.
9. Use adversarial final review to judge objective correctness and repository
   health.
10. Close honestly and update delivery-map/backlog memory.

Mechanism skills should not redefine readiness. Platform and tool skills
(`flutter-expert`, `svelte-code-writer`, `tailwind-design-system`,
`just-recipe-routing`, `uv`, `github-cli`) provide local execution mechanics.
Governance skills (`harness-governance`, `documentation-stewardship`) decide
where reusable rules live and keep one durable owner per concept.

Delivery maps and work notes are memory, not authority. A delivery-map item is
a remembered starting point for discovery, not executable scope. The current
objective, repo reality, owner docs, and reviewer judgment decide the work.

Subagents are adversarial engineering capacity, not ceremony. Use `explorer`
for bounded repository discovery and `implementer` for bounded implementation
slices once objective coverage, target shape, evidence strategy, and owned
scope are clear enough to hand off. Use `planning_critic`, `quality_guard`, and
`final_reviewer` to challenge strategy, implementation, and merge readiness against the user
objective and repo reality, not against artifact shape. The parent thread keeps
orchestration, shared runtime lifecycle, closeout synthesis, and review
routing.

The intended shape is shallow at the top and precise at the edges: preserve the
objective, discover enough to choose the final shape, execute meaningful
slices, prove real behavior, review repo health, and keep remaining required
work visible.

Adapter:
- Codex: `adapters/codex/install.sh`

Reusable automation:
- `agent-harness memory refs --repo-root <project-root> --item <item-id>`
- `agent-harness memory cleanup --repo-root <project-root> --item <item-id>`
- `agent-harness memory bootstrap --repo-root <project-root> --item <item-id> --title "<title>"`
- `agent-harness governance check --repo-root <project-root>`
