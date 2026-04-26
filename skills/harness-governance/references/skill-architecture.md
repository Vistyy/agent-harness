# Skill Architecture

Reusable skill guidance belongs in focused skill directories.

## Shape

- `SKILL.md` owns trigger description and workflow mechanics.
- references folders own durable supporting doctrine.
- assets folders own templates copied or consumed by the skill.
- scripts folders own helper scripts used by the skill.
- agents folders own adapter hints for agent platforms.

## Rules

- Keep project facts out of reusable skills.
- Keep skill frontmatter concise and route by description.
- Move reusable references with the owning skill instead of leaving them in a
  project documentation tree.
- Do not duplicate the same durable rule in multiple skills; link to the owner.
- Keep examples generic unless the skill is explicitly project-local.
