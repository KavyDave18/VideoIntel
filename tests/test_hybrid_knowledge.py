from backend.services.hybrid_knowledge_service import (
    hybrid_knowledge_service
)

queries = [

    "self attention",

    "transformer architecture",

    "latest iphone launch",

    "openai gpt 5"

]

for query in queries:

    print()
    print("=" * 80)

    result = (
        hybrid_knowledge_service.search(
            query=query
        )
    )

    print(
        f"Query: {query}"
    )

    print(
        f"Source: "
        f"{result['source']}"
    )

    print()

    print(
        "Confidence:"
    )

    print(
        result["confidence"]
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

    print()

    print("-" * 80)

    print(
        "TOP VIDEO RESULTS"
    )

    print("-" * 80)

    for rank, video in enumerate(
        result["video_results"][:3],
        start=1
    ):

        print()

        print(
            f"Rank #{rank}"
        )

        print(
            f"Video ID: "
            f"{video['result']['video_id']}"
        )

        print(
            f"Rerank Score: "
            f"{video['rerank_score']:.4f}"
        )

        print(
            f"Hybrid Score: "
            f"{video['result']['score']:.4f}"
        )

        print()

        print(
            video["result"][
                "chunk_text"
            ][:200]
        )

        print()

    if len(
        result["web_results"]
    ) > 0:

        print()

        print("-" * 80)

        print(
            "TOP WEB RESULTS"
        )

        print("-" * 80)

        for rank, web in enumerate(
            result["web_results"][:3],
            start=1
        ):

            print()

            print(
                f"Rank #{rank}"
            )

            print(
                web["title"]
            )

            print()

            print(
                web["url"]
            )

            print()

            print(
                web["content"][:200]
            )

            print()

    print()
    print("=" * 80)