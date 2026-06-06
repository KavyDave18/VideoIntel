from backend.services.bm25_service import (
    bm25_service
)

results = bm25_service.search(
    "self attention"
)

for chunk, score in results:

    print()

    print(
        "Score:",
        score
    )

    print(
        chunk.video_id
    )

    print(
        chunk.chunk_text[:300]
    )

    print("-" * 50)