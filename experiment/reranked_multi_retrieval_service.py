from experiment.multi_retrieval_service import (
    multi_retrieval_service
)

from backend.services.reranker_service import (
    reranker_service
)


class RerankedMultiRetrievalService:

    def search(
        self,
        query,
        category=None,
        candidate_limit=5,
        final_limit=5
    ):

        candidates = (
            multi_retrieval_service.search(
                query=query,
                category=category,
                per_query_limit=candidate_limit
            )
        )

        chunks = [

            candidate["result"]["chunk_text"]

            for candidate in candidates
        ]

        reranked = (
            reranker_service.rerank(
                query=query,
                chunks=chunks
            )
        )

        final_results = []

        for chunk_text, rerank_score in reranked:

            for candidate in candidates:

                if (
                    candidate["result"]["chunk_text"]
                    ==
                    chunk_text
                ):

                    final_results.append(

                        {
                            "rerank_score":
                            float(
                                rerank_score
                            ),

                            "result":
                            candidate
                        }

                    )

                    break

        return (
            final_results[:final_limit]
        )


reranked_multi_retrieval_service = (
    RerankedMultiRetrievalService()
)