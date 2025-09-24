from sqlalchemy import Column, Integer, ForeignKey, LargeBinary, DateTime
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class UserEmbedding(Base):
    __tablename__ = "user_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    embedding = Column(Vector(512))  # InsightFace default = 512 dims
    image = Column(LargeBinary, nullable=True)  # guarda a imagem original
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relação
    user = relationship("User", back_populates="embeddings") 

    def __init__(self, user_id, embedding, image=None):
        self.user_id = user_id
        self.embedding = embedding
        self.image = image
    def __repr__(self):
        return f"UserEmbedding(id={self.id}, user_id={self.user_id}, embedding={self.embedding})"
