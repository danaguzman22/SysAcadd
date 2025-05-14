from dataclasses import dataclass
from .facultad import Facultad
from .cargos import Cargo

@dataclass (init=False, repr=True, eq=True)
class Autoridad:
    nombre : str
    cargo : Cargo 
    telefono : str
    email : str
    facultad : Facultad 
