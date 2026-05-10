from multiprocessing import Process, Queue
import time
import sys
import os

# Importando o utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import obter_lista_pokemons, baixar_e_salvar_img, criar_estrutura_pastas

# Seguindo o modelo do professor: Função que usa a Queue
def worker_pokemon(url, pasta, q):
    resultado = baixar_e_salvar_img(url, pasta)
    q.put(resultado)

def executar_multiprocessing(quantidade, num_workers):
    print(f"--- Iniciando Multiprocessing ({quantidade} Pokémons com {num_workers} workers) ---")
    
    criar_estrutura_pastas()
    lista_pokes = obter_lista_pokemons(quantidade)
    pasta_destino = "imagens/multiprocessing"
    
    q = Queue()
    processes = []
    
    start_time = time.time()

    # Requisito (8): Usar lotes baseados no num_workers (2, 4 ou 8)
    for i in range(0, len(lista_pokes), num_workers):
        lote = lista_pokes[i : i + num_workers]
        
        for poke in lote:
            # Requisito (3): Implementar usando multiprocessing
            p = Process(target=worker_pokemon, args=(poke['url'], pasta_destino, q))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
        
        processes.clear()

    end_time = time.time()
    duracao = end_time - start_time
    print(f"Tempo total Multiprocessing: {duracao:.2f} segundos")
    return duracao

if __name__ == "__main__":
    # Teste com 10 pokémons e 4 workers
    executar_multiprocessing(10, 4)