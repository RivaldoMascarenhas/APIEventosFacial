from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env automaticamente
load_dotenv()

class Settings(BaseSettings):
    # Banco de Dados
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str

    # Segurança (exemplo para JWT depois)
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instância global para usar no projeto
settings = Settings()
