# architect-profile

Canonical operator configuration for successor ChatGPT Architects.

This repository answers one question:

> How should an Architect work with this operator?

It does not own generic agent governance or target-product truth.

## Ownership

```text
architect-profile
→ durable operator configuration and working preferences

ARCHITECT_CALIBRATION.md
→ compact operator-specific, cross-target, experience-derived judgment

agent-skills
→ generic work governance and task/execution semantics

agent-standards
→ generic engineering and evidence semantics

agent-documents
→ documentation structure and closure semantics

agent-runtime
→ optional local execution capability

target repository
→ product truth and exact task authority
```

If two sources appear to own the same rule, keep the rule with the narrowest canonical owner instead of copying it here.

## Selective bootstrap

A fresh Architect should load only the context required for the current decision:

```text
1. Read this README and ARCHITECT_PROFILE.md from current canonical GitHub main.
2. Bind the exact target repository and refresh its canonical truth.
3. Load only the canonical owner or pinned skill material required by the current task or judgment.
4. Read ARCHITECT_CALIBRATION.md only when operator-specific learned judgment can materially change that judgment.
5. Expand context only when required evidence is missing, stale, contradictory, or explicitly requested.
```

Do not preload every `agent-*` repository, all calibration, raw chat history, historical tasks, or broad repository context by default. Selective loading reduces context without hiding authority that is required for the current decision.

Successor continuity must remain reconstructible from canonical repositories without hidden chat history.

## Maintenance

- Keep this repository small and operator-specific.
- Prefer delete → merge → simplify → rewrite.
- Modify the existing canonical owner instead of creating profile shards, registries, loaders, manifests, context managers, or another framework.
- Keep generic governance with `agent-skills` and target-specific truth with the target repository.
- Preserve historical `.agent` task, report, and review evidence.
- Never store secrets, credentials, tokens, private environment values, or sensitive personal data.
- GitHub `main` is the canonical truth for this repository.

## License

Licensed under the [Apache License 2.0](LICENSE).
