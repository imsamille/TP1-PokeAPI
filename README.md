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
- `scripts_paralelos/`: Pasta contendo as implementações de cada método de concorrência.
- `TP1_PokéAPI_Relatório.pdf`: Relatório técnico final com toda a análise dos testes.
- `main.py`: Script principal que executa os experimentos e gera os resultados.
- `requirements.txt`: Arquivo com as dependências necessárias (`requests`).
- `utils.py`: Funções auxiliares de limpeza e gerenciamento de pastas.

## 🚀 Como Executar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar o projeto:**
```bash
python main.py
```
---

### ⚠️ Observação Importante
Devido à carga dos experimentos (testes com 100, 500 e 1.000 imagens, com 10 repetições para cada variação de 2, 4 e 8 workers), a execução completa do script `main.py` é **extremamente demorada**. O processo pode levar várias horas para concluir todas as iterações, dependendo da latência da rede e do hardware. 

Para detalhes sobre os resultados e médias obtidas, consulte o arquivo PDF do relatório incluído na raiz deste repositório.
