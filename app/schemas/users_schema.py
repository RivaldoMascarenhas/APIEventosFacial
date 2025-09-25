from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))  # só números
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Valida dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True
class UserBase(BaseModel):
    full_name: str = Field(..., min_length=1, description="Nome completo do usuário")
    email: Optional[EmailStr] = Field(..., description="E-mail válido")
    cpf: Optional[str] = Field(..., min_length=11, description="CPF do usuário")
    matricula: str = Field(..., min_length=1, description="Número da matrícula")
    is_admin: Optional[bool] = Field(False, description="Flag de administrador")
    is_organizer: Optional[bool] = Field(False, description="Flag de organizador")

    @field_validator("cpf")
    def cpf_must_be_valid(cls, v: str):
        v = ''.join(filter(str.isdigit, v))
        if not validar_cpf(v):
            raise ValueError("CPF inválido.")
        return v
    @field_validator("matricula")
    def matricula_not_blank(cls, v: str):
        if not v.strip():
            raise ValueError("Matrícula não pode ser vazia")
        if not v.isdigit():
            raise ValueError("Matrícula deve conter apenas números")
        return v

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Senha em texto (será hasheada no servidor)")

    @field_validator("password")
    def password_not_blank(cls, v: str):
        if not v.strip():
            raise ValueError("password must not be empty")
        return v

class UserPublic(UserBase):
    id: int

    class Config:
        from_attributes = True  # Usar os campos da classe como atributos

class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=1, description="Nome completo do usuário")
    email: Optional[EmailStr] = Field(None, description="E-mail válido")
    matricula: Optional[str] = Field(None, min_length=1, description="Número da matrícula")
    is_admin: Optional[bool] = Field(None, description="Flag de administrador")
    is_organizer: Optional[bool] = Field(None, description="Flag de organizador")
