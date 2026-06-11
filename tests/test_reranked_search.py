from backend.services.reranked_search_service import reranked_search_service

results = reranked_search_service.search(
            query="self attention",
            category="education"
        )

for result in results:
    print()
    print(
        "Rerank Score:",
        result["rerank_score"]
    )

    print(
    "Hybrid Score:",
    result["hybrid_score"]
    )

    print(
        "Video:",
        result["result"]["video_id"]
    )

    print()

    print(
        result["result"][
            "chunk_text"
        ][:300]
    )

    print()

    print("-" * 80)