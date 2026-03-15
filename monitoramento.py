# monitoramento.py - Módulo de Monitoramento de Safra
# Projeto de Software 2026 - Gerenciamento de Configuração

from datetime import datetime

class MonitoramentoSafra:
    """Classe para monitoramento de safras agrícolas."""

    def __init__(self, propriedade, cultura, data_plantio):
        self.propriedade = propriedade
        self.cultura = cultura
        self.data_plantio = data_plantio
        self.registros = []

    def adicionar_registro(self, descricao, status):
        """Adiciona um registro de monitoramento."""
        registro = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "descricao": descricao,
            "status": status
        }
        self.registros.append(registro)
        print(f"Registro adicionado: {descricao} - Status: {status}")

    def gerar_relatorio(self):
        """Gera relatório de monitoramento da safra."""
        print(f"\n=== Relatório de Monitoramento ===")
        print(f"Propriedade: {self.propriedade}")
        print(f"Cultura: {self.cultura}")
        print(f"Data de Plantio: {self.data_plantio}")
        print(f"Total de Registros: {len(self.registros)}")
        for reg in self.registros:
            print(f"  [{reg['data']}] {reg['descricao']} - {reg['status']}")
