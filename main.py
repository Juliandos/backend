from typing import Union

from fastapi import FastAPI
from database import engine, Base
from models import usuario, marca


# Crear las tablas en la BD
Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Mundo!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
