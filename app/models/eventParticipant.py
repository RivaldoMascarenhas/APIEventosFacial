from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EventParticipant(Base):
    __tablename__ = "event_participants"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # Relações
    event = relationship("Event", back_populates="participants")
    
    def __init__(self, event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id
    def __repr__(self):
        return f"EventParticipant(id={self.id}, event_id={self.event_id}, user_id={self.user_id})"