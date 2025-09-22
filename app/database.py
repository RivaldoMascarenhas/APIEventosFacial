from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager
from app.config import settings  

# URL do banco vinda do config
DATABASE_URL = (
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Cria engine assíncrono
engine = create_async_engine(DATABASE_URL, echo=True, future=True, pool_size=10, max_overflow=20)

# Cria pool de conexões
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base para os models
Base = declarative_base()

# Dependência para FastAPI
@asynccontextmanager
async def get_session():
    session = async_session_maker()
    try:
        yield session
    finally:
        await session.close()
