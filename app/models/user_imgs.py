from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class UserImage(Base):
    __tablename__ = "user_images"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String(500), nullable=False)  # caminho no servidor
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="images")

    def __init__(self, user_id, file_path):
        self.user_id = user_id
        self.file_path = file_path