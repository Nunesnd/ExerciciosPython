"""
evoluindo o exec 61, faça o prog perguntar quantos termos deseja mostrar
"""
termo = int(input('Termo: '))
razao = int(input('Razão: '))
quant = int(input('Quantidade de termos: '))

n = 0 

while n < quant:

    termo=termo+razao
    print(f'Termo nº {n+1}: {termo}')
    n+=1