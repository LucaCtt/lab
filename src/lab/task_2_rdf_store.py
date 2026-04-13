"""
Task 2: Local RDF Store with rdflib
======================================
Goal: instead of discarding Wikidata results after each query, persist them
into a local RDF graph. Then query the local graph with SPARQL — no network
needed after the initial fetch.

This simulates a lightweight knowledge base that grows as you ask questions.

Pipeline:
   question -> generate_sparql() -> query_wikidata()
            -> store_results()   -> sparql_local() -> verbalize() -> answer()

You will reuse generate_sparql(), query_wikidata(), verbalize(), and
answer_with_context() from Task 1. Import them here rather than copying.

Instructions
------------
1. Complete the three TODO functions: store_results(), sparql_local(), ask().
2. Run ask() for at least two questions and verify the graph grows.
3. After loading a few questions, run sparql_local() with a hand-written query
   to confirm the data is really stored locally.
"""

from rdflib import Graph


def fetch_and_store(sparql: str, graph: Graph) -> None: ...  # TODO

def sparql_local(graph: Graph, query: str) -> list[dict]: ...  # TODO

def ask(question: str, graph: Graph) -> str: ...  # TODO

if __name__ == "__main__":
    g = Graph()
    q1 = "What is the capital of France?"
    q2 = "Who is the president of the United States?"
    print(ask(q1, g))
    print(ask(q2, g))