---
name: architect-bootstrap
description: Use at the start of Architect work, when switching into repository-governance work, or whenever canonical Architect authority must be refreshed. Loads the operator profile and generic Architect governance from canonical GitHub, proves exact identities, and fails closed instead of relying on stale Project Sources, uploads, memory, or prompt claims.
---

# Architect Bootstrap

Bootstrap only. This skill does not replace the operator profile, generic Architect governance, target-repository authority, task authority, or runtime documentation.

## Canonical sources

Before repository-specific Architect planning, review, task creation, continuation, or mutation, read these sources through the authenticated GitHub connector:

1. `phatnguyen03022001/architect-profile`
   - branch: `main`
   - file: `ARCHITECT_PROFILE.md`
2. `phatnguyen03022001/agent-skills`
   - branch: `main`
   - file: `architect/SKILL.md`

Do not substitute web search, Project Sources, uploaded copies, local checkout contents, memory, previous chat text, or a prompt that merely names these files.

## Required bootstrap evidence

For each canonical source, obtain and retain:

- repository;
- branch;
- exact branch commit SHA;
- exact file/blob SHA;
- actual file content from that GitHub identity.

Do not claim that Architect authority was loaded unless both canonical reads succeeded.

After successful bootstrap, report one compact evidence block:

```text
ARCHITECT_BOOTSTRAP: READY
profile: phatnguyen03022001/architect-profile@<commit> ARCHITECT_PROFILE.md#<blob>
governance: phatnguyen03022001/agent-skills@<commit> architect/SKILL.md#<blob>
target: <owner/repo | UNBOUND>
```

Do not hard-code commit or blob SHAs in this skill; always resolve current GitHub `main` at bootstrap time.

## Failure behavior

If authenticated GitHub cannot read either canonical source, return:

```text
ARCHITECT_BOOTSTRAP: BLOCKED
reason: CANONICAL_GITHUB_AUTHORITY_UNAVAILABLE
```

Then do not claim to be bootstrapped and do not perform repository-specific mutation based on stale substitutes.

A missing or unavailable local tunnel, `agent-runtime`, Codex, terminal, or other execution surface does not block bootstrap because GitHub is the canonical source for these authorities.

## Target binding

After canonical bootstrap:

- if the operator already supplied an exact `owner/repo`, bind it directly; do not ask for redundant confirmation;
- otherwise ask for the exact target only when repository-specific work actually requires one;
- refresh current GitHub repository and branch truth before repository-specific mutation;
- one Architect conversation may switch target repositories sequentially; repository switching alone does not require a new Architect conversation;
- discard repository-specific assumptions from the prior target when rebinding.

## Local execution boundary

Do not probe or require local execution by ceremony.

Use `agent-runtime` or another local surface only when the current phase materially benefits from or requires native/local evidence. If local capability is unavailable and local evidence is optional, continue with GitHub-capable work. If local evidence becomes mandatory, block only that phase until an authorized local surface is available.

## Precedence

Use this order:

```text
explicit current user authority
→ canonical target-repository truth / exact task-handoff authority
→ canonical operator profile
→ canonical generic Architect governance
→ optional execution methodology and tools
```

This skill is only the loader and proof mechanism. If its wording conflicts with freshly loaded canonical authority, the freshly loaded canonical authority wins.
