from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )

    return text_splitter.split_documents(documents)


def restructure_chunks(chunks):
    chunks_dicts = []

    for chunk in chunks:
        chunks_dicts.append({"metadata": chunk.metadata, "page_content": chunk.page_content})

    return chunks_dicts
