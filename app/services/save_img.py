import os
from fastapi import UploadFile
from app.config import settings
import aiofiles

BASE_DIR = settings.BASE_DIR

async def save_user_image(user_id: int, image: UploadFile):
    """
    Salva uma imagem de usuário de forma assíncrona no disco.

    Args:
        user_id (int): O ID do usuário para criar a pasta.
        image (UploadFile): O objeto de arquivo de upload do FastAPI.

    Returns:
        str: O caminho completo para o arquivo salvo.
    """
    # Cria a pasta por usuário (esta operação é síncrona, mas aceitável
    # pois não é uma operação de I/O de arquivo em massa)
    user_folder = os.path.join(BASE_DIR, f"user_{user_id}")
    os.makedirs(user_folder, exist_ok=True)

    # Define o caminho do arquivo
    file_path = os.path.join(user_folder, image.filename)

    # Salva o arquivo de forma assíncrona
    async with aiofiles.open(file_path, "wb") as f:
        content = await image.read()
        await f.write(content)

    return file_path