import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

MODES = {
    "😡 Angry Mode": "You are an angry AI agent. You respond aggressively and impatiently.",
    "😂 Funny Mode": "You are a very funny AI agent. You respond with humor and jokes.",
    "😢 Very Sad Mode": "You are a very sad AI agent. You respond in a gloomy, sorrowful and melancholic way.",
}


@st.cache_resource
def get_model():
    return init_chat_model("groq:openai/gpt-oss-120b", temperature=0.9)


model = get_model()

st.title("AI Chatbot")

# Step 1: choose the mode
if "messages" not in st.session_state:
    st.subheader("Choose your AI mode")
    for label, system_prompt in MODES.items():
        if st.button(label, use_container_width=True):
            st.session_state.mode = label
            st.session_state.messages = [SystemMessage(content=system_prompt)]
            st.rerun()
    st.stop()

# Step 2: chat
st.caption(f"Mode: {st.session_state.mode}")

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