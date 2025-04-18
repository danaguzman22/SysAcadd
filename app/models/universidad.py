from dataclasses import dataclass


@dataclass (init=False, repr=True, eq=True)
class Universidad:
    nombre_universidad : str
    sigla : str
