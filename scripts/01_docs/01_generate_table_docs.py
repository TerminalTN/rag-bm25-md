"""
Generate one Markdown file per table in the AdventureWorks DuckDB.

For each table emit:
  - table & schema metadata
  - human description (from docs/descriptions.yaml, when present)
  - a column block: type, non-null count, null %, distinct count,
    min/max/avg/std/median (via DuckDB SUMMARIZE)

Usage:
    python scripts/01_docs/01_generate_table_docs.py
"""

import math
import re
from pathlib import Path
from types import SimpleNamespace

import duckdb
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "adventureworks.duckdb"
DOCS_DIR = ROOT / "docs"
OUT_DIR = DOCS_DIR / "tables"
DESCRIPTIONS_FILE = DOCS_DIR / "descriptions.yaml"
RELATIONSHIPS_FILE = DOCS_DIR / "relationships.yaml"
TEMPLATE = "table.md.j2"

SUMMARIZE_FIELDS = [
    "column_name", "column_type", "min", "max", "approx_unique",
    "avg", "std", "q25", "q50", "q75", "count", "null_percentage",
]


def fmt(value) -> str:
    if value is None:
        return "–"
    if isinstance(value, float):
        if not math.isfinite(value):
            return "–"
        return f"{value:,.2f}"
    text = str(value)
    return text if len(text) <= 60 else text[:57] + "..."


def filter_num(value) -> str:
    if value is None:
        return "–"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return "–"
    if not math.isfinite(number):
        return "–"
    if number.is_integer():
        return f"{int(number):,}"
    return f"{number:,.2f}"


def filter_md(value) -> str:
    if value is None:
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def load_descriptions() -> dict:
    if not DESCRIPTIONS_FILE.exists():
        return {}
    with open(DESCRIPTIONS_FILE, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_relationships() -> dict:
    if not RELATIONSHIPS_FILE.exists():
        return {}
    with open(RELATIONSHIPS_FILE, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def quote_ident(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


def get_tables(con) -> list:
    rows = con.execute(
        "SELECT table_schema, table_name, table_type FROM information_schema.tables "
        "WHERE table_schema NOT IN ('information_schema') "
        "ORDER BY table_schema, table_name"
    ).fetchall()
    return [(schema, name, table_type) for schema, name, table_type in rows]


def kind_for(name: str) -> str:
    """View-like objects are identifiable only by name: in AdventureWorks the
    v* tables (e.g. vEmployee, vPersonDemographics) are views. DuckDB cannot
    tell: the CSV mirror imported every object as a physical BASE TABLE."""
    return "view" if re.match(r"^v[A-Z]", name) else "table"


def build_key_map(relationships: dict) -> tuple[dict, dict, dict]:
    """Return (key_map, referenced_by, fk_by_table)."""
    tables_meta = (relationships.get("tables") or {})
    fk_by_table = {}
    referenced_by: dict[str, list] = {}

    for table, meta in tables_meta.items():
        fks = [
            SimpleNamespace(**fk)
            for fk in (meta or {}).get("foreign_keys", [])
        ]
        fk_by_table[table] = {"foreign_keys": fks, "primary_key": (meta or {}).get("primary_key", [])}
        for fk in fks:
            ref = fk.ref_table
            referenced_by.setdefault(ref, []).append(SimpleNamespace(table=table, column=fk.column))

    key_map = {}
    for table, meta in fk_by_table.items():
        roles = {}
        for pk_col in meta["primary_key"]:
            roles[pk_col] = "PK"
        for fk in meta["foreign_keys"]:
            roles[fk.column] = "PK,FK" if fk.column in roles else "FK"
        key_map[table] = roles

    return key_map, referenced_by, fk_by_table


def analyze_table(con, schema: str, table: str, kind: str, descriptions: dict, relationships: dict) -> dict:
    qualified = f"{quote_ident(schema)}.{quote_ident(table)}"
    key = f"{schema}.{table}"

    meta = (descriptions.get(key) or {})
    keys_mapping = relationships["key_map"].get(key, {})
    rels = relationships["fk_by_table"].get(key, {"foreign_keys": [], "primary_key": []})

    columns = []
    describe = con.execute(f"DESCRIBE {qualified}").fetchall()
    types = {row[0]: row[1] for row in describe}

    row_count = con.execute(f"SELECT COUNT(*) FROM {qualified}").fetchone()[0]
    col_count = len(describe)

    summarize = con.execute(f"SUMMARIZE {qualified}").fetchall()
    col_descs = meta.get("columns") or {}

    for row in summarize:
        stats = dict(zip(SUMMARIZE_FIELDS, row))
        col = stats["column_name"]
        null_pct = stats["null_percentage"]
        col_type = types.get(col, stats["column_type"])
        columns.append(SimpleNamespace(
            name=col,
            type=col_type,
            numeric=col_type.upper().startswith(
                ("TINYINT", "SMALLINT", "INTEGER", "BIGINT", "HUGEINT",
                 "DECIMAL", "NUMERIC", "FLOAT", "DOUBLE", "REAL")
            ),
            count=stats["count"],
            null_pct=round(null_pct, 1) if null_pct is not None else None,
            approx_unique=stats["approx_unique"],
            min=fmt(stats["min"]),
            max=fmt(stats["max"]),
            avg=stats["avg"],
            std=stats["std"],
            q25=fmt(stats["q25"]),
            q50=stats["q50"],
            q75=fmt(stats["q75"]),
            key=keys_mapping.get(col, ""),
            desc=col_descs.get(col),
        ))

    return {
        "schema": schema,
        "name": table,
        "kind": kind,
        "row_count": row_count,
        "column_count": col_count,
        "domain": meta.get("domain"),
        "primary_key": rels["primary_key"],
        "foreign_keys": rels["foreign_keys"],
        "referenced_by": relationships["referenced_by"].get(key, []),
        "tags": meta.get("tags", []),
        "keywords": meta.get("keywords", []),
        "questions": meta.get("questions", []),
        "description": meta.get("description"),
        "columns": columns,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    env = Environment(loader=FileSystemLoader(str(ROOT / "templates")))
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.filters["num"] = filter_num
    env.filters["md"] = filter_md
    template = env.get_template(TEMPLATE)

    descriptions = load_descriptions()
    relationships = load_relationships()
    key_map, referenced_by, fk_by_table = build_key_map(relationships)
    relationships["key_map"] = key_map
    relationships["referenced_by"] = referenced_by
    relationships["fk_by_table"] = fk_by_table

    con = duckdb.connect(str(DB_PATH), read_only=True)

    tables = get_tables(con)
    written = 0
    for schema, table, table_type in tables:
        info = analyze_table(con, schema, table, kind_for(table), descriptions, relationships)
        target = OUT_DIR / f"{schema}.{table}.md"
        target.write_text(template.render(table=info), encoding="utf-8")
        written += 1
        print(f"  {schema}.{table}.md  ({info['row_count']} rows)")

    con.close()
    print(f"\nDone. {written} table docs written to {OUT_DIR}")


if __name__ == "__main__":
    main()