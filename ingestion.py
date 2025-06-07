from typing import List

from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/e5-small",  # or "all-MiniLM-L6-v2"
    encode_kwargs={"normalize_embeddings": True}
)

vector_dir = "./resources"

def ingest(web_urls: List):
    docs = [WebBaseLoader(urls).load() for urls in web_urls]

    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size = 250,
        chunk_overlap = 0,
    )

    doc_splits = text_splitter.split_documents(docs_list)
    vs = Chroma.from_documents(
        collection_name="demo_data",
        embedding=embeddings,
        persist_directory=vector_dir,
        documents=doc_splits,
    )


retriever = Chroma(
    collection_name = "demo_data",
    embedding_function=embeddings,
    persist_directory=vector_dir,
).as_retriever()


if __name__ == "__main__":
    web_urls = [
        "https://www.guvi.in/blog/40-java-interview-questions-for-freshers",
        "https://www.scholarhat.com/tutorial/java/java-interview-questions-and-answers",
        "https://arc.dev/talent-blog/java-interview-questions",
    ]
    #
    ingest(web_urls)
    res = retriever.invoke(
        input="What’s the difference between String, StringBuffer, and StringBuilder?"
    )
    print(res)