from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Presence(Base):
    __tablename__ = "presences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    confirmed = Column(Boolean, default=False)  # validada manualmente
    match_score = Column(Float, nullable=True)  # melhor se tiver decimais
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relações
    user = relationship("User", back_populates="presences", passive_deletes=True)
    event = relationship("Event", back_populates="presences", passive_deletes=True)

    def __repr__(self):
        return (
            f"Presence(id={self.id}, user_id={self.user_id}, event_id={self.event_id}, "
            f"confirmed={self.confirmed}, match_score={self.match_score})"
        )

    def __init__(self, user_id, event_id, confirmed=False, match_score=None):
        self.user_id = user_id
        self.event_id = event_id
        self.confirmed = confirmed
        self.match_score = match_score