from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento():
    tipoDocumento : str

@dataclass(init=False, repr=True, eq=True)    
class Persona():
        apellido : str
        nombre : str
        nroDocumento : str
        tipoDocumento : TipoDocumento
        fechaNacimiento : str
        sexo : str

