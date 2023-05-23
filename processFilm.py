import requests
import json
import time
import os

req = None
sagaFilmes = None
filme = None
movies = []

def clearTerminal():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

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

def printFilmDetails(filme):
    print()
    print(f"Título: \033[35m{filme['Title']}\033[0m")
    print(f"Data de lançamento: {filme['Released']}")
    print(f"Nota (IMDB): {filme['imdbRating']}")
    print(f"Duração do filme: {filme['Runtime']}")
    print(f"Genêros: {filme['Genre']}")
    print(f"Diretor: {filme['Director']}")
    print()
    input('Enter continua...')

def giveFilmOptions(sagaFilmes, search):
    clearTerminal()
    print(f'\nAqui estão alguns filmes relacionados a saga \033[35m{search}\033[0m:\n')
    for n, movie in enumerate(sagaFilmes["Search"]):
        movies.append(movie['Title'])
        print(f"{n+1} - {movie['Title']}")
        print('-----------------------\n')
        time.sleep(0.8)
    time.sleep(2)
    chooseFilm(movies)

def chooseFilm(movies):
    seeDetails = input('Você gostaria de ver mais detalhes sobre algum destes filmes? ').strip().lower()
    if seeDetails == '' or seeDetails[0] not in 'ys': pass
    else:
        while True:
            wichFilm = input('\nInsira o \033[35mtitulo ou o número\033[0m correspondente ao filme: ').strip().title()
            if wichFilm.isdigit() and (int(wichFilm)-1) <= len(movies):
                print(f'\nVocê escolheu ver detalhes do filme - \033[35m{movies[int(wichFilm)-1]}\033[0m')
                requestingDetails(movies[int(wichFilm)-1])
            elif wichFilm in movies:
                print(f'\nVocê escolheu ver detalhes do filme - \033[35m{wichFilm}\033[0m')
                requestingDetails(wichFilm)
            elif wichFilm == '': break
            else:
                print('\033[31mFilme não encontrado tente novamente!\033[0m')
                continue
            break

def requestingDetails(film):
    filme = requisicao(film, 1)
    printFilmDetails(filme)

def searchBar(mode):
    while True:
        if mode == 1:
            search = input("\nInsira o \033[35mnome do filme\033[0m que você deseja saber sobre: ").strip().title()
        else:
            search = input("\nInsira a \033[35msaga de filmes\033[0m que você deseja saber sobre: ").strip().title()
        if search == '': break
        else:
            if mode == 1:
                filme = requisicao(search, 1)
                if filme['Response'] == 'False':
                    print("\033[31mFilme não encontrado!\033[0m\n\nTente novamente.")
                    clearTerminal()
                else:
                    printFilmDetails(filme)
                    break
            else:
                sagaFilmes = requisicao(search, 2)
                if sagaFilmes['Response'] == 'False':
                    print("\033[31mFilmes não encontrados!\033[0m\n\nTente novamente.")
                    clearTerminal()
                else:
                    giveFilmOptions(sagaFilmes, search)
                    break