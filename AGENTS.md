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

Scripts live in `scripts\`, grouped by pipeline stage, and are always run from
the repo root (`scripts\<stage>\<file>.py` resolve
`ROOT = Path(__file__).resolve().parents[2]`; `scripts\pipeline.py` uses
`parents[1]`).

```
scripts/pipeline.py                    # ONE-COMMAND pipeline: everything after the CSV ingest
scripts/ingest/extract_adventureworks.py   # prerequisite (once): GitHub CSV -> DuckDB
scripts/ingest/fetch_relationships.py      # prerequisite (once): CTU MariaDB PK/FK -> docs/relationships.yaml
scripts/docs/generate_table_docs.py        # DuckDB -> one .md file per table (docs/tables/)
scripts/docs/generate_index.py             # descriptions.yaml -> docs/index.md (domain-grouped index)
scripts/docs/enrich_descriptions.py        # local LLM (LM Studio) -> docs/descriptions.yaml
scripts/docs/check_docs.py                 # validation of generated docs (6 checks, exit code)
scripts/rag/bm25.py                        # BM25 retrieval over docs/tables/*.md (top-5)
scripts/rag/ask.py                         # QA loop: BM25 top-5 -> local LLM grounded answer
data/adventureworks.duckdb  # DuckDB database (gitignored)
data/bm25_index.json        # cached BM25 index (gitignored, auto-rebuilt on .md change)
data/raw/adventureworks/    # downloaded CSV cache (gitignored)
docs/tables/                # generated per-table markdown docs
docs/index.md               # domain-grouped index of the table docs (generated)
docs/descriptions.yaml      # human metadata (table/column descriptions)
docs/relationships.yaml     # PK/FK relationships (from CTU, AW2014)
templates/table.md.j2       # Jinja2 template for table docs
progress.md                 # session-by-session progress log (always consult!)
AGENTS.md                   # this file
```

## Commands

```powershell
# ONE-COMMAND pipeline (everything after the CSV ingest; see pipeline notes below)
.\.venv\Scripts\python.exe scripts\pipeline.py
#   --full                  describe all 91 tables with the LLM (1-2h+)
#   --limit N               max tables described this run (default 5)
#   --force-enrich          re-describe already-described tables (to see the LLM work)
#   --force-human           ... and also hand-edited (source: human) entries
#   --skip-enrich           reuse docs/descriptions.yaml, no LLM call (fully offline)
#   --clean                 delete docs/tables/*.md + docs/index.md first
#   --demo-question [Q]     finish with an ask.py Q&A (default question if omitted)
#   --dry-run               print the stage plan and exit
.\.venv\Scripts\python.exe scripts\pipeline.py --skip-enrich
.\.venv\Scripts\python.exe scripts\pipeline.py --full
.\.venv\Scripts\python.exe scripts\pipeline.py --demo-question

# run the DB build pipeline (idempotent, caches CSVs locally)
.\.venv\Scripts\python.exe scripts\ingest\extract_adventureworks.py

# ad-hoc query
.\.venv\Scripts\python.exe -c "import duckdb; c=duckdb.connect(r'data\adventureworks.duckdb', read_only=True); print(c.execute('SELECT COUNT(*) FROM \"Production\".\"Product\"').fetchall())"

# regenerate per-table markdown docs
.\.venv\Scripts\python.exe scripts\docs\generate_table_docs.py

# regenerate docs/index.md (domain-grouped table index)
.\.venv\Scripts\python.exe scripts\docs\generate_index.py

# re-fetch PK/FK relationships from CTU MariaDB (see version caveat below)
.\.venv\Scripts\python.exe scripts\ingest\fetch_relationships.py

# describe undocumented tables via local LLM (LM Studio, default model = google/gemma-4-e4b)
#   optional single table:      python scripts/docs/enrich_descriptions.py "Person.Address"
#   optional batch limit:       python scripts/docs/enrich_descriptions.py --limit 20
#   rebuild only AW views (v*): python scripts/docs/enrich_descriptions.py --views
#   force rebuild all entries:  python scripts/docs/enrich_descriptions.py --force
#   stale entries (columns changed/removed, old column referenced) are
#   regenerated automatically thanks to the stored columns_snapshot.
#   hand-edited entries (source: human) are NEVER overwritten — not by --force,
#   --views or a drift rebuild — unless --force-human is passed.
.\.venv\Scripts\python.exe scripts\docs\enrich_descriptions.py

