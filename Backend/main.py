from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from patient import Patient, cargar_paciente

# Tipos.

app = FastAPI()
templates = Jinja2Templates(directory='templates')

# Páginas comunes.

@app.get('/', response_class=HTMLResponse)
def index(req: Request):
  return templates.TemplateResponse(
    name='index.html', context={'request': req}
  )

@app.get('/leerqr', response_class=HTMLResponse)
def paciente(req: Request):
  return templates.TemplateResponse(
    name='leerqr.html', context={'request': req}
  )

@app.get('/verqr', response_class=HTMLResponse)
def paciente(req: Request, id: int):
  pac = cargar_paciente(id)
  return templates.TemplateResponse(
    name='verqr.html', context={'request': req, 'nombrePac': pac.nombre}
  )

# deprecado, intentar no usar.
@app.get('/datos_paciente/{id}')
def datos_paciente(id: int):
  print(f'cargando datos de paciente {id}')
  pat = cargar_paciente(id)
  return jsonable_encoder(pat)

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

# Páginas paciente.

@app.get('/paciente/{id}', response_class=HTMLResponse)
def paciente(req: Request, id: str):
  pac = cargar_paciente(id)
  return templates.TemplateResponse(
    name='paciente.html',
    context={'request': req, 'pac': pac}
  )

@app.post('/guardar_paciente')
async def guardar_paciente(req: Request):
  async with req.form() as form:
    id = form['id']
    pac = cargar_paciente(id)
    print('guardando datos de paciente')
    for sin_name in pac.sintomas.keys():
      new_val = sin_name in form
      pac.sintomas[sin_name] = new_val
      print(f'{sin_name} -> {new_val}')
  print('redirigiendo a QR de paciente')
  return RedirectResponse(f'verqr?id={id}', status_code=303) # POST->GET

# Páginas especialista.

@app.get('/especialista/{pac_id}', response_class=HTMLResponse)
def paciente(req: Request, pac_id: int):
  pac = cargar_paciente(pac_id)
  return templates.TemplateResponse(
    name='especialista.html',
    context={'request': req, 'pac': pac}
  )

# Páginas urgencia.

@app.get('/urgencia/{pac_id}', response_class=HTMLResponse)
def paciente(req: Request, pac_id: int):
  pac = cargar_paciente(pac_id)
  return templates.TemplateResponse(
    name='urgencia.html',
    context={'request': req, 'pac': pac}
  )
