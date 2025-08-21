from typing import Union

from fastapi import FastAPI
from database import engine, Base
from models import usuario, marca
from routes import marca as marca_routes


# Crear las tablas en la BD
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(marca_routes.router)


@app.get("/")
def read_root():
    return {"Hello": "Mundo!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
