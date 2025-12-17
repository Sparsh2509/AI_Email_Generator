import streamlit as st
from google import genai

# 🔐 API key yahin daalo
client = genai.Client(api_key="YOUR_API_KEY_HERE")

st.title("📧 AI Email Generator")

topic = st.text_input("Enter email topic")
tone = st.selectbox("Select tone", ["Formal", "Angry", "Friendly"])

if st.button("Generate Email"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        prompt = f"""
        Write an email on the topic: {topic}.
        Tone: {tone}.
        Keep it clear and well structured.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        st.subheader("Generated Email")
        st.write(response.text)
