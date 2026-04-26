# Just Command Router

Harness-managed projects expose standard workflow commands through `just`.

Required recipe names:

- `just quality-fast`
- `just quality`
- `just quality-full`
- `just test`
- `just fmt`
- `just agent profile .`
- `just agent up <target> .`
- `just agent verify .`
- `just agent down <target>`
- `just agent logs <service>`

The harness owns when these commands are selected. The project owns recipe
bodies, stack aliases, runtime targets, and project-specific recipes.
