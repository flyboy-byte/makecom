# What To Sell

> **Tier:** High-level (strategy) · **Audience:** whoever is deciding the offer ·
> **Use when:** working out what the actual product is, before quoting anyone. Pairs
> with [`feasibility.md`](./feasibility.md), which covers what the market pays, and
> [`architecture.md`](./architecture.md), which covers what gets built.

## The problem this page exists to solve

The source manual assumed one shape: a custom build, plus a mandatory monthly retainer,
on Make.com. Research killed part of that — [the retainer can't be mandatory](./feasibility.md)
without fighting competitors who sell one-time builds and market against lock-in — but
nothing replaced it. This page works out what else the offer could be.

Two assumptions get examined here, because both are inherited rather than chosen: that
the platform is Make.com, and that recurring revenue means a maintenance retainer.

## The platform is a business decision, not a technical one

[`architecture.md`](./architecture.md) establishes that the eight-stage pipeline is
platform-agnostic — the stages are a shape, not a vendor's feature list. That means the
platform choice is free to be made on business grounds. It is the single decision that
most changes what can honestly be sold.

| | **Make.com** | **Self-hosted n8n** | **Zapier** | **Plain code** |
|---|---|---|---|---|
| Who pays to run it | Client, forever, per operation | Client, ~$5–20/mo for a server | Client, forever, most expensive per task | Client, near-zero at this volume |
| Can they truly own it | **No** — it stops if they stop paying Make | **Yes** — it's their server, their files | No | Yes |
| Build speed | Fast | Moderate | Fastest | Slowest |
| Fits the hardened architecture | Well | Well | Poorly — limited custom logic | Perfectly |
| Who can maintain it after you | Anyone who knows Make | Someone technical | Anyone who knows Zapier | A developer |
| Honest recurring revenue | Hard — you're reselling someone else's product | **Easy — you're running infrastructure** | Hard | Moderate |

**The consequence is sharper than it looks.** On Make.com, "build and own" is close to a
lie: the client owns a configuration inside a product they must keep renting, and if
Make changes pricing or deprecates a module, that's their problem and your support call.
On self-hosted n8n, ownership is real and transferable — which is exactly why the
competitor found in research selling one-time builds with no retainer
([AutomateNexus](./feasibility.md)) runs self-hosted n8n. Their business model is
downstream of their platform choice.

It also inverts the retainer argument. On Make.com the retainer has to be justified by
something vague ("APIs drift"). On self-hosted infrastructure, the retainer is justified
by something concrete and true: **somebody has to run the server, patch it, and notice
when it stops.** That is a service, not a maintenance fee looking for a rationale.

**Unresolved:** nobody has actually built the same pipeline twice on two platforms to
compare real cost and effort. Everything above is reasoning from the platforms' published
models, not measured. It belongs in [`FRAMEWORK.md`](../FRAMEWORK.md) Phase 3 as something
to settle by building, not by more research.

## Why the retainer keeps failing to justify itself

The recurring-revenue problem here is not price. It's that **a working automation is
invisible.** It runs, nothing goes wrong, and the client sees no evidence they're getting
anything for the money. Month four is when they ask what they're paying for.

"Maintenance" makes this worse, because it's a promise about problems that mostly don't
happen. Recurring revenue survives only when it produces something the client can
actually see. Four things can do that:

1. **You run the infrastructure.** Real, ongoing, and obviously a service. Only available
   if you host — which is a platform decision, not a pricing one.
2. **You absorb the consumption.** LLM and platform costs, passed through with a modest
   margin, billed as one predictable number instead of a variable bill they have to
   reason about. The value is the predictability.
3. **You reserve capacity for changes.** A fixed number of hours a month for
   modifications. Businesses change constantly; the workflow will need edits. This is the
   most honest recurring value in the list because the need is certain, not hypothetical.
4. **You make the invisible visible.** A monthly report: runs completed, records created,
   malformed inputs caught before they reached anyone, hours of manual entry displaced.
   This is the cheapest of the four to deliver and the one that most directly solves the
   month-four problem — it's not really a service, it's evidence.

The fourth is worth attaching to whichever of the others gets sold. A retainer that
reports on itself is much harder to cancel than one that doesn't.

## Product shapes

Six things that could be sold, roughly in order of how easily an unproven operator could
sell them.

### 1. The diagnostic — sold on its own

A paid discovery engagement that produces a mapped workflow, a qualification verdict, and
a fixed quote to build it. No build commitment either way.

The packet already contains the entire methodology for this: the intake questionnaire,
the recorded-walkthrough requirement, and the 3-Trait Qualification Test
(`make.com review.md` §1), plus the screening process in
[`vertical-playbook.md`](./vertical-playbook.md).

This is the strongest opening product and it's currently being given away. It sells before
anything is built, so it needs no track record and carries no delivery risk. It qualifies
bad fits *out* at the client's expense rather than yours. It produces something genuinely
valuable even if they never buy a build — a documented map of a process the business has
never written down. And it converts the source manual's biggest sales obstacle (asking a
stranger for five screen recordings) into something they've paid for and are therefore
invested in completing.

**Downside:** small, and it caps out. Nobody builds a business on diagnostics alone.

### 2. Fixed-price pipeline, build and own

One workflow, built, tested, handed over. They own it outright and owe nothing after.
Priced at the benchmark established in [`feasibility.md`](./feasibility.md).

Neutralises the lock-in objection completely, matches what the no-retainer competitors
sell, and is the easiest thing to say yes to. **Requires a platform where ownership is
real** — see the table above.

**Downside:** no recurring revenue, so income restarts at zero every month.

### 3. Build, plus hosted operations

The same build, but you host and run it. Monthly covers infrastructure, consumption, and
a monthly report.

The retainer here is defensible because it's tied to something real and ongoing rather
than to hypothetical breakage.

**Downside:** you now operate production infrastructure for other people, with everything
that implies. This is a genuine operational commitment, not a billing arrangement.

### 4. Retained change capacity

A fixed monthly block of hours for modifications, on top of any of the above.

Honest, easy to explain, and the underlying need is real rather than speculative.

**Downside:** unused hours breed resentment; heavy months breed disputes. Needs clear
rules about rollover before it's sold, not after.

### 5. The productised repeat

The same pipeline sold repeatedly into one vertical — configured per client rather than
rebuilt. Margin improves every time it's sold.

**Downside:** requires having done it at least twice, and requires the vertical focus this
packet [deliberately loosened](./business-idea.md). It's a later-stage move, and it
reintroduces a constraint that was removed for good reasons.

### 6. Build-with, not build-for

Built alongside someone technical on the client's staff, who is left able to maintain it.
Priced above a plain build because it's slower.

Only sellable to businesses that have such a person, which most of the target market
doesn't. Worth knowing about; not worth planning around.

## A defensible default

Nothing here is tested. But if a first offer had to be assembled today from what's
actually known:

**Sell the diagnostic. Then sell a fixed-price build on a platform the client can really
own. Offer hosted operations as a genuine alternative — for clients who don't want to run
anything themselves — rather than as a condition of the build. Attach a monthly report to
any recurring arrangement, so the value stays visible.**

That structure has no lock-in objection to defend, produces revenue before anything is
built, and gives recurring revenue an honest justification. Whether anyone buys it is
exactly the [Phase 2](../FRAMEWORK.md) question that no amount of writing settles.
