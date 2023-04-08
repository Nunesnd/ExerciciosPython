"""
leia o ano de nascimento de 7 pessoas e descubra quantas ainda não atingiram a maioridade e quantas já são maiores
"""

from datetime import date

maiores = 0
menores = 0

quant = int(input("Quantas pessoas serão analisadas? "))

dataHoje = date.today()

print(f'Ano atual {dataHoje.year}')

for c in range(0, quant):

    ano = int(input(f'Pessoa {c}: '))

    if (dataHoje.year - ano)>=18:
        maiores=maiores+1
    elif (dataHoje.year - ano)<18:
        menores=menores+1

print(f'Temos {maiores} maiores de idade enquanto {menores} menores')