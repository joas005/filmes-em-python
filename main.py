import os
import processFilm
os.system('cls' if os.name == 'nt' else 'clear')

# Functions - 
def seeCredits():
    print('\n\033[34mObrigado por querer me conhecer\033[0m 😁✌️\nEste programa foi desenvolvido por \033[35m@joas005\033[0m no github, entre lá para conheça um pouco mais sobre mim e meus projetos!')
    input('\nEnter continua...')

def exitingProgram():
    print('\nObrigado por utilizar \033[35mComo é esse filme?\033[0m\nVolte sempre que estiver em dúvida do que assistir! 😘✌️')
    print(56*'-')
    exit()

# Main - 
print('\033[35mComo é esse filme?\033[0m')
print('\nUm pequeno aplicativo para você se guiar quanndo estiver decidindo o que assistir!')
      
while True:
    print('\nO que você deseja fazer?\n\n\033[32m[1] Pesquisar filme específico.\n\033[1;35m[2] Pesquisar saga de filmes.\n\033[34m[3] Ver créditos.\n\033[31m[4] Sair.\033[0m')
    modo = input('>> ')
    match(modo):
        case '1': processFilm.searchBar(1)
        case '2': processFilm.searchBar(2)      
        case '3': seeCredits()
        case '4': exitingProgram()
        case _: print('\033[31mVocê inseriu algo inválido!\033[0m\nTente novamente')
    processFilm.clearTerminal()
