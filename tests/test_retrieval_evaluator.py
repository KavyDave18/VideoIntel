from backend.services.reranked_search_service import (
    reranked_search_service
)

from backend.services.retrieval_evaluator_service import (
    retrieval_evaluator_service
)


queries = [

    "self attention",
    "transformers",
    "virat kohli sixes",
    "iphone 17",
    "weather ahmedabad",
    "gpt 5"

]


print()
print("=" * 100)
print("RETRIEVAL EVALUATOR TEST")
print("=" * 100)

for query in queries:

    results = (
        reranked_search_service.search(
            query=query
        )
    )

    evaluation = (
        retrieval_evaluator_service.evaluate(
            query=query,
            results=results
        )
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print()

    print(
        f"Sufficient: "
        f"{evaluation['sufficient']}"
    )

    print(
        f"Confidence: "
        f"{evaluation['confidence']}"
    )

    print()

    print(
        f"Reason: "
        f"{evaluation['reason']}"
    )

    print()

    print(
        f"Retrieved Results: "
        f"{len(results)}"
    )

    if results:

        print()

        print(
            "Top Result:"
        )

        print(
            f"Video ID: "
            f"{results[0]['result']['video_id']}"
        )

        print(
            f"Rerank Score: "
            f"{results[0]['rerank_score']:.4f}"
        )

        print()

        print(
            results[0]["result"][
                "chunk_text"
            ][:300]
        )

    print()
    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)