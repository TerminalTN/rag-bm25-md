"""
Extract AdventureWorks (2019 OLTP) data into DuckDB.

Data source: olafusimichael/AdventureWorksCSV on GitHub
(CSV dump of the AdventureWorks 2019 OLTP sample database).
Every table from the AdventureWorks DB is loaded into
data/adventureworks.duckdb, organised by schema (e.g. HumanResources.Employee).

Usage:
    python scripts/ingest/extract_adventureworks.py
"""

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import duckdb

REPO = "olafusimichael/AdventureWorksCSV"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"
API_CONTENTS = f"https://api.github.com/repos/{REPO}/contents/"

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw" / "adventureworks"
DB_PATH = DATA_DIR / "adventureworks.duckdb"


def fetch_json(url: str) -> list:
    req = urllib.request.Request(url, headers={"User-Agent": "opencode-rag"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def csv_manifest() -> list[str]:
    entries = fetch_json(API_CONTENTS)
    names = [e["name"] for e in entries if e["type"] == "file" and e["name"].lower().endswith(".csv")]
    return sorted(names)


def download(name: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 0:
        return False
    url = RAW_BASE + urllib.parse.quote(name)
    req = urllib.request.Request(url, headers={"User-Agent": "opencode-rag"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        dest.write_bytes(resp.read())
    return True


def schema_table(filename: str) -> tuple[str, str]:
    stem = filename[:-4]
    if " " in stem:
        schema, table = stem.split(" ", 1)
    else:
        schema, table = "dbo", stem
    return schema, table


def quote_ident(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Fetching CSV manifest from GitHub...")
    files = csv_manifest()
    print(f"Found {len(files)} CSV files.")

    downloaded = 0
    for name in files:
        if download(name, RAW_DIR / name):
            downloaded += 1
    print(f"Downloaded {downloaded} new files, {len(files) - downloaded} already cached.")

    con = duckdb.connect(str(DB_PATH))
    loaded = []
    for name in files:
        schema, table = schema_table(name)
        query = (
            f"CREATE SCHEMA IF NOT EXISTS {quote_ident(schema)}; "
            f"CREATE OR REPLACE TABLE {quote_ident(schema)}.{quote_ident(table)} AS "
            f"SELECT * FROM read_csv('{RAW_DIR / name}', header=true, sample_size=-1);"
        )
        con.execute(query)
        count = con.execute(
            f'SELECT COUNT(*) FROM {quote_ident(schema)}.{quote_ident(table)}'
        ).fetchone()[0]
        loaded.append((f"{schema}.{table}", count))
        print(f"  loaded {schema}.{table}: {count} rows")

    con.close()

    print(f"Done. Database written to {DB_PATH}")
    print(f"Loaded {len(loaded)} tables. Total rows: {sum(c for _, c in loaded)}")


if __name__ == "__main__":
    sys.exit(main())