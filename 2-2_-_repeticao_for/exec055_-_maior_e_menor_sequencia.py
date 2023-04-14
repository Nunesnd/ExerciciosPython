"""
leia o peso de cinco pessoas e descubra qual o mais pesado e o leve
"""

maior = 0
menor = 0

quant_numeros = int(input("Quantos números irá informar? "))

for c in range (0,quant_numeros):
    num = float(input(f'Informe o peso da pessao nº {c+1}º: '))
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Maior informado foi {maior}, enquanto o menor foi {menor}')