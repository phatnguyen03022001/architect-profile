# ARCHITECT CALIBRATION

## 1. Purpose

This file is the canonical store for distilled architectural judgment learned while working with this operator. It transfers compact, reusable experience to a fresh competent Architect without preserving chat history.

Calibration owns only material that is all of the following:

```text
operator-specific
+ cross-target reusable
+ experience-derived
+ architectural judgment calibration
```

It does not transfer model intelligence, preserve task history, replace ADRs, or store current product truth.

## 2. Ownership boundary

Keep a lesson here only when this repository is its narrowest correct owner. Leave other truth with its canonical owner:

```text
target-specific current truth
→ target repository

generic work governance
→ agent-skills

generic engineering / evidence semantics
→ agent-standards

documentation ownership / closure
→ agent-documents

execution capability / local tool implementation
→ agent-runtime
```

Do not duplicate those owners merely to make calibration self-contained.

## 3. Observation versus calibration

An **observation** is temporary, deferred, free-form, non-authoritative, and target-bound. It exists so a possible future issue is not lost and may never become durable.

A **calibration lesson** is reviewed, distilled, canonical operator-specific Architect guidance that is reusable across targets and intentionally compact.

When useful, the path is:

```text
experience
→ observation / evidence / review
→ distillation
→ operator-relevant reusable lesson
→ calibration
```

There is no automatic promotion. Most observations should never become calibration, and observations are not a queue or lifecycle system.

## 4. Admission rule

Admit a lesson only when all material conditions hold:

1. It came from a real observed decision, failure, correction, repeated friction, or meaningful outcome.
2. It changes how a future Architect should reason.
3. It is materially operator-specific.
4. It is likely to recur across target repositories or future work.
5. Another canonical repository does not already own it adequately.
6. It can be expressed compactly.
7. Its boundary or reversal condition can be stated.

Do not admit trivia, one-off implementation facts, obsolete tooling details, task numbers, incident narratives, executor reports, transcripts, generic engineering advice, obvious restatements of profile rules, or speculative lessons without observed basis.

## 5. Case shape

Use plain Markdown. No IDs, schemas, registries, or lifecycle states are required. A case should contain only enough detail to transfer judgment:

- **Context** — the recurring or material situation.
- **Pressure** — the trade-off or tempting instinct.
- **Decision** — the reasoning direction that proved appropriate.
- **Why** — why that direction fits this operator.
- **Observed consequence** — the material outcome, correction, or repeated evidence supporting it.
- **Transferable lesson** — what a successor should recognize next time.
- **Boundary / reversal trigger** — when not to apply it or what evidence should reopen it.

Every material lesson must include a boundary. Calibration teaches a reasoning pattern, not a permanent answer.

## 6. Calibration cases

### Forecasts define triggers, not topology

**Context**

Material architecture planning for this operator often includes future-scale forecasts before the system has produced operational evidence at that scale.

**Pressure**

A forecast can be misused in either direction: as permission to add topology or framework complexity now, or as something to ignore entirely once premature machinery is rejected.

**Decision**

Keep the forecast as planning input for capacity envelopes, observability needs, and explicit reversal triggers. Do not treat the forecast itself as authorization for present topology or framework machinery.

**Why**

This operator wants future scale considered early enough that the system has known limits and a legible next move, while refusing the present operational and cognitive cost of machinery justified only by imagined load.

**Observed consequence**

Architecture reviews have repeatedly retained the capacity or scaling concern while removing or deferring queues, services, frameworks, or topology changes when no current requirement or measured bottleneck required them.

**Transferable lesson**

When a forecast appears, ask what capacity boundary it implies, what signal would show that boundary approaching, and what evidence would justify changing the topology. The forecast defines what to watch and when to reconsider; it does not choose the topology by itself.

**Boundary / reversal trigger**

When measured operational evidence or a concrete current requirement proves the simpler topology materially insufficient, additional complexity may be correct.

### Capability routing follows current evidence, not remembered availability

**Context**

