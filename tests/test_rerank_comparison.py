from backend.services.hybrid_search_service import (
    hybrid_search_service
)

from backend.services.reranked_search_service import (
    reranked_search_service
)

query = "self attention"

print()
print("=" * 80)
print("HYBRID SEARCH")
print("=" * 80)

hybrid_results = (
    hybrid_search_service.search(
        query=query,
        category="education",
        limit=5,
        candidate_limit=50
    )
)

for rank, result in enumerate(
    hybrid_results,
    start=1
):

    print()
    print(f"Rank #{rank}")

    print(
        result["score"]
    )

    print(
        result["result"]["chunk_text"][:300]
    )

    print("-" * 80)

print()
print("=" * 80)
print("RERANKED SEARCH")
print("=" * 80)

reranked_results = (
    reranked_search_service.search(
        query=query,
        category="education",
        final_limit=5
    )
)

for rank, result in enumerate(
    reranked_results,
    start=1
):

    print()

    print(f"Rank #{rank}")

    print(
        result["rerank_score"]
    )

    print(
        result["result"]["chunk_text"][:300]
    )

    print("-" * 80)