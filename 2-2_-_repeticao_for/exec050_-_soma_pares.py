"""
Leia seis números inteiros quaisquer, e mostre a soma apenas dos números que forem pares, se número for ímpar deve ser desconsiderado
"""

soma = 0

for c in range(0,6):
    num = int(input("Escreva um número: "))
    if (num%2)==0:
        soma=soma+num
print(f'resultado é {soma}')