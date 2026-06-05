from backend.database.session import SessionLocal
from backend.models.transcript_chunk import TranscriptChunk
from backend.services.embedding_service import (embedding_service)
from backend.services.qdrant_service import (qdrant_service)

db = SessionLocal()

chunks = db.query(TranscriptChunk).all()

print(f"Fount {len(chunks)} chunks")

for chunk in chunks:
    
    embedding = embedding_service.generate_embedding(chunk.chunk_text)

    payload = {
        "video_id" : chunk.video_id,
        "start_time":chunk.start_time,
        "end_time" : chunk.end_time,
        "chunk_text" : chunk.chunk_text
        }

    qdrant_service.insert_chunk(
        chunk_id=chunk.id,
        embedding=embedding,
        payload=payload
    )

    print(f"indexed Chunk{chunk.id}")

db.close()
print()
print("All chunks indexed successfully.")


