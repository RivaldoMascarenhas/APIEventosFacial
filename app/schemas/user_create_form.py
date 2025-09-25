from fastapi import Form, HTTPException, status
from typing import Optional
from pydantic import EmailStr
from .users_schema import validar_cpf  

class UserCreateForm:
    def __init__(
        self,
        full_name: str = Form(...),   # Obrigatório
        matricula: str = Form(...),   # Obrigatório
        email: Optional[EmailStr] = Form(None),  # Opcional
        cpf: Optional[str] = Form(None),         # Opcional
        password: Optional[str] = Form(None),    # Opcional
        is_admin: Optional[bool] = Form(False), 
        is_organizer: Optional[bool] = Form(False),
    ):
        # --- Validações ---
        if cpf and not validar_cpf(cpf):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="CPF inválido."
            )
        if not matricula.strip() or not matricula.isdigit():
            raise ValueError("Matrícula deve conter apenas números")
        if password and (not password.strip() or len(password) < 6):
            raise ValueError("Senha deve ter pelo menos 6 caracteres")

        # --- Atribuições ---
        self.full_name = full_name
        self.email = email
        self.cpf = cpf
        self.matricula = matricula
        self.password = password
        self.is_admin = is_admin
        self.is_organizer = is_organizer

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "cpf": self.cpf,
            "matricula": self.matricula,
            "password": self.password,
            "is_admin": self.is_admin,
            "is_organizer": self.is_organizer,
        }
