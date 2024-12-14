from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict


class Visita:
  def __init__(self, tratamientos_dados, tratamientos_algo):
    self.tratamientos_dados = tratamientos_dados
    self.tratamientos_algo = tratamientos_algo
    self.fecha = datetime.now()

class Patient:
  def __init__(self, id):
    self.id = 1
    self.nombre = 'Juan García López'
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
      # Información introducïda por el médico de urgéncia
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
    self.urgencias = [
      Visita(
        tratamientos_dados=['Cefalosporina 3ª generació'],
        tratamientos_algo=['Cefalosporina 3ª generació'],
      )
    ]
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

    def introducir_sintomas_graves(self, sintomas_graves: [str]):
        """
        Añade una lista de síntomas graves al atributo 'síntomas' del paciente.
        Esta función es llamada por el médico de urgencia solamente.
        """
        sintomas_a_agregar = [
            "Febre",
            "Desaturació",
            "Increment respiracions per minut o respiracions per minut > 19",
            "Tiratge muscular per respirar",
            "Ofeg en repòs",
            "Auscultació de xiulets (sibilants) o altres sorolls diferents als que té el pacient de base",
            "To blau distal als dits o llavis"
        ]
        for sintoma in sintomas_graves:
            if sintoma in sintomas_a_agregar and sintoma not in self.síntomas:
                self.síntomas.append(sintoma)

    def introducir_sintomas_generales(self, sintomas_generales: [str]):
        """
        Añade una lista de síntomas generales al atributo 'síntomas' del paciente.
        Esta función es llamada por el médico especialista o por el paciente
        """
        sintomas_a_agregar = [
            "Increment o aparició d’ofeg i/o tos en els darrers dies (maxim darreres 2 setmanes), sense altres símptomes o amb altres símptomes",
            "Increment mucositat i congestió nasal",
            "Increment mucositat i dolor gola",
            "Increment mucositat i febre",
            "Dolor toràcic",
            "Xiulets",
            "Increment de la mucositat, mal estat general, +/- congestió nasal o dolor gola",
            "Dolor toràcic e. increment d’ofec sense tos ni altres símptomes"
        ]
        for sintoma in sintomas_generales:
            if sintoma in sintomas_a_agregar and sintoma not in self.síntomas:
                self.sintomas.append(sintoma)


unico_paciente = Patient(1)

def cargar_paciente(id: int) -> Patient:
  print(f'cargando info de paciente {id}')
  return unico_paciente
