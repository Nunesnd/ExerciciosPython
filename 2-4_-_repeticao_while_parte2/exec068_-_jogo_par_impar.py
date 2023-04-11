"""
Fazer um jogo de par ou ímpar constante. o jogo será interrompido quando o jogador perder.
Deverá mostrar no final quantas vitórias consecutivas o jogador conquistou.
"""

import random

vitorias = 0

while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    jogador = int(input("Escolha seu número: "))
    comp = random.randint(0,10)
    result = jogador+comp    
    escolha =''
        
    while escolha.upper() != 'P' or escolha.upper() != 'I':    
        escolha = input("Você deseja Par ou Impar? [ P - I ]: ").strip()
        print(' - - - - - - - - - - - - - - - - - - - - - - - - - -')        
        print(f'Jogador: {jogador}, Computador: {comp}, resultado: {result}')        
        print(f"Escolha foi {escolha.upper()}\n")        
        break
    
    if escolha.upper() == 'P':
        if (result % 2) == 0:
            print("VITÓRIA!\n")
            vitorias += 1
        else:
            print("VOCÊ PERDEU!\n")
            break
    elif escolha.upper() == 'I':
        if (result % 2) != 0:
            print("VITÓRIA!\n")
            vitorias += 1
        else:
            print("VOCÊ PERDEU!\n")
            break
        
print(f'Você conquistou {vitorias} votórias')
print('###############################')