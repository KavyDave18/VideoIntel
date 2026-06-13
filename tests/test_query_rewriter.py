from backend.services.query_rewriter_service import (
    query_rewriter_service
)

queries = [

    "transformers",
    "attention",
    "llm",
    "gpt",
    "kohli batting"

]

print()
print("=" * 100)
print("QUERY REWRITER TEST")
print("=" * 100)

for query in queries:

    rewritten_queries = (
        query_rewriter_service.rewrite(
            query=query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Original Query: {query}"
    )

    print()

    for index, rewritten_query in enumerate(
        rewritten_queries,
        start=1
    ):

        print(
            f"{index}. {rewritten_query}"
        )

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)