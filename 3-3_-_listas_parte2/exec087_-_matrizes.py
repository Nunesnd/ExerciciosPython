"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
par = terc = maior = 0
matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Informe valor para [{linha}], [{coluna}]: '))
        if (matriz[linha][coluna] % 2) == 0:
            par += matriz[linha][coluna]
        terc += matriz[linha][2]
        if linha == 0:
            maior = matriz[linha][1]
        if matriz[linha][1] > maior:
            maior = matriz[linha][1]
        
print(matriz)

print('#'*30)



for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print('')
    
print(f'Valores pares somados resultam em : {par}')
print(f'Valores da terceira coluna somados : {terc}')
print(f'Maior valor da segunda coluna : {maior}')