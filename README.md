# Workflow Repair Agency — Business Idea Packet

**Start at [`FRAMEWORK.md`](./FRAMEWORK.md)** — it tracks what phase this project is
actually in and what has to happen next. This README is the doc index; `FRAMEWORK.md` is
the status tracker and the thing worth re-opening after time away.

This directory is a staged expansion of a potential business: a **Make.com-based
"Workflow Repair" service** that builds deterministic, fault-tolerant automation
pipelines for any business whose workflows pass a specific qualification test (high
volume, unstructured input, structured destination — see `docs/business-idea.md`), with
an ongoing maintenance retainer offered on top. **Updated 2026-07-23:** originally scoped
narrowly to HVAC and auto-repair trade businesses (the source manual's example
verticals); the target is now defined by the qualification test rather than by industry.
HVAC/auto-repair remain this project's researched case study — see `docs/feasibility.md`
— but are an example of the target, not its definition.

The original technical/operating manual — `make.com review.md` (and the matching PDF) —
is the source material. It already defines the operating model in detail: client
qualification, engineering standards, testing/deployment process, data governance, SLA
retainer tiers, an SOW template, and three worked automation examples. Treat that file as
the **technical spine**. The docs below are the **strategic layer** built on top of it,
written to help decide whether this is worth pursuing and how to start.

## Contents

| Doc | Tier | Purpose |
| --- | --- | --- |
| [`FRAMEWORK.md`](./FRAMEWORK.md) | Meta | Phase-gated status tracker — where this project actually is and what's next |
| [`make.com review.md`](./make.com%20review.md) | Low-level | Original technical/operating manual (source material) — architecture, SLA tiers, SOW, code walkthroughs |
| [`docs/documentation-guide.md`](./docs/documentation-guide.md) | Meta | Explains the tiers below, who each doc is for, and how they fit together |
| [`docs/business-idea.md`](./docs/business-idea.md) | High-level | The pitch: what it is, who it's for, why now, what makes it different |
| [`docs/feasibility.md`](./docs/feasibility.md) | High-level | Market demand, competition, unit economics, time-to-first-dollar |
| [`docs/architecture.md`](./docs/architecture.md) | Low-level | The vertical-agnostic technical reference architecture — what's fixed vs. pluggable per client |
| [`docs/vertical-playbook.md`](./docs/vertical-playbook.md) | Mixed | Repeatable process for screening a new vertical and onboarding a new client |
| [`docs/vertical-scenarios.md`](./docs/vertical-scenarios.md) | High-level | Three hypothetical verticals stress-testing whether the qualification-test framing actually holds |
| [`docs/infrastructure.md`](./docs/infrastructure.md) | Low-level | What you actually need to stand this up — accounts, tools, stack |
| [`docs/risks.md`](./docs/risks.md) | Mixed | Legal, technical, market, and operational risks with mitigations |
| [`docs/entrepreneur-notes.md`](./docs/entrepreneur-notes.md) | High-level | Positioning, pricing rationale, go-to-market, open questions, next steps |
| [`docs/research-handoff.md`](./docs/research-handoff.md) | Meta | Workflow for offloading unverified claims to Claude/ChatGPT deep research |
| [`research/`](./research/) | — | Intake folder for raw output from those research sessions |

## How to use this packet

Start with [`docs/documentation-guide.md`](./docs/documentation-guide.md) — it explains
the high-level/low-level split and which docs are for deciding vs. building. Short version:

1. Read `docs/business-idea.md` first for the framing.
2. Read `docs/feasibility.md` and `docs/risks.md` together — they're the go/no-go inputs.
3. `docs/infrastructure.md` is what it costs (in setup effort and dollars) to actually build
   the first client pipeline.
4. `docs/entrepreneur-notes.md` is the working scratchpad of decisions still open.
5. When a doc flags a claim as unverified, check `docs/research-handoff.md` — it's likely
   already queued for a Claude/ChatGPT deep-research pass, with a ready-to-use prompt.

Everything here is inferred from the single source document plus general reasoning about
the automation-agency space — it has not been validated against real client conversations,
pricing tests, or a working prototype. Treat conclusions as hypotheses to test, not facts.
