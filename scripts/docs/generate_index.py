"""
Generate docs/index.md, a domain-grouped index of every documented table.

Data comes from docs/descriptions.yaml (domain + first sentence of the
description). Within each domain, tables are sorted by name.

Usage:
    python scripts/docs/generate_index.py
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"
DESCRIPTIONS_FILE = DOCS_DIR / "descriptions.yaml"
TABLES_DIR = DOCS_DIR / "tables"
OUT_FILE = DOCS_DIR / "index.md"

DEFAULT_DOMAIN = "non-classe"


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    match = re.search(r"(.*?\.)", text)
    return match.group(1).strip() if match else text


def build_index(descriptions: dict) -> dict:
    by_domain: dict[str, list[tuple[str, str]]] = {}
    for key, meta in descriptions.items():
        if not isinstance(meta, dict) or not meta.get("description"):
            continue
        domain = str(meta.get("domain") or DEFAULT_DOMAIN).strip().lower() or DEFAULT_DOMAIN
        by_domain.setdefault(domain, []).append(
            (key, first_sentence(str(meta["description"])))
        )
    for entries in by_domain.values():
        entries.sort()
    return dict(sorted(by_domain.items()))


def render_index(by_domain: dict) -> str:
    lines = ["# Index des tables", ""]
    for domain, entries in by_domain.items():
        lines.append(f"## {domain}")
        lines.append("")
        for key, snippet in entries:
            lines.append(f"- [`{key}`](tables/{key}.md) — {snippet}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    descriptions = yaml.safe_load(DESCRIPTIONS_FILE.read_text(encoding="utf-8")) or {}
    by_domain = build_index(descriptions)
    OUT_FILE.write_text(render_index(by_domain), encoding="utf-8")

    total = sum(len(v) for v in by_domain.values())
    print(f"indexed {total} tables, {len(by_domain)} domains -> {OUT_FILE}")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())