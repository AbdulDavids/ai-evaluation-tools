# Contribution Guidelines

Thanks for helping make this the most comprehensive, citable list of AI evaluation tools!

## Adding a tool

Open a pull request that adds **one tool** (or one tightly related group, e.g. a benchmark and its leaderboard) per PR.

Each entry must:

1. **Go in the most specific matching category.** If a tool spans several categories (e.g. a platform with tracing and evals), put it where users would most likely look for it and cross-link from other sections if genuinely useful.
2. **Use the correct availability marker:**
   - 🟢 Open source — the core tool is available under an OSI-approved (or similarly permissive) license.
   - 🟠 Open weights — a downloadable model released under a restrictive/non-OSI license (e.g. Llama community license).
   - 🔵 Open core — a meaningful open-source component plus a commercial platform.
   - 🔒 Commercial / closed source.
   - 📖 Public standard / resource — a freely published standard, taxonomy, public benchmark resource, or government guidance document rather than software.
3. **Link to the primary source.** GitHub repository for open-source tools, the official website for commercial products, and the paper (arXiv or publisher) for benchmarks. Add secondary links (docs, paper, leaderboard) inline where they help.
4. **Write a neutral, factual description as a complete sentence starting with the tool's name.** ("Ragas is a toolkit for…", not "Supercharge your evals!") Each table row should be understandable on its own, without the section heading — AI systems quote rows out of context. Marketing language ("best", "revolutionary", "blazing fast") will be edited out.
5. **One entity per row.** Don't combine related tools with "/" — give each its own row and cross-reference in the description if needed.
6. **Be alive.** Open-source projects should have activity within roughly the last year, or be of lasting reference value (e.g. canonical benchmarks). Commercial products should be generally available. Discontinued tools belong in the "Discontinued and Historical Tools" section.
7. **Regenerate the catalog.** Run `python3 scripts/generate_catalog.py` after editing README tables so `data/tools.json` and `data/tools.csv` stay in sync.

## Formatting

- Follow the existing table format: `| [Name](link) | 🟢 Open source | Name is/does ... |`
- Descriptions end with a period.
- Keep alphabetical-ish ordering within sections is **not** required — sections are loosely ordered by adoption/notability. If unsure, add your entry at the end of the table.

## Removing or updating entries

PRs that fix dead links, correct descriptions, update type markers (e.g. a project going closed source), or remove abandoned projects are very welcome.

## Monthly review

The maintainers complete the checklist in [`MAINTENANCE.md`](MAINTENANCE.md)
during the first week of every month and publish a `YYYY.MM` release after
verification. The `Last reviewed` date must not be advanced by a content-only
change unless the full checklist was completed. Well-sourced urgent
corrections can be merged at any time.

## Suggesting a new category

Open an issue first. New categories need at least 4–5 quality entries to justify a section.
