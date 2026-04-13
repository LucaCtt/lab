"""
Task 4: RAG Agent with Tool Calling
======================================
Goal: wrap the three retrieval strategies from Task 3 as LLM tools and let the
model decide which one (or which combination) to use for each question.

The model will:
  1. Receive a question.
  2. Choose a retrieval tool (or multiple).
  3. Use the tool output as context.
  4. Produce a grounded final answer.

You can refere to example_2_function_calls.py for a template on how to implement tool calling with litellm.

Instructions
------------
1. Complete the three tool wrapper functions.
2. Complete run_agent() following the pattern in example_2_function_calls.py.
3. Test with at least three questions and observe which tool(s) the model picks.

"""

from rdflib import Graph
from lab.task_3_hybrid_retrieval import (
    retrieve_sparql,
    retrieve_text,
    retrieve_embedding,
)

functions = {
    "sparql_retrieve": retrieve_sparql,
    "text_retrieve": retrieve_text,
    "embedding_retrieve": retrieve_embedding,
}


def run_agent(question: str, graph: Graph) -> str: ...  # TODO


if __name__ == "__main__":
    graph = Graph()
    # Optionally pre-populate the graph with some data here.
    question = "How many F1 championships has Lewis Hamilton won?"
    answer = run_agent(question, graph)
    print(f"Question: {question}\nAnswer: {answer}")
