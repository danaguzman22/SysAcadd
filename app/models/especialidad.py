from dataclasses import dataclass
from .tipoespecialidad import TipoEspecialidad

dataclass  (init=False, repr=True, eq=True)

class Especialidad():
    nombre: str
    letra: str
    observaciones: str

@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad():
    nombre: str
    nivel : str