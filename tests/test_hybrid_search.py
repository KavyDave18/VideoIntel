from backend.services.hybrid_search_service import (
    hybrid_search_service
)

results = hybrid_search_service.search(
    "self attention"
)

for result in results:

    print()

    print(
        "Score:",
        result["score"]
    )

    print()

    print(
        result["result"]["chunk_text"][:500]
    )

    print()

    print("-" * 80)