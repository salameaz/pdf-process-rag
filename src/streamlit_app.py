from __future__ import annotations
from typing import Literal, TypedDict
import os
import streamlit as st
from google import genai
from knowledge_base.vector_store import get_vector_store
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


class ChatMessage(TypedDict):
    """Format of messages sent to the browser/API."""

    role: Literal['user', 'model']
    timestamp: str
    content: str


def display_message_part(part):
    """
    Display a single part of a message in the Streamlit UI.
    Customize how you display system prompts, user prompts,
    tool calls, tool returns, etc.
    """
    # system-prompt
    if part.part_kind == 'system-prompt':
        with st.chat_message("system"):
            st.markdown(f"**System**: {part.content}")
    # user-prompt
    elif part.part_kind == 'user-prompt':
        with st.chat_message("user"):
            st.markdown(part.content)
    # text
    elif part.part_kind == 'text':
        with st.chat_message("assistant"):
            st.markdown(part.content)


def rag_agent(user_input: str, vector_store):
    """
    run a wraper around gemini model to get the response, first get the vector of the user input, build a query and get the response
    """
    client = genai.Client(api_key=API_KEY)
    llm_model_name = "gemini-2.0-flash"

    docs = vector_store.similarity_search(user_input, k=1)
    context = ""
    for doc in docs:
        # adding to the context 2/3 of the page content
        page_content = doc.page_content

        context += page_content

    query = f'{user_input}\n{context}'

    genai_response = client.models.generate_content(
        model=llm_model_name,
        contents=query
    )

    if genai_response and genai_response.candidates:
        response = genai_response.candidates[0].content.parts[0].text

    return response


def main():
    st.title("PDF AI  RAG")
    st.write("Please upload a PDF file to get started.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)

    if uploaded_file is not None:
        st.write("Processing file...")
        st.spinner()
        try:
            vector_store = get_vector_store(uploaded_file.read())
            st.session_state.vector_store = vector_store
            st.write("File processed successfully.")
        except Exception as e:
            st.write("An error occurred while processing the file.")
            st.write(e)

    # Initialize chat history in session state if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display all messages from the conversation so far

    # Chat input for the user
    user_input = st.chat_input("What questions do you have about the uploaded PDF?")

    if user_input:
        # We append a new request to the conversation explicitly

        # Display user prompt in the UI
        with st.chat_message("user"):
            st.markdown(user_input)

        # Display the assistant's partial response while streaming
        with st.chat_message("assistant"):
            # Actually run the agent now, streaming the text
            response = rag_agent(user_input, st.session_state.vector_store)
            st.markdown(response)
            # st.text(response)


if __name__ == "__main__":
    main()
