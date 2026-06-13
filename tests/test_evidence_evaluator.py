from backend.services.web_search_service import (
    web_search_service
)

from backend.services.evidence_evaluator_service import (
    evidence_evaluator_service
)


queries = [

    "iphone 17",
    "weather ahmedabad",
    "latest ai news",
    "gpt 5"

]


print()
print("=" * 100)
print("EVIDENCE EVALUATOR TEST")
print("=" * 100)

for query in queries:

    web_results = (
        web_search_service.search(
            query=query
        )
    )

    evaluation = (
        evidence_evaluator_service.evaluate(
            query=query,
            web_results=web_results
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
        f"Web Results: "
        f"{len(web_results)}"
    )

    if web_results:

        print()

        print(
            "Top Web Result:"
        )

        print(
            f"Title: "
            f"{web_results[0]['title']}"
        )

        print()

        print(
            f"URL: "
            f"{web_results[0]['url']}"
        )

        print()

        print(
            web_results[0][
                "content"
            ][:300]
        )

    print()
    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)