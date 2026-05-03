# Codex Install Scope

The baseline Codex adapter installs only individual symlinks:

- `$CODEX_HOME/AGENTS.md` -> `AGENTS.md`
- `$CODEX_HOME/skills/<skill-name>` -> `skills/<skill-name>`
- `$CODEX_HOME/agents/<agent-name>.toml` -> `adapters/codex/agents/<agent-name>.toml`

It never replaces whole directories.

Full install prunes stale harness-owned symlinks directly under
`$CODEX_HOME/skills` and `$CODEX_HOME/agents` when the link target is inside
this harness repo and the basename is outside the current planned install set.
It does not prune during `--stage-harness-governance`.

Pruning never removes regular files, directories, `.system`, or symlinks that
point outside this harness repo. Pruned symlinks are recorded in the backup
manifest.

`AGENTS.md` is the installed adapter prompt source for reusable harness policy.
Do not move global policy only into a project-local overlay or role file.

Full apply also merges the required Codex role config into
`$CODEX_HOME/config.toml` after backing up the live file. It does not symlink or
wholesale replace live config.

## Excluded Surfaces

Baseline install must not mutate:

- `$CODEX_HOME/prompts`
- the user's Copilot home
- the user's Gemini home

Prompt, Copilot, and Gemini/Antigravity installation behavior is intentionally
not preserved in this reusable baseline. Copilot can read project-local skill
folders through editor configuration. Gemini support can be reintroduced later
only through a concrete reviewed request.

GitHub Copilot custom agent sources live under `adapters/github-copilot/agents/`.
They are source assets only; this baseline keeps Copilot-home mutation out
of scope.

Backups are rollback evidence. They do not authorize replacing unknown user
content.
