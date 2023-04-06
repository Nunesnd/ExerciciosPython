"""
Nova versão do exec 009, faça uma nova tabuada com o número que o usuário escolher
"""

numero = int(input("Escolha a tabuada: "))

fim = int(input("Informe o termo final: "))

for c in range(0,fim+1):
    print(f'{numero} X {c} = {numero*c}')