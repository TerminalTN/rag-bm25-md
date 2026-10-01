"""
End-to-end RAG documentation pipeline: everything after the AdventureWorks
CSV ingest, in one command.

Stages, in order:
  0. preflight              DuckDB + relationships.yaml present, LM Studio up
  1. generate_table_docs    DuckDB + relationships -> docs/tables/*.md
  2. enrich_descriptions    local LLM -> docs/descriptions.yaml (--limit N, default 5)
  3. generate_table_docs    again, so the enriched metadata lands in the .md files
  4. generate_index         descriptions.yaml -> docs/index.md
  5. check_docs             validation gate (non-zero exit stops the pipeline)
  6. bm25 --build           retrieval index over docs/tables/*.md
  7. ask.py <question>      optional streamed Q&A over the built index

Doc generation runs TWICE on purpose: enrich_descriptions.py parses the
generated docs/tables/*.md, and those same docs must then be re-rendered to
carry the new descriptions, domains, keywords and questions. Hand-edited
descriptions (source: human) are never overwritten by the enrichment stage
unless --force-human is passed.

Not part of this pipeline (both are one-off prerequisites, committed to git,
in scripts/00_ingest/):
  - 01_extract_adventureworks.py  (CSV dump -> data/adventureworks.duckdb)
  - 02_fetch_relationships.py     (CTU MariaDB -> docs/relationships.yaml)
The pipeline therefore never touches the network except the local LLM.

The stage scripts are numbered in workflow order under scripts/:
  00_ingest/  one-off prerequisites
  01_docs/    01 generate -> 02 enrich -> (01 again) -> 03 index -> 04 check
  02_rag/     bm25.py (retrieval library) + ask.py (QA loop)

Usage:
    python scripts/pipeline.py                             # 5 tables enriched, then index + checks + bm25
    python scripts/pipeline.py --full                      # enrich all 91 tables (1-2h+ on a local LLM)
    python scripts/pipeline.py --skip-enrich               # reuse docs/descriptions.yaml as-is (fastest)
    python scripts/pipeline.py --clean                     # delete generated docs first (visible rebuild)
    python scripts/pipeline.py --force-enrich --limit 3    # re-describe 3 tables live with the LLM
    python scripts/pipeline.py --force-enrich --force-human  # ... including hand-edited (source: human) entries
    python scripts/pipeline.py --demo-question             # end with a streamed grounded answer
    python scripts/pipeline.py --demo-question "combien d'unites en stock par produit ?"
    python scripts/pipeline.py --dry-run                   # print the plan, run nothing
"""

import argparse
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "adventureworks.duckdb"
RELATIONSHIPS_FILE = ROOT / "docs" / "relationships.yaml"
DESCRIPTIONS_FILE = ROOT / "docs" / "descriptions.yaml"
TABLES_DIR = ROOT / "docs" / "tables"
INDEX_FILE = ROOT / "docs" / "index.md"

DOCS_SCRIPT = "scripts/01_docs/01_generate_table_docs.py"
ENRICH_SCRIPT = "scripts/01_docs/02_enrich_descriptions.py"
INDEX_SCRIPT = "scripts/01_docs/03_generate_index.py"
CHECK_SCRIPT = "scripts/01_docs/04_check_docs.py"
BM25_SCRIPT = "scripts/02_rag/bm25.py"
ASK_SCRIPT = "scripts/02_rag/ask.py"

LLM_BASE_FALLBACK = "http://127.0.0.1:1234"
DEFAULT_LIMIT = 5
DEFAULT_DEMO_QUESTION = "combien d'unités en stock pour chaque produit ?"

results: list[tuple[str, bool, float]] = []


def llm_base() -> str:
    """Base URL of the local LLM server, read from enrich_descriptions.py so the
    preflight probe cannot drift from the URL the stages actually call."""
    src = (ROOT / ENRICH_SCRIPT).read_text(encoding="utf-8")
    match = re.search(r'LLM_URL\s*=\s*"([^"]+)"', src)
    url = match.group(1) if match else LLM_BASE_FALLBACK
    return url.split("/v1/")[0]


def preflight(needs_llm: bool) -> list[str]:
    errors = []
    if not DB_PATH.exists():
        errors.append(
            f"missing database {DB_PATH} - run scripts/00_ingest/01_extract_adventureworks.py once"
        )
    if not RELATIONSHIPS_FILE.exists():
        errors.append(
            f"missing {RELATIONSHIPS_FILE} - run scripts/00_ingest/02_fetch_relationships.py once (needs network)"
        )
    if needs_llm:
        url = f"{llm_base()}/v1/models"
        try:
            with urllib.request.urlopen(url, timeout=5) as resp:
                resp.read(1)
        except (urllib.error.URLError, OSError, TimeoutError) as exc:
            errors.append(
                f"local LLM not reachable at {url} ({exc}) - start LM Studio and load a model, "
                f"or re-run with --skip-enrich"
            )
    return errors


