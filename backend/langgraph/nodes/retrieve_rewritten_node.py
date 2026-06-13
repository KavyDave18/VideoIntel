from backend.services.reranked_search_service import reranked_search_service

def retrieve_rewritten_node(state):

    rewritten_queries = (state["rewritten_queries"])

    category = (state.get("category"))

    all_results = []

    for rewritten_query in rewritten_queries:
        try:
            results = (reranked_search_service.search(query = rewritten_query,category=category))
            all_results.extend(results)

        except Exception as e:
            print(
                f"Rewrite Retrieval Error: {e}"
            )

        unique_results = {}

    for result in all_results:

        chunk_text = (
            result["result"][
                "chunk_text"
            ]
        )

        if (
            chunk_text
            not in unique_results
        ):

            unique_results[
                chunk_text
            ] = result

        else:

            existing_score = (
                unique_results[
                    chunk_text
                ]["rerank_score"]
            )

            new_score = (
                result[
                    "rerank_score"
                ]
            )

            if (
                new_score
                >
                existing_score
            ):

                unique_results[
                    chunk_text
                ] = result

    final_results = list(
        unique_results.values()
    )

    final_results.sort(
        key=lambda x:
            x["rerank_score"],
        reverse=True
    )

    state[
        "video_results"
    ] = final_results[:5]

    return state

