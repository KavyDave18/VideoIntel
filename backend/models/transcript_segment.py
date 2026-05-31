from sqlalchemy import Column, Integer, Float, Text, ForeignKey
from backend.database.base import Base

class TranscriptSegment(Base):
    __tablename__ = "transcript_segments"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    start_time = Column(Float)
    end_time = Column(Float)
    text = Column(Text)