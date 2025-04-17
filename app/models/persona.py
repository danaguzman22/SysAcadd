from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento():
    tipoDocumento : str

@dataclass(init=False, repr=True, eq=True)    
class Persona():
        t_Documento = TipoDocumento()
        apellido : str
        nombre : str
        nroDocumento : str
        tipoDocumento = t_Documento
        fechaNacimiento : str
        sexo : str

