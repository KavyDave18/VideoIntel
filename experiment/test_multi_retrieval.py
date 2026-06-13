from experiment.multi_retrieval_service import (
    multi_retrieval_service
)

queries = [

    "transformers",
    "attention",
    "llm",
    "kohli batting"

]

print()
print("=" * 100)
print("MULTI RETRIEVAL TEST")
print("=" * 100)

for query in queries:

    results = (
        multi_retrieval_service.search(
            query=query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print(
        f"Candidates Found: "
        f"{len(results)}"
    )

    print()

    for rank, result in enumerate(
        results[:10],
        start=1
    ):

        print(
            f"Rank #{rank}"
        )

        print(
            f"Retrieved From: "
            f"{result['retrieved_from']}"
        )

        print(
            f"Video ID: "
            f"{result["result"]['video_id']}"
        )

        print(
            f"Score: "
            f"{result['score']:.4f}"
        )

        print()

        print(
            result["result"]["chunk_text"][:150]
        )

        print()

    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)