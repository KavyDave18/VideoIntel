from backend.services.embedding_service import (
    embedding_service
)

from backend.services.qdrant_service import (
    qdrant_service
)

query_embedding = (
    embedding_service.generate_embedding(
        "self attention"
    )
)

results = (
    qdrant_service.search(
        query_embedding=query_embedding,
        limit=10,
        category="education"
    )
)

for result in results:

    print()

    print(
        result.payload["category"]
    )

    print(
        result.payload["video_id"]
    )

    print(
        result.score
    )

    print()

    print("-" * 80)