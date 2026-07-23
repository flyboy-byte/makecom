**Prompt used:**
> Make.com Zapier automation agency pricing HVAC auto repair shop

**Engine:** Claude Code `WebSearch` tool (standard web search, not a browser-based Claude.ai/ChatGPT deep-research session — see caveat below) · **Date:** 2026-07-23

**Caveat:** `docs/research-handoff.md` originally specified running this through a browser
deep-research mode. This was run instead via Claude Code's own `WebSearch` tool, which
does a standard web search rather than a multi-step deep-research pass. Treat this as a
faster, shallower first pass — good enough to sanity-check the pricing range, but a real
deep-research session (or direct outreach to a few competing agencies) would likely surface
more specific, better-sourced competitor data if this becomes decision-critical.

**Raw findings:**

Make.com's paid plans start at $12/month (billed annually) for 10,000 credits; Zapier
starts free with paid plans from $20/month (Starter) to $799/month (Team). Make.com is
reported to save mid-market companies over $4,000/year in tool costs versus Zapier for
comparable automation needs.

For service businesses like HVAC and auto repair shops specifically, automation agencies
serving trades (including HVAC) typically charge **$2,000–$15,000 one-time for a build,
with no monthly retainer required** in at least some competitor offerings — this directly
contradicts the "mandatory retainer" assumption in this packet's business model and is
the single most important finding here (see merge into `docs/feasibility.md` and
`docs/entrepreneur-notes.md`). One agency lists n8n/Zapier/Make.com workflow builds
starting at $50, with AI agents from $500 — clearly a much lower floor than this packet's
$499–$2,950+/mo retainer tiers, though not necessarily a comparable scope of engineering
rigor.

No pricing was found broken out specifically by client size/complexity tier, and no
agency was found doing the specific idempotency/signature-verification/staged-testing
discipline this packet assumes as a differentiator — can't confirm or rule out whether
that rigor is actually visible/marketed by competitors, or just not surfaced in search
results.

Sources:
- [Make.com pricing: Is it worth it? [2026] | Zapier](https://zapier.com/blog/make-com-pricing/)
- [Make vs Zapier Pricing: More value for money in 2024?](https://integrately.com/blog/zapier-vs-make-pricing)
- [AI Automation Services Pricing | Fixed Rates Starting at $50](https://aiadoptionagency.com/ai-automation-services-pricing/)
- [Automation Agency vs. DIY Zapier or Make: Which Route Wins for Small Business](https://aplosai.com/blog/automation-agency-vs-diy)
- [Make.com vs Zapier Pricing 2026: Real Tool Costs From 3 Mid-Market Implementations](https://www.automationshowroom.com/en/blog/make-vs-zapier-pricing)
