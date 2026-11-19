import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.title("Funny AI Chatbot")


@st.cache_resource
def get_model():
    return init_chat_model("groq:openai/gpt-oss-120b", temperature=0.9)


model = get_model()

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="you are a funny AI agent")]

# Show chat history (skip the system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)