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

**This is also, honestly, a hobby project and a way to see what this kind of
Claude-driven process can actually do** — not something on a hard timeline toward
launching a real agency. That doesn't change what the gates *require* (if this ever
became a real business, the same real-world steps would still be necessary), but it does
change the tone: there's no pressure to rush toward Phase 4, and it's fine for the next
move to be "build something interesting" rather than "close the next commercial
blocker." Both are legitimate uses of this packet.

Update the checkboxes below as things actually happen. This file is the honest answer to
"where are we" at any point in the future.

## Phase model

```
Phase 0          Phase 1              Phase 2            Phase 3         Phase 4            Phase 5
Capture    ──►    Strategic Framing ──► Validation  ──►   Build     ──►  First Client  ──►  Formalize & Scale
(done)            (done)                (research          (blocked      (blocked on 3)      (blocked on 4)
                                          closed out,        on 2)
                                          primary research
                                          still open)
```

### Phase 0 — Capture ✅ done

The raw source material exists and has been read in full.

- [x] Source manual captured (`make.com review.md`, matching PDF)
- [x] Manual reviewed and understood well enough to extract the strategic questions it
      implies

**Gate to Phase 1:** none — automatic once the source material exists.

### Phase 1 — Strategic Framing ✅ done

Turn the raw manual into a decision-ready packet: what it is, whether it's worth pursuing
in principle, what could kill it, what it costs to build.

- [x] `docs/business-idea.md` — the pitch
- [x] `docs/feasibility.md` — demand/cost/validation reasoning (unvalidated)
- [x] `docs/risks.md` — legal/technical/market/operational risk map
- [x] `docs/infrastructure.md` — what building it actually requires
- [x] `docs/entrepreneur-notes.md` — open decisions log
- [x] `docs/documentation-guide.md` + `docs/research-handoff.md` — the packet knows how
      to be read and how to close its own gaps
- [x] **Added 2026-07-23 — architecture and vertical-agnostic scaffolding**, prompted by
      the observation that the vertical-agnostic reframe (see above) was still abstract
      without a technical and process backbone to match it:
      - `docs/architecture.md` — the eight-stage reference architecture, splitting what's
        fixed (the actual technical moat) from what's pluggable per client, grounded
        against the three existing worked examples in `make.com review.md` §7
      - `docs/vertical-playbook.md` — a two-layer screening/onboarding process: cheap
        vertical-level checks before committing research time, then the (already
        vertical-agnostic) per-client discovery process already in the source manual
      - `docs/vertical-scenarios.md` — three hypothetical verticals (dental/medical
        front desk, small law firm intake, e-commerce returns) run through the
        architecture and screening checks as a reasoning stress test — explicitly
        unresearched, meant to test whether the abstraction holds, not to identify a
        real second market. Found the architecture holds up reasonably well, with one
        honest exception (the law-firm scenario suggests an unmodeled ninth stage for
        some verticals) — see that doc for the full reasoning.

**Gate to Phase 2:** none blocking — Phase 1 is a documentation exercise and is
essentially complete. What's *not* done is anything that required leaving this directory.

### Phase 2 — Validation 🔶 in progress

Everything in Phase 1 was reasoning from a single document plus priors — this is where
that starts changing.

- [ ] Talk to 5–10 real trade-business owners/ops people about their actual pain
      (`docs/feasibility.md` §"What needs to be validated") — **still not done, and now
      the single highest-leverage next action, and the only thing left blocking Phase 3**
- [x] Run the `docs/research-handoff.md` queue and merge findings back — done in three
      passes on 2026-07-23: a quick web-search first pass, then two independent
      deep-research passes as a cross-check — ChatGPT
      (`research/2026-07-23-full-deep-research-chatgpt.md`) and Claude/Opus
      (`research/2026-07-23-full-deep-research-opus.md`). Both resolved all 6 questions
      (or confirmed unresolvable-by-web-research on the one that needed to be) and
      **independently corrected the same error** the quick pass had made on Anthropic's
      data-retention figure — genuine corroboration, since the two passes found entirely
      different named competitors from each other yet reached the same conclusion.
      Question 3 (missed-call SMS legality) still needs an actual lawyer, not more
      research — see `docs/risks.md`.
- [x] Sanity-check SLA pricing against what target businesses currently spend — done
      2026-07-23, confirmed by both deep-research passes, see `docs/feasibility.md`

**Finding that changes the priority order:** both deep-research passes confirmed and
strengthened the earlier quick-search signal, each finding a different set of real,
currently-active competitors (17 total between them) — most don't require a mandatory
retainer, several sell one-time builds and market explicitly against lock-in. This is
now a **well-corroborated market fact**, not a hypothesis — see `docs/feasibility.md`
and `docs/entrepreneur-notes.md`. Both passes independently recommend the same fix: stop
presenting the retainer as mandatory, offer a one-time build-and-own path at a premium
($5,000–$8,000+) alongside an incentivized ongoing retainer. Every remaining research
question that could be answered from public data has been answered, by two independent
sources. The only things left in Phase 2 both require leaving this directory: real
conversations with trade-business owners (is the pain real, will they pay ongoing at
all, does the two-path pricing land), and actual lawyer review of the missed-call SMS
pattern before it's sold to anyone.
- [ ] **New action item from research:** decide whether to adopt the two-path pricing
      recommendation (one-time build-and-own + incentivized retainer) before or after
      the first real prospect conversations — see `docs/entrepreneur-notes.md`.
