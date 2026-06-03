from backend.database.session import SessionLocal

from backend.models.video import Video
from backend.models.transcript_segment import TranscriptSegment
from backend.models.transcript_chunk import TranscriptChunk

from backend.services.chunking_service import create_chunks


db = SessionLocal()

videos = db.query(Video).all()

for video in videos:

    print("\n----------------------------------")
    print(f"Processing Video: {video.title}")

    existing_chunk = db.query(
        TranscriptChunk
    ).filter(
        TranscriptChunk.video_id == video.id
    ).first()

    if existing_chunk:

        print("Chunks already exist. Skipping.")
        continue

    segments = (
        db.query(TranscriptSegment)
        .filter(
            TranscriptSegment.video_id == video.id
        )
        .order_by(
            TranscriptSegment.start_time
        )
        .all()
    )

    if not segments:

        print("No transcript segments found.")
        continue

    chunks = create_chunks(segments)

    print(f"Generated {len(chunks)} chunks")

    for chunk in chunks:

        db_chunk = TranscriptChunk(
            video_id=video.id,
            chunk_index=chunk["chunk_index"],
            start_time=chunk["start_time"],
            end_time=chunk["end_time"],
            word_count=chunk["word_count"],
            chunk_text=chunk["chunk_text"]
        )

        db.add(db_chunk)

    db.commit()

    print("Chunks stored successfully")

db.close()

print("\n===================================")
print("Chunk generation completed")
print("===================================")