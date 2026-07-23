# Vertical & Client Onboarding Playbook

> **Tier:** Mixed — the screening pass is high-level (founder judgment call), the
> discovery process is low-level (structured intake) · **Audience:** whoever is
> evaluating a candidate vertical or a candidate client · **Use when:** a new industry
> or a new prospect shows up and you need a repeatable way to decide "is this worth
> pursuing" before investing real time.

## Why this doc exists

`make.com review.md` §1 already contains a genuinely vertical-agnostic discovery
process — the Client Intake Questionnaire (§1.1) and the 3-Trait Qualification Test
(§1.3) are written in industry-neutral language ("What specific app, inbox, or trigger
event initiates this workflow?"). The only place the source manual hardcodes a vertical
is the *example* mapping table in §1.4 (HVAC/auto-repair). That table got mistaken for a
requirement earlier in this packet's history — see `docs/business-idea.md`'s 2026-07-23
rework. This doc adds the piece that was actually missing: a **screening pass for a new
vertical**, one level more abstract than the existing per-client discovery process,
since "is this business a good fit" and "is this entire industry worth researching" are
different questions.

## Layer 1 — Vertical screening (new, not in the source manual)

Before spending real research time on a vertical (the way `docs/feasibility.md` and
`docs/research-handoff.md` did for HVAC/auto-repair), run it through these cheaper,
faster checks first:

1. **Does the 3-Trait Test plausibly apply industry-wide, not just to one business you
   happen to know?** A single anecdote ("my dentist complains about missed calls") is a
   reason to look closer, not a reason to commit — the test needs to plausibly hold
   across many businesses in that industry, not just the one you have access to.
2. **Is there a visible existing budget line this competes with?** Every real market
   this packet has looked at so far (HVAC/auto-repair CRM software, answering services,
   VAs) had one. If a candidate vertical has no comparable existing spend to benchmark
   against, that's not disqualifying, but it removes a cheap sanity check the other
   verticals had — flag it explicitly rather than skipping the check.
3. **Is there a regulatory dimension that changes the technical/legal picture?**
   HVAC/auto-repair's answer was TCPA (see `docs/risks.md`). Other verticals will have
   their own — HIPAA for healthcare, financial-services regs for anything touching
   payments, bar-association rules for legal services. Identify this *before* deep
   research, since it changes what questions belong in the research-handoff queue.
4. **Can you sketch the architecture table from `docs/architecture.md` at least roughly**
   — plausible trigger, plausible destination system, plausible extraction schema —
   even without talking to a real business yet? If stages 5 and 8 are a total blank,
   that's a sign this vertical needs a real conversation before it's researchable at all.
5. **Do you have real access** — a personal connection, a warm intro, a channel to
   actually reach businesses in this vertical for primary research? Per
   `docs/entrepreneur-notes.md`, this is the tie-breaker between multiple candidates that
   pass checks 1–4 equally well.

A vertical that clears all five is worth the kind of investment HVAC/auto-repair already
got (a `docs/feasibility.md`-style demand analysis, a `docs/research-handoff.md` queue,
a competitor scan). A vertical that fails check 5 specifically is worth *researching*
but not worth *validating* yet — research can happen from a desk, validation can't.

## Layer 2 — Per-client discovery (already vertical-agnostic in the source manual)

Once a vertical is chosen and a specific candidate business is being evaluated, the
existing source-manual process applies as-is — it doesn't need reworking, just doesn't
need to be re-derived per vertical either:

1. **The Client Intake Questionnaire** (`review.md` §1.1) — five questions, all
   industry-neutral: trigger event, downstream systems, weekly frequency, top manual-fix
   reasons, financial impact if offline 24 hours.
2. **The Video Capture Mandate** (`review.md` §1.2) — 5 recordings of staff doing the
   workflow by hand. Already flagged in `docs/entrepreneur-notes.md` as possibly too
   high-friction for client #1 specifically — that concern is unrelated to vertical
   choice and applies the same way regardless of industry.
3. **The 3-Trait Qualification Test** (`review.md` §1.3) — volume, unstructured input,
   structured destination. This is the actual gate; everything above feeds it.
4. **Sketch the `docs/architecture.md` table concretely** for this specific business —
   this is the point where the qualification test's "right shape" claim either holds up
   in detail or doesn't. If it doesn't, that's a real signal to walk away from this
   *client*, independent of whether the *vertical* is still worth pursuing.

## What decides "go" at each layer

- **Layer 1 (vertical) fails** → don't invest research time in this industry yet; keep
  it as a candidate if a specific opportunity to learn more shows up.
- **Layer 1 passes, Layer 2 (client) fails** → this vertical may still be worth pursuing;
  this particular business isn't a fit. Don't let one bad-fit conversation kill an
  otherwise-promising vertical.
- **Both pass** → proceed to `FRAMEWORK.md` Phase 2's actual validation step: the real
  conversation.
