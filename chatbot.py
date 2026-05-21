import streamlit as st
from langchain_groq import ChatGroq

st.title("🤖 Chatbot")

api_key = st.secrets["GROQ_API_KEY"]

st.write(api_key[:10])   # temporary test

llm = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

user_input = st.chat_input("Ask something")

if user_input:
    response = llm.invoke(user_input)

    st.write(response.content)
