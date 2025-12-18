from dataclasses import dataclass

from .personagem import Personagem
from .elementos import Elemento


@dataclass
class ResultadoAtaque:
    """Resultado de um ataque executado."""
    atacante: str
    defensor: str
    dano: int
    defensor_hp_restante: int
    defensor_derrotado: bool
    mensagem: str

    def __str__(self) -> str:
        return self.mensagem


class SistemaCombate:
    """
    Sistema de combate entre personagens.

    Regras:
    - Dano base = ataque - defesa (mínimo 1)
    - Fraqueza elemental: +50% dano
    - Resistência elemental: -50% dano

    Attributes:
        multiplicador_fraqueza: Multiplicador de fraqueza (default: 1.5)
        multiplicador_resistencia: Multiplicador de resistência (default: 0.5)
    """

    def __init__(
        self,
        multiplicador_fraqueza: float = 1.5,
        multiplicador_resistencia: float = 0.5
    ):
        self.multiplicador_fraqueza = multiplicador_fraqueza
        self.multiplicador_resistencia = multiplicador_resistencia
