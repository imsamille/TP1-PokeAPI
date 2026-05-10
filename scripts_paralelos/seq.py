import time
import sys
import os

# Adiciona a pasta raiz ao path para conseguirmos importar o utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import obter_lista_pokemons, baixar_e_salvar_img, criar_estrutura_pastas

def executar_sequencial(quantidade):
    print(f"--- Iniciando Sequencial ({quantidade} Pokémons) ---")
    
    # GARANTIA: Cria as pastas antes de baixar
    criar_estrutura_pastas()
    
    # 1. Obtém a lista de URLs
    lista_pokes = obter_lista_pokemons(quantidade)
    pasta_destino = "imagens/sequencial"
    
    start_time = time.time()
    
    # 2. Percorre a lista um por um (Sequencial)
    for poke in lista_pokes:
        baixar_e_salvar_img(poke['url'], pasta_destino)
        
    end_time = time.time()
    duracao = end_time - start_time
    
    print(f"Tempo total Sequencial: {duracao:.2f} segundos")
    return duracao

if __name__ == "__main__":
    executar_sequencial(10)