from experiment.reranked_multi_retrieval_service import (
    reranked_multi_retrieval_service
)

queries = [

    "transformers",
    "attention",
    "llm",
    "kohli batting"

]

print()
print("=" * 100)
print("RERANKED MULTI RETRIEVAL TEST")
print("=" * 100)

for query in queries:

    results = (
        reranked_multi_retrieval_service.search(
            query=query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print()

    for rank, result in enumerate(
        results,
        start=1
    ):

        candidate = result["result"]
        payload = candidate["result"]

        print(
            f"Rank #{rank}"
        )

        print(
            f"Rerank Score: "
            f"{result['rerank_score']:.4f}"
        )

        print(
            f"Retrieved From: "
            f"{candidate['retrieved_from']}"
        )

        print(
            f"Video ID: "
            f"{payload['video_id']}"
        )

        print(
            f"Hybrid Score: "
            f"{candidate['score']:.4f}"
        )

        print()

        print(
            payload["chunk_text"][:250]
        )

        print()
        print("-" * 50)

    print()
    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)
