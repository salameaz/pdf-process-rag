import streamlit as st
from src.pdf_processing.text_extraction import extract_text_from_pdf
import os
import tempfile


def main():
    st.title("PDF Chatbot")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    pages = []

    if uploaded_file is not None:
        # Create a temporary directory to save the uploaded file
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, uploaded_file.name)

            # Save the uploaded file to the temporary location
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            st.write(f"File uploaded and saved temporarily to: {file_path}")
            try:
                pages = extract_text_from_pdf(file_path)
            except Exception as e:
                st.error(f"Error loading PDF: {e}")
            # You can now proceed with chunking, embedding, and RAG using the 'pages' list
            # For example:
            # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            # chunks = text_splitter.split_documents(pages)
            # embeddings = OpenAIEmbeddings()
            # knowledge_base = FAISS.from_documents(chunks, embeddings)
        print(pages)


if __name__ == "__main__":
    main()
