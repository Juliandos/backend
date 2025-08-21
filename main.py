from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from models import usuario, marca
from routes import marca as marca_routes
from routes import usuario as usuario_routes
from routes import auth as auth_routes

# Crear las tablas en la BD
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],    # Permite todos los métodos: GET, POST, PUT, DELETE...
    allow_headers=["*"],    # Permite todos los headers
)

app.include_router(marca_routes.router)
app.include_router(usuario_routes.router)
app.include_router(auth_routes.router)



@app.get("/")
def read_root():
    return {"Hello": "Mundo!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
