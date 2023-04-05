"""
Escreva um prog que leia um número inteiro e dê a opção, qual a base para converção
(binário, octal ou hexadecimal)
"""
import math

num = int(input("Informe o valor a converter: "))

opcao = input('Para qual opção você deseja converter? \nB - Binário\nO - Octal\nH - Hexadecimal\n')

if opcao.upper() == 'B':
    print(f'Número {num} em binário {bin(num)}')
    print("Binário")
elif opcao.upper() == 'O':
    print(f'Número {num} em binário {oct(num)}')
    print("Octal")
elif opcao.upper() == 'H':
    print(f'Número {num} em binário {hex(num)}')
    print("Hexadecimal")
else:
    print("Opção incorreta!")