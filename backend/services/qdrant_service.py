from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class QdrantService:

    COLLECTION_NAME = "video_chunks"

    def __init__(self):

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

    def create_collection(self):

        collections = self.client.get_collections()

        collection_names = [
            collection.name
            for collection in collections.collections
        ]

        if self.COLLECTION_NAME in collection_names:
            print(
                f"Collection '{self.COLLECTION_NAME}' already exists"
            )
            return

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )

        print(
            f"Collection '{self.COLLECTION_NAME}' created successfully"
        )

    def insert_chunk(
        self,
        chunk_id,
        embedding,
        payload
    ):

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,

            points=[
                PointStruct(
                    id=chunk_id,
                    vector=embedding,
                    payload=payload
                )
            ]
        )

    def search(
        self,
        query_embedding,
        limit=5
    ):

        response = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=query_embedding,
            limit=limit,
            with_payload=True
        )

        return response.points

    def get_vector_count(self):

        result = self.client.count(
            collection_name=self.COLLECTION_NAME
        )

        return result.count


qdrant_service = QdrantService()