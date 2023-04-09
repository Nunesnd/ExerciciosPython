"""
Faça um prog que leia um número e mostre o seu fatorial
"""

num = int(input('Informe o número positivo inteiro: '))

fatorial = num

while num != 0:
    
    num=num-1
        
    fatorial = fatorial * num

print(f'Resultado do fatorial é {fatorial}')