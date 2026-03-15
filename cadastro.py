# cadastro.py - Módulo de Cadastro de Propriedades Rurais
# Projeto de Software 2026 - Gerenciamento de Configuração

class Propriedade:
    """Classe que representa uma propriedade rural no sistema."""

    def __init__(self, nome, localizacao, area_hectares, tipo_cultivo):
        self.nome = nome
        self.localizacao = localizacao
        self.area_hectares = area_hectares
        self.tipo_cultivo = tipo_cultivo

    def exibir_dados(self):
        """Exibe os dados da propriedade cadastrada."""
        print(f"Propriedade: {self.nome}")
        print(f"Localização: {self.localizacao}")
        print(f"Área: {self.area_hectares} hectares")
        print(f"Cultivo: {self.tipo_cultivo}")


def cadastrar_propriedade(nome, localizacao, area, cultivo):
    """Cadastra uma nova propriedade no sistema."""
    nova_propriedade = Propriedade(nome, localizacao, area, cultivo)
    print(f"Propriedade '{nome}' cadastrada com sucesso!")
    return nova_propriedade


def listar_propriedades(lista_propriedades):
    """Lista todas as propriedades cadastradas."""
    if not lista_propriedades:
        print("Nenhuma propriedade cadastrada.")
        return
    for i, prop in enumerate(lista_propriedades, 1):
        print(f"\n--- Propriedade {i} ---")
        prop.exibir_dados()
