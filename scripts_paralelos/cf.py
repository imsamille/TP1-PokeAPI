from concurrent.futures import ThreadPoolExecutor
import time
import sys
import os

# Importando o utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import obter_lista_pokemons, baixar_e_salvar_img, criar_estrutura_pastas

def executar_futures(quantidade, num_workers):
    print(f"--- Iniciando Concurrent Futures ({quantidade} Pokémons com {num_workers} workers) ---")
    
    criar_estrutura_pastas()
    lista_pokes = obter_lista_pokemons(quantidade)
    pasta_destino = "imagens/futures"
    
    # Preparamos a lista de URLs para o executor.map
    urls = [poke['url'] for poke in lista_pokes]
    
    start_time = time.time()

    # Requisito (3 e 8): Usando o ThreadPoolExecutor com o limite de workers
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        # Seguindo o modelo do professor: usando map para disparar as tarefas
        # Como baixar_e_salvar_img precisa de dois argumentos, usamos uma função lambda rápida
        list(executor.map(lambda url: baixar_e_salvar_img(url, pasta_destino), urls))

    end_time = time.time()
    duracao = end_time - start_time
    print(f"Tempo total Futures: {duracao:.2f} segundos")
    return duracao

if __name__ == "__main__":
    # Teste com 10 pokémons e 4 workers
    executar_futures(10, 4)