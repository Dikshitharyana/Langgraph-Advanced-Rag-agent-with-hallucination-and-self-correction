
from langgraph.constants import END
from langgraph.graph import StateGraph

from src.generate import generate_node
from src.grading import (
    grading_node,
    grade_conditional_node,
    grade_generation_grounded_in_documents_and_question,
)
from src.retriever import retriever_node
from src.constant import (
    RETRIEVER,
    GENERATE,
    WEBSEARCH,
    NOT_SUPPORTED,
    NOT_USEFUL,
    USEFUL,
    GRADE_DOCS
)

from src.state import GraphState
from src.websearch import websearch_node

workflow = StateGraph(GraphState)
workflow.add_node(RETRIEVER,retriever_node)
workflow.add_node(GRADE_DOCS,grading_node)
workflow.add_node(GENERATE,generate_node)
workflow.add_node(WEBSEARCH,websearch_node)

workflow.set_entry_point(RETRIEVER)
workflow.add_edge(RETRIEVER,GRADE_DOCS)
workflow.add_conditional_edges(
    GRADE_DOCS,
    grade_conditional_node,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

workflow.add_edge(WEBSEARCH,GENERATE)
# workflow.add_edge(GENERATE,END)

workflow.add_conditional_edges(
    GENERATE,
    grade_generation_grounded_in_documents_and_question,
    {NOT_SUPPORTED: GENERATE, NOT_USEFUL: WEBSEARCH, USEFUL:END}
)

graph = workflow.compile()

if __name__ == "__main__":
    res = graph.invoke(input={"question": "where is Taj Mahal Located"})
    print(res)