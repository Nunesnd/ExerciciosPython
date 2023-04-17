"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

print('+ '*30, end='+\n')
lista = []
listaPar = []
listaImpar = []

while True:
    
    valor = int(input(f'Informe o valor da posição : '))
    
    lista.append(valor)
    
    cont = str(input('Deseja continuar[S/N]? '))
    
    if cont[0].upper() == 'N':
        print('Saindo do prog')
        break

cont = 0
lst = len(lista)
print('seguno while')

while cont < lst:
        
    if (lista[cont] % 2) == 0:
        print('entrou no if true')
        listaPar.append(lista[cont])
    else:        
        print('entrou no if false')
        listaImpar.append(lista[cont])
    
    cont += 1
    
print('- '*30, end='-\n')

print(f'A lista original é: {lista}')

print(f'A lista de números pares é: {listaPar}')

print(f'A lista de números ímpares é: {listaImpar}')
    
print('+ '*30, end='+')

