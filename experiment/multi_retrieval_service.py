from experiment.query_expansion_service import (
    query_expansion_service
)

from backend.services.hybrid_search_service import (
    hybrid_search_service
)


class MultiRetrievalService:

    def search(
        self,
        query,
        category=None,
        per_query_limit=5
    ):

        expanded_queries = (
            query_expansion_service.expand(
                query
            )
        )

        all_results = []

        seen_chunks = set()

        for expanded_query in expanded_queries:

            results = (
                hybrid_search_service.search(
                    query=expanded_query,
                    category=category,
                    limit=per_query_limit
                )
            )

            for result in results:

                chunk_text = (
                    result["result"]["chunk_text"]
                )

                if chunk_text in seen_chunks:
                    continue

                seen_chunks.add(
                    chunk_text
                )

                result[
                    "retrieved_from"
                ] = expanded_query

                all_results.append(
                    result
                )

        all_results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return all_results


multi_retrieval_service = (
    MultiRetrievalService()
)
