"""
16 - crie um programa que leia um número fracionário (float) qualquer pelo teclado e mostre sua porção inteira
"""
import math
num = float(input('informe um número fracionário (para casas decimais use ponto): '))

print(f'o número ficou {math.trunc(num)}')

