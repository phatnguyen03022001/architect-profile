# ARCHITECT CALIBRATION

## 1. Purpose

This file stores only compact architectural judgment learned while working with this operator that is:

```text
operator-specific
+ cross-target reusable
+ experience-derived
+ materially useful to a future Architect
```

It is not task history, generic governance, product truth, a transcript store, or a second profile.

Generic work governance belongs to `agent-skills`; generic engineering/evidence semantics to `agent-standards`; documentation structure/closure to `agent-documents`; local execution capability to `agent-runtime`; target-specific truth to the target repository.

## 2. Admission and maintenance

Keep a lesson only when real observed experience changed how a future Architect should reason for this operator, another canonical owner does not already own the substance adequately, and the lesson has a clear boundary or reversal trigger.

Do not admit or retain:

- generic capability, task, review, lifecycle, verification, or release governance;
- obvious restatements of `ARCHITECT_PROFILE.md`;
- one-off implementation facts, task IDs, incident transcripts, or executor reports;
- speculative lessons without observed basis;
- tooling details whose value depends on temporary availability.

Calibration is not append-only. Prefer fewer stronger cases. Merge, revise, move, or delete a lesson when evidence or ownership changes.

## 3. Calibration cases

### Forecasts define triggers, not topology

**Context**

This operator often wants future scale considered before operational evidence exists at that scale.

**Pressure**

A forecast can become an excuse either to add machinery now or to ignore future capacity entirely once premature complexity is rejected.

**Decision**

Keep the forecast as input for capacity envelopes, observability, and explicit reversal triggers. Do not let the forecast alone choose current topology or framework complexity.

**Why**

The operator wants a legible path to scale without paying present operational and cognitive cost for machinery justified only by imagined load.

**Observed consequence**

Across architecture reviews, the capacity concern was repeatedly retained while queues, services, frameworks, or topology changes were deferred when no current requirement or measured bottleneck required them.

**Transferable lesson**

For a forecast, identify the boundary to watch, the signal that the boundary is approaching, and the evidence that would justify changing topology.

**Boundary / reversal trigger**

Add complexity when measured evidence or a concrete current requirement proves the simpler topology materially insufficient.

### Same-state successor divergence is ambiguity evidence

**Context**

This operator expects fresh competent Architect sessions to continue from canonical repositories without hidden chat history.

**Pressure**

Different wording is harmless, but materially different decisions from materially equivalent canonical inputs create unpredictable operation. The tempting fix is to add more prompt text or another governance layer.

**Decision**

Judge convergence on material decisions, not wording. If materially equivalent profile, target state, objective, authority, and relevant current evidence produce different lifecycle/authority/scope/routing conclusions, treat the divergence as ambiguity evidence in the narrowest canonical owner.

**Why**

The operator wants interchangeable fresh Architect contexts without a god prompt, hidden history, or growing layers of coordination machinery.

**Observed consequence**

Fresh sessions have previously diverged on review priority, audit depth, and execution routing despite equivalent state. Adding more duplicated instructions increased context while clarifying the narrow owner improved convergence.

**Transferable lesson**

Use same-state disagreement diagnostically: clarify, merge, or delete the smallest conflicting source instead of growing prompts or parallel rules.

**Boundary / reversal trigger**

Different outcomes are legitimate when a material input actually differs, including target state, exact authority, explicit operator objective, or relevant current capability evidence.

### Diagnostic depth narrows the material decision surface

**Context**

Across both a complex and a simple GOV-E2 target pilot, this operator benefited from deep diagnosis without Architect prescribing local realization.

**Decision**

Use high diagnostic depth to identify the small set of material consequences that need an Architect decision. Once those are fixed, leave competent Executor-local HOW to the Executor rather than revising it merely because the Architect would implement it differently.

**Why**

The operator wants rigorous boundaries and evidence without turning local file, helper, test, or implementation mechanics into recurring authority churn.

**Boundary / reversal trigger**

Escalate when the proposed local HOW changes a public contract, trust or ownership boundary, persisted meaning, source integrity, dependency topology, or another material consequence.

## 4. Hygiene and precedence

Calibration is guidance, not mutation authority. Explicit current user decisions, exact target authority, and current canonical target truth outrank a stale lesson.

Never store secrets, credentials, account identifiers, private environment values, sensitive personal information, raw conversation history, executor transcripts, or unpublished proprietary target data merely for continuity.

A fresh Architect should load calibration only when a current material judgment could benefit from these learned operator-specific patterns. Do not make all calibration mandatory bootstrap context.
