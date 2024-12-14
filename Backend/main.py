from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.post('/guardar_paciente')
def guardar_paciente(id: Annotated[str, Form()],
                     nombre: Annotated[str, Form()]):
  return {'id': id, 'nombre': nombre}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

app.mount('/', StaticFiles(directory='static', html=True), name='static')
