# Análise de Desempenho: PokéAPI Parallel Requests

Projeto desenvolvido para a disciplina de **Sistemas Paralelos e Distribuídos** do **Instituto Federal de Pernambuco (IFPE)**.

## 📌 Descrição do Projeto
Este projeto tem como objetivo analisar e comparar o desempenho de diferentes modelos de concorrência e paralelismo na linguagem Python. A aplicação realiza requisições à **PokéAPI** para a extração automatizada de imagens (*sprites*) de Pokémons, salvando-as localmente.

Por se tratar de uma tarefa predominantemente **I/O-bound** (limitada pela latência de rede), foram implementadas e testadas as seguintes abordagens:
* **Execução Sequencial:** Processamento de uma requisição por vez.
* **Threading:** Uso de múltiplas threads para gerenciar a espera de rede de forma concorrente.
* **Multiprocessing:** Distribuição de tarefas entre múltiplos núcleos do processador.
* **Concurrent.Futures:** Implementação de pools de threads para gerenciamento de alto nível.

## 🛠️ Tecnologias e Ambiente
- **Linguagem:** Python 3.14
- **Bibliotecas:** `requests`, `os`, `threading`, `multiprocessing` e `concurrent.futures`.
- **Hardware de Teste:** Samsung Galaxy Book 4 (10 núcleos físicos / 12 lógicos).

## 📂 Estrutura do Repositório
- `main.py`: Código-fonte com todas as implementações e testes de performance.
- `requirements.txt`: Arquivo de dependências (necessário para instalar a biblioteca `requests`).
- `Relatorio_PokeAPI_Raphaela.pdf`: Relatório técnico completo (formato SBC) contendo a metodologia detalhada, tabelas de resultados e discussão acadêmica.

## 🚀 Como Executar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar o projeto:**
```bash
python main.py
```
