# architect-profile

Canonical operator profile for successor ChatGPT Architects.

This repository answers one question:

> How should the Architect work with this operator?

It is intentionally small and operator-specific.

## Ownership

- `ARCHITECT_PROFILE.md` — canonical operator environment, priorities, execution preferences, cost/usage guardrails, and Architect handoff presentation preferences.

This repository does **not** own generic agent governance, engineering standards, documentation architecture, runtime implementation, target-repository design, task history, or secrets.

Canonical split:

```text
architect-profile
→ HOW TO WORK WITH THIS OPERATOR

agent-skills
→ HOW AGENTS GOVERN WORK

agent-standards
→ WHAT GOOD ENGINEERING LOOKS LIKE

agent-documents
→ HOW PRODUCT/DESIGN KNOWLEDGE IS STRUCTURED

agent-runtime
→ HOW EXECUTION / LOCAL VERIFICATION WORKS
```

## Rules

- Keep this repository small.
- Prefer modifying `ARCHITECT_PROFILE.md` over adding files.
- Do not store passwords, tokens, `.env` values, account identifiers, or other secrets.
- Do not duplicate rules that have a canonical owner elsewhere.
- GitHub `main` is the canonical truth for this profile.
- No CI, Actions, task protocol, dev/staging workflow, or runtime machinery is needed unless a concrete future requirement proves otherwise.
