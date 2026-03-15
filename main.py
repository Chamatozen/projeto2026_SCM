# main.py - Módulo Principal do Sistema de Gestão Agrícola
# Projeto de Software 2026 - Gerenciamento de Configuração
# Autor: Aluno(a) - Analista de Sistemas
# Atualização: Integração do módulo de relatórios (solicitação do cliente)

def iniciar_sistema():
    """Função principal que inicializa o sistema de gestão agrícola."""
    print("=== Sistema de Gestão Agrícola - AgroTech 2026 ===")
    print("Inicializando módulos...")
    print("Sistema pronto para uso.")
    print("Versão 1.1 - Módulo de Relatórios integrado")

def menu_principal():
    """Exibe o menu principal do sistema."""
    opcoes = {
        1: "Cadastro de Propriedades",
        2: "Monitoramento de Safra",
        3: "Relatórios Gerenciais",
        4: "Gestão de Insumos",
        5: "Sair"
    }
    for chave, valor in opcoes.items():
        print(f"{chave} - {valor}")

if __name__ == "__main__":
    iniciar_sistema()
    menu_principal()
