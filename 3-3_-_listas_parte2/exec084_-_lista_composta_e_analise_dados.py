"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoa = list()
lista = list()
pesado = leve = cont = 0

while True:
    
    pessoa.append(str(input(f'Informe o nome : ')))
    pessoa.append(str(input(f'Informe o peso : ')))    
    lista.append(pessoa[:])
    pessoa.clear()
    
    adicionar = str(input('Deseja continuar[S/N]? '))
    
    if adicionar[0].upper() == 'N':
        print('Saindo do prog')
        break

elementos = len(lista)

while cont < elementos:

    if cont == 0:
        pesado = leve = lista[cont][1]
    
    if lista[cont][1] > pesado:
        pesado = lista[cont][1]
    
    if lista[cont][1] < leve:
        leve = lista[cont][1]

    cont += 1

print('#'*50)
    
print(f'Total de cadastrados: {len(lista)}')
print(f'O mais pesado tem: {pesado} kg. ', end='')
for peso in lista:
    if peso[1] == pesado:
        print(f'[{peso[0]}] ', end='')
print()
print(f'O mais leve tem: {leve} kg. ', end='')
for peso in lista:
    if peso[1] == leve:
        print(f'[{peso[0]}] ', end='')