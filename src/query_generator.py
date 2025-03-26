def query_generator(user_input: str, vector_store):

    docs = vector_store.similarity_search(user_input, k=6)
    context = ""
    for doc in docs:
        # adding to the context 2/3 of the page content
        page_content = doc.page_content

        context += page_content

    query = f"""
    You have access to a single PDF document that contains detailed information on the topic. Use the content of this PDF as your primary reference.
    If the information in the PDF is insufficient, you may use external knowledge, but only as a last resort.

    ---------------------
    Context (from the PDF):
    {context}

    ---------------------
    Question:
    {user_input}

    ---------------------
    Instructions:
    1. Base your answer entirely on the information from the PDF document.
    2. Use external knowledge strictly as a last resort.
    3. Do not include meta commentary or phrases such as "Based on the provided PDF context" in your answer.
    4. Provide citations where applicable.
    """

    return query
