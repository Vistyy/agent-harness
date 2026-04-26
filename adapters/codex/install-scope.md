# Codex Install Scope

The baseline Codex adapter installs only individual symlinks:

- `~/.codex/skills/<skill-name>` -> `skills/<skill-name>`
- `~/.codex/agents/<agent-name>.toml` -> `adapters/codex/agents/<agent-name>.toml`

It never replaces whole directories.

## Excluded Surfaces

Baseline install must not mutate:

- `~/.codex/config.toml`
- `~/.codex/prompts`
- `~/.copilot`
- `~/.gemini`

Prompt, Copilot, and Gemini/Antigravity installation behavior is intentionally
not preserved in this reusable baseline. Copilot can read project-local skill
folders through editor configuration. Gemini support can be reintroduced later
only through a concrete reviewed request.

Backups are rollback evidence. They do not authorize replacing unknown user
content.
