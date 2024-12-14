from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
@dataclass
class Pacient:
    id: uuid.UUID
    nombre: str
    síntomas: List[str] = ([
    #Información introducida por el médico de urgéncia y/o el paciente
    "Increment o aparició d’ofeg i/o tos en els darrers dies (màxim darreres 2 setmanes), sense altres símptomes o amb altres símptomes",
    "Increment mucositat i congestió nasal",
    "Increment mucositat i dolor gola",
    "Increment mucositat i febre",
    "Dolor toràcic",
    "Xiulets",
    "Increment de la mucositat, mal estat general, +/- congestió nasal o dolor gola",
    "Dolor toràcic e increment d’ofec sense tos ni altres símptomes",

    # Información introducïda por el médico de urgéncia
    "Febre",
    "Desaturació",
    "Increment respiracions per minut o respiracions per minut > 19",
    "Tiratge muscular per respirar",
    "Ofeg en repòs",
    "Auscultació de xiulets (sibilants) o altres sorolls diferents als que té el pacient de base",
    "To blau distal als dits o llavis"
])
    medicaments_si: List[str]
    medicaments_no: List[str]
    pruebas: List[str]
    malalties: List[str] = (
        ["Infeccions", [
            "Virus",
            "Fongs",
            "Bacteris",
            "Oportunistes (CMV, Pneumocystis jirovecii, micobacteris tuberculoses i atípics)"
        ],
        "Insuficiència cardíaca esquerra",
        "Tromboembolisme pulmonar (inclosa embòlia grassa)",
        "Fàrmacs",
        "Transfusió de sang",
        "Inhalació aguda de tòxics pulmonars",
        "Reflux gastroesofàgic (RGE)",
        "Causes d’abdomen agut (pancreatitis, apendicitis, peritonitis, etc.)",
        "Intervencions quirúrgiques en les setmanes prèvies",
        "Procediments invasius (endoscòpia, radioteràpia) en les setmanes prèvies",
        "Pneumotòrax",
        "Contusió pulmonar",
        "Exacerbació aguda (ExA) de la malaltia pulmonar intersticial de base (com en la FPI)"]
    )
  
@app.post('/guardar_paciente')
def guardar_paciente(id: Annotated[str, Form()],
                     nombre: Annotated[str, Form()]):
  print('guardando datos de paciente')
  print('redirigiendo a QR de paciente')
  #return {'id': id, 'nombre': nombre}
  return RedirectResponse(f'verqr.html?id={id}')

@app.get('/datos_especialista/{id_paciente}')
def datos_especialista(id_paciente: int):
  print(f'cargando datos de paciente {id_paciente} para especialista')
  return {'id': id_paciente}

@app.get('/datos_urgencia/{id_paciente}')
def datos_urgencia(id_paciente: int):
  print(f'cargando datos de paciente {id_paciente} para urgencia')
  return {'id': id_paciente}

@app.get('/datos_paciente/{id}')
def datos_paciente(id: int):
  print(f'cargando datos de paciente {id} para paciente')
  return {'id': id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

app.mount('/', StaticFiles(directory='static', html=True), name='static')
