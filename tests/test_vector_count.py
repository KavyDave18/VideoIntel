from backend.services.qdrant_service import (
    qdrant_service
)

count = qdrant_service.client.count(
    collection_name="video_chunks"
)

print(count)