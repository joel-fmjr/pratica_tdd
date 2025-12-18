# Sistema de Batalha RPG

Projeto desenvolvido para prática de **Test-Driven Development (TDD)** utilizando Python e pytest.

## Descrição

Sistema de batalha RPG que implementa:

- **Personagens** com atributos (HP, Ataque, Defesa)
- **Sistema Elemental** (Fogo, Gelo, Raio) com vantagens e fraquezas
- **Sistema de Combate** com cálculo de dano e modificadores elementais
- **Demonstração Interativa** simulando batalhas entre personagens

## Estrutura do Projeto

```
pratica_tdd/
├── src/
│   ├── personagem.py      # Classe Personagem
│   ├── elementos.py       # Enum de elementos
│   ├── combate.py         # Sistema de combate
├── tests/
│   ├── test_personagem.py # Testes do personagem
│   └── test_combate.py    # Testes do sistema de combate
├── main.py                # Demonstração interativa
└── requirements.txt       # Dependências do projeto
```

## Instalação

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente virtual

**Linux/Mac:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## Executando os Testes

### Executar todos os testes

```bash
pytest
```

### Executar com informações detalhadas

```bash
pytest -v
```

### Executar com saída completa (sem truncar)

```bash
pytest -vv
```

### Executar arquivo de teste específico

**Testes de personagem:**
```bash
pytest tests/test_personagem.py
```

**Testes de combate:**
```bash
pytest tests/test_combate.py
```

### Executar classe de teste específica

**Testes de validação do personagem:**
```bash
pytest tests/test_personagem.py::TestValidacoesPersonagem
```

**Testes do sistema elemental:**
```bash
pytest tests/test_combate.py::TestSistemaElemental
```

**Outras classes disponíveis:**
```bash
pytest tests/test_personagem.py::TestEstadoPersonagem
pytest tests/test_personagem.py::TestReceberDano
pytest tests/test_personagem.py::TestCurar
pytest tests/test_combate.py::TestCalculoDanoBasico
pytest tests/test_combate.py::TestExecutarAtaque
pytest tests/test_combate.py::TestMensagensResultado
```

### Executar teste específico

```bash
pytest tests/test_personagem.py::TestValidacoesPersonagem::test_hp_nao_pode_ser_zero
```

```bash
pytest tests/test_combate.py::TestSistemaElemental::test_fraqueza_aumenta_dano_50_porcento
```

### Executar testes por palavra-chave (pattern matching)

**Todos os testes relacionados a "dano":**
```bash
pytest -k dano
```

**Todos os testes relacionados a "elemental":**
```bash
pytest -k elemental
```

**Todos os testes relacionados a "validação":**
```bash
pytest -k validacao
```

### Executar testes e parar no primeiro erro

```bash
pytest -x
```

### Executar testes mostrando variáveis locais em falhas

```bash
pytest -l
```

### Executar testes com saída de print

```bash
pytest -s
```

### Combinando opções

```bash
pytest -v -s tests/test_combate.py
```

## Executando a Demonstração

Para ver uma simulação de batalha entre personagens:

```bash
python main.py
```

A demonstração mostra uma batalha entre Gandalf (Fogo) e Elsa (Gelo), incluindo:
- Status inicial dos personagens
- Turnos de combate com dano calculado
- Modificadores elementais aplicados
- Resultado final da batalha

## Funcionalidades Implementadas

### Personagem
- Validação de atributos (HP, ataque, defesa)
- Sistema de HP (atual e máximo)
- Receber dano (com proteção contra HP negativo)
- Curar (com limite de HP máximo)
- Verificação de estado (vivo/derrotado)

### Sistema de Combate
- Cálculo de dano: `Ataque - Defesa` (mínimo 1)
- Modificadores elementais:
  - Vantagem: +50% de dano (Fogo > Gelo > Raio > Fogo)
  - Resistência: -50% de dano (mesmo elemento)
- Validações de combate (atacante vivo, defensor vivo, não auto-ataque)
- Mensagens descritivas de resultado

### Sistema Elemental
- **FOGO**: Forte contra Gelo
- **GELO**: Forte contra Raio
- **RAIO**: Forte contra Fogo
- **NENHUM**: Sem modificadores

## Exemplos de Uso

```python
from src.personagem import Personagem
from src.elementos import Elemento
from src.combate import SistemaCombate

# Criar personagens
guerreiro = Personagem(
    nome="Aragorn",
    classe="Guerreiro",
    hp=120,
    ataque=25,
    defesa=20,
    elemento=Elemento.NENHUM
)

mago = Personagem(
    nome="Gandalf",
    classe="Mago",
    hp=80,
    ataque=40,
    defesa=10,
    elemento=Elemento.FOGO
)

# Sistema de combate
combate = SistemaCombate()
resultado = combate.atacar(mago, guerreiro)

print(resultado.mensagem)  # "Gandalf atacou Guerreiro causando 20 de dano!"
print(f"HP restante: {resultado.defensor_hp_restante}")
```

## Tecnologias Utilizadas

- **Python 3.13**
- **pytest**: Framework de testes
- **TDD**: Metodologia de desenvolvimento orientado a testes

## Licença

Projeto educacional - IFRN
