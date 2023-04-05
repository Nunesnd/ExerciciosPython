"""
Crie um prog que faça o computador jogar jokenpo com você
"""

import random

jogador = input("Jogador, informe seu nome: ")

opcao = int(input("Faça sua escolha: \n0 - Papel \n1 - Pedra \n2 - Tesoura\n"))

computador = (random.randint(0,2))

print(f'Jogador: {jogador}, computador {computador}')

if (computador == 0):
    if (opcao == 0):
        print(f"{jogador} = Papel e Computador Papel\nTemos um empate!")
    elif (opcao == 1):
        print(f"{jogador} = Pedra e Computador Papel\nVitória do Computador!")
    elif (opcao == 2):
        print(f"{jogador} = Tesoura e Computador Papel\nVitória do {jogador}!")

elif(computador == 1):
    if (opcao == 0):
        print(f"{jogador} = Papel e Computador Pedra\nVitória do {jogador}!")
    elif (opcao == 1):
        print(f"{jogador} = Pedra e Computador Pedra\nTemos um empate!")
    elif (opcao == 2):
        print(f"{jogador} = Tesoura e Computador Pedra\nVitória do Computador!")

elif(computador == 2):
    if (opcao == 0):
        print(f"{jogador} = Papel e Computador Tesoura\nVitória do Computador!")
    elif (opcao == 1):
        print(f"{jogador} = Pedra e Computador Tesoura\nVitória do {jogador}!")
    elif (opcao == 2):
        print(f"{jogador} = Tesoura e Computador Tesoura\nTemos um empate!")