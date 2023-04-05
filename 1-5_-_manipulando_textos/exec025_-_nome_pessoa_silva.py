"""
Faça um prog que leia o nome de uma pessoa e diga se tem ou não o nome silva
"""

nome = input("Informe o nome da pessoa: ")

nome_separado = nome.upper().split()

print("SILVA" in nome_separado)