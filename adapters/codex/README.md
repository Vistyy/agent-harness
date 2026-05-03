# Codex Adapter

Codex adapter files live here.

The adapter owns:

- `config.toml`: reusable Codex role registry template.
- `agents/*.toml`: role definitions.
- `install.sh`: safe individual-symlink installer for global `AGENTS.md`,
  skills, and agents.
- `assert_prompt_input_agents.py`: proof helper for fresh-process role registry
  discovery.

Live `$CODEX_HOME/config.toml` remains user-local; full apply merges the required
role registry into it with a backup. Baseline install excludes prompts,
Copilot, and Gemini homes.

## Prompt Contract

Global `AGENTS.md` is the installed Codex adapter prompt source for reusable
harness policy. Adapter install must preserve that source instead of relocating
global policy into project overlays or role files.

Provider install/config prompts are maps, not doctrine owners.

- Do not name removed workflow skills.
- Do not classify blocking evidence as advisory.
- Do not copy review/runtime rules owned by skills or role files.
