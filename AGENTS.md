# AGENTS.md — Project Guide

RAG project over AdventureWorks (2019 OLTP) data, stored in DuckDB.

## Non-negotiable workflow rule

- **ALWAYS read `progress.md` before writing any code** — it is the source of truth
  for what has been done, what was set up, and what is next.
- **Review for staleness.** If `progress.md` does not match the current state of the
  repo or the last session's outcome, update it (fix it) before proceeding.
- After every task, **append to `progress.md`**: a timestamped entry (with date/time)
  stating what was done, what was decided, and what's next.
- If you add/remove any dependency or change the stack, also update the stack section
  below the same session.

## Stack

| Component  | Version              | Notes                                                              |
|------------|----------------------|--------------------------------------------------------------------|
| Python     | 3.14.6               | via `py -3.14` launcher (Windows). `python` is NOT on PATH.        |
| venv       | `.venv\`             | activate with `.\.venv\Scripts\Activate.ps1` or call `.venv\Scripts\python.exe` directly |
| duckdb     | 1.5.5                | Python client, pip-installed                                       |
| jinja2     | 3.1.6                | Markdown doc generation (templates\table.md.j2)                    |
| pyyaml     | 6.0.3                | docs\descriptions.yaml metadata                                    |
| pymysql    | 1.2.3                | fetch_relationships.py (CTU MariaDB)                                |
| pandas     | not installed        | (was skipped — duckdb reads CSVs directly)                         |
| AdventureWorks source | `olafusimichael/AdventureWorksCSV` (GitHub, branch `main`) | Full CSV dump of AW2019 OLTP (91 tables) |
| Relationships source | CTU relational repo, MariaDB `AdventureWorks2014` (relational.fel.cvut.cz, guest/ctu-relational) | PK/FK from AW **2014** — base tables match our 2019 set 1:1 by name |
| DB file    | `data/adventureworks.duckdb` | 91 tables, ~804,801 rows, kept out of git |

Previous attempt (do not retry): the PyPI package `adventureworks` and the upstream
repo `NickLumley/adventureworks_python_duckdb` no longer exist (removed / 404), so we
use the CSV mirror above.

## Layout

```
extract_adventureworks.py   # pipeline: GitHub CSV -> DuckDB
generate_table_docs.py      # DuckDB -> one .md file per table (docs/tables/)
fetch_relationships.py      # CTU MariaDB PK/FK -> docs/relationships.yaml
check_docs.py               # validation of generated docs (4 checks, exit code)
data/adventureworks.duckdb  # DuckDB database (gitignored)
data/raw/adventureworks/    # downloaded CSV cache (gitignored)
docs/tables/                # generated per-table markdown docs
docs/descriptions.yaml      # human metadata (table/column descriptions)
docs/relationships.yaml     # PK/FK relationships (from CTU, AW2014)
templates/table.md.j2       # Jinja2 template for table docs
progress.md                 # session-by-session progress log (always consult!)
AGENTS.md                   # this file
```

## Commands

```powershell
# run the DB build pipeline (idempotent, caches CSVs locally)
.\.venv\Scripts\python.exe extract_adventureworks.py

# ad-hoc query
.\.venv\Scripts\python.exe -c "import duckdb; c=duckdb.connect(r'data\adventureworks.duckdb', read_only=True); print(c.execute('SELECT COUNT(*) FROM \"Production\".\"Product\"').fetchall())"

# regenerate per-table markdown docs
.\.venv\Scripts\python.exe generate_table_docs.py

# re-fetch PK/FK relationships from CTU MariaDB (see version caveat below)
.\.venv\Scripts\python.exe fetch_relationships.py

# validate the generated docs (exit code 0 = all good)
.\.venv\Scripts\python.exe check_docs.py
```

## Version caveat for relationships

CTU publishes AdventureWorks **2014** OLTP only. Our CSV dump is AW **2019**.
The 71 base tables match 1:1 by name (the extra 20 tables in our DB are views,
which CTU excludes), so the FK graph is considered accurate but may miss
2019-only changes. Re-run `fetch_relationships.py` after any DB refresh.

## Conventions / gotchas

- Tables are schema-qualified, e.g. `Production.Product`, `Person.Person`.
  Always quote identifiers: `"Production"."Product"`.
- Schema-less CSV dumps (`AWBuildVersion`, `DatabaseLog`, `ErrorLog`) live in `dbo`.
- **DuckDB is single-process**: only one process may open the DB file at a time.
  Close the DuckDB CLI (or any connection) before running scripts — otherwise
  scripts fail with "file already open in ..." (file lock on Windows).
- Never commit `.venv\`, `data\`, or `__pycache__\`.
- Windows / PowerShell host: use quoted paths and `.\.venv\Scripts\python.exe`.