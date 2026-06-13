from backend.services.crag_service import (
    crag_service
)


queries = [

    "self attention",
    "transformers",
    "virat kohli sixes",
    "iphone 17",
    "weather ahmedabad",
    "gpt 5",
    "latest ai news"

]


print()
print("=" * 100)
print("CRAG TEST")
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

    print()

    print(
        f"Status: "
        f"{result['status']}"
    )

    print()

    print(
        "Retrieval Evaluation:"
    )

    print(
        result[
            "retrieval_evaluation"
        ]
    )

    print()

    if result[
        "evidence_evaluation"
    ]:

        print(
            "Evidence Evaluation:"
        )

        print(
            result[
                "evidence_evaluation"
            ]
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

    if result[
        "rewritten_queries"
    ]:

        print()

        print(
            "Rewritten Queries:"
        )

        for rewritten_query in result[
            "rewritten_queries"
        ]:

            print(
                f"- {rewritten_query}"
            )

    if result[
        "video_results"
    ]:

        print()

        print(
            "Top Video Result:"
        )

        top_result = result[
            "video_results"
        ][0]

        print(
            f"Video ID: "
            f"{top_result['result']['video_id']}"
        )

        print(
            f"Rerank Score: "
            f"{top_result['rerank_score']:.4f}"
        )

        print()

        print(
            top_result["result"][
                "chunk_text"
            ][:250]
        )

    if result[
        "web_results"
    ]:

        print()

        print(
            "Top Web Result:"
        )

        print(
            result[
                "web_results"
            ][0]["title"]
        )

    print()
    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)