"""
Fala quem prog que receba o ano de nascimento de um jovem e diga
    se ele ainda vai se alistar
    se está na hora de se alistar
    se já passou da hora de se alistar

    o prog tem que informar também se falta muito tempo para se apresentar ou quanto tempo passou do prazo de apresentação

"""
from datetime import datetime, date

nasc = int(input("Informe o ano de nascimento: "))

ano_atual = date.today()

if (ano_atual.year - nasc) < 18:
    print(f'Ainda vai se alistar, faltam {18 - (ano_atual.year - nasc)} anos.')
elif (ano_atual.year - nasc) == 18:
    print('Está no ano de alistamento.')
elif (ano_atual.year - nasc) > 18:
    print(f'Já passou do tempo de se alistar, deveria ter ido à {(ano_atual.year - nasc) - 18} anos.')
print(f'Idade atual {ano_atual.year-nasc}')
