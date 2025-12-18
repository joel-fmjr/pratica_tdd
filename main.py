"""Demo interativa do sistema de batalha."""

from src.personagem import Personagem
from src.elementos import Elemento
from src.combate import SistemaCombate


def criar_personagens_exemplo():
    """Cria alguns personagens para demonstração."""
    return [
        Personagem(
            "Aragorn", "Guerreiro", hp=120, ataque=0, defesa=20,
            elemento=Elemento.NENHUM
        ),
        Personagem(
            "Gandalf", "Mago", hp=80, ataque=40, defesa=10,
            elemento=Elemento.FOGO
        ),
        Personagem(
            "Legolas", "Arqueiro", hp=90, ataque=30, defesa=15,
            elemento=Elemento.NENHUM
        ),
        Personagem(
            "Elsa", "Feiticeira", hp=70, ataque=35, defesa=12,
            elemento=Elemento.GELO
        ),
        Personagem(
            "Thor", "Deus", hp=150, ataque=45, defesa=25,
            elemento=Elemento.RAIO
        ),
    ]


def exibir_status(personagens: list[Personagem]):
    """Exibe o status de todos os personagens."""
    print("\n" + "=" * 50)
    print("STATUS DOS PERSONAGENS")
    print("=" * 50)

    for p in personagens:
        status = "💀" if not p.esta_vivo() else "❤️"
        elemento = (
            p.elemento.name if p.elemento != Elemento.NENHUM else "-"
        )
        print(
            f"{status} {p.nome:12} | HP: {p.hp:3}/{p.hp_maximo:3} | "
            f"ATK: {p.ataque:2} | DEF: {p.defesa:2} | Elem: {elemento}"
        )

    print("=" * 50)


def simular_batalha():
    """Simula uma batalha entre dois personagens."""
    personagens = criar_personagens_exemplo()
    combate = SistemaCombate()

    print("\n🎮 BEM-VINDO À ARENA DE BATALHA RPG! 🎮")
    exibir_status(personagens)

    # Selecionar lutadores
    gandalf = personagens[1]  # Mago de Fogo
    elsa = personagens[3]     # Feiticeira de Gelo

    print(f"\n⚔️  BATALHA: {gandalf} vs {elsa}  ⚔️")
    print("-" * 40)

    turno = 1
    while gandalf.esta_vivo() and elsa.esta_vivo():
        print(f"\n--- Turno {turno} ---")

        # Gandalf ataca
        if gandalf.esta_vivo():
            resultado = combate.atacar(gandalf, elsa)
            print(f"🔥 {resultado.mensagem}")

        # Elsa contra-ataca
        if elsa.esta_vivo():
            resultado = combate.atacar(elsa, gandalf)
            print(f"❄️  {resultado.mensagem}")

        turno += 1

        if turno > 20:  # Limite de turnos
            print("\n⏰ Batalha muito longa! Empate!")
            break

    print("\n" + "=" * 40)
    if not gandalf.esta_vivo():
        print(f"🏆 {elsa.nome} VENCEU!")
    elif not elsa.esta_vivo():
        print(f"🏆 {gandalf.nome} VENCEU!")
    print("=" * 40)


if __name__ == "__main__":
    simular_batalha()
