from backend.services.confidence_service import confidence_service

from backend.services.reranked_search_service import reranked_search_service

query = "openai gpt 5"

results = (
    reranked_search_service.search(
        query=query
    )
)

print(
    confidence_service.is_confident(
        results
    )
)