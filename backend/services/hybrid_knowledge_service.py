from backend.services.reranked_search_service import (
    reranked_search_service
)

from backend.services.confidence_service import (
    confidence_service
)

from backend.services.web_search_service import (
    web_search_service
)


class HybridKnowledgeService:

    def search(
        self,
        query
    ):

        video_results = (
            reranked_search_service.search(
                query=query
            )
        )

        analysis = (
            confidence_service.analyze(
                video_results
            )
        )

        if analysis["is_confident"]:

            return {
                "query": query,
                "source": "video",
                "confidence": analysis,
                "video_results": video_results,
                "web_results": []
            }

        web_results = (
            web_search_service.search(
                query=query
            )
        )

        return {
            "query": query,
            "source": "video+web",
            "confidence": analysis,
            "video_results": video_results,
            "web_results": web_results
        }


hybrid_knowledge_service = (
    HybridKnowledgeService()
)