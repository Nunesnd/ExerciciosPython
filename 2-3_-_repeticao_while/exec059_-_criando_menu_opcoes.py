"""
Crie um pro que leia dois valores e mostre um menu na tela:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - sair do prog
"""

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

opcao = 0

while opcao != 5:
    opcao = int(input("Escolha uma opção:\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - sair do prog\n\n"))
    
    if opcao == 1:
        print(f"A soma é {num1+num2}.")
    if opcao == 2:
        print(f"A multiplicação é {num1*num2}.")
    if opcao == 3:
        if num1 > num2:
            print(f"O número maior é {num1}")
        elif num1 < num2:
            print(f'O número maior é {num2}')
        else:
            print('Os números são iguais.')
    if opcao == 4:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
    if opcao == 5:
        break
