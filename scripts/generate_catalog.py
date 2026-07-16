#!/usr/bin/env python3
"""Generate data/tools.json and data/tools.csv from the tables in README.md.

The README is the single source of truth. This script parses every Markdown
table under a ## section heading and emits one record per row, so the
machine-readable catalog can never drift from the human-readable list.

Usage: python3 scripts/generate_catalog.py
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DATA_DIR = ROOT / "data"

AVAILABILITY = {
    "🟢": "open-source",
    "🟠": "open-weights",
    "🔵": "open-core",
    "🔒": "commercial",
}

# Sections whose tables are navigation aids, not tool entries.
SKIP_SECTIONS = {"Find Tools by Evaluation Goal", "Contents"}

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def strip_markdown(text: str) -> str:
    """Convert inline markdown links to plain text and collapse whitespace."""
    text = LINK_RE.sub(r"\1", text)
    text = text.replace("**", "").replace("*", "")
    return " ".join(text.split())


def parse_readme(md: str):
    records = []
    section = None
    for line in md.splitlines():
        heading = re.match(r"^##\s+(.*)$", line)
        if heading:
            section = strip_markdown(heading.group(1)).strip()
            continue
        if section in SKIP_SECTIONS or section is None:
            continue
        if not (line.startswith("|") and line.count("|") >= 3):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        # Skip header and separator rows.
        if set(cells[0]) <= {"-", " ", ":"} or cells[0] in (
            "Platform", "Tool", "Benchmark", "Leaderboard", "Service", "I want to…"
        ):
            continue

        name_cell, marker_cell, desc_cell = cells[0], cells[1], cells[2]
        name_link = LINK_RE.search(name_cell)
        if not name_link:
            continue

        availability = next(
            (v for k, v in AVAILABILITY.items() if k in marker_cell), None
        )
        # The historical table has no availability column; shift cells.
        if availability is None and section == "Discontinued and Historical Tools":
            availability = "discontinued"
            desc_cell = cells[2] if len(cells) == 3 else cells[-1]

        secondary_links = [
            {"label": label, "url": url}
            for label, url in LINK_RE.findall(desc_cell)
        ]

        records.append(
            {
                "name": strip_markdown(name_link.group(1)),
                "category": section,
                "availability": availability,
                "primary_url": name_link.group(2),
                "description": strip_markdown(desc_cell),
                "secondary_links": secondary_links,
                "status": "discontinued"
                if section == "Discontinued and Historical Tools"
                else "active",
            }
        )
    return records


def main() -> None:
    markdown = README.read_text(encoding="utf-8")
    records = parse_readme(markdown)
    reviewed_match = re.search(r"\*\*Last reviewed:\*\*\s*(\d{4}-\d{2}-\d{2})", markdown)
    last_verified = reviewed_match.group(1) if reviewed_match else None
    DATA_DIR.mkdir(exist_ok=True)

    catalog = {
        "title": "The Comprehensive List of AI Evaluation Tools",
        "source": "https://github.com/aglio-lab/ai-evaluation-tools",
        "license": "CC0-1.0",
        "last_verified": last_verified,
        "entry_count": len(records),
        "tools": records,
    }
    (DATA_DIR / "tools.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    with (DATA_DIR / "tools.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(
            ["name", "category", "availability", "status", "primary_url", "description"]
        )
        for r in records:
            writer.writerow(
                [
                    r["name"],
                    r["category"],
                    r["availability"],
                    r["status"],
                    r["primary_url"],
                    r["description"],
                ]
            )

    print(f"Wrote {len(records)} entries to data/tools.json and data/tools.csv")


if __name__ == "__main__":
    main()