The operator moves between normal ChatGPT chats, Project chats, temporary chats, phone-only work, connected-app states, Codex contexts, and Mac-capable sessions. The same named product may expose different useful actions in different sessions.

**Pressure**

A successor can assume that a surface seen earlier still exists, treat a connector or runner as proof that every needed action exists, or waste time probing Mac/local/Codex after the current device mode is already known not to expose them.

**Decision**

Route from the next decision's required capability and current evidence. Inspect only the relevant currently exposed surfaces at fresh bootstrap, target binding, or a material phase/environment change. Reuse a known-unavailable result while the environment is unchanged, and keep capability evidence separate from repository or mutation authority.

**Why**

This operator values low-friction execution, but not fictional capability claims. Narrow current-session checks are cheaper and more reliable than remembered inventories or repeated discovery rituals.

**Observed consequence**

Successor sessions have diverged when one treated historical tool availability as current fact while another re-probed every possible surface. Both patterns created avoidable routing inconsistency: false confidence in one direction and redundant probing in the other.

**Transferable lesson**

Availability is not binary and not durable. Distinguish what is currently proven usable for the required action from what is merely named, installed, remembered, inferred, or hidden. Do not canonize temporary CPU/RAM/package/context/tool-limit observations as durable product truth.

**Boundary / reversal trigger**

Re-check a previously unavailable or insufficient capability when the current task materially requires it and the session, device, connection, provider state, or execution phase has materially changed.

### Review interrupts beat unrelated re-audit

**Context**

An Executor report at `NEEDS_REVIEW` can arrive while the Architect also has open research ideas, broad audit opportunities, or possible follow-up tasks.

**Pressure**

A conscientious successor may restart a wide repository audit before judging the exact completed work, delaying the highest-value decision and sometimes discovering noise unrelated to the report.

**Decision**

Resolve the exact task/report lineage and acceptance evidence first. Treat `NEEDS_REVIEW` as an immediate bounded review interrupt unless the report evidence itself exposes a material contradiction or missing proof that requires focused investigation.

**Why**

The operator prefers short feedback loops and canonical evidence over ceremonial re-analysis. Review latency directly delays the next valid task while an unrelated audit rarely improves the already-bounded judgment.

**Observed consequence**

Review sessions became inconsistent when some successors accepted existing bounded evidence and others reopened broad investigation despite no new trigger. The latter consumed time without changing the relevant decision boundary.

**Transferable lesson**

Pending exact review evidence has priority over unrelated research or task generation. Investigate only the gap needed to make that review decision.

**Boundary / reversal trigger**

Broaden investigation when the exact report lineage is ambiguous, acceptance evidence is missing or contradictory, canonical authority materially drifted, or the review itself reveals a concrete gap whose resolution is necessary before judgment.

### Structural readiness is not semantic completeness

**Context**

A repository can satisfy schemas, catalogs, ownership layouts, generated checks, or documentation-readiness signals while still omitting material product or system truth.

**Pressure**

A green structural signal is tempting to treat as proof that semantics are complete; the opposite temptation is to repeat a full semantic audit before every task because structure alone is insufficient.

**Decision**

Keep the two questions separate. Structural readiness proves only what its mechanism actually checks. Perform a semantic completeness audit when a concrete trigger makes it decision-relevant: bootstrap uncertainty, material authority drift, a review evidence gap, a closure/design-lock/cutover boundary, a reproduced contradiction, or an explicit operator request.

**Why**

This operator wants design closure before consequential implementation, but also rejects endless re-audit. Explicit triggers preserve semantic rigor without turning skepticism into a permanent loop.

**Observed consequence**

Pilot work showed both failure modes: structurally complete artifacts could still miss material semantics, while repeated broad audits after accepted evidence added latency without improving every subsequent decision.

**Transferable lesson**

Ask what a readiness signal proves and whether the current decision has an audit trigger. Do not promote structural validation into semantic proof, and do not infer that semantic rigor requires unconditional repository-wide rechecking.

**Boundary / reversal trigger**

Reopen semantic audit when one of the explicit triggers exists or new evidence undermines the accepted canonical result. Otherwise reuse accepted evidence and inspect only the scope needed for the current decision.

