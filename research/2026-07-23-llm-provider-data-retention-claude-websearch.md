**Prompt used:**
> Anthropic API data retention policy zero data retention ZDR enterprise
> OpenAI API data retention policy zero data retention enterprise 2026

**Engine:** Claude Code `WebSearch` tool (standard web search) · **Date:** 2026-07-23

**Raw findings — Anthropic:**

Standard Claude API retention is **7 days** (reduced from 30 days as of September 2025)
— this updates `make.com review.md` §4.1's "30-Day Retention" claim, which is now stale.
API data is not used for model training by default. Zero Data Retention (ZDR) eliminates
even the 7-day window — inputs/outputs are not stored at rest after the response
returns — but is scoped to eligible Anthropic API usage and Claude Code on Claude
Enterprise specifically; it does not cover Claude Team/Enterprise chat interfaces.
Sessions flagged for a policy violation may be retained up to 2 years regardless of ZDR
status. Certain "Covered Models" are excluded from ZDR entirely and require 30-day
retention regardless.

**Raw findings — OpenAI:**

Default API retention is **30 days**, not used for training by default; inputs/outputs
are removed after 30 days unless legally required to be kept longer. ZDR is available for
eligible enterprise customers on supported endpoints only, requires an explicit request
and approval — it's not a self-service toggle. Training-exclusion and retention are
separate controls: an account can have training excluded without also having ZDR. Even
under ZDR, some metadata/abuse-monitoring data may still be retained for legal/safety
reasons — "zero" isn't absolute.

**Merge implications:** `make.com review.md` §4.1's blanket "30-Day Retention" framing is
outdated for Anthropic (now 7 days) and was already roughly accurate for OpenAI (still
30 days). ZDR is real for both providers but is an enterprise-tier, request-and-approval
process for OpenAI, and API/Claude-Code-Enterprise-scoped (not blanket) for Anthropic —
this packet should not represent ZDR as a simple settings flag either provider offers.

Sources:
- [Zero data retention - Claude Code Docs](https://code.claude.com/docs/en/zero-data-retention)
- [API and data retention - Claude Platform Docs](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)
- [I have a zero data retention agreement with Anthropic. What products does it apply to? | Anthropic Privacy Center](https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to)
- [Enterprise privacy at OpenAI](https://openai.com/enterprise-privacy/)
- [Business data privacy, security, and compliance | OpenAI](https://openai.com/business-data/)
