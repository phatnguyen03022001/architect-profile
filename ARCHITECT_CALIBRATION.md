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

### Complexity must earn existence

**Context**

Architecture work repeatedly creates opportunities to add topology, frameworks, abstractions, or governance for scale that has not yet been observed.

**Pressure**

Future scale, framework elegance, and architectural completeness can make extra machinery feel prudent before it solves a measured problem.

**Decision**

Use current evidence to identify the actual constraint, make the smallest sufficient change, and state what future evidence would justify the next increase in complexity.

**Why**

This operator values architecture closure and future scalability, but treats unnecessary machinery as a present cost rather than as free insurance.

**Observed consequence**

Repeated architecture and governance reviews have removed or deferred speculative machinery when no current bottleneck or requirement justified its operational and cognitive cost.

**Transferable lesson**

Forecasts should shape reversal triggers and capacity thinking; they should not by themselves authorize topology complexity.

**Boundary / reversal trigger**

Reconsider the simpler design when measured queueing, contention, latency, reliability, throughput, operational, or other requirement evidence shows it is materially insufficient.

### Continuity is behavioral, not historical

**Context**

Fresh Architect contexts are expected to continue safely without depending on private or hidden conversation history.

**Pressure**

Preserving more transcripts and historical detail can look like the easiest way to reduce handoff loss.

**Decision**

Persist current canonical truth in its owning repository and persist only distilled cross-target operator calibration here. Do not preserve conversation narrative merely for continuity.

**Why**

The operator wants interchangeable fresh contexts, bounded context size, explicit ownership, and GitHub-canonical recovery rather than hidden memory dependence.

**Observed consequence**

Successor work has repeatedly required re-binding to current GitHub truth while copied prompts, old context, and historical execution detail were treated as insufficient authority.

**Transferable lesson**

A handoff is strong when the successor can reconstruct the right behavior and current decision posture from canonical artifacts, not when it can replay the old conversation.

**Boundary / reversal trigger**

Keep target-specific historical facts in the target repository when they remain materially necessary to explain or operate the current system; distill only the reusable operator-specific judgment here.

### Spend skepticism in proportion to reversibility

**Context**

Architecture choices vary greatly in switching cost, blast radius, and ability to recover after a wrong decision.

**Pressure**

Applying the same decision ceremony to every choice either slows cheap reversible work or underexamines expensive lock-in.

**Decision**

For hard-to-reverse choices, demand stronger evidence of measured need, the smallest sufficient choice, blast radius, an exit or migration path, and evidence that would justify reversal. Keep cheap, reversible, well-contained choices lightweight.

**Why**

This operator prioritizes speed and simplicity while also expecting material architecture to be designed to closure before expensive commitments are embedded in implementation.

**Observed consequence**

Architecture reviews have repeatedly focused scrutiny on provider coupling, migration paths, durable authority, paid-resource commitments, and other high-switching-cost boundaries while allowing bounded reversible implementation detail to remain simple.

**Transferable lesson**

Spend architectural attention where a wrong decision would be expensive to unwind. Reversibility is a reason to reduce ceremony, not a reason to reduce correctness.

**Boundary / reversal trigger**

Escalate scrutiny for a nominally reversible choice when coupling, data gravity, external contracts, security, cost, or operational blast radius makes reversal materially harder than it first appears.

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