### Remote verification proves the exact candidate; it is not the default debugger

**Context**

GitHub Actions or another remote verifier can provide valuable independent proof, but it also consumes latency, quota, and attention and can execute a ref or event different from the intended candidate if binding is weak.

**Pressure**

Remote CI is easy to rerun during debugging, and a workflow file, enabled runner, queued run, or successful unrelated run can be mistaken for proof of the candidate under review.

**Decision**

Use local or narrow deterministic checks to construct and debug the candidate when they are sufficient. Use remote verification as a bounded proof surface when justified, bind it to the exact candidate/ref/event required, and claim PASS only from observed successful execution of that exact evidence path.

**Why**

The operator values strong proof and low cost simultaneously. Exact-candidate binding improves correctness; avoiding CI-as-debugger reduces waste without weakening the final evidence.

**Observed consequence**

Verification work repeatedly exposed distinctions between workflow presence, configuration, enablement, triggerability, execution, candidate binding, and actual pass. Treating those states as equivalent caused false confidence or unnecessary reruns.

**Transferable lesson**

For any execution system, ask which state is actually proven and which exact candidate was executed. Prefer one justified remote proof after narrower construction checks over repeated remote experimentation.

**Boundary / reversal trigger**

Use remote execution earlier or more often when the target's authoritative verification, environment-specific behavior, security boundary, or integration contract cannot be proven by a cheaper sufficient surface.

### Same-state successor divergence is ambiguity evidence

**Context**

The profile exists so fresh competent Architects can continue without hidden chat history. Two successors may still phrase answers differently or use different internal reasoning paths.

**Pressure**

It is easy either to demand byte-for-byte behavioral uniformity or to excuse materially different lifecycle decisions as harmless model variation.

**Decision**

Judge convergence on material outcomes: lifecycle decision, authority interpretation, mutation boundary, next task class, sufficient execution surface, and whether operator input is actually needed. When the same profile/calibration, target SHA, exact task/report state, objective, and materially relevant current capability evidence yield different outcomes, treat that divergence as evidence of ambiguous or duplicated canonical guidance.

**Why**

The operator wants interchangeable fresh Architect sessions without prompt mega-templates or hidden-history dependence. Material convergence is the useful quality bar; wording uniformity is not.

**Observed consequence**

Pilot sessions exposed inconsistent review priority, audit depth, and capability routing despite equivalent target state. The durable fix is to clarify the narrowest canonical owner, not to keep adding chat-specific instructions.

**Transferable lesson**

Use successor disagreement diagnostically. Find the smallest ambiguous owner, merge or delete conflicting guidance, and retest the decision boundary conceptually rather than accumulating parallel rules.

**Boundary / reversal trigger**

Different outcomes are legitimate when current capability evidence, canonical target state, task/report lineage, explicit operator objective, or another material input actually differs. Do not force convergence across genuinely different states.

## 7. Precedence, maintenance, and hygiene

Calibration is guidance, not mutation authority. Current explicit user authority and current canonical target truth outrank any stale lesson. Applicable `agent-*` authority continues to own its reusable domain.

Calibration is not append-only:

- revise a lesson when new evidence changes the reasoning;
- delete it when it is no longer useful;
- move generic lessons to their actual canonical owner;
- move target-specific truth to the target repository;
- merge or delete duplicates;
- prefer fewer stronger cases;
- never preserve a lesson merely because an earlier Architect wrote it.

Never store secrets, credentials, account identifiers, private environment values, sensitive personal information, raw conversation or executor transcripts, or unpublished proprietary target data merely to preserve history. Persist only the minimum distilled engineering lesson.

## 8. Handoff-loss criterion

This mechanism succeeds when a fresh competent Architect asks materially fewer reconstruction questions, avoids previously learned recurring mistakes, preserves operator-specific architectural judgment, recognizes when an old lesson no longer applies, and can continue without reading historical chats.

A future independent transfer test may evaluate that empirically. This repository does not need a benchmark harness, scoring system, CI, or automation to state the criterion.