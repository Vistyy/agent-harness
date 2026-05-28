# Python Skill Candidate

This note records the open question of whether this overlay needs a reusable
Python practice skill.

## Candidate Owner

A new skill may be justified if it has a distinct trigger:

- changing non-trivial Python code
- reviewing Python code quality
- designing Python module boundaries
- diagnosing Python runtime/test failures where project recipes do not already
  own execution

It should not duplicate `uv`, `testing-best-practices`, `code-review`, or
project-local architecture docs.

## Useful Scope

A useful Python skill would focus on patterns agents repeatedly get wrong:

- use the repo command route first; do not bypass `just`/`uv` policy
- prefer simple functions and data structures before new classes/frameworks
- keep I/O, parsing, validation, and business decisions in clear owners
- avoid hidden global state and mutable default traps
- avoid broad exception swallowing and fake defensive fallbacks
- prefer typed boundaries where the repo already uses typing
- keep tests at the behavior boundary, not private helper seams
- use standard library parsers and structured APIs before ad hoc strings
- do not add compatibility layers, flags, or wrappers without owner and removal
  condition

## Risk

A generic Python style skill can become low-signal bloat. The better first
shape may be a `code-review` reference for Python simplicity/ownership, plus a
small Python implementation skill only if repeated implementation failures
show a distinct need.

## Current Recommendation

Do not create the Python skill immediately. First harden `code-review`
simplicity/shape and `solution-shaping` owner-boundary rules. Revisit this
candidate if Python-specific failures remain after the broader overlay gates
are fixed.
