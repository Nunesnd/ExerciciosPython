"""
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 - 10.
Só que agora o jogador vai tentar adivinhar até acertar. No final informe quantos palpites foram necessários.
"""

import random

palpites = 0

computador = (random.randint(0,5))
jogador = int(input("Escolha um número entre 0 e 5: "))

while computador != jogador:

    jogador = int(input("Errou, escolha novamente: "))
    palpites+=1


print(f"Acertou é o {computador}, mesmo com {palpites}, você merece um prêmio!")
