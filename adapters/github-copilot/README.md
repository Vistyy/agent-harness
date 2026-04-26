# GitHub Copilot Adapter

Reusable Copilot custom agent profiles.

VS Code discovers workspace agents from `.github/agents` and user-level agents
from `~/.copilot/agents` or VS Code profile user data. This adapter installs
the reusable harness agents at user scope so projects do not need local copies.

GitHub.com cloud agent repository/organization discovery is separate: repository
agents live in `.github/agents`, and organization/enterprise agents live in
`/agents` in a `.github-private` repository.

