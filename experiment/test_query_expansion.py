from experiment.query_expansion_service import (
    query_expansion_service
)

queries = [

    "transformers",
    "attention",
    "llm",
    "kohli batting",
    "iphone 17"

]

print()
print("=" * 100)
print("QUERY EXPANSION TEST")
print("=" * 100)

for query in queries:

    expansions = (
        query_expansion_service.expand(
            query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print()

    print(
        "Expanded Queries:"
    )

    for expansion in expansions:

        print(
            f"  - {expansion}"
        )

    print()
    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)