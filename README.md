# architect-profile

Canonical operator profile for successor ChatGPT Architects.

This repository answers one question:

> How should the Architect work with this operator?

It is intentionally small, operator-specific, and designed to be read before repository-specific work begins.

## System role

`architect-profile` is the operator layer in a five-repository engineering system:

```text
architect-profile
→ HOW TO WORK WITH THIS OPERATOR

agent-skills
→ HOW AGENTS GOVERN WORK

agent-standards
→ WHAT GOOD ENGINEERING LOOKS LIKE

agent-documents
→ HOW PRODUCT / DESIGN KNOWLEDGE IS STRUCTURED

agent-runtime
→ HOW OPTIONAL LOCAL EXECUTION / VERIFICATION WORKS
```

Actual product truth, source code, live tasks, environment-specific configuration, and deployment state remain in the target repository.

The repositories are intentionally separated by ownership. They are not one shared mutable control plane and do not require a central orchestrator.

## Entry point

A fresh Architect should read this README first, then read [`ARCHITECT_PROFILE.md`](ARCHITECT_PROFILE.md) before making operator-specific planning or execution decisions.

Typical bootstrap:

```text
architect-profile README
→ ARCHITECT_PROFILE.md
→ target repository README / canonical product authority
→ applicable agent-* README
→ only the deeper canonical artifacts required by the current task
```

The goal is bounded context: understand the system map first, then load only the authority needed for the current decision.

## Ownership

[`ARCHITECT_PROFILE.md`](ARCHITECT_PROFILE.md) is the canonical owner of:

- operator environment and durable working preferences;
- Architect / Executor interaction preferences;
- execution-surface preferences;
- cost, quota, and human-attention guardrails;
- task-launch and handoff presentation preferences;
- successor-Architect continuity expectations.

This repository does **not** own generic agent governance, engineering standards, documentation architecture, runtime implementation, target-repository design, task history, or secrets.

## Maintenance

- Keep this repository small.
- Prefer modifying `ARCHITECT_PROFILE.md` over adding files.
- Preserve stable content unless an observed material decision or execution failure proves a profile change is needed.
- Do not store passwords, tokens, `.env` values, account identifiers, or other secrets.
- Do not duplicate rules that have a canonical owner elsewhere.
- GitHub `main` is the canonical truth for this profile.
- No CI, Actions, task protocol, dev/staging workflow, or runtime machinery is needed unless a concrete future requirement proves otherwise.

## License

Licensed under the [Apache License 2.0](LICENSE).
