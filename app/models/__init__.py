# app/models/__init__.py

from app.database import Base

# Importa todos os modelos para que o Alembic reconheça
from app.models.user import User
from app.models.event import Event
from app.models.eventParticipant import EventParticipant
from app.models.presence import Presence
from app.models.userEmbedding import UserEmbedding

# Se quiser facilitar, você pode expor todos no __all__
__all__ = [
    "User",
    "Event",
    "EventParticipant",
    "Presence",
    "UserEmbedding",
    "Base",
]
