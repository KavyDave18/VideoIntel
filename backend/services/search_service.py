from backend.database.session import SessionLocal

from backend.models.video import Video

from backend.services.embedding_service import (
    embedding_service
)

from backend.services.qdrant_service import (
    qdrant_service
)


class SearchService:

    def search(
        self,
        query,
        limit=5,
        category=None
    ):

        db = SessionLocal()

        query_embedding = (
            embedding_service
            .generate_embedding(query)
        )

        results = qdrant_service.search(
            query_embedding=query_embedding,
            limit=limit,
            category=category
        )

        formatted_results = []

        for result in results:

            video = (
                db.query(Video)
                .filter(
                    Video.id ==
                    result.payload["video_id"]
                )
                .first()
            )

            formatted_results.append(
                {
                    "score":
                        result.score,

                    "video_title":
                        video.title,

                    "video_id":
                        video.id,

                    "category":
                        result.payload["category"],

                    "start_time":
                        result.payload["start_time"],

                    "end_time":
                        result.payload["end_time"],

                    "chunk_text":
                        result.payload["chunk_text"]
                }
            )

        db.close()

        return formatted_results


search_service = SearchService()