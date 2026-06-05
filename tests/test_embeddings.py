from backend.services.embedding_service import (
    embedding_service
)

text = """
Transformers use self attention
mechanisms for sequence modeling.
"""

embedding = embedding_service.generate_embedding(
    text
)

print(f"Vector Dimension: {len(embedding)}")

print()

print(embedding[:10])