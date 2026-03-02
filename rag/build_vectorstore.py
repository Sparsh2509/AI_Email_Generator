import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def build_vectorstore():
    docs = []

    for file in os.listdir("Email_Templates_idea"):
        if file.endswith(".txt"):
            loader = TextLoader(f"Email_Templates_idea/{file}")
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="text-embedding-004"
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vectorstore = FAISS.from_documents(split_docs, embeddings)
    vectorstore.save_local("faiss_index")

if __name__ == "__main__":
    build_vectorstore()