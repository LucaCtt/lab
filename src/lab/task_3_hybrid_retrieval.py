"""
Task 3: Hybrid Retrieval over RDF store
====================================================
Goal: implement three different retrieval strategies over the local rdflib
graph built in Task 2, then compare their outputs for the same question.

Retrieval strategies
--------------------
A) SPARQL retrieval: precise, structured, requires well-formed query
B) Text retrieval: keyword/regex match over literal values (FILTER + REGEX)
C) Embedding retrieval: semantic similarity between question and stored labels

Instructions
------------
1. Populate the graph by running a few ask() calls from Task 2 first,
   or call populate_graph() below.
2. Complete retrieve_sparql(), retrieve_text(), retrieve_embedding().
3. Run compare() for at least two questions and note differences.

Note: Make sure to include clear docstrings describing their purpose and expected input/output,
as you will use these functions as tools in the next task.

"""

from rdflib import Graph


def retrieve_sparql(graph: Graph, query: str) -> str: ...  # TODO


def retrieve_text(graph: Graph, keyword: str) -> str: ...  # TODO


def retrieve_embedding(graph: Graph, question: str) -> str: ...  # TODO
