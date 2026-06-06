from backend.services.search_service import (
    search_service
)

from backend.services.bm25_service import (
    bm25_service
)


class HybridSearchService:

    def normalize_scores(
        self,
        scores
    ):

        max_score = max(scores)

        if max_score == 0:

            return [
                0
                for _
                in scores
            ]

        return [
            score / max_score
            for score in scores
        ]

    def search(
        self,
        query,
        limit=5
    ):

        vector_results = (
            search_service.search(
                query=query,
                limit=10
            )
        )

        bm25_results = (
            bm25_service.search(
                query=query,
                limit=10
            )
        )

        vector_scores = [
            result["score"]
            for result
            in vector_results
        ]

        bm25_scores = [
            score
            for _, score
            in bm25_results
        ]

        normalized_vector_scores = (
            self.normalize_scores(
                vector_scores
            )
        )

        normalized_bm25_scores = (
            self.normalize_scores(
                bm25_scores
            )
        )

        combined_scores = {}

        for result, score in zip(
            vector_results,
            normalized_vector_scores
        ):

            chunk_text = (
                result["chunk_text"]
            )

            combined_scores[
                chunk_text
            ] = {
                "score": score,
                "result": result
            }

        for (
            (chunk, _),
            normalized_score
        ) in zip(
            bm25_results,
            normalized_bm25_scores
        ):

            chunk_text = (
                chunk.chunk_text
            )

            if chunk_text in combined_scores:

                combined_scores[
                    chunk_text
                ]["score"] += (
                    normalized_score
                )

            else:

                combined_scores[
                    chunk_text
                ] = {
                    "score":
                        normalized_score,

                    "result": {
                        "video_id":
                            chunk.video_id,

                        "video_title":
                            None,

                        "start_time":
                            chunk.start_time,

                        "end_time":
                            chunk.end_time,

                        "chunk_text":
                            chunk.chunk_text
                    }
                }

        sorted_results = sorted(
            combined_scores.values(),
            key=lambda x:
                x["score"],
            reverse=True
        )

        return sorted_results[:limit]


hybrid_search_service = (
    HybridSearchService()
)