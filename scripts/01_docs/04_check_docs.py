"""
Control / validation script for the generated AdventureWorks docs.

Checks:
  1. Number of .md files == number of tables in the DuckDB.
  2. YAML front matter of every .md file parses without error.
  3. Every table cited in docs/relationships.yaml exists as a .md file.
  4. No stray "None" / "nan" literals in the generated text.
  5. Front-matter `kind` (view/table) matches the AW v* naming convention.
  6. docs/index.md lists every documented table exactly once and links resolve.

Exit code is 0 when all checks pass, 1 otherwise.

Usage:
    python scripts/01_docs/04_check_docs.py
"""

import re
import sys
from pathlib import Path

import duckdb
import yaml

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "adventureworks.duckdb"
OUT_DIR = ROOT / "docs" / "tables"
RELATIONSHIPS_FILE = ROOT / "docs" / "relationships.yaml"
DESCRIPTIONS_FILE = ROOT / "docs" / "descriptions.yaml"

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


def check_view_kinds() -> list[str]:
    """kind (view/table) in the front matter must match the AW source naming
    convention. DuckDB can't tell (CSV mirror imports everything as a physical
    BASE TABLE), so views are identified by the v* name pattern, consistent
    with generate_table_docs.py."""
    con = duckdb.connect(str(DB_PATH), read_only=True)
    try:
        rows = con.execute(
            "SELECT table_schema, table_name FROM information_schema.tables "
            "WHERE table_schema NOT IN ('information_schema')"
        ).fetchall()
    finally:
        con.close()

    errors = []
    for schema, name in rows:
        key = f"{schema}.{name}"
        kind = "view" if re.match(r"^v[A-Z]", name) else "table"
        path = OUT_DIR / f"{key}.md"
        if not path.exists():
            continue  # counted by check 1
        meta = parse_front_matter(path.read_text(encoding="utf-8"))
        if meta is None:
            continue  # counted by check 2
        if meta.get("kind") != kind:
            errors.append(f"{key}.md: front-matter kind={meta.get('kind')!r} but expected {kind}")
    return errors


def check_index() -> list[str]:
    """docs/index.md must list every documented table exactly once, and every
    link target must exist in docs/tables/."""
    index_path = ROOT / "docs" / "index.md"
    if not index_path.exists():
        return ["docs/index.md does not exist — run scripts/01_docs/03_generate_index.py"]

    text = index_path.read_text(encoding="utf-8")
    links = re.findall(r"\[`([^`]+)`\]\(([^)]+)\)", text)
    duplicated = sorted({key for key, _ in links if sum(1 for k, _ in links if k == key) > 1})
    errors = [f"index.md: table listed more than once: {key}" for key in duplicated]

    descriptions = yaml.safe_load(DESCRIPTIONS_FILE.read_text(encoding="utf-8")) or {}
    documented = {k for k, v in descriptions.items() if isinstance(v, dict) and v.get("description")}
    listed = {key for key, _ in links}
    missing = sorted(documented - listed)
    unexpected = sorted(listed - documented)
    errors.extend(f"index.md: missing documented table {t}" for t in missing)
    errors.extend(f"index.md: listed table has no description {t}" for t in unexpected)

    for _, target in links:
        if not (ROOT / "docs" / target).exists():
            errors.append(f"index.md: broken link target {target}")
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
        ("5. view/table kind matches DB catalog", check_view_kinds()),
        ("6. index.md complete and links resolve", check_index()),
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