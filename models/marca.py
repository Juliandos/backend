from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Marca(Base):
    __tablename__ = "marca"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    titular = Column(String(100), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    usuarios_id = Column(Integer, ForeignKey("usuario.id"))

    # Relación con usuario
    usuario = relationship("Usuario", back_populates="marcas")
