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

@app.post('/guardar_sintomas')
async def guardar_sintomas(req: Request, dest: str = '', correr_algo: bool = False, diag: str = ''):
  async with req.form() as form:
    id = form['id']
    pac = cargar_paciente(id)
    print('guardando síntomas de paciente')
    for sin_name in pac.sintomas.keys():
      new_val = sin_name in form
      pac.sintomas[sin_name] = new_val
      print(f'{sin_name} -> {new_val}')
  if correr_algo:
    print('corriendo algoritmo para generar visita')
    res_ix = pac.crear_visita(diag) # diagnóstico
    dest = f'/resultado/{id}/{res_ix}'
  print(f'redirigiendo a {dest}')
  return RedirectResponse(dest, status_code=303) # POST->GET

# En realidad es para guardar AgudMPID (Causes d’agudització)
@app.post('/guardar_malalties')
async def guardar_malalties(req: Request, dest: str):
  async with req.form() as form:
    id = form['id']
    pac = cargar_paciente(id)
    print('guardando AgudMPID de paciente')
    for sin_name in pac.AgudMPID.keys():
      new_val = sin_name in form
      pac.AgudMPID[sin_name] = new_val
      print(f'{sin_name} -> {new_val}')
  print(f'redirigiendo a {dest}')
  return RedirectResponse(dest, status_code=303) # POST->GET

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


@app.get('/resultado/{pac_id}/{res_id}', response_class=HTMLResponse)
def resultado(req: Request, pac_id: int, res_id: int):
  pac = cargar_paciente(pac_id)
  try:
    res = pac.urgencias[res_id]
    return templates.TemplateResponse(
      name='resultado.html',
      context={'request': req, 'pac': pac, 'res': res}
    )
  except IndexError:
    return RedirectResponse(f'/urgencia/{pac_id}', status_code=303) # POST->GET


#Algoritmo

def Algoritmo(paciente: Patient):
    """
    Define el algoritmo de tratamiento basado en el diagnóstico del paciente, su condición y los resultados de las pruebas.
    """

    # Verifica si el diagnóstico es concreto o no
    if paciente.visita[-1].diagnostico == "Concreto pero no pneumonia":
        #print("El diagnóstico es específico pero no neumonía. No aplica un tratamiento específico.")
        return

    # Lógica específica para neumonía
    if paciente.visita[-1].diagnostico == "Pneumonia":

        # Verifica el estado inmunológico
        if paciente.immunodeprimit == 1:
            if paciente.AgudMPID["Virus"]:
                # Se detecta Virus Influenza
                paciente.tratamientos_algo['Piperacilina/Tazobactam 4g/0,5g cada 8h e.v.'] = True
                paciente.tratamientos_algo['Levofloxacino 500mg/24h v.o.'] = True
            elif paciente.AgudMPID["CMV"]:
                # Sospecha de Citomegalovirus (CMV)
                paciente.tratamientos_algo['Ganciclovir 5mg/Kg pes/12h e.v.'] = True
            elif paciente.AgudMPID["Pneumocystis jirovecii"]:
                # Sospecha de Pneumocystis jirovecii
                paciente.tratamientos_algo['Sulfametoxazol/trimetoprim 800/160 mg/12h v.o.'] = True
                paciente.tratamientos_algo['Àc. Fòlic'] = True

        elif paciente.immunodeprimit == 0:
            if paciente.AgudMPID["Virus"]:
                # Se detecta Virus Influenza
                paciente.tratamientos_algo['Oseltamivir 75mg/12h v.o.'] = True
            else:
                # Neumonía bacteriana
                paciente.tratamientos_algo['Cefalosporina 3ª generació'] = True
                paciente.tratamientos_algo['Levofloxacino 500mg/24h v.o.'] = True

    # Para diagnósticos no concretos
    elif paciente.visita.diagnostico == "No Concreto":
        # Realiza estudios adicionales o pruebas para TEP (tromboembolismo pulmonar)
        paciente.AgudMPID["Tromboembolisme pulmonar (inclosa embòlia grassa)"] == True

    if (paciente.MPID == True and
    paciente.simptomes['xiulets'] == False and
    paciente.simptomes['virus'] == False and
    paciente.simptomes['increment_mucositat'] == False and
    paciente.simptomes['tos_en_els_darrers_dies'] == False):
        paciente.visita[-1].bronco = 1
