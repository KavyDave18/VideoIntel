from backend.services.web_search_service import (
    web_search_service
)


def web_search_node(
    state
):

    rewritten_queries = (
        state[
            "rewritten_queries"
        ]
    )

    all_results = []

    for rewritten_query in rewritten_queries:

        try:

            results = (
                web_search_service.search(
                    query=rewritten_query
                )
            )

            all_results.extend(
                results
            )

        except Exception as e:

            print(
                f"Web Search Error: {e}"
            )

    unique_results = {}

    for result in all_results:

        url = (
            result.get(
                "url",
                ""
            )
        )

        if not url:

            continue

        if (
            url
            not in unique_results
        ):

            unique_results[
                url
            ] = result

        else:

            existing_score = (
                unique_results[
                    url
                ].get(
                    "score",
                    0
                )
            )

            new_score = (
                result.get(
                    "score",
                    0
                )
            )

            if (
                new_score
                >
                existing_score
            ):

                unique_results[
                    url
                ] = result

    web_results = list(
        unique_results.values()
    )

    web_results.sort(
        key=lambda x:
            x.get(
                "score",
                0
            ),
        reverse=True
    )

    state[
        "web_results"
    ] = web_results[:10]

    return state