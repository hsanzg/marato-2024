from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict

TRATAMIENTOS_DISPONIBLES = [
  'piperacilina_tazobactam', 'cefalosporina', 'levofloxacino', 'oseltamivir', 'ganciclovir', 'sulfametoxazol_trimetoprim', 'ac_folic', 'omeprazol', 'n_acetilcisteina', 'morfina', 'bemiparina', 'metilprednisolona', 'losartan', 'calci_vitamina_d', 'tinzaparina'
]

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
    self.bronco = True

class Patient:
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre
    self.immunodeprimit = False
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
    self.tratamientos = {nom: False for nom in TRATAMIENTOS_DISPONIBLES}
    self.urgencias = []
    self.pruebas = []
    self.MPID = False
    self.AgudMPID = {
      'virus': False,
      "cmv": False,
      "pneumocystis jirovecii": False,
      'insuficiencia_cardiaca_esquerra': False,
      'tromboembolisme_pulmonar': False,
      'farmacs': False,
      'transfusio_de_sang': False,
      'inhalacio_aguda_toxics_pulmonars': False,
      'reflux_gastroesofagic': False,
      'causes_abdomen_agut': False,
      'intervencions_quirurgiques_prèvies': False,
      'procediments_invasius_prèvies': False,
      'pneumotorax': False,
      'contusio_pulmonar': False,
      'exacerbacio_aguda':False
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
