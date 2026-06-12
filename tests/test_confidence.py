from backend.services.confidence_service import confidence_services

from backend.services.reranked_search_service import reranked_search_service

query = "latest iphone launch"

results = (
    reranked_search_service.search(
        query=query
    )
)

print(
    confidence_services.is_confident(
        results
    )
)