- [x] **Reworked 2026-07-23 — decoupled the target market from HVAC/auto-repair.** The
      packet originally inherited its target vertical directly from the source manual's
      worked examples. On reflection, the actual targeting mechanism should be the
      source manual's own **3-Trait Qualification Test** (volume, unstructured input,
      structured destination — `make.com review.md` §1.3), which is industry-agnostic,
      not a fixed vertical list. `docs/business-idea.md`, `README.md`,
      `docs/feasibility.md`, `docs/entrepreneur-notes.md`, and `docs/risks.md` were all
      updated accordingly. HVAC/auto-repair remain this project's researched case study
      — genuinely useful if that ends up being the first real vertical — but they're no
      longer treated as the definition of the target.
- [ ] **New open decision from that rework:** which vertical to actually validate in
      first is now genuinely open, not pre-answered. Should be decided by where real
      access/domain knowledge exists, not by which industry sounds biggest — see
      `docs/entrepreneur-notes.md` §"Which vertical to actually validate in first."
- [ ] **Expansion plan drafted, 2026-07-23 — not yet executed.** Five specific people
      identified as the first outside readers (two operators in adjacent/comparable
      retainer businesses, a technical peer, an experienced business owner, and a
      low-context reader as a comprehension test), with per-person framing and questions
      worked out before sending anything — see [`docs/expansion.md`](./docs/expansion.md).
      The two operator conversations are the actual Phase 2 primary research this
      tracker has been blocked on; nothing has been sent yet.
- [ ] **New open decision, 2026-07-23 — the platform, and therefore the offer.**
      `docs/what-to-sell.md` works through six product shapes and finds the platform
      choice decides most of them: on Make.com the client rents forever and "build and
      own" isn't quite honest, while on self-hosted n8n ownership is real and a retainer
      has something concrete to charge for (running the thing). The competitor found in
      research who sells one-time builds with no retainer runs self-hosted n8n — their
      model follows from their platform. **Nobody has built the same pipeline on two
      platforms to compare**, so this is reasoning, not measurement; settling it belongs
      in Phase 3. The provisional default is: sell the diagnostic first, then a
      fixed-price build on a platform the client can genuinely own, with hosted
      operations offered as an alternative rather than a condition.

**Gate to Phase 3:** at least one real conversation confirming the pain is real *and*
worth paying for, or a clear signal it's not (in which case: revisit which vertical to
target, per the open decision above, before building anything).

### Phase 3 — Build ⬜ blocked on Phase 2

Stand up the first working pipeline, per `docs/infrastructure.md`.

- [ ] Make.com account + plan tier chosen
- [ ] LLM provider account (Anthropic/OpenAI) with direct HTTP-module access, not native
      Make AI connector
- [ ] Pick the cheapest worked pattern to build first (missed-call SMS resuscitation is
      the current leading candidate — see `docs/entrepreneur-notes.md`)
- [ ] **Build one pipeline twice — once on Make.com, once on self-hosted n8n** — to
      settle the platform question with measurement instead of reasoning
      (`docs/what-to-sell.md`). Cheap to do, and it decides the shape of the offer.
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

**Phase 1 is complete. Phase 2's desk research is done; its primary research is not
started.** Everything answerable from a desk has been answered: two independent
deep-research passes (2026-07-23) resolved the research queue, found 17 competitors
between them, corrected an error from an earlier quick pass, and confirmed the retainer
can't be sold as mandatory. The target market was reframed from a fixed vertical
(HVAC/auto-repair) to the source manual's own qualification test, and the technical
architecture was generalized and stress-tested to match. `docs/what-to-sell.md` then
worked out what the actual offer should be, and found the platform choice (Make.com vs.
self-hosted) decides most of it — unresolved, and now a Phase 3 task.

**The honest read, stated plainly on the site:** the evidence gathered so far leans
against this. Underpriced by real competitors, a differentiator the buyer can't perceive,
a capability being commoditized by the platforms it's built on, and genuine legal risk in
one flagship workflow. None of that is fatal, but no more research changes it — see the
site's "honest read" section.

**Nothing left in Phase 2 can be resolved from inside this directory.** An expansion plan
was drafted 2026-07-23 (`docs/expansion.md`) for showing this to five specific people
first, two of whom run comparable or adjacent retainer businesses — that's the actual
primary research this phase has been blocked on. Not yet sent.

## The second output: the method — ✅ built

The *process* used to get here — turning a raw source doc into a tiered, gated packet —
was generalised into a reusable Claude Code skill at `~/.claude/skills/idea-to-business/`,
so it can be pointed at any future spark without re-deriving the structure. It was tested
by running it against this project from scratch in a separate directory; it mostly
reproduced the packet, and the test surfaced three defects in the skill, two of which were
fixed.

This matters for how the project is read. The business evaluation is the **specimen** and
is genuinely unfinished — Phase 2, unvalidated, possibly never viable. The method is the
**second output**, and unlike the business it has been through a complete cycle including
self-correction. [`docs/method.md`](./docs/method.md) is the honest account of it: the
five moves, what actually worked, and what was overhead — including the observation that
1,800 lines of Markdown now exist in service of an idea no customer has ever heard
described.
