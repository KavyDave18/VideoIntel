from backend.services.web_search_service import (
    web_search_service
)

results = web_search_service.search(
    "iphone 17"
)

print(results[0])