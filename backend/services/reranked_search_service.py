from backend.services.hybrid_search_service import (
    hybrid_search_service
)

from backend.services.reranker_service import (
    reranker_service
)


class RerankedSearchService:

    def search(
        self,
        query,
        category=None,
        candidate_limit=50,
        final_limit=5
    ):

        candidates = (
            hybrid_search_service.search(
                query=query,
                category=category,
                limit=candidate_limit,
                candidate_limit=candidate_limit
            )
        )

        pairs = [
            (
                query,
                candidate["result"]["chunk_text"]
            )
            for candidate
            in candidates
        ]

        scores = (
            reranker_service.model.predict(
                pairs
            )
        )

        reranked_results = []

        for candidate, score in zip(
            candidates,
            scores
        ):

            reranked_results.append(
                {
                    "rerank_score":
                        float(score),

                    "result":
                        candidate["result"]
                }
            )

        reranked_results.sort(
            key=lambda x:
                x["rerank_score"],
            reverse=True
        )

        return (
            reranked_results[
                :final_limit
            ]
        )


reranked_search_service = (
    RerankedSearchService()
)