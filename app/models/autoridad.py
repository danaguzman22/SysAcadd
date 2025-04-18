from dataclasses import dataclass
from .facultad import Facultad

@dataclass (init=False, repr=True, eq=True)
class Autoridad:
    nombre : str
    cargo : str 
    telefono : str
    email : str
    facultad : str 
