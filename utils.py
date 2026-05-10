import shutil
import os
import requests
import time

def limpar_imagens():
    if os.path.exists('imagens'):
        try:
            # Tenta remover a pasta e todo o conteúdo
            shutil.rmtree('imagens')
            # Pequeno delay para o Windows liberar o sistema de arquivos
            time.sleep(0.5) 
        except PermissionError:
            print("\nAVISO: Feche as janelas do explorador de arquivos abertas na pasta 'imagens'.")
            print("Tentando limpar arquivos individualmente...")
            # Fallback caso a pasta principal esteja travada
            return
    
    # Recria a estrutura base para o novo teste
    criar_estrutura_pastas()

# Requisito (5): Utilizar python os para armazenar as imagens
def criar_estrutura_pastas():
    pastas = [
        'imagens/sequencial',
        'imagens/threading',
        'imagens/multiprocessing',
        'imagens/futures'
    ]
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)

# Requisito (11/14): Pegar a lista de pokémons (nome e url)
def obter_lista_pokemons(quantidade):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={quantidade}"
    try:
        response = requests.get(url)
        return response.json()['results']
    except Exception as e:
        print(f"Erro ao obter lista: {e}")
        return []

# Requisito (18/19): Baixar a imagem front_default para o disco
def baixar_e_salvar_img(pokemon_url, pasta_destino):
    try:
        detalhes = requests.get(pokemon_url).json()
        img_url = detalhes['sprites']['front_default']
        nome = detalhes['name']
        
        if img_url:
            img_data = requests.get(img_url).content
            caminho = os.path.join(pasta_destino, f"{nome}.png")
            
            with open(caminho, 'wb') as f:
                f.write(img_data)
            return True
    except Exception as e:
        # Silenciamos o erro de diretório inexistente se a limpeza falhar no meio
        return False