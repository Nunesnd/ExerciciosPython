"""
Desenvolva um programa que pergunte a distância de uma viagem  em km.
Calcule o preço da passagem cobrando $0,50 por km de até 200km e R$0,45 para viagens mais longas
"""

dist = int(input("Qual a distância da viagem em km? "))

if dist <= 200:
    passagem = dist * 0.5
    print(f"O valor da passagem é R${passagem:.2f}")
else:
    passagem = dist * 0.45
    print(f"O valor da passagem é R${passagem:.2f}")