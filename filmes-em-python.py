import requests
import json
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

# Defining -
req = None
sagaFilmes = None

# Functions - 
def requisicao(titulo, tipo):
    match (tipo):
        case 1:
            try:
                req = requests.get('https://www.omdbapi.com/?apikey=834e6d40&t=' + titulo)
                dicionario = json.loads(req.text)
                return dicionario
            except:
                print('Erro na requisição!')
                return req
        
        case 2:
            try:
                req = requests.get('https://www.omdbapi.com/?apikey=834e6d40&s=' + titulo)
                moviesSaga = json.loads(req.text)
                return moviesSaga
            except:
                print('Erro na requisição!')
                return req

def printFilmDetails():
    print()
    print(f"Título: {filme['Title']}")
    print(f"Data de lançamento: {filme['Released']}")
    print(f"Nota (Rotten Tomatoes) : {filme['Ratings'][1]['Value']}")
    print(f"Duração do filme: {filme['Runtime']}")
    print(f"Genêros: {filme['Genre']}")
    print(f"Diretor: {filme['Director']}")
    print()
    input('Enter continua...')

def giveFilmOptions():
    print(f'Aqui estão alguns filmes relacionados a saga {op}:\n')
    for n, movies in enumerate(sagaFilmes["Search"]):
        print(f"{n+1} - {movies['Title']}")
        print('-----------------------\n')
        time.sleep(0.8)
    time.sleep(2)

# Main - 
print('\033[35mComo é esse filme?\033[0m')
print('\nUm pequeno aplicativo para você se guiar qunando estiver decidindo o que assistir!')
      
while True:
    print('\nO que você deseja fazer?\n\n[1] Pesquisar filme específico.\n[2] Pesquisar saga de filmes.\n[3] Ver lista de favoritos.\n[4] Sair.')
    modo = input('> ')
    match(modo):
        case '1': 
            while True:
                op = input("Insira o nome do filme que você deseja saber sobre: ").strip().title()
                if op == '':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                else:
                    filme = requisicao(op, 1)
                    if filme['Response'] == 'False':
                        print("Filme não encontrado!\n\nTente novamente.")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        printFilmDetails()
                        break
        case '2': 
            while True:
                op = input("Insira a saga de filmes que você deseja saber sobre: ").strip().title()
                if op == '':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                else:
                    sagaFilmes = requisicao(op, 2)
                    if sagaFilmes['Response'] == 'False':
                        print("Filmea não encontrados!\n\nTente novamente.")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        giveFilmOptions()
                        break
        case '3': pass
        case '4':
            exit()
