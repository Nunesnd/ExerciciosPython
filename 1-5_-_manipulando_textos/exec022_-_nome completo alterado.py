"""
Faça um programa que leia o nome ocompleto de uma pessoa e mostre:
A) O nome com todos os caracteres em maiúsculos
B) O nome com todos os caracteres em minúsculos
C) Quantidade de letras sem considerar espaços
D) Quantas letras tem o primeiro nome
"""

frase = input("Informe uma frase: ")

print("O nome com todos os caracteres em maiúsculos")
print(frase.upper())
print()

print("O nome com todos os caracteres em minúsculos")
print(frase.lower())
print()

print("Quantidade de letras sem considerar espaços")
print(len(frase.replace(" ","")))
print()

print("Quantas letras tem o primeiro nome")
NomeFrase = frase.split()
print(len(NomeFrase[0]))
print()