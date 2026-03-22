import os
import streamlit as st
from dotenv import load_dotenv
from rag.retriever import retrieve_context
from prompts.email_prompt import build_email_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not gemini_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
    api_key=gemini_key
)

st.set_page_config(page_title="AI Email Copilot", page_icon="📧")
st.title("📧 AI Email Copilot (RAG Powered)")
st.write("Generate professional emails using Retrieval-Augmented Generation.")

with st.form("email_form"):
    sender = st.text_input("Sender Name")
    recipient = st.text_input("Recipient Name")
    company = st.text_input("Company Name")
    purpose = st.selectbox("Purpose", ["cold email", "internship request", "follow up", "apology", "sales outreach"])
    tone = st.selectbox("Tone", ["professional", "friendly", "persuasive", "formal", "confident"])
    length = st.selectbox("Length", ["short", "medium", "long"])
    key_points = st.text_area("Key Points (Write bullet points, one per line)")
    submit_button = st.form_submit_button("Generate Email")

if submit_button:

    if not sender or not recipient or not company:
        st.warning("Please fill all required fields.")
        st.stop()

    if not key_points.strip():
        key_points = "No specific key points provided. Write a general email."

    with st.spinner("Retrieving context and generating email..."):

        # ✅ Fix 1 — same retriever query as API
        context = retrieve_context(purpose)

        # ✅ Fix 2 — same argument order as API
        prompt = build_email_prompt(
            sender_name=sender,
            recipient_name=recipient,
            company_name=company,
            purpose=purpose,
            tone=tone,
            length=length,
            key_points=key_points,
            context=context
        )

        response = llm.invoke(prompt)

    st.success("Email Generated Successfully!")
    st.markdown("Generated Email")
    st.text_area("Output", response.content, height=400)