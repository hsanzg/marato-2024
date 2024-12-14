from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.post('/guardar_paciente')
def guardar_paciente(id: Annotated[str, Form()],
                     nombre: Annotated[str, Form()]):
  print('guardando datos de paciente')
  print('redirigiendo a QR de paciente')
  #return {'id': id, 'nombre': nombre}
  return RedirectResponse(f'verqr.html?id={id}')

@app.get('/datos_especialista.html')
def datos_especialista(id_paciente: Annotated[str, Form()]):
  print(f'cargando datos de paciente {id_paciente} para especialista')
  return {'id': id_paciente}

@app.get('/datos_urgencia.html')
def datos_urgencia(id_paciente: Annotated[str, Form()]):
  print(f'cargando datos de paciente {id_paciente} para urgencia')
  return {'id': id_paciente}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

app.mount('/', StaticFiles(directory='static', html=True), name='static')
