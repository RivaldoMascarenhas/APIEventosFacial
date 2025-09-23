from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    matricula = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True)  # apenas para não-LDAP
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)  # definido via LDAP, não pelo app
    is_organizer = Column(Boolean, default=False)  # atribuído por admin

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relações
    embeddings = relationship("UserEmbedding", back_populates="user")
    presences = relationship("Presence", back_populates="user")

    def __init__(self, full_name, email, matricula, hashed_password=None, is_admin=False, is_organizer=False):
        self.full_name = full_name
        self.email = email
        self.matricula = matricula
        self.hashed_password = hashed_password
        self.is_admin = is_admin
        self.is_organizer = is_organizer
    def __repr__(self):
        return f"User(id={self.id}, full_name={self.full_name}, email={self.email}, matricula={self.matricula}, is_admin={self.is_admin}, is_organizer={self.is_organizer})"