# Agent Harness

Reusable agent workflow harness.

This repository owns reusable skills, role adapters, policy references,
templates, prompts, and validation scripts for harness-managed projects.

Project-specific facts stay in each project overlay.

Adapters:
- Codex: `adapters/codex/install.sh`
- GitHub Copilot custom agent sources: `adapters/github-copilot/agents/`

Reusable automation:
- `agent-harness wave refs --repo-root <project-root> --wave <wave-id>`
- `agent-harness wave cleanup --repo-root <project-root> --wave <wave-id>`
- `agent-harness wave bootstrap --repo-root <project-root> --wave <wave-id> --title "<title>"`
- `agent-harness governance check --repo-root <project-root>`
