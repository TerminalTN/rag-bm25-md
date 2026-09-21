"""
Control / validation script for the generated AdventureWorks docs.

Checks:
  1. Number of .md files == number of tables in the DuckDB.
  2. YAML front matter of every .md file parses without error.
  3. Every table cited in docs/relationships.yaml exists as a .md file.
  4. No stray "None" / "nan" literals in the generated text.

Exit code is 0 when all checks pass, 1 otherwise.

Usage:
    python check_docs.py
"""

import re
import sys
from pathlib import Path

import duckdb
import yaml

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "adventureworks.duckdb"
OUT_DIR = ROOT / "docs" / "tables"
RELATIONSHIPS_FILE = ROOT / "docs" / "relationships.yaml"

NONE_RE = re.compile(r"\bNone\b")
NAN_RE = re.compile(r"\bnan\b", re.IGNORECASE)


def db_table_count() -> int:
    con = duckdb.connect(str(DB_PATH), read_only=True)
    try:
        return con.execute(
            "SELECT COUNT(*) FROM information_schema.tables "
            "WHERE table_schema NOT IN ('information_schema')"
        ).fetchone()[0]
    finally:
        con.close()


def parse_front_matter(text: str):
    if not text.startswith("---"):
        return None
    body = text.split("---", 2)[1]
    return yaml.safe_load(body)


def check_md_count(n_tables: int) -> list[str]:
    files = list(OUT_DIR.glob("*.md"))
    if len(files) != n_tables:
        return [f"{n_tables} tables in DB but {len(files)} .md files in {OUT_DIR}"]
    return []


def check_front_matter() -> list[str]:
    errors = []
    for path in sorted(OUT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        try:
            meta = parse_front_matter(text)
        except Exception as exc:
            errors.append(f"{path.name}: front-matter parse error: {exc}")
            continue
        if meta is None:
            errors.append(f"{path.name}: missing or malformed YAML front matter")
        elif not isinstance(meta, dict):
            errors.append(f"{path.name}: front matter is not a YAML mapping")
    return errors


def check_relationships() -> list[str]:
    try:
        data = yaml.safe_load(RELATIONSHIPS_FILE.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{RELATIONSHIPS_FILE.name}: parse error: {exc}"]

    cited = set(data.get("tables", {}).keys())
    for meta in data.get("tables", {}).values():
        for fk in meta.get("foreign_keys", []):
            cited.add(fk["ref_table"])

    missing = sorted(t for t in cited if not (OUT_DIR / f"{t}.md").exists())
    return [f"no .md file for cited table {t}" for t in missing]


def check_text_clean() -> list[str]:
    errors = []
    for path in sorted(OUT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for label, regex in (("None", NONE_RE), ("nan", NAN_RE)):
            hits = sorted({m.group() for m in regex.finditer(text)})
            if hits:
                errors.append(f"{path.name}: literal(s) {hits} found")
    return errors


def main() -> int:
    try:
        n_tables = db_table_count()
    except duckdb.IOException as exc:
        print(f"ERROR: cannot open DuckDB ({exc}). Is the DB locked by another process?")
        return 1

    checks = [
        ("1. .md files == tables in DB", check_md_count(n_tables)),
        ("2. YAML front matter parses", check_front_matter()),
        ("3. relationships cited have .md files", check_relationships()),
        ("4. no stray None/nan in docs", check_text_clean()),
    ]

    failed = 0
    for label, errors in checks:
        if errors:
            failed += 1
            print(f"FAIL  {label}")
            for err in errors[:20]:
                print(f"        - {err}")
        else:
            print(f"PASS  {label}")

    print()
    if failed:
        print(f"{failed} check(s) failed.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())