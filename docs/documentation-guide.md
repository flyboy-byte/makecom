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
| [`infrastructure.md`](./infrastructure.md) | What accounts/tools/stack to actually set up |
| [`risks.md`](./risks.md) *(technical/operational sections)* | What breaks in production and how it's guarded against |

## How the tiers relate

The low-level doc (`make.com review.md`) came first and is the most concrete artifact in
the packet — it's a real operating manual, not a sketch. The high-level docs were written
*around* it, extracting the strategic questions it implies but doesn't answer (will anyone
pay for this, what's the actual risk exposure, what's still undecided). Read top-down if
you're new to the idea (`business-idea.md` → `feasibility.md` → `risks.md` →
`make.com review.md` → `infrastructure.md`); read bottom-up if you already believe in the
idea and want to know what building it involves.

## Who this whole packet is actually for, concretely

Right now: a single audience — you, the founder, at two different moments. The high-level
docs are for the moment you're deciding whether to keep going or explaining the idea to
someone else for the first time. The low-level docs are for the moment you sit down to
actually configure a Make.com scenario. Nobody else has read any of this yet — which means
none of it has been pressure-tested against an outside reader. That's the gap
[`research-handoff.md`](./research-handoff.md) and real client conversations
(`feasibility.md`) are meant to close.

If this packet later grows a second audience — a hired contractor, an investor, a
co-founder — the tiering above is what determines what they get handed: decision-makers
get the high-level set only; implementers get the low-level set plus enough of
`business-idea.md` for context.

## Adding a new doc

Before writing: decide which tier it belongs to (does it answer "should we" or "how do
we"), add it to the table above, and give it the same header block used in the existing
docs (`Tier / Audience / Use when`, one line each, at the top of the file). If a section
depends on facts nobody in this project actually knows yet (market size, legal specifics,
competitor pricing), don't invent numbers — flag it as a research-handoff candidate
instead (see next doc).
