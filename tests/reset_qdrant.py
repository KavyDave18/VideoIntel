from backend.services.qdrant_service import (
    qdrant_service
)

qdrant_service.client.delete_collection(
    collection_name=
    qdrant_service.COLLECTION_NAME
)

print(
    "Collection deleted"
)