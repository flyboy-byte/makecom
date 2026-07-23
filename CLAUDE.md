# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is not a codebase — there is no build, lint, or test tooling here. It is a
phase-gated business-evaluation packet for a single idea (a Make.com-based "Workflow
Repair Agency"), written as structured Markdown.

## Where to start

Read `FRAMEWORK.md` first, always — it is the self-aware status tracker for this
project: which phase it's in (Capture → Strategic Framing → Validation → Build → First
Client → Formalize & Scale), what's actually done vs. just written down, and the single
next unblocking action. Do not treat the existence of a doc as evidence a phase is
complete — phases advance by something happening outside the documents (a conversation,
a test, a signed agreement), not by more writing.

`docs/documentation-guide.md` explains the doc tiering in full; the short version:

- **High-level** (`docs/business-idea.md`, `docs/feasibility.md`,
  `docs/entrepreneur-notes.md`, `docs/vertical-scenarios.md`, and the legal/market
  sections of `docs/risks.md`) answers "should this exist" — written for the
  decision-maker, assumes no technical background.
- **Low-level** (`docs/architecture.md`, `docs/infrastructure.md`, the
  technical/operational sections of `docs/risks.md`) answers "how does this get built" —
  assumes the high-level case is already accepted.
- **Mixed** (`docs/vertical-playbook.md`) bridges both — a repeatable process that spans
  a high-level screening judgment call and a low-level structured intake.
- **Meta** (`FRAMEWORK.md`, `docs/documentation-guide.md`, `docs/research-handoff.md`)
  describes the packet itself.

The target market is defined by the source manual's 3-Trait Qualification Test (volume,
unstructured input, structured destination — `make.com review.md` §1.3), not by a fixed
industry. HVAC/auto-repair are this project's researched case study, not the definition
of who it's for — see `docs/business-idea.md` and `docs/vertical-scenarios.md`. Don't
reintroduce vertical-specific language into vertical-agnostic docs (`architecture.md`,
`vertical-playbook.md`) without a good reason.

`make.com review.md` (with matching PDF) is the original source manual this packet was
built from — treat it as the technical spine; the `docs/` files are the strategic layer
built on top of it, and cite it by section (`§2.2`, etc.) rather than restating it.

## Working conventions in this repo

- Every doc opens with a `> **Tier:** ... · **Audience:** ... · **Use when:** ...` header
  block. Preserve this pattern in any new or edited doc.
- Distinguish inferred/unverified claims from confirmed ones explicitly, inline — do not
  let a placeholder number or an assumption read as a fact. Unverified market, pricing,
  or legal claims belong in `docs/research-handoff.md`'s queue (for external deep
  research) rather than being asserted directly, unless they've since been confirmed with
  a cited source in `research/`.
- `research/` holds raw, unedited output from external Claude/ChatGPT deep-research
  sessions, named `YYYY-MM-DD-<topic-slug>-<engine>.md`. Corrections and synthesis happen
  in the consuming doc, never by editing the saved research file.
- After any substantive change to this packet's content or status, update the relevant
  checkboxes and the "Current status" line in `FRAMEWORK.md` — it is meant to always be
  the honest, current answer to "where are we."

## Related tooling

A generalized version of this packet's structure exists as a Claude Code skill,
`idea-to-business` (`~/.claude/skills/idea-to-business/`), for applying the same
framework to other ideas. It is intentionally a separate, standalone tool — do not use it
to regenerate or restructure files in this directory; edit this project's docs directly.
