import streamlit as st
import google.generativeai as genai
# from langchain import PromptTemplate, FewShotPromptTemplate
from dotenv import load_dotenv
load_dotenv()
import os




API_KEY = os.getenv("GOOGLE_GEMINI_API")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-pro")

# st.header("Personal Fitness Bot 🤖")

st.markdown("<h1 style='text-align: center;'>Personal Fitness Bot 🤖</h1>", unsafe_allow_html=True)
# st.markdown("<h5 style='text-align: center;'>🚀 A fitness personal chatbot</h5>", unsafe_allow_html=True)

st.caption("🚀 A fitness personal chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "human", "content": prompt})
    st.chat_message("user").write(prompt)
    print("prompt",st.session_state.messages)
    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = model.generate_content(prompt).text
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

