# User Apps Text Constraints Convention

Owner for end-user text length, validation, overflow, truncation, and inline
highlight posture in web and mobile applications.

- This file is norm for text-constraint and overflow behavior.
- Copy-source ownership lives in
  the project end-user copy governance reference.
- Parity timing lives in the project delivery policy.
- Atomic extraction lives in `atomic-design.md`.

## Scope

Covers:

- editable text fields,
- persisted user-authored labels and names,
- read-only text surfaces that can overflow or truncate,
- validation timing for deterministic text constraints.

## Core Rule

No ad hoc text behavior per surface.

Every user-visible text constraint needs three decisions:

- hard domain limit,
- frontend editing and validation behavior,
- read-only overflow behavior.

If one is missing, feature is under-specified.

## Max-Length Ownership

For every persisted or domain-significant field:

- hard max lives in domain or API contract,
- frontend mirrors limit proactively,
- web and mobile use same hard limit unless explicit divergence is recorded.

Not allowed:

- backend rejects at `N` while client accepts unlimited input until submit,
- one client uses different limit without explicit decision,
- component-local magic number with no contract owner.

## Editing Contract

Default:

- enforce hard max during editing when control supports it cleanly,
- keep submit-time validation as backstop,
- show constraint before late server rejection or lost work.

While editing:

- do not visually truncate editable text,
- keep full editable value in field,
- single-line fields prefer horizontal scroll or equivalent caret-safe behavior,
- do not silently rewrite or normalize visible text unless field contract says
  so.

## Validation UX

Use this posture:

- prevent over-limit entry when feasible,
- if prevention is not feasible, show immediate local validation,
- preserve user text so user can shorten it,
- error text states real constraint and recovery action.

Progressive visibility:

- do not add counters everywhere,
- add counters or remaining-length affordances when limit is tight, users are
  likely to hit it, or evidence says they do hit it,
- if field is likely to hit cap in normal use, limit must be visible before
  submit.

## Read-Only Overflow Contract

Do not improvise per surface. Use explicit surface class.

Defaults:

- primary and secondary read-only user-authored or user-critical text wraps,
- truncation or clamping is dense-exception behavior only,
- dense-exception fallback is single-line truncation unless owner contract says
  otherwise,
- surface only gets dense behavior when explicitly classified dense,
- persisted user-authored and user-critical text are normative scope now,
- catalog or integration text follows this matrix provisionally until separate
  audit changes scope,
- hover-only disclosure never counts as recovery because mobile has no hover.

| Surface class | Default behavior | Dense fallback | Recovery rule |
| --- | --- | --- | --- |
| Standard read-only display surfaces | wrap fully | not applicable unless explicitly reclassified dense | none; full value already visible |
| Dense display rows | dense only when explicitly marked | single-line truncate | row or card must open, expand, or reveal full value in same flow |
| Commit-on-tap selection rows | wrap fully | single-line truncate only when explicitly dense and wrap is unacceptable | separate local pre-commit reveal or expand affordance; main row tap cannot be only recovery path |
| Compact inline controls | dense by default | single-line truncate | if text is user-critical, provide non-hover local recovery path; otherwise surrounding surface owns meaning |

Rules:

- non-interactive dense display rows do not truncate by default; if no natural
  open or expand path exists, keep wrap until local recovery exists,
- critical meaning, destructive context, and validation errors cannot hide
  behind truncation,
- multiline clamp is not default dense behavior; use only when owner surface
  contract says extra line budget is worth complexity.

## Seamless Highlighting

When inline semantic highlights appear inside editable text (`tokenized`
editors, mentions, chips-within-text, similar):

- preserve surrounding text metrics by default,
- keep same font, size, line-height, and baseline unless product contract says
  otherwise,
- background or border treatment must not make highlight feel like different
  font run unless intentional.

Goal: same text, clearer meaning. Not separate control disguised as text.

## Review Gate

UI work touching text is not complete until review can answer:

- hard length owner for each persisted or domain-significant field,
- whether frontend proactively enforces or locally validates limit,
- which read-only surface class owns display behavior,
- if surface is dense exception, why that classification is explicit and what
  local recovery path reveals full value,
- where full value is recoverable when text truncates or clamps,
- whether inline highlights preserve surrounding text metrics,
- whether web and mobile follow same text-constraint contract.

If review cannot answer these, change fails text-constraints gate.
