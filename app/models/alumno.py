from dataclasses import dataclass
from .persona import Persona

@dataclass (init=False, repr=True, eq=True)
class Alumno(Persona):
    nroLegajo : str
    fechaIngreso : str
