# app/models/__init__.py

from app.database import Base

# Importa todos os modelos para que o Alembic reconheça
from app.models.user import User
from app.models.event import Event
from app.models.event_participant import EventParticipant
from app.models.presence import Presence
from app.models.user_embedding import UserEmbedding
from app.models.user_imgs import UserImage

# Se quiser facilitar, você pode expor todos no __all__
__all__ = [
    "User",
    "UserImage",
    "Event",
    "EventParticipant",
    "Presence",
    "UserEmbedding",
    "Base",
]
