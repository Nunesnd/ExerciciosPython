"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
import random
q_jogos = linha = 0
matriz = []

print('-'*30)
print('{:^30}'.format('Jogos Mega Sena'))
print('-'*30)

q_jogos = int(input("Quantos jogos quer fazer: "))

while linha < q_jogos:
    coluna = 0
    jogo = [0,0,0,0,0,0]
    while coluna < 6:
        num = random.randint(1,60)
        
        if num not in jogo:        
            jogo[coluna] = num
        coluna += 1
    matriz.append(jogo)
    print(f'Sorteando jogo nº {linha+1}: {sorted(jogo)}')
    linha += 1
#print(matriz)





print('#'*30)

#for linha in range(0, 3):
#    for coluna in range(0, 3):
#        print(f'[{matriz[linha][coluna]:^5}]', end='')
#    print('')