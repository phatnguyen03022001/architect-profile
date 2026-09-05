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

The machine-readable entrypoint is [`.agent/bootstrap/bootstrap.json`](.agent/bootstrap/bootstrap.json). Start from one exact `architect-profile` commit `P`; that commit is the authority-set identity and is not self-pinned inside the authority lock.

A fresh Architect should resolve only the context required for the current decision:

```text
1. Resolve the exact architect-profile commit P from accepted repository authority or an explicit handoff.
2. Read .agent/bootstrap/bootstrap.json at P, then its exact authority lock.
3. Bind the target only from the explicit current request or an exact active binding, then fresh-resolve that repository on GitHub; never infer it from stale chat history, memory, `cwd`, or a local directory name. If no exact target is available, ask the operator.
4. Resolve the bootstrap-known Case Router from its canonical path at the exact locked agent-skills SHA before ordinary capability selection. BOOTSTRAP is pre-router, not a CASE.
5. Select only the admitted `EXECUTE` CASE, which routes to `executor`, then use the existing capability route for its locked owner/path entrypoint. Missing/unresolvable/malformed router inputs and unknown cases fail closed with no mutable-ref fallback.
6. Load ARCHITECT_PROFILE.md and, only when materially relevant, ARCHITECT_CALIBRATION.md.
7. Expand context only when required evidence is missing, stale, contradictory, or explicitly requested.
```

The bootstrap files are static locators and validation inputs, not a registry, daemon, cache, execution engine, or duplicated copy of support-repository semantics. Do not preload every `agent-*` repository, all calibration, raw chat history, historical tasks, or broad repository context by default.

After an authority set is accepted and promoted, `main` is the stable activation ref. `dev` is the integration/evolution ref. `DEV_MAIN` is the default for newly bootstrapped repositories; an existing repository may explicitly remain `MAIN_ONLY` when its own authority says so. A future rollback is another forward activation commit, never a requirement to force-move `main` backward.

`MANAGED_MIRROR` means GitHub wins for tracked repository state at idle and successful task boundaries. Local reset/reclone reconciliation is allowed only when it cannot discard operator-owned edits; the policy does not authorize a sync daemon, background service, or destructive workspace sweep.

Successor continuity must remain reconstructible from canonical repositories without hidden chat history.

The optional [closure PROGRAM](.agent/program.generated.json) is navigation only; canonical owner task and review artifacts decide each predicate.

## Maintenance

- Keep this repository small and operator-specific.
- Prefer delete → merge → simplify → rewrite.
- Modify the existing canonical owner instead of creating profile shards, registries, loaders, manifests, context managers, or another framework.
- Keep generic governance with `agent-skills` and target-specific truth with the target repository.
- Preserve historical `.agent` task, report, and review evidence.
- Never store secrets, credentials, tokens, private environment values, or sensitive personal data.
- GitHub is canonical repository truth. The explicit repository contract is `DEV_MAIN`: working/evolution ref `dev`, stable ref `main`, local policy `MANAGED_MIRROR`.

## License

Licensed under the [Apache License 2.0](LICENSE).
