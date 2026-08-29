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
