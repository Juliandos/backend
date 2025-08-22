from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from auth.security import get_password_hash, get_current_user
from database import get_db
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)


# ------- CREATE -------
@router.post("/", response_model=UsuarioResponse)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# ------- READ ALL -------
@router.get("/", response_model=List[UsuarioResponse])
def get_usuarios(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return db.query(Usuario).all()

# ------- READ ONE -------
@router.get("/{usuario_id}", response_model=UsuarioResponse)
def get_usuario(usuario_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# ------- UPDATE -------
@router.put("/{usuario_id}", response_model=UsuarioResponse)
def update_usuario(usuario_id: int, usuario_update: UsuarioUpdate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    for key, value in usuario_update.dict(exclude_unset=True).items():
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario

# ------- DELETE -------
@router.delete("/{usuario_id}")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()
    return {"msg": "Usuario eliminado correctamente"}

# ------- REGISTRO -------
@router.post("/registro", response_model=UsuarioResponse)
def create_user(user: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        # Verificar si ya existe
        db_user = db.query(Usuario).filter(Usuario.correo == user.correo).first()
        if db_user:
            raise HTTPException(status_code=400, detail="El correo ya está registrado")

        # Hashear contraseña
        hashed_pw = get_password_hash(user.password)

        new_user = Usuario(
            nombre=user.nombre,
            correo=user.correo,
            password=hashed_pw
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

