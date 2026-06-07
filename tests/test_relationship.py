from backend.database.session import SessionLocal

from backend.models.video import Video
from backend.models.transcript_chunk import TranscriptChunk

db = SessionLocal()

chunk = (
    db.query(
        TranscriptChunk
    )
    .first()
)

print()

print(
    "Video ID:",
    chunk.video_id
)

print(
    "Title:",
    chunk.video.title
)

print(
    "Category:",
    chunk.video.category
)

print()

print(
    "Number of Chunks in Video:",
    len(chunk.video.chunks)
)

db.close()