"""
Faça um prog que leia a idade e sexo de várias pessoas.
A cada pessoa cadastrada pergunte se deseja continuar cadastrando mais. No fim mostre:
1) - Quantas pessoas tem mais de 18 anos
2) - Quantos homens foram cadastrados
3) - Quantas mulheres tem menos de 20 anos
"""

mais18 = homens = idade = sexo = mulheresMenor20 = 0

cont =''

while cont.upper() != 'N':
    idade = int(input("Informe idade: "))
    sexo = str(input('Informe o sexo [M/F]: '))
    
    while sexo.upper() != ('M' or 'F'):
        print('Informação incorreta.')
        sexo = str(input('Informe o sexo [M/F]: '))
    
    if idade < 18:
        mais18 += 1
    
    if sexo.strip().upper()[0] == 'M':
        homens += 1
        
    if sexo.strip().upper()[0] == 'F' and idade < 20 :
        mulheresMenor20 += 1
            
    cont = str(input('Continuar cadastrando [S/N]: '))

print('= = = = = = = = =')
print(f"Maiores de idade: {mais18}. \nHomens: {homens}. \nMulheres menores de 20: {mulheresMenor20}")