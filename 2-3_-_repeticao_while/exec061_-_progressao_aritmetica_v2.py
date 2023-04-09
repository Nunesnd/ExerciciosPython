"""
Refaça o desafio 051 lendo o termo e a razão de uma PA mostrando os 10 primeiros termos da progressão usando while
"""

termo = int(input('Termo: '))
razao = int(input('Razão: '))

n = 0 

while n < 10:

    termo=termo+razao
    print(f'Termo nº {n+1}: {termo}')
    n+=1