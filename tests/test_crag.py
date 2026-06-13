from backend.services.crag_service import (
    crag_service
)

queries = [

    "transformers",

    "attention",

    "kohli batting",

    "llm",

    "gpt",

    "iphone 17"

]

print()
print("=" * 100)
print("CRAG REWRITE TEST")
print("=" * 100)

for query in queries:

    result = (
        crag_service.search(
            query=query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print(
        f"Status: "
        f"{result['status']}"
    )

    if (
        "rewritten_query"
        in result
    ):

        print(
            f"Rewritten Query: "
            f"{result['rewritten_query']}"
        )

    print()

    print(
        f"Video Results: "
        f"{len(result['video_results'])}"
    )

    print(
        f"Web Results: "
        f"{len(result['web_results'])}"
    )

    if len(
        result["video_results"]
    ) > 0:

        print()

        top_result = (
            result["video_results"][0]
        )

        print(
            f"Top Video ID: "
            f"{top_result['result']['video_id']}"
        )

        print(
            f"Rerank Score: "
            f"{top_result['rerank_score']:.4f}"
        )

    print()
    print("-" * 100)

print()
print("=" * 100)
print("CRAG REWRITE TEST COMPLETE")
print("=" * 100)
