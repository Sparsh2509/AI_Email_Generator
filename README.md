# 📧 AI Email Copilot using RAG

An AI-powered Email Generator built using **Retrieval-Augmented Generation (RAG)**.  
This system generates context-aware professional emails using semantic search over email templates.

Live Demo: [https://aiemailgeneratorusingrag-lfcvucjigqzpjmza3ruhhg.streamlit.app/](https://aiemailgeneratorusingrag-lfcvucjigqzpjmza3ruhhg.streamlit.app/) 

---

## 🚀 Features

- Generate professional emails (Cold Email, Internship Request, Follow-up, Apology, Sales Outreach)
- Context-aware generation using RAG
- Semantic template retrieval using FAISS
- HuggingFace embeddings (all-MiniLM-L6-v2)
- Gemini 2.5 Flash Lite for generation
- Interactive Streamlit UI
- Deployed on Streamlit Cloud

---

## 🏗 Architecture

User Input  
↓  
Generate Semantic Query  
↓  
HuggingFace Embeddings  
↓  
FAISS Vector Search  
↓  
Retrieve Top-K Templates  
↓  
Inject Context into Prompt  
↓  
Gemini LLM Generates Email  

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- HuggingFace Embeddings
- FAISS Vector Database
- Google Gemini API
- dotenv

---

## 📂 Project Structure


```
AI_Email_Generator/
│
├── streamlit_app.py            # Streamlit UI for generating emails using Gemini API
├── app.py                      # CLI-based email generation interface
│
├── rag/
│   ├── build_vectorstore.py    # Creates hugging face embeddings and builds FAISS vector index
│   ├── retriever.py            # Retrieves top relevant email templates using semantic search
│
├── prompts/
│   ├── email_prompt.py         # Builds structured prompt using user input + retrieved context to 
│                               # controlled and formatted LLM output
│
├── Email_Templates_idea/       # Collection of sample email templates for RAG knowledge base
│
├── faiss_index/                # Stored FAISS vector database files
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## ⚙ How It Works

1. User enters:
   - Sender name
   - Recipient name
   - Company name
   - Purpose
   - Tone
   - Key points

2. System:
   - Converts query into embeddings
   - Retrieves similar email templates from FAISS
   - Injects context into structured prompt
   - Gemini generates final email

This ensures more structured and consistent output compared to plain prompt-based generation.

---

## 🧪 Run Locally

### Clone Repository

```bash
git clone https://github.com/Sparsh2509/AI_Email_Generator_Using_Rag.git
cd AI_Email_Generator_Using_Rag
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


### Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---




