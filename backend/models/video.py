from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP
)

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from backend.database.base import Base


class Video(Base):

    __tablename__ = "videos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255)
    )

    path = Column(
        String(500)
    )

    category = Column(
        String(100)
    )

    duration = Column(
        Float
    )

    fps = Column(
        Float
    )

    resolution = Column(
        String(50)
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    chunks = relationship(
        "TranscriptChunk",
        back_populates="video"
    )