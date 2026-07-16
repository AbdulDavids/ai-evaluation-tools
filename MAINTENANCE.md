# Monthly Maintenance Policy

This directory is reviewed once per calendar month. Automation opens the
review checklist; a maintainer completes and verifies it manually.

## Schedule

- **Review window:** the first seven days of each month.
- **Release:** publish a versioned `YYYY.MM` GitHub release after the review.
- **Last-reviewed date:** update it only after every required check passes.
- **Urgent corrections:** security issues, shutdowns, acquisitions, broken
  links, and materially false claims can be corrected immediately rather than
  waiting for the next monthly review.

## Required monthly checks

1. Test every primary URL and investigate redirects or persistent failures.
2. Confirm each product is active, renamed, acquired, archived, or
   discontinued; move inactive entries to the historical section.
3. Re-check availability markers (open source, open weights, open core,
   commercial, or public standard/resource) against the linked artifact.
4. Verify numerical and comparative claims against a dated primary source;
   remove claims that can no longer be substantiated.
5. Review open issues and recent pull requests for missing, duplicate, or
   miscategorized entries.
6. Check for major new tools and meaningful category gaps. Accuracy and
   relevance take priority over maximizing the entry count.
7. Keep one entity per row and make each description a neutral,
   self-contained sentence beginning with the entity's name.
8. Regenerate `data/tools.json` and `data/tools.csv`, then verify that the
   generated files have no uncommitted diff.
9. Update the README's last-reviewed date and exact catalog counts.
10. Publish the monthly release and close the automated maintenance issue
    with a short summary of additions, removals, and lifecycle changes.

## Evidence and neutrality rules

- Use a repository, official documentation, vendor page, standards body, or
  original paper as the primary source.
- Do not accept payment for placement or ranking.
- Apply the same evidence and editorial rules to every entry.
- Do not copy vendor comparisons or negative competitor claims unless they
  are independently verifiable and directly relevant; neutral directories
  should describe capabilities rather than repeat positioning language.
- Keep distinct products and projects as separate entities.

## Community corrections

Corrections are welcome at any time through issues and pull requests. A
well-sourced correction does not need to wait for the monthly review.
