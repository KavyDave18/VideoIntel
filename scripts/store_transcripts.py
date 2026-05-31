import os

from backend.database.session import SessionLocal

from backend.models.video import Video
from backend.models.transcript_segment import TranscriptSegment

from backend.services.transcription_service import transcribe_audio


# Create DB session
db = SessionLocal()


videos = db.query(Video).all()

for video in videos:

    print(video.id)

    filename = os.path.splitext(video.title)[0]

    audio_path = f"processed/audio/{filename}.wav"

    result = transcribe_audio(audio_path)

    for segment in result["segments"]:

        transcript = TranscriptSegment(
            video_id=video.id,

            start_time=segment["start"],
            end_time=segment["end"],
            text=segment["text"]
        )

        db.add(transcript)

    db.commit()