from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# Tipos.

class Paciente:
  def __init__(self):
    pass

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
def paciente(req: Request):
  return templates.TemplateResponse(
    name='verqr.html', context={'request': req}
  )

@app.get('/datos_paciente/{id}')
def datos_paciente(id: int):
  print(f'cargando datos de paciente {id}')
  return {'id': id}

app.mount('/static', StaticFiles(directory='static', html=True), name='static')

# Páginas paciente.

@app.get('/paciente/{id}', response_class=HTMLResponse)
def paciente(req: Request, id: str):
  pac = Paciente()
  return templates.TemplateResponse(
    name='paciente.html',
    context={'request': req, 'pac': pac}
  )

  
@app.post('/guardar_paciente')
def guardar_paciente(id: Annotated[str, Form()],
                     nombre: Annotated[str, Form()]):
  print('guardando datos de paciente')
  print('redirigiendo a QR de paciente')
  return RedirectResponse(f'verqr?id={id}', status_code=303) # POST->GET

# Páginas especialista.

@app.get('/especialista/{pac_id}', response_class=HTMLResponse)
def paciente(req: Request, pac_id: int):
  pac = Paciente()
  return templates.TemplateResponse(
    name='especialista.html',
    context={'request': req, 'pac': pac}
  )