def clean() -> None:
    removed = 0
    for md in TABLES_DIR.glob("*.md"):
        md.unlink()
        removed += 1
    if INDEX_FILE.exists():
        INDEX_FILE.unlink()
        removed += 1
    print(f"Removed {removed} generated file(s) ({TABLES_DIR.name}/*.md, {INDEX_FILE.name}).")
    print(f"Kept {RELATIONSHIPS_FILE.name} and {DESCRIPTIONS_FILE.name} (expensive inputs).")


def run_stage(name: str, script: str, args: list[str]) -> bool:
    cmd = f"python {script}" + (f" {' '.join(args)}" if args else "")
    print(f"\n{'=' * 70}\n== {name}\n$ {cmd}\n{'=' * 70}", flush=True)
    start = time.perf_counter()
    code = subprocess.call([sys.executable, str(ROOT / script), *args], cwd=str(ROOT))
    elapsed = time.perf_counter() - start
    ok = code == 0
    results.append((name, ok, elapsed))
    print(f"\n-- {name}: {'OK' if ok else f'FAILED (exit {code})'} in {elapsed:.1f}s", flush=True)
    return ok


def print_summary() -> None:
    total = sum(elapsed for _, _, elapsed in results)
    print(f"\n{'=' * 70}\nPIPELINE SUMMARY ({len(results)} stages, {total:.1f}s total)")
    for name, ok, elapsed in results:
        print(f"  [{'ok' if ok else 'FAILED':6}] {name} ({elapsed:.1f}s)")
    docs = len(list(TABLES_DIR.glob("*.md")))
    print(f"  docs/tables: {docs} files | index: {'yes' if INDEX_FILE.exists() else 'no'}")
    print(f"{'=' * 70}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build the whole AdventureWorks RAG doc set from the DuckDB database."
    )
    parser.add_argument(
        "--limit", type=int, default=DEFAULT_LIMIT,
        help=f"max tables to describe with the LLM this run (default {DEFAULT_LIMIT})",
    )
    parser.add_argument(
        "--full", action="store_true",
        help="describe every table (no --limit); slow: 91 LLM calls",
    )
    parser.add_argument(
        "--force-enrich", action="store_true",
        help="pass --force so already-described tables are re-described (needed to see the LLM work live)",
    )
    parser.add_argument(
        "--force-human", action="store_true",
        help="also re-describe hand-edited entries (source: human); they are protected by default",
    )
    parser.add_argument(
        "--skip-enrich", action="store_true",
        help=f"reuse {DESCRIPTIONS_FILE.name} as-is (no LLM call)",
    )
    parser.add_argument(
        "--clean", action="store_true",
        help="delete docs/tables/*.md and docs/index.md before generating (keeps the YAML metadata)",
    )
    parser.add_argument(
        "--demo-question", nargs="?", const=DEFAULT_DEMO_QUESTION, metavar="QUESTION",
        help=f"finish with an ask.py Q&A (default question: {DEFAULT_DEMO_QUESTION!r})",
    )
    parser.add_argument("--dry-run", action="store_true", help="print the plan and exit")
    args = parser.parse_args()

    limit: int | None = None if args.full else args.limit
    if args.full and args.limit != DEFAULT_LIMIT:
        print("note: --full wins over --limit")

    stages: list[tuple[str, str, list[str]]] = []
    enrich_args: list[str] = []
    if not args.skip_enrich:
        if limit:
            enrich_args += ["--limit", str(limit)]
        if args.force_enrich:
            enrich_args.append("--force")
        if args.force_human:
            enrich_args.append("--force-human")
        label = "enrich descriptions (all tables)" if limit is None else f"enrich descriptions (limit {limit})"
        stages.append((label, ENRICH_SCRIPT, enrich_args))
    stages += [
        ("generate table docs", DOCS_SCRIPT, []),
        ("generate table docs (with enriched metadata)", DOCS_SCRIPT, []),
        ("generate docs/index.md", INDEX_SCRIPT, []),
        ("validate docs (6 checks)", CHECK_SCRIPT, []),
        ("build BM25 index", BM25_SCRIPT, ["--build"]),
    ]
    if args.demo_question:
        stages.append(("demo question (ask.py)", ASK_SCRIPT, [args.demo_question]))

    needs_llm = not args.skip_enrich or bool(args.demo_question)
    if args.dry_run:
        print(f"DRY RUN - {len(stages)} stages" + (f", clean={args.clean}" if args.clean else ""))
        for name, script, stage_args in stages:
            cmd = f"python {script}" + (f" {' '.join(stage_args)}" if stage_args else "")
            print(f"  {name}\n    $ {cmd}")
        return 0

    if args.clean:
        print("\n-- clean: removing generated docs")
        clean()

    errors = preflight(needs_llm)
    if errors:
        print("\nPREFLIGHT FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("Preflight OK (database, relationships metadata"
          f"{', local LLM' if needs_llm else ''}).")

    for name, script, stage_args in stages:
        if not run_stage(name, script, stage_args):
            print_summary()
            print(
                f"\nPipeline stopped at stage '{name}'.\n"
                f"If this is a DuckDB error, close any open duckdb.exe / GUI connection "
                f"(single-process lock) and re-run."
            )
            return 1

    print_summary()
    print(f"\nDone. Ask a question with: python {ASK_SCRIPT} \"your question\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
