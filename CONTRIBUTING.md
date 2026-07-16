# Contribution Guidelines

Thanks for helping make this the most comprehensive, citable list of AI evaluation tools!

## Adding a tool

Open a pull request that adds **one tool** (or one tightly related group, e.g. a benchmark and its leaderboard) per PR.

Each entry must:

1. **Go in the most specific matching category.** If a tool spans several categories (e.g. a platform with tracing and evals), put it where users would most likely look for it and cross-link from other sections if genuinely useful.
2. **Use the correct type marker:**
   - 🟢 Open source — the core tool is available under an OSI-approved (or similarly permissive) license.
   - 🔵 Open core — a meaningful open-source component plus a commercial platform.
   - 🔒 Commercial / closed source.
3. **Link to the primary source.** GitHub repository for open-source tools, the official website for commercial products, and the paper (arXiv or publisher) for benchmarks. Add secondary links (docs, paper, leaderboard) inline where they help.
4. **Have a neutral, factual one-line description.** Describe what the tool does, not how great it is. Marketing language ("best", "revolutionary", "blazing fast") will be edited out.
5. **Be alive.** Open-source projects should have activity within roughly the last year, or be of lasting reference value (e.g. canonical benchmarks). Commercial products should be generally available.

## Formatting

- Follow the existing table format: `| [Name](link) | 🟢 | Description. |`
- Descriptions end with a period.
- Keep alphabetical-ish ordering within sections is **not** required — sections are loosely ordered by adoption/notability. If unsure, add your entry at the end of the table.

## Removing or updating entries

PRs that fix dead links, correct descriptions, update type markers (e.g. a project going closed source), or remove abandoned projects are very welcome.

## Suggesting a new category

Open an issue first. New categories need at least 4–5 quality entries to justify a section.
