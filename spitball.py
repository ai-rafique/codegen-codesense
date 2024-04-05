import ollama
import streamlit as st


def model_chunk__generation(model):
    stream = ollama.chat(
        model=model,
        messages=st.session_state["messages"],
        stream=True
    )
    for chunk in stream:
        yield chunk["message"]["content"]