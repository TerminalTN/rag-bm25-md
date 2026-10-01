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

---

## 2026-09-21 20:40 — LLM enrichment of all table descriptions

### Done
- `enrich_descriptions.py` (new): for each table without a description in
  `docs/descriptions.yaml`, calls LM Studio (`http://127.0.0.1:1234`,
  local OpenAI-compatible server) to generate description / domain /
  keywords / questions as JSON.
- Prompt hardening:
  - Few-shot examples (SalesOrderHeader, Address, Product) anchored the
    format and bilingual keyword style.
  - Rules enforced in BOTH the system prompt and code via `validate()`:
    exactly 3 questions, >= 8 keywords, domain required, and every
    backticked name in the description must exist in the table's columns.
  - JSON is parsed (markdown fences tolerated) and validated before saving;
  - 3 attempts per table, transient HTTP errors retried.
- **`reasoning_effort: "none"` added to the request payload** — gemma-4-e4b
  reasons by default and burns max_tokens on thinking (returns nothing).
  That's a known LM Studio + Gemma-4-E4B issue (UI "Enable Thinking" toggle
  is unreliable for the E4B/E2B sizes; API param works). Documented in AGENTS.md.
- Incremental save: `descriptions.yaml` is rewritten after every successful
  table, so a long batch can be interrupted/resumed safely.
- Runs executed in 3 chunks (30-min tool caps) → **91/91 tables described,
  0 failures**. Then `generate_table_docs.py` re-run + `check_docs.py`:
  **all 4 checks PASS**, e.g. Sales.Customer.md now shows description,
  domain, keywords, and "Typical questions".

### Next
- Define RAG chunking strategy & retrieval layer (embeddings, vector store,
  QA loop). Possibly commit the enriched docs.

---

## 2026-09-21 ~21:00 — Schema-drift handling in enrichment

### Done
- You were right: the old check ("has a description?") ignores schema changes.
  Added staleness detection to `enrich_descriptions.py`:
  - Every generated entry now stores **`columns_snapshot`** (sorted column list).
  - On re-run, entries whose snapshot != current columns are **REBUILT**
    (prints `REBUILD (schema change)`).
  - Older/human entries without a snapshot are kept UNLESS their description
    references a now-missing column (backtick check) → rebuilt.
  - `--force` flag rebuilds everything regardless (also documented in AGENTS.md).
- Fixed a parsing bug discovered while testing: the column list regex also
  matched the "Numeric statistics" table rows (duplicate columns in the
  snapshot). Column parsing is now scoped to the "## Columns" section only.
- Verified: normal run skips cleanly (1 skipped, 0 rebuilt), `--force` rebuilds,
  drift detector returns correct reasons for removed column / stale reference.

### Next
- RAG: chunking strategy, embeddings + vector store, retrieval + QA loop.

---

## 2026-09-21 ~22:15 — Views now explicit (kind field + read-only note)

### Done
- View descriptions did NOT mention they were views. Fixed via discussion:
  - **`generate_table_docs.py`**: front matter now carries `kind: view|table`.
    Detection is by name convention `^v[A-Z]` — NOT the DuckDB catalog:
    `duckdb_views()` shows zero user views and all 91 objects are physical
    BASE TABLES (CSV mirror materializes views as tables). AGENTS.md gotcha
    updated accordingly.
  - **Template**: view docs render a "View (AdventureWorks)" blockquote note
    explaining it's a read-only projection in the source, imported as a table.
  - **`enrich_descriptions.py`**: `build_prompt` now adds a view hint telling
    the model to say explicitly that it's a view; new `--views` flag rebuilds
    only the 20 v* tables.
  - **`check_docs.py`**: new check 5 — front-matter `kind` matches the v* rule.
- Rebuilt all 20 view descriptions (`--views`): every description now starts
  with "A read-only view over ...". Re-generated docs. All 5 checks PASS.