# validate the generated docs (exit code 0 = all good)
.\.venv\Scripts\python.exe scripts\docs\check_docs.py

# BM25 retrieval over docs/tables/*.md (index auto-rebuilds when a .md changes)
.\.venv\Scripts\python.exe scripts\rag\bm25.py "how many vacation hours does an employee have"
#   --top 10     more results          --build     rebuild index and exit
.\.venv\Scripts\python.exe scripts\rag\bm25.py --top 10 "product list price by vendor"

# QA loop: BM25 top-5 -> local LLM grounded answer (streams; may take minutes)
.\.venv\Scripts\python.exe scripts\rag\ask.py "combien d'unités en stock pour chaque produit ?"
#   --top 10       more context        --model <m>  pick another model
```

## Version caveat for relationships

CTU publishes AdventureWorks **2014** OLTP only. Our CSV dump is AW **2019**.
The 71 base tables match 1:1 by name (the extra 20 tables in our DB are views,
which CTU excludes), so the FK graph is considered accurate but may miss
2019-only changes. Re-run `fetch_relationships.py` after any DB refresh.

## Pipeline notes (`scripts\pipeline.py`)

- The two `scripts/ingest/` scripts are **one-off prerequisites, not stages**:
  `extract_adventureworks.py` builds `data/adventureworks.duckdb`, and
  `fetch_relationships.py` builds `docs/relationships.yaml` from CTU MariaDB.
  Both outputs are committed, so `pipeline.py` never hits the network except
  the local LLM.
- `generate_table_docs.py` runs **twice on purpose**: `enrich_descriptions.py`
  parses the generated `docs/tables/*.md`, so the docs must then be re-rendered
  to carry the new descriptions / domain / keywords / questions.
- `--limit` counts *files taken from the sorted doc list*, and already-described
  tables are skipped, not described. On a repo where `docs/descriptions.yaml` is
  already complete, a plain run enriches **nothing** — pass `--force-enrich`
  (with `--limit 3`) to actually watch the LLM work.
- Each stage runs as a **subprocess** of `sys.executable`, so every DuckDB
  connection is released on stage exit (no single-process lock across stages)
  and stage output streams live.
- **Hand-edited descriptions are protected**: `source: human` entries in
  `docs/descriptions.yaml` are never replaced by the LLM — not by `--force`,
  `--views`, or a `columns_snapshot` drift rebuild. `--force-human` overrides.
  Note that on Windows `sorted()` is case-insensitive, so `dbo.*` comes first:
  `--force-enrich --limit 5` targets `dbo.AWBuildVersion`, `dbo.DatabaseLog`,
  `dbo.ErrorLog` (the human-marked ones) before any LLM entry.

## Conventions / gotchas

- Tables are schema-qualified, e.g. `Production.Product`, `Person.Person`.
  Always quote identifiers: `"Production"."Product"`.
- Schema-less CSV dumps (`AWBuildVersion`, `DatabaseLog`, `ErrorLog`) live in `dbo`.
- **kind field (view vs table)**: front matter carries `kind: view` for AW view
  objects (v* naming convention). DuckDB cannot distinguish them — the CSV
  mirror imports every object as a physical BASE TABLE — so view-ness is derived
  from the name (`^v[A-Z]`), consistent in generate_table_docs.py and check_docs.py.
  View descriptions and docs carry an explicit "read-only view" note.
- **DuckDB is single-process**: only one process may open the DB file at a time.
  Close the DuckDB CLI (or any connection) before running scripts — otherwise
  scripts fail with "file already open in ..." (file lock on Windows).
- **gemma-4-e4b reasons by default** and burns the whole `max_tokens` budget on
  reasoning (returns nothing). `enrich_descriptions.py` already sends
  `"reasoning_effort": "none"`; if the UI is used, set per-model
  Reasoning → Enable Thinking = Off.
- Never commit `.venv\`, `data\`, or `__pycache__\`.
- Windows / PowerShell host: use quoted paths and `.\.venv\Scripts\python.exe`.