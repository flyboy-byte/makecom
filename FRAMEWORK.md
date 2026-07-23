# Framework — Idea → Business

> **Tier:** Meta (self-aware — this doc describes and tracks the project it's part of)
> **Audience:** you · **Use when:** you don't know what to do next, or you're checking
> in on progress after time away.

## What this is

This directory started as one file — a technical manual (`make.com review.md`) pulled
from Google Drive. This doc is what turns that single spark into a staged process for
finding out whether it's a real business, and building it if so. It's not a plan that
gets written once and followed blindly — it's a **status tracker with gates**: each phase
has a concrete exit condition, and you don't move to the next phase by writing more docs,
you move by doing the thing the gate actually requires (a conversation, a test, a signed
contract). Docs support the phases; they don't substitute for them.

Update the checkboxes below as things actually happen. This file is the honest answer to
"where are we" at any point in the future.

## Phase model

```
Phase 0          Phase 1              Phase 2            Phase 3         Phase 4            Phase 5
Capture    ──►    Strategic Framing ──► Validation  ──►   Build     ──►  First Client  ──►  Formalize & Scale
(done)            (mostly done)         (not started)     (blocked      (blocked on 3)      (blocked on 4)
                                                            on 2)
```

### Phase 0 — Capture ✅ done

The raw source material exists and has been read in full.

- [x] Source manual captured (`make.com review.md`, matching PDF)
- [x] Manual reviewed and understood well enough to extract the strategic questions it
      implies

**Gate to Phase 1:** none — automatic once the source material exists.

### Phase 1 — Strategic Framing ✅ mostly done

Turn the raw manual into a decision-ready packet: what it is, whether it's worth pursuing
in principle, what could kill it, what it costs to build.

- [x] `docs/business-idea.md` — the pitch
- [x] `docs/feasibility.md` — demand/cost/validation reasoning (unvalidated)
- [x] `docs/risks.md` — legal/technical/market/operational risk map
- [x] `docs/infrastructure.md` — what building it actually requires
- [x] `docs/entrepreneur-notes.md` — open decisions log
- [x] `docs/documentation-guide.md` + `docs/research-handoff.md` — the packet knows how
      to be read and how to close its own gaps

**Gate to Phase 2:** none blocking — Phase 1 is a documentation exercise and is
essentially complete. What's *not* done is anything that required leaving this directory.

### Phase 2 — Validation 🔶 in progress

Everything in Phase 1 was reasoning from a single document plus priors — this is where
that starts changing.

- [ ] Talk to 5–10 real trade-business owners/ops people about their actual pain
      (`docs/feasibility.md` §"What needs to be validated") — **still not done, and now
      the single highest-leverage next action, and the only thing left blocking Phase 3**
- [x] Run the `docs/research-handoff.md` queue and merge findings back — done in two
      passes on 2026-07-23: a quick web-search first pass, then a full ChatGPT
      deep-research pass (`research/2026-07-23-full-deep-research-chatgpt.md`) that
      resolved all 6 questions (or confirmed unresolvable-by-web-research on the one that
      needed to be) and **corrected an error** the quick pass had made on Anthropic's
      data-retention figure. Question 3 (missed-call SMS legality) still needs an actual
      lawyer, not more research — see `docs/risks.md`.
- [x] Sanity-check SLA pricing against what target businesses currently spend — done
      2026-07-23 (deep research), see `docs/feasibility.md` and
      `research/2026-07-23-full-deep-research-chatgpt.md`
- [ ] Decide, based on the above, whether the ≥10-runs/week qualification bar is
      realistic for the reachable prospect pool

**Finding that changes the priority order:** the deep-research pass confirmed and
strengthened the earlier quick-search signal — at least 9 real, currently-active
competitors serve this exact niche, and most don't require a mandatory retainer (one
sells a $497 one-time, no-monthly, no-contract package). This is now a **sourced market
fact**, not a hypothesis — see `docs/feasibility.md` and `docs/entrepreneur-notes.md`.
Every remaining research question that could be answered from public data has been
answered. The only things left in Phase 2 both require leaving this directory: real
conversations with trade-business owners (is the pain real, will they pay ongoing at
all), and actual lawyer review of the missed-call SMS pattern before it's sold to anyone.

