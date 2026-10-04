import streamlit as st

from backend import chatbot
from langchain_core.messages import HumanMessage


CONFIG = {
    "configurable": {
        "thread_id": "thread-1"
    }
}


st.title("My AI Chatbot")


# Initialize chat history
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


# Display previous messages
for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Type here...")


if user_input:

    # Add user message
    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)


    # Get response from LangGraph
    response = chatbot.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config=CONFIG
    )


    ai_message = response["messages"][-1].content


    # Add AI response
    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })


    with st.chat_message("assistant"):
        st.write(ai_message)