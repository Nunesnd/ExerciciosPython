"""
Faça um programa que leia Nome, Idade e Sexo. No final mostre:

1 - Média de idade do grupo
2 - Nome do homem mais velho
3 - Quant mulheres tem menos de 20 anos
"""

quant = int(input('Pessoas a cadastrar: '))

nome = ''
nomeH = ''
idade = 0
iddH = 0
sexo = ''
contM = 0

for c in range(0,quant):
    print(f'----- Cadastro nº{c+1} -----')

    nome = input('Nome: ')
    idd = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    idade+=idd

    if sexo.upper() == 'M':
        if idd > iddH:
            iddH = idd
            nomeH = nome
    elif sexo.upper() == 'F':
        if idd <= 20:
            contM += 1

print(f'Média de idade é {idade/quant:.2f}.')
print(f'Homem mais velho é o Sr. {nomeH}, tem {iddH} anos.')
print(f'Total de mulhures com menos de 20 anos é de {contM}.')
