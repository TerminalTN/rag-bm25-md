"""
BM25 retrieval over the per-table markdown docs (docs/tables/*.md).

What is indexed: the 91 full {table}.md files (columns, relationships,
description, keywords, questions) — NOT docs/index.md (that one is a human
summary).

Build: tokenize every .md file and store term frequencies, doc lengths,
avg doc length and per-term document frequencies. The index is cached in
data/bm25_index.json and rebuilt automatically whenever a .md file changes
(compared via size + mtime signature).

Query: tokenize the question, score every indexed doc with Okapi BM25
(k1 = 1.5, b = 0.75), return the top-n (default 5) docs.

Usage:
    python scripts/rag/bm25.py                # build / refresh the index explicitly
    python scripts/rag/bm25.py "question..."  # retrieve top-5
    python scripts/rag/bm25.py --top 10 "question..."
"""

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLES_DIR = ROOT / "docs" / "tables"
INDEX_FILE = ROOT / "data" / "bm25_index.json"

K1 = 1.5
B = 0.75
TOP_N = 5

CAMEL_ACRONYM = re.compile(r"([A-Z]+)(?=[A-Z][a-z])")
CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
WORD = re.compile(r"[a-zà-ÿ0-9]+")


def tokenize(text: str) -> list[str]:
    """Mail: split camelCase/acronym boundaries, lowercase, keep word chars
    (letters incl. accents + digits), drop punctuation and single chars."""
    text = CAMEL_ACRONYM.sub(r"\1 ", text)
    text = CAMEL_BOUNDARY.sub(" ", text)
    text = text.lower()
    return [tok for tok in WORD.findall(text) if len(tok) >= 2]


def files_signature(directory: Path) -> dict:
    return {
        path.name: [path.stat().st_size, path.stat().st_mtime_ns]
        for path in sorted(directory.glob("*.md"))
    }


class BM25Index:
    def __init__(self):
        self.doc_keys: list[str] = []
        self.doc_freqs: dict[str, dict[str, int]] = {}  # doc key -> {term: count}
        self.doc_lengths: dict[str, int] = {}            # doc key -> token count
        self.doc_frequency: dict[str, int] = {}          # term -> #docs containing it
        self.avgdl = 0.0
        self.signature: dict = {}
        self.total = 0

    def build(self, docs: dict[str, str]) -> None:
        self.doc_keys = list(docs)
        lengths: dict[str, int] = {}
        freq: dict[str, dict[str, int]] = {}
        df: dict[str, int] = {}

        for key, text in docs.items():
            tokens = tokenize(text)
            lengths[key] = len(tokens)
            counter: dict[str, int] = {}
            for tok in tokens:
                counter[tok] = counter.get(tok, 0) + 1
            freq[key] = counter
            for tok in counter:
                df[tok] = df.get(tok, 0) + 1

        if not lengths:
            self.avgdl = 0.0
        else:
            self.avgdl = sum(lengths.values()) / len(lengths)

        self.doc_freqs = freq
        self.doc_lengths = lengths
        self.doc_frequency = df
        self.total = sum(df.values())

    def idf(self, term: str) -> float:
        n = self.doc_frequency.get(term, 0)
        return math.log(1.0 + (len(self.doc_keys) - n + 0.5) / (n + 0.5))

    def score(self, doc_key: str, query_tokens: list[str]) -> float:
        length = self.doc_lengths.get(doc_key, 0)
        if length == 0:
            return 0.0
        freqs = self.doc_freqs.get(doc_key, {})
        norm = 1.0 - B + B * length / self.avgdl
        total = 0.0
        for tok in query_tokens:
            f = freqs.get(tok, 0)
            if f == 0:
                continue
            total += self.idf(tok) * f * (K1 + 1) / (f + K1 * norm)
        return total

    def search(self, query: str, top_n: int = TOP_N) -> list[tuple[str, float]]:
        q_tokens = tokenize(query)
        if not q_tokens:
            return []
        scored = sorted(
            ((key, self.score(key, q_tokens)) for key in self.doc_keys),
            key=lambda kv: kv[1],
            reverse=True,
        )
        return [(key, round(s, 3)) for key, s in scored if s > 0][:top_n]

    def save(self, path: Path) -> None:
        payload = {
            "params": {"k1": K1, "b": B},
            "avgdl": self.avgdl,
            "signature": files_signature(TABLES_DIR),
            "doc_keys": self.doc_keys,
            "doc_lengths": self.doc_lengths,
            "doc_frequencies": self.doc_freqs,
            "doc_frequency": self.doc_frequency,
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload), encoding="utf-8")

    def load(self, path: Path) -> bool:
        if not path.exists():
            return False
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("signature") != files_signature(TABLES_DIR):
            return False
        self.avgdl = payload["avgdl"]
        self.doc_keys = payload["doc_keys"]
        self.doc_lengths = payload["doc_lengths"]
        self.doc_freqs = payload["doc_frequencies"]
        self.doc_frequency = payload["doc_frequency"]
        self.total = sum(self.doc_frequency.values())
        return True


def build_index(docs: dict[str, str]) -> BM25Index:
    index = BM25Index()
    index.build(docs)
    index.save(INDEX_FILE)
    return index


def load_or_build() -> BM25Index:
    index = BM25Index()
    if index.load(INDEX_FILE):
        print(f"Loaded cached index from {INDEX_FILE}")
        return index
    docs = {p.stem: p.read_text(encoding="utf-8") for p in sorted(TABLES_DIR.glob("*.md"))}
    index = build_index(docs)
    print(f"Indexed {len(docs)} docs / {index.total} terms / avgdl={index.avgdl:.1f} -> {INDEX_FILE}")
    return index


def show_result(key: str, score: float) -> bytes:
    path = TABLES_DIR / f"{key}.md"
    text = path.read_text(encoding="utf-8")
    prefix = "No description"
    m = re.search(r"\n# .+?\n\n(.*?)(?=\n## )", text, re.S)
    if m:
        snippet = " ".join(line for line in m.group(1).splitlines() if not line.lstrip().startswith(">"))
        prefix = re.sub(r"\s+", " ", snippet).strip()[:160]
    return (f"  {key}  (score {score})\n  {path}\n  {prefix}\n".encode())


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="BM25 retrieval over the table docs")
    parser.add_argument("--top", type=int, default=TOP_N, help=f"number of results (default {TOP_N})")
    parser.add_argument("--build", action="store_true", help="rebuild the index and exit")
    parser.add_argument("query", nargs="?", help="user question")
    args = parser.parse_args(argv)

    index = load_or_build()
    if args.build:
        return 0
    if not args.query:
        print("Give a question as argument, or --build to refresh the index.")
        return 0

    results = index.search(args.query, top_n=args.top)
    out = f"\nTop {len(results)} results for: {args.query}\n\n".encode()
    sys.stdout.buffer.write(out)
    for key, score in results:
        sys.stdout.buffer.write(show_result(key, score))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))