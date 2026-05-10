import time
from scripts_paralelos.seq import executar_sequencial
from scripts_paralelos.thr import executar_threads
from scripts_paralelos.mp import executar_multiprocessing
from scripts_paralelos.cf import executar_futures
from utils import limpar_imagens

def realizar_experimentos_teste():
    # --- CONFIGURAÇÃO DE TESTE RÁPIDO (Validar fluxo) ---
    quantidades = [100, 500, 1000]         # requisito 6
    setups_workers = [2, 4, 8]       # requisito 8
    repeticoes = 10             # requisito 7
    
    resultados = []

    for qtd in quantidades:
        print(f"\n=== [TESTE] INICIANDO VALIDAÇÃO DE FLUXO ({qtd} IMAGENS) ===")
        
        # 1. Teste Sequencial
        limpar_imagens()
        print("Executando Sequencial...")
        inicio = time.time()
        executar_sequencial(qtd)
        tempo_seq = time.time() - inicio
        resultados.append({'Metodo': 'Sequencial', 'Qtd': qtd, 'Workers': 1, 'Media': tempo_seq})

        for workers in setups_workers:
            # 2. Teste Threads
            limpar_imagens()
            print(f"Executando Threads ({workers} workers)...")
            inicio = time.time()
            executar_threads(qtd, workers)
            tempo_thr = time.time() - inicio
            resultados.append({'Metodo': 'Threads', 'Qtd': qtd, 'Workers': workers, 'Media': tempo_thr})

            # 3. Teste Multiprocessing
            limpar_imagens()
            print(f"Executando Multiprocessing ({workers} workers)...")
            inicio = time.time()
            executar_multiprocessing(qtd, workers)
            tempo_mp = time.time() - inicio
            resultados.append({'Metodo': 'Multiprocessing', 'Qtd': qtd, 'Workers': workers, 'Media': tempo_mp})

            # 4. Teste Futures
            limpar_imagens()
            print(f"Executando Futures ({workers} workers)...")
            inicio = time.time()
            executar_futures(qtd, workers)
            tempo_cf = time.time() - inicio
            resultados.append({'Metodo': 'Futures', 'Qtd': qtd, 'Workers': workers, 'Media': tempo_cf})

    # Resumo visual para você conferir no terminal
    print("\n" + "="*45)
    print(f"{'MÉTODO':15} | {'WORKERS':8} | {'TEMPO':8}")
    print("-" * 45)
    for r in resultados:
        print(f"{r['Metodo']:15} | {r['Workers']:8} | {r['Media']:.2f}s")
    print("="*45)

if __name__ == "__main__":
    realizar_experimentos_teste()