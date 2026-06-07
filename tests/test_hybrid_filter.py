from backend.services.hybrid_search_service import (
    hybrid_search_service
)

results = (
    hybrid_search_service.search(
        query="self attention",
        category="education",
        limit=10,
        candidate_limit=50
    )
)

for result in results:

    print()

    print(
        result["result"]["category"]
    )

    print(
        result["result"]["video_id"]
    )

    print(
        result["score"]
    )

    print()

    print("-" * 80)