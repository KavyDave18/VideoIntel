import os

from backend.database.session import SessionLocal

from backend.models.video import Video
from backend.models.transcript_segment import TranscriptSegment

from backend.services.transcription_service import transcribe_audio


# Create DB session
db = SessionLocal()


videos = db.query(Video).filter(
    Video.id.in_([
        # Cricket
        3, 12, 17,

        # Education
        43, 39, 34, 25, 24,

        # Talks
        46, 47, 48,

        # Podcasts
        59, 60, 61,

        # Random
        67, 68, 69
    ])
).all()


for video in videos:

    print("\n----------------------------------")
    print(f"Processing Video ID: {video.id}")
    print(f"Processing Video: {video.title}")

    # Skip if transcript already exists
    existing = db.query(TranscriptSegment).filter(
        TranscriptSegment.video_id == video.id
    ).first()

    if existing:
        print(f"Skipping {video.title} (already transcribed)")
        continue

    filename = os.path.splitext(video.title)[0]

    audio_path = f"processed/audio/{filename}.wav"

    # Check audio exists
    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        continue

    try:

        result = transcribe_audio(audio_path)

        print(f"Segments Found: {len(result['segments'])}")

        for segment in result["segments"]:

            transcript = TranscriptSegment(
                video_id=video.id,
                start_time=segment["start"],
                end_time=segment["end"],
                text=segment["text"]
            )

            db.add(transcript)

        db.commit()

        print(f"Saved transcript for: {video.title}")

    except Exception as e:

        print(f"Error processing {video.title}")
        print(e)

        db.rollback()

        continue


db.close()

print("\n==================================")
print("Transcript processing completed!")
print("==================================")