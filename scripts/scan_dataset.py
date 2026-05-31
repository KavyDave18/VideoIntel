import os
from backend.services.metadata_service import extract_video_metadata
from backend.database.session import SessionLocal
from backend.models.video import Video

DATASET_PATH = "dataset"

db = SessionLocal()

for category in os.listdir(DATASET_PATH):
    category_path = os.path.join(DATASET_PATH,category)

    if os.path.isdir(category_path):
        for filename in os.listdir(category_path):
            if filename.endswith((".mp4",".avi",".mkv")):
                video_path = os.path.join(category_path,filename)
                metadata = extract_video_metadata(video_path)

                video = Video(
                    title=filename,
                    path=video_path,
                    category=category,
                    duration=metadata["duration"],
                    fps=metadata["fps"],
                    resolution=metadata["resolution"]
                    )
                db.add(video)
                db.commit()
                print(f"Added video: {filename} in category: {category}")
db.close()