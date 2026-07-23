# The Idea

> **Tier:** High-level · **Audience:** founder/decision-maker, and anyone being pitched
> the idea (co-founder, early advisor, investor) · **Use when:** deciding whether to
> pursue this at all, or explaining the idea to someone new in under 5 minutes.
> See [`documentation-guide.md`](./documentation-guide.md) for how this fits with the
> rest of the packet.

## One-line pitch

A "Workflow Repair" service that replaces messy, manual, error-prone business processes
with deterministic, human-supervised automation pipelines built on Make.com — sold as a
one-time build, with an ongoing maintenance retainer offered as the recommended (not
required) path. **Updated 2026-07-23, in two ways:**

1. The source manual's original framing sold the retainer as mandatory; two independent
   deep-research passes found this is a real competitive liability (see Revenue model
   below) and this doc now reflects the corrected positioning.
2. **The target market is now defined by a qualification test, not by industry.** The
   source manual named HVAC and automotive repair as its example verticals, and this
   packet inherited that framing directly. On reflection, that's backwards: the thing
   that actually makes a business a good fit isn't its industry, it's whether its
   workflows pass the qualification test below. HVAC and auto repair remain useful — they're
   this project's researched case study (see `feasibility.md`, `entrepreneur-notes.md`) —
   but they're an example of the target, not the definition of it.

## Who it's for — the qualification test, not a vertical list

Any business whose workflow passes the source manual's **3-Trait Qualification Test**
(`make.com review.md` §1.3), regardless of industry:

1. **Volume** — the workflow runs at real frequency (the manual sets a bar of ≥10
   executions/week — see [`feasibility.md`](./feasibility.md) for whether that's the
   right threshold for any given vertical).
2. **Unstructured input** — the workflow currently starts from free-text emails, PDFs,
   call transcripts, or similar messy input that a person reads and interprets by hand.
3. **Structured destination** — the output needs to land in a rigid, machine-readable
   system (CRM, ERP, dispatch software, inventory, whatever the business already runs on).

A business that clears all three is a candidate, whether it's a trade shop, a dental
office, a law firm's intake process, or an e-commerce return desk. A business that fails
any one of them probably isn't a good fit yet — see "explicitly not the target" below.

**This doesn't remove the need for domain knowledge — it relocates it.** Passing the
qualification test tells you a business's workflow has the right *shape* for this kind
of automation. It tells you nothing about the actual details of that workflow, and you
can't design a real pipeline without those details. That means either you already
understand the target business's operations, or you get that understanding directly from
a real (or at minimum a carefully-considered hypothetical) customer conversation — this
packet's own research can't substitute for that, no matter how broad or narrow the
target industry is. Picking a *first* vertical to validate in should be driven by where
you actually have that access, not by which industry sounds biggest.

Explicitly **not** the target: businesses wanting an open-ended AI chatbot, or businesses
whose process hasn't been mapped/diagrammed yet — regardless of industry. The source
manual is emphatic that "vague AI executive assistant" and "fully autonomous customer
service bot" pitches are disqualifying — see the vertical mapping table in
`make.com review.md` §1.4 (worth reading as an illustration of the qualification test in
action, even though the specific verticals in that table are examples, not requirements).

## Why this framing (vs. generic "AI automation agency")

The generic version of this business (broad "we automate anything with AI") is crowded and
commoditized. This version narrows on three specific, defensible choices:

1. **Narrow workflow shape, not a narrow industry.** The qualification test above (not a
   vertical label) is what keeps this from being a vague "we automate anything with AI"
   pitch — it's specific about *what kind* of problem gets solved, while staying open
   about *which industry* has that problem. Three concrete workflow patterns from the
   source manual — inbound quote/lead intake, invoice/parts extraction, missed-call text
   follow-up (`make.com review.md` §7.1–7.3) — are worked examples of the shape, not an
   exhaustive list of what qualifies.
2. **Engineering discipline as the differentiator.** Most no-code automation shops ship
   fragile scenarios that break on the first malformed input. This model's actual product
   is reliability: webhook signature verification, idempotency keys, schema validation,
   a formal 50-run/10-failure test suite before go-live (§2–3). That's a real technical
   moat against competitors who just drag-and-drop a demo together.
3. **Human-in-the-loop as a liability firewall, not just a UX choice.** No automation
   writes live data or messages customers without a human approval step (§2.2, §4.2).
   This is simultaneously a trust-building sales point and a legal risk mitigation — see
   [`risks.md`](./risks.md).

## Revenue model

Two-part, not project-only — **revised 2026-07-23** based on two independent
deep-research passes (see `docs/entrepreneur-notes.md` and
`docs/research-handoff.md`):

- **One-time implementation fee** — target **$5,000–$8,000/pipeline** (research-backed
  range: $3,000–$18,000 depending on freelancer vs. agency delivery), reflecting the
  actual engineering scope (discovery, signature verification, idempotency, schema
  validation, HITL gate, formal test suite) rather than "simple Zapier automation"
  pricing. This is a real, higher-than-original number: the source manual's SOW template
  left this blank, and the researched benchmark is well above a naive guess.
- **Ongoing SLA retainer, now offered as strongly recommended rather than mandatory**,
  same tiers as the source manual:
  - Essentials — $499/mo (12-hr patch window, monthly audits, 10k credit pool)
  - Growth — $1,250/mo (4-hr patch window, weekly audits, 50k credit pool)
  - Enterprise — $2,950+/mo (2-hr patch window, bi-weekly audits, custom credit pool)

  (Full tier detail in `review.md` §5.1.) The source manual frames this as mandatory,
  arguing that unmaintained automations rot as upstream APIs drift — a real technical
  argument, but research found it's **not the market norm**: several real, published
  competitors sell one-time builds with no retainer and market explicitly against
  lock-in. The corrected pitch: **offer the one-time build as a complete, standalone
  deliverable** (priced to reflect that — see the higher implementation fee above), and
  sell the retainer on its own merits (compliance-grade testing, audited reliability,
  fast incident response) rather than as an unavoidable add-on. This has not been tested
  with a real prospect yet — see `FRAMEWORK.md` Phase 2.

## What's genuinely novel here vs. what's just good practice

Worth being honest about, since this affects how defensible the business is:

- The **engineering practices** (idempotency, signature verification, staged
  testing, HITL gates) are not novel — they're standard practice for any production
  webhook system, just rarely applied by no-code automation freelancers. The moat is
  applying rigor where competitors don't, not the rigor itself.
- The **workflow-shape focus + productized retainer** structure is a well-worn playbook in
  the agency world (see "productized service" / niche agency models generally). Novelty is
  in execution and which specific vertical gets picked first, not the business model shape.
- The **specific workflow patterns** (missed-call SMS resuscitation, invoice line-item
  extraction, quote intake parsing) are concrete and testable — this is the part worth
  validating first, since it's the part that actually determines whether real businesses
  will pay.
