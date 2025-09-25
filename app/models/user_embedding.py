from sqlalchemy import Column, Integer, ForeignKey, LargeBinary, DateTime
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

EMBEDDING_DIM = 512  # pode parametrizar em config se quiser flexibilidade

class UserEmbedding(Base):
    __tablename__ = "user_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    embedding = Column(Vector(EMBEDDING_DIM), nullable=False)  # embedding não deveria ser nulo
    image = Column(LargeBinary, nullable=True)  # opcional, mas atenção ao tamanho
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relação
    user = relationship("User", back_populates="embeddings", passive_deletes=True) 

    def __repr__(self):
        preview = str(self.embedding[:5]) + "..." if self.embedding is not None else None
        return f"UserEmbedding(id={self.id}, user_id={self.user_id}, embedding={preview})"

    def __init__(self, user_id, embedding):
        self.user_id = user_id
        if embedding is None:
            raise ValueError("Embedding não pode ser None. Verifique o pipeline de reconhecimento facial.")
        self.embedding = embedding