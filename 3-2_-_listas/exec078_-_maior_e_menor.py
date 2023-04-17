"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
cont = 0 
print('#'*40)

#lista = [4, 2, 3, 9, 5, 8]
lista = []

while cont < 5:
    valor = int(input(f'Informe o valor da posição {cont}: '))
    lista.append(valor)
    cont += 1

print(f'A lista digitada foi {lista}.')

menor = sorted(lista)
print(f'Menor número foi: {menor[0]}')

maior = sorted(lista, reverse=True)
print(f'Maior número foi: {maior[0]}')

print('')

