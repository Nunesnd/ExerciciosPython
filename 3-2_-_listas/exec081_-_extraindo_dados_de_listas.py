"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

print('+ '*30, end='+\n')
lista = []

while True:
    
    valor = int(input(f'Informe o valor da posição : '))
    
    lista.append(valor)
    
    cont = str(input('Deseja continuar[S/N]? '))
    
    if cont[0].upper() == 'N':
        print('Saindo do prog')
        break

print('- '*30, end='-\n')

print(f'Foram digitados {len(lista)}')

print(f'A lista ordenada é {sorted(lista)}')

if 5 in lista:
    print('Há o valor 5 na lista.')
else:
    print('Não encontramos o valor 5 na lista.')
    
print('+ '*30, end='+')