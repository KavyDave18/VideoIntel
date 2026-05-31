import os

from backend.database.session import SessionLocal

from backend.models.video import Video

from backend.services.audio_service import extract_audio


# Create DB session
db = SessionLocal()


# Fetch all videos
videos = db.query(Video).all()


# Process each video
for video in videos:

    print("\n-----------------------------------")
    print(f"Processing: {video.title}")

    video_path = video.path

    # Check if video exists
    if not os.path.exists(video_path):

        print(f"Video file missing: {video_path}")

        continue

    # Extract audio
    audio_path = extract_audio(video_path)

    print(f"Audio extracted: {audio_path}")


# Close DB session
db.close()

print("\n===================================")
print("All audio extracted successfully!")
print("===================================")