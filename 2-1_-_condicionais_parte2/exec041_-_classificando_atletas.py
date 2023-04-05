"""
a confederaão de natação precisa de um programa que leia o ano de nascimento e classifique o atleta em categorias
    até 9 mirim
    até 14 infaltil
    até 19 júnior
    até 25 senior
    acima de 25 master
"""

from datetime import datetime, date

nasc = int(input("Informe o ano de nascimento: "))

ano_atual = date.today()

if (ano_atual.year - nasc) <= 9:
    print(f'Atleta mirim {(ano_atual.year - nasc)} anos.')
elif (ano_atual.year - nasc) <= 14:
    print(f'Atleta infantil {(ano_atual.year - nasc)} anos.')
elif (ano_atual.year - nasc) <= 19:
    print(f'Atleta júnior {(ano_atual.year - nasc)} anos.')
elif (ano_atual.year - nasc) <= 25:
    print(f'Atleta sênior {(ano_atual.year - nasc)} anos.')
elif (ano_atual.year - nasc) > 25:
    print(f'Atleta master {(ano_atual.year - nasc)} anos.')