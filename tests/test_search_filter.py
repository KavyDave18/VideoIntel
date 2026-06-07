from backend.services.search_service import (
    search_service
)

results = (
    search_service.search(
        query="self attention",
        category="education",
        limit=10
    )
)

for result in results:

    print()

    print(
        "Category:",
        result["category"]
    )

    print(
        "Video ID:",
        result["video_id"]
    )

    print(
        "Score:",
        result["score"]
    )

    print()

    print("-" * 80)