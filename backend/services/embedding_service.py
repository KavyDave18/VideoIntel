from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embedding(self, text):

        return self.model.encode(
            text,
            normalize_embeddings=True
        ).tolist()


embedding_service = EmbeddingService()