"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido.
O programada deverá escrever na tela se o usuário acertou ou errou
"""

import random

computador = (random.randint(0,5))

jogador = int(input("Escolha um número entre 0 e 5: "))

if computador == jogador:
    print("Acertou, você merece um prêmio!")
else:
    print("Você errou.")
print("Aguardo-o para uma próxima partida, se você tiver coragem")