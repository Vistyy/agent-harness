# GitHub Copilot Adapter

Reusable Copilot custom agent profile sources.

VS Code discovers workspace agents from `.github/agents` and user-level agents
from the user's Copilot agent home or VS Code profile user data. This adapter
keeps the reusable harness agent sources in one place; user-scope installation is
intentionally out of the baseline install scope.

GitHub.com cloud agent repository/organization discovery is separate: repository
agents live in `.github/agents`, and organization/enterprise agents live in
`/agents` in a `.github-private` repository.

Provider docs are maps, not doctrine owners.

- Do not name removed workflow skills.
- Do not classify blocking evidence as advisory.
- Do not copy review/runtime rules owned by skills or agent profiles.