### Notes / gotchas hit
- First `--views` run failed with WinError 10061: LM Studio was not running.
  Existing entries were preserved (no data loss) — re-ran after starting LM
  Studio, 20/20 OK.
- Transient `DLL load failed (application control policy blocked)` on duckdb
  import — resolved on retry; not reproducible.
- DuckDB was locked by `duckdb.exe` (PID 12496) as expected; closed before re-run.

### Next
- Commit this phase (lang: "views explicit").
- RAG: chunking strategy, embeddings + vector store, retrieval + QA loop.

---

## 2026-09-21 ~23:00 — docs/index.md (domain-grouped index)

### Done
- **`generate_index.py`**: reads `docs/descriptions.yaml`, groups tables by
  `domain` (lowercased, sorted), takes the first sentence of each description,
  writes `docs/index.md` at the docs root (links `tables/<name>.md`).
- **`check_docs.py`**: new check 6 — index lists every documented table exactly
  once, links resolve, no missing/unexpected tables. 6/6 PASS.
- Data fixes in descriptions.yaml:
  - Seeded entries had no `domain`: Person.Address→person,
    Production.Product→production, Sales.SalesOrderHeader→sales.
  - HumanResources.Employee had mis-cased `HumanResources` → human-resources.
  - **LLM had mislabeled the dbo tables**: DatabaseLog/ErrorLog→`person`,
    AWBuildVersion→`production`. Reclassified to `system` and marked
    `source: human` (they're database-internals objects, not business domains).
- Dropped the auto-"..." suffix: index shows the first sentence only
  (Person.AddressType no longer shows a dangling ellipsis).

### Next
- Commit this phase (index + kind + drift handling), then RAG chunking strategy,
  embeddings + vector store, retrieval + QA loop.

---

## 2026-09-22 ~00:10 — BM25 retrieval step

### Done
- **`bm25.py`**: Okapi BM25 (k1=1.5, b=0.75) retrieval over the 91 full
  `docs/tables/*.md` files — NOT docs/index.md (that stays a human summary).
  - Tokenizer: splits camelCase / acronym boundaries (`SalesOrderHeader` ->
    `sales order header`), lowercases, keeps letters (incl. accents) + digits,
    drops punctuation and single-char tokens.
  - Build: per-doc term frequencies, doc lengths, avg doc length, term doc
    frequency; cached to `data/bm25_index.json` with a size+mtime signature of
    the .md files → auto-rebuilds whenever a .md changes.
  - Query: tokenizes only the question, scores every doc, returns top-5
    (`--top N` to change, `--build` to force rebuild).
- Verified: cache round-trip fix (JSON turns tuples into lists — signature now
  uses lists), snippet extraction (skip the view blockquote note). Sample
  queries rank correctly:
  - "how many vacation hours does an employee have" → HumanResources.Employee
  - "product list price and standard cost" → Production.Product, *ListPriceHistory, *CostHistory
  - "when was a purchase order approved" → Purchasing.PurchaseOrder*
  - "shipping address of a customer in a city" → v*WithAddresses + Person.Address

### Next
- Commit this phase. Then: retrieval unit check / QA loop on top of BM25
  (LLM answer grounded on the top-5 docs), later optional embeddings.

---

## 2026-09-22 ~00:40 — ask.py (BM25 -> local LLM QA loop)

### Done
- **`ask.py`**: retrieves top-5 via bm25.py, builds a grounded prompt
  (question + up to 3000 chars of each doc), calls LM Studio
  `google/gemma-4-e4b` (system prompt: answer ONLY from context, answer in the
  question's language, cite Sources, say when info is not in docs).
  Options: `--top N`, `--model <m>`.
- Non-streaming first version repeatedly hit the 300s total timeout
  (5-doc prompts are slow on local gemma-4-e4b). Switched to **streaming**
  (`stream: true`, SSE parsing): tokens appear as generated, and urllib only
  times out per-read, so long generations no longer die.
- Verified: French question "combien d'unités en stock pour chaque produit ?"
  -> French answer, correctly grounded on Production.ProductInventory
  (Quantity per product, location). English questions also work.

### Next
- Commit this phase. Consider: `--top` quality tuning, grounding-answer
  evaluation, later optional embeddings (nomic-embed + vector store).

---

## 2026-10-01 22:29 — Scripts reorganised into `scripts/` (by pipeline stage)

### Done
- The 8 Python scripts no longer live at the repo root; they are grouped by
  pipeline stage (git history preserved via `git mv` for the 6 tracked ones):
  ```
  scripts/ingest/extract_adventureworks.py   GitHub CSV -> DuckDB
  scripts/ingest/fetch_relationships.py      CTU MariaDB PK/FK -> docs/relationships.yaml
  scripts/docs/generate_table_docs.py        DuckDB -> docs/tables/*.md
  scripts/docs/generate_index.py             descriptions.yaml -> docs/index.md
  scripts/docs/enrich_descriptions.py        local LLM -> docs/descriptions.yaml
  scripts/docs/check_docs.py                 doc validation (6 checks)
  scripts/rag/bm25.py                        BM25 retrieval over docs/tables/*.md
  scripts/rag/ask.py                         BM25 -> local LLM QA loop
  ```
- Every script resolved repo paths as `Path(__file__).resolve().parent`, which
  broke at depth 2 — all 8 now use `parents[2]` (repo root), so scripts are
  still run from the repo root. `ask.py` keeps working with its plain
  `import bm25` (same directory on `sys.path`).
- Usage docstrings updated to the new paths (`python scripts/<stage>/<file>.py`),
  and AGENTS.md Layout + Commands sections rewritten.
- Verified after the move: `generate_table_docs.py` (91 docs),
  `generate_index.py` (91 tables, 6 domains), `check_docs.py` **6/6 PASS**,
  `bm25.py` (index rebuilt, correct hits, accented query tokens fine),
  `ask.py --help` (import chain OK), `py_compile` on the 3 non-executed scripts.

### Gotcha hit (Windows PowerShell 5.1)
- Rewriting docstrings with `Set-Content -Encoding UTF8` **corrupted every
  non-ASCII character**: files were read back as ANSI (cp1252) and re-written as
  UTF-8, so em dashes became `â€"` and — worse — the BM25 tokenizer regex
  `r"[a-zà-ÿ0-9]+"` became `r"[a-zÃ -Ã¿0-9]+"` (accented letters would have
  been silently dropped). A BOM was also added to all 8 files.
  Both were repaired (cp1252 round-trip inverse, BOM stripped, LF endings
  preserved) and verified byte-wise. **Rule for this repo: never use
  `Set-Content`/`Get-Content` for editing source files — use the Edit tool or a
  Python script with explicit `encoding="utf-8"`.**

### Next
- Commit this phase (includes the uncommitted views/index/BM25/ask work).
- RAG: chunking strategy, embeddings + vector store, retrieval quality tuning.

---

## 2026-10-01 22:45 — Repo published on GitHub + one-command pipeline

### Done — GitHub
- Published the project as **public** repo `TerminalTN/rag-bm25-md`
  (https://github.com/TerminalTN/rag-bm25-md), created empty by the user.
- Local branch `master` renamed to `main` (matches the GitHub default).
- `origin` = `https://TerminalTN@github.com/TerminalTN/rag-bm25-md.git` — the
  username is in the URL **on purpose**: Git Credential Manager keys stored
  credentials per URL, and the machine already had a token stored for
  `https://github.com` belonging to a **different account** (`veritasflux`).
  With the username in the URL, GCM asks for a separate TerminalTN login.
- Pushed 3 commits (`8707324` + the two foundation commits). `data/`, `.venv/`,
  `__pycache__/` stayed ignored.

### Done — `scripts/pipeline.py` (one-command workflow, for the video)
- Orchestrates **everything after the CSV ingest** as subprocesses of the
  existing stage scripts (each keeps its own DuckDB connection lifetime, so the
  single-process file lock can't bite across stages; output streams live).
  Stages: preflight → enrich → generate_table_docs → **generate_table_docs
  again** → index → check_docs (gate) → `bm25 --build` → optional `ask.py` demo.
- Why doc generation runs **twice**: `enrich_descriptions.py` *parses*
  `docs/tables/*.md` (it has no DuckDB access), so the docs must be re-rendered
  to carry the new descriptions/domains/keywords/questions.
- `fetch_relationships.py` is **not** a stage: `docs/relationships.yaml` is
  committed, so the pipeline is offline (no network except the local LLM).
  Preflight fails with an explicit hint if that YAML is ever missing.
- Preflight: DB file exists, relationships YAML exists, and (when the LLM is
  needed) `GET {LLM_BASE}/v1/models` answers. The base URL is parsed out of
  `enrich_descriptions.py` at runtime so the probe can't drift from the real
  endpoint.
- Flags: `--limit N` (default **5** tables), `--full` (all 91, 1-2h+),
  `--force-enrich` (re-describe already-described tables — needed to *see* the
  LLM work live), `--skip-enrich` (offline), `--clean` (delete generated docs
  first, keeping the expensive YAML), `--demo-question [Q]`, `--dry-run`.
- Ends with a per-stage timing summary; on failure it stops at that stage and
  prints the DuckDB single-process-lock hint.

### Verified
- `--dry-run` (both default and `--full --demo-question`) prints the right plan.
- `--skip-enrich` full run: 91 docs regenerated, index (91 tables / 6 domains),
  **6/6 checks PASS**, BM25 index rebuilt — **~13s total**.
- `--clean --skip-enrich`: removed 92 generated files, rebuilt them
  **byte-identical** to what is committed (`git status` clean) → the pipeline is
  deterministic and re-runnable.
- Preflight guard: with LM Studio down it exits 1 with an actionable message.
- The LLM stages (`enrich`, `--demo-question`) are **untested** — LM Studio was
  not running during this session.

### Done — human-edited descriptions are now protected
- Found a real data-loss hazard: `enrich_descriptions.py` replaced the whole
  entry dict (`output[key] = entry`) for anything it re-described, so
  `source: human` entries were destroyed by `--force`, by `--views`, and by a
  `columns_snapshot` drift rebuild. On Windows `sorted()` is case-insensitive,
  so `dbo.AWBuildVersion` / `dbo.DatabaseLog` / `dbo.ErrorLog` — the three
  hand-edited entries — are the **first three** files any `--limit N` run
  touches. A `--force-enrich --limit 5` demo run would have wiped them.
- Added `is_human(meta)` + the guard in `enrich_descriptions.py`, checked
  **before** the drift check so every re-description path is covered:
  `source: human` → `SKIP (source=human, hand-edited; --force-human to
  override)`, counted as skipped. New flag `--force-human` overrides it.
  `pipeline.py --force-human` passes it through.
- Verified all five paths (LM Studio was up, so the override test really did
  call the model — `dbo.AWBuildVersion` was restored from git afterwards):
  - `--limit 3` → 3 human skipped, no LLM call
  - `--force --limit 3` → still 3 human skipped (the point of the guard)
  - `--force --force-human --limit 1` → REBUILD (forced), entry replaced
  - `--views` with `HumanResources.vEmployee` temporarily marked human → skipped,
    other 19 views rebuilt
  - stale `columns_snapshot` on human `dbo.ErrorLog` → still skipped
- Also confirmed a no-op enrichment run rewrites `descriptions.yaml`
  **byte-identically** (no reformatting churn). After restoring,
  `generate_table_docs.py` + `generate_index.py` + `check_docs.py` → **6/6 PASS**,
  `git status` clean: the 3 human entries are intact.

### Next
- Test the LLM path once LM Studio is up: `--force-enrich --limit 1`, then
  `--demo-question`.
- Add a `README.md` (the repo currently has only `AGENTS.md`).
- Commit + push this phase.
