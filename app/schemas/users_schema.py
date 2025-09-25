from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class UserBase(BaseModel):
    full_name: str = Field(..., min_length=1, description="Nome completo do usuário")
    email: EmailStr = Field(..., description="E-mail válido")
    matricula: str = Field(..., min_length=1, description="Número da matrícula")
    is_admin: bool = Field(False, description="Flag de administrador")
    is_organizer: bool = Field(False, description="Flag de organizador")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Senha em texto (será hasheada no servidor)")

    # Novo estilo de validação em Pydantic v2
    @field_validator("password")
    def password_not_blank(cls, v: str):
        if not v.strip():
            raise ValueError("password must not be empty")
        return v

class UserPublic(UserBase):
    id: int

    class Config:
        from_attributes = True  # Usar os campos da classe como atributos

# (opcional) Para uso interno
class UserInDB(UserPublic):
    hashed_password: str
