"""
Faça um programa que mostre na tela uma contagem regressiva de 10 à 0 com pause de 1 segundo
"""
from time import sleep

for c in range(0,10):
    print(f'Lançamento em t - {10-c}')
    sleep(1)
print("Lançado")