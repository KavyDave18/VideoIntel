from backend.database.session import SessionLocal
from backend.models.video import Video

db = SessionLocal()

videos = db.query(Video).all()

for video in videos:
    print(
        video.id,
        video.category
    )