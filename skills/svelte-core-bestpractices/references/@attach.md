## `{@attach ...}`

Attachments are reactive DOM hooks for elements/components.

They run when element mounts, and rerun when reactive state read by attachment
changes. They may return cleanup function.

Available in Svelte `5.29+`.

Basic shape:

```svelte
<div {@attach myAttachment}>...</div>
```

## Core Rules

- attachment may return cleanup
- one element may have many attachments
- falsy value means no attachment
- attachments are reactive, unlike old actions

## Attachment Factories

Common pattern: function returns attachment.

Good fit:

- tooltip setup
- library integration
- element-local imperative wiring

Remember:

- `tooltip(content)` runs inside effect
- if `content` changes, attachment tears down and rebuilds

If setup work is expensive and rebuild is bad, move changing data into child
effect inside attachment instead of factory arguments.

## Inline Attachments

Inline attachment is fine for small local imperative setup.

Useful when:

- setup belongs to one element only
- nested `$effect` handles reactive updates after one-time mount work

## Conditional Attachments

Use falsy guard:

```svelte
<div {@attach enabled && myAttachment}>...</div>
```

## Passing Through Components

When used on component, attachment becomes symbol-keyed prop.
If component spreads props onto underlying element, attachment reaches element.

Good fit for wrapper components that should still allow DOM augmentation.

## Controlling Re-Runs

Default rule:

- `{@attach foo(bar)}` reruns when `foo` changes
- it also reruns when `bar` changes
- it also reruns when reactive state read inside `foo` changes

If that is too expensive:

- keep expensive setup inside attachment outer body
- move changing values into nested `$effect`
- pass getter function instead of raw value when needed

## Programmatic Use

Use `createAttachmentKey` to add attachments to object that will later be
spread onto element/component.

## Action Migration

If library still exposes actions only, use `fromAction` to adapt them into
attachments.

Prefer attachments for new Svelte `5` code.
