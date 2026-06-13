from backend.services.reranked_search_service import (
    reranked_search_service
)

from backend.services.retrieval_evaluator_service import (
    retrieval_evaluator_service
)

from backend.services.query_rewriter_service import (
    query_rewriter_service
)

from backend.services.web_search_service import (
    web_search_service
)

from backend.services.evidence_evaluator_service import (
    evidence_evaluator_service
)


class CRAGService:

    def search(
        self,
        query,
        category=None
    ):

        # =====================================
        # ROUND 1
        # INITIAL RETRIEVAL
        # =====================================

        video_results = (
            reranked_search_service.search(
                query=query,
                category=category
            )
        )

        retrieval_evaluation = (
            retrieval_evaluator_service.evaluate(
                query=query,
                results=video_results
            )
        )

        if retrieval_evaluation[
            "sufficient"
        ]:

            return {

                "status":
                "accepted",

                "query":
                query,

                "rewritten_queries":
                [],

                "video_results":
                video_results,

                "web_results":
                [],

                "retrieval_evaluation":
                retrieval_evaluation,

                "evidence_evaluation":
                None

            }

        # =====================================
        # ROUND 2
        # QUERY REWRITE + RETRIEVE AGAIN
        # =====================================

        rewritten_queries = (
            query_rewriter_service.rewrite(
                query=query
            )
        )

        improved_results = []

        for rewritten_query in rewritten_queries:

            try:

                results = (
                    reranked_search_service.search(
                        query=rewritten_query,
                        category=category
                    )
                )

                improved_results.extend(
                    results
                )

            except Exception as e:

                print(
                    f"Rewrite Retrieval Error: {e}"
                )

        improved_results.sort(
            key=lambda x:
                x["rerank_score"],
            reverse=True
        )

        improved_results = (
            improved_results[:5]
        )

        second_evaluation = (
            retrieval_evaluator_service.evaluate(
                query=query,
                results=improved_results
            )
        )

        if second_evaluation[
            "sufficient"
        ]:

            return {

                "status":
                "retrieved_again",

                "query":
                query,

                "rewritten_queries":
                rewritten_queries,

                "video_results":
                improved_results,

                "web_results":
                [],

                "retrieval_evaluation":
                second_evaluation,

                "evidence_evaluation":
                None

            }

        # =====================================
        # ROUND 3
        # WEB SEARCH
        # =====================================

        web_results = []

        for rewritten_query in rewritten_queries:

            try:

                results = (
                    web_search_service.search(
                        query=rewritten_query
                    )
                )

                web_results.extend(
                    results
                )

            except Exception as e:

                print(
                    f"Web Search Error: {e}"
                )

        evidence_evaluation = (
            evidence_evaluator_service.evaluate(
                query=query,
                web_results=web_results
            )
        )

        if evidence_evaluation[
            "sufficient"
        ]:

            return {

                "status":
                "web_corrected",

                "query":
                query,

                "rewritten_queries":
                rewritten_queries,

                "video_results":
                improved_results,

                "web_results":
                web_results[:10],

                "retrieval_evaluation":
                second_evaluation,

                "evidence_evaluation":
                evidence_evaluation

            }

        # =====================================
        # KNOWLEDGE GAP
        # =====================================

        return {

            "status":
            "knowledge_gap",

            "query":
            query,

            "rewritten_queries":
            rewritten_queries,

            "video_results":
            improved_results,

            "web_results":
            web_results[:10],

            "retrieval_evaluation":
            second_evaluation,

            "evidence_evaluation":
            evidence_evaluation

        }


crag_service = (
    CRAGService()
)