"""
Faça um prog que gere cinco números aleatórios e os coloque em uma tupla.
Depois mostre a listagem de números
O maior número
O menor número
"""
import random

maior = menor = 0

num1 = random.randint(0,99)
num2 = random.randint(0,99)
num3 = random.randint(0,99)
num4 = random.randint(0,99)
num5 = random.randint(0,99)

seq = [num1, num2, num3, num4, num5]

for c in range (0,6):
    
    num = seq[c-1]
    
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Valores são: {seq}')
print(f'Maior é: {maior}') 
print(f'Menor é: {menor}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')