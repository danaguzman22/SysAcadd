from dataclasses import dataclass
from .universidad import Universidad

@dataclass(init=False, repr=True, eq=True)
class Facultad():
    universidad : Universidad
    nombre : str
    abreviatura : str
    directorio : str
    codigoPostal : str
    ciudad : str
    domicilio : str
    telefono : str
    contacto :  str 
    email : str