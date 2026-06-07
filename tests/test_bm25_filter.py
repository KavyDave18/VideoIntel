from backend.services.bm25_service import (
    bm25_service
)

results = (
    bm25_service.search(
        query="self attention",
        category="education",
        limit=10
    )
)

for chunk, score in results:

    print()

    print(
        chunk.video.category
    )

    print(
        chunk.video_id
    )

    print(
        score
    )

    print()

    print("-" * 80)