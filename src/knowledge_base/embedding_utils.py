from langchain_community.embeddings import SentenceTransformerEmbeddings


def get_embedding_model():
    model_name = "sentence-transformers/all-mpnet-base-v2"
    embedding_model = SentenceTransformerEmbeddings(model_name=model_name)
    return embedding_model
