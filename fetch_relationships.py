"""
Fetch PK/FK relationships for AdventureWorks from the CTU relational
database repository and write them to docs/relationships.yaml.

Source: https://relational.fel.cvut.cz/dataset/AdventureWorks
Public MariaDB: relational.fel.cvut.cz:3306, db "AdventureWorks2014",
user guest / ctu-relational.

NOTE: CTU hosts the 2014 OLTP schema. Our DuckDB holds the 2019 OLTP
dump; the base-table sets match 1:1 (CTU's 71 base tables == our 71 base
tables; the extra 20 tables in our DB are views, which CTU excludes).
Column/table names are identical, but 2014 vs 2019 may differ in edge
cases — the mapping is reconciled against our DuckDB by name.

Usage:
    python fetch_relationships.py
"""

import pymysql
import yaml
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "adventureworks.duckdb"
OUT_FILE = ROOT / "docs" / "relationships.yaml"

CTU_HOST = "relational.fel.cvut.cz"
CTU_PORT = 3306
CTU_USER = "guest"
CTU_PASS = "ctu-relational"
CTU_DB = "AdventureWorks2014"


def fetch_constraints() -> dict:
    conn = pymysql.connect(
        host=CTU_HOST, port=CTU_PORT, user=CTU_USER,
        password=CTU_PASS, database=CTU_DB, connect_timeout=30,
    )
    cur = conn.cursor()

    cur.execute(
        "SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, "
        "REFERENCED_COLUMN_NAME, ORDINAL_POSITION FROM "
        "information_schema.KEY_COLUMN_USAGE "
        "WHERE constraint_schema = %s "
        "ORDER BY TABLE_NAME, CONSTRAINT_NAME, ORDINAL_POSITION",
        (CTU_DB,),
    )
    key_cols = cur.fetchall()

    cur.execute(
        "SELECT TABLE_NAME, CONSTRAINT_NAME, COLUMN_NAME, ORDINAL_POSITION "
        "FROM information_schema.KEY_COLUMN_USAGE "
        "WHERE constraint_schema = %s AND constraint_name = 'PRIMARY'",
        (CTU_DB,),
    )
    pk_cols = cur.fetchall()

    cur.execute(
        "SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.KEY_COLUMN_USAGE "
        "WHERE constraint_schema = %s AND constraint_name = 'UNIQUE'",
        (CTU_DB,),
    )
    unique_cols = cur.fetchall()

    conn.close()

    fk = {}
    for table, column, ref_table, ref_column, _pos in key_cols:
        if not ref_table:
            continue
        fk.setdefault(table, []).append({
            "column": column,
            "ref_table": ref_table,
            "ref_column": ref_column,
        })

    pk = {}
    for table, _cname, column, _pos in pk_cols:
        pk.setdefault(table, []).append(column)

    unique = {}
    for table, column in unique_cols:
        unique.setdefault(table, []).append(column)

    return {"pk": pk, "fk": fk, "unique": unique}


def map_to_ours(tables: dict) -> dict:
    con = duckdb.connect(str(DB_PATH), read_only=True)
    rows = con.execute(
        "SELECT table_schema, table_name FROM information_schema.tables "
        "WHERE table_schema NOT IN ('information_schema')"
    ).fetchall()
    con.close()

    match = {}
    for schema, table in rows:
        key = table
        if key not in match:
            match[key] = f"{schema}.{table}"
    return match


def main() -> None:
    print("Fetching constraints from CTU MariaDB...")
    raw = fetch_constraints()

    print("Mapping to our DuckDB (by table name)...")
    match = map_to_ours(raw)

    unknown_pk = set(raw["pk"]) - set(match)
    unknown_fk_tables = set(raw["fk"]) - set(match)
    unknown_fk_refs = {
        fk["ref_table"]
        for fks in raw["fk"].values()
        for fk in fks
        if fk["ref_table"] not in match
    }
    if unknown_pk or unknown_fk_tables or unknown_fk_refs:
        print("WARNING: tables not present in our DB:")
        for t in sorted(unknown_pk | unknown_fk_tables | unknown_fk_refs):
            print(f"  - {t}")

    tables = {}
    for base, cols in raw["pk"].items():
        key = match.get(base)
        if key:
            tables.setdefault(key, {})["primary_key"] = cols
    for base, fks in raw["fk"].items():
        key = match.get(base)
        if not key:
            continue
        entries = [
            {"column": fk["column"],
             "ref_table": match.get(fk["ref_table"], fk["ref_table"]),
             "ref_column": fk["ref_column"]}
            for fk in fks
            if fk["ref_table"] in match
        ]
        if entries:
            tables.setdefault(key, {})["foreign_keys"] = entries

    data = {
        "schema": "AdventureWorks2014 (CTU relational.fel.cvut.cz)",
        "target_schema": "AdventureWorks 2019 OLTP (our DuckDB)",
        "note": (
            "Relationships extracted from the CTU MariaDB copy of "
            "AdventureWorks2014 and mapped onto our 2019 tables by name. "
            "Base-table sets are 1:1 identical; values/edge cases may differ."
        ),
        "tables": dict(sorted(tables.items())),
    }

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True)
    n_pk = sum(1 for t in tables if "primary_key" in tables[t])
    n_fk = sum(len(t.get("foreign_keys", [])) for t in tables.values())
    print(f"Wrote {OUT_FILE}: {len(tables)} tables, {n_pk} with PK, {n_fk} FK links")


if __name__ == "__main__":
    main()