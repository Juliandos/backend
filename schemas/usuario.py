from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from schemas.marca import MarcaResponse


# -------- Base --------
class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr


# -------- Create --------
class UsuarioCreate(UsuarioBase):
    password: str


# -------- Update --------
class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    password: Optional[str] = None


# -------- Response --------
class UsuarioResponse(UsuarioBase):
    id: int
    created_at: datetime
    updated_at: datetime
    marcas: List[MarcaResponse] = []   # relación con Marca

    class Config:
        from_attributes = True
