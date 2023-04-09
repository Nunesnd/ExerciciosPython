"""
Fazer um prog que leia varios números inteiros. Perguntar se o usuário quer continuar ou não inserindo valores.
Mostrar a média dos valores, o número maior e o menor lidos.
"""

num = soma = maior = menor = 0
encerra = 'N'

while encerra == 'N':
    
    num = int(input('Número: '))
    
    if soma == 0:
        maior = menor = num
    
    if maior < num: 
        maior = num
    
    if menor > num:
        menor = num
        
    soma+=num
    
    fim = input("Deseja encerrar? [S/N] ")
    encerra = fim.upper()

print(f'Soma: {soma}\nMaior: {maior}\nMenor: {menor}\n')