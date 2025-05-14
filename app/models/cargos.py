
from dataclasses import dataclass

@dataclass (init=False, repr=True, eq=True)
class Categoria:
    nombre : str
    puntos : str

@dataclass (init=False, repr=True, eq=True)
class TipoDedicacion:
    nombre : str
    observaciones : str

@dataclass (init=False, repr=True, eq=True)
class Cargo:
    nombre : str
    puntos : str
    categoria : Categoria
    tipo_dedicacion : TipoDedicacion

