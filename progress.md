# progress.md — Progress Log

Source of truth. Read before coding, append after every task. Entries are
timestamped with date + time.

---

## 2026-09-20 19:30 — Project bootstrap + AdventureWorks → DuckDB

### Done
- Initialized git repo, created project skeleton.
- Created venv at `.venv\` (Python 3.14.6, via `py -3.14`).
- Installed `duckdb==1.5.5`. `pandas` intentionally skipped (DuckDB reads CSVs directly).
- Wrote `extract_adventureworks.py`:
  - Fetches CSV manifest (91 files) from `olafusimichael/AdventureWorksCSV` (GitHub, `main`).
  - Caches CSVs in `data/raw/adventureworks\` (idempotent re-runs).
  - Loads each CSV into `data/adventureworks.duckdb`, schema-qualified
    (`"Production"."Product"`, bare dumps → `dbo`).
- Ran pipeline successfully: **91 tables / 804,801 rows** loaded; verified with
  ad-hoc queries against `Production.Product`, `Person.Person`, etc.

### Decided
- AdventureWorks source = CSV mirror `olafusimichael/AdventureWorksCSV`.
  (PyPI package `adventureworks` + repo `NickLumley/adventureworks_python_duckdb`
  are gone — removed / 404 — do not retry.)
- DuckDB DB lives at `data/adventureworks.duckdb`, kept out of git.

### Next
- Define chunking strategy for RAG (per-table row → text chunk? entity docs?).
- Add embeddings + vector storage (duckdb vss? / external vector store).
- Build retrieval + QA loop over the AW data.

---

## 2026-09-20 ~19:45 — Per-table Markdown docs generator

### Done
- Installed `jinja2==3.1.6`, `pyyaml==6.0.3` into venv. Stack section in AGENTS.md updated.
- Created `generate_table_docs.py`:
  - Reads every table from `data/adventureworks.duckdb` (read-only, 91 tables).
  - Per table: metric = row count (`COUNT(*)`), column count, per-column
    stats via DuckDB `SUMMARIZE` (type, non-null count, null %, approximate
    distinct, min/max/avg/std/median).
  - Renders `templates/table.md.j2` (Jinja2) → `docs/tables/<Schema>.<Table>.md`.
- Created `docs/descriptions.yaml`: seeded human descriptions for
  `Person.Address`, `Production.Product`, `Sales.SalesOrderHeader`
  (table + key columns). Script merges these when present; otherwise the docs
  say "no description provided".
- Template/script are written but NOT executed yet — blocked by the DuckDB
  file lock (user had the CLID open). Need to run and verify.

### Decided
- Column/stats analysis approach = DuckDB `SUMMARIZE` (no pandas needed).
- Descriptions live as human-maintained YAML (the CSV dump has no column
  comments, so there's nothing to extract from the DB itself).

### Next
1. Close DuckDB CLI → run `generate_table_docs.py` → verify `.md` output.
2. Decide RAG chunking strategy (rows → chunks? table docs as context?).

---

## 2026-09-20 ~20:10 — New doc template + PK/FK relationships from CTU

### Done
- Applied the user's proposed `templates/table.md.j2`:
  - YAML front matter (table, schema, domain, rows, primary_key, tags, documented).
  - Columns table with **Key** role (PK / FK), null %, approx distinct, description.
  - **Relationships** section: outgoing FKs + "referenced by" (inverse index, auto-computed).
  - **Numeric statistics** section gated on numeric column types (`selectattr("numeric")`.
  - Keywords / Typical questions sections (opt-in via `docs/descriptions.yaml`).
- Added Jinja2 filters `num` + `md` in `generate_table_docs.py`;
  columns are now `SimpleNamespace` so `selectattr` works.
- **`fetch_relationships.py`** (new): pulls PK/FK from CTU public MariaDB
  (`relational.fel.cvut.cz:3306`, db `AdventureWorks2014`, guest/ctu-relational),
  maps table names 1:1 onto our DuckDB, writes **`docs/relationships.yaml`**:
  **71 tables, 71 with PK, 91 FK links** (including composite keys).
- Installed `pymysql==1.2.3`. Stack + layout + commands + version-caveat
  section added to AGENTS.md.
- Generador re-ran: **91 .md files** under `docs/tables\`, verified
  `Person.Address.md` and `Sales.SalesOrderHeader.md`.

### Decided (important caveat)
- **CTU only hosts AdventureWorks 2014**, not 2019. We used 2014:
  base-table set is identical to our 2019 set (71 vs 91 = +20 views),
  so relationships are considered accurate, but 2019-only FK changes
  would be missed. Noted in AGENTS.md ("Version caveat for relationships").

### Next
- Populate `docs/descriptions.yaml` with `domain`, `tags`, `keywords`,
  `questions` for each table (currently only 3 tables seeded).
- Decide RAG chunking strategy (rows → chunks? table docs as context?).

---

## 2026-09-20 ~20:25 — `check_docs.py` validation script

### Done
- Added `check_docs.py` with the 4 requested checks:
  1. `.md` file count == number of tables in DuckDB.
  2. YAML front matter of every `.md` parses cleanly (`yaml.safe_load`).
  3. Every table cited in `docs/relationships.yaml` (tables keys + all
     `ref_table` targets) has a `.md` file.
  4. No stray `None` / `nan` literals anywhere in the generated docs.
- Exit code 0 = all good, 1 = at least one check failed (each failing
  check lists the offending files). Added to AGENTS.md (layout + commands).

### Result
- First run: **all 4 checks PASS** on the 91 generated docs.

### Next
- Seed `docs/descriptions.yaml` (domain/tags/keywords/questions) for all tables.
- Define RAG chunking strategy & retrieval layer.