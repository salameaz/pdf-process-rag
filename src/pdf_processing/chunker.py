from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


def restructure_chunks(chunks):
    chunks_dicts = []

    for chunk in chunks:
        chunks_dicts.append({"metadata": chunk.metadata, "page_content": chunk.page_content})

    return chunks_dicts
