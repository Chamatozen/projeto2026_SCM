# Projeto 2026 - Gerenciamento de Configuração de Software (SCM)

## Descrição

Este projeto é uma atividade prática da disciplina **Projeto de Software** (Unidade U4 — Projeto de Software Avançado, Aula A1 — Gerenciamento de Configuração) que demonstra o uso de ferramentas de gerenciamento de configuração como Git e GitHub.

## Objetivo

Aprender a gestão de artefatos gerados pelo desenvolvimento de software através de ferramenta de gerenciamento de configuração, compreendendo o funcionamento de um repositório de artefatos compartilhados com todos os colaboradores do time de desenvolvimento.

## Cenário do Projeto

O **AgroTech 2026** é um Sistema de Gestão Agrícola desenvolvido para auxiliar produtores rurais no monitoramento e controle de suas propriedades e safras. O projeto envolve múltiplos stakeholders e uma equipe de desenvolvimento que necessita de controle efetivo dos artefatos.

## Artefatos do Projeto

- **main.py**: Módulo principal com menu do sistema e inicialização
- **cadastro.py**: Módulo de cadastro e gestão de propriedades rurais
- **monitoramento.py**: Módulo de monitoramento de safras e geração de relatórios
- **relatorios.py**: Módulo de relatórios gerenciais (nova funcionalidade solicitada pelo cliente)
- **DOCUMENTACAO.md**: Documentação técnica do projeto
- **LICENSE**: Licença MIT

## Estrutura do Repositório

```
projeto2026_SCM/
├── main.py
├── cadastro.py
├── monitoramento.py
├── relatorios.py
├── DOCUMENTACAO.md
├── README.md
├── LICENSE
└── .git/
```

## Como Usar

### Pré-requisitos

- Git instalado (https://git-scm.com/downloads)
- Python 3.7 ou superior

### Clonar o Repositório

```bash
git clone https://github.com/Chamatozen/projeto2026_SCM.git
cd projeto2026_SCM
```

### Executar os Módulos

```bash
# Executar o módulo principal
python3 main.py

# Executar o módulo de cadastro
python3 cadastro.py

# Executar o módulo de monitoramento
python3 monitoramento.py

# Executar o módulo de relatórios
python3 relatorios.py
```

## Fluxo de Trabalho Git

### Verificar Status

```bash
git status
```

### Adicionar Alterações

```bash
git add .
```

### Fazer Commit

```bash
git commit -m "Descrição das alterações"
```

### Enviar para o Repositório Remoto

```bash
git push origin main
```

## Equipe de Desenvolvimento

- Analista de Sistemas (Responsável pelo projeto)
- Desenvolvedor Backend
- Desenvolvedor Frontend
- Testador QA

## Competências Desenvolvidas

- Configuração local do Git
- Criação de repositórios no GitHub
- Clonagem de repositórios remotos
- Criação e modificação de artefatos de software
- Operações de commit e push
- Controle de versão e rastreabilidade
- Colaboração em equipe via repositório centralizado

## Referências

- [GitHub Documentation](https://docs.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)

## Autor

**Leonardo** (Chamatozen)

## Data de Criação

15 de março de 2026

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
