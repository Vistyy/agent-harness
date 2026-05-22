# Agent Workflow Overlay

Reusable workflow overlay for agents.

This repository owns reusable skills, role adapters, policy references,
templates, prompts, and validation scripts that fit agent workflows to the way
this workspace works.

Project-specific facts stay in each project overlay.

## Architecture

Keep this section high-level. It should describe the overlay shape and owner
relationships, not restate skill bodies, adapter prompts, work-note fields, or
project-specific doctrine.

The overlay is a compact contract layer, not a project playbook. It gives
agents a small set of reusable workflow owners and leaves product facts,
runtime topology, roadmap, queue state, local commands, and exceptions in each
project.

The core loop is:

1. Define the real objective when needed.
2. Inspect current repo reality.
3. Shape the simplest coherent final solution.
4. Decompose work without narrowing the objective.
5. Implement focused slices through the selected owner/interface.
6. Verify with proof that would fail if the claim were false.
7. Use planning, quality, and final reviewers when risk warrants.
8. Keep memory and docs current without making notes authoritative.
9. Report blockers honestly instead of substituting fake progress.

Mechanism skills should not redefine readiness. Upstream OpenAI skills and
plugins provide mechanics for browser testing, screenshots, Android QA,
GitHub, security, and durable CLI creation. Local overlay skills preserve
objective integrity, proof honesty, handoff discipline, and memory/document
lifecycle.

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
slices, verify honestly, review repo health, and keep remaining required work
visible.

Adapter:
- Codex: `adapters/codex/install.sh`

Reusable automation:
- `agent-harness memory refs --repo-root <project-root> --item <item-id>`
- `agent-harness memory cleanup --repo-root <project-root> --item <item-id>`
- `agent-harness memory bootstrap --repo-root <project-root> --item <item-id> --title "<title>"`
- `agent-harness governance check --repo-root <project-root>`
