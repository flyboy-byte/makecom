# Documentation Guide

> **Tier:** Meta (about the docs themselves) · **Audience:** anyone new to this packet,
> including future-you after time away · **Use when:** you don't know which doc to open,
> or you're adding a new doc and need to decide where it fits.

This packet has two altitudes. Knowing which altitude you're reading (or writing) at
prevents the two failure modes that hit business-idea docs specifically: pitch decks that
are all vision and no way to actually build the thing, and build docs that bury the "is
this worth doing" question under implementation detail.

## The two tiers

### High-level — the decision layer

**Question it answers:** *Should this exist, and is it worth pursuing?*
**Written for:** the founder making the go/no-go call, or anyone being pitched the idea
cold (co-founder, advisor, investor).
**Properties:** short enough to read in one sitting, states conclusions and open
questions plainly, doesn't require Make.com/webhook/API literacy to follow.

| Doc | What it's for |
| --- | --- |
| [`business-idea.md`](./business-idea.md) | The pitch — what it is, who it's for, why now |
| [`feasibility.md`](./feasibility.md) | Is this worth pursuing — demand, cost, validation plan |
| [`entrepreneur-notes.md`](./entrepreneur-notes.md) | Live scratchpad of open decisions |
| [`expansion.md`](./expansion.md) | Who this gets shown to first, and the plan for it — not yet executed |
| [`vertical-scenarios.md`](./vertical-scenarios.md) | Stress-tests whether the qualification-test framing holds outside HVAC/auto-repair |
| [`risks.md`](./risks.md) *(legal/market sections)* | What could kill this and why |

### Low-level — the build layer

**Question it answers:** *Given we're doing this, how does it actually get built and run?*
**Written for:** whoever is implementing (you-as-engineer, or a hired contractor).
Assumes the high-level case has already been read — doesn't re-argue the pitch.
**Properties:** specific enough to act on directly — account names, module sequences,
config flags, response-time numbers.

| Doc | What it's for |
| --- | --- |
| [`../make.com review.md`](../make.com%20review.md) | The technical/operating spine — architecture, SLA tiers, SOW template, worked examples |
| [`architecture.md`](./architecture.md) | The vertical-agnostic reference architecture — what's fixed vs. pluggable per client |
| [`infrastructure.md`](./infrastructure.md) | What accounts/tools/stack to actually set up |
| [`risks.md`](./risks.md) *(technical/operational sections)* | What breaks in production and how it's guarded against |

### Mixed — process docs that bridge both altitudes

| Doc | What it's for |
| --- | --- |
| [`vertical-playbook.md`](./vertical-playbook.md) | Screening a new vertical (high-level judgment call) and onboarding a new client (low-level structured intake) in one repeatable process |

### Meta — about the packet rather than the business

| Doc | What it's for |
| --- | --- |
| [`../FRAMEWORK.md`](../FRAMEWORK.md) | The phase tracker — what's genuinely done versus merely written |
| [`method.md`](./method.md) | How the packet was built, what worked, what was overhead, and the reusable form the process was extracted into |
| [`research-handoff.md`](./research-handoff.md) | How unverifiable claims get handed to an external research engine |
| this file | The tier system itself |

## How the tiers relate

The low-level source manual (`make.com review.md`) came first and is the most concrete
artifact in the packet — a real operating manual, not a sketch. The high-level docs were
written *around* it, extracting the strategic questions it implies but doesn't answer
(will anyone pay for this, what's the actual risk exposure, what's still undecided). The
remaining docs came later, when the packet's own claims needed backing:
[`architecture.md`](./architecture.md) after the target market was redefined and the
technical model had to be shown to actually generalise, and
[`vertical-playbook.md`](./vertical-playbook.md) plus
[`vertical-scenarios.md`](./vertical-scenarios.md) to make that claim testable rather
than asserted.

Two reading orders work. Top-down if the idea is new to you: `business-idea.md` →
`feasibility.md` → `risks.md` → `architecture.md`. Bottom-up if you already accept the
premise and want to know what building it involves: `make.com review.md` →
`architecture.md` → `infrastructure.md`.

## Who this packet is actually for, concretely

**This changed, and the change matters.** For most of its life this packet had exactly
one reader — the founder, at two different moments: deciding whether to keep going, and
sitting down to actually configure a scenario. The tiering exists because those two
moments want completely different documents.

It is now a public repository with a published site, so the audience is open-ended: anyone
reading it as a worked example of the method, anyone evaluating the idea itself, anyone
who found it by accident. That doesn't change the tiering — if anything it makes it more
load-bearing, since a stranger has no context to compensate with — but it does mean the
"nobody has read this yet" caveat that used to sit here is no longer true, and claims in
these docs should be written as though a skeptical outsider will check them. Several
already have been checked, and [`method.md`](./method.md) records where that went badly.

What has *not* changed: none of it has been pressure-tested against a prospective
**customer**. That gap is what [`../FRAMEWORK.md`](../FRAMEWORK.md)'s Phase 2 exists to
close, and no amount of readers substitutes for it.

## Adding a new doc

Before writing: decide which tier it belongs to (does it answer "should we" or "how do
we"), add it to the table above, and give it the same header block used in the existing
docs (`Tier / Audience / Use when`, one line each, at the top of the file). If a section
depends on facts nobody in this project actually knows yet (market size, legal specifics,
competitor pricing), don't invent numbers — flag it as a research-handoff candidate
instead (see next doc).
