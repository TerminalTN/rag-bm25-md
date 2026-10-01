"""
Question-answering over the AdventureWorks docs using the local LLM.

Pipeline: BM25 retrieval (bm25.py) over the 91 table docs -> build a grounded
prompt with the top-5 documents -> local LLM (LM Studio, OpenAI-compatible
server) answers only from that context -> answer + used sources are printed.

Usage:
    python scripts/02_rag/ask.py "how many vacation hours does an employee have"
    python scripts/02_rag/ask.py --top 10 "list prices by product category"
    python scripts/02_rag/ask.py --model <model> "question"

Requires the LM Studio server to be running (http://127.0.0.1:1234).
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

import bm25

ROOT = Path(__file__).resolve().parents[2]
LLM_URL = "http://127.0.0.1:1234/v1/chat/completions"
LLM_MODEL = "google/gemma-4-e4b"
TIMEOUT = 600
MAX_TOKENS = 512
CONTEXT_CHARS = 3000

SYSTEM_PROMPT = (
    "You are a precise assistant for the AdventureWorks sample database. "
    "Answer ONLY using the documents provided by the user as context; each "
    "document describes one database table. If the context does not answer the "
    "question, say clearly that this information is not available in the docs. "
    "Base your answer on the table columns and descriptions found in the "
    "context. End your answer with a 'Sources:' line listing the table names "
    "you used, separated by commas. Answer in the same language as the "
    "question (a French question gets a French answer). Be concise."
)


def render_context(results: list[tuple[str, float]]) -> str:
    sections = []
    for key, score in results:
        path = bm25.TABLES_DIR / f"{key}.md"
        text = path.read_text(encoding="utf-8")
        sections.append(
            f"--- Document: {key} (BM25 score {score}) ---\n{text[:CONTEXT_CHARS]}"
        )
    return "\n\n".join(sections)


def stream_answer(prompt: str, model: str) -> None:
    """Stream the LLM answer to stdout as tokens arrive (no total timeout)."""
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": MAX_TOKENS,
        "reasoning_effort": "none",
        "stream": True,
    }
    req = urllib.request.Request(
        LLM_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    out = sys.stdout.buffer
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        for raw in resp:
            line = raw.decode("utf-8", errors="replace").strip()
            if not line.startswith("data:"):
                continue
            data = line[len("data:"):].strip()
            if not data or data == "[DONE]":
                continue
            chunk = json.loads(data)
            delta = chunk["choices"][0].get("delta", {})
            content = delta.get("content")
            if content:
                out.write(content.encode("utf-8"))
                out.flush()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Ask the local LLM over the AdventureWorks docs")
    parser.add_argument("--top", type=int, default=5, help="number of retrieved docs (default 5)")
    parser.add_argument("--model", default=LLM_MODEL, help=f"LM Studio model (default {LLM_MODEL})")
    parser.add_argument("query", nargs="?", help="your question")
    args = parser.parse_args(argv)

    if not args.query:
        print("Give a question as argument, e.g. python scripts/02_rag/ask.py \"why is... ?\"")
        return 0

    index = bm25.load_or_build()
    results = index.search(args.query, top_n=args.top)
    if not results:
        print("No relevant document found for this question.")
        return 1

    prompt = f"Question: {args.query}\n\nContext documents:\n{render_context(results)}"
    print(f"Question: {args.query}\n", flush=True)
    print(f"Using {len(results)} documents as context, querying {args.model} ...\n", flush=True)
    print("Answer:", flush=True)
    try:
        stream_answer(prompt, args.model)
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as exc:
        print(f"\nERROR: cannot reach LM Studio ({exc}). Is the server running?")
        return 1

    print("\n\nSources:", flush=True)
    for key, score in results:
        print(f"  - {key} (score {score})", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))