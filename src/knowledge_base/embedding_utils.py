from sentence_transformers import SentenceTransformer


def get_embedding_model():
    model_name = 'all-mpnet-base-v2'

    model = SentenceTransformer(model_name)

    return model
