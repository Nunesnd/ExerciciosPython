"""
Faça um prog que leia o sexo de uma pessoa, mas só aceite valores 'M' e 'F'.
Caso errado, peça pra escrever novamente até acertar o valor
"""

sexo = ''

while sexo.upper() != ('M' or 'F'):
    
    sexo = input('Informe o sexo [M/F]: ')
    
    print('Informe o valor correto')

print('Obrigado!')