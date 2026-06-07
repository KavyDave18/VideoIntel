from rank_bm25 import BM25Okapi

from backend.models.video import Video

from backend.database.session import SessionLocal

from backend.models.transcript_chunk import (
    TranscriptChunk
)


class BM25Service:

    def __init__(self):

        self.db = SessionLocal()

        self.chunks = (
            self.db.query(
                TranscriptChunk
            ).all()
        )

        corpus = [
            chunk.chunk_text.lower().split()
            for chunk in self.chunks
        ]

        self.bm25 = BM25Okapi(
            corpus
        )

    def search(
        self,
        query,
        limit=5,
        category=None
    ):

        tokenized_query = (
            query.lower().split()
        )

        scores = self.bm25.get_scores(
            tokenized_query
        )

        results = []

        for chunk, score in zip(
            self.chunks,
            scores
        ):

            if (
                category is not None
                and
                chunk.video.category != category
            ):
                continue

            results.append(
                (
                    chunk,
                    score
                )
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return results[:limit]


bm25_service = BM25Service()