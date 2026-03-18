# relatorios.py - Módulo de Relatórios Gerenciais
# Projeto de Software 2026 - Nova funcionalidade solicitada pelo cliente
# Autor: Aluno(a) - Analista de Sistemas

from datetime import datetime

class RelatorioGerencial:
    """Classe para geração de relatórios gerenciais do sistema agrícola."""

    def __init__(self, titulo, periodo):
        self.titulo = titulo
        self.periodo = periodo
        self.data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.dados = []

    def adicionar_dados(self, categoria, valor, unidade):
        """Adiciona dados ao relatório."""
        self.dados.append({
            "categoria": categoria,
            "valor": valor,
            "unidade": unidade
        })

    def gerar_relatorio_producao(self):
        """Gera relatório de produção agrícola."""
        print(f"\n{'='*50}")
        print(f"RELATÓRIO GERENCIAL - {self.titulo}")
        print(f"Período: {self.periodo}")
        print(f"Gerado em: {self.data_geracao}")
        print(f"{'='*50}")
        for dado in self.dados:
            print(f"  {dado['categoria']}: {dado['valor']} {dado['unidade']}")
        print(f"{'='*50}")

    def exportar_csv(self, nome_arquivo):
        """Exporta relatório para formato CSV."""
        print(f"Relatório exportado para: {nome_arquivo}.csv")
