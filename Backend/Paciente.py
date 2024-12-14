class Paciente:
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


    def añadir_sintomas_graves(self, sintomas_graves: List[str]):
        """
        Añade una lista de síntomas graves al atributo 'síntomas' del paciente.
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

    def añadir_sintomas_generales(self, sintomas_generales: List[str]):
        """
        Añade una lista de síntomas generales al atributo 'síntomas' del paciente.
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




