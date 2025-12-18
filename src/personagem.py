"""Classe Personagem e sua lógica."""

from .elementos import Elemento


class Personagem:
    """
    Representa um personagem na arena de batalha.

    Attributes:
        nome: Nome do personagem
        classe: Classe/profissão do personagem
        hp: Hit Points iniciais (e máximos)
        ataque: Poder de ataque
        defesa: Poder de defesa
    """

    def __init__(
        self,
        nome: str,
        classe: str,
        hp: int,
        ataque: int,
        defesa: int,
        elemento: Elemento = Elemento.NENHUM
    ):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.elemento = elemento
