"""
Leia uma frase qualquer e descubra se é um palíndromo, desconsidere os espaços
"""


texto = input("Escreva a frase: ")

arrumado = texto.replace(' ','')

#print(len(arrumado))

for c in range(0,len(arrumado)):

    #lendo da esquerda para a direita
    contEsq = c
    #print(arrumado[contEsq])

    # lendo da direita para a esquerda
    contDir = len(arrumado)
    #print(arrumado[(contDir-c)-1])

    if (arrumado[contEsq]) != (arrumado[(contDir-c)-1]):
        print('Não é palíndromo')
        break

    if (c==(len(arrumado)-1)):
        print("É um palíndromo")

