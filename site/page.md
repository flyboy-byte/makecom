# Page content

*Source for the single-page site. Everything else lives as Markdown in the repository.*

## The idea

Small businesses run the same processes by hand every week. Someone reads a quote request
out of an inbox and retypes it into a CRM. Someone keys supplier invoices into inventory,
line by line. Someone notices, eventually, that a call went unanswered.

All of it has the same shape: messy input going in, structured records coming out. That's
the shape automation is genuinely good at — and the shape that goes wrong quietly when
it's built carelessly, because a pipeline that silently writes bad data is worse than no
pipeline at all.

The proposal is to build these properly and charge for the build: every request verified
before it's trusted, duplicates caught, output validated against a schema, and a person
approving anything that reaches a customer or a ledger. Not an autonomous agent. A
supervised one.

**Who it's for isn't an industry.** It's any business with a workflow that runs often
enough to matter — roughly ten times a week — that starts from unstructured input and
ends in a system of record. A trade shop, a clinic's front desk, a returns queue. The
qualification is the workflow's shape, not the sector.

## What you'd sell

Three things, in order of how easily an unproven operator can sell them.

**A paid diagnostic.** Discovery as a product: map the workflow, verify it qualifies,
produce a fixed quote to build it. No build commitment. It sells before anything exists,
so it needs no track record, and it's worth something even if they never buy — most
businesses have never had the process written down.

**A fixed-price build.** One pipeline, tested, handed over, owned outright. Nothing owed
afterwards.

**Hosted operations, optional.** If you run the infrastructure, a monthly fee has
something concrete behind it. Offered as an alternative for clients who don't want to run
anything — never as a condition of the build.

Two constraints shape all of it. The retainer **cannot be mandatory**: competitors sell
one-time builds and market explicitly against lock-in. And the platform decides the offer
— on rented infrastructure "you own it" isn't quite true, because the client owns a
configuration inside a product they must keep paying for. On self-hosted infrastructure,
ownership is real and a retainer has something honest to charge for.

## The honest read

**The evidence gathered so far leans against this.** Not fatally, but it points one way,
and no document in the repository ever adds it up — so here it is.

Competitors were found selling comparable work for a fraction of the price, several with
no ongoing fee at all. The differentiator is engineering rigour, which the buyer cannot
perceive: a shop owner can judge whether it works and what it costs, not whether the
idempotency gate is correct. That puts the offer above the market on price with a quality
difference that's invisible at the point of sale. The core capability — turning
unstructured input into structured records — is exactly what the platforms and vertical
software vendors are shipping natively right now, so the window is narrowing. And one of
the three flagship workflows sits in genuinely unsettled law, with per-message statutory
damages and class-action filings up sharply.

The economics describe a job rather than a business: bespoke builds, sold one at a time,
to a segment that is slow to buy and hard to reach.

**What would change the answer** is not more analysis. It's a real conversation with
someone who actually runs a business like this — not a prospective customer, an operator.
Two are planned. Until they happen, everything here — including this paragraph — is
inference.

The part most likely to survive contact with reality is the diagnostic sold on its own.
It has no delivery risk, needs no track record, and is useful to the buyer whether or not
anything gets built.

## The documents

The full evaluation lives in the repository as Markdown — the strategic case, the
research with citations, the risk analysis, and an honest account of how it was all
assembled, including the parts that turned out to be wrong.

- [The idea in full](https://github.com/flyboy-byte/makecom/blob/main/docs/business-idea.md)
  · who it's for, and what's genuinely novel versus merely competent
- [What to sell](https://github.com/flyboy-byte/makecom/blob/main/docs/what-to-sell.md)
  · six product shapes, and why the platform choice decides most of them
- [Feasibility](https://github.com/flyboy-byte/makecom/blob/main/docs/feasibility.md)
  · competitors, pricing, build costs, and what the market already pays
- [Risks](https://github.com/flyboy-byte/makecom/blob/main/docs/risks.md)
  · including the unsettled legal question
- [Architecture](https://github.com/flyboy-byte/makecom/blob/main/docs/architecture.md)
  · the eight stages, and which of them are the same for every client
- [Where it stands](https://github.com/flyboy-byte/makecom/blob/main/FRAMEWORK.md)
  · the phase tracker, and what has to happen next
- [The method](https://github.com/flyboy-byte/makecom/blob/main/docs/method.md)
  · how the packet was built, what worked, and what was overhead
- [Research](https://github.com/flyboy-byte/makecom/tree/main/research)
  · every pass in full, unedited, with sources
- [The source manual](https://github.com/flyboy-byte/makecom/blob/main/make.com%20review.md)
  · the original document all of this came from
