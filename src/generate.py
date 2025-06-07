from typing import Dict, Any
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_together import ChatTogether

from src.state import GraphState
from src.config import TOGETHER_API_KEY, TAVILY_API_KEY

prompt = hub.pull('rlm/rag-prompt')
llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    temperature= 0
)
generated_prompt_chain = prompt | llm | StrOutputParser()

#generate node
def generate_node(state: GraphState) -> Dict[str,Any]:
    print("Invoked :: generated_node")
    question = state["question"]
    documents = state["documents"]

    generation = generated_prompt_chain.invoke(
        {"context": documents, "question": question}
    )

    return {"documents": documents, "question": question, "generation" : generation}