from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from collections.abc import AsyncGenerator
from app.config import settings  

# ------------------------------------------------------
# URL de conexão ao banco (pegando do config.py)
# ------------------------------------------------------
DATABASE_URL = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# ------------------------------------------------------
# Criação da Engine assíncrona
# ------------------------------------------------------
engine = create_async_engine(
    DATABASE_URL,
    echo=True,            # Mostra as queries no console (ótimo para debug)
    future=True,          # Usa a 2.0-style API do SQLAlchemy
    pool_size=10,         # Tamanho do pool de conexões
    max_overflow=20       # Conexões extras além do pool_size
)

# ------------------------------------------------------
# Criação da Session Factory
# ------------------------------------------------------
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,   # Mantém objetos acessíveis após commit
)

# ------------------------------------------------------
# Base para os modelos ORM
# ------------------------------------------------------
Base = declarative_base()

# ------------------------------------------------------
# Dependência para FastAPI
# Cada request recebe uma sessão isolada
# ------------------------------------------------------
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

# ------------------------------------------------------
# Exporta apenas o necessário
# ------------------------------------------------------
__all__ = ["Base", "engine", "async_session_maker", "get_session"]
