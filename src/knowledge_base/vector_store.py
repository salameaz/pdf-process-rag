import tempfile
import os
from langchain_core.vectorstores import InMemoryVectorStore
from .embedding_utils import get_embedding_model
from pdf_processing import text_extraction, chunker
# import asyncio


def get_vector_store(file_bytes):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(file_bytes)
        temp_file_path = temp_file.name

    try:
        documents = text_extraction.extract_text_from_pdf(temp_file_path)
        chunks = chunker.chunk_documents(documents)
        # chunks_dicts = chunker.restructure_chunks(chunks)

        embedding_model = get_embedding_model()

        # vector_store = InMemoryVectorStore.from_documents(documents=documents, embedding=embedding_model)
        vector_store = InMemoryVectorStore.from_documents(chunks, embedding_model)

    except Exception as e:
        raise e
    finally:
        os.remove(temp_file_path)

    return vector_store
