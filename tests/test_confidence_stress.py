from backend.services.search_router_service import (
    search_router_service
)

queries = [

    # Strong in-dataset queries
    "self attention",
    "virat kohli sixes",
    "jack ma advice",
    "sleep superpower",

    # Related but harder
    "transformers",
    "kohli batting",
    "attention mechanism",
    "neural networks",

    # Out-of-domain
    "iphone 17",
    "tesla stock",
    "donald trump",
    "bitcoin price",
    "weather ahmedabad",

    # Additional edge cases
    "gpt 5",
    "latest ai news"
]

print()
print("=" * 100)
print("CONFIDENCE STRESS TEST")
print("=" * 100)

for query in queries:

    result = (
        search_router_service.search(
            query
        )
    )

    confidence = (
        result["confidence"]
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print(
        f"Source: {result['source']}"
    )

    print(
        f"Top Score: "
        f"{confidence['top_score']:.4f}"
    )

    print(
        f"Second Score: "
        f"{confidence['second_score']:.4f}"
    )

    print(
        f"Score Gap: "
        f"{confidence['score_gap']:.4f}"
    )

    print(
        f"Confident: "
        f"{confidence['is_confident']}"
    )

    print("-" * 100)

print()
print("=" * 100)
print("STRESS TEST COMPLETE")
print("=" * 100)