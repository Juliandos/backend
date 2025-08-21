from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# -------- Base --------
class MarcaBase(BaseModel):
    nombre: str
    titular: str
    estado: Optional[bool] = True


# -------- Create --------
class MarcaCreate(MarcaBase):
    usuarios_id: int   # Relación con usuario


# -------- Update --------
class MarcaUpdate(BaseModel):
    nombre: Optional[str] = None
    titular: Optional[str] = None
    estado: Optional[bool] = None


# -------- Response --------
class MarcaResponse(MarcaBase):
    id: int
    usuarios_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True   # 🔑 Permite convertir desde SQLAlchemy a Pydantic
