import streamlit as st
from graph import graph

st.set_page_config(page_title="LangGraph Q&A App", page_icon="🧠", layout="centered")

st.title("🧠 LangGraph Q&A Workflow Demo")
st.markdown(
    """
    Ask any question and watch how the workflow processes your query using retrieval, grading, generation, and web search!
    """
)

# Sidebar for workflow explanation
with st.sidebar:
    st.header("Workflow Steps")
    st.markdown("""
    - **Retriever**: Finds relevant documents.
    - **Grader**: Assesses document usefulness.
    - **Web Search**: Looks up information if needed.
    - **Generator**: Creates the final answer.
    - **Conditional Logic**: Decides next steps based on grading.
    """)

# User input
user_question = st.text_input("Enter your question:", value="Where is Taj Mahal Located?")

if st.button("Ask"):
    with st.spinner("Processing..."):
        result = graph.invoke(input={"question": user_question})
    st.success("Here's the answer:")
    st.write(result)

    # Optionally, display the intermediate workflow state if available
    if hasattr(result, "dict"):
        st.subheader("Workflow State Details")
        st.json(result.dict())
    else:
        st.subheader("Raw Output")
        st.write(result)

st.markdown("---")
st.caption("Built with [Streamlit](https://streamlit.io/) and LangGraph 🚀")
