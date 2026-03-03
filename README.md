# 📧 AI Email Copilot using RAG

An AI-powered Email Generator built using **Retrieval-Augmented Generation (RAG)**.  
This system generates context-aware professional emails using semantic search over email templates.

Live Demo: https://your-streamlit-link.streamlit.app  

---

## 🚀 Features

- ✉ Generate professional emails (Cold Email, Internship Request, Follow-up, Apology, Sales Outreach)
- 🧠 Context-aware generation using RAG
- 🔎 Semantic template retrieval using FAISS
- 🤗 HuggingFace embeddings (all-MiniLM-L6-v2)
- ⚡ Gemini 2.5 Flash Lite for generation
- 🎛 Interactive Streamlit UI
- ☁ Deployed on Streamlit Cloud

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
├── streamlit_app.py
├── app.py
├── rag/
│   ├── build_vectorstore.py
│   ├── retriever.py
│
├── prompts/
│   ├── email_prompt.py
│
├── Email_Templates_idea/
│
├── faiss_index/
├── requirements.txt
└── README.md
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

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI_Email_Generator_Using_Rag.git
cd AI_Email_Generator_Using_Rag
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 🔐 Environment Variables

For deployment (Streamlit Cloud), add secret:

```
GEMINI_API_KEY = "your_api_key_here"
```

---

## 📌 Resume Description

> Built a context-aware AI Email Copilot using Retrieval-Augmented Generation (RAG) with FAISS and HuggingFace embeddings, integrated with Gemini 2.5 for structured professional email generation. Deployed using Streamlit Cloud.

---

## 🎯 Future Improvements

- Metadata-based smart retrieval
- Hybrid search (semantic + keyword)
- Email history memory
- PDF resume-based email generation
- Agentic workflow

---

## 📄 License

MIT License