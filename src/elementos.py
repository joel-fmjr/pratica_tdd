from enum import Enum, auto


class Elemento(Enum):
    """Elementos disponíveis no sistema de combate."""
    NENHUM = auto()
    FOGO = auto()
    GELO = auto()
    RAIO = auto()
