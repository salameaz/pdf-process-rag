def query_generator(user_input: str, vector_store):

    docs = vector_store.similarity_search(user_input, k=2)
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
    1. Thoroughly analyze the provided PDF context.
    2. Answer the question using the PDF as the main source.
    3. Only reference external information if the PDF does not cover the question adequately.
    4. Provide citations where applicable.
    """

    return query
