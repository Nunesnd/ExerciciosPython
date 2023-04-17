"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

cont = 0 

lista = []

quant = int(input('Quantos valores serão digitados? '))

while cont < quant:
    
    valor = int(input(f'Informe o valor da posição {cont}: '))
    
    if valor in lista:
        print('Valor já existente.')
    else:
        lista.append(valor)
        
    cont += 1

print(f'A lista digitada foi {lista}.')