# Codex Install Scope

The baseline Codex adapter installs only individual symlinks:

- `~/.codex/AGENTS.md` -> `AGENTS.md`
- `~/.codex/skills/<skill-name>` -> `skills/<skill-name>`
- `~/.codex/agents/<agent-name>.toml` -> `adapters/codex/agents/<agent-name>.toml`

It never replaces whole directories.

Full apply also merges the required Codex role config into
`~/.codex/config.toml` after backing up the live file. It does not symlink or
wholesale replace live config.

## Excluded Surfaces

Baseline install must not mutate:

- `~/.codex/prompts`
- `~/.copilot`
- `~/.gemini`

Prompt, Copilot, and Gemini/Antigravity installation behavior is intentionally
not preserved in this reusable baseline. Copilot can read project-local skill
folders through editor configuration. Gemini support can be reintroduced later
only through a concrete reviewed request.

GitHub Copilot custom agents are owned by the separate
`adapters/github-copilot` adapter. VS Code user-level installation uses
`~/.copilot/agents`.

Backups are rollback evidence. They do not authorize replacing unknown user
content.
