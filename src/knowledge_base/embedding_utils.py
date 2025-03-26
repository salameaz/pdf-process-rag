from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    model_name = "sentence-transformers/all-mpnet-base-v2"
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    return embedding_model
