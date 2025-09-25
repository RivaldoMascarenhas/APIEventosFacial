from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_session
from app.models.user import User
from app.schemas.users_schema import UserCreate, UserPublic
from app.config import bcrypt_context

router_users = APIRouter(prefix="/users", tags=["Users"])

@router_users.post("/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    """
    Cria um novo usuário no banco de dados.
    """
    query = select(User).where(
        (User.email == user.email) | (User.matricula == user.matricula)
    )
    result = await session.execute(query)
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"error": "User with this email or matricula already exists."}
        )

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        matricula=user.matricula,
        hashed_password=bcrypt_context.hash(user.password), 
        is_admin=user.is_admin,
        is_organizer=user.is_organizer
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user

@router_users.get("/", response_model=list[UserPublic])
async def get_users(session: AsyncSession = Depends(get_session)):
    """
    Retorna a lista de todos os usuários.
    """
    query = select(User)
    result = await session.execute(query)
    users = result.scalars().all()
    return users

@router_users.get("/{user_id}", response_model=UserPublic)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    """
    Busca um usuário pelo ID.
    """
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "User not found."} 
        )
    return user

@router_users.get("/by-matricula/{matricula}", response_model=UserPublic)
async def get_user_by_matricula(matricula: str, session: AsyncSession = Depends(get_session)):
    """
    Busca um usuário pela matrícula.
    """
    query = select(User).where(User.matricula == matricula)
    result = await session.execute(query)
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= {"error": "User not found."}
        )
    return user
