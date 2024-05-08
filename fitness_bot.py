import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("GOOGLE_GEMINIAPI")

# Configure the API
genai.configure(api_key=API_KEY)

# Create the GenerativeModel instance
model = genai.GenerativeModel(model_name="gemini-pro")

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>Personal Fitness Bot 🤖</h1>", unsafe_allow_html=True)
st.caption("🚀 A fitness personal chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "human", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate content
    try:
        msg = model.generate_content(prompt).text
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    except Exception as e:
        st.error(f"Error generating content: {str(e)}")
