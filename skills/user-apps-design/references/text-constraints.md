# Text Constraints

Owner for end-user text length, validation, overflow, truncation, and inline
highlight posture.

## Rule

No ad hoc text behavior per surface.

Every user-visible text constraint needs:

- hard domain or API limit
- frontend editing and validation behavior
- read-only overflow behavior

If one is missing, the feature is under-specified.

## Editing

Persisted or domain-significant fields keep one hard limit across clients unless
explicit divergence is recorded. Frontends mirror the limit proactively and keep
submit-time validation as backstop.

While editing:

- do not visually truncate editable text
- preserve the full value so the user can shorten it
- show the constraint before late server rejection or lost work
- prevent over-limit entry when clean; otherwise show immediate local validation
- do not silently rewrite visible text unless the field contract says so

Counters are required only when the limit is tight or normally reachable.

## Read-Only Overflow

Default user-authored or user-critical text wraps fully.

Truncation is a dense-surface exception. When text truncates or clamps, the same
flow must provide non-hover recovery for the full value. Hover-only recovery is
invalid because mobile has no hover.

Critical meaning, destructive context, and validation errors cannot hide behind
truncation.

## Inline Highlights

Token highlights, mentions, and chips inside text preserve surrounding font,
size, line height, baseline, and editing metrics unless the product contract
requires a different run.

Goal: same text, clearer meaning.

## Review

Text work is complete only when review can name the hard limit owner, editing
behavior, overflow class, truncation recovery path, and client parity decision.
