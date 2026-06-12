from backend.services.search_router_service import (
    search_router_service
)

queries = [

    "self attention",

    "virat kohli sixes",

    "latest iphone launch",

    "openai gpt 5"
]

for query in queries:

    print()
    print("=" * 80)

    result = (
        search_router_service.search(
            query
        )
    )

    print(
        f"Query: {query}"
    )

    print(
        f"Source: {result['source']}"
    )

    print(
        f"Confidence: "
        f"{result['confidence']}"
    )