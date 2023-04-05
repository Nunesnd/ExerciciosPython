"""
Faça um prog que leia um número entre 0 e 9999 e mostre separadamente Unidade, Dezena, Centena e Milhar
"""

num = input("Informe um número: ")
print(f"Número informado foi: {num}")

print(f"Unidade: {format(num[3])}")
print(f"Dezena: {format(num[2])}")
print(f"Centena: {format(num[1])}")
print(f"Milhar: {format(num[0])}")
