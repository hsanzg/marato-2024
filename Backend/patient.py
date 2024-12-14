class Patient:
  def __init__(self, id):
    self.id = 1
    self.nombre = 'Juan García López'
    self.síntomas: ([
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
    self.tratamientos_si = ([
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
    self.tratamientos_no = ([
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
    self.pruebas = []
    self.malalties = (
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
                self.síntomas.append(sintoma)


unico_paciente = Patient(1)

def cargar_paciente(id: int) -> Patient:
  print(f'cargando info de paciente {id}')
  return unico_paciente
