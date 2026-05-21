
import streamlit as st
from langchain_groq import ChatGroq

# load env variables


# streamlit page setup
st.set_page_config(
    page_title="Generative AI ChatBot",
    page_icon="📥",
    layout="centered",
)

st.title("🤖CHOTU")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# show old chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):#with:Every thing belong to that chat bubbal
        st.markdown(message["content"])

# initialize LLM
llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)
# user input
user_prompt = st.chat_input("Ask a question")

if user_prompt:# runs only user enter something

    # show user message
    st.chat_message("user").markdown(user_prompt)# disply user message instantly

    # save user message
    st.session_state.chat_history.append({"role": "user", "content": user_prompt}
    )

    # generate response
    # invoke :send request to model
    response = llm.invoke(
        input=[{"role":"system","content":"you are a helpful assistant"},*st.session_state.chat_history
    ])#* unpack list items

    assistant_response = response.content

    # save assistant response
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )
    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