**Gate to Phase 3:** at least one real conversation confirming the pain is real *and*
worth paying for, or a clear signal it's not (in which case: revisit `business-idea.md`'s
vertical choice before building anything, not after).

### Phase 3 — Build ⬜ blocked on Phase 2

Stand up the first working pipeline, per `docs/infrastructure.md`.

- [ ] Make.com account + plan tier chosen
- [ ] LLM provider account (Anthropic/OpenAI) with direct HTTP-module access, not native
      Make AI connector
- [ ] Pick the cheapest worked pattern to build first (missed-call SMS resuscitation is
      the current leading candidate — see `docs/entrepreneur-notes.md`)
- [ ] Build one working demo end-to-end, even without a paying client yet
- [ ] Run the 50-valid / 10-malformed test suite against it (`make.com review.md` §3.2)

**Gate to Phase 4:** one working, tested pipeline that could be shown to a real prospect.

### Phase 4 — First Client ⬜ blocked on Phase 3

- [ ] Land one paying client on the built pattern
- [ ] Get the MSA clauses (`make.com review.md` §4.2) reviewed by an actual lawyer before
      this client signs anything
- [ ] Fill in the real implementation fee (currently a blank in the SOW template,
      `make.com review.md` §6) based on actual build time from Phase 3
- [ ] Deliver through the full Sandbox → Production sequence (§3.3), including the
      14-day rollback window

**Gate to Phase 5:** first client live in production, retainer billing started.

### Phase 5 — Formalize & Scale ⬜ blocked on Phase 4

- [ ] Decide whether "mandatory retainer" framing survived contact with a real client
- [ ] Formalize pricing/SOW numbers based on what actually worked, not the placeholder
      figures in this packet
- [ ] Decide ZDR policy per client tier
- [ ] Start building internal tooling for the test-payload generation process (currently
      manual per `docs/infrastructure.md` §"Testing infrastructure") once past 2–3 clients
- [ ] Name/brand the agency (currently unnamed — `docs/entrepreneur-notes.md`)

## Current status (update this line as phases advance)

**We are in Phase 2, in progress — the research-handoff queue is done.** Phase 1 is
complete. All 6 research questions have been resolved (or correctly confirmed
unresolvable by web research) via a real ChatGPT deep-research pass on 2026-07-23,
which also corrected an error from an earlier quick-search first pass (Anthropic's data
retention figure — see `docs/risks.md`). The confirmed headline finding: at least 9 real
competitors serve this exact niche, and most don't require a mandatory retainer — this
is now a sourced market fact, not a hypothesis, and directly threatens this packet's
pricing model (see `docs/feasibility.md`, `docs/entrepreneur-notes.md`). Nothing left in
Phase 2 can be resolved from inside this directory. The single highest-leverage next
action: talk to real trade-business owners, specifically testing whether they'll pay an
ongoing retainer at all given named competitors don't require one. The missed-call SMS
workflow pattern also needs an actual lawyer before it's ever sold to a client — that's
the other real-world action item research alone can't close.

## On the "reusable framework" idea

Separately, you flagged that the *process* used to get here — a handful of prompts
turning a raw source doc into this tiered, gated packet — is worth generalizing into
something you could point at any future spark of inspiration (the "college, get inspired"
case). That's a good idea and a natural fit for a Claude Code Skill, but it's explicitly
out of scope for this directory, which is about *this* idea specifically. If you want to
pursue that later, say so and it can be built as a separate, standalone thing — probably
by generalizing this file and the `docs/` structure into a template once this project has
been through a full cycle and you know what actually mattered vs. what was overhead.
