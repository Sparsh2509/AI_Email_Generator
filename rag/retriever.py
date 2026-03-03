from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def retrieve_context(query: str) -> str:
    
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    docs = retriever.invoke(query)

    context_text = "\n\n".join([doc.page_content for doc in docs])

    return context_text