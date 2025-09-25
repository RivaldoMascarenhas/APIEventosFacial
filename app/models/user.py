from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

cascade = "all, delete-orphan"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    matricula = Column(String(50), unique=True, index=True, nullable=False)  # ajuste conforme padrão real
    hashed_password = Column(CHAR(60), nullable=True)  # hash fixo (bcrypt)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)   # definido via LDAP
    is_organizer = Column(Boolean, default=False)  # atribuído por admin

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relações
    embeddings = relationship("UserEmbedding", back_populates="user", cascade=cascade)
    presences = relationship("Presence", back_populates="user", cascade=cascade)
    event_participations = relationship("EventParticipant", back_populates="user", cascade=cascade)


    def __repr__(self):
        return (
            f"User(id={self.id}, full_name={self.full_name}, email={self.email}, "
            f"matricula={self.matricula}, is_admin={self.is_admin}, is_organizer={self.is_organizer})"
        )

def __init__(self, full_name, email, matricula, hashed_password, is_admin=False, is_organizer=False):
    self.full_name = full_name
    self.email = email
    self.matricula = matricula
    self.hashed_password = hashed_password
    self.is_admin = is_admin
    self.is_organizer = is_organizer