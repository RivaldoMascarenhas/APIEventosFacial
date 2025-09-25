from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)  
    description = Column(Text, nullable=True)  
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relações 
    participants = relationship(
        "EventParticipant",
        back_populates="event",
        cascade="all, delete-orphan"
    )
    presences = relationship("Presence", back_populates="event", cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"Event(id={self.id}, name={self.name}, "
            f"description={self.description}, start_time={self.start_time}, "
            f"end_time={self.end_time}, created_by={self.created_by})"
        )

    def __init__(self, name, description, start_time, end_time, created_by):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.created_by = created_by