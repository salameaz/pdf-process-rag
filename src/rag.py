from google import genai
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


def rag(user_input: str, vector_store):
    client = genai.Client(api_key=API_KEY)
    llm_model_name = "gemini-2.0-flash"

    docs = vector_store.similarity_search(user_input, k=2)
    context = ""
    for doc in docs:
        # adding to the context 2/3 of the page content
        page_content = doc.page_content

        context += page_content

    query = f"""
    Answer the question based on the following context:
    {context}

    ---------------------
    Question: {user_input}

    ---------------------
    use external knowledge JUST when needed.
    """

    genai_response = client.models.generate_content(
        model=llm_model_name,
        contents=query,
    )

    if genai_response and genai_response.candidates:
        response = genai_response.candidates[0].content.parts[0].text

    return response
