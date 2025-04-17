from dataclasses import dataclass


@dataclass (init=False, repr=True, eq=True)
class Universidad:
    universidad : str
    sigla : str
