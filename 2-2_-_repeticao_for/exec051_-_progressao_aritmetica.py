"""
Leia o primeiro termo e a razão de uma PA, depois mostre os 10 próximos termos
"""

termo = int(input("Informe o primeiro termo da PA: "))

razao = int(input("Informe a razão: "))

print(f'{termo}')

for c in range (0,9):
    termo=termo+razao
    print(termo)