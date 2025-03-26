from __future__ import annotations
import os
import streamlit as st
from knowledge_base.vector_store import get_vector_store
from dotenv import load_dotenv
from query_generator import query_generator
from google import genai

load_dotenv()
API_KEY = os.getenv("API_KEY")


def main():
    st.title("PDF AI  RAG")
    st.write("Please upload a PDF file to get started.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)

    if uploaded_file is not None:
        file_id = uploaded_file.name  # Use filename as an identifier
        if "vector_store" not in st.session_state or st.session_state.get("file_id") != file_id:
            with st.spinner("Processing file..."):
                try:
                    vector_store = get_vector_store(uploaded_file.read())
                    st.session_state.vector_store = vector_store
                    st.session_state.file_id = file_id  # Store the file identifier
                    st.write("File processed successfully.")
                except Exception as e:
                    st.write("An error occurred while processing the file.")
                    st.write(e)

    try:
        client = genai.Client(api_key=API_KEY)
        llm_model_name = "gemini-2.0-flash"
        chat = client.chats.create(model=llm_model_name)
    except Exception as e:
        st.write("An error occurred while creating the chat.")
        st.write(e)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("What questions do you have about the uploaded PDF?")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            query = query_generator(user_input, st.session_state.vector_store)
            response = chat.send_message(query).text
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
