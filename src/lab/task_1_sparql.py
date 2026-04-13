"""
Task 1 — SPARQL-based RAG with Wikidata
========================================
Goal: build a minimal pipeline where the LLM generates a SPARQL query,
your code executes it on Wikidata, and the LLM answers using the results.

Pipeline:
    question -> generate_sparql() -> query_wikidata() -> verbalize() -> answer()

Instructions
------------
1. Choose a narrow topic (e.g. programming languages, F1, etc.).
   All your test questions should belong to that topic.
2. Complete the five TODO functions below.
3. Test with at least three different questions and print all intermediate steps.
"""


def query_wikidata(sparql: str) -> list[dict]: ...  # TODO


def verbalize(results: list[dict]) -> str: ...  # TODO


def generate_sparql(question: str) -> str: ...  # TODO


def answer(question: str, context: str) -> str: ...  # TODO


def ask(question: str): ...  # TODO


if __name__ == "__main__":
    ask("How many F1 championships has Lewis Hamilton won?")
