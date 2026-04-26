# Codex Adapter

Codex adapter files live here.

The adapter owns:

- `config.toml`: reusable Codex role registry template.
- `agents/*.toml`: role definitions.
- `install.sh`: safe individual-symlink installer for global `AGENTS.md`,
  skills, and agents.
- `assert_prompt_input_agents.py`: proof helper for fresh-process role registry
  discovery.

Live `~/.codex/config.toml` remains user-local; full apply merges the required
role registry into it with a backup. Baseline install excludes prompts,
Copilot, and Gemini homes.
