from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from patient import Patient, cargar_paciente, NOMBRES_TRATS

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
async def guardar_sintomas(req: Request, dest: str = '', correr_algo: bool = False):
  async with req.form() as form:
    id = form['id']
    pac = cargar_paciente(id)
    print('guardando síntomas de paciente')
    for sin_name in pac.sintomas.keys():
      new_val = sin_name in form
      pac.sintomas[sin_name] = new_val
      print(f'{sin_name} -> {new_val}')
    print(f'actualizando otros a {form["altres"]}')
    pac.altres_sint = form['altres']
    if correr_algo:
      diagnostico = form['diagnostico']
      print(f'corriendo algoritmo para generar visita, diagnostico={diagnostico}')
      res_ix = pac.crear_visita(diagnostico) # diagnóstico
      algoritmo(pac, res_ix)
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
    pac.immunodeprimit = 'immunodeprimit' in form
    pac.fumador = 'fumador' in form
  print(f'redirigiendo a {dest}')
  return RedirectResponse(dest, status_code=303) # POST->GET

# Páginas especialista.

@app.get('/especialista/{pac_id}', response_class=HTMLResponse)
def paciente(req: Request, pac_id: int):
  pac = cargar_paciente(pac_id)
  return templates.TemplateResponse(
    name='especialista.html',
    context={'request': req, 'pac': pac, 'trat_names': NOMBRES_TRATS}
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
      context={'request': req, 'pac': pac, 'res': res, 'res_ix': res_id, 'trat_names': NOMBRES_TRATS }
    )
  except IndexError:
    return RedirectResponse(f'/urgencia/{pac_id}', status_code=303) # POST->GET

@app.post('/guardar_trats')
async def guardar_trats(req: Request, dest: str):
  async with req.form() as form:
    pac_id = form['id']
    pac = cargar_paciente(pac_id)
    res_ix = int(form['res'])
    try:
      res = pac.urgencias[res_ix]
    except IndexError:
      print(f'no hemos encontrado res {res_ix} para paciente {pac_id}')
      return RedirectResponse('/', status_code=303) # POST->GET
    assig_trats = []
    print(f'guardando tratamientos de paciente en urgencia {res_ix}')
    for trat_name in pac.tratamientos.keys():
      new_val = trat_name in form
      pac.tratamientos[trat_name] = new_val
      print(f'{trat_name} -> {new_val}')
      if new_val:
        assig_trats.append(trat_name)
    res.tratamientos_dados = assig_trats
  print(f'redirigiendo a {dest}')
  return RedirectResponse(dest, status_code=303) # POST->GET


#Algoritmo

def algoritmo(paciente: Patient, vis_id: int):
    """
    Define el algoritmo de tratamiento basado en el diagnóstico del paciente, su condición y los resultados de las pruebas.
    """
    vis = paciente.urgencias[vis_id]
    print(vis.diagnostico)

    # Verifica si el diagnóstico es concreto o no
    if vis.diagnostico == "concret_no_pneumo":
        print("El diagnóstico es específico pero no neumonía. No aplica un tratamiento específico.")
        return

    # Lógica específica para neumonía
    if vis.diagnostico == "concret_pneumo":

        # Verifica el estado inmunológico
        if paciente.immunodeprimit:
            if paciente.AgudMPID['virus']:
                print('Se detecta Virus Influenza')
                vis.tratamientos_algo.append('piperacilina_tazobactam')
                vis.tratamientos_algo.append('levofloxacino')
            if paciente.AgudMPID['cmv']:
                print('Sospecha de Citomegalovirus (CMV)')
                vis.tratamientos_algo.append('ganciclovir')
            if paciente.AgudMPID["pneumocystis jirovecii"]:
                print('Sospecha de Pneumocystis jirovecii')
                vis.tratamientos_algo.append('sulfametoxazol_trimetoprim')
                vis.tratamientos_algo.append('ac_folic')
        elif not paciente.immunodeprimit:
            if paciente.AgudMPID['virus']:
                print('Se detecta Virus Influenza')
                vis.tratamientos_algo.append('oseltamivir')
            else:
                print('Neumonía bacteriana')
                vis.tratamientos_algo.append('cefalosporina')
                vis.tratamientos_algo.append('levofloxacino')

    # Para diagnósticos no concretos
    elif vis.diagnostico == "no_concret":
        # Realiza estudios adicionales o pruebas para TEP (tromboembolismo pulmonar)
        paciente.AgudMPID['tromboembolisme_pulmonar'] == True

    if (paciente.MPID == True and
    paciente.simptomes['xiulets'] == False and
    paciente.simptomes['virus'] == False and
    paciente.simptomes['increment_mucositat'] == False and
    paciente.simptomes['tos_en_els_darrers_dies'] == False):
        vis.bronco = True
