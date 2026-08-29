# architect-profile

Canonical operator profile for successor ChatGPT Architects.

This repository answers two related questions:

> How should the Architect work with this operator?

> What reusable architectural judgment have prior Architects learned while doing so?

It is intentionally small, operator-specific, and designed to be read before repository-specific work begins.

## System role

`architect-profile` is the operator layer in a five-repository engineering system:

```text
architect-profile
→ HOW TO WORK WITH THIS OPERATOR
→ WHAT REUSABLE OPERATOR-SPECIFIC ARCHITECTURAL JUDGMENT HAS BEEN LEARNED

agent-skills
→ HOW AGENTS GOVERN WORK

agent-standards
→ WHAT GOOD ENGINEERING LOOKS LIKE

agent-documents
→ HOW PRODUCT / DESIGN KNOWLEDGE IS STRUCTURED

agent-runtime
→ OPTIONAL BOUNDED LOCAL EXECUTION / VERIFICATION CAPABILITY
```

Actual product truth, source code, live tasks, environment-specific configuration, and deployment state remain in the target repository.

The repositories are intentionally separated by ownership. They are not one shared mutable control plane and do not require a central orchestrator.

## Entry point

A fresh Architect should read this README first, then read [`ARCHITECT_PROFILE.md`](ARCHITECT_PROFILE.md) before making operator-specific planning or execution decisions. Before material architecture, planning, or review judgment, also read [`ARCHITECT_CALIBRATION.md`](ARCHITECT_CALIBRATION.md) from the same current canonical GitHub state. Calibration need not be loaded for trivial interaction where it cannot materially affect judgment.

Typical bootstrap:

```text
architect-profile README
→ ARCHITECT_PROFILE.md
→ ARCHITECT_CALIBRATION.md when material judgment is required
→ target repository README / canonical product authority
→ applicable agent-* README
→ only the deeper canonical artifacts required by the current task
```

The goal is bounded context: understand the system map first, then load only the authority needed for the current decision.

## Ownership

[`ARCHITECT_PROFILE.md`](ARCHITECT_PROFILE.md) is the canonical owner of stable operator contract, preferences, working model, and successor-bootstrap expectations.

[`ARCHITECT_CALIBRATION.md`](ARCHITECT_CALIBRATION.md) is the canonical owner of compact, reviewed, operator-specific architectural judgment distilled from experience when that judgment is reusable across target repositories.

This repository does **not** own generic agent governance, generic engineering or evidence semantics, documentation architecture, runtime implementation, target-repository design, task history, or secrets.

## Maintenance

- Keep this repository small.
- Modify the existing canonical owner instead of adding files; `ARCHITECT_CALIBRATION.md` exists only because stable profile contract and experience-derived judgment have different semantic roles and change rates.
- Preserve stable content unless an observed material decision or execution failure proves a profile or calibration change is needed.
- Do not store passwords, tokens, `.env` values, account identifiers, or other secrets.
- Do not duplicate rules that have a canonical owner elsewhere.
- GitHub `main` is the canonical truth for this profile.
- No CI, Actions, task protocol, dev/staging workflow, or runtime machinery is needed unless a concrete future requirement proves otherwise.

## License

Licensed under the [Apache License 2.0](LICENSE).
