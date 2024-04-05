import streamlit as st
from spitball import model_chunk__generation

st.title("Llama Codes Stuff")

# initialize history and use history of messages to render to screen
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# every message has a role(ai or user) and a content
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # collect user input and render the message
    # user prompts and assistant response
    # if block is no null, render
    # streamlit knows whether user or assistant/ai
    if prompt := st.chat_input("What do you need"):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt, unsafe_allow_html=True)

        with st.chat_message("user"):
            # now to allow ollama to response, steam false for waiting to get answer til block generated
            message = st.write_stream(model_chunk__generation("dolphincoder"))
            st.session_state["messages"].append({"role": "assistant", "content": message})
