
from backend.services.reranked_search_service import (reranked_search_service)

from backend.services.confidence_service import (confidence_service)

from backend.services.web_search_service import (web_search_service)

from backend.services.query_rewriter_service import (query_rewriter_service)


class CRAGService:

    def search(
        self,
        query
    ):

        video_results = (
            reranked_search_service.search(
                query=query
            )
        )

        evaluation = (
            confidence_service.analyze(
                video_results
            )
        )

        if evaluation["is_confident"]:

            return {
                "query": query,
                "status": "accepted",
                "video_results": video_results,
                "web_results": []
            }

        rewritten_query = (
            query_rewriter_service.rewrite(
                query
            )
        )

        if rewritten_query != query:

            rewritten_results = (
                reranked_search_service.search(
                    query=rewritten_query
                )
            )

            rewritten_evaluation = (
                confidence_service.analyze(
                    rewritten_results
                )
            )

            if rewritten_evaluation[
                "is_confident"
            ]:

                return {
                    "query": query,
                    "rewritten_query":
                    rewritten_query,
                    "status": "rewritten",
                    "video_results":
                    rewritten_results,
                    "web_results": []
                }

        web_results = (
            web_search_service.search(
                query=query
            )
        )

        return {
            "query": query,
            "status": "corrected",
            "video_results": video_results,
            "web_results": web_results
        }

crag_service = (
    CRAGService()
)
