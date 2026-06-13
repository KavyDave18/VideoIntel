from backend.services.query_rewriter_service import (
    query_rewriter_service
)

queries = [

    "transformers",

    "attention",

    "kohli batting",

    "llm",

    "gpt",

    "self attention",

    "virat kohli sixes"

]

print()
print("=" * 100)
print("QUERY REWRITER TEST")
print("=" * 100)

for query in queries:

    rewritten_query = (
        query_rewriter_service.rewrite(
            query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Original Query : {query}"
    )

    print(
        f"Rewritten Query: {rewritten_query}"
    )

    if query == rewritten_query:

        print(
            "Status: No Rewrite"
        )

    else:

        print(
            "Status: Rewritten"
        )

    print("-" * 100)

print()
print("=" * 100)
print("QUERY REWRITER TEST COMPLETE")
print("=" * 100)
