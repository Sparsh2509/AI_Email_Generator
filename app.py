import streamlit as st
import google.generativeai as genai
import os

# API key environment variable se lena
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Email Generator", page_icon="📧")

st.title("📧 AI Email Generator")
st.write("Bas topic likho, email ready 🚀")

# User input
topic = st.text_input("Email kis topic par chahiye?")

if st.button("Generate Email"):
    if topic.strip() == "":
        st.warning("Topic likh bhai 😅")
    else:
        model = genai.GenerativeModel("gemini-pro")

        prompt = f"""
        Write a professional email on the topic: {topic}.
        Keep it clear and polite.
        """

        response = model.generate_content(prompt)

        st.subheader("✉️ Generated Email")
        st.write(response.text)
