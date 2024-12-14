from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict

# Tipos de diagnóstico:
# - concret_pneumo
# - concret_no_pneumo
# - no_concret


class Visita:
  def __init__(self, diagnostico: str):
    self.diagnostico = diagnostico
    self.fecha = datetime.now()
    # A rellenar por el algoritmo.
    self.tratamientos_dados = []
    self.tratamientos_algo = []

class Patient:
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre
    self.sintomas = {
      # Información introducida por el médico de urgéncia y/o el paciente.
      'increment_o_aparcio_ofeg': False,
      'tos_en_els_darrers_dies': True,
      'increment_mucositat': False,
      'congestio_nasal': False,
      'dolor_gola': False,
      'febre': False,
      'dolor_toracic': False,
      'xiulets': False,
      'mal_estat_general': False,
      'altres_simptomes': False,
      # Información introducida por el médico de urgéncia.
      "desaturacio": False,
      "increment_respiracions": False, #  per minut o respiracions per minut > 19
      "tiratge_muscular_per_respirar": False,
      "ofeg_en_repos": False,
      "auscultacio_de_xiulets": False, #  (sibilants) o altres sorolls diferents als que té el pacient de base
      "to_blau_distal": False # als dits o llavis
    }
    self.tratamientos = {
      'Piperacilina/Tazobactam 4g/0,5g cada 8h e.v.': False,
      'Cefalosporina 3ª generació': False,
      'Levofloxacino 500mg/24h v.o.': True,
      'Oseltamivir 75mg/12h v.o.': False,
      'Ganciclovir 5mg/Kg pes/12h e.v.': True,
      'Sulfametoxazol/trimetoprim 800/160 mg/12h v.o.': False,
      'Àc. Fòlic': False,
      'Omeprazol 20mg/12-24h e.v.': False,
      'N-acetilcisteïna 600mg/8h v.o.': False,
      'Morfina 2,5-5mg s.c.': False,
      'Bemiparina 2500-3500 UI/0,2 mL (segons Kg pes) s.c./dia': False,
      'Metilprednisolona 1-2 mg/Kg pes/d e.v.': False,
      'Losartan 50mg/24h v.o.': False,
      'Calci + Vitamina D 500mg/400 UI 2comp/d v.o.': False,
      'Tinzaparina 20000UI/0,5-0,9 mL (segons Kg pes)': False
    }
    self.urgencias = []
    self.pruebas = []
    self.AgudMPID = {
            "Virus": False,
            "CMV": False,
            "Pneumocystis jirovecii": False,
            "Insuficiència cardíaca esquerra": False,
            "Tromboembolisme pulmonar (inclosa embòlia grassa)": False,
            "Fàrmacs": False,
            "Transfusió de sang": False,
            "Inhalació aguda de tòxics pulmonars": False,
            "Reflux gastroesofàgic (RGE)": False,
            "Causes d’abdomen agut (pancreatitis, apendicitis, peritonitis, etc.)": False,
            "Intervencions quirúrgiques en les setmanes prèvies": False,
            "Procediments invasius (endoscòpia, radioteràpia) en les setmanes prèvies": False,
            "Pneumotòrax": False,
            "Contusió pulmonar": False,
            "Exacerbació aguda (ExA) de la malaltia pulmonar intersticial de base (com en la FPI)": False
        }

  def crear_visita(self, diagnostico: str) -> int:
    new_ix = len(self.urgencias)
    self.urgencias.append(Visita(diagnostico))
    return new_ix


pacientes = [
  Patient(0, 'Juan García López'),
  Patient(1, 'Ana María Gómez Paiporta'),
  Patient(2, 'Andreu Serra Marroig')
]


def cargar_paciente(id: str | int) -> Patient:
  print(f'cargando info de paciente {id}')
  try:
    act_id = int(id)
    return pacientes[act_id]
  except (ValueError, IndexError):
    print(f'-> no existe, devolviendo primero')
    return pacientes[0]
