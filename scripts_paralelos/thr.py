import threading
import time
import sys
import os

# Adiciona a pasta raiz ao path para importar o utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import obter_lista_pokemons, baixar_e_salvar_img, criar_estrutura_pastas

# Seguindo o modelo do professor: listas para gerenciar threads
threads = []

def executar_threads(quantidade, num_workers):
    print(f"--- Iniciando Threads ({quantidade} Pokémons com {num_workers} workers) ---")
    
    # Requisito (5): Garante a pasta de destino [cite: 27]
    criar_estrutura_pastas()
    lista_pokes = obter_lista_pokemons(quantidade)
    pasta_destino = "imagens/threading"
    
    start_time = time.time()

    # O requisito (8) pede setups de 2, 4 ou 8 workers 
    # Vamos processar em lotes (chunks) para respeitar o limite de workers
    for i in range(0, len(lista_pokes), num_workers):
        lote = lista_pokes[i : i + num_workers]
        
        # Cria e inicia as threads do lote atual
        for poke in lote:
            # Requisito (3): Implementar usando threading [cite: 25]
            t = threading.Thread(target=baixar_e_salvar_img, args=(poke['url'], pasta_destino))
            threads.append(t)
            t.start()

        # Requisito: Aguardar todas as threads do lote terminarem (join)
        for t in threads:
            t.join()
        
        # Limpa a lista para o próximo lote
        threads.clear()
        
    end_time = time.time()
    duracao = end_time - start_time
    print(f"Tempo total Threads: {duracao:.2f} segundos")
    return duracao

if __name__ == "__main__":
    # Teste inicial com 10 pokémons e 4 threads (como no exemplo do prof)
    executar_threads(10, 4)