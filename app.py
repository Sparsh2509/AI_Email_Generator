import streamlit as st
from google import genai

# 🔐 API key
client = genai.Client(api_key="AIzaSyDNWRFn9t9i7gs9E_coVkPFa4p2hafVx-w")

import streamlit as st
from google import genai

# 🔐 API key
client = genai.Client(api_key="AIzaSyDNWRFn9t9i7gs9E_coVkPFa4p2hafVx-w")

st.title("📧 AI Email Generator")

topic = st.text_input("Enter email topic")
tone = st.selectbox("Select tone", ["Formal", "Angry", "Friendly"])

if st.button("Generate Email"):
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        prompt = f"Write an email on the topic: {topic}. Tone: {tone}. Keep it clear and well structured."

        # ✅ Pass contents as a string, not a dict
        response = client.models.generate_content(
            model="models/gemini-2.5-flash-lite",
            contents=prompt
        )

        st.subheader("Generated Email")

        # ✅ Access content correctly
        st.write(response.text)