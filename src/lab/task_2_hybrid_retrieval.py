"""
Task 3: Hybrid Retrieval over RDF store
================================
Goal: implement three different retrieval strategies over the local rdflib
graph built in Task 2, then compare their outputs for the same question.

Retrieval strategies
---
A) SPARQL retrieval: precise, structured, requires well-formed query
B) Embedding retrieval: semantic similarity between question and stored labels

Instructions
---
1. Load the RDF graph you built in Task 2.
2. Complete retrieve_sparql(), retrieve_text(), retrieve_embedding().
3. Run compare() for at least two questions and note differences.

Note: Make sure to include clear docstrings describing their purpose and expected input/output,
as you will use these functions as tools in the next task.

"""

import math

from rdflib import Graph
from sentence_transformers import SentenceTransformer

from lab.task_1_sparql import answer  # reusing answer() from Task 1


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    """OPTIONAL. Compute cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def _get_embedding(text: str) -> list[float]:
    """OPTIONAL. Get an embedding vector for a text string via LiteLLM.

    Falls back to a zero-vector on failure (e.g. if the proxy has no embedding model).
    """
    embeddings_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )  # or any other model you prefer

    embeddings = embeddings_model.encode([text], show_progress_bar=False)
    return embeddings[0].tolist()


def retrieve_sparql(graph: Graph, query: str) -> str: ...  # TODO


def retrieve_text(graph: Graph, question: str) -> str: ...  # TODO


def retrieve_embedding(graph: Graph, question: str) -> str: ...  # OPTIONAL


def compare(graph: Graph, question: str) -> None:
    """Run all retrieval strategies on the same question and print results."""
    print(f"\n{'=' * 60}")
    print(f"QUESTION: {question}")
    print("=" * 60)

    for label, fn in [
        ("A) SPARQL retrieval", retrieve_sparql),
        ("B) Text retrieval", retrieve_text),
        # ("C) Embedding retrieval", retrieve_embedding),
    ]:
        print(f"\n--- {label} ---")
        try:
            context = fn(graph, question)
        except NotImplementedError:
            print("  [not implemented yet]")
            continue
        print(context or "  (no results)")

        print("\n[ANSWER]")
        print(answer(question, context))


if __name__ == "__main__":
    g = Graph()
    g.parse("local_graph.ttl", format="turtle")
