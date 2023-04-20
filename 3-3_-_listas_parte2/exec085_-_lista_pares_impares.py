"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
cont = 0
numPar = numImp = ''
numeros = list()

for c in range(0,7):    
    num = int(input(f"Digite o {c+1}º número: "))    
    numeros.append(num)

for cont in range(0,7):
    if sorted(numeros)[cont] % 2 == 0:
        n = str(sorted(numeros)[cont])
        numPar += n+" "
        
    elif sorted(numeros)[cont] % 2 != 0:
        n = str(sorted(numeros)[cont])
        numImp += n+" "

    
print('-='*30)    
print(f"Lista pares: {numPar}")
print(f"Lista impares: {numImp}")
print(f"Lista original: {numeros}")
print(f"Lista organizada: {sorted(numeros)}")