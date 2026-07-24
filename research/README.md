# Research Intake

Raw output from external deep-research sessions (Claude.ai / ChatGPT research modes),
saved here before being merged into the docs that consume them. See
[`../docs/research-handoff.md`](../docs/research-handoff.md) for the full workflow and
current queue of open research questions.

File naming: `YYYY-MM-DD-<short-topic-slug>-<engine>.md`. Each file should preserve the
exact prompt used plus the raw response, unedited — corrections and synthesis happen in
the consuming doc (`docs/feasibility.md`, `docs/risks.md`, etc.), not here.

Seven files, all 2026-07-23, in three rounds:

1. **Five fast passes** via Claude Code's `WebSearch` tool — quick, shallow, and useful
   mainly for revealing which questions were load-bearing. One of them introduced a
   factual error about API data retention.
2. **A full ChatGPT deep-research pass** against the whole question set, which caught
   that error.
3. **A full Claude/Opus deep-research pass** against the identical prompt, as a second
   opinion. It found an entirely different set of competitors while reaching the same
   conclusion, and independently confirmed the same correction.

Where the fast passes and the deep passes disagree, the deep passes win — see
`docs/method.md` for what that episode says about the process.
