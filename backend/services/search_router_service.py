from backend.services.reranked_search_service import reranked_search_service
from backend.services.confidence_service import confidence_service
from backend.services.web_search_service import web_search_service

class SearchRouterService:

    def search(self,query):

        video_result = (reranked_search_service.search(query=query))

        analysis = (confidence_service.analyze(video_result))

        if analysis["is_confident"]:
            return {
                "query": query,
                "source": "video",
                "confidence": analysis,
                "results": video_result
            }

        web_results=(web_search_service.search(query=query))

        return {
            "query": query,
            "source": "web",
            "confidence": analysis,
            "results": web_results
        }

search_router_service = (SearchRouterService())