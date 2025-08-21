from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.marca import Marca
from schemas.marca import MarcaCreate, MarcaResponse, MarcaUpdate

router = APIRouter(
    prefix="/marcas",
    tags=["marcas"]
)


# ------- CREATE -------
@router.post("/", response_model=MarcaResponse)
def create_marca(marca: MarcaCreate, db: Session = Depends(get_db)):
    nueva_marca = Marca(**marca.dict())
    db.add(nueva_marca)
    db.commit()
    db.refresh(nueva_marca)
    return nueva_marca


# ------- READ ALL -------
@router.get("/", response_model=List[MarcaResponse])
def get_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()


# ------- READ ONE -------
@router.get("/{marca_id}", response_model=MarcaResponse)
def get_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return marca


# ------- UPDATE -------
@router.put("/{marca_id}", response_model=MarcaResponse)
def update_marca(marca_id: int, marca_update: MarcaUpdate, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")

    for key, value in marca_update.dict(exclude_unset=True).items():
        setattr(marca, key, value)

    db.commit()
    db.refresh(marca)
    return marca


# ------- DELETE -------
@router.delete("/{marca_id}")
def delete_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == marca_id).first()
    if not marca:
        raise HTTPException(status_code=404, detail="Marca no encontrada")

    db.delete(marca)
    db.commit()
    return {"msg": "Marca eliminada correctamente"}
