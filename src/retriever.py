#retriever
from typing import Dict, Any
from src.state import GraphState
from ingestion import retriever

def retriever_node(state:GraphState) -> Dict[str,Any]:
    print("Invoked::: retriever_node")
    question = state["question"]
    documents = retriever.invoke(question)
    return {"question":question,"documents":documents}