from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    Text,
    TIMESTAMP
)

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from backend.database.base import Base


class TranscriptChunk(Base):

    __tablename__ = "transcript_chunks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    video_id = Column(
        Integer,
        ForeignKey("videos.id"),
        nullable=False
    )

    video = relationship(
        "Video",
        back_populates="chunks"
    )

    chunk_index = Column(
        Integer,
        nullable=False
    )

    start_time = Column(
        Float,
        nullable=False
    )

    end_time = Column(
        Float,
        nullable=False
    )

    word_count = Column(
        Integer,
        nullable=False
    )

    chunk_text = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